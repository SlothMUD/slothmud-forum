---
title: "Changelog 2019-03-02"
topic_id: 4893
author: "*teker*"
date: 2019-03-02T19:11:14+00:00
last_activity: 2019-03-18T16:06:25+00:00
last_author: "*Breeze*"
sticky: false
locked: false
post_count: 5
---

<div class="post" data-post-id="39107" data-author="*teker*" data-date="2019-03-02T19:11:14+00:00" data-subject="Changelog 2019-03-02">

I made some changes to eqset regarding clasps.  The code now tries to remove conflicting clasps before wearing new ones of the same category.  Performing an EQSET SWITCH will now remove clasps that are not in the set.  Also, if wielding a weapon is blocked due to strength, it will skip the weapon, finish switching gear, and then try again at the end in case your strength has been improved to wield the weapon.  I've also cleaned up how Holy Items show up in the lists.

The issue with shifted players bypassing some traps has been fixed.  Druids beware...

Some fixes also went in regarding the eqlist forge exports.

</div>

<div class="post" data-post-id="39112" data-author="*teker*" data-date="2019-03-04T16:23:55+00:00" data-subject="Re: Changelog 2019-03-02">

I forgot about the "boat" thing.  Prior to this weekend, effects created in rooms (brambles, fog, portals, and even docked ships) were timed on the game hour (tick).  That meant if you created one of these effects 1 second before the tick you lost 59 seconds of duration on the spell.  I've changed things so that the timing is now based on 10 second intervals - so worst case you lose 9 seconds on a spell.  I've also done some things to make this part of the code run more efficiently.

Along the same lines, I've made a number of internal changes regarding item procs that should not be visible during gameplay but with the goal of running them more efficiently.  I went ahead and tested choppers and other weapons pretty extensively but if you see any items behaving strangely, please let me know.  There's a couple more steps involved in finishing this and in the end it'll allow our builders to write procs in an easier fashion (which means more custom items, cooler areas, etc).

</div>

<div class="post" data-post-id="39131" data-author="*teker*" data-date="2019-03-13T19:53:41+00:00" data-subject="Re: Changelog 2019-03-02">

Further changes today.  Most notable is a change in the mob pop algorithm where the same mob pops in multiple rooms.  It should fix the pupil problem mentioned here:  [<LINK_TEXT text="http://www.slothmud.org/forum/viewtopic ... 126#p39126">http://www.slothmud.org/forum/viewtopic.php?f=27&t=4892&p=39126#p39126</LINK_TEXT>](http://www.slothmud.org/forum/viewtopic.php?f=27&t=4892&p=39126#p39126) and may slightly change mob pop locations in other situations.  Let us know if you see strange behavior or mobs not popping where they should.

Also - I made a change to eqsets that was supposed to automatically upgrade rank clasps in sets when the player gains rank.  Gorka has reported an issue with his clasp not wearing correctly so I'll pull that code out for the next reboot.

A while back, I added EQSET STOW - here's help file text for it now.  It looks at any items in inventory with a specified container and puts them away.

</div>

<div class="post" data-post-id="39135" data-author="*Idjit*" data-date="2019-03-17T21:16:12+00:00" data-subject="Re: Changelog 2019-03-02">

A funny thought about EQSET STOW is we could conceivably set select potions to setcontainer to the kangaroo pouch, and then type this to stow them at the end of a run.  However it must be said, at the time all these potions were created probably 97% of them don't have held-low in their wear flag and only 'take'.  (This being important because in order to setcontainer a potion to the pouch you'd have to 'equip' it to held-low for a split second).  I mean they were mostly created eons before eqset existed, so who knew?

We might go through and do this wear-flag modification for all the potions that used to load in the chaos-pit, such as radiant blues.

And then this might go for other pertinent item combiners like the tassled dice bag.

Perhaps a batch process could be done offline to add the 'hold' bit to their wear flag to a bunch of these things en masse.

Just a thought.

--Idj

</div>

<div class="post" data-post-id="39137" data-author="*Breeze*" data-date="2019-03-18T16:06:25+00:00" data-subject="Re: Changelog 2019-03-02">

> ***Idjit* wrote:**
> Perhaps a batch process could be done offline to add the 'hold' bit to their wear flag to a bunch of these things en masse.
> 
> Just a thought.
> 
> --Idj

dont take this the wrong way, but like my predecessors, i decree this will never be done offline.

sloth datafiles are .. touchy .. it would be easier to script wintin or mudlet to add the proper flags than to deal with all the things that could go wrong in an offline process.

when we (really splork) added level required to enter the zone restriction, we put the test mud into a crash loop before we realized that its just easier to do it online.

// F

</div>
