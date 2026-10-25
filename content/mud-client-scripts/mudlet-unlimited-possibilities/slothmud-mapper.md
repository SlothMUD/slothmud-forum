---
title: "SlothMUD Mapper"
topic_id: 4395
author: "Akaya"
date: 2014-10-11T15:14:57+00:00
last_activity: 2016-07-09T04:10:53+00:00
last_author: "Akaya"
sticky: false
locked: false
post_count: 7
---

<div class="post" data-post-id="35449" data-author="Akaya" data-date="2014-10-11T15:14:57+00:00">

It's finally here! The SlothMUD Mapper!

![](https://imageshack.com/i/eyeEnzNTp)

SlothMUD Mapper is a mapping script that automatically maps rooms as you move through the world of Jord.

FEATURES:

* Auto-mapping based on MSDP information

* Double click any room to run there

* Customize room colors by terrain type

* Zoom in/out

* View any room or area from anywhere

* Create custom run paths

To get it to work:

- 1 ) I recommend a new profile.

2 ) Create a new script and copy/paste the following into it:

```
function initialise_msdp()
  local vars = {
    "ROOM_DESC",
    "ROOM_RNUM",
    "WEAR_HEAD",
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
    "HUNGER",
    "THIRST",
    "COORD1","COORD2","COORD3","COORD4","COORD5","COORD6","COORD7","COORD8","COORD9","COORD10","COORD11","COORD12","COORD13","COORD14","COORD15","COORD16","COORD17","COORD18","COORD19","COORD20","COORD21","COORD22","COORD23","COORD24","COORD25",
  }
  for k,v in pairs(vars) do
    sendMSDP("REPORT",v)
  end
end
```

3 ) Before logging in, enable MSDP in Mudlet Settings and restart the profile.

4 ) Install the attachment via the Package Manager on the Mudlet toolbar.

5 ) Login.

6 ) Enter lua initialise_msdp() send("\n") from the command line.

7 ) Enter mapping mode on from the command line.

8 ) Enter map start from the command line.

That should create your first room. You can then move around the script will do everything for you. 

NOTES:

* Some locations won't map perfectly on a square grid in which you can right click the room you need to move     and drag the mouse in the direction you wish. 

* You can alter the room colors  in the appropriate script by altering setCustomEnvColor(17, 0, 0, 0, 100) to whatever you want. The last four parameters are the rgba values. In this case it would be 0, 0, 0, 100 which is black with 100 transparency.

* Special exits (such as flying via dragon/phoenix/griffon) will not work with the speedwalk function just yet.

* If you need to connect two rooms that the mapper may have missed, use the alias CONNECT [room1] [room2] [direction] So for example, connect 126 150 east will connect room 126 to 150 in a eastward direction.

</div>

<div class="post" data-post-id="35450" data-author="DarkArtist" data-date="2014-10-12T11:12:11+00:00">

YESS! You're the man Akaya. This is big news!

Question: Do I have to update to the new Beta version for it to work?

</div>

<div class="post" data-post-id="35452" data-author="Akaya" data-date="2014-10-12T15:02:05+00:00">

Yes. It requires Mudlet 3.0 beta+ as it utilizes the new sendMSDP function and requires that you enable the new 'Enable MSDP' feature in Mudlet's settings.

</div>

<div class="post" data-post-id="35474" data-author="Calex" data-date="2014-10-27T20:02:46+00:00">

I have been using Akaya's mapper. Brilliant effort! A few things I needed to do to get it to work for me (I'm using OSX 10.10). Note. This mapper requires MSDP functionality. You must be using mudlet 3.0.0-beta 2 or later and have selected MSDP in the Settings/General window. (If you are doing that as you read this, you must restart mudlet for the MSDP functionality to be in use).

In the package Akaya has provided, import it as he specifies.

Then, before you do anything else, open the editor window (any pane e.g. Alias, Trigger, Script will do) and search on RNUM. There is a box to type this in at the bottom left of the editor. If you find any files that reference RNUM (they will be in the form ROOM_RNUM), change the occurrences to ROOM_VNUM.

Akaya also provides a lua function you can copy and paste into a mudlet Script file. The function's name is initialise_msdp(). Note the british 's', not the american 'z' in initialise if you ever want to run this manually. Create a script file with that function. One of the items in the local_vars table is "ROOM_RNUM". Just delete that line in the table. Further down you will see that "ROOM_VNUM" is provided, which is what you want.

Once you have done the preceding steps, you can enter the command, MAPPING ON, at the command line. You should get a message back that all is ok.

Then enter the command, MAP START, at the command line. You should get back a message saying that initialisation must be done first and the command will do it for you and report it done.

If you open the mudlet mapper now, and you've not used the mapper before, you should see a single room that is highlighted because you are in that room. Move in one of the exit directions and you should see a second room created on your map. If you see this, congratulations, everything is working!

Note: Each time you log back in to SlothMud, execute the MAPPING ON and MAP START commands

Below are instructions for installing a starter map for SlothMud that has many newbie areas already mapped for you. If you want to use this starter map, then you need to exit from mudlet like you would normally and save your contents

The first challenge is to find the folder you want to put this .dat file in.

On a mac, you will find your SlothMud profile using ~/.config/mudlet/profiles/

On a pc, you fill find your SlothMud profile using User/<your login name>/.config/mudlet/profiles

In the profiles directory, you will have one or more profiles for SlothMud. Open the profile for the SlothMud you were using when you created the initial room mappings

There should be a folder/directory there called 'map'. Inside the map directory you will find one or more .dat files. You will want to put my .dat file in the 'map' directory, but change the date time in the name to one that is later than your latest .dat file, but on or before the current date time.

When you go back into SlothMud, open the map window, do MAPPING ON and MAP START. At the very bottom of the map window there is a small arrow shaped like ^ or v. If you don't see the settings window in the map window, click on that arrow. In the settings window you will see a dropdown for various areas that have been created with some mapping. If there are a lot of them, you have loaded my map.dat successfully.

</div>

<div class="post" data-post-id="35475" data-author="Calex" data-date="2014-10-27T20:06:48+00:00">

The map.dat file did not upload. Trying again. Can't upload. Here's a link

[<LINK_TEXT text="https://dl.dropboxusercontent.com/u/483 ... -35map.dat">https://dl.dropboxusercontent.com/u/48327224/27-10-2014%2312-16-35map.dat</LINK_TEXT>](https://dl.dropboxusercontent.com/u/48327224/27-10-2014%2312-16-35map.dat)

</div>

<div class="post" data-post-id="35477" data-author="Akaya" data-date="2014-10-28T20:15:41+00:00">

Thank you for this! Most appreciated! Still adding some new features. 

I'll have an update soon (with fixes that should make installation easier  :lol: )

New features will include (but not limited to):

- door display

- window display

- special exit creation API (so you can ride boats, dragons, griffons, etc. with speedwalk)

- renovated path creation API

</div>

<div class="post" data-post-id="37032" data-author="Akaya" data-date="2016-07-09T04:10:53+00:00">

With the removal of msdp.COORD#, this script is broken. I'll need to rewrite it using msdp.ROOM_EXITS instead.

</div>
