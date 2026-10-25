---
title: "wth is this"
topic_id: 2771
author: "Alberich"
date: 2008-03-25T23:14:42+00:00
last_activity: 2008-03-26T13:44:20+00:00
last_author: "13"
sticky: false
locked: false
post_count: 6
---

<div class="post" data-post-id="23418" data-author="Alberich" data-date="2008-03-25T23:14:42+00:00">

mxp: Error : Received undefined tag ~pirate~!

mxp: Error : Received undefined tag goldentigers!

mxp: Error : Received undefined tag ~pirate~!

this has been turning up in my debug window every time i check 'who' (i've been redoing all my scripts so yes, i keep the debug window open all the time these days).

anyone else seen this/know what the hell it means?

</div>

<div class="post" data-post-id="23419" data-author="jezer" data-date="2008-03-25T23:19:41+00:00">

I think the "!" or the "~" symbol causes a syntax error in the MXP protocol. Maybe because those symbols are reserved in the protocol?!? Nothing to worry about, apart from the spam it causes in your debug window.

I like to have my debug window open too. :)

</div>

<div class="post" data-post-id="23420" data-author="Rynquald" data-date="2008-03-25T23:23:41+00:00">

mxp doesn't seem to handle <> well, apparently it thinks anything enclosed in them is something to do with mxp.

Personally, Pirate titles (and presumably GT, haven't noticed though) always get stripped out of the who list when I check.

I'm not sure if it's client-specific, or if it happens to anything using mxp.

</div>

<div class="post" data-post-id="23422" data-author="Alberich" data-date="2008-03-25T23:29:26+00:00">

huh

good thing i don't look at who list all that often ;)

thanks guys

</div>

<div class="post" data-post-id="23423" data-author="jezer" data-date="2008-03-25T23:30:01+00:00">

If it's the <>, then maybe the MXP language is a bit like HTML. Tags are enclosed between the <>, and if it can't identify the tag you get the error.

</div>

<div class="post" data-post-id="23435" data-author="13" data-date="2008-03-26T13:44:20+00:00">

haha

error: pirates!

</div>
