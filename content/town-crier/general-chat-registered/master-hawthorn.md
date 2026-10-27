---
title: "Master Hawthorn"
topic_id: 5070
author: "Insomnia"
date: 2022-08-26T20:01:34+00:00
last_activity: 2024-01-22T01:42:07+00:00
last_author: "Driven"
sticky: false
locked: false
post_count: 23
---

<div class="post" data-post-id="39968" data-author="Insomnia" data-date="2022-08-26T20:01:34+00:00" data-subject="Master Hawthorn">

(Since only immortals have the rights to post in Mud changes and New Stuff, I'll post here.)

I really like these new tiny autoquests! I already managed to get a couple drachma, a 100k conquest points and a million coins from Hawthorn. <img src="/images/smilies/icon_cool.svg" alt="8)" title="8)" width="15" height="15" class="smiley nozoom"> A suggestion: how about a ranking system? I personally don't really need coins, conquest points, or drachma, but I know a list of scores will motivate me to log in and complete a bounty or two, on a daily basis. I guess there are other people like me, so...

</div>

<div class="post" data-post-id="39969" data-author="Ezekiel" data-date="2022-08-27T21:26:48+00:00" data-subject="Re: Master Hawthorn">

See below, found a bug, probably due to lack of difficulty level on paladin subdue. It gave max rewards plus some based on the tier:

list

\-----------------------------------------------------------------------------------------------------

Master Hawthorn smiles brightly and greets you, saying

 'Welcome fine hero, I hope that you are well! Here are the

 bounties that I am offering at the moment.'

\-----------------------------------------------------------------------------------------------------

 [Available] [1-5m] Daily subdue: an orangutan librarian (difficulty: 1)

 [Available] [5-10m] Daily subdue: an obnoxious peddler (difficulty: 2)

 [Available] [10-100m] Daily subdue: the paladin of flame (difficulty: ??)

 [Available] Weekly forge: a pair of mosaic boots (difficulty: 4)

 [Available] Quarterly forge: the Iolite of Omah (difficulty: 15)

\-----------------------------------------------------------------------------------------------------

 To turn in one of the bounties, simply type 'offer hawthorn \<itemName\>'.

 For example, 'offer hawthorn devilskin', or

 'offer hawthorn subdued'.

Rewards are scaled according to the difficulty of the bounty.

\-----------------------------------------------------------------------------------------------------

 [1-5m] Daily subdue: 0.5k-2.5k honor, 1k-5k conquest, 10k-50k gold, 10% chance 1 drachma.

 [5-10m] Daily subdue: 2.5k-5.0k honor, 5k-10k conquest, 50k-100k gold, 17% chance 1 drachma.

 [10-100m] Daily subdue: 5k-50k honor, 10k-100k conquest, 100k-1M gold, 33% chance 1 drachma.

 Weekly Forge: 10k-100k honor, 10k-100k conquest, 1-10 drachma.

 Quarterly Forge: 150k-200k honor, 150k-200k conquest, 50-75 drachma.

\-----------------------------------------------------------------------------------------------------

\<1079hp 370ma 394mv\> -9 \<-\>

offer hawthorn subdued

You offer a subdued paladin of flame to Master Hawthorn.

Master Hawthorn tells you 'Excellent work! Here is your reward!'

<strong>You receive 55000 honor points.</strong>

<strong>You receive 110000 conquest points.</strong>

<strong>You receive 1100000 gold coins.</strong>

</div>

<div class="post" data-post-id="39972" data-author="Insomnia" data-date="2022-09-04T15:59:11+00:00" data-subject="Re: Master Hawthorn">

It looks like difficulty can change for no obvious reason, feels a bit wrong.

```
[Available] [10-100m] Daily subdue: a wild baboon (difficulty: 1)

offer hawthorn subdued
You offer a subdued wild baboon to Master Hawthorn.
Master Hawthorn tells you 'Excellent work! Here is your reward!'
You receive 5000 honor points.
You receive 10000 conquest points.
You receive 100000 gold coins.

[Completed] [10-100m] Daily subdue: a wild baboon (difficulty: 1)

// a couple of hours later

[Completed] [10-100m] Daily subdue: a wild baboon (difficulty: 2)
```

Also, I haven't had a tier 3 subdue with difficulty higher than 4. Is it not random? I want to get 11 like Ezekiel!

</div>

<div class="post" data-post-id="39973" data-author="Driven" data-date="2022-09-04T18:20:49+00:00" data-subject="Re: Master Hawthorn">

Several things..

\- Difficulty on mobs is based on a real-time calculation using an actual instance of the mob, and Sloth has a lot of randomness built into the hps and xp of a mob, so if a given mob happens to be on the border of one difficulty and the next, it can fluctaute between two difficulties.

\- This is how you end up with difficulty 11 mobs, because the mob is right at the top end of difficulty 10 and randomness pushes the mob over the edge. Nice little bonus, so I have left it in there like that.

\- As far how mobs are chosen, it is not random, as I was keeping the amount of data stored on your character to a bare minumum. I believe the way the math works out is that the # of mobs in the kill-list for each tier is vast enough that you will likely not see the same mob until about 3 years from now. Doing it this way made it so that you are generally not at the mercy of the RNG gods, that if you stick with it, you will earn the same rewards as another player who sticks with it, which seemed more fair.

\- Yes, I am open to adding cool things like leader boards for the week/month/year/lifetime.

</div>

<div class="post" data-post-id="39978" data-author="Insomnia" data-date="2022-10-15T19:06:35+00:00" data-subject="Re: Master Hawthorn">

> <strong>Quote:</strong>
> I believe the way the math works out is that the # of mobs in the kill-list for each tier is vast enough that you will likely not see the same mob until about 3 years from now

Did you say 3 years?

```
grep "You offer a subdued Paladin of goodness to Master Hawthorn." -R ./2022*
./2022-09-28#19-20-00.txt:You offer a subdued Paladin of goodness to Master Hawthorn.
./2022-10-02#12-44-38.txt:You offer a subdued Paladin of goodness to Master Hawthorn.
./2022-10-15#17-42-40.txt:You offer a subdued Paladin of goodness to Master Hawthorn.
```

</div>

<div class="post" data-post-id="39980" data-author="Insomnia" data-date="2022-10-27T15:30:17+00:00" data-subject="Re: Master Hawthorn">

```
offer subdued hawthorn
You offer a subdued dark wizard to Master Hawthorn.
Master Hawthorn tells you 'Excellent work! Here is your reward!'
You receive 25000 honor points.
You receive 50000 conquest points.
You receive 500000 gold coins.
```

This is also not the first dark wizard I'm subduing for Hawthorn, the previous one was exactly 1 month ago (September, 27).

</div>

<div class="post" data-post-id="39982" data-author="Insomnia" data-date="2022-10-28T13:14:52+00:00" data-subject="Re: Master Hawthorn">

```
offer subdued hawthorn
offer subdued hawthorn
You offer a subdued Paladin of goodness to Master Hawthorn.
Master Hawthorn tells you 'Excellent work! Here is your reward!'
You receive 5500 honor points.
You receive 11000 conquest points.
You receive 110000 gold coins.
<1149/1149hp 3562/1178ma 417/423mv>
You offer a subdued Grblrg to Master Hawthorn.
Master Hawthorn tells you 'Excellent work! Here is your reward!'
You receive 15000 honor points.
You receive 30000 conquest points.
You receive 300000 gold coins.
```

Both turned in already, Paladin 13 days ago (see my post above), Grblrg 1 month ago (September, 28).

I'll stop spamming you, just know that something is broken there. <img src="/images/smilies/icon_cool.svg" alt="8)" title="8)" width="15" height="15" class="smiley nozoom">

</div>

<div class="post" data-post-id="39983" data-author="cnl" data-date="2022-10-29T23:39:48+00:00" data-subject="Re: Master Hawthorn">

Mr Haws is a pretty cool addition. optional extra ways to acquire spirit points and drachma but throttled so AQs are still worthwhile doing. thanks for adding him to the game.

I have a couple of suggestions understanding that implementing things is much harder than suggesting them -

1\) allow some kind of grace period around maintaining your streak

to maintain a streak you need to have quarterly completed, weekly completed, and all daily subdues

I can probably manage to pop on to do the daily subdues but not all weeklies some and the quarterly in a day is rough. Perhaps, 3 days in advance Haw tells you what the next weeks weekly is, and 2 weeks in advance of the quarterly?

2\) I'm pretty good at subdues but there's a certain amount after which I'm not having fun. some alternative tasks would be nice. I'm not sure if this would be implemented as Either do X or Y or just sometimes the task is not subdue.

some ideas that may lack feasibility : 

Kill some number of mobs in a limited amount of time.

Clear an area in a limited amount of time

Earn a certain amount of lead XP. 

Perhaps a thief could triple stab or splork a certain number of mobs in a given amount of time.

Hand in an item

Hand in X corpses of a mob

Rare spellbook handin (if it went to the library somehow)

</div>

<div class="post" data-post-id="39984" data-author="Insomnia" data-date="2022-11-02T23:42:55+00:00" data-subject="Re: Master Hawthorn">

One thing I would improve in Hawthorn is the way the quests are given. Instead of a simple list of mobs and items, wouldn't it be cooler if there was a puzzle to solve? Nowhere else in the game do we get direct instructions like this, "bring me X and I will give you Y" – except that from Hawthorn. If we had to figure out what exactly he wants, it would have been a lot more fun.

Of course, I'm not suggesting encrypting names and making puzzles for 12k mobs in the game, there should be a smarter approach to do it. One way to do it (a random idea) could be to not just give names of the mobs directly, but describe them using their attributes.

- Difficulty 1: ...
- Difficulty 2: This creature from The Demonweb and Citadel is known to have a beautiful piece of neckware.
- Difficulty 3: This creature from Positive Energy Plane is known to have the reflection spell on it.

In most cases you should be able to identify the mob easily. Sometimes not, but that will only make it more interesting.

</div>

<div class="post" data-post-id="40058" data-author="Driven" data-date="2023-08-09T20:52:38+00:00" data-subject="Re: Master Hawthorn">

Master Hawthorn now shows you the forge bounties for next week and next quarter. This should enable us to keep streaks going. This was rather difficult to code, so beware to the user. If you find that Master Hawthorn is ever incorrect in his predictions, please let me know ASAP and I'll work to fix it. 

I hope to make the following updates, sooner than later:

\- Leader board

\- Daily item pop

\- Daily area clear

</div>

<div class="post" data-post-id="40059" data-author="Insomnia" data-date="2023-08-10T10:36:12+00:00" data-subject="Re: Master Hawthorn">

Here are two very different forges of difficulty 1:

```
Weekly forge: The Dagger of Mortality's Cleansing (difficulty: 1)
...
Next Weekly forge: a charcoal tome (difficulty: 1)
```

Is this correct? While charcoal tome is indeed one of the easiest forges in the game, I don't think "difficulty: 1" is right for the dagger.

</div>

<div class="post" data-post-id="40060" data-author="Driven" data-date="2023-08-10T20:12:08+00:00" data-subject="Re: Master Hawthorn">

That is a bug that was introduced as a result of adding the next object info. Code has been fixed--note that your forge turn-ins for next period may change as a result of this fix.

</div>

<div class="post" data-post-id="40061" data-author="Driven" data-date="2023-08-10T20:35:54+00:00" data-subject="Re: Master Hawthorn">

If you "look hunters" in Hawthorn's room, you should now see a leaderboard that starts as of today. It tracks the total rewards you have received from Hawthorn, where each type of reward has its own list (conquest, gold, honor, and drachma). There is also a 5th category for the longest streak in days. Some comments

\- I will likely be updating the formatting of the leaderboard as time goes on to make it easier to read.

\- I will be adding the top hunters for each reward to the main 'list" screen at Hawthorn.

\- I will be adding Hawthorn social gossips when someone overtakes someone else in a given category. Hawthorn likes to talk trash, apparently.

</div>

<div class="post" data-post-id="40062" data-author="cnl" data-date="2023-08-15T17:39:17+00:00" data-subject="Re: Master Hawthorn">

Neat feature improvements. Thanks! Now just need to find the time to work some of these tricky forges.

</div>

<div class="post" data-post-id="40069" data-author="cnl" data-date="2023-09-05T19:39:02+00:00" data-subject="Re: Master Hawthorn">

After the crash, the new hunters board is empty and not populating.

Hawthorn beams with pride and shows you the bounty hunters of Jord.

\----------------------------------------------------------------------------------------------------

\------------------

 Conquest \| Gold \| Honor \| Drachma \| 

Streak 

\----------------------------------------------------------------------------------------------------

\------------------

\----------------------------------------------------------------------------------------------------

\------------------

might need a push start <img src="/images/smilies/icon_e_smile.svg" alt=":)" title=":)" width="15" height="15" class="smiley nozoom">

The pre-weekly forge warnings seem to be working well. Now I just see how long I can last before some impossible task is set <img src="/images/smilies/icon_e_smile.svg" alt=":)" title=":)" width="15" height="15" class="smiley nozoom">

</div>

<div class="post" data-post-id="40070" data-author="Insomnia" data-date="2023-09-11T10:41:10+00:00" data-subject="Re: Master Hawthorn">

```
 [Available] Weekly forge: the sage's walking stick (difficulty: 1)
```

```
id stick
Ok.
You feel informed:
Object 'stick staff sages walking cp', Item type: WAND
Item is: HUM TEMPORARY 
Weight: 2, Value: 70000gold, Worn in: TAKE HOLD 
Has 3 charges, with 3 charges left.
Level 41 spell of:
firewind
Can affect you as:
 Affects: MANA by 15
 Affects: REGEN_MANA by 4
Only those who are at least apprentice avatars may use this item.
```

Is it a correct behavior that Hawthorn requests temp forges?

</div>

<div class="post" data-post-id="40071" data-author="Insomnia" data-date="2023-09-13T09:13:37+00:00" data-subject="Re: Master Hawthorn">

I also think that ?? in difficulty meant that the mob was bigger than the normal difficulty of the bounty, and you get the highest reward or even a little more for such mobs. But now it's seems to be broken:

```
[Available] [5-10m] Daily subdue: The witch priestess Ziela (difficulty: ??)
...
 [5-10m] Daily subdue: 2.5k-5.0k honor, 5k-10k conquest, 50k-100k gold, 17% chance 1 drachma.
...
offer subdued hawthorn
You offer a subdued witch priestess Ziela to Master Hawthorn.
Master Hawthorn tells you 'Excellent work! Here is your reward!'
You receive 2500 honor points.
You receive 5000 conquest points.
You receive 50000 gold coins.
```

Here I got the lowest possible reward for the ?? difficulty mob.

</div>

<div class="post" data-post-id="40073" data-author="Insomnia" data-date="2023-10-01T20:13:06+00:00" data-subject="Re: Master Hawthorn">

Yesterday:

```
 [Completed] [1-5m] Daily subdue: a battered demon (difficulty: 2)
 [Completed] [5-10m] Daily subdue: a lookout guard (difficulty: 6)
 [Completed] [10-100m] Daily subdue: a force wall (difficulty: 3)
 [Completed] Weekly forge: a wolfskin robe (difficulty: 3)
 [Completed] Quarterly forge: an adamantite greatshield (difficulty: 20)
-----------------------------------------------------------------------------------------------------
 Next Weekly forge: steel spurs (difficulty: 4)
 Next Quarterly forge: flaming black silk sleeve (difficulty: 15)
-----------------------------------------------------------------------------------------------------
```

Today:

```
 [Available] [1-5m] Daily subdue: Chimalpopoca (difficulty: 8)
 [Available] [5-10m] Daily subdue: a purple worm (difficulty: 5)
 [Available] [10-100m] Daily subdue: the ettin stapler (difficulty: 2)
 [Available] Weekly forge: steel spurs (difficulty: 4)
 [Available] Quarterly forge: The Winterblade (difficulty: 15)
-----------------------------------------------------------------------------------------------------
 Next Weekly forge: Bloodstained Blad (difficulty: 4)
 Next Quarterly forge: an adamantite gre (difficulty: 20)
-----------------------------------------------------------------------------------------------------
```

Not only it's Winterblade instead of flaming black silk sleeves, but an adamantite greatshield again!!! (which is a terrible forge, I had to do dozens of Olympus runs to get it done)

</div>

<div class="post" data-post-id="40081" data-author="Insomnia" data-date="2023-11-26T11:45:58+00:00" data-subject="Re: Master Hawthorn">

Yesterday:

```
 Next Weekly forge: the berserker's girdle (difficulty: 8)
```

Today:

```
 [Available] Weekly forge: an ugly decaying ankh (difficulty: 2)
```

¯\\\_(ツ)\_/¯

</div>

<div class="post" data-post-id="40083" data-author="Driven" data-date="2023-12-10T01:10:28+00:00" data-subject="Re: Master Hawthorn">

When I get some time over the Christmas break, I will look at these oddities and why look hunters isn't working.

</div>

<div class="post" data-post-id="40084" data-author="Insomnia" data-date="2023-12-10T02:06:37+00:00" data-subject="Re: Master Hawthorn">

Thanks, we appreciate it! <img src="/images/smilies/icon_e_smile.svg" alt=":)" title=":)" width="15" height="15" class="smiley nozoom">

Hunters magically started working again. Maybe it required somebody else other than me to complete all bounties. I also wonder if it's possible to hack my streak to 53 + 25 days... because it was not me, it was the game that was down for two weeks. I never missed a day. <img src="/images/smilies/icon_e_smile.svg" alt=":)" title=":)" width="15" height="15" class="smiley nozoom">

</div>

<div class="post" data-post-id="40086" data-author="Driven" data-date="2023-12-26T17:19:24+00:00" data-subject="Re: Master Hawthorn">

Ok, fixed a couple things--

(1) Sage's walking stick has been removed -- was an oversight.

(2) Found a bug in the next-quarterly forge code and fixed it -- please take a look at your list screen to see if it now points to something other than the dreaded adamantite greatshield, and at the end of the year, please let me know whether your new quarterly forge reflects this new forge.

The ?? difficulty can go either up or down -- so it can push you up to 11 or down to 0.

As for 'look hunters', I strongly suspect there is an array initialization problem, but for the life of me I can't find it. I will have to look at what is happening the next time this breaks.

</div>

<div class="post" data-post-id="40087" data-author="Driven" data-date="2024-01-22T01:42:07+00:00" data-subject="Re: Master Hawthorn">

Look hunters should be fixed now.

</div>
