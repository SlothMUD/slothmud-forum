---
title: "Changelog 2017-07-29"
topic_id: 4781
author: "*teker*"
date: 2017-07-30T02:38:10+00:00
last_activity: 2017-08-08T19:43:25+00:00
last_author: "*teker*"
sticky: false
locked: false
post_count: 4
---

<div class="post" data-post-id="38361" data-author="*teker*" data-date="2017-07-30T02:38:10+00:00">

The crash brought us:

- The schedule list colors have changed to make it more readable

- New MSDP variables GROUP2 and GROUP2_JSON.  They're a little different than GROUP.  The player name is listed in the top level table and the STATUS field for each player contains things like "Dead" or "Webbed" or "Blind,Bound,Webbed", etc.  Or it could contain "Ok".  I also believe it will work correctly with incredibly large groups like we sometimes see on major holidays.

</div>

<div class="post" data-post-id="38385" data-author="Gorka" data-date="2017-08-07T06:34:18+00:00">

Teker, can't confirm this is a "thing" but I had weird "send and receive" issues when I added GROUP2 to my msdp variables. At times I would type things like eq or inv and nothing would happen... like my send and receives of some mud text were being lost... this effected mud messages, grouptells and fighting. However I noted msdp was updating during these times because the timers on my spells were decreasing. Removing this variable from my msdp variables list seem to clear this issue up. Also Jackalope told me that the JSON variable arrives malformed sometimes. My suspicion is GROUP2 is either malformed, or lagging things to hell which leads to failed communications.

Also could you please tell me which msdp variable is the best to use for my hp, mana and move currently as there are two. Would prefer to use the one that gets updated the fastest.

</div>

<div class="post" data-post-id="38387" data-author="*teker*" data-date="2017-08-08T02:01:57+00:00">

I would love to see one of the malformed JSON values.  The code for native MSDP versus JSON is the same except for the encoder so the same bug will be present in both.  I suspect it may have to do with the code I put in to handle larger groups.  I've only been able to test it with a small group myself, but I'm travelling this week so maybe I'll be able to catch a group one evening.

Right now the updates are the same for GROUP2 and CHARACTER_HEALTH.  I'm thinking CHARACTER_HEALTH might go away if GROUP2 contains the same amount of player information.  The older variables (MANA, etc) refresh at the same time as well.

</div>

<div class="post" data-post-id="38388" data-author="*teker*" data-date="2017-08-08T19:43:25+00:00">

I'm pretty sure I found it.  The fix should go in next reboot.

</div>
