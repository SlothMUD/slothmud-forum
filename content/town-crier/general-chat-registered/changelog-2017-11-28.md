---
title: "Changelog 2017-11-28"
topic_id: 4803
author: "*teker*"
date: 2017-11-28T15:48:43+00:00
last_activity: 2017-12-02T16:29:50+00:00
last_author: "*teker*"
sticky: false
locked: false
post_count: 4
---

<div class="post" data-post-id="38506" data-author="*teker*" data-date="2017-11-28T15:48:43+00:00" data-subject="Changelog 2017-11-28">

Today's boot popped items normally since the game had been running for a significant amount of time. It also popped additional items based on what was in game before the reboot. Hopefully this is the best of both worlds for everyone.

More work on cleaning up spells on bad arguments:

\- Mantra of the Ancient Tribes

\- Force Field

\- Lloyds Beacon

\- Greater Lloyds Beacon

\- Passage

\- There and Back Again

There was some incomplete code regarding the use of Lloyds and Passage at the same time. I've cleaned up the code to what I think the original intent was:

\- "Lesser" Lloyds can not be used at the same time as Passage or There and Back Again.

\- Passage and There and Back Again use the same variable to store data so setting one overwrites the other.

\- Greater Lloyds can be used at the same time as any of the other spells.

Mantra of the Ancient Tribes was draining 2x the listed mana - I have changed this to drain mana normally.

</div>

<div class="post" data-post-id="38507" data-author="Gorka" data-date="2017-11-28T21:46:30+00:00" data-subject="Re: Changelog 2017-11-28">

Could you explain how this works?

> <strong>Quote:</strong>
> It also popped additional items based on what was in game before the reboot.

</div>

<div class="post" data-post-id="38508" data-author="*teker*" data-date="2017-11-28T23:27:32+00:00" data-subject="Re: Changelog 2017-11-28">

At shutdown, we save a list of items that mobiles have popped.

At boot, if an item doesn't pop via normal rules, we check the saved list to see if the item is in there. If it is, there's an additional chance the item will pop. We see something in our logs like:

REPOP: a sea green spellbook (#8102) on a green-robed acolyte (#10409) in room #98358

REPOP: a short sword (#2904) on a firenewt guard (#2907) in room #2914

or even

REPOP: Specularem (#9807) on [Redacted] in room [Redacted]

REPOP: Macuahuitl (#69118) on [Redacted] in room [Redacted]

</div>

<div class="post" data-post-id="38516" data-author="*teker*" data-date="2017-12-02T16:29:50+00:00" data-subject="Re: Changelog 2017-11-28">

I've been told that passage and beacon we not exclusive previously so this morning's reboot should return it to its prior state.

Avatar supplications should be fixed also.

</div>
