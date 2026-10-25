---
title: "MSDP Update ( Group )"
topic_id: 4399
author: "*Splork*"
date: 2014-10-18T13:47:37+00:00
last_activity: 2014-10-20T05:07:55+00:00
last_author: "*Breeze*"
sticky: false
locked: false
post_count: 4
---

<div class="post" data-post-id="35458" data-author="*Splork*" data-date="2014-10-18T13:47:37+00:00" data-subject="MSDP Update ( Group )">

Added a new variable called group. It looks something like the following:

```
GROUP = {
    MEMBER1 = {
      MANA = "611",
      POSITION = "Back",
      NAME = "Splork",
      MAX_MANA = "611",
      HITPOINTS = "1216",
      MAX_HITPOINTS = "1216"
    },
    MEMBER2 = {
      MANA = "316",
      POSITION = "Leader",
      NAME = "Whatta",
      MAX_MANA = "316",
      HITPOINTS = "319",
      MAX_HITPOINTS = "319"
    },
    MEMBER0 = {
      MANA = "179",
      POSITION = "Back",
      NAME = "Unmace",
      MAX_MANA = "179",
      HITPOINTS = "251",
      MAX_HITPOINTS = "251"
    }
```

This may change slightly if I can come up with a better way to declare position of the player in a group or decide to add more information. Currently, there are 5 possible positions: Pleader ( point and leader), Leader, Point, Front, or Back.

This creates variables inside the original "Group" variable. An example of how these can be accessed within Mudlet:

lua msdp.GROUP.MEMBER0.NAME

"Splork"

lua msdp.GROUP.MEMBER0.HITPOINTS

"1216"

Splork

</div>

<div class="post" data-post-id="35459" data-author="*Breeze*" data-date="2014-10-19T05:25:51+00:00" data-subject="Re: MSDP Update ( Group )">

You could add 'pstate'

For the groupie..

Standing 

Sitting

Sleeping

Fighting

Incap

Morted

Dead

Etc

</div>

<div class="post" data-post-id="35460" data-author="*Splork*" data-date="2014-10-19T23:36:36+00:00" data-subject="Re: MSDP Update ( Group )">

The new group variable looks like the following:

```
 GROUP = {
    MEMBER0 = {
      MANA = "578",
      POSITION = "Leader",
      MAX_MOVES = "366",
      MAX_HITPOINTS = "1382",
      MOVES = "366",
      MAX_MANA = "578",
      STATUS = "Fighting",
      HITPOINTS = "1382",
      NAME = "Jake"
    }
  },
```

Status options are the following:

Dead

Dying

Incapped

Stunned

Absent

Fighting

Standing

Resting

Sleeping

-- if none of those, Present

Thanks for the idea Breeze, enjoy your vacation@

Enjoy,

Splork

</div>

<div class="post" data-post-id="35461" data-author="*Breeze*" data-date="2014-10-20T05:07:55+00:00" data-subject="Re: MSDP Update ( Group )">

Looks good :)

And thanks

</div>
