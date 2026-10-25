---
title: "MSDP Updates"
topic_id: 4175
author: "*Splork*"
date: 2013-12-24T13:16:26+00:00
last_activity: 2014-01-24T18:29:20+00:00
last_author: "*Splork*"
sticky: false
locked: false
post_count: 3
---

<div class="post" data-post-id="34686" data-author="*Splork*" data-date="2013-12-24T13:16:26+00:00" data-subject="MSDP Updates">

MSDP Changes after reboot

â€¢	MSDP_Coord1-25 variables changed to just Coord1, coord2, etc to 25 ( I will flush this out better after       Christmast, similar to the new string variables

â€¢	MSDP_ROOM_DIR variables changed to just ROOM_SOUTH, ROOM_NORTH, etc

â€¢	STAT_PERM variables now read correctly, wonâ€™t mimic Str, Int, and other MSDP stat variables

â€¢	HUNGER added

â€¢	THIRST added

â€¢	STRING_AFFECTS added,  in string format, easier parsing

â€¢	STRING_PERM_AFFECTS added, in string format, easier parsing, permanent and innate affects

â€¢	STRING_EXITS added, in string format, easier parsing

These go in on reboot or crash,

Splork

</div>

<div class="post" data-post-id="34689" data-author="*Splork*" data-date="2013-12-26T04:14:38+00:00" data-subject="Re: MSDP Updates">

MSDP variables added:

Position : current position of the player

Worships : who the player worships

These will be in on next reboot or crash, same as the ones mentioned above,

Splork

</div>

<div class="post" data-post-id="34823" data-author="*Splork*" data-date="2014-01-24T18:29:20+00:00" data-subject="Re: MSDP Updates">

The following MSDP string variables have been added. The variables are set upon wearing an item. The string resembles the following: Vnum: #, DESC: description, AC:value, AFF: value

Examples:

MSDPWEAR_LIGHT = "VNUM:4,DESC:a hexagonal shaped token",

 MSDPWEAR_FINGER_R = "VNUM:2103,DESC:a small topaz ring,AC-apply:-0.1, SPELL_BONUS:100, HITPOINT:3",

As with ALL MSDP variables, please do not request the data if you are not going to use it.

WEAR_LIGHT,

WEAR_FINGER_R,

WEAR_FINGER_L,

WEAR_NECK_1,

WEAR_NECK_2,

WEAR_BODY,

WEAR_HEAD,

WEAR_LEGS,

WEAR_FEET,

WEAR_HANDS,

WEAR_ARMS,

WEAR_SHIELD,

WEAR_ABOUT,

WEAR_WAIST,

WEAR_WRIST_R,

WEAR_WRIST_L,

WEAR_WIELD,

WEAR_HOLD,

WEAR_TWO_HANDED,

I will add these to the helpfile soon.

Splork

</div>
