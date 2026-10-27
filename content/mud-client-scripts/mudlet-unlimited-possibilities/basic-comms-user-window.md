---
title: "Basic Comms User Window"
topic_id: 4397
author: "DarkArtist"
date: 2014-10-17T04:32:08+00:00
last_activity: 2014-10-17T04:32:08+00:00
last_author: "DarkArtist"
sticky: false
locked: false
post_count: 1
---

<div class="post" data-post-id="35454" data-author="DarkArtist" data-date="2014-10-17T04:32:08+00:00" data-subject="Basic Comms User Window">

For a basic comms user window:

insert into defintions:

openUserWindow("gossip")

Then make a trigger for gossip with the following regex triggers:

^(\\w+) (gossips\|newbies)--(.\*) 

^You (gossip\|newbie)-- (.\*)

That does the following:

if table.contains(shopKeepers,matches[2])==false then

selectString(line,1)

fg("RoyalBlue")

copy()

appendBuffer("gossip")

end

Then create a table of shopkeepers in your definitions (keeps out the spam):

shopKeepers={"Valishael","Regina","Shelda","Shayne","Mikala"}

It's very basic. Just posting upon someone's request. Hope that helps. You have to adjust the size of the user window manually. There are better ways to do it, but this is one.

</div>
