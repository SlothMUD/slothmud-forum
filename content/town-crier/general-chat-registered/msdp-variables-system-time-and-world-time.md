---
title: "msdp variables SYSTEM_TIME and WORLD_TIME"
topic_id: 5111
author: "Woody"
date: 2024-10-31T14:54:56+00:00
last_activity: 2024-11-01T19:41:29+00:00
last_author: "cnl"
sticky: false
locked: false
post_count: 5
---

<div class="post" data-post-id="40120" data-author="Woody" data-date="2024-10-31T14:54:56+00:00" data-subject="msdp variables SYSTEM_TIME and WORLD_TIME">

The msdp variables SYSTEM_TIME and WORLD_TIME are returning "0" for me.

I'm currently using DURATION on ' avatar sight' to time tick length for a lagometer, as my newbies don't have long duration spells, Is there a better variable to use?

</div>

<div class="post" data-post-id="40121" data-author="cnl" data-date="2024-11-01T01:23:31+00:00" data-subject="Re: msdp variables SYSTEM_TIME and WORLD_TIME">

Not sure how your lag… thing works but quite a few msdp variables seem to be placeholders 

I put game time in my prompt and pull it from there (timestamping capture time)

I kinda keep an eye on this for mob regen ticks - not sure if this is the tick you’re looking for

System time is just PST - it doesn’t lag

</div>

<div class="post" data-post-id="40123" data-author="Woody" data-date="2024-11-01T14:05:12+00:00" data-subject="Re: msdp variables SYSTEM_TIME and WORLD_TIME">

The msdp.CHARACTER_AFFECTS spell DURATION is in seconds.

I compare this to a local timer and it's usually accurate to +/- 0.01 seconds.

Twice a day we get lagstorms where 1 tick will take 3, 5 or even 10+ seconds, afterwards the server seems to run ticks at 0.33 seconds to 'catch up'.

It's handy to know when these storms hit, and more importantly, have ended!

Running a big group at 3x speed is a bit too clenchy for me, but Asterix appears to enjoy it!

</div>

<div class="post" data-post-id="40124" data-author="Woody" data-date="2024-11-01T14:38:35+00:00" data-subject="Re: msdp variables SYSTEM_TIME and WORLD_TIME">

If it's a config on the server a 'catch up' tick duration of 0.5 or 0.66 would be preferable!

</div>

<div class="post" data-post-id="40128" data-author="cnl" data-date="2024-11-01T19:41:29+00:00" data-subject="Re: msdp variables SYSTEM_TIME and WORLD_TIME">

msdp.CHARACTER_AFFECTS becomes bugged at high numbers of effects, spells being up - it hardly ever reports any values at all for Fuligin with my permanent buys and artifacts etc - I had to unreport it.

So I suggest you don't get too dependent on using it.

I use msdp.AFFECTS even though it has way less data and supplement with triggers were needed.

I suggest if you're going to continue with your approach of detecting lag you just make it more flexible than hard coded to a single spell type, and base it off msdp.AFFECTS instead. maybe just keep picking whatever has the most time on it.

</div>
