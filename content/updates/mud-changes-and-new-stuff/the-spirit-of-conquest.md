---
title: "The Spirit of Conquest"
topic_id: 5022
author: "Driven"
date: 2021-06-21T22:13:50+00:00
last_activity: 2021-06-27T17:51:17+00:00
last_author: "Driven"
sticky: false
locked: false
post_count: 4
---

<div class="post" data-post-id="39739" data-author="Driven" data-date="2021-06-21T22:13:50+00:00" data-subject="The Spirit of Conquest">

Ladies and gentlemen, we offer you the Spirit of Conquest.  We will be rebooting the mud this afternoon to allow the code to go live, and the mud will need to be wizlocked for 30 minutes or so to get the Spirit of Conquest setup properly, as the commands required will lag the entire mud.  Fortunately this only needs to occur once, so once the object is properly initialized, we will release the wizlock and the conquest will begin.  

The Spirit of Conquest will be available via a quest, and it shouldn't be too terribly difficult to figure out who the quester is.  He is not friendly, so be careful.

The Spirit of Conquest enables two things--(1) An expansion of the Rebirth Shop, and (2) A new Conquest System that every player can enjoy, regardless of whether you are reborn.  

Because I think discovery is more fun than being told everything, I'll leave it at that.  Please see me ingame if you have any problems or issues.  Idjit and I have tested this thing quite a bit, but you never know what bugs are lurking.  I would be conservative with what equipment you part with over the first week so that the Spirit of Conquest can get some mileage under its belt.

</div>

<div class="post" data-post-id="39740" data-author="Driven" data-date="2021-06-22T02:25:39+00:00" data-subject="Re: The Spirit of Conquest">

There are indeed some bugs lurking with renting that we never saw on the test port.  I will debug tomorrow, so don't spend too much effort on this until this gets ironed out.

</div>

<div class="post" data-post-id="39742" data-author="Driven" data-date="2021-06-24T14:17:57+00:00" data-subject="Re: The Spirit of Conquest">

Code updates have been pushed to the game machine and reboot is scheduled for 9:30am server time (12:30pm EST).  Once I log back in after reboot, I will re-enable the Spirit of Conquest and off we go.  Here are a few answers to some FAQs.

1) Are there guaranteed to be no more bugs in the Spirit of Conquest?

No, but we are making significant forward progress.  Obviously a system that tracks every single mob and popped item in the mud, and "just works" when new areas are added, is a complicated system.  The updates for the code puts all of the personal data on the player now, which is a far more stable solution.

2) Why aren't certain mobs/eq showing up on 'look area'?

Mobs and equipment that spawn due to MUDL or built-in procs are not part of this system.  This system crawls the mud and finds zoned mobs and the equipment zoned to the mob.

3) What's the difference between "total conquest points" and "conquest points"?

"Total conquest points" is the value that you see when you "look conquerors".  This value represents the conquest points that you have earned over the life of your character and never goes down.  The intent with "total conquest points" is for the "look conquerors" to be a contest to see who is the strongest conqueror.  "Total conquest points" also determines your Title as a conqueror and the stats on the Spirit of Conquest itself.

"Conquest points" is the actual conquest points that you currently have on your character and can be spent in the Rebirth Shop.  This is the value that you see in your score screen.  This value goes down as you buy stats in the Rebirth Shop.

4) Why is the Spirit of Conquest zapping me (and falls off) when I try to attach it to a piece of worn equipment?

As of the writing of this post, the Spirit of Conquest is not yet approved, so once a 45+ is able to approve the item, this will go away.

5) Can we change the cost of certain things in the Rebirth Shop?

Talk with a creator.  :lol:

</div>

<div class="post" data-post-id="39745" data-author="Driven" data-date="2021-06-27T17:51:17+00:00" data-subject="Re: The Spirit of Conquest">

A few more answers to FAQs:

(6) Why do I get different conquest points for mobs than what I see in 'look area'?

When you turn in a corpse or subdue, the mob has been destroyed, and so information associated with that mob is also gone.  To get the information, I have to recreate the mob under the covers, get the information (such as xp, which is used in the formula for conquest points), and then purge the mob again.  When the mob is created in this way, you get the unaged version of the mob.  The 'look area' information that you see is highly optimized for speed of execution so that the mud doesn't lag.  One way in which I do that is to get the information off mobs that are already loaded (which may be aged), and so the conquest point calculation is based on the mob's aged xp.   This is all a consequence of not storing the conquest points in a data structure, but rather calculating them on the fly.  The former would produce so much data that the Spirit could eventually crash the mud.  Besides, recreating the mob on-the-fly ensures that everyone gets exactly the same conquest points regardless of how aged the mob is.

(7) Is the same true for ether/astral mobs?  What about eq?

Yes, even though I do have access to the mob at the moment of death, I purposefully create another copy to get the unaged xp.  Equipment is also based on unaged xp, as the conquest points for eq is stored in the data structures (a necessary evil), and those structures were created within the first 20 minutes after the initial boot wizlock.

(8) Does any of the above impact the 300m cap in the game?

No, that 300m was calculated using unaged mobs directly after a reboot.

</div>
