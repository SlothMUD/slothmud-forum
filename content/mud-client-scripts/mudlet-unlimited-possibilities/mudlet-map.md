---
title: "Mudlet map"
topic_id: 4970
author: "Bandit"
date: 2020-05-08T23:57:59+00:00
last_activity: 2020-10-24T06:02:06+00:00
last_author: "Gorka"
sticky: false
locked: false
post_count: 7
---

<div class="post" data-post-id="39475" data-author="Bandit" data-date="2020-05-08T23:57:59+00:00" data-subject="Mudlet map">

Map scripts: [https://app.box.com/s/il2lpk701m2u2qwykgox6lxigkr4t4me](https://app.box.com/s/il2lpk701m2u2qwykgox6lxigkr4t4me)

Map data: [https://app.box.com/s/0mica9lo2dur7pnbvdeydp2zkuc3jew1](https://app.box.com/s/0mica9lo2dur7pnbvdeydp2zkuc3jew1)

Grab both of those. Install the scripts in the mudlet package manager and move the sloth-map.dat file to the mudlet/profiles/Sloth Mud folder (or whatever your profile is in Sloth). You'll probably have to open up Mudlet settings and go to the Mapper tab and load the map file in there. If it all works you'll be able to open a map window and start seeing the map and your location.

Not everything is mapped, but probably 87.5% (basing this on my explored value) is mapped. If you'd like to help me map out some missing areas the best way would be to group with me and clear out anything big that would stop me from getting the map. I'd like to keep the map creation script to myself so we don't have a bunch of diverging maps since there isn't a good way to merge them together.

You'll also need to make sure MSDP variables are being reported, this post has a script that is useful for that: [http://www.slothmud.org/forum/viewtopic.php?f=39&t=4424](http://www.slothmud.org/forum/viewtopic.php?f=39&t=4424)

Also if you have the generic_mapper installed you should disable / remove it, as it can cause issues.

</div>

<div class="post" data-post-id="39582" data-author="cnl" data-date="2020-10-21T04:04:57+00:00" data-subject="Re: Mudlet map">

Thanks for posting this - 

I tried to get your script working but I seem to be missing some pieces.

Does this depend on the generic_mapper being installed?

</div>

<div class="post" data-post-id="39583" data-author="cnl" data-date="2020-10-21T07:13:59+00:00" data-subject="Re: Mudlet map">

I'm probably recreating the wheel here but I've mostly got a working instance of the mapper going -

[https://imgur.com/a/tBuJ8st](https://imgur.com/a/tBuJ8st) - I'm assuming there's always no way around manually correcting the rooms that don't line up.

</div>

<div class="post" data-post-id="39584" data-author="cnl" data-date="2020-10-21T17:30:28+00:00" data-subject="Re: Mudlet map">

Your map data is super cool.

It looks like you also saved it with Id == room vnum so it loads perfectly with what I have.

</div>

<div class="post" data-post-id="39586" data-author="cnl" data-date="2020-10-22T07:53:34+00:00" data-subject="Re: Mudlet map">

I've been playing around with the msdp.COORD* variables and the map.

See [https://imgur.com/a/T5uMpkY](https://imgur.com/a/T5uMpkY)

The rooms with a "glow" are ones being currently included in the COORD returns.

X means they reported Mob==1. It looks like this is a yes / no type result?

</div>

<div class="post" data-post-id="39588" data-author="Bandit" data-date="2020-10-22T22:22:47+00:00" data-subject="Re: Mudlet map">

The map tends to use data like msdp.CHARACTER_LOCATION.ROOM.VNUM to know where you are. It watches mspd.CHARACTER_LOCATION for changes and updates. I don't think I use the COORDS variables at all, those always seemed a bit weird.

The mud doesn't always have rooms that line up nicely. What I did is used ne/nw for up rooms, sw/se for down rooms, and then n/e/s/w for those directions. I tried to make the maps somewhat represent how they've been created on the website with all the map images. There's a few early maps I mad that use the z axis, but those are pretty rare and just there to avoid lots of rooms from overlapping. Outside of that there are some zones that really line up poorly, like energy plane, the rooms have some crazy exits that aren't a grid.

I play Shatterhand and Bandit in the mud, feel free to ask anything there.

</div>

<div class="post" data-post-id="39590" data-author="Gorka" data-date="2020-10-24T06:02:06+00:00" data-subject="Re: Mudlet map">

IIRC there are some areas where the builders didn't even set the COORDS for the area. 

In a perfect world, all areas would be fixed by a few commands given to certain players who could set correctly the X,Y,Z over time for all areas. Currently I don't think there is even a Z axis - which really would need to be added.

Also at one stage the immortals almost gave us a dump of certain info from the area files,which would have allowed us to generate the world maps without visiting the rooms, but it never got finished.

</div>
