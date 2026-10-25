---
title: "msdp with tinyfugue"
topic_id: 3981
author: "raincrab"
date: 2012-12-19T21:31:01+00:00
last_activity: 2012-12-19T22:33:36+00:00
last_author: "raincrab"
sticky: false
locked: false
post_count: 2
---

<div class="post" data-post-id="33850" data-author="raincrab" data-date="2012-12-19T21:31:01+00:00">

Using a copy of tf patched with msdp support, http://www.mudbytes.net/file-2875, you can access the msdp variables.  They are automatically updated, and you can grab the msdp variable change events as well.

First request them when connected (run the macro **/enablemsdp** or have it triggered to run when you enter the game):

```
/def enablemsdp = \
	/msdp REPORT =CHARACTER_NAME %; \
	/msdp REPORT =SERVER_ID %; \
	/msdp REPORT =SERVER_TIME %; \
	/msdp REPORT =SNIPPET_VERSION %; \
	/msdp REPORT =AFFECTS %; \
	/msdp REPORT =ALIGNMENT %; \
	/msdp REPORT =EXPERIENCE %; \
	/msdp REPORT =EXPERIENCE_MAX %; \
	/msdp REPORT =EXPERIENCE_TNL %; \
	/msdp REPORT =HEALTH %; \
	/msdp REPORT =HEALTH_MAX %; \
	/msdp REPORT =HEALTH_REGEN %; \
	/msdp REPORT =LEVEL %; \
	/msdp REPORT =LEVEL_SEC %; \
	/msdp REPORT =LEVEL_TER %; \
	/msdp REPORT =LEVEL_QUA %; \
	/msdp REPORT =LEVEL_QUI %; \
	/msdp REPORT =LEVEL_HEX %; \
	/msdp REPORT =LEVEL_SEP %; \
	/msdp REPORT =LEVEL_OCT %; \
	/msdp REPORT =LEVEL_AVA %; \
	/msdp REPORT =CITIZEN %; \
	/msdp REPORT =CLASS %; \
	/msdp REPORT =CLASS_SEC %; \
	/msdp REPORT =CLASS_TER %; \
	/msdp REPORT =CLASS_QUA %; \
	/msdp REPORT =CLASS_QUI %; \
	/msdp REPORT =CLASS_HEX %; \
	/msdp REPORT =CLASS_SEP %; \
	/msdp REPORT =CLASS_OCT %; \
	/msdp REPORT =CLASS_AVA %; \
	/msdp REPORT =MANA %; \
	/msdp REPORT =MANA_MAX %; \
	/msdp REPORT =MANA_REGEN %; \
	/msdp REPORT =BANK %; \
	/msdp REPORT =PRACTICE %; \
	/msdp REPORT =MONEY %; \
	/msdp REPORT =HONOR %; \
	/msdp REPORT =DRACHMA %; \
	/msdp REPORT =MOVEMENT %; \
	/msdp REPORT =MOVEMENT_MAX %; \
	/msdp REPORT =MOVEMENT_REGEN %; \
	/msdp REPORT =HITROLL %; \
	/msdp REPORT =DAMROLL %; \
	/msdp REPORT =AC %; \
	/msdp REPORT =STR %; \
	/msdp REPORT =INT %; \
	/msdp REPORT =WIS %; \
	/msdp REPORT =DEX %; \
	/msdp REPORT =CON %; \
	/msdp REPORT =STR_PERM %; \
	/msdp REPORT =INT_PERM %; \
	/msdp REPORT =WIS_PERM %; \
	/msdp REPORT =DEX_PERM %; \
	/msdp REPORT =CON_PERM %; \
	/msdp REPORT =OPPONENT_HEALTH %; \
	/msdp REPORT =OPPONENT_HEALTH_MAX %; \
	/msdp REPORT =OPPONENT_LEVEL %; \
	/msdp REPORT =OPPONENT_NAME %; \
	/msdp REPORT =TANK_HEALTH %; \
	/msdp REPORT =TANK_HEALTH_MAX %; \
	/msdp REPORT =TANK_LEVEL %; \
	/msdp REPORT =TANK_NAME %; \
	/msdp REPORT =AREA_NAME %; \
	/msdp REPORT =ROOM_EXITS %; \
	/msdp REPORT =ROOM_NAME %; \
	/msdp REPORT =ROOM_VNUM %; \
	/msdp REPORT =TERRAIN %; \
	/msdp REPORT =CONTINENT %; \
	/msdp REPORT =WORLD_TIME %; \
	/msdp REPORT =CLIENT_ID %; \
	/msdp REPORT =CLIENT_VERSION %; \
	/msdp REPORT =PLUGIN_ID %; \
	/msdp REPORT =ANSI_COLORS %; \
	/msdp REPORT =XTERM_256_COLORS %; \
	/msdp REPORT =UTF_8 %; \
	/msdp REPORT =SOUND %; \
	/msdp REPORT =MXP %; \
	/msdp REPORT =WEAPON_DAM %; \
	/msdp REPORT =STAB_DAM %; \
	/msdp REPORT =STAB_DAM_CAP %; \
	/msdp REPORT =UNDEAD_CONT %; \
	/msdp REPORT =UNDEAD_CONT_CAP %; \
	/msdp REPORT =SPELL_BONUS %; \
	/msdp REPORT =SPELL_BONUS_CAP %; \
	/msdp REPORT =HEAL_BONUS %; \
	/msdp REPORT =HEAL_BONUS_CAP %; \
	/msdp REPORT =CHARISMA %; \
	/msdp REPORT =CHARISMA_CAP %; \
	/msdp REPORT =FLAILDAM %; \
	/msdp REPORT =KICKDAM %; \
	/msdp REPORT =HAND_DAM %; \
	/msdp REPORT =HAND_DAM_CAP %; \
	/msdp REPORT =DAM_RED %; \
	/msdp REPORT =DAM_RED_CAP %; \
	/msdp REPORT =SEX %; \
	/msdp REPORT =GROUP_LEADER
```

Then access the variable names with the convention **MSDP__<varname>**. for example:

```
/def whoami = /echo i am %MSDP__CHARACTER_NAME
```

Hooking the events is a little different, as hooks are not used as they are for other events, instead a trigger is used:

```
/def -mglob -t"MSDP *" msdp_update = /echo achtung! %{*} was set
```

**BUGS**

Since there is no native array support in tf, list variables are named with the convention **MSDP__<listname>_<elementname>** which creates unaccessible variable names when <elementname> contains spaces; Spell names like "stone skin" for example are troublesome.

Direction variables are being set, (their value is zero), i.e. from BH inn north and south get set, after going south, east and west get set, going back north to the inn, all 4 direction variables remain set, as there is no mechanism unsetting the variables.

Also any variable returning -1 should be ignored.

If you're still having trouble, turn on debugging with **/set msdp_dbg 1** and it will spew all msdp variable changes to the world window.

</div>

<div class="post" data-post-id="33852" data-author="raincrab" data-date="2012-12-19T22:33:36+00:00">

a workaround for the exits, just use a trigger to regex them out

```
/def -mregexp -t"^Exits: (.+)  " = /set exits %P1 %; \
    /test north := regmatch("North", %exits) %; \
    /test south := regmatch("South", %exits) %; \
    /test east := regmatch("East", %exits) %; \
    /test west := regmatch("West", %exits) %; \
    /test up := regmatch("Up", %exits) %; \
    /test down := regmatch("Down", %exits)
```

</div>
