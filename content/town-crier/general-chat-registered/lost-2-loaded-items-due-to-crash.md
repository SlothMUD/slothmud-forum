---
title: "Lost 2 loaded items due to crash"
topic_id: 4649
author: "Teron"
date: 2016-07-08T08:51:25+00:00
last_activity: 2016-07-09T14:26:10+00:00
last_author: "Ker"
sticky: false
locked: false
post_count: 6
---

<div class="post" data-post-id="37028" data-author="Teron" data-date="2016-07-08T08:51:25+00:00" data-subject="Lost 2 loaded items due to crash">

Hello.

I'm cycling mobs that pop cps for the 6x40 jodhpurs and two of them (Tarogel and an armanite demon) were loaded before the crash and now the items are gone.

What could be done to keep the loaded items through crashes/reboots?

Is there a slim chance to load those items back on the mobs?

Thanks.

</div>

<div class="post" data-post-id="37029" data-author="Yasik" data-date="2016-07-08T10:09:40+00:00" data-subject="Re: Lost 2 loaded items due to crash">

Nothing personal, but we cannot lose something we dont own yet :)

Items on mobs are not players' property until they actually kill the mob, loot the item, and do save.

Not sure anyone will do what you asking. Back in my days I remember a case when a player lost ALL his eq in some kind of disaster and guess what, noone reimbursed him nothing. He ran eq-groups several weeks until he popped all his eq back from zero, including forges.

This of crash as "force majeure" that cannot be predicted or avoided. I understand your feelings.

</div>

<div class="post" data-post-id="37030" data-author="Teron" data-date="2016-07-08T14:00:59+00:00" data-subject="Re: Lost 2 loaded items due to crash">

Funny you've used the phrase, force majeure.

Let's dig in:

> **Wikipedia wrote:**
> Force majeure is generally intended to include occurrences *beyond the reasonable control* of a party, and therefore would not cover:
> 

1. >
2. 1. any result of the negligence or malfeasance of a party, which has a materially adverse effect on the ability of such party to perform its obligations;
>
3. 2. any result of the usual and natural consequences of external forces (for example, predicted rain stops an outdoor event); and
>
4. 3. any circumstances that are specifically contemplated (included) in the contract.

Crashes occur, not because a tornado hit the server (which would be a force majeure), but because the game code is not 100% perfect (1.) and needs fixing, which *Teker has proved to be possible* by reducing the rate of crashes recently, for which I'm sure we all thankful. Unless the hosting server was, indeed, hit by a sharknado, but this should be a negligible occurance.

Therefore, crashes are not unavoidable and are under full control of the immortals, therefore they are not force majeure, unless the server is powered by a dragon-heated power station and a Schroedinger's cat (I dunno, why the cat needs to admin the server, but why not). So unless we get any evidence of the crash, I don't see it as force majeure.

Moreover, it's known and publicly accepted that the game crashes in 8-10+ days of uptime (3.) (the recent uptime of 15 days was phenomenal, good work, Teker), therefore it can be predicted that the game will crash (2.).

Therefore, a crash is definitely not a force majeure.

I am not saying that crashes are particularly a malfeasance (again, Splork and Teker and doing what they can to keep the game up and I wish there were more ways to help), nor I demand that the game has 100% uptime, as I understand that:

- there will always be bugs, however small

- the server itself needs at least some downtime, if only for maintenance

- immorts need to reboot the servers to add stuff to the game.

As I see it, items disappearing from mobs is noticeable disruption of gameplay (worse than lags), leading to player dissatisfaction, when (s)he had put time and effort into popping the item (I actually killed the mobs before they loaded, check the logs). Age-less mobs mean that a leader won't start an exp group in 2-4 hrs since crash, unless there's a noticeable incentive or level of boredom involved.

So, since crashes are predictable (i.e., we can say that the game will crash or be rebooted in 15 days), I'd appreciate if there was something done to make crashes/reboots playable for the players by:

- saving the game state through crashes/reboots, at least in 5-15-30 min increments

- only saving the stuff that doesn't crash the game, such as approved items on mobs and on the ground (a filter can be made for junk below 300 coin value)

- whether the mob was/is alive and for how long should also be saved (yes, including the epics).

If the problem is with increased and/or exponential memory usage, then immorts can identify, what increases the usage and deal with it. I'm pretty sure the loaded items on mobs do not overload the server, maybe lots of junk on the floor does.

Funny enough, the suggested changes will kill any chance of popping anything on reboot, which I believe was the problem earlier, and that's why some items were made *not to load on reboots*?

So, to respond to the only comment so far:

> **Odin wrote:**
> 1. Items on mobs are not players' property until they actually kill the mob, loot the item, and do save.
> 
> 2. Not sure anyone will do what you asking. Back in my days ... noone reimbursed him nothing. ...
> 
> 3. This of crash as "force majeure" that cannot be predicted or avoided. I understand your feelings.

1. I never said the items were mine. I accept that if immorts put them back on the mobs, someone might kill them before me and forge the jodhpurs or try to sell them to or extort me. So be it. Losing pops you worked for is like losing a cheque. 

2. Since the dark ages of Sloth, when Ming was young and Dug was busy, a few cases of complete eq loss, a public dissatisfaction and a forum uproar, imms introduced a 20 item reimbursement rule. Later, they made possible complete reimbursements or char restorals, which I really appreciate, though I'm not sure I used the opportunity. Now even singular lost items can be reimbursed (which I did use, thank you very much), if you lost them due to a game glitch and are on good standing with the immort you talk to.

I believe this helps to keep players in the game, because they'd quit, if the lost their char eq, especially after 5-6x40. 

And I did lose all my char eq on my *first* char at 1x40, and I did recover, even with better eq. This is not possible to do within a reasonable time frame for a 6x40+ player, because (s)he uses high-end eq, for the most part, which is hard to make and you can't upgrade it by getting smth better.

3. Again, I believe I've proved beyond reasonable doubt that crashes are not a force majeure.

</div>

<div class="post" data-post-id="37031" data-author="*Splork*" data-date="2016-07-09T00:23:19+00:00" data-subject="Re: Lost 2 loaded items due to crash">

The game crashes, far less than it ever has in its 26+ year history.  We are finding ourselves forcing reboots more than we are crashing, due to our memory growth. This is an issue I have personally spent hundreds of hours trying to fix and also hundreds of my own dollars  having our code "audited" in an attempt to solve. While we do find some of the issues and correct them, anyone who has dealt with memory leaks knows its not something which can be fixed or figured out in an evening!

Either way, our policies in regards to reimbursing equipment have improved from the days of 1992, where no equipment was reimbursed to the present day where a good attitude and a polite request will get your entire player file backed up. Rita also added code years ago which gave creatures which were down at the time of crash the same possibility to load equipment once the MUD had resumed.  I think, overall, we are doing a really nice job of being fair and attempting to solve the many issues players have in this regards. 

Crashes will never go away for Sloth, that should not surprise anyone. If we stop crashing, it means we have no immortals and it most likely means we will have no players because our game has come to a complete stop in regards to development.  Honestly, when our game is crashing the most, I am personally quite happy because it means our Immortal staff is incredibly busy adding tons of great features and our players are actively playing and finding those bugs that we add. That sounds bad but I have been here for 25 years and its the truth:)

Anyways, sorry you were not able to pop the items. Better luck next time!

</div>

<div class="post" data-post-id="37033" data-author="Teron" data-date="2016-07-09T06:16:43+00:00" data-subject="Re: Lost 2 loaded items due to crash">

I understand that crashes can't and won't go away.

However, since crashes are inevitable, I suggest to keep the popped equipment on mobs, and possibly the loaded components that are worth something, to keep the game playable regardless of crashes.

What if we analyze, what players lose on crashes, such as:

- items, worth more, than 100k

- components, worth more, than 5k in shops or on the ground

and see, if they don't affect memory usage, to actually preserve them through crashes?

This might partly solve the problem if disappearing quality items from shops, which only few players bother to solve by auctioning the items instead of selling them to the shop.

If you really need to clean the memory, you could reboot without keeping the components and other junk, but the loaded items and more expensive, rarer items in the shops.

I'm sure there is some middle ground here to solve the problem.

</div>

<div class="post" data-post-id="37034" data-author="Ker" data-date="2016-07-09T14:26:10+00:00" data-subject="Re: Lost 2 loaded items due to crash">

Hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii Splork!! <3

R,

Dr!

</div>
