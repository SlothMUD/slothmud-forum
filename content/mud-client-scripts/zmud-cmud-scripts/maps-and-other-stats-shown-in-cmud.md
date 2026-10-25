---
title: "Maps and other stats shown in CMUD?"
topic_id: 4389
author: "Kolockey"
date: 2014-08-22T23:01:54+00:00
last_activity: 2014-08-23T04:08:36+00:00
last_author: "Filk"
sticky: false
locked: false
post_count: 2
---

<div class="post" data-post-id="35427" data-author="Kolockey" data-date="2014-08-22T23:01:54+00:00">

I am new to MUDs and SlothMud.  I have been playing SlothMud from their website, but recently started playing through CMUD.  I like how it shows the map and your character stats right on the screen from when you play from the website.  Is there a way to show this same map and character stats from within CMUD when I play SlothMud using CMUD?

Thanks.

* If there is another client I can use which shows the map and stats instead of CMUD, please let me know.  Thanks.

</div>

<div class="post" data-post-id="35428" data-author="Filk" data-date="2014-08-23T04:08:36+00:00">

There is "map" command. It show rooms around current once for each using.

But you cant display it permanently, neither stats, without some heavy scripting while playing through cmud.

Some of stats, which included in mxp, arent that hard(list is in "help MXPVARIABLES"). You can get access to them with %mud.statname from cmud. And put anywhere in interface you like to.

Mdsp values are quite complicated. Cmud dont support them directly, but there was script for cmud on that forum, to get them.

Map requires to request it each time while entering new room. Then gag and display in some other window. Not easy thing to script for start.

</div>
