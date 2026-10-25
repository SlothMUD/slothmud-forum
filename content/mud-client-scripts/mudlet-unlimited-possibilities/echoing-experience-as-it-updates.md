---
title: "Echoing Experience as it Updates"
topic_id: 4596
author: "*juggleblood*"
date: 2016-02-26T01:53:29+00:00
last_activity: 2016-02-26T09:38:54+00:00
last_author: "Teron"
sticky: false
locked: false
post_count: 3
---

<div class="post" data-post-id="36639" data-author="*juggleblood*" data-date="2016-02-26T01:53:29+00:00">

This is something that I knew some people were doing, but didn't appreciate how nice it is until I tried it. Every time the MSDP Experience variable updates, I simply echo the amount of the increase. So then I can have a better feel for which of my special abilities are doing the best damage. 

So step 1 is to get MSDP experience updating. 

Then, find your update exp function which should look something like:

function updateExperience()

xp=atcp.MSDPEXPERIENCE+0

end 

and change it to:

function updateExperience()

if atcp.MSDPEXPERIENCE+0~=xp then

lastXp=xp

xp=atcp.MSDPEXPERIENCE+0

xpDelta=xp-lastXp

cecho("<cyan>"..xpDelta.."<reset>") end

end

*don't forget to put xp, lastXp, and xpDelta in definitions, i.e. xp=xp or 0, etc...

Now you are seeing your exp increases and can use xpDelta in triggers to track various statistics and such.

Cheers.

</div>

<div class="post" data-post-id="36642" data-author="Madigan" data-date="2016-02-26T06:34:31+00:00">

I've been foaming at the bits to get up and running on mudlet ever since you mentioned being able to do this. Can't wait to give it a shot. GREAT feature.

THx for sharing.

</div>

<div class="post" data-post-id="36643" data-author="Teron" data-date="2016-02-26T09:38:54+00:00">

You also need to take into account that the exp delta you see is pretty much randomized and you can only average it between 10 increases for the same skill to estimate your damage more or less accurately.

Also, exp depends on mob level, so you have to take it into account, which further complicates things.

If you find a way to accurately do math with the variable mob level, do let me know. Thanks.

</div>
