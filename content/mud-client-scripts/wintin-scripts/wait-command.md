---
title: "#wait Command"
topic_id: 2168
author: "Rizik"
date: 2006-11-11T21:53:55+00:00
last_activity: 2006-11-12T01:53:02+00:00
last_author: "Briar"
sticky: false
locked: false
post_count: 3
---

<div class="post" data-post-id="15110" data-author="Rizik" data-date="2006-11-11T21:53:55+00:00" data-subject="#wait Command">

I'm having some trouble using the #wait command. Rather, it doesn't seem to be working.

I tried:

\#wait {5};#showme 5 seconds elapsed.

and (had to try)

\#wait {5000};#showme 5000 miliseconds elapsed.

But neither worked- the messages showed up immediately.

What is wrong?

</div>

<div class="post" data-post-id="15112" data-author="Briar" data-date="2006-11-12T01:47:42+00:00" data-subject="">

; is a seperator, so u're infact inputting 2 commands

it should be #wait {5} {#showme 5 seconds has lapsed}

</div>

<div class="post" data-post-id="15113" data-author="Briar" data-date="2006-11-12T01:53:02+00:00" data-subject="">

my fault....what i typed was wrong

anyways why yours doesn't work is prob because all # commands are executed immediately.

u could try this, might work

\#alias xxx {#showme 5 seconds has lapsed}

\#wait {5};xxx

</div>
