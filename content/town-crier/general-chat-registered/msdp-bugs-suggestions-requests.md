---
title: "MSDP: bugs, suggestions, requests."
topic_id: 4131
author: "Tuck"
date: 2013-10-11T20:25:50+00:00
last_activity: 2014-07-18T09:21:34+00:00
last_author: "Filk"
sticky: false
locked: false
post_count: 10
---

<div class="post" data-post-id="34487" data-author="Tuck" data-date="2013-10-11T20:25:50+00:00">

Yo,

we are looking for msdp fixed/advances. Let's collect them and bug imms to implement it. Thanks for your opinions.

First of all, msdp help file is not up to date, as i can see. Please update it.

**Bugs**:

1a. WEAPON_DAM is frozen, i have it 19, not matter what i use or naked, we also need WEAPON_DAM_CAP.

1b. WORLD_TIME is permanent 0.

1c. My SPELL_BONUS_CAP is 137, if i get moar spellbonus than cap, it's reset to negative value (i reported it long ago).

1d. Msdp do not work at all while shifted.

1e. ROOM_EXITS separated by strange symbols, please fix it

**Suggestions/needs**:

2a. We deadly need msdp variable for SPELLSAVES/SPELLSAVES_CAP.

2b. Var that display active spells on players, including buffs/debuffs.

2c. Var with value of room type: inside/outside. There is var TERRAIN, but it's no use, as i can see.

2d. Var to display AC_CAP.

2e. Vars to display str/int/wis/dex/con CAPs.

2f. Maybe implement Var to display group members names/their hps/their mana/their mvs (submited by Vasu). List, separated by commas will be cool.

MSDP var list (**please let me know if it is incomplete**):

```
CHARACTER_NAME
SERVER_ID
ALIGNMENT
EXPERIENCE
HEALTH
HEALTH_MAX
LEVEL
LEVEL_SEC
LEVEL_TER
LEVEL_QUA
LEVEL_QUI
LEVEL_HEX
LEVEL_SEP
LEVEL_OCT
LEVEL_AVA
CITIZEN
CLASS
CLASS_SEC
CLASS_TER
CLASS_QUA
CLASS_QUI
CLASS_HEX
CLASS_SEP
CLASS_OCT
CLASS_AVA
MANA
MANA_MAX
BANK
MONEY
HONOR
DRACHMA
MOVEMENT
MOVEMENT_MAX
HITROLL
DAMROLL
AC
STR
INT
WIS
DEX
CON
STR_PERM
INT_PERM
WIS_PERM
DEX_PERM
CON_PERM
OPPONENT_HEALTH
OPPONENT_HEALTH_MAX
OPPONENT_LEVEL
OPPONENT_NAME
TANK_HEALTH
TANK_HEALTH_MAX
TANK_LEVEL
TANK_NAME
AREA_NAME
ROOM_NAME
ROOM_VNUM
TERRAIN
CONTINENT
WORLD_TIME
WEAPON_DAM
STAB_DAM
STAB_DAM_CAP
UNDEAD_CONT
UNDEAD_CONT_CAP
SPELL_BONUS
SPELL_BONUS_CAP
HEAL_BONUS
HEAL_BONUS_CAP
CHARISMA
CHARISMA_CAP
HAND_DAM
HAND_DAM_CAP
DAM_RED
DAM_RED_CAP
SEX
GROUP_LEADER
ROOM_EXITS
```

Thanks, 

your tukster.

</div>

<div class="post" data-post-id="34488" data-author="Tuck" data-date="2013-10-11T21:32:25+00:00">

Thanks Akaya for pointing me to @MSDP.ROOM_EXITS unofficial variable :)

</div>

<div class="post" data-post-id="34490" data-author="*Splork*" data-date="2013-10-12T00:50:52+00:00">

The room_exits odd character is actually not a bug but we should probably try to replace it with a comma or something else.

</div>

<div class="post" data-post-id="34491" data-author="Tuck" data-date="2013-10-12T01:21:48+00:00">

> ***Splork* wrote:**
> The room_exits odd character is actually not a bug but we should probably try to replace it with a comma or something else.

i wrote parser for it already :P

what about other things, rickster?

</div>

<div class="post" data-post-id="34492" data-author="*Splork*" data-date="2013-10-12T01:25:50+00:00">

Ill look into the other things.

</div>

<div class="post" data-post-id="34493" data-author="Tuck" data-date="2013-10-12T10:45:34+00:00">

thank you, thank you, thank you

</div>

<div class="post" data-post-id="34507" data-author="dimiric" data-date="2013-10-23T15:23:35+00:00">

I second these requests!  ;-)  as you can see from my other post.

Ones I'd like to see:

- better spell Affects variable

- wholist (with titles, levels, etc)

- wholist to show local people and locations

- inventory

- worn.all, worn.<slot> for equipment

- saving throws?

I'd also like to get something working with the mapper in mudlet, but I haven't had time to even start researching this so I have no idea if it exists already or is impossible.

</div>

<div class="post" data-post-id="34514" data-author="Tuck" data-date="2013-10-25T15:36:52+00:00">

> **dimiric wrote:**
> I second these requests!  ;-)  as you can see from my other post.
> 
> 
> 
> Ones I'd like to see:
> 
> - better spell Affects variable
> 
> - wholist (with titles, levels, etc)
> 
> - wholist to show local people and locations
> 
> - inventory
> 
> - worn.all, worn.<slot> for equipment
> 
> - saving throws?
> 
> 
> 
> I'd also like to get something working with the mapper in mudlet, but I haven't had time to even start researching this so I have no idea if it exists already or is impossible.

While i'm ok with most of your request, i don't see why do we need wholist, inventory, and worn.all in MSDP vars.

You can write parser for your client for this things easily.

</div>

<div class="post" data-post-id="34516" data-author="Dragoth" data-date="2013-10-26T08:09:29+00:00">

If possible, please add msdp var for Aerial Servant hp %, very helpful for clerics.

</div>

<div class="post" data-post-id="35393" data-author="Filk" data-date="2014-07-18T09:21:34+00:00">

Bump.

Any news on group list as msdp value? Even with same syntax that "affects" value have for simplicity.

Would be very good additional for group healers and leaders. I'd love to see basic list with name, hp and mana.

It is posible to request group command each turn for that purpose, and even gag it after, but thats quite spammy anyway.

Also, there is kinda bug with Stats_perm values while in form. Some of them(at least checked for dex), shows value increased by 1. Though no items +stats could raise it to that max. Or better fix forms with that values  :lol: 

Stats like weapon_dam,spell_bonus etc kinda not working with forms as well.

</div>
