---
title: "Perfect storm"
topic_id: 4639
author: "Yasik"
date: 2016-05-21T06:46:25+00:00
last_activity: 2016-05-21T06:46:25+00:00
last_author: "Yasik"
sticky: false
locked: false
post_count: 1
---

<div class="post" data-post-id="36939" data-author="Yasik" data-date="2016-05-21T06:46:25+00:00">

2 days ago there was a power outage in my home.

I was editing some triggers in my MUSH client and about to save the changes.

I pressed Ctrl+S to save, power went off. Then, after it restored, the client could not load world file (settings, all triggers, aliases, timers, everything).

Looking in world file itself (XML format) shows its completely empty, but still has correct size (661 kb, its normal).

But is empty: FAR manager viewer (F3) shows nothing, Notepad++ displays "NUL" characters.

I tried chkdsk, several undelete software - nothing helped.

Last backup dated Feb 14, 2014 - did it manually; looking inside shows its about for little Ozzy to leave VK.

So I guess the power went off precisely **in exact millisecond** in between world file was opened for writing and actually wrote from memory to disk. Murphy's Law worked out in best way possible.

Any hints on how to restore the content?

</div>
