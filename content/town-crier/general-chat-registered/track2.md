---
title: "track2"
topic_id: 4765
author: "*teker*"
date: 2017-05-31T17:41:49+00:00
last_activity: 2017-05-31T19:45:47+00:00
last_author: "Gorka"
sticky: false
locked: false
post_count: 4
---

<div class="post" data-post-id="38271" data-author="*teker*" data-date="2017-05-31T17:41:49+00:00" data-subject="track2">

I forgot to mention that I added a track2 command to test out a different algorithm for tracking.  It performs the same skill check that track uses but the search algorithm is different.  It specifically will not track through water or air or flying creatures.  Let me know what you think of it.

</div>

<div class="post" data-post-id="38272" data-author="Gorka" data-date="2017-05-31T18:54:56+00:00" data-subject="Re: track2">

Teker, one issue with track I think I have seen is that when you give it a target, it doesn't necessarily track to the nearest target... unless it goes through that room... it's noticeable in a place like positive plan when tracking beings or elemental school when tracking dwarf. Can you confirm that is the case and could the algorithm be smarter in these cases to go to the closest target rather than zig zagging across an area.

</div>

<div class="post" data-post-id="38274" data-author="*teker*" data-date="2017-05-31T19:25:36+00:00" data-subject="Re: track2">

The new algorithm tries to find the closest one (breadth first search).  I didn't want to just swap the code out in case there are other issues that arise that I didn't think of.

</div>

<div class="post" data-post-id="38275" data-author="Gorka" data-date="2017-05-31T19:45:47+00:00" data-subject="Re: track2">

![](https://68.media.tumblr.com/be4c843583271df2665b99da0aa480d9/tumblr_o3v2a0cCs11uqe8iio1_500.gif)

</div>
