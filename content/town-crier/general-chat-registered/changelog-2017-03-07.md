---
title: "Changelog 2017-03-07"
topic_id: 4742
author: "*teker*"
date: 2017-03-07T15:39:40+00:00
last_activity: 2017-03-14T16:58:52+00:00
last_author: "Josiah"
sticky: false
locked: false
post_count: 16
---

<div class="post" data-post-id="38097" data-author="*teker*" data-date="2017-03-07T15:39:40+00:00">

I didn't schedule the reboot so there's going to be more changes than what's listed here.

Stuff I worked on:

Minor fix to counters so that leveling doesn't mess them up.

Minor changes to counter formatting.

Added some new counters that I think some of you will find valuable.  It's a first attempt so feel free to suggest improvements/changes.  I'm going to go update the help files now...

</div>

<div class="post" data-post-id="38099" data-author="*teker*" data-date="2017-03-07T18:33:38+00:00">

Forgot to mention that I added "score affects2" which shows spells and how much time they have left.  For people that don't use MSDP to pull that information.

</div>

<div class="post" data-post-id="38100" data-author="Gorka" data-date="2017-03-07T18:53:16+00:00">

Wow, very nice change to counters.

I've done a few coliseum test runs calculating my total damage wearing my various eq modes. 

Already I've worked out...

That a spell save is worth about 5 spell damage or greater.

That damage increasing eq has more of a net benefit than wearing damage reduction/ac.

That a handdam is about +10 damage to grip.

That two strikes don't beat my firewind.

That a minor sun house is pretty much +20 spell damage.

I guess all of this could be calculated before with hours and hours of work in the arena, some of the information isn't exactly new, but very grateful all the same for a massive opportunity to get a bit more nerdy with the numbers... a part of sloth I really enjoy.

PS msdp.LOCATION still stuffed, ran all the way to coliseum without it updating.

</div>

<div class="post" data-post-id="38101" data-author="Gorka" data-date="2017-03-07T22:04:23+00:00">

5 hours now playing with stats  :lol: 

I've come to the conclusion that the long debated difference in "power" between monks and warriors and warrior playing monks is negligible, and actually it mostly comes down to play style and the size of the mobs you hit. The differences between, riposte, counterattack, deathblow, flurry, strike, firewind, ac difference, weapons vs hands, caps more a less cancel each other out. The advantage coming down to monks being better for smaller mobs, and warrior being better for larger mobs. I have 5hrs of calculating numbers... but not sharing here, you can run them yourselves, besides... strong numerical evidence has proven to be ineffective on most players opinions anyway, if past experience is anything to go by.  :P 

A couple of requests for consideration...

* Can you count hit point damage to the character as a counter. (So we can calculate AC effectiveness - can't wait to calculate how much ac sacrifice is worth a damage point)

* I suspect the counter for deathblow shows more damage than what was required to kill the mob?

* Do we get a counter for damage from our pets?

What a night..! Off to bed...

</div>

<div class="post" data-post-id="38102" data-author="*teker*" data-date="2017-03-07T23:13:49+00:00">

> **Gorka wrote:**
> * Can you count hit point damage to the character as a counter. (So we can calculate AC effectiveness - can't wait to calculate how much ac sacrifice is worth a damage point)

I'll probably build a similar table for damage received and add totals at the bottom for both tables.

> **Quote:**
> * I suspect the counter for deathblow shows more damage than what was required to kill the mob?

I'm not capping the damage on death because that would drop your average if a mob is at -9 before the last strike.  That being said, the numbers do get inflated since you get bonus damage against targets that aren't standing.

> **Quote:**
> * Do we get a counter for damage from our pets?

We could probably do a singular counter that totals all pet damage dealt.

</div>

<div class="post" data-post-id="38103" data-author="Filk" data-date="2017-03-08T06:18:45+00:00">

Great addition with counters. Highly appreciate that, Teker.

Some bugs about it.

1. Missing average when amount of hits lower then 5. Guess thats working as intended to not reveal exact value of each attack. 

2. Some skills missing in counters. For example piasa blasts(both), or makara chomp, or bear maul. Some other forms works fine though. Not tested much of them yet.

3. Thorns, petrified armor, and other such kind of damage also not counting

Just some blank ideas about that addition.

1. Maybe critical hits of any different kind should be count as separate source of damage. I mean separate basic, critical and massive critical. Same for spell saves. Same for any kind of dots - like poison, deathgrip cycles, solar blast ticks and so on. To not mix damage of main strike and it dot.

Also basic attacks with same name of different forms should be list separated. Ie Bite(Chimaera), Bite(Makara)

2. Make specaial "dummy" mob. With zero attack power, but infinite hps(or it could just heal up each round). And each minute that mob reports, how much damage you made on it from start of the fight. And also showing dps value. Fighting it for several minutes will be good way to know your real combat dps.

There could be several such dummies actually with different ac/damage reduce value. Like low level mob, mid level mob, huge epic and so on.

</div>

<div class="post" data-post-id="38104" data-author="Tuck" data-date="2017-03-08T19:02:00+00:00">

Great job Teker.

Counters/new housing/levels and counting. Very good job.

</div>

<div class="post" data-post-id="38105" data-author="*Breeze*" data-date="2017-03-09T09:27:34+00:00">

> **Filk wrote:**
> Great addition with counters. Highly appreciate that, Teker.
> 
> 
> 
> Some bugs about it.
> 
> 
> 
> 1. Missing average when amount of hits lower then 5. Guess thats working as intended to not reveal exact value of each attack. 
> 
> 
> 
> 2. Some skills missing in counters. For example piasa blasts(both), or makara chomp, or bear maul. Some other forms works fine though. Not tested much of them yet.
> 
> 
> 
> 3. Thorns, petrified armor, and other such kind of damage also not counting
> 
> 
> 
> 
> 
> Just some blank ideas about that addition.
> 
> 
> 
> 1. Maybe critical hits of any different kind should be count as separate source of damage. I mean separate basic, critical and massive critical. Same for spell saves. Same for any kind of dots - like poison, deathgrip cycles, solar blast ticks and so on. To not mix damage of main strike and it dot.
> 
> Also basic attacks with same name of different forms should be list separated. Ie Bite(Chimaera), Bite(Makara)
> 
> 
> 
> 2. Make specaial "dummy" mob. With zero attack power, but infinite hps(or it could just heal up each round). And each minute that mob reports, how much damage you made on it from start of the fight. And also showing dps value. Fighting it for several minutes will be good way to know your real combat dps.
> 
> There could be several such dummies actually with different ac/damage reduce value. Like low level mob, mid level mob, huge epic and so on.

1- not a bug.  its a design choice that we 3 agreed on.

2- not a bug. that damage is added in a different place. can be considered a lets get it in game for now and tweak it later.

3- not a bug. that damage is added in a different place. can be considered a lets get it in game for now and tweak it later.

re: blank ideas

 no comment

</div>

<div class="post" data-post-id="38106" data-author="Filk" data-date="2017-03-09T13:53:17+00:00">

> ***Breeze* wrote:**
> 2- not a bug. that damage is added in a different place. can be considered a lets get it in game for now and tweak it later.
> 
> 
> 
> 3- not a bug. that damage is added in a different place. can be considered a lets get it in game for now and tweak it later.

Well. Its all about definitions for sure :)

But i consider it as a bug, since damage source dont appears in counters in any way. So in defined new functionality of counters it could be counted as bug. Imho for sure :)

```
counters
Solo counters:
You have gained 0 experience points in 26 seconds.
You have gained 0 gold coins in 26 seconds.
You have gained 0 honor points in 26 seconds.

Your counters are currently in solo mode.

<907hp 1169ma 272mv>
shapeshift piasa
You raise your hands to the sky and rapidly shift into an enormous piasa bird (Fluffy).

<1939hp 1127ma 166mv>
blast solar kobold
Flames burst forth from your body, scorching a male kobold to a crisp.
A male kobold hates your guts!
A male kobold is dead! R.I.P.
[LEVEL 30] 
You gain 461 bonus experience!
Total exp for kill is 1,306.[BonusEXP:35%]
Your blood freezes as you hear a male kobold's death cry.
You get gold coins from the corpse of a male kobold that's on the ground.
There were 350 coins.

<1939hp 1076ma 171mv>
counters
Solo counters:
You have gained 5,871 experience points in 41 seconds.
    Average = 143.2 xp/second.
You have gained 350 gold coins in 41 seconds.
    Average = 8.5 gold/second.
You have gained 0 honor points in 41 seconds.
1 kill, 5.9k xp/kill, 350.0 gold/kill.
    87.8 kills/hour, 1.5 kills/minute.

Your counters are currently in solo mode.

<1939hp 1080ma 175mv>
```

</div>

<div class="post" data-post-id="38107" data-author="*Breeze*" data-date="2017-03-09T14:00:40+00:00">

personally i told him to just add all mudl damage (which is how shapeshift skills work)

under one counter for "other"

if he wants to go through and tweak every shapeshift form / skill thats his thing.

i would probably add the thorns/wall/etc damage to "other" also.

</div>

<div class="post" data-post-id="38108" data-author="*teker*" data-date="2017-03-09T18:54:49+00:00">

A fix for the score affects2 crash went live during the last crash reboot.

Next reboot will have the "other" counter, a total at the bottom, and a counter for pet damage.

I changed the script for the piasa arctic blast so that it treats the damage internally as "frost breath" and uses the counter for it.  This is live now.  As a positive, it changes it to work with resist cold as all normal spells do rather than a hacked solution in the script.  It does display an extra message on the attack - let me know how this looks and I'll try to find a way to proceed from there.

EDIT: Fixed spelling

</div>

<div class="post" data-post-id="38109" data-author="Filk" data-date="2017-03-10T02:10:14+00:00">

> ***teker* wrote:**
> I changed the script for the piasa arctic blast so that it treats the damage internally as "frost breath"

I used piasa only as example of not displayed source. That form is rarely used anyway - its heavy unbalanced.

</div>

<div class="post" data-post-id="38112" data-author="Gorka" data-date="2017-03-13T08:47:42+00:00">

Any reason damage averages have dropped out of being shown in counters?

</div>

<div class="post" data-post-id="38113" data-author="*Splork*" data-date="2017-03-13T11:00:11+00:00">

We had an issue last night with some new code and had to go back a week to a previous build.

Once the bugs are figured out, we will update and push forward.

Sorry,

</div>

<div class="post" data-post-id="38114" data-author="*teker*" data-date="2017-03-13T14:18:11+00:00">

Sorry guys - I had put in a fix for GAG_FIGHT and a condition showed up that I didn't see on the test server.  I've committed a fix so next reboot everything should be put back in.

</div>

<div class="post" data-post-id="38115" data-author="Josiah" data-date="2017-03-14T16:58:52+00:00">

> **Gorka wrote:**
> Wow, very nice change to counters.
> 
> 
> 
> I've done a few coliseum test runs calculating my total damage wearing my various eq modes. 
> 
> 
> 
> Already I've worked out...
> 
> 
> 
> That a spell save is worth about 5 spell damage or greater.
> 
> That damage increasing eq has more of a net benefit than wearing damage reduction/ac.
> 
> That a handdam is about +10 damage to grip.
> 
> That two strikes don't beat my firewind.
> 
> That a minor sun house is pretty much +20 spell damage.
> 
> 
> 
> I guess all of this could be calculated before with hours and hours of work in the arena, some of the information isn't exactly new, but very grateful all the same for a massive opportunity to get a bit more nerdy with the numbers... a part of sloth I really enjoy.
> 
> 
> 
> PS msdp.LOCATION still stuffed, ran all the way to coliseum without it updating.

Yep, it was all calculated previously, but with enormous amounts of effort. I'm happy that the numbers are now available to everyone without the need to reverse engineer the game.

Also, either your strikes are weaksauce or your firewinds are unexpectedly strong.  Strike maxes out at about 230 average damage.

Nerdy numbers are awesome.

</div>
