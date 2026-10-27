---
title: "Changelog 2017-01-10"
topic_id: 4725
author: "*teker*"
date: 2017-01-10T15:39:56+00:00
last_activity: 2017-01-27T15:36:51+00:00
last_author: "*teker*"
sticky: false
locked: false
post_count: 4
---

<div class="post" data-post-id="37957" data-author="*teker*" data-date="2017-01-10T15:39:56+00:00" data-subject="Changelog 2017-01-10">

I believe I have banished the demon that was periodically blocking recall scrolls.

The T1 -\> T2 upgrade should be in place.

I've added a line to the counters command to show whether it thinks you're in solo mode or group mode. Hopefully someone can figure out how to manipulate it into the wrong mode.

Most of the work I did in this reboot was blocking remort exploits. The following skills were modified:

double attack

triple attack

quad attack

backstab

double stab

excruciating blow

sleight

squirm

bash

trip

kick

circlestab

apply poison

tactics

counterattack

tumbling defense

stalk

deathgrip

wraithtouch

flurry

stun

improved stun

strike

dodge

kensai

presage

prediction

deathtouch

sixth sense

kenning

equanimity

berserk

entrench

feign death

frenzy

deathblow

toss

warcry

stealth

broadside

stomp

bodyslam

study

parry

There are probably other exploits I missed but these were the obvious ones.

</div>

<div class="post" data-post-id="37979" data-author="*teker*" data-date="2017-01-19T00:18:15+00:00" data-subject="Re: Changelog 2017-01-10">

This morning's reboot added some tracing so we can try to get to the bottom of the lag that's been going on. It appears to be in the combat code somewhere. The next reboot will add a lot more tracing to narrow it down further.

The boar form lost its ability to frenzy with the rebirth-nerf code - it should be fixed now.

I made the changes to fortune should prevent mobs from having 1hp and will prevent them from phase-dooring when sitting idle.

</div>

<div class="post" data-post-id="37995" data-author="*teker*" data-date="2017-01-25T16:02:10+00:00" data-subject="Re: Changelog 2017-01-10">

I added more tracing in the reboot this morning to try to further isolate the lag. It appears to be related to combat and more specifically when mobs die. Hopefully this set of debugging will show us exactly where the lag is coming from.

</div>

<div class="post" data-post-id="37999" data-author="*teker*" data-date="2017-01-27T15:36:51+00:00" data-subject="Re: Changelog 2017-01-10">

We believe that Breeze has pinpointed the major source of lag and that it has been fixed. We've added more tracing to be sure.

</div>
