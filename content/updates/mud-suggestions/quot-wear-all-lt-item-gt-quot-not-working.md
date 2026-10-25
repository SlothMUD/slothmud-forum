---
title: "&quot;wear all.&lt;item&gt;&quot; not working?"
topic_id: 4543
author: "Yasik"
date: 2015-11-24T09:41:39+00:00
last_activity: 2015-12-09T11:21:15+00:00
last_author: "*Breeze*"
sticky: false
locked: false
post_count: 12
---

<div class="post" data-post-id="36206" data-author="Yasik" data-date="2015-11-24T09:41:39+00:00" data-subject="&amp;quot;wear all.&amp;lt;item&amp;gt;&amp;quot; not working?">

Is it I do something wrong or "all." feature do not apply to "wear all"? Can we have this fixed anytime soon, please?

<112hp 156ma 97mv>  >> - <<  -4   1.0   67637   14733   indoors   Newbatia

buy sky

Marta the librarian tells you 'Here you go honey. It's courtesy of the guilds.'

You now have a sky blue spellbook.

<112hp 156ma 98mv>  >> - <<  -4   1.0   67637   14733   indoors   Newbatia

rest

You sit down and rest your tired bones.

<112hp 156ma 98mv>  >> - <<  -4   1.0   67637   14733   indoors   Newbatia

rem all.chain

You stop using a gold chain.

You stop using a gold chain.

<112hp 156ma 99mv>  >> - <<  -4   1.6   67637   14733   indoors   Newbatia

wea all.pendant

You do not seem to have the 'all.pendant'.

<112hp 156ma 101mv>  >> - <<  -4   1.6   67637   14733   indoors   Newbatia

i

You are carrying:

a gold chain [2]

a sky blue spellbook..It emits a faint humming sound!

a canteen

a small gold bird pendant [2]

a dwarvish recall scroll [2]

a forest green wreath

an ether-coated ticket

a minor scroll of recall

a backpack

a pair of rose colored glasses

<112hp 156ma 102mv>  >> - <<  -4   1.6   67637   14733   indoors   Newbatia

wear all.pendant

You do not seem to have the 'all.pendant'.

<112hp 156ma 104mv>  >> - <<  -4   1.6   67637   14733   indoors   Newbatia

Marta the librarian says 'Ah, a seeker of knowledge.  Welcome to our humble library!'

<112hp 156ma 105mv>  >> - <<  -4   1.6   67637   14733   indoors   Newbatia

wear pendant

You wear a small gold bird pendant around your neck.

<112hp 156ma 107mv>  >> - <<  -4   1.6   67637   14733   indoors   Newbatia

wear pendant

You wear a small gold bird pendant around your neck.

<112hp 156ma 107mv>  >> - <<  -4   1.6   67637   14733   indoors   Newbatia

</div>

<div class="post" data-post-id="36207" data-author="Marvel" data-date="2015-11-24T21:22:40+00:00" data-subject="Re: &amp;quot;wear all.&amp;lt;item&amp;gt;&amp;quot; not working?">

wear all.<item> has never worked before for me. Likely it just hasn't been coded in.

</div>

<div class="post" data-post-id="36208" data-author="Teron" data-date="2015-11-25T07:19:39+00:00" data-subject="Re: &amp;quot;wear all.&amp;lt;item&amp;gt;&amp;quot; not working?">

Meanwhile, you can use this:

wear gold gold

</div>

<div class="post" data-post-id="36218" data-author="*teker*" data-date="2015-11-28T20:33:07+00:00" data-subject="Re: &amp;quot;wear all.&amp;lt;item&amp;gt;&amp;quot; not working?">

I purposely skipped doing this one because of the current behavior of allowing wear <item1> <item2> <item3>.  For some reason I thought the required changes might break backwards compatibility but I can look at it again to make sure.  It does stand out now that I've enabled the functionality for drop, remove, and sell.

</div>

<div class="post" data-post-id="36231" data-author="Josiah" data-date="2015-12-01T19:02:23+00:00" data-subject="Re: &amp;quot;wear all.&amp;lt;item&amp;gt;&amp;quot; not working?">

What?!?  I can 'sell all.hex' ???  You truly are a god!

Lately I've taken to dropping them in town.  There's probably a streetsweeper roaming around bh with his inventory full of tokens right now!

</div>

<div class="post" data-post-id="36235" data-author="*teker*" data-date="2015-12-03T03:59:28+00:00" data-subject="Re: &amp;quot;wear all.&amp;lt;item&amp;gt;&amp;quot; not working?">

Sell all.spellbook is useful also.

I went ahead and added the code for "wear all.item".  It'll be in whenever we put up the next build.  It still allows you to specify multiple items so that commands like "wear bracelet all.ring helmet" will attempt to wear 1 bracelet, all rings, and 1 helmet from inventory.

</div>

<div class="post" data-post-id="36255" data-author="Yasik" data-date="2015-12-05T11:12:12+00:00" data-subject="Re: &amp;quot;wear all.&amp;lt;item&amp;gt;&amp;quot; not working?">

I hope that build goes live soon, bc atm it works as it alwayes worked before.

Thanks for taking care of it, Teker.

eq

You are using:

<used as light>      the symbol of the dark lord (with a flawed glowing gem attached to it)

<worn on finger>     a crystal ring..It has a soft glowing aura!

<worn on finger>     a crystal ring..It has a soft glowing aura!

<worn around neck>   a purple dragon's claw..It has a soft glowing aura!

<worn around neck>   a purple dragon's claw..It has a soft glowing aura!

<worn on body>       a woven cloth shirt

<worn on head>       crown of the quickling king

<worn on legs>       a pair of black riding pants

<worn on feet>       boots of radiance

<worn on hands>      a pair of durs-hide gloves

<worn on arms>       a pair of singing sleeves..It emits a faint humming sound!

<worn as shield>     a runed shield of the moon..It has a soft glowing aura!

<worn about body>    an adamantite-plated knight's war robe (with a golden, eight-pointed star (General) attached to it)

<worn about waist>   a circle of flames..It emits a faint humming sound!

<worn around wrist>  a dragonskin bracelet..It has a soft glowing aura!

<worn around wrist>  a dragonskin bracelet..It has a soft glowing aura!

<wielded>            Brilliant Sword of Valor..It emits a faint humming sound!

<held>               a crystal teardrop..It has a soft glowing aura!

<1089hp 647ma 405mv>   >> - <<   +9   -0.3   1,121,933,871   1,246,784   indoors   Hellwell

rem all.ring

You stop using a crystal ring.

You stop using a crystal ring.

<1089hp 647ma 405mv>   >> - <<   +9   -0.3   1,121,933,871   1,246,784   indoors   Hellwell

wear all.ring

You do not seem to have the 'all.ring'.

<1089hp 647ma 404mv>   >> - <<   +9   -0.3   1,121,933,871   1,246,784   indoors   Hellwell

i

You are carrying:

a crystal ring [2]..It has a soft glowing aura!

a major scroll of recall [5]

a decanter of endless water

swirling black and red robes

a multi-colored crystal rod

<1089hp 647ma 405mv>   >> - <<   +9   -0.3   1,121,933,871   1,246,784   indoors   Hellwell

wear all.ring

You do not seem to have the 'all.ring'.

<1089hp 647ma 405mv>   >> - <<   +9   -0.3   1,121,933,871   1,246,784   indoors   Hellwell

wear ring

You slide a crystal ring onto your left finger.

<1089hp 647ma 405mv>   >> - <<   +9   -0.3   1,121,933,871   1,246,784   indoors   Hellwell

wear ring

You slide a crystal ring onto your right finger.

</div>

<div class="post" data-post-id="36273" data-author="*teker*" data-date="2015-12-08T02:33:37+00:00" data-subject="Re: &amp;quot;wear all.&amp;lt;item&amp;gt;&amp;quot; not working?">

This went live Sunday morning after the reboot.

</div>

<div class="post" data-post-id="36276" data-author="Teron" data-date="2015-12-08T08:57:47+00:00" data-subject="Re: &amp;quot;wear all.&amp;lt;item&amp;gt;&amp;quot; not working?">

Thanks.

It means I can replace

wear forge forge many other items hit space limit for wear command

wear have to use another wear command

with

wear all.forge all.ring item5 item7 more items one command hooray

Speaking of which.

Would it be terribly hard to increase the character limit in the wear command? It'd give me more freedom to remove the extra wear command from an alias (not that it matters much, but still).

Thanks again.

</div>

<div class="post" data-post-id="36279" data-author="*Breeze*" data-date="2015-12-09T08:43:47+00:00" data-subject="Re: &amp;quot;wear all.&amp;lt;item&amp;gt;&amp;quot; not working?">

input buffer is already huge.  i doubt we make it bigger..

</div>

<div class="post" data-post-id="36280" data-author="Filk" data-date="2015-12-09T09:01:53+00:00" data-subject="Re: &amp;quot;wear all.&amp;lt;item&amp;gt;&amp;quot; not working?">

How about extra 50 letters? On some long eq change chains its *near* enough for whole set. But sometimes it is not, so you have to dance around that limitation to pick up some unique item keyword not messing with other items. Extra 30-50 letters would solve that completely, at least to me :)

ps^ btw, would like to remind you about wwwpass, its still not connected to the site kinda.

</div>

<div class="post" data-post-id="36283" data-author="*Breeze*" data-date="2015-12-09T11:21:15+00:00" data-subject="Re: &amp;quot;wear all.&amp;lt;item&amp;gt;&amp;quot; not working?">

yes i know about wwwpass.  i still need to redo all the www stuff

as for 30-50 char buffer increase, convince teker ;)

</div>
