---
title: "map.roomFind()"
topic_id: 5115
author: "Woody"
date: 2024-12-02T10:53:16+00:00
last_activity: 2024-12-02T19:35:14+00:00
last_author: "Woody"
sticky: false
locked: false
post_count: 2
---

<div class="post" data-post-id="40138" data-author="Woody" data-date="2024-12-02T10:53:16+00:00" data-subject="map.roomFind()">

I was trying to find a way to search the room names in the sloth-map.dat and stumbled upon the function roomFind!

I added a trigger to make a clickable link in the output of locate:

perl-regex pattern (probably too wide, but it works):

^.* is in (.*).$

lua:

  selectString(matches[2], 1)

  setLink([[map.roomFind("]]..matches[2]..[[")]], matches[2])

Then you can just click on the room name in the locate result! e.g.

cast 'locate' Gnoph-Keh

Ok.

The horn of Gnoph-Keh is in The Bamboo Copse.

*click*

You know the following relevant rooms:

 ROOM ID   ROOM NAME                               ROOM AREA

 74039     The Bamboo Copse                        Herbalist Isle II

1 rooms found.

</div>

<div class="post" data-post-id="40139" data-author="Woody" data-date="2024-12-02T19:35:14+00:00" data-subject="Re: map.roomFind()">

gotoRoom() is not much use if you mainly use roomFind for global searches, and even if the room is in the same area, you can still double click to speedwalk there.

In the Generic Mapper - Mapso, iScript the function map.roomFind(query, lines) at line 3045 can be 'tweaked' to be more useful by changing gotoRoom() to centreview().

replace:

```
      cechoLink(
        string.format("<cyan> %-10s", roomid),
        'gotoRoom(' .. roomid .. ')',
        string.format("Go to %s (%s)", roomid, tostring(roomname)),
        true
      )
```

with:

```
      cechoLink(
        string.format("<cyan> %-10s", roomid),
        'centerview(' .. roomid .. ')',
        string.format("Center view on %s (%s)", roomid, tostring(roomname)),
        true
      )
```

Then the Room ID click will load the right map and centre on the room you are interested in!

</div>
