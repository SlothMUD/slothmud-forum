---
title: "Mudlet 3.0.0 Beta (Native MSDP support)"
topic_id: 4394
author: "*Splork*"
date: 2014-10-06T14:23:36+00:00
last_activity: 2016-07-01T07:45:18+00:00
last_author: "Akaya"
sticky: false
locked: false
post_count: 6
---

<div class="post" data-post-id="35444" data-author="*Splork*" data-date="2014-10-06T14:23:36+00:00" data-subject="Mudlet 3.0.0 Beta (Native MSDP support)">

A new version of Mudlet has  been released. This is the version we have been waiting for because it contains full support for MSDP. No more hacks using ATCP or parsing data, 

For those with working MSDP scripts, if you switch to MSDP from ATCP, you will need to adjust your scripts a bit. 

For more information see http://www.mudlet.org/

Splork

</div>

<div class="post" data-post-id="35445" data-author="*Splork*" data-date="2014-10-06T15:21:27+00:00" data-subject="Re: Mudlet 3.0.0 Beta (Native MSDP support) Variable Window">

One of new additions is a variable window. In this example you can see the MSDP variable registering as they are received.

Pretty simple stuff:

lua sendMSDP("REPORT", "ROOM_EXITS")    will request room_exits variable

lua msdp        will show the results

 ROOM_EXITS = {

    South = "O",

    Up = "O",

    West = "O",

    East = "O",

    North = "O"

  },

O stands for open.

</div>

<div class="post" data-post-id="35446" data-author="Akaya" data-date="2014-10-06T15:50:45+00:00" data-subject="Re: Mudlet 3.0.0 Beta (Native MSDP support)">

Here's a snippet of what I use to request all msdp variables from Sloth...

```
function initialise_msdp()
  local vars = {
    "SERVER_ID", 
    "WORLD_TIME", 
    "CHARACTER_NAME",
    "HEALTH",
    "HEALTH_MAX",
    "MANA",
    "MANA_MAX",
    "MOVEMENT",
    "MOVEMENT_MAX",
    "AREA_NAME",
    "ROOM_NAME",
    "ROOM_VNUM",
    "AC",
    "HONOR",
    "CONTINENT",
    "LEVEL",
    "CLASS",
    "DRACHMA",
    "ALIGNMENT",
    "EXPERIENCE",
    "MONEY",
    "STR",
    "CON",
    "DEX",
    "WIS",
    "INT",
    "STR_PERM",
    "CON_PERM",
    "DEX_PERM",
    "WIS_PERM",
    "INT_PERM",
    "WEAPON_DAM",
    "SPELL_BONUS_CAP",
    "HEAL_BONUS",
    "HEAL_BONUS_CAP",
   	 "CHARISMA",
    "CHARISMA_CAP",
    "FLAIL_DAM",
    "KICK_DAM",
    "HAND_DAM",
    "HAND_DAM_CAP",
    "DAM_RED",
    "DAM_RED_CAP",
    "SEX",
    "GROUP_LEADER",
    "TANK_HEALTH",
    "TANK_HEALTH_MAX",
    "TANK_LEVEL",
    "TANK_NAME",
    "LEVEL_SEC",
    "LEVEL_TER",
    "LEVEL_QUA",
    "LEVEL_QUI",
    "LEVEL_HEX",
    "LEVEL_SEP",
    "LEVEL_OCT",
    "LEVEL_AVA",
    "CITIZEN",
    "CLASS_SEC",
    "CLASS_TER",
    "CLASS_QUA",
    "CLASS_QUI",
    "CLASS_HEX",
    "CLASS_SEP",
    "CLASS_OCT",
    "CLASS_AVA",
    "STAB_DAM",
    "STAB_DAM_CAP",
    "INT_PERM",
    "HITROLL",
    "DAMROLL",
    "OPPONENT_HEALTH",
    "OPPONENT_HEALTH_MAX",
    "OPPONENT_NAME",
    "OPPONENT_LEVEL",
    "TERRAIN",
    "AFFECTS",
    "ROOM_EXITS",
      }
  for k,v in pairs(vars) do
    sendMSDP("REPORT",v)
  end
end

initialise_msdp()
```

After copy/pasting this in a new script, you can enter **lua msdp** on the command line to see all the variables that will automatically update!

</div>

<div class="post" data-post-id="35447" data-author="*Idjit*" data-date="2014-10-07T03:12:12+00:00" data-subject="Re: Mudlet 3.0.0 Beta (Native MSDP support)">

I notice that Akaya doesn't list WEAPON_DAM_CAP in his variables.

This was added in August, Akaya see that post.

Thanks

</div>

<div class="post" data-post-id="35448" data-author="Akaya" data-date="2014-10-07T14:31:16+00:00" data-subject="Re: Mudlet 3.0.0 Beta (Native MSDP support)">

There are a few I'm missing, you're right. I noticed HUNGER and THIRST wasn't on there either. Let me see if I can hunt down a full list...

</div>

<div class="post" data-post-id="37020" data-author="Akaya" data-date="2016-07-01T07:45:18+00:00" data-subject="Re: Mudlet 3.0.0 Beta (Native MSDP support)">

Is there MSDP support for AREA_VNUM or something like it? I know there's AREA_NAME but a matching VNUM would do wonders.

</div>
