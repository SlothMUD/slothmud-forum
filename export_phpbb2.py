#!/usr/bin/env python3
"""
Export a PUBLIC phpBB forum to a Hugo content tree.

Safety model (fails closed):
  * Only forums that the GUESTS group (i.e. a logged-out visitor) can both
    list and read are exported. Password-protected forums, link forums, and
    forums beneath a hidden parent are skipped.
  * Only approved / visible posts and topics are exported. Soft-deleted posts
    and posts still in the moderation queue are skipped.
  * If the guest permissions can't be determined, the script aborts instead of
    exporting everything (unless you pass an explicit --forums allowlist).
  * Ancestor forums that guests can't see (possible with --forums or
    --exclude-forums) never have their real name or description written; they
    get a generic "Forum <id>" placeholder so the Hugo tree stays valid.

The output directory is WIPED before writing (only after the forum selection
and database queries have succeeded), so every run is a clean snapshot: topics
from forums that went private, or posts that were deleted, disappear from the
next export. Pass --no-clean to disable. The wipe refuses to run on dangerous
targets (/, your home dir, the current dir, the script dir, static/, anything
containing those, or a directory that looks like a Hugo site / git repo root).

Usage:
    # 1. See what the script thinks is public, then compare with the live
    #    forum while logged out:
    python export_phpbb.py --user U --database DB --list-forums

    # 2. Export (wipes ./content first):
    python export_phpbb.py --user U --database DB --out ./content --prefix phpbb_

    # Optional overrides:
    #   --forums 2,5,7          export ONLY these forum ids (guest ACL is still
    #                           evaluated for warnings, but not required)
    #   --exclude-forums 9,12   never export these, even if guests can see them
    #   --no-clean              don't delete existing contents of --out first

The DB password is read from --password, else $PHPBB_DB_PASSWORD, else prompted.
"""
import argparse
import getpass
import html
import itertools
import os
import re
import shutil
import sys
from collections import defaultdict
from datetime import datetime, timezone
from urllib.parse import quote

import pymysql

STATIC_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')

ANONYMOUS_USER_ID = 1  # phpBB's built-in guest user

# Files whose presence means "this directory is a site/repo root, not a content dir".
CLEAR_REFUSE_MARKERS = ('.git', 'hugo.toml', 'hugo.yaml', 'hugo.yml', 'hugo.json',
                        'config.toml', 'config.yaml', 'config.yml', 'go.mod')


class AclError(Exception):
    """Raised when guest permissions can't be determined."""


# ---------- Smilies ----------

# Where the smiley image files live in the Hugo site (static/images/smilies/)
# and the URL they are served from.
SMILEY_DIR = os.path.join(STATIC_DIR, 'images', 'smilies')
SMILEY_URL = '/images/smilies'

# phpBB's stock smilies, used only if the board's own smilies table can't be read.
DEFAULT_SMILIES = {
    ':D': 'icon_e_biggrin.svg', ':-D': 'icon_e_biggrin.svg', ':grin:': 'icon_e_biggrin.svg',
    ':)': 'icon_e_smile.svg', ':-)': 'icon_e_smile.svg', ':smile:': 'icon_e_smile.svg',
    ':(': 'icon_e_sad.svg', ':-(': 'icon_e_sad.svg', ':sad:': 'icon_e_sad.svg',
    ':o': 'icon_e_surprised.svg', ':-o': 'icon_e_surprised.svg', ':eek:': 'icon_eek.svg',
    ':shock:': 'icon_eek.svg', ':?': 'icon_e_confused.svg', ':-?': 'icon_e_confused.svg',
    ':???:': 'icon_e_confused.svg', '8)': 'icon_cool.svg', '8-)': 'icon_cool.svg',
    ':cool:': 'icon_cool.svg', ':lol:': 'icon_lol.svg', ':x': 'icon_mad.svg',
    ':-x': 'icon_mad.svg', ':mad:': 'icon_mad.svg', ':P': 'icon_razz.svg',
    ':-P': 'icon_razz.svg', ':razz:': 'icon_razz.svg', ':oops:': 'icon_redface.svg',
    ':cry:': 'icon_cry.svg', ':evil:': 'icon_evil.svg', ':twisted:': 'icon_twisted.svg',
    ':roll:': 'icon_rolleyes.svg', ';)': 'icon_e_wink.svg', ';-)': 'icon_e_wink.svg',
    ':wink:': 'icon_e_wink.svg', ':!:': 'icon_exclaim.svg', ':?:': 'icon_question.svg',
    ':idea:': 'icon_idea.svg', ':arrow:': 'icon_arrow.svg', ':|': 'icon_neutral.svg',
    ':-|': 'icon_neutral.svg', ':mrgreen:': 'icon_mrgreen.svg', ':geek:': 'icon_e_geek.svg',
    ':ugeek:': 'icon_e_ugeek.svg',
}

SMILIES = {}          # code -> (file, width, height)
SMILIES_LOWER = {}    # lower-cased code -> code
SMILIES_BY_FILE = {}  # file -> first code using it
_missing_smilies = set()


def load_smilies(cur, prefix):
    """Read code -> image from the board's own smilies table (falls back to the stock set)."""
    SMILIES.clear()
    SMILIES_LOWER.clear()
    SMILIES_BY_FILE.clear()
    rows = []
    try:
        cur.execute(f"SELECT code, smiley_url, smiley_width, smiley_height FROM {prefix}smilies")
        rows = cur.fetchall()
    except pymysql.MySQLError as e:
        print(f'warning: could not read {prefix}smilies ({e}); using the stock phpBB smilies.',
              file=sys.stderr)
    if rows:
        for r in rows:
            SMILIES[r['code']] = (r['smiley_url'], r['smiley_width'], r['smiley_height'])
    else:
        for code, fname in DEFAULT_SMILIES.items():
            SMILIES[code] = (fname, None, None)
    for code, (fname, _w, _h) in SMILIES.items():
        SMILIES_LOWER.setdefault(code.lower(), code)
        SMILIES_BY_FILE.setdefault(fname, code)
    print(f'Loaded {len(SMILIES)} smiley codes.', file=sys.stderr)


def _dim(v):
    try:
        v = int(v)
        return v if v > 0 else None
    except (TypeError, ValueError):
        return None


def _smiley_html(key):
    """HTML for a smiley (looked up by code, or by file name for legacy posts).
    If the image file isn't in static/images/smilies, the plain code is kept."""
    code = key
    entry = SMILIES.get(key)
    if entry is None and key.lower() in SMILIES_LOWER:
        code = SMILIES_LOWER[key.lower()]
        entry = SMILIES[code]
    if entry is None and key in SMILIES_BY_FILE:
        code = SMILIES_BY_FILE[code if code in SMILIES else key] # safe fallback
        entry = SMILIES.get(code)

    if entry is not None:
        raw_fname = os.path.basename(entry[0] or '')
        w, h = _dim(entry[1]), _dim(entry[2])
    else:
        raw_fname = key
        w, h = None, None

    base_name = os.path.splitext(raw_fname)[0]

    # Generate unique candidate base names (handling prefix toggles)
    bases = {base_name}
    if base_name.startswith('icon_e_'):
        bases.add('icon_' + base_name[7:])
    elif base_name.startswith('icon_'):
        bases.add('icon_e_' + base_name[5:])

    # Test combinations (.svg first, then .gif, across valid bases)
    fname = None
    target_path = None
    for b in bases:
        for ext in ['.svg', '.gif']:
            candidate = b + ext
            p = os.path.join(SMILEY_DIR, candidate)
            if os.path.isfile(p):
                fname = candidate
                target_path = p
                break
        if fname:
            break

    if not fname or not target_path:
        _missing_smilies.add(raw_fname or code)
        return _escape_md(code)

    size = f' width="{w}" height="{h}"' if w and h else ''
    alt = html.escape(code, quote=True)
    return (f'<img src="{SMILEY_URL}/{quote(fname)}" alt="{alt}" title="{alt}"'
            f'{size} class="smiley nozoom">')

# ---------- Literal-text escaping ----------
#
# phpBB shows post text literally; Markdown does not. Anything the author typed
# that Markdown would treat as syntax ("* item", "_x_", "1. x", "# x", "<tag>",
# "[a](b)" ...) is backslash-escaped, so it renders exactly as typed. A backslash
# before ASCII punctuation is always safe, so over-escaping is harmless.

_MD_ESC_RE = re.compile(r'([\\`*_~|<>&]|\](?=[(\[:]))')
_LEAD_NUM_RE = re.compile(r'(?m)^([ \t]*)(\d{1,9})([.)])(?=\s)')
_LEAD_MARK_RE = re.compile(r'(?m)^([ \t]*)([-+#=])')


def _escape_md(s):
    s = _MD_ESC_RE.sub(r'\\\1', s)
    s = _LEAD_NUM_RE.sub(r'\1\2\\\3', s)
    return _LEAD_MARK_RE.sub(r'\1\\\2', s)


# ---------- URL / BBCode conversion ----------

_POPUP_RE = re.compile(
    r"""^javascript:\s*PopupPic\(\s*['"]([^'"]+)['"]\s*\)$""", re.I
)
_BAD_SCHEME_RE = re.compile(r'^\s*(javascript|data|vbscript):', re.I)


def _normalize_url(url):
    url = url.strip()
    m = _POPUP_RE.match(url)
    if m:
        url = m.group(1).strip()
    if _BAD_SCHEME_RE.match(url):
        return '#'
    url = url.replace('\\', '/')
    url = re.sub(r'^(https?):/+', r'\1://', url, flags=re.I)
    if re.match(r'^https?://', url, re.I) or url.startswith('//'):
        return url
    if re.match(r'^[a-z0-9.-]+\.[a-z]{2,}/', url, re.I):
        return 'https://' + url
    if not url.startswith('/'):
        url = '/' + url
    return url


def _markdown_image(raw_url):
    url = _normalize_url(raw_url)
    if re.match(r'^(https?:)?//', url, re.I):
        return f'![]({_safe_dest(url)})'
    if url.startswith('/'):
        rel = url.lstrip('/')
        disk = os.path.join(STATIC_DIR, rel.replace('%20', ' '))
        if os.path.isfile(disk):
            return f'![]({_safe_dest(url)})'
    # Not a web URL and not a file we have: plain text, never a Markdown link.
    # (Theme link render hooks such as Blowfish's call resources.Get on
    # non-web destinations, which fails the build on paths like C:\\...)
    return _escape_md(f'(image: {url})')


def _safe_dest(url):
    """Make a URL safe as a Markdown link/image destination."""
    return (url.replace(' ', '%20').replace('(', '%28').replace(')', '%29')
               .replace('<', '%3C').replace('>', '%3E'))


def _indent_quote(text):
    return '\n'.join('> ' + line for line in text.strip().splitlines())


# Innermost [quote] only (no nested opening tag inside), so nesting resolves
# from the inside out. Handles [quote], [quote="Name"], and the phpBB 3.2 form
# [quote=Name post_id=1 time=2 user_id=3].
_QUOTE_RE = re.compile(
    r'\[quote(?:=(?:"([^"]*)"|([^\]\s]+))[^\]]*)?\]'
    r'((?:(?!\[quote[\]=]).)*?)\[/quote\]',
    re.S | re.I)


def _quote_repl(m):
    who = (m.group(1) or m.group(2) or '').strip()
    head = f'<strong>{_escape_md(who)} wrote:</strong>' if who else '<strong>Quote:</strong>'
    return f'\n\n> {head}\n{_indent_quote(m.group(3))}\n\n'


def _convert_quotes(text):
    prev = None
    while prev != text:
        prev = text
        text = _QUOTE_RE.sub(_quote_repl, text)
    return text


def _list_repl(m):
    ordered = bool(m.group(1))
    items = [i.strip() for i in re.split(r'\[\*\]', m.group(2)) if i.strip()]
    if ordered:
        body = '\n'.join(f'{n}. {i}' for n, i in enumerate(items, 1))
    else:
        body = '\n'.join('- ' + i for i in items)
    return f'\n\n{body}\n\n'


def _fence(code):
    code = code.strip('\n')
    longest = max((len(r) for r in re.findall(r'`+', code)), default=0)
    f = '`' * max(3, longest + 1)
    return f'\n\n{f}\n{code}\n{f}\n\n'


def _wrap_inline(tag):
    """[b]/[i] -> <strong>/<em>. Spaces around the content stay outside the tag
    (so "[i] text [/i]" can't become a stray "* text *"), and the tag is closed and
    reopened across blank lines so paragraphs stay well-formed."""
    def repl(m):
        inner = m.group(1)
        core = inner.strip()
        if not core:
            return inner
        lead = inner[:len(inner) - len(inner.lstrip())]
        trail = inner[len(inner.rstrip()):]
        core = re.sub(r'\n{2,}', f'</{tag}>\n\n<{tag}>', core)
        return f'{lead}<{tag}>{core}</{tag}>{trail}'
    return repl


# Only strip BBCode tags we know about, so legitimate bracketed text such as
# "[sic]" or "[1]" survives. Add custom BBCodes here if your board has them.
KNOWN_BBCODE = (r'(?:b|i|u|s|url|img|code|quote|color|size|list|attachment|flash|'
                r'email|font|align|center|left|right|sub|sup|youtube|spoiler|hide|'
                r'table|tr|td|th|h[1-6]|\*)')
# phpBB <= 3.1 BBCode tags carry a per-post uid: [b:3r4t5y], [/quote:3r4t5y],
# [quote:3r4t5y="Name"], [color=red:3r4t5y], [/list:u:3r4t5y], [*:3r4t5y],
# [/*:m:3r4t5y], [code:1:3r4t5y]. The post row's bbcode_uid normally matches, but
# merged / split / converted posts can carry a different one, so strip by shape.
_UID = r'[a-z0-9]{5,10}'
_BBUID_NAME_RE = re.compile(r'(\[/?' + KNOWN_BBCODE + r')(?::[a-z0-9])?:' + _UID + r'(?=[\]=])', re.I)
_BBUID_PARAM_RE = re.compile(
    r'(\[(?:color|size|list|font|align|quote)=[^\]]*?):' + _UID + r'(?=\])', re.I)


def _strip_bbcode_uids(text):
    text = _BBUID_NAME_RE.sub(r'\1', text)
    return _BBUID_PARAM_RE.sub(r'\1', text)


_BBTAG = r'\[/?' + KNOWN_BBCODE + r'(?:[= ][^\]]*)?\]'
_LEFTOVER_BBCODE_RE = re.compile(_BBTAG, re.I)

# Pieces of text that must NOT be escaped: stashed fragments, BBCode tags, bare URLs.
_NO_ESCAPE_RE = re.compile(
    r'(\x00(?:K|CODE)\d+\x00|' + _BBTAG + r'|\bhttps?://[^\s<>\[\]]+)', re.I)


def _escape_raw(text):
    parts = _NO_ESCAPE_RE.split(text)  # odd items are the protected pieces
    return ''.join(p if i % 2 else _escape_md(p) for i, p in enumerate(parts))


def _bb_img(m):
    return f'[img]{m.group(1)}[/img]'


# Legacy (phpBB <= 3.1) posts: HTML left in the text by the old parser.
LEGACY_RULES = [
    # smilies: <img src="{SMILIES_PATH}/icon_x.gif" alt=":x:" ... />
    (re.compile(r'<img\s+[^>]*?src\s*=\s*["\']\{SMILIES_PATH\}/([^"\']+)["\'][^>]*>',
                re.S | re.I),
        lambda m: '\x00SM' + m.group(1) + '\x00'),
    (re.compile(
        r'<img\s+[^>]*?src\s*=\s*["\']([^"\']+)["\'][^>]*>'
        r'<s>\[img\]</s>\1<e>\[/img\]</e></img>',
        re.S | re.I),
        _bb_img),
    (re.compile(r'<img\s+[^>]*?src\s*=\s*["\']([^"\']+)["\'][^>]*>', re.S | re.I),
        _bb_img),
    (re.compile(r'<br\s*/?>', re.I), '\n'),
    (re.compile(r'<!--.*?-->', re.S), ''),
    (re.compile(r'<a\s+[^>]*?href\s*=\s*["\']([^"\']+)["\'][^>]*>(.*?)</a>', re.S | re.I),
        lambda m: f'[url={m.group(1)}]{m.group(2)}[/url]'),
]

_CODE_RE = re.compile(r'\[code(?:=[^\]]*)?\](.*?)\[/code\]', re.S | re.I)
_LIST_RE = re.compile(r'\[list(=[^\]]*)?\](.*?)\[/list\]', re.S | re.I)

# ---- phpBB 3.2+ stores posts as s9e XML (<r>...</r> or <t>...</t>) ----
_XML_ROOT_RE = re.compile(r'^\s*<[rt](?:\s[^<>]*)?>')
_XML_AUTOLINK_RE = re.compile(r'<URL url="([^"]*)">((?:(?!<s>).)*?)</URL>', re.S)
_XML_IMG_RE = re.compile(r'<IMG\b[^>]*?\bsrc="([^"]*)"[^>]*>.*?</IMG>', re.S)
# element names may contain underscores (LINK_TEXT)
_XML_TAG_RE = re.compile(r'</?[A-Za-z][A-Za-z0-9_]*(?:\s[^<>]*)?/?>')
_SMILEY_MARK_RE = re.compile(r'\x00SM(.*?)\x00', re.S)


def _xml_to_bbcode(text):
    """
    Turn s9e XML into the original BBCode. The <s>/<e> elements carry the
    original BBCode markers, so removing the wrapper elements (and keeping
    their contents) restores the author's source text. Text inside XML is
    entity-escaped, so callers must html.unescape AFTER this runs.
    """
    text = re.sub(r'<br\s*/>', '\n', text)
    # Images: take the address from the element's own src attribute. Its children
    # can hold a nested <URL>/<LINK_TEXT> (an auto-linked image URL), which would
    # otherwise be mistaken for the address.
    text = _XML_IMG_RE.sub(lambda m: f'[img]{m.group(1)}[/img]', text)
    # Emoticons: mark them; they become <img> tags later (see _smiley_html).
    text = re.sub(r'<E>(.*?)</E>', lambda m: '\x00SM' + m.group(1) + '\x00', text, flags=re.S)
    text = _XML_AUTOLINK_RE.sub(r'[url=\1]\2[/url]', text)         # auto-linked URLs
    text = re.sub(r'</?[se]>', '', text)                           # keep BBCode markers
    text = _XML_TAG_RE.sub('', text)                               # drop remaining elements
    return text


# Belt and braces: every literal "<" is already escaped by _escape_raw, so these
# should never match; "(?<!\\)" skips the escaped ones.
_DANGEROUS_TAG_RE = re.compile(
    r'(?<!\\)<(/?\s*(?:script|iframe|object|embed|style|form|link|meta|base|svg|math)\b)', re.I)
_EVENT_HANDLER_TAG_RE = re.compile(r'(?<!\\)<(?=[^>]*\bon\w+\s*=)', re.I)


def bbcode_to_md(text, post_id=None, uid=''):
    text = (text or '').replace('\r\n', '\n').replace('\r', '\n')

    if _XML_ROOT_RE.match(text):
        text = _strip_bbcode_uids(html.unescape(_xml_to_bbcode(text)))
    else:
        # phpBB <= 3.1: BBCode tags carry a per-post uid, e.g. [b:3r4t5y]
        text = _strip_bbcode_uids(html.unescape(text))
        if uid:
            text = text.replace(':' + uid, '')
        for pat, repl in LEGACY_RULES:
            text = pat.sub(repl, text)
    text = text.replace('\xa0', ' ')

    # hook for attachment URL rewriting:
    # text = rewrite_attachments(text, post_id)

    # Fragments that must reach the output untouched (images, links, smilies).
    # They are swapped for placeholders now and restored at the very end.
    kept = []

    def keep(s):
        kept.append(s)
        return f'\x00K{len(kept) - 1}\x00'

    # Protect code blocks from every other rule (fenced code is literal text).
    codes = []

    def stash(m):
        codes.append(m.group(1))
        return f'\x00CODE{len(codes) - 1}\x00'

    text = _CODE_RE.sub(stash, text)

    # Smilies, images and links first: their URLs must not be escaped.
    text = _SMILEY_MARK_RE.sub(lambda m: keep(_smiley_html(m.group(1))), text)
    text = re.sub(r'\[img\](.*?)\[/img\]',
                  lambda m: keep(_markdown_image(m.group(1))), text, flags=re.S | re.I)
    text = re.sub(r'\[url\](.*?)\[/url\]',
                  lambda m: keep(m.group(1).strip().replace('<', '%3C').replace('>', '%3E')),
                  text, flags=re.S | re.I)

    def url_repl(m):
        dest = _normalize_url(m.group(1))
        label = m.group(2)
        if re.match(r'^(https?:)?//', dest, re.I):
            return keep('[') + (label if label.strip() else dest) + keep(f']({_safe_dest(dest)})')
        # Only web URLs become Markdown links. Local/relative destinations (old
        # C:\\... paths, /viewtopic.php?... etc.) are written as plain text.
        return f'{label} ({dest})'

    text = re.sub(r'\[url=(.*?)\](.*?)\[/url\]', url_repl, text, flags=re.S | re.I)

    # Everything left is text the author typed: make Markdown show it literally.
    text = _escape_raw(text)

    # Formatting BBCode.
    text = re.sub(r'\[b\](.*?)\[/b\]', _wrap_inline('strong'), text, flags=re.S | re.I)
    text = re.sub(r'\[i\](.*?)\[/i\]', _wrap_inline('em'), text, flags=re.S | re.I)
    text = re.sub(r'\[u\](.*?)\[/u\]', r'\1', text, flags=re.S | re.I)
    text = re.sub(r'\[color=.*?\](.*?)\[/color\]', r'\1', text, flags=re.S | re.I)
    text = re.sub(r'\[size=.*?\](.*?)\[/size\]', r'\1', text, flags=re.S | re.I)
    text = _convert_quotes(text)
    text = _LIST_RE.sub(_list_repl, text)
    text = _LEFTOVER_BBCODE_RE.sub('', text)

    text = _DANGEROUS_TAG_RE.sub(r'&lt;\1', text)
    text = _EVENT_HANDLER_TAG_RE.sub('&lt;', text)

    text = re.sub(r'\x00K(\d+)\x00', lambda m: kept[int(m.group(1))], text)
    text = re.sub(r'\x00CODE(\d+)\x00', lambda m: _fence(codes[int(m.group(1))]), text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    # Collapse multiple spaces (excluding newlines) into a single space
    text = re.sub(r'[ \t]{2,}', ' ', text)
    text = re.sub(r'\n[ \t]*\n[ \t]*\n+', '\n\n', text)
    return text.strip()


# ---------- Helpers ----------

def slugify(s, fallback):
    s = re.sub(r'[^a-z0-9]+', '-', (s or '').lower()).strip('-')
    return s[:80].strip('-') or fallback


def ts(epoch):
    if not epoch:
        return ''
    return datetime.fromtimestamp(int(epoch), tz=timezone.utc).isoformat()


def yaml_str(s):
    # newlines/control chars break front matter
    s = re.sub(r'[\x00-\x1f\x7f\x85\u2028\u2029]+', ' ', str(s))
    return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'


def write(path, body):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(body)


def has_column(cur, table, column):
    cur.execute(f"SHOW COLUMNS FROM {table} LIKE %s", (column,))
    return cur.fetchone() is not None


def parse_id_list(s):
    if not s:
        return set()
    try:
        return {int(x) for x in s.split(',') if x.strip()}
    except ValueError:
        sys.exit(f'error: expected a comma-separated list of integers, got {s!r}')


def clear_output_dir(out_root):
    """Delete everything inside out_root (but not out_root itself)."""
    target = os.path.realpath(out_root)
    protected = [os.sep, os.path.expanduser('~'), os.getcwd(),
                 os.path.dirname(os.path.abspath(__file__)), STATIC_DIR]
    for p in protected:
        rp = os.path.realpath(p)
        # refuse if target IS a protected path or CONTAINS one
        if rp == target or rp.startswith(target.rstrip(os.sep) + os.sep):
            sys.exit(f'error: refusing to clear {target!r}: it is, or contains, '
                     f'{rp!r}. Use a dedicated output directory.')
    if not os.path.exists(target):
        os.makedirs(target)
        return
    if not os.path.isdir(target):
        sys.exit(f'error: --out {target!r} exists and is not a directory')
    for marker in CLEAR_REFUSE_MARKERS:
        if os.path.exists(os.path.join(target, marker)):
            sys.exit(f'error: refusing to clear {target!r}: it contains {marker!r}, so it '
                     f'looks like a site or repo root rather than a content directory.')

    removed = 0
    for entry in os.scandir(target):
        if entry.is_dir(follow_symlinks=False):
            shutil.rmtree(entry.path)
        else:  # files and symlinks (never follow links)
            os.unlink(entry.path)
        removed += 1
    print(f'Cleared {removed} item(s) from {target}', file=sys.stderr)


# ---------- Visibility / permission checks ----------

def visibility_clauses(cur, prefix):
    """phpBB 3.2+ uses *_visibility = 1 (approved); 3.1 and earlier use *_approved = 1."""
    if has_column(cur, f'{prefix}posts', 'post_visibility'):
        post_vis = 'post_visibility = 1'
    elif has_column(cur, f'{prefix}posts', 'post_approved'):
        post_vis = 'post_approved = 1'
    else:
        sys.exit('error: posts table has neither post_visibility nor post_approved; '
                 'refusing to export without a visibility filter.')

    if has_column(cur, f'{prefix}topics', 'topic_visibility'):
        topic_vis = 'topic_visibility = 1'
    elif has_column(cur, f'{prefix}topics', 'topic_approved'):
        topic_vis = 'topic_approved = 1'
    else:
        sys.exit('error: topics table has neither topic_visibility nor topic_approved; '
                 'refusing to export without a visibility filter.')
    return post_vis, topic_vis


def guest_forum_permissions(cur, prefix):
    """
    Return {forum_id: {'f_list': bool, 'f_read': bool}} for what a logged-out
    visitor is allowed. Evaluates the GUESTS group plus any per-user ACL on the
    anonymous user. NEVER (0) beats YES (1); no row means not granted.
    Raises AclError if the data needed can't be found (callers fail closed).
    """
    wanted = ('f_list', 'f_read')

    cur.execute(f"SELECT group_id FROM {prefix}groups WHERE group_name = 'GUESTS'")
    row = cur.fetchone()
    if not row:
        raise AclError("couldn't find the GUESTS group")
    guests_gid = row['group_id']

    cur.execute(f"SELECT auth_option_id, auth_option FROM {prefix}acl_options "
                f"WHERE auth_option IN ('f_list', 'f_read')")
    opt_by_id = {r['auth_option_id']: r['auth_option'] for r in cur.fetchall()}
    if set(opt_by_id.values()) != set(wanted):
        raise AclError('f_list / f_read options not found in acl_options')

    cur.execute(f"SELECT role_id, auth_option_id, auth_setting FROM {prefix}acl_roles_data "
                f"WHERE auth_option_id IN ({','.join(['%s'] * len(opt_by_id))})",
                tuple(opt_by_id))
    role_data = defaultdict(dict)  # role_id -> {option_name: setting}
    for r in cur.fetchall():
        role_data[r['role_id']][opt_by_id[r['auth_option_id']]] = r['auth_setting']

    settings = defaultdict(lambda: defaultdict(list))  # fid -> option -> [settings]

    def load(table, key_col, key_val):
        cur.execute(f"SELECT forum_id, auth_option_id, auth_role_id, auth_setting "
                    f"FROM {prefix}{table} WHERE {key_col} = %s AND forum_id > 0",
                    (key_val,))
        for r in cur.fetchall():
            fid = r['forum_id']
            if r['auth_role_id']:
                for opt, setting in role_data.get(r['auth_role_id'], {}).items():
                    settings[fid][opt].append(setting)
            elif r['auth_option_id'] in opt_by_id:
                settings[fid][opt_by_id[r['auth_option_id']]].append(r['auth_setting'])

    load('acl_groups', 'group_id', guests_gid)
    load('acl_users', 'user_id', ANONYMOUS_USER_ID)

    perms = {}
    for fid, per_opt in settings.items():
        perms[fid] = {}
        for opt in wanted:
            vals = per_opt.get(opt, [])
            perms[fid][opt] = bool(vals) and 0 not in vals and 1 in vals
    return perms


def classify_forums(forums, perms):
    """Return {forum_id: (is_public, reason)}, requiring every ancestor to be public too."""
    memo = {}

    def check(fid, seen=()):
        if fid in memo:
            return memo[fid]
        f = forums[fid]
        if fid in seen:
            res = (False, 'parent loop')
        elif f['forum_type'] == 2:
            res = (False, 'link forum (no content)')
        elif f['forum_password']:
            res = (False, 'password protected')
        else:
            p = perms.get(fid, {})
            if not p.get('f_list'):
                res = (False, 'guests lack f_list')
            elif f['forum_type'] == 1 and not p.get('f_read'):
                res = (False, 'guests lack f_read')
            else:
                res = (True, 'guests can see')
                parent = f['parent_id']
                if parent and parent in forums:
                    ok, why = check(parent, seen + (fid,))
                    if not ok:
                        res = (False, f'ancestor hidden ({forums[parent]["forum_name"]}: {why})')
        memo[fid] = res
        return res

    return {fid: check(fid) for fid in forums}


# ---------- Main export ----------

def load_forums(cur, prefix):
    cur.execute(f"SELECT forum_id, parent_id, forum_name, forum_type, left_id, "
                f"forum_desc, forum_desc_uid, forum_password "
                f"FROM {prefix}forums ORDER BY parent_id, left_id")
    return {r['forum_id']: r for r in cur.fetchall()}


def list_forums(forums, status):
    print(f'{"id":>5}  {"parent":>6}  {"type":<8}  {"public":<6}  name  [reason]')
    for fid, f in sorted(forums.items(), key=lambda kv: (kv[1]['left_id'] or 0)):
        ok, why = status[fid]
        ftype = {0: 'category', 1: 'forum', 2: 'link'}.get(f['forum_type'], str(f['forum_type']))
        print(f'{fid:>5}  {f["parent_id"]:>6}  {ftype:<8}  {"YES" if ok else "no":<6}  '
              f'{f["forum_name"]}  [{why}]')


def export(out_root, prefix, db, forum_allow, forum_exclude, clean=True):
    cur = db.cursor(pymysql.cursors.DictCursor)
    post_vis, topic_vis = visibility_clauses(cur, prefix)
    forums = load_forums(cur, prefix)
    load_smilies(cur, prefix)

    # ---- guest ACL: required in default mode, advisory with --forums ----
    try:
        status = classify_forums(forums, guest_forum_permissions(cur, prefix))
    except AclError as e:
        if not forum_allow:
            sys.exit(f'error: {e}; can\'t determine public forums. '
                     f'Use --forums to give an explicit allowlist.')
        print(f'warning: could not evaluate guest permissions ({e}); '
              f'trusting --forums as given.', file=sys.stderr)
        status = None

    # ---- decide which forums are exported ----
    if forum_allow:
        unknown = forum_allow - set(forums)
        if unknown:
            sys.exit(f'error: --forums contains unknown forum ids: {sorted(unknown)}')
        if status:
            for fid in sorted(forum_allow):
                if not status[fid][0]:
                    print(f'warning: forum {fid} ({forums[fid]["forum_name"]}) is in --forums but '
                          f'looks non-public to guests ({status[fid][1]}); exporting anyway.',
                          file=sys.stderr)
        included = set(forum_allow)
    else:
        included = {fid for fid, (ok, _) in status.items() if ok}

    included -= forum_exclude
    included = {fid for fid in included if forums[fid]['forum_type'] != 2}

    print('Skipping forums:', file=sys.stderr)
    for fid, f in forums.items():
        if fid not in included:
            why = 'excluded by --exclude-forums' if fid in forum_exclude else \
                  ('not in --forums allowlist' if forum_allow else status[fid][1])
            print(f'  {fid:>5}  {f["forum_name"]}  [{why}]', file=sys.stderr)

    if not included:
        sys.exit('error: no forums selected for export.')

    # Ancestors of included forums need an _index.md so Hugo's tree is valid.
    index_ids = set(included)
    for fid in included:
        p = forums[fid]['parent_id']
        while p and p in forums and p not in index_ids:
            index_ids.add(p)
            p = forums[p]['parent_id']

    def is_known_public(fid):
        return status is not None and status[fid][0] and fid not in forum_exclude

    def forum_label(fid):
        """Real name for exported / known-public forums; generic for hidden ancestors."""
        if fid in included or is_known_public(fid):
            return forums[fid]['forum_name']
        return f'Forum {fid}'

    # ---- load metadata (visible content in included forums only) ----
    id_ph = ','.join(['%s'] * len(included))
    id_args = tuple(included)

    cur.execute(f"SELECT user_id, username FROM {prefix}users")
    users = {r['user_id']: r['username'] for r in cur.fetchall()}

    cur.execute(f"SELECT topic_id, forum_id, topic_title, topic_poster, "
                f"topic_first_poster_name, topic_time, topic_type, topic_status "
                f"FROM {prefix}topics "
                f"WHERE forum_id IN ({id_ph}) AND {topic_vis} AND topic_status <> 2 "
                f"ORDER BY topic_id", id_args)
    topics_by_id = {t['topic_id']: t for t in cur.fetchall()}

    def display_name(poster_id, fallback_name):
        if poster_id != ANONYMOUS_USER_ID and poster_id in users:
            return users[poster_id]
        return fallback_name or 'guest'

    # ---- forum -> content path mapping (unique among siblings) ----
    forum_path = {}
    used_slugs = defaultdict(set)  # parent path -> slugs already taken

    def path_for(fid, seen=()):
        if fid in forum_path:
            return forum_path[fid]
        f = forums[fid]
        parent = f['parent_id']
        if parent in index_ids and parent != fid and parent not in seen:
            parent_path = path_for(parent, seen + (fid,))
        else:
            parent_path = ''  # top level (also breaks parent loops)
        slug = slugify(forum_label(fid), f'forum-{fid}')
        if slug in used_slugs[parent_path]:
            slug = f'{slug}-{fid}'
        used_slugs[parent_path].add(slug)
        p = os.path.join(parent_path, slug) if parent_path else slug
        forum_path[fid] = p
        return p

    for fid in sorted(index_ids):
        path_for(fid)

    # Names a topic file may not take in each directory: Hugo's index.md (makes
    # a leaf bundle) and the directory names of child forums.
    topic_names = defaultdict(lambda: {'index'})
    for fid in index_ids:
        p = forums[fid]['parent_id']
        if p in index_ids and p != fid:
            topic_names[forum_path[p]].add(os.path.basename(forum_path[fid]))

    # ---- start the streaming posts query, THEN wipe the output dir ----
    # Streaming keeps memory flat on big boards. Executing first means a failing
    # query aborts before anything is deleted.
    post_cur = db.cursor(pymysql.cursors.SSDictCursor)
    try:
        post_cur.execute(
            f"SELECT post_id, topic_id, poster_id, post_username, post_time, "
            f"post_text, bbcode_uid "
            f"FROM {prefix}posts "
            f"WHERE forum_id IN ({id_ph}) AND {post_vis} "
            f"ORDER BY topic_id, post_time, post_id", id_args)

        if clean:
            clear_output_dir(out_root)

        # ---- forum _index.md files ----
        for fid in sorted(index_ids):
            f = forums[fid]
            has_children = any(forums[c]['parent_id'] == fid for c in index_ids if c != fid)
            is_category = has_children or f['forum_type'] == 0
            # Only describe forums that were actually selected for export.
            desc = bbcode_to_md(f['forum_desc'], uid=f['forum_desc_uid'] or '') \
                if fid in included else ''
            body = (
                '---\n'
                f'title: {yaml_str(forum_label(fid))}\n'
                f'forum_id: {fid}\n'
                f'layout: forum\n'
                f'type: forum\n'
                f'is_category: {"true" if is_category else "false"}\n'
                f'weight: {f["left_id"] or 0}\n'
                '---\n\n'
                f'{desc}\n'
            )
            write(os.path.join(out_root, forum_path[fid], '_index.md'), body)

        # ---- topic files (posts arrive grouped by topic_id) ----
        n_topics = n_posts = 0
        for tid, group in itertools.groupby(post_cur, key=lambda p: p['topic_id']):
            t = topics_by_id.get(tid)
            if t is None:
                continue  # topic hidden / moved / outside the export
            posts = list(group)
            if not posts:
                continue

            # Derived from visible posts only, so hidden-post timing doesn't leak.
            last_post = max(posts, key=lambda p: (p['post_time'] or 0, p['post_id']))
            last = last_post['post_time'] or 0
            last_author = display_name(last_post['poster_id'], last_post['post_username'])
            sticky = bool(t['topic_type'] and t['topic_type'] > 0)
            locked = t['topic_status'] == 1
            author = display_name(t['topic_poster'], t['topic_first_poster_name'])

            parts = [
                '---',
                f'title: {yaml_str(t["topic_title"])}',
                f'topic_id: {t["topic_id"]}',
                f'author: {yaml_str(author)}',
                f'date: {ts(t["topic_time"])}',
                f'last_activity: {ts(last)}',
                f'last_author: {yaml_str(last_author)}',
                f'sticky: {"true" if sticky else "false"}',
                f'locked: {"true" if locked else "false"}',
                f'post_count: {len(posts)}',
                '---',
                '',
            ]
            for p in posts:
                p_author = display_name(p['poster_id'], p['post_username'])
                md = bbcode_to_md(p['post_text'], p['post_id'], uid=p['bbcode_uid'] or '')
                parts.append(
                    f'<div class="post" data-post-id="{p["post_id"]}" '
                    f'data-author="{html.escape(p_author, quote=True)}" '
                    f'data-date="{ts(p["post_time"])}">\n\n'
                    f'{md}\n\n</div>\n'
                )

            rel = forum_path[t['forum_id']]
            used = topic_names[rel]
            base = slugify(t['topic_title'], f'topic-{t["topic_id"]}')
            name = base
            if name in used:
                name = f'{base}-{t["topic_id"]}'  # stable, unlike -2/-3 counters
                while name in used:
                    name += '-x'
            used.add(name)
            write(os.path.join(out_root, rel, name + '.md'), '\n'.join(parts))
            n_topics += 1
            n_posts += len(posts)
    finally:
        post_cur.close()

    if _missing_smilies:
        print(f'warning: smiley image(s) not found in {SMILEY_DIR}, left as text: '
              f'{sorted(_missing_smilies)}', file=sys.stderr)
    print(f'Exported {len(index_ids)} forum index pages ({len(included)} with content), '
          f'{n_topics} topics, {n_posts} posts.', file=sys.stderr)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--out', help='output content directory (required unless --list-forums)')
    ap.add_argument('--prefix', default='phpbb_')
    ap.add_argument('--host', default='localhost')
    ap.add_argument('--port', type=int, default=3306)
    ap.add_argument('--user', required=True)
    ap.add_argument('--password', default=None,
                    help='DB password (else $PHPBB_DB_PASSWORD, else prompt)')
    ap.add_argument('--database', required=True)
    ap.add_argument('--forums', help='comma-separated forum ids to export (explicit allowlist)')
    ap.add_argument('--exclude-forums', help='comma-separated forum ids to never export')
    ap.add_argument('--no-clean', action='store_true',
                    help="don't delete the existing contents of --out before exporting")
    ap.add_argument('--list-forums', action='store_true',
                    help='print each forum and whether guests can see it, then exit')
    args = ap.parse_args()

    if not re.fullmatch(r'\w*', args.prefix):
        sys.exit('error: --prefix may only contain letters, digits and underscores')
    if not args.list_forums and not args.out:
        sys.exit('error: --out is required')

    password = args.password or os.environ.get('PHPBB_DB_PASSWORD') or getpass.getpass('DB password: ')

    db = pymysql.connect(host=args.host, port=args.port, user=args.user, password=password,
                         database=args.database, charset='utf8mb4')
    try:
        if args.list_forums:
            cur = db.cursor(pymysql.cursors.DictCursor)
            forums = load_forums(cur, args.prefix)
            try:
                perms = guest_forum_permissions(cur, args.prefix)
            except AclError as e:
                sys.exit(f'error: {e}; can\'t determine public forums.')
            list_forums(forums, classify_forums(forums, perms))
        else:
            export(args.out, args.prefix, db,
                   parse_id_list(args.forums), parse_id_list(args.exclude_forums),
                   clean=not args.no_clean)
    finally:
        db.close()


if __name__ == '__main__':
    main()