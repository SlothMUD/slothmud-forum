---
title: "Simulacrum"
topic_id: 4711
author: "*teker*"
date: 2016-12-19T23:35:13+00:00
last_activity: 2016-12-21T23:13:36+00:00
last_author: "*Splork*"
sticky: false
locked: false
post_count: 8
---

<div class="post" data-post-id="37852" data-author="*teker*" data-date="2016-12-19T23:35:13+00:00" data-subject="Simulacrum">

So we've had 2 crashes in the last 2 weeks that were different players fireballing their own simulacrum. I've tried to repro on the test server by creating one and then killing it over and over without a repro. What do you guys use the simulacrum for? Something is going on during its lifetime that is causing the game to crash when it dies.

</div>

<div class="post" data-post-id="37853" data-author="*juggleblood*" data-date="2016-12-20T20:17:44+00:00" data-subject="Re: Simulacrum">

Taron makes simulacra of himself to raise as his children and he fireballs them when they disappoint him.

</div>

<div class="post" data-post-id="37855" data-author="Teron" data-date="2016-12-21T02:59:28+00:00" data-subject="Re: Simulacrum">

This should work <strong>on a test server</strong>:

cast 'simulacrum';

\#2 cast 'dispel magic' teker;

cast 'familiar' teker;

cast 'fireball' teker

Also test it without it being a familiar. Fireballing non-familairs was safe at least a few weeks ago.

</div>

<div class="post" data-post-id="37856" data-author="Gorka" data-date="2016-12-21T08:37:17+00:00" data-subject="Re: Simulacrum">

Rumor has it they were a partially implemented project then abandoned for some reason. It did provide a new spellbook that Shyla had to get for all the newbies... <img src="/images/smilies/icon_e_smile.svg" alt=":)" title=":)" width="15" height="15" class="smiley nozoom"> To my mind, something that is a copy of something, creates possible in game exploits... and possibly null pointers... 

The crier suggests they were implemented by Splork 11 years ago. 

http://www.slothmud.org/forum/viewtopic.php?f=26&t=1015&p=5451&hilit=simulacrum#p5451

Anyone else know a use for them?... besides asexual reproduction and abuse at the hands of Taron? <img src="/images/smilies/icon_lol.svg" alt=":lol:" title=":lol:" width="15" height="15" class="smiley nozoom">

I wonder if Taron also draws pictures of himself and then burns them? <img src="/images/smilies/icon_twisted.svg" alt=":twisted:" title=":twisted:" width="15" height="15" class="smiley nozoom">

</div>

<div class="post" data-post-id="37857" data-author="Teron" data-date="2016-12-21T10:10:04+00:00" data-subject="Re: Simulacrum">

Interesting, I've thought about having laser tag games here, it'd be fun!

How finished are the arena and the mechanics?

</div>

<div class="post" data-post-id="37860" data-author="*juggleblood*" data-date="2016-12-21T13:43:16+00:00" data-subject="Re: Simulacrum">

I think it has something to do with the fact that simulacrum upon creation is mastered to caster, then you are familiaring it and dispelling it, removing master. Maybe there is some code that is called on simulacrum death that expects to find master(%c) and doesn't because it's been nulled out by familiar/dispel.

</div>

<div class="post" data-post-id="37864" data-author="Josiah" data-date="2016-12-21T18:26:13+00:00" data-subject="Re: Simulacrum">

That's amusing, Taron you use fireball on your 'self' too? Guess both us warrior types think alike.

I'll refrain from any more 'self' mutilation until we hear that the spell is fixed.

</div>

<div class="post" data-post-id="37865" data-author="*Splork*" data-date="2016-12-21T23:13:36+00:00" data-subject="Re: Simulacrum">

> <strong>Quote:</strong>
> Rumor has it they were a partially implemented project then abandoned for some reason.

Nah, it wasn't abandoned and was used quite a few times actually. It was quite fun to play and also create a Sloth styled Lazer Tag game...

At one time simulacrum could also be used to attract aggressive mobs away from a player but I believe that was removed...

> <strong>Quote:</strong>
> creates possible in game exploits... and possibly null pointers...

This could be said of just about everything we add to the game <img src="/images/smilies/icon_lol.svg" alt=":lol:" title=":lol:" width="15" height="15" class="smiley nozoom">

</div>
