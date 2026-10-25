---
title: "Changelog 2017-03-25"
topic_id: 4747
author: "*teker*"
date: 2017-03-25T18:52:55+00:00
last_activity: 2017-03-30T02:24:02+00:00
last_author: "cyprimus"
sticky: false
locked: false
post_count: 14
---

<div class="post" data-post-id="38151" data-author="*teker*" data-date="2017-03-25T18:52:55+00:00" data-subject="Changelog 2017-03-25">

CHARACTER_LOCATAION and CHARACTER_EQUIPMENT should be working is MSDP.

A bunch of new code went in for the builders - they've got an exciting project going on.

I broke the BRIEF flag while attempting to fix some MSDP exploits.  That will be fixed in the next reboot.

Apparently people aren't getting messages indicating they are poisoned - that will also be fixed in the next reboot.

</div>

<div class="post" data-post-id="38153" data-author="Gorka" data-date="2017-03-26T10:31:18+00:00" data-subject="Re: Changelog 2017-03-25">

Teker, the amount of information in CHARACTER_EQUIPMENT is great, but I can't find a way to even make use of any of it. Do any commands work with SERIAL/VNUM or even SHORT_DESCRIPTION? The most useful value you can actually put in that array is the NAMES of the item.

I can't remove "Axe of Dwarvish Lords" but I can remove axe-dwarvish-lords. This would make the array actually useful... for example, in chop groups weapons often need changing, and you won't always have the same type of chopper each group... it would be nice to be able to remove msdp.CHARACTER_EQUIPMENT[16].NAMES as it's a pain in the butt to keep track of your weapon, especially if you are removing it to stab or grip on chopper runs or if your chopper keeps changing when you break them. My point is, you don't always actually know the name of the weapon you are wearing without looking sometimes.

Also is there a way to make the array referenced, rather than positional... for example... 

msdp.CHARACTER_EQUIPMENT["WIELDED"].NAMES

I guess we could just define our own arrays with the slot names from 0-17 but just thought I would ask.

After the crash it seems CHARACTER_LOCATION no longer updates except on "look" again, and before the crash I don't think it was updating for trig traps when you "pull chain" to enter coliseum or "sign ledger" at the weaver.

Yes, there is no longer a poison message, but I captured it in my msdp.AFFECTS array instead to get around it.

</div>

<div class="post" data-post-id="38155" data-author="Gorka" data-date="2017-03-26T14:48:04+00:00" data-subject="Re: Changelog 2017-03-25">

Another thing I have noticed... resting cancels the monk skill flurry... pretty sure that's new... and annoying for any monk who tries to keep this up while resting to take advantage of contemplation. Can it be fixed please?

</div>

<div class="post" data-post-id="38156" data-author="*teker*" data-date="2017-03-27T00:05:54+00:00" data-subject="Re: Changelog 2017-03-25">

The two crashes today were related to mobs shadow walking and the MSDP code for CHARACTER_LOCATION.  The fix should be in place after the 2nd crash.

Brief should be fixed.

Poison message should be fixed.

CHARACTER_LOCATION should be updating again but I can't remember if it made this reboot or if it'll be in the next one.

Concise is broken - will be fixed next reboot.

Seeing combat messages while sleeping should be fixed next reboot.

Arcane focus should be logging successful uses after next reboot.

I'll consider what to do next with CHARACTER_EQUIPMENT to make the information useful.

</div>

<div class="post" data-post-id="38157" data-author="Teron" data-date="2017-03-27T08:17:44+00:00" data-subject="Re: Changelog 2017-03-25">

1. choppers have keyword 'chopper' in them.

You only need to know the chopper name, if you hand out specs or pick it from the ground.

2. Before any major switches, I remove 3 weapons:

- chopper

- stab weapon

- hammer

so I don't have to dive into my robe to fish them out.

I agree, "remove weapon" would've made it simpler.

However, making the auction accept multiple items in a batch is much more important, than this, in my opinion.

P.S. Thanks to whoever fixed Macuahuitl's keyword. I had to use a hack to go around it, when handing out specs on broken macus.

</div>

<div class="post" data-post-id="38159" data-author="*Breeze*" data-date="2017-03-27T09:22:32+00:00" data-subject="Re: Changelog 2017-03-25">

> **Teron wrote:**
> However, making the auction accept multiple items in a batch is much more important, than this, in my opinion.

that is 100% not going to happen at least not by me.

Teker or Splork is welcome to code a new auctioneer that can support "lots"

but I don't have the time to code/test a whole new auctioneer.

</div>

<div class="post" data-post-id="38164" data-author="Teron" data-date="2017-03-28T03:16:53+00:00" data-subject="Re: Changelog 2017-03-25">

I didn't imply that you'd do it, Breeze. I remember you saying you weren't touching it, which is why I suggested it to Teker.

</div>

<div class="post" data-post-id="38166" data-author="*Breeze*" data-date="2017-03-28T03:59:15+00:00" data-subject="Re: Changelog 2017-03-25">

i already asked him to.  

in fact i suggested he use the vault code as a starting point.

</div>

<div class="post" data-post-id="38167" data-author="Teron" data-date="2017-03-28T04:06:07+00:00" data-subject="Re: Changelog 2017-03-25">

Cool beans!

</div>

<div class="post" data-post-id="38168" data-author="*Breeze*" data-date="2017-03-28T04:15:47+00:00" data-subject="Re: Changelog 2017-03-25">

iirc i asked him to do a postmaster also

its just if he wants to / gets around to doing it.

i have some special code i am working on for Neptune atm

</div>

<div class="post" data-post-id="38181" data-author="*teker*" data-date="2017-03-29T02:15:18+00:00" data-subject="Re: Changelog 2017-03-25">

> **Quote:**
> Another thing I have noticed... resting cancels the monk skill flurry...

I don't see it in rest, but I do see it when switching weapons.

</div>

<div class="post" data-post-id="38182" data-author="Gorka" data-date="2017-03-29T05:19:37+00:00" data-subject="Re: Changelog 2017-03-25">

Definitely a gremlin in here somewhere Teker... 100% repeatable. You can catch me in game if you need. Pretty sure this never used to happen but not entirely sure. Maybe it's just dropping from MSDP.AFFECTS... since you've been modding that code recently.

<944hp 468ma 249mv 3290526291xp -8.3ac -%>

GREATER FLUIDITY    	 8:18

SUPPLICATION        	 0:17

RESIST WEBS         	10:38

PETRIFIED ARMOR     	 1:05

BLESSING OF THE AVATAR	57:15

REJUVENATION        	27:34

PERCEPTION          	20:11

AVATAR SIGHT        	20:11

FLURRY              	 0:16

AEGIS               	 1:26

IMPROVED HASTE      	 3:43

You sacrifice the corpse to Krom.

<949hp 470ma 252mv 3290526291xp -8.3ac -%>

You sit down and rest your tired bones.

<950hp 471ma 253mv 3290526291xp -8.3ac -%>

GREATER FLUIDITY    	 8:17

SUPPLICATION        	 0:16

RESIST WEBS         	10:37

BLESSING OF THE AVATAR	57:14

PETRIFIED ARMOR     	 1:04

PERCEPTION          	20:10

AVATAR SIGHT        	20:10

REJUVENATION        	27:33

AEGIS               	 1:25

IMPROVED HASTE      	 3:42

</div>

<div class="post" data-post-id="38187" data-author="*teker*" data-date="2017-03-29T14:17:27+00:00" data-subject="Re: Changelog 2017-03-25">

Oh yeah, I found it somewhere else.  It does remove flurry, counter attack, and tumbling defense if you rest, sit, sleep, get stunned, etc.  I don't think it's anything new.

</div>

<div class="post" data-post-id="38190" data-author="cyprimus" data-date="2017-03-30T02:24:02+00:00" data-subject="Re: Changelog 2017-03-25">

Its not new

</div>
