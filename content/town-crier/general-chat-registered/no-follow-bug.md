---
title: "No Follow Bug"
topic_id: 4972
author: "Gorka"
date: 2020-05-13T18:41:37+00:00
last_activity: 2020-07-01T14:21:05+00:00
last_author: "Gorka"
sticky: false
locked: false
post_count: 2
---

<div class="post" data-post-id="39482" data-author="Gorka" data-date="2020-05-13T18:41:37+00:00">

Players are VERY OFTEN not following the leader in groups. It has happened in the past, but it seems to have come back in the past couple of months... to the point where we can't group anymore without it happening to someone, or multiple people throughout the course of a group.

<1078hp 651ma 355mv -11.1ac The Lower Planes - Minauros 4642130212xp -%>

Stun reports 1519/1559 hp. Change: -197. Need: 40. Spells: glowing, greater fluidity.

<1078hp 651ma 355mv -11.1ac The Lower Planes - Minauros 4642130212xp -%>

Guinex splits 29798 coins.  Your share is 2292 coins.

<1078hp 651ma 355mv -11.1ac The Lower Planes - Minauros 4642130212xp -%>

Stun yells 'BOLLE SNYLLE GRYF BYLLE?!!?'

warcry BOLLE SNYLLE GRYF BYLLE?!!?

<1078hp 652ma 356mv -11.1ac The Lower Planes - Minauros 4642130212xp -%>

Stun leaves west.

Guinex leaves west.

Xxx leaves west.

Skyle leaves west.

Knifey leaves west.

Insomnia leaves west.

Usually the message would be something like this...

<1078hp 683ma 308mv -11.1ac Mount 'An Mystica 4725733356xp -%>

Stun leaves south.

Guinex leaves south.

Xxx leaves south.

Skyle leaves south.

You follow Guinex.

I've been trying to figure out why it happens, my suspicion is that somehow in some cases the player.position variable is not correct for the player to follow.

</div>

<div class="post" data-post-id="39511" data-author="Gorka" data-date="2020-07-01T14:21:05+00:00">

This bug is still occurring...

It occurs to the person who gets the kill shot on a mob, if the leader leaves the room quickly after death.

My theory is the player who gets the kill shot, does not have their status updated from "FIGHTING" quick enough before the leader leaves the room, and so in some cases that player is left behind. It appears to be timing dependent.

Could a coder force the killers position to not be "FIGHTING" when a mob dies so that player will follow the leader. I don't understand why, but the status update appears to happen to the killer last, or not at the same time as everyone else, allowing them a brief window where a leader can leave them behind.

</div>
