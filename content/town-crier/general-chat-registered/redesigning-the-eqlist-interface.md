---
title: "Redesigning the eqlist interface"
topic_id: 4192
author: "van"
date: 2014-01-31T21:37:46+00:00
last_activity: 2014-02-18T08:07:05+00:00
last_author: "Ezekiel"
sticky: false
locked: false
post_count: 7
---

<div class="post" data-post-id="34844" data-author="van" data-date="2014-01-31T21:37:46+00:00" data-subject="Redesigning the eqlist interface">

Hi all!

In consultation with Splork and Breeze, I'm undertaking a side project of redesigning the interface for the eqlist. Primarily, this is because I want specific features that the web-based eqlist doesn't have (or can't do easily), and I'm just OCD enough to spend more time on a new UI than I would simply adapting to the new tool. I'm looking for input from other players on what features they like, what features they don't like, what features they'd like to see added, and so forth.

First, a shout-out to Splork and Breeze and whoever else for creating a system with truly impressive retrieval, filtering, and query features, and many thanks to them: without the back-end they've put together none of what I'm hoping to do will be possible. I plan to leave <strong>everything</strong> they've done intact for people who like the new eqlist tool, while incorporating some of my favorite new features into the tool I create.

So: I want suggestions! From my viewpoint as a newly returning person who had truly crappy gear, I found myself looking for some of the features below. Again, the current tool can do a lot of these things, but I would like to create a tool that has more of the "Type, Click, Found it!" behavior of the old S3 eqlist. 

Things I'm already thinking about:

\- Compacting results to reduce the size of individual items (for instance, "tidy" the restrictions, default to not showing fields that aren't very interesting), and using mouseover dialogs to give you access to full item info

\- Results presented by equipment type (e.g. head, light, feet, cp, potion) so you can jump directly to the slot you're interested in.

\- Drop-down menus to search by common stats (str, dex, mana\_regen, blast\_dam, what have you), replacing the long list format of the current site. Allow for \<, =, \> queries on item values.

\- Dynamic filtering of retrieved search results (e.g. change parameters to eliminate those damn 6x40 items you know you'll never get to wear, or get a list of +dam items and then decide you only want to see the ones that come with +mana, too).

I could go on, but hopefully you get the idea.

First step is revamping the interface so it's something I (and maybe you) enjoy using. I have some longer term goals, for instance a "Find upgrade" system, saving personal search results via your website account (I spend way too much time querying the same thing over and over!), a "Dress Me For [STAT]!" optimization program, and silly things like that.

I'll be posting forum updates on this as I hit certain milestones, and I'd love to have input from everybody on what they like, what they hate, and what they want from our beloved eqlist.

</div>

<div class="post" data-post-id="34847" data-author="*Breeze*" data-date="2014-02-01T07:52:16+00:00" data-subject="Re: Redesigning the eqlist interface">

Remember to get with me whenever you want to save or load something to/from a chars profile so I can tell you how to auth the char and access the storage linked to the char logged in, including their stats for the dressing room bits.

Also I want to remind everyone I have nothing to do with the version that van is doing other than validating the code, so bug reports will go to him.

Are you going to use my database or will you need your own? (Email me)

</div>

<div class="post" data-post-id="34848" data-author="Marvel" data-date="2014-02-01T23:45:39+00:00" data-subject="Re: Redesigning the eqlist interface">

\#1 on list: Make xtraflag searchable so you can find CAN-SHAPESHIFT items.

</div>

<div class="post" data-post-id="34853" data-author="*Breeze*" data-date="2014-02-04T23:04:11+00:00" data-subject="Re: Redesigning the eqlist interface">

you \_can\_ search for shapeshiftable (TYPE\_SHAPESHIFT) stuff but you cant combine with other type\_ filters but you should be able to use the wear\_ filters with it..

</div>

<div class="post" data-post-id="34854" data-author="Reece" data-date="2014-02-05T09:54:30+00:00" data-subject="Re: Redesigning the eqlist interface">

Like I already told you on the mud but you told me to put it here..

I would like to see a comparison feature implemented, be much easier to figure out which eq is better, etc. This point may be moot after you implement the Upgrade My Eq feature, but oh well.

</div>

<div class="post" data-post-id="34855" data-author="*Breeze*" data-date="2014-02-05T10:43:12+00:00" data-subject="Re: Redesigning the eqlist interface">

Patrick is doing it. I am providing him the data and he is redoing it.

The list should have been a mortal thing anyways.

</div>

<div class="post" data-post-id="34870" data-author="Ezekiel" data-date="2014-02-18T08:07:05+00:00" data-subject="Re: Redesigning the eqlist interface">

I liked it when I would be helping newbs navigate the site two eq lists ago... when say they were level 20:

I could tell them 'ok, look for all equipment ...order items by= armor class, slot filter dropdown=foot... and then in the open query line i would get them to type '-0.3'. This would yield them all the comparative equipment that they could wear at their levels for that slot at that armor class. It was insanely easy, after doing this once...for newbs to grasp exactly how to search for what their next upgrade should be, or what they were currently lacking. I don't know if because of the new way things are filtered this could be accessible...but that sure was a nice feature to help both new and old players alike to do comparative eq shopping. Just my input. Thanks, Ezekiel

</div>
