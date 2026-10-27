---
title: "prompt score bug"
topic_id: 2395
author: "Marchessa_red_witch"
date: 2007-03-14T05:04:47+00:00
last_activity: 2007-03-18T14:51:59+00:00
last_author: "Marchessa_red_witch"
sticky: false
locked: false
post_count: 15
---

<div class="post" data-post-id="17281" data-author="Marchessa_red_witch" data-date="2007-03-14T05:04:47+00:00" data-subject="prompt score bug">

You have +8 to hit and +8 on damage.

You have 501355 gold coins.

You have forty-seven drachma.

You have 1006902233 unused experience points.

You have been playing for 81 days and 22 hours.

You are well-attuned to the channelling stratum.

Str: 18 / 3, Int: 18, Wis: 14, Dex: 18, Con: 18

You are resting.

You are affected by the following spells:

 Infravision 

 Resist Fire 

 Resist Cold 

 Iron Skin 

 Corona 

1-\> 983/983/+44hp 355/369/+34ma 216/216/+34mv +5/+8 

Note the hit not being the same in both places

</div>

<div class="post" data-post-id="17282" data-author="Weasel" data-date="2007-03-14T05:14:04+00:00" data-subject="">

swordsmanship probably

</div>

<div class="post" data-post-id="17283" data-author="Marchessa_red_witch" data-date="2007-03-14T12:43:22+00:00" data-subject="If that is the case">

Then why are frenzy and berserk (skills) never reflected in score's damage.

</div>

<div class="post" data-post-id="17284" data-author="Autolycos" data-date="2007-03-14T12:47:05+00:00" data-subject="">

people actually use frenzy and berzerk?? <img src="/images/smilies/icon_eek.svg" alt=":shock:" title=":shock:" width="15" height="15" class="smiley nozoom">

</div>

<div class="post" data-post-id="17285" data-author="Marchessa_red_witch" data-date="2007-03-14T12:48:10+00:00" data-subject="Sure">

If you're 4.meat who cares what your ac is...

But back to this - it's clear there two different algorythms determining score and prompt, when they should be the same. Leave aside that there are things which there is no way to actually track, or are tracked through yet another different location.

</div>

<div class="post" data-post-id="17287" data-author="13" data-date="2007-03-14T13:00:50+00:00" data-subject="">

I use frenzy constantly. As far as I know it doesn't affect your ac at all. Zerk is, meh.

</div>

<div class="post" data-post-id="17290" data-author="Autolycos" data-date="2007-03-14T17:08:57+00:00" data-subject="">

> <strong>13 wrote:</strong>
> I use frenzy constantly.

DOH! <img src="/images/smilies/icon_eek.svg" alt=":shock:" title=":shock:" width="15" height="15" class="smiley nozoom"> 

all this time i thought you were having dt convulsions <img src="/images/smilies/icon_twisted.svg" alt=":twisted:" title=":twisted:" width="15" height="15" class="smiley nozoom">

</div>

<div class="post" data-post-id="17291" data-author="banedon" data-date="2007-03-14T18:40:27+00:00" data-subject="">

I use frenzy all the time too. I've compared runs, and frenzy adds just a lil more damage, especially on my grip. for example, usually when i just focus before i grip the monk guards in the BH guild, it takes 2 or 3 rounds to kill them, using frenzy and focus, I splork them more than 50% of the time

</div>

<div class="post" data-post-id="17293" data-author="Avatar" data-date="2007-03-15T14:14:25+00:00" data-subject="berserk">

Berserk seems to have some effect on your critical / massive criticals. Namely, you don't get any criticals while using berserk. You might run some tests to see if the bonus damage from berserk compares favorably to the bonuses from the criticals that you might normally get. I haven't compared the numbers, I don't use berserk much because of the AC penalty.

Anyway, I was going to mention that since berserk has some bearing on criticals it may be possible that frenzy reduces the crit rate. Otherwise, I haven't noticed any side effects to frenzy.

</div>

<div class="post" data-post-id="17294" data-author="Guinex" data-date="2007-03-15T18:56:41+00:00" data-subject="">

If you deal low damage berserk is worth it, but if you have 18/100 str decent eq and a good weapon frenzy is better.

</div>

<div class="post" data-post-id="17295" data-author="Atwell" data-date="2007-03-16T02:55:05+00:00" data-subject="">

Indeed. Frenzy applies +2dam with no other apparent effects. Berserk applies +10dam +2 ac and suppresses critical hits. A critical hit doubles damage, while a massive critical hit triples damage. Let D be your average damage per attack before either skill, including average weapon dice, damroll, and weapon damage effects. Let C be the probability that an attack is critical, and M be the probability that a critical hit is massive. It can be shown that frenzy yields better average damage when the following inequality holds:

D \> 8/(C(1+M)) - 2

I have not measured C or M, and small changes in their values rapidly affect the outcome. I do suspect an M = .85 for warriors with the skill fully learned, and of course M = 0 for those without the massive critical hit skill.

I have not measured how frenzy or berserk affect backstab, deathgrip, deathtouch, or wraithtouch.

</div>

<div class="post" data-post-id="17296" data-author="Weasel" data-date="2007-03-16T03:07:23+00:00" data-subject="">

hmm.. suggest perma-frenzy be added to Lyme shop for purchase.. <img src="/images/smilies/icon_e_smile.svg" alt=":)" title=":)" width="15" height="15" class="smiley nozoom">

</div>

<div class="post" data-post-id="17297" data-author="12345" data-date="2007-03-16T03:19:41+00:00" data-subject="">

If there were such a thing as a Mud Diploma.... I'd give it to Atwell.

</div>

<div class="post" data-post-id="17346" data-author="Avatar" data-date="2007-03-18T13:10:05+00:00" data-subject="mud diploma">

I second that, nice job Atwell.

</div>

<div class="post" data-post-id="17350" data-author="Marchessa_red_witch" data-date="2007-03-18T14:51:59+00:00" data-subject="Berserk and Spiritual Hammer">

Are a worthwhile combination. Can't parry the etheral anyway, and it is not as if hps are really an issue.

</div>
