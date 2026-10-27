---
title: "Group UI"
topic_id: 4400
author: "Akaya"
date: 2014-10-20T19:55:05+00:00
last_activity: 2014-11-13T14:37:40+00:00
last_author: "Tuck"
sticky: false
locked: false
post_count: 12
---

<div class="post" data-post-id="35462" data-author="Akaya" data-date="2014-10-20T19:55:05+00:00" data-subject="Group UI">

The new msdp.GROUP variable opened the doors for a group user interface. Very exciting! Here's a sneak peak...

![](http://i.imgur.com/xy8bI1i.png)

Every member of the group is listed. Each member has 3 gauges beneath their name. Health, mana and move. The icons at the top-right of every member represent their position in the group. In the above example War is at the point (and is also leader), Stilgar and Gnu are front line, and everyone else is on the back line. The background colors of each member represent their current state or status. Green shows that the member is currently fighting. Blue is for standing. And poor ol' Edwin is grey for absent.

How is this useful? Well you can now know when \*anyone\* in the group needs health/mana/move. When the group should stop for regen. When a group member dies. When someone isn't participating like they should. If someone gets lost/falls behind. When the group lead changes. When the 'world is thrown into chaos', you'll know.

</div>

<div class="post" data-post-id="35463" data-author="*Splork*" data-date="2014-10-20T22:09:19+00:00" data-subject="Re: Group UI">

This is pretty damn sweet!

</div>

<div class="post" data-post-id="35470" data-author="*Breeze*" data-date="2014-10-23T15:42:47+00:00" data-subject="Re: Group UI">

Yup can't wait to get my hands on it <img src="/images/smilies/icon_e_smile.svg" alt=":)" title=":)" width="15" height="15" class="smiley nozoom">

</div>

<div class="post" data-post-id="35481" data-author="Filk" data-date="2014-10-31T19:27:57+00:00" data-subject="Re: Group UI">

Cant post in mud updates topic, and probably thats best place for my thoughts.

Finaly got my hands on that new group msdp variable. And realized that i missing 2 more values compared to my old party status.

Would love to see Class and Level values there.

Like in basic group command output.

Class is just primary class short name: Dr, Wa, Cl, etc

Level is level summary: 0.20, 1,20, 6.20, 9.40...

Thanks in advance

</div>

<div class="post" data-post-id="35482" data-author="Akaya" data-date="2014-10-31T21:53:05+00:00" data-subject="Re: Group UI">

Not a bad idea <img src="/images/smilies/icon_e_smile.svg" alt=":)" title=":)" width="15" height="15" class="smiley nozoom">

</div>

<div class="post" data-post-id="35485" data-author="Filk" data-date="2014-11-03T05:49:02+00:00" data-subject="Re: Group UI">

Found another moment with group msdp var.

There are no value for POSITION indicating leader AND front. So when leader not on point, he shows only as leader, but not in front line.

And i still really want these class and level values.

And sorting of group is messy btw. Absent ppl and fron line ppl. All goes without sorting in random order. So i have to do it by myself in scripts, but probably still can be fixed.

Anyway, that realization is way much better then sending group and gaging all spam each every second. 

Great job.

ps: Thats how my interface looking right now: 

[![](https://img-fotki.yandex.ru/get/4805/92250543.0/0_10d128_c4ce24ff_M.jpg)](https://img-fotki.yandex.ru/get/4805/92250543.0/0_10d128_c4ce24ff_orig.jpg)

2014-11-03\_103557.jpg

</div>

<div class="post" data-post-id="35486" data-author="*Splork*" data-date="2014-11-03T12:47:10+00:00" data-subject="Re: Group UI">

I plan on adding Class and levels when I get a chance.I can also add a value for Leader/Front(LF).

However, I haven't been able to find an easy way to order the group and don't plan on working on looking at that again until I have more time.

Splork

</div>

<div class="post" data-post-id="35488" data-author="*Splork*" data-date="2014-11-04T01:04:27+00:00" data-subject="Re: Group UI">

Added GROUP.CLASS and GROUP.LEVELS

GROUP = {

 MEMBER0 = {

 MANA = "452",

 POSITION = "Leader",

 MAX\_MOVES = "426",

 MAX\_HITPOINTS = "1477",

 MOVES = "426",

 CLASS = "Wa",

 LEVELS = "9.47",

 MAX\_MANA = "452",

 STATUS = "Standing",

 HITPOINTS = "1477",

 NAME = "Splork"

 }

 },

Will be in on reboot,

Splork

</div>

<div class="post" data-post-id="35490" data-author="Filk" data-date="2014-11-06T01:22:15+00:00" data-subject="Re: Group UI">

Not sure if i am correct, but you posted these changes 2 days ago, and reset was, 1 day 9 hours ago. But changes still not ingame. Maybe something went wrong. Or maybe i am dumb <img src="/images/smilies/icon_lol.svg" alt=":lol:" title=":lol:" width="15" height="15" class="smiley nozoom">

</div>

<div class="post" data-post-id="35492" data-author="Filk" data-date="2014-11-07T01:50:09+00:00" data-subject="Re: Group UI">

Well. It appeared after last reboot. But now it has my own level and class values for each player in group <img src="/images/smilies/icon_e_smile.svg" alt=":)" title=":)" width="15" height="15" class="smiley nozoom">

</div>

<div class="post" data-post-id="35494" data-author="*Splork*" data-date="2014-11-07T19:34:50+00:00" data-subject="Re: Group UI">

This is fixed on reboot.

</div>

<div class="post" data-post-id="35506" data-author="Tuck" data-date="2014-11-13T14:37:40+00:00" data-subject="Re: Group UI">

Jeez, Filk's cmud look amazing! Good job Filk!

</div>
