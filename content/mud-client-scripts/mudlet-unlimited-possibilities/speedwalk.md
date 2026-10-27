---
title: "Speedwalk"
topic_id: 4167
author: "DarkArtist"
date: 2013-12-10T22:45:23+00:00
last_activity: 2013-12-12T11:41:11+00:00
last_author: "DarkArtist"
sticky: false
locked: false
post_count: 3
---

<div class="post" data-post-id="34618" data-author="DarkArtist" data-date="2013-12-10T22:45:23+00:00" data-subject="Speedwalk">

Alias Speedwalk

Pattern:

^([0-9neswdu]+)$

for count, direction in string.gmatch(matches[2], "([0-9]\*)([neswdu])") do 

 count = (count == "" and 1 or count)

 for i=1, count do send(direction,false) end

end

\--Except that this matches on the opening screen when you hit 1 to enter the game. If anyone can figure out how to fix the pattern to not match on a single \\d, pls post it.

to correct this i added:

if matches[1]="1" then send("1") else ...

It'd be better to just fix the pattern tho.

</div>

<div class="post" data-post-id="34623" data-author="Avar" data-date="2013-12-11T18:49:23+00:00" data-subject="Re: Speedwalk">

Maybe this will work:

^([0-9neswud]\*[neswud]+)$

</div>

<div class="post" data-post-id="34624" data-author="DarkArtist" data-date="2013-12-12T11:41:11+00:00" data-subject="Re: Speedwalk">

Yup, thanks <img src="/images/smilies/icon_e_smile.svg" alt=":)" title=":)" width="15" height="15" class="smiley nozoom">

</div>
