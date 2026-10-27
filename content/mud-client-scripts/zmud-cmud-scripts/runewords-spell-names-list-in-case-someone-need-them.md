---
title: "Runewords / Spell names list in case someone need them."
topic_id: 3704
author: "Tuck"
date: 2011-04-08T20:52:47+00:00
last_activity: 2011-04-13T20:18:14+00:00
last_author: "Tuck"
sticky: false
locked: false
post_count: 3
---

<div class="post" data-post-id="32560" data-author="Tuck" data-date="2011-04-08T20:52:47+00:00" data-subject="Runewords / Spell names list in case someone need them.">

Here is array of 160 spellnames and runewords. Might be used not in just cmud, just decode easy xml format.

Update: 190 spells for now. Example trigger to read on cast, decrypt, and display attached.

<strong>Update2: 207 spells for now. All decrypted. Guess, there is no more spells in Sloth. Even blizzard decoded.</strong>

Trigger pattern is: 

```
Trigger pattern is: ^(*) utters the words, '(*)'$

Trigger body:
$spelltoconvert=%2
#loop %numitems(@converspellarray) {
 $spelljumblekey=%dbkey(@converspellarray,%i)
 $spellnamevalue=%db(@converspellarray,%dbkey(@converspellarray,%i))
 #if ($spelltoconvert = $spelljumblekey OR $spelltoconvert = $spellnamevalue) {
 #gagspace
 #show %ansi(green)%1%ansi(reset)%if(%len(%1)<20,%repeat(".",@wraplength-%len(%1))) casts '%ansi(magenta)$spellnamevalue%ansi(reset)' ~($spelljumblekey~)
 #BREAK
 }
}
```

</div>

<div class="post" data-post-id="32561" data-author="*Breeze*" data-date="2011-04-09T10:16:54+00:00" data-subject="Re: Runewords / Spell names list in case someone need them.">

try now Tuk

</div>

<div class="post" data-post-id="32562" data-author="Tuck" data-date="2011-04-13T20:18:14+00:00" data-subject="Re: Runewords / Spell names list in case someone need them.">

Thanks Benq!

</div>
