---
title: "Grouped But Not Following..."
topic_id: 4730
author: "Gorka"
date: 2017-01-21T17:11:41+00:00
last_activity: 2017-01-24T06:16:34+00:00
last_author: "Teron"
sticky: false
locked: false
post_count: 7
---

<div class="post" data-post-id="37981" data-author="Gorka" data-date="2017-01-21T17:11:41+00:00">

I could have just sent this to teker... but I think others need to know about this issue as well.

I was grouped with Zuzu, I had moves and I wasn't webbed but did not follow him...

---------------------------------------------------------------------------------------------------------------------

War massacres a temple guard to small fragments with his pierce.

War brutally massacres a temple guard with his pierce.

A temple guard hates your guts!

You can taste the impending victory!

You brutally massacre a temple guard with your slash.

A temple guard is dead! R.I.P.

You receive 153314 experience points as your share.

You gain 64762 bonus experience!

Total exp for kill is 580059.

----------

MOB : Negator Demon scorpion

AREA : The Caverns of Matterhorn

XP : 580059

LVL : 41

----------

|

recast

Your blood freezes as you hear a temple guard's death cry.

War gets the story of Molly Droit from the corpse of a temple guard that's on the ground.

War gets gold coins from the corpse of a temple guard that's on the ground.

War splits 12913 coins.  Your share is 2582 coins.

War reports 1736/1736 hp. Change: -140. Need: 0. Spells: aegis, greater fluidity.

<1244hp 175ma 365mv 625959735xp -10.4ac -%>

War yells 'BEAT YOU WITH A DEAD CAT!'

warcry BEAT YOU WITH A DEAD CAT!

<1244hp 176ma 367mv 625959735xp -10.4ac -%>

Zuzu -- 'target guard'

Targetting: guard

<1244hp 177ma 368mv 625959735xp -10.4ac -%>

Zuzu leaves east.

Songster leaves east.

Rose the peri leaves east.

<1244hp 177ma 368mv 625959735xp -10.4ac -%>

That didn't sound quite right...

<1244hp 179ma 370mv 625959735xp -10.4ac -%>

The 'petrified armor' spell on you is about to wear off.

<1244hp 184ma 376mv 625959735xp -10.4ac -%>

group

Group 'stuffs OPEN to ALL' is led by Zuzu and consists of:

  (Point)              War [Wa:9.40 1721hp 242ma 193mv] orange zircon | paradot       

  (Front)            Sochi [Ba:8.35 1138hp 136ma 378mv] sb pearl|gyt                  

 (Leader)             Zuzu [Cl:2.32  842hp 365ma 190mv] Rhodo|TJade                   

                  Songster [Ba:1.39  901hp 162ma 237mv] jacinth/jet moon knight       

 (Absent)            Gorka [Wa:6.39 1244hp 187ma 378mv] rcquartz/csapphire fire-demon 

<1244hp 187ma 378mv 625959735xp -10.4ac -%>

gt weird

You grouptell: 'weird'

<1244hp 190ma 382mv 625959735xp -10.4ac -%>

War yells 'BEAT YOU WITH A DEAD CAT!'

warcry BEAT YOU WITH A DEAD CAT!

<1244hp 190ma 383mv 625959735xp -10.4ac -%>

Songster -- 'gorka missing'

<1244hp 191ma 384mv 625959735xp -10.4ac -%>

That didn't sound quite right...

<1244hp 191ma 384mv 625959735xp -10.4ac -%>

Zuzu -- 'target guard'

Targetting: guard

<1244hp 192ma 384mv 625959735xp -10.4ac -%>

find war

track war

Tracks to War lead eastward.

e

track war

<1244hp 195ma 388mv 625959735xp -10.4ac -%>

Along a Bleak Hallway

   Twin sets of torches line either side of this long, desolate hallway.  

The darkness in the corridor is all-consuming, and prevents the light from 

the torches from penetrating further than a few feet.  Ritualistic chants 

echo through the marble corridor, followed closely by the hollow moans of 

the undead.  Although the corridor extends both east and west, nothing is 

visible in either direction beyond arms-length.

Exits: East  West  

<1244hp 196ma 388mv 625959735xp -10.4ac -%>

</div>

<div class="post" data-post-id="37985" data-author="*Idjit*" data-date="2017-01-22T06:55:38+00:00">

The same happened to Zuzu with Songster leading, same day different time.

In Irap near the squads of fire ants.. Group moved, I had 150 moves so I wasn't out of moves,

and wasn't webbed, but I didn't move.

Gorka may not have mentioned in the above post but the "You follow X." message was missing for him when that happened.  He talked about it shortly afterward in group, though.

--D

</div>

<div class="post" data-post-id="37986" data-author="Gorka" data-date="2017-01-22T08:53:24+00:00">

Just a stab in the dark... is it possible counters changed something?

My reasoning is, if counters can't count correctly or they get stuck in the wrong mode, that must mean the mud must lose my "grouped/solo" status at some point. If the mud does in fact lose that status that would also lead to me not following the group. So I'm thinking, it could be the same problem, but two symptoms.... just a thought.

</div>

<div class="post" data-post-id="37989" data-author="*juggleblood*" data-date="2017-01-22T14:31:07+00:00">

I have another hypothesis. 

Another bug / issue that has appeared recently (within a month or so?) is that combat is continuing after the mob dies, i.e. the mob will die and then get in another melee attack or even a special procedure.  My guess is that this is occasionally causing some players position flag to remain as 'fighting', instead of 'standing' and thus they are unable to follow the leader immediately following the fight.

Teker, if you would like me to explore this possibility, I can give a few people mudl objects that report the value of their position flag everytime leader leaves the room. Then if the bug occurs again, player would see "Fighting" when the leader leaves and it would confirm the hypothesis.

</div>

<div class="post" data-post-id="37990" data-author="Gorka" data-date="2017-01-22T15:07:51+00:00">

Something to add to JB's point... if you echo msdp.STATUS on a trigger line for R.I.P it often outputs "Fighting." I am unsure why MSDP seems lagged.

Furthermore, when fighting two mobs... and one has just died... the code seems confused about if you are fighting or not, until the next round of combat takes place with the second mob.

</div>

<div class="post" data-post-id="37991" data-author="*Breeze*" data-date="2017-01-22T19:37:56+00:00">

> **Gorka wrote:**
> Something to add to JB's point... if you echo msdp.STATUS on a trigger line for R.I.P it often outputs "Fighting." I am unsure why MSDP seems lagged.
> 
> 
> 
> Furthermore, when fighting two mobs... and one has just died... the code seems confused about if you are fighting or not, until the next round of combat takes place with the second mob.

makes perfect sense.

MSDP sends it info every X seconds, if something has changed.

to get 100% accurate MSDP we would have had to call the function which sends MSDP data  after each and every bit of code/action possible which would lag the game horribly.

i am pretty sure we experimented with that at one point.

as for mobs, you are only ever fighting one mob at a time.  in multiple mob fights, you fight one mob, the other mobs fight you. after you kill the first mob, then you start fighting the next mob.  so no code confusion there.

</div>

<div class="post" data-post-id="37994" data-author="Teron" data-date="2017-01-24T06:16:34+00:00">

Another theory was that it has something to do with the new skill checks, since it has appeared recently (since the last 1-2 reboots).

</div>
