---
title: "Changelog 2019-05-21"
topic_id: 4911
author: "*teker*"
date: 2019-05-21T14:02:46+00:00
last_activity: 2019-05-30T08:23:04+00:00
last_author: "Filk"
sticky: false
locked: false
post_count: 8
---

<div class="post" data-post-id="39197" data-author="*teker*" data-date="2019-05-21T14:02:46+00:00" data-subject="Changelog 2019-05-21">

With yesterday's crash a few things went in.

Mirror Image: Mages can now specify how many images they want to cast in a single spell.  The cap is still the same and masterful yields one extra.  Mana cost should be the same and the game is nice so that if you specify more than your cap, it only casts up to the cap and only charges for the new images.

A bunch of changes went in behind the scenes regarding item procs to make it easier for builders to write special items.  This involved a complete rewrite of "use" and "quaff".  I've left recite alone thus far so that if something breaks you can still recall.  Part of this was to make it easier to create a forge item to take players to the rebirth shop.

</div>

<div class="post" data-post-id="39198" data-author="Gorka" data-date="2019-05-21T16:39:07+00:00" data-subject="Re: Changelog 2019-05-21">

I would appreciate more items which transfer players to different zones if the code has helped enable that, much along the lines of blood filled diamond, pink invitation. Ideal candiates... Moors of Grv on Island (long), Onyx Tower AH (long, somewhat dangerous), BH volcano (fly issue), Solar in Ether Plane (conjunction of 6 areas)... Demonweb (long), Ogres (awkward)... very very useful. They all have something either silly or long about the runs at the moment.

</div>

<div class="post" data-post-id="39199" data-author="*teker*" data-date="2019-05-21T19:46:59+00:00" data-subject="Re: Changelog 2019-05-21">

Also forgot to mention - Eu is now perma chop/temp items.  Whether it says so under "time" or not.  It should be functioning the same as Lyme moving forward.

</div>

<div class="post" data-post-id="39201" data-author="*teker*" data-date="2019-05-22T14:01:29+00:00" data-subject="Re: Changelog 2019-05-21">

Also - future eq list dumps (starting now) will list proc names with the items.  It may not be intuitive what the proc does, but you'll know that the item has one or more.

</div>

<div class="post" data-post-id="39202" data-author="*teker*" data-date="2019-05-22T16:10:41+00:00" data-subject="Re: Changelog 2019-05-21">

Oh yeah - forgot to mention that I changed the proc code in how it handles clasps and runes with procs.  So that fancy clasp with the damage proc should fire now even if the equipment has a rune on it.  Let me know if there are any strange side effects.

</div>

<div class="post" data-post-id="39203" data-author="*Idjit*" data-date="2019-05-24T00:36:55+00:00" data-subject="Re: Changelog 2019-05-21">

Are we going to see some of the information exposed in the new EQlist dump, also exposed in the Identify spell when cast on a proc weapon.

Silly question but wondering if there would then be a parallel development there.

--D

</div>

<div class="post" data-post-id="39205" data-author="*teker*" data-date="2019-05-28T19:18:08+00:00" data-subject="Re: Changelog 2019-05-21">

I've added a lesser amount of info to the identify spell for procs.

There will also be a fix at next reboot for mirror image.  It's behaving incorrectly when the mage's mana is low.

</div>

<div class="post" data-post-id="39206" data-author="Filk" data-date="2019-05-30T08:23:04+00:00" data-subject="Re: Changelog 2019-05-21">

> ***teker* wrote:**
> Also - future eq list dumps (starting now) will list proc names with the items.  It may not be intuitive what the proc does, but you'll know that the item has one or more.

Changed eq list site to display such procs on weapons.

</div>
