---
title: "Assisting mobs"
topic_id: 3588
author: "*Isabo*"
date: 2010-11-27T04:18:34+00:00
last_activity: 2010-11-27T04:18:34+00:00
last_author: "*Isabo*"
sticky: false
locked: false
post_count: 1
---

<div class="post" data-post-id="32101" data-author="*Isabo*" data-date="2010-11-27T04:18:34+00:00" data-subject="Assisting mobs">

Greetings, mortals.

There have been for quite a while an annoying bug related to mob assisting other mobs.  Game was not correctly setting the assisting mob to be fighting, so it was showing on look as not fighting, remembering people (and attacking) over and over, etc.  Think we finally got it :

**Before :**

<5501rm 0wz 0sv>

You magically create a giant spiked lizard!

<5501rm 0wz 0sv>

You magically create a giant spiked lizard!

<5501rm 0wz 0sv>The jaguar arrives from the west.

<5501rm 0wz 0sv>

A giant spiked lizard hates your guts!

You hit a giant spiked lizard extremely hard.

<5501rm 0wz 0sv>You deal a massive blow to one of a giant spiked lizard's vital 

organs.

You brutally massacre a giant spiked lizard with your hit.

A giant spiked lizard misses you with his beat. <- 14 attacks, mob have 7 per

A giant spiked lizard misses you with his beat.    round, so both are attacking.

A giant spiked lizard misses you with his beat.

A giant spiked lizard misses you with his beat.

A giant spiked lizard misses you with his beat.

A giant spiked lizard misses you with his beat.

A giant spiked lizard misses you with his bite.

A giant spiked lizard misses you with his beat.

A giant spiked lizard misses you with his beat.

A giant spiked lizard misses you with his beat.

A giant spiked lizard misses you with his beat.

A giant spiked lizard misses you with his beat.

A giant spiked lizard misses you with his beat.

A giant spiked lizard misses you with his bite.

You hit a giant spiked lizard extremely hard.

You massacre a giant spiked lizard to small fragments with your hit.

You miss a giant spiked lizard with your hit.

<5501rm 0wz 0sv>

The Foot of the Great Tree

   You are at the base of the trunk of an immense tree, at least twenty

feet in diameter.  The trunk is covered with vines, mosses and kudzu,

which you could probably climb.  Ancient roots stretch out across the

leaf-covered forest floor.

   The dim sunlight filtering down through the leaves shows a path

running east and west.

Exits: East  West  Up  

A giant spiked lizard is here, fighting  YOU!

A giant spiked lizard wanders around aimlessly. <- But this one do not show it.

<5501rm 0wz 0sv>

**After the fix :**

<5727rm 0wz 0sv>

You magically create a giant spiked lizard!

<5727rm 0wz 0sv>

You magically create a giant spiked lizard!

<5727rm 0wz 0sv>

Edge of the Jungle

   The wide trail disappears into a thick, noisy jungle to the west.  You

can see some huge trees deep inside of it.  The raucous noises of birds

and animals pour forth from the jungle, which evidently teems with life.

The trail gets larger to the east.

Exits: East  West  

A large warning sign stands next to the entrance to the jungle.

A giant spiked lizard wanders around aimlessly.

A giant spiked lizard wanders around aimlessly.

<5727rm 0wz 0sv>

A giant spiked lizard hates your guts!

You massacre a giant spiked lizard to small fragments with your hit.

<5727rm 0wz 0sv>You hit a giant spiked lizard extremely hard.

A giant spiked lizard misses you with his beat.

A giant spiked lizard misses you with his beat.

A giant spiked lizard misses you with his beat.

A giant spiked lizard misses you with his beat.

A giant spiked lizard misses you with his beat.

A giant spiked lizard misses you with his beat.

A giant spiked lizard misses you with his bite.

You massacre a giant spiked lizard to small fragments with your hit.

You massacre a giant spiked lizard to small fragments with your hit.

You hit a giant spiked lizard extremely hard.

A giant spiked lizard misses you with his beat. <- Second mob join fight.

<5727rm 0wz 0sv>

Edge of the Jungle

   The wide trail disappears into a thick, noisy jungle to the west.  You

can see some huge trees deep inside of it.  The raucous noises of birds

and animals pour forth from the jungle, which evidently teems with life.

The trail gets larger to the east.

Exits: East  West  

A large warning sign stands next to the entrance to the jungle.

A giant spiked lizard is here, fighting  YOU! <- And voila, both are fighting

A giant spiked lizard is here, fighting  YOU!

<5727rm 0wz 0sv

This bug has been there a lot of time and we tried to fix it several times withouth any luck.  Also, we have tested the fix for several hours, but it could have some colateral effect that we didnt see.  For those reasons, I would like to ask you guys to keep an eye on assisting mobs and report any odd things that you see.

Thanks Nobody and Taron for reporting.

Fix will be available on crash/reboot (after someone recompiles the code).

Best regards.

</div>
