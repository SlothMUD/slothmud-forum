---
title: "Junk protection"
topic_id: 4953
author: "Gorka"
date: 2020-02-27T13:42:16+00:00
last_activity: 2021-09-15T04:28:38+00:00
last_author: "cnl"
sticky: false
locked: false
post_count: 10
---

<div class="post" data-post-id="39375" data-author="Gorka" data-date="2020-02-27T13:42:16+00:00" data-subject="Junk protection">

I accidentally junked my spear of pestilence today, after noticing a wooden spear in inv, and typing "junk spear."

Thanks to Maniac I got it back, but I got to thinking how I can protect against it happening again. Some people just don't junk things. Well, that's not really practical... if you run areas like EU where most of the mobs are astrals, and all the items drop to the ground and you have to use "get all" to sift through them. Dropping them instead of junking them only leads to massive piles of crap at the mob for the next pop, and the game performance is effected by the amount of objects in memory after a while. Here is how you can code around it with mudlet...

Pattern: ^junk(.+)$

Proc:

if matches[2] == " spear" then

 echo("DO NOT JUNK!!")

elseif matches[2] == " winter" then

 echo("DO NOT JUNK!!")

elseif matches[2] == " hell" then

 echo("DO NOT JUNK!!")

elseif matches[2] == " blade" then

 echo("DO NOT JUNK!!")

elseif matches[2] == " sword" then

 echo("DO NOT JUNK!!")

elseif matches[2] == " souls" then

 echo("DO NOT JUNK!!")

elseif matches[2] == " elite" then

 echo("DO NOT JUNK!!")

elseif matches[2] == " sphairai" then

 echo("DO NOT JUNK!!")

else

 send("junk"..matches[2])

end

Now this is fairly light protection... theoretically you could grab matches[2], then "names" it to get the full item name... ie, names matches[2] then match it against a list of items names you aren't allowed to junk, or store the names of your items in a database table. That would be the ultimate protection. However those items which you usually have in inv, like weapons, keychains, flux etc you could protect quickly with this approach.

Ideally the game wouldn't allow you to junk PERSONAL items, or items with a rune/clasp attached... forcing you to abandon them on the ground or drop them at the dump to get rid of them.

</div>

<div class="post" data-post-id="39376" data-author="Filk" data-date="2020-02-28T02:50:10+00:00" data-subject="Re: Junk protection">

Ideally, there should be standart confirmation question after junking personal item

</div>

<div class="post" data-post-id="39377" data-author="Bandit" data-date="2020-02-28T16:10:52+00:00" data-subject="Re: Junk protection">

Maybe a "junk!" command for personal items? Just like some other things require the ! as a confirmation of something that can't be reversed.

</div>

<div class="post" data-post-id="39378" data-author="*teker*" data-date="2020-03-02T19:07:37+00:00" data-subject="Re: Junk protection">

So thinking along these lines, would it also make sense to protect against:

\- drop

\- give

\- sell

What items should be protected?

\- personal

\- items with clasps/runes

\- items in eqsets

\- containers with any of the above items inside

</div>

<div class="post" data-post-id="39379" data-author="Gorka" data-date="2020-03-03T06:36:16+00:00" data-subject="Re: Junk protection">

> <strong>\*teker\* wrote:</strong>
> So thinking along these lines, would it also make sense to protect against:
> 
> \- drop
> 
> \- give
> 
> \- sell
> 
> 
> 
> What items should be protected?
> 
> \- personal
> 
> \- items with clasps/runes
> 
> \- items in eqsets
> 
> \- containers with any of the above items inside

Not sure about protecting against, drop, give and sell... and these options don't destroy the item anyway, so they are less harmful. How else would one drop the bag of merchandise from quickling king for example, while trying to load a haste book. Would need to allow giving personal items anyway for quests. Sell is already blocked if I recall correctly, unless it's a drachma item. So I'd suggest nothing here.

\>What items should be protected?

\- personal - YES

\- items with clasps/runes - YES

\- items in eqsets - Hmm, bare in mind some items you don't want to junk aren't in eq sets.

\- containers with any of the above items inside - Already can't junk containers with items inside.

Just stopping the junking of items with clasps / runes or personal items would go 95% of the way. Not sure the other 5% (eqset items) is worth the work and most valuable eqset items would be covered with runes or clasps anyway. The benefit is, once coded, imms don't have to be involved with reimbursement which must be a bit of a nuisance.

Implementing a confirmation to junk for certain items, isn't a bad idea, but seems a lot of work for little benefit.

</div>

<div class="post" data-post-id="39380" data-author="*teker*" data-date="2020-03-03T17:24:04+00:00" data-subject="Re: Junk protection">

> <strong>Gorka wrote:</strong>
> Not sure about protecting against, drop, give and sell... and these options don't destroy the item anyway, so they are less harmful. How else would one drop the bag of merchandise from quickling king for example, while trying to load a haste book.

I'm thinking we'd implement drop!, give!, sell!, etc just like junk! that would bypass protection (if protection is desired).

</div>

<div class="post" data-post-id="39381" data-author="*Breeze*" data-date="2020-03-04T18:41:48+00:00" data-subject="Re: Junk protection">

Good idea teker

</div>

<div class="post" data-post-id="39413" data-author="*teker*" data-date="2020-04-01T14:14:09+00:00" data-subject="Re: Junk protection">

Version 1 of this feature went live with the reboot yesterday. Help IPROTECT.

</div>

<div class="post" data-post-id="39414" data-author="Gorka" data-date="2020-04-01T15:53:29+00:00" data-subject="Re: Junk protection">

\>IPROTECT

ILIKEIT Teker!

I wondered if the immortals and builders might consider adding a blank no effects clasp to the game which attaches to anything, so that we might be able to attach it to things like our drinking containers and key chains to protect those also. There maybe other solutions to this problem through item personalization (may create exploits though), or through cursing them, or options in eqset, but the clasp idea... if it were possible to attach this to anything, it would allow us to protect any item of subjective importance, not just what is deemed valuable. Also another thing to cycle... and probably very easy to create and zone as a clasp in the game.

</div>

<div class="post" data-post-id="39821" data-author="cnl" data-date="2021-09-15T04:28:38+00:00" data-subject="Re: Junk protection">

good news.

the clasps in Kings Bazaar are very non discriminating about what you attach them to (except the fruit one). put some on my flask of fury and a gold sack.

iprotect works very well.

</div>
