---
title: "Squelching ..."
topic_id: 988
author: "Firon"
date: 2005-03-29T15:18:32+00:00
last_activity: 2005-12-09T20:14:55+00:00
last_author: "Firon"
sticky: false
locked: false
post_count: 12
---

<div class="post" data-post-id="5306" data-author="Firon" data-date="2005-03-29T15:18:32+00:00" data-subject="Squelching ...">

Here are two scripts I worked up real quick other night for wintin95. May want to add shouts to it, too, but hopefully the imms would noshout the person by that point.  An alternate route with .net would be to send these to a window that was in the background instead of gagging them, not sure if the method has changed with .net version or not.

#alias {squelch} {#gag ^$1[;#gag ^$1 gossips--;#gag ^$1 auctions--;#gag ^$1 quests--;#gag ^$1 says;notell add $1}

#alias {squelch} {#ungag ^$1[;#ungag ^$1 gossips--;#ungag ^$1 auctions--;#ungag ^$1 quests--;#ungag ^$1 says;notell delete $1}

</div>

<div class="post" data-post-id="5307" data-author="Firon" data-date="2005-03-29T15:19:59+00:00" data-subject="&lt;---- newbie!">

well crap, forgot to change the second alias to {unsquelch} when i posted to the board.  :roll:

</div>

<div class="post" data-post-id="5308" data-author="Leaf" data-date="2005-03-29T16:04:22+00:00" data-subject="">

why not just re-type gos, auc, newb ???

</div>

<div class="post" data-post-id="5311" data-author="Deju" data-date="2005-03-29T19:39:39+00:00" data-subject="">

beacause this way you can squelch a particular player and still see the contents of a channel

</div>

<div class="post" data-post-id="5312" data-author="Autolycos" data-date="2005-03-29T20:10:51+00:00" data-subject="">

easy to squelch individuals that bug the crap out of ya...

notell leaf

muahhaha  :twisted:

</div>

<div class="post" data-post-id="5314" data-author="Leaf" data-date="2005-03-29T21:35:55+00:00" data-subject="">

Then y not just gag the player, then you won't see that player in goss, 

auc, or newb.

Auto I'm going to smack u!

</div>

<div class="post" data-post-id="5318" data-author="Clink" data-date="2005-03-30T02:51:32+00:00" data-subject="">

Uh, I completely gagged a particular player that was particularliy annoying. Turned out it wasn't such a good idea in hindsight since that person turned out to be a tank in my group where I was quickly assigned to a healo.  It was a bit embarrasing for me to admit to the group after I couldn't figure out why they were all ignoring me when I kept asking "who's the FRICKIN TANK?!?!"

Also was common practice to not gag people completely in the old days when there were more pthieves.

Nice script, btw.

</div>

<div class="post" data-post-id="5319" data-author="Weasel" data-date="2005-03-30T03:30:13+00:00" data-subject="">

hehe just visualized that one..

</div>

<div class="post" data-post-id="9749" data-author="Firon" data-date="2005-12-09T03:09:50+00:00" data-subject="gag different in .net?">

Okay, can't figure out why this doesn't work:

#defgroup {Gagger}

#alias  {gaga} {#gag {^$1 gossips};#gag {^$1 auctions};#gag {^$1 quests};#gag {^$1 shouts};notell add $1} {G|Gagger}

#alias  {rmgag} {#ungag {^$1 gossips};#ungag {^$1 auctions};#ungag {^$1 quests};#ungag {^$1 shouts};notell delete $1} {G|Gagger}

#defgroup {}

I want to anchor the gag so it only gets the originating message and not copies to gossip, etc but when i 'gaga example' and list gags I get:

#gag

#Defined gags:

{^$1 auctions}

{^$1 gossips}

{^$1 quests}

{^$1 shouts}

Any ideas?

</div>

<div class="post" data-post-id="9751" data-author="Malison" data-date="2005-12-09T04:32:59+00:00" data-subject="">

don't know if it makes a difference but I've always used ^%1 instead of ^$1

</div>

<div class="post" data-post-id="9752" data-author="12345" data-date="2005-12-09T06:47:38+00:00" data-subject="">

I forget it it's 95 or .net, but it sometimes gets goofy with layering.  Try it with $$ and see if it works.

</div>

<div class="post" data-post-id="9753" data-author="Firon" data-date="2005-12-09T20:14:55+00:00" data-subject="">

Well % had the same results but the double $ worked, apparently having a single $ following the carat confuses wintin. Thx for the suggestion Malison, and 12345 for the solution.

#defgroup {Gagger}

#alias  {gaga} {#gag {^$$1 gossips};#gag {^$$1 auctions};#gag {^$$1 quests};#gag {^$$1 shouts};notell add $1} {G|Gagger}

#alias  {rmgag} {#ungag {^$$1 gossips};#ungag {^$$1 auctions};#ungag {^$$1 quests};#ungag {^$$1 shouts};notell delete $1} {G|Gagger}

#defgroup {}

Has some flaws with edge cases but should work for 95% of people who are a little too chatty :)

</div>
