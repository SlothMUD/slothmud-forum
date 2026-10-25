---
title: "Spell warnings"
topic_id: 1539
author: "mudder"
date: 2005-11-08T12:53:13+00:00
last_activity: 2005-11-08T13:23:08+00:00
last_author: "mudder"
sticky: false
locked: false
post_count: 3
---

<div class="post" data-post-id="9416" data-author="mudder" data-date="2005-11-08T12:53:13+00:00">

I'm trying to write triggers scripts codes aliases etc 

One I've written is a coundown timer for spells about to wear off, based on:

Trigger:

The '<spellname>' spell on you is about to wear off.

Action:

#set ticktime = 60;

#delay ticktick 1 60 #set ticktime = ticktime -1

ticktime being a variable shown on my clients status bar along with the spellname.

I've noticed however that sometimes spells just wear off without the warning prompt.

Does anyone know why this happens? is it a bug or a feature or random luck or level based?

</div>

<div class="post" data-post-id="9417" data-author="madmax" data-date="2005-11-08T13:10:13+00:00">

The spell failing message is a product of the "spellcraft" skill.

Since it is learned only to 85%, it has a 15% chance to not give you any

message at all.

Madmax

</div>

<div class="post" data-post-id="9418" data-author="mudder" data-date="2005-11-08T13:23:08+00:00">

thanks .... that makes sense :)

</div>
