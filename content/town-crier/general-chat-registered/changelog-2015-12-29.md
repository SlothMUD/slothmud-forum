---
title: "Changelog 2015-12-29"
topic_id: 4567
author: "*teker*"
date: 2015-12-29T15:55:30+00:00
last_activity: 2016-01-13T20:43:34+00:00
last_author: "*teker*"
sticky: false
locked: false
post_count: 8
---

<div class="post" data-post-id="36391" data-author="*teker*" data-date="2015-12-29T15:55:30+00:00" data-subject="Changelog 2015-12-29">

Some minor bugfixes:

366\) Wed Oct 28 07:08:27 2015 Ozzy 11011

 Parry seems to NOT working with Spirit Hammer!

Can someone test this for me? I think it's fixed but I need someone to verify.

380\) Wed Nov 4 07:26:13 2015 Taron 23225

 when fighting librarian-old-bard in lirgea I get Librarian bleeding in after some of the rounds

I found this in the code that summons other mobs and fixed it. Hopefully it'll fix most of the bleeds/extra garbage that people see. Keep bugging those with details and I'll try to find any more that remain.

398\) Tue Nov 24 06:17:16 2015 Fluffy 90145

 when you cast supplicatiion and type mob with first letter in uppercase, it

dont recognize it. Like Eudaemon instead of eudaemon. Found when was directly

399\) Tue Nov 24 06:17:24 2015 Fluffy 90145

 when was directly copypa from help file

Fixed.

The code that prevents you from leveling secondary classes higher than prime is in now. Same goes for the newbie graveyard change. Anyone playing 15/16+ characters will no longer see this benefit.

</div>

<div class="post" data-post-id="36392" data-author="Dragoth" data-date="2015-12-29T16:13:37+00:00" data-subject="Re: Changelog 2015-12-29">

\<901hp 628ma 369mv\>save

Connected to host slothmud.org

Connected to host slothmud.org

Connected to host slothmud.org

Connected to host slothmud.org

save

Connected to host slothmud.org

save

Connected to host slothmud.org

</div>

<div class="post" data-post-id="36395" data-author="*teker*" data-date="2015-12-30T02:58:59+00:00" data-subject="Re: Changelog 2015-12-29">

Was that during my test this morning that caused an infinite loop, or something else?

I forgot to mention that I also fixed the maneuver code so that change messages are shown while sleeping.

</div>

<div class="post" data-post-id="36397" data-author="*juggleblood*" data-date="2015-12-30T15:51:16+00:00" data-subject="Re: Changelog 2015-12-29">

Regarding the bleeds, I have seen a few recently. It always seems to be after I've been in the pit and handled a lot of coliseum potions. I see a class abbrev on an empty line, usually bard, i.e.

Ba

</div>

<div class="post" data-post-id="36399" data-author="Yasik" data-date="2015-12-31T09:22:27+00:00" data-subject="Re: Changelog 2015-12-29">

> <strong>\*teker\* wrote:</strong>
> Some minor bugfixes:
> 
> 366\) Wed Oct 28 07:08:27 2015 Ozzy 11011
> 
> Parry seems to NOT working with Spirit Hammer!
> 
> 
> 
> Can someone test this for me? I think it's fixed but I need someone to verify.

A red rakasha misses you with its claw.

A red rakasha misses you with its claw.

You skillfully parry the attack of a red rakasha.

A red rakasha misses you with its sting.

You massacre a red rakasha to small fragments with your pound.

You massacre a red rakasha to small fragments with your pound.

A red rakasha utters the words, 'yufzbarr'

\<1164hp 524ma 261mv\> \>\> 71 \<\< +9 -10.5 2,020,132,009 227,012 indoors Hellwell

You skillfully parry the attack of a red rakasha.

A red rakasha misses you with its claw.

A red rakasha misses you with its sting.

A red rakasha misses you with its sting.

You massacre a red rakasha to small fragments with your pound.

A red rakasha utters the words, 'yufzbarr'

The pitiful creature before you tries to burn you.

\<1145hp 527ma 264mv\> \>\> 65 \<\< +9 -10.5 2,020,132,063 227,012 indoors Hellwell

eq

You are using:

\<used as light\> the symbol of the dark lord (with a flawed glowing gem attached to it)

\<worn on finger\> a heavy iron ring

\<worn on finger\> a heavy iron ring

\<worn around neck\> an amulet of protection..It emits a faint humming sound!

\<worn on shoulders\> frosty white shoulder guards

\<worn on body\> Adamantine Cuirass of the Ancients

\<worn on head\> spiked helm of black steel..It emits a faint humming sound!

\<worn on legs\> the greaves of the forsaken..It emits a faint humming sound!

\<worn on feet\> black orcskin boots..It emits a faint humming sound!

\<worn on hands\> devilskin gauntlets..It emits a faint humming sound!

\<worn on arms\> polished rock sleeves

\<worn as shield\> a heavy greatshield..It emits a faint humming sound!

\<worn about body\> an adamantite-plated knight's war robe (with a golden, eight-pointed star (General) attached to it)

\<worn about waist\> a feathered cincture

\<worn around wrist\> a blue steel bracelet

\<worn around wrist\> a blue steel bracelet

\<wielded\> a glowing hammer

\<held\> a battered silver medallion..It has a soft glowing aura!

The mob is ethereal. I guess its working now, thanks for fix.

</div>

<div class="post" data-post-id="36403" data-author="Teron" data-date="2016-01-01T09:08:30+00:00" data-subject="Re: Changelog 2015-12-29">

You can parry ethers w/o a hammer now:

You skillfully parry the attack of the kobold ghost king.

Your riposte viciously massacres the kobold ghost king.

The kobold ghost king pierces you extremely hard.

Your hit passes right through the kobold ghost king!

Your hit passes right through the kobold ghost king!

Noticed it earlier on an ether dragon too.

</div>

<div class="post" data-post-id="36405" data-author="*teker*" data-date="2016-01-04T03:05:07+00:00" data-subject="Re: Changelog 2015-12-29">

The fix will be in the next build. Enjoy the bonus until then!

</div>

<div class="post" data-post-id="36464" data-author="*teker*" data-date="2016-01-13T20:43:34+00:00" data-subject="Re: Changelog 2015-12-29">

Today's reboot should have fixed the bleed caused by MAX-attribute potions wearing off. They should display the same message that plus-attribute potions display. This was the one JB mentioned above which would print out a class string like "Ba" or "Dr" on a blank line.

Let us know if you see any more of this type of thing.

There are also some additional changes made under the covers that you probably won't notice.

</div>
