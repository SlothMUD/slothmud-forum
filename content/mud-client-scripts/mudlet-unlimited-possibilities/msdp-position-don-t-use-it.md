---
title: "MSDP_POSITION, don't use it."
topic_id: 4206
author: "DarkArtist"
date: 2014-03-11T13:05:56+00:00
last_activity: 2014-03-11T13:05:56+00:00
last_author: "DarkArtist"
sticky: false
locked: false
post_count: 1
---

<div class="post" data-post-id="34905" data-author="DarkArtist" data-date="2014-03-11T13:05:56+00:00" data-subject="MSDP_POSITION, don&#x27;t use it.">

Given that there is up to 2 seconds of delay time for it's update, MSDP_POSITION is effectively useless. I find that for anything involving my position, i.e. Fighting, Standing, Sleeping, Sitting, Resting 2 seconds of delay is too much for anything to work properly. Some battles don't even last 2 seconds long. I can't imagine what this variable could actually be used for the way it exists.

This is an FYI not to waste your time/get frustrated with it. Just use triggers to set your position variable as it will be accurate. 

Similarly, if your scripts depend on know what room you are in, capture the room name manually and forsake MSDP. With the delay you can't count on the MSDP giving you the right result for the room name or number.

So you'll need triggers for:

sleep, stand, wake up, rest, bashed (sitting), hates your guts, R.I.P., You are dead/stunned/incap/mort, etc...

</div>
