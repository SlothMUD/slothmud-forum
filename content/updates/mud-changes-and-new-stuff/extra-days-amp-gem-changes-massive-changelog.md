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

* The following new extra days will be combined with our world configs..

New World Configs

    * Regen Increased on a specific Continent

     ( these regens are 12+ bonus on a specific continent, combines with World  config MD_REGEN and could make 20+ if both continent and world is  triggered, and player is on that continent )

   * Fast repop Increased on a specific Continent

     ( Increases zone resets on specific continent, combines with World config   MD_FASTREPOP and could only if zone reset time is still greater than  30 minutes using continent specific zone fastrepop )

   * Increased Mob XP on a specific Continent

     ( about 25% if continent picked and mob on continent, combines with 

       MD_EXP_BONUS and could give about 35% total when combined and off lyme     and on   picked continent, if on lyme, no bonus given, just normal bonus from world config md_exp_bonus )

   * No lost concentration on a specific Continent

     ( prevents spell disruption on specific continent )

   * Group XP on a specific Continent

     ( This is done slightly different than our World wide config, groupexp. 

       This extra adds a flat 20-25 % bonus(about) to each player's share in the group.  This does combine with world wide config groupexp and can make a pretty nice bonus off of Lyme )

   * Mob eq pop on a specific Continent

     ( flat 10% bonus for each continent when triggered, does not combine 

       with MD_MOBEQPOP )

   * Fargate on a specific Continent

     ( Gates are allowed to a certain continent )

    The code is available for Lyme however this will be restricted for use for

 quests and special occasions. This addition is an attempt to get people 

 moving around the game and off of Lyme.

  

    A break down of what the configs look like are below, they will be rotated every few months so that the same continent configs are not combined with the same world configs every month. Hopefully the result from this code is that we see much more movement with our playerbase throughout the world.

1)    FASTREPOP_BH      &           WORLD_FARGATE

2)    REGEN_AH 

3)    NOLOSTC_ISLAND    &          WORLD_REGEN

4)    GROUPEXP_SS

5)    INCREASE_MOB_EXP_BH

6)    MOBEQPOP_AH          &          WORLD INCREASE_EXP

7)    FARGATE_ISLAND       

8)    FASTREPOP_SS           &        WORLD_MOBEQPOP

9)    REGEN_BH                    &      WORLD_GROUPEXP

10)   NOLOSTC_AH           

11)   GROUPEXP_ISLAND

12)   INCREASED_MOB-EXP_SS       &              WORLD_FARGATE

13)   MOBEQPOP_BH                   &           WORLD_NOCAP

14)   FARGATE_AH

15)   FASTREPOP_ISLAND           &           WORLD_NOLOSTCONC

16)   REGEN_SS                    &               WORLD_FASTREPOP

17)   NOLOSTC_BH              &               WORLD_KILL_HISTORY

18)   GROUPEXP_AH           

19)   INCREASE_MOB_EXP_ISLAND 

20)   MOBEQPOP_SS              &                WORLD_NOCAP

21)   FARGATE_BH

22)   FASTREPOP_AH              &                WORLD_MOBEQPOP

23)   REGEN_ISLAND                &               WORLD_GROUPEXP 

24)   NOLOSTC_SS

25)   GROUPEXP_BH                  &              WORLD_REGEN

26)   INCREASE_MOB_EXP_AH

27)   MOBEQPOP_ISLAND           &              WORLD_FARGATE

28)   FARGATE_SS                    &              WORLD_INCREASES_EXP

29)   WORLD GEM_POP( all conts but lyme )

30    WORLD FASTREPOP

31)   WORLD KILL_HISTORY

*****************************************************************************

 The way gem's pop has been changed a bit.

 All gem's have been tiered into 3 groups.  

 High, Middle, Low (Previously there were 6 groups!)

 When you kill a monster that is eligible to pop a gem, the mud will calculate 

 your % chance to pop a gem.

This % is based on the following things..

 * # of people in group

 * size of the mob

 * xp value of the mob

 * if it is an epic mob or not

 *** This does not mean the bigger the mob, the better the poprate! ***

 *** This does not mean the bigger the mob, the better the poprate! ***

 *** This does not mean the bigger the mob, the better the poprate! ***

After the mud determines if a gem will pop, it will randomly

choose 1 of the 3 tiers, and randomly choose a gem from the tier.

All tiers are mostly balanced gem count wise, but each tier has a

% chance of being selected.

The Future...

  In the coming days/weeks, caps will be adjusted and some runes may be adjusted.

**** Please report any bugs via bugs command or email Splork@slothmud.org *****

</div>
