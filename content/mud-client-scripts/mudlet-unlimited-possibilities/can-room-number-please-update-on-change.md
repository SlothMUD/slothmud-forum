---
title: "Can Room Number please update on change?"
topic_id: 4194
author: "DarkArtist"
date: 2014-02-07T19:17:44+00:00
last_activity: 2014-02-08T13:26:36+00:00
last_author: "DarkArtist"
sticky: false
locked: false
post_count: 3
---

<div class="post" data-post-id="34857" data-author="DarkArtist" data-date="2014-02-07T19:17:44+00:00">

Instead of sending MSDPROOM_NUMBER on a timed interval, would it be possible to please have it update everytime it changes instead?

It would make it more usable, since currently there is a one or two second delay. The delay is problematic if you are triggering off something in the room such as a mob and you want to test what room you're in.

i.e.

Trigger: A big nasty monster is here.

Script: if roomNumber==x then do y elseif roomNumber==y then do z.

Currently you would have to put the script on a tempTimer to give the msdp room variable a chance to update.

Likewise for room_name and position and any others you can think of where a 1 or 2 second delay is undesirable.

Pretty pls. Thanks for considering!

</div>

<div class="post" data-post-id="34858" data-author="*Splork*" data-date="2014-02-07T23:28:39+00:00">

The delay is about a second, sometimes a bit more or sometimes a bit less, depending on when the last "pulse" passed. I will move the function and cut the time in half which should make it pretty much automatic. 

Currently, just about all MSDP data( except the new worn_msdp stuff ) is kept in one function which makes it easy to add to or find bugs. If I start separating everything it will cause too much of a mess, so hopefully this will work. I'll make the changes tonight, commit them, post the change, and reboot in the morning.

Let me know, after I have posted that the changes are in, if it is working quick enough. It should be at that point as any of the other main timing functions such as for fighting or prompts is actually slower than the MSDP stuff. 

Splork

</div>

<div class="post" data-post-id="34859" data-author="DarkArtist" data-date="2014-02-08T13:26:36+00:00">

Thanks much :) Happy to test it.

</div>
