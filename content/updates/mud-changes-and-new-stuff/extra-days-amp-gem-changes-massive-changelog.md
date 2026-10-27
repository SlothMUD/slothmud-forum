---
title: "Extra days &amp; gem changes ( Massive changelog )"
topic_id: 3840
author: "*Splork*"
date: 2012-01-12T05:28:28+00:00
last_activity: 2012-01-12T05:28:28+00:00
last_author: "*Splork*"
sticky: false
locked: false
post_count: 1
---

<div class="post" data-post-id="33134" data-author="*Splork*" data-date="2012-01-12T05:28:28+00:00" data-subject="Extra days &amp;amp; gem changes ( Massive changelog )">

Massive Changelog

Breeze and I have been working for a few weeks on this one, 

and it is finally done.

\* The following new extra days will be combined with our world configs..

New World Configs

 \* Regen Increased on a specific Continent

 ( these regens are 12+ bonus on a specific continent, combines with World config MD\_REGEN and could make 20+ if both continent and world is triggered, and player is on that continent )

 \* Fast repop Increased on a specific Continent

 ( Increases zone resets on specific continent, combines with World config MD\_FASTREPOP and could only if zone reset time is still greater than 30 minutes using continent specific zone fastrepop )

 \* Increased Mob XP on a specific Continent

 ( about 25% if continent picked and mob on continent, combines with 

 MD\_EXP\_BONUS and could give about 35% total when combined and off lyme and on picked continent, if on lyme, no bonus given, just normal bonus from world config md\_exp\_bonus )

 \* No lost concentration on a specific Continent

 ( prevents spell disruption on specific continent )

 \* Group XP on a specific Continent

 ( This is done slightly different than our World wide config, groupexp. 

 This extra adds a flat 20-25 % bonus(about) to each player's share in the group. This does combine with world wide config groupexp and can make a pretty nice bonus off of Lyme )

 \* Mob eq pop on a specific Continent

 ( flat 10% bonus for each continent when triggered, does not combine 

 with MD\_MOBEQPOP )

 \* Fargate on a specific Continent

 ( Gates are allowed to a certain continent )

 The code is available for Lyme however this will be restricted for use for

 quests and special occasions. This addition is an attempt to get people 

 moving around the game and off of Lyme.

 A break down of what the configs look like are below, they will be rotated every few months so that the same continent configs are not combined with the same world configs every month. Hopefully the result from this code is that we see much more movement with our playerbase throughout the world.

1\) FASTREPOP\_BH \& WORLD\_FARGATE

2\) REGEN\_AH 

3\) NOLOSTC\_ISLAND \& WORLD\_REGEN

4\) GROUPEXP\_SS

5\) INCREASE\_MOB\_EXP\_BH

6\) MOBEQPOP\_AH \& WORLD INCREASE\_EXP

7\) FARGATE\_ISLAND 

8\) FASTREPOP\_SS \& WORLD\_MOBEQPOP

9\) REGEN\_BH \& WORLD\_GROUPEXP

10\) NOLOSTC\_AH 

11\) GROUPEXP\_ISLAND

12\) INCREASED\_MOB-EXP\_SS \& WORLD\_FARGATE

13\) MOBEQPOP\_BH \& WORLD\_NOCAP

14\) FARGATE\_AH

15\) FASTREPOP\_ISLAND \& WORLD\_NOLOSTCONC

16\) REGEN\_SS \& WORLD\_FASTREPOP

17\) NOLOSTC\_BH \& WORLD\_KILL\_HISTORY

18\) GROUPEXP\_AH 

19\) INCREASE\_MOB\_EXP\_ISLAND 

20\) MOBEQPOP\_SS \& WORLD\_NOCAP

21\) FARGATE\_BH

22\) FASTREPOP\_AH \& WORLD\_MOBEQPOP

23\) REGEN\_ISLAND \& WORLD\_GROUPEXP 

24\) NOLOSTC\_SS

25\) GROUPEXP\_BH \& WORLD\_REGEN

26\) INCREASE\_MOB\_EXP\_AH

27\) MOBEQPOP\_ISLAND \& WORLD\_FARGATE

28\) FARGATE\_SS \& WORLD\_INCREASES\_EXP

29\) WORLD GEM\_POP( all conts but lyme )

30 WORLD FASTREPOP

31\) WORLD KILL\_HISTORY

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

 The way gem's pop has been changed a bit.

 All gem's have been tiered into 3 groups. 

 High, Middle, Low (Previously there were 6 groups!)

 When you kill a monster that is eligible to pop a gem, the mud will calculate 

 your % chance to pop a gem.

This % is based on the following things..

 \* # of people in group

 \* size of the mob

 \* xp value of the mob

 \* if it is an epic mob or not

 \*\*\* This does not mean the bigger the mob, the better the poprate! \*\*\*

 \*\*\* This does not mean the bigger the mob, the better the poprate! \*\*\*

 \*\*\* This does not mean the bigger the mob, the better the poprate! \*\*\*

After the mud determines if a gem will pop, it will randomly

choose 1 of the 3 tiers, and randomly choose a gem from the tier.

All tiers are mostly balanced gem count wise, but each tier has a

% chance of being selected.

The Future...

 In the coming days/weeks, caps will be adjusted and some runes may be adjusted.

\*\*\*\* Please report any bugs via bugs command or email Splork@slothmud.org \*\*\*\*\*

</div>
