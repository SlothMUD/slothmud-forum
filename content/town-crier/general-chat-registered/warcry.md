---
title: "warcry"
topic_id: 1134
author: "Qa"
date: 2005-05-23T11:47:31+00:00
last_activity: 2005-05-26T15:26:11+00:00
last_author: "impz"
sticky: false
locked: false
post_count: 35
---

<div class="post" data-post-id="6417" data-author="Qa" data-date="2005-05-23T11:47:31+00:00">

So I grouped for the first time in a couple of months Friday night.  Deju lead a nice tight group, I got another 5% or the way to a level, and I wasted a couple of hours.  Sloth usual.

I have posted frequently about not being able to keep up with all the crap that gets added to the mud, and couldn't read the help file with the group spam going, so it took me a while to figure out this warcry thing.

I think warcry is horrendously overpowered.

In my "group" mode I am running a touch over 800 hp (with stamina up.)  Pretty buff for an old-school Cl/Ma yeah?  Imagine my surprise when I notice my hp over 1000!  This is cool, but every once in a while it will happen with a eudaemon in "tank" mode.  Next thing I know my hp is over 1100!  Stop the bus - somebody put me in Sarge!

Not sure what all warcry does, but what is the idea with this?  A 40% hp increase is a big deal.

Qa

ps - Now if ya want to give me a cleric prime spell that bops up my hp 40% that would be truly cool.

</div>

<div class="post" data-post-id="6420" data-author="kjartan" data-date="2005-05-23T12:01:06+00:00">

It's supposed to max out at +100 maxhp.  Possibly there's a bug.

</div>

<div class="post" data-post-id="6421" data-author="Deju" data-date="2005-05-23T12:01:56+00:00">

One thing to keep in mind:

Our tank for that group (Bird) has a very large number of kills associated with his warcry.  The higher the # of kills, the better the bonuses... or at least this is what i understand.  Therefore Qa, what you were getting was probably somewhere around the top of the heap as far as bonuses are concerned.

Is warcry overpowered in general?  Maybe, but I personally dont think so.  Is warcry overpowered relative to other aspects of the game?  Absolutely NOT.  There are plenty of other aspects of the game that are way, WAY out of control (high level Juju and followers come to mind quickly, although i could come up with more).

</div>

<div class="post" data-post-id="6431" data-author="kjartan" data-date="2005-05-23T14:22:51+00:00">

We're going to leave it alone.  If it's overpowered, it's only much overpowered in big groups, and what can we say, we like big groups.

</div>

<div class="post" data-post-id="6438" data-author="Autolycos" data-date="2005-05-23T15:51:15+00:00">

thats good to know..  I have over 1000 kills on my warcry atm, and my group sunday was getting +50 to +100hp on cry and it was great..  

As far as Bird goes, that meatshield is just a badass tank anyway, so i would expect to get crazy bonuses from his warcry..

LONG FLAP DA' BIRD!!  :twisted:

</div>

<div class="post" data-post-id="6440" data-author="Leaf" data-date="2005-05-23T16:11:18+00:00">

Well Bird is OLD School class order.  More Bad ass are like Ash, Ninja and

Flight

</div>

<div class="post" data-post-id="6441" data-author="Leaf" data-date="2005-05-23T16:11:45+00:00">

Well Bird is OLD School class order.  More Bad ass are like Ash, Ninja and

Flight

</div>

<div class="post" data-post-id="6479" data-author="kjartan" data-date="2005-05-24T18:40:31+00:00">

I thought I'd warn you that there does appear to be a bug in warcry, and I intend to fix it.  Sometimes it may be applying the effects twice.  I'd suspect if you're seeing the message twice, then you're getting the effects twice and you should not be surprised if this stops.  (For example, the max hp bonus it can give is +100; the level below this of hp bonus is +60.  If you're getting more than +100 then you are definitely getting affected twice).

Also, I am going to change it to make the hp bonus work like temporary hp do in D&D, which is that you get them during the warcry and if you use them, great, but if you don't they go away when the warcry wears off.  Basically, damage goes to the warcry extra hp first, and only when they are exhausted does it start hitting your real hp.  This will fix a possible exploit where warcry could be used for free (if slow) healing.  Allegedly there is not widespread use of this exploit, in which case this should have little visible effect.

</div>

<div class="post" data-post-id="6480" data-author="Qa" data-date="2005-05-24T19:05:04+00:00">

Not sure if my sieve that I call a brain can remember correctly, but it didn't seem like I was getting +200 hp for joining a single attack after uttering the warcry.  Bird and the Deju were smacking through mobs like no tomorrow, so the warcries and RIPs were pretty close together.  Think that I was getting the +100 bump every other kill or so, and I lose the 'excess' hp kinda slow, so that is how I got to 1.1k and change.

I am trying to understand here, though.  You consider it ok for a ca/ca running in a 'regen' mode to be able to amass 1100 hp through warcry?  Those juju's must really effing be powerful, if this is considered 'in balance.'

Here I thought I was going to be cool and all.  I have (half-heartedly) been trying to amass a complete set of +hp items.  Thinking that at 5x40 I would get to about 1k hp in -10 gear.  (A tanking cleric!  Film at 11.)  Parry eliminated any real usefullness of this, and then the addition of +spelldam EQ made +hp gear for non-warriors even more so.  Just funny that I can finally get not 1k hp, but 1.1k.  Hell, I could probably get to 1.2 or even 1.3 k!

-Qa

Edited for spelling mistakes.

</div>

<div class="post" data-post-id="6483" data-author="Avatar" data-date="2005-05-24T19:56:31+00:00">

That's pretty much only going to happen during large groups.  Warcry when you're soloing isn't quite so powerful.

</div>

<div class="post" data-post-id="6494" data-author="13" data-date="2005-05-25T11:49:37+00:00">

Get something valid to whine about already QA.

</div>

<div class="post" data-post-id="6496" data-author="kjartan" data-date="2005-05-25T12:34:42+00:00">

Ok, changes are in next crash or reboot.  These are that 

1. instead of raising your max hp, warcry will now give you the same amount of temporary hp.  These will look like they are over your max (310/300 or whatever) but they won't bleed away like over-the-max hp usually do.  They will however go away immediately when the fight ends.  Damage comes off temporary hp until they run out, then off real hp.  Temporary hp cannot be healed.

2. The bug that sometimes applied the effects twice is fixed.

</div>

<div class="post" data-post-id="6499" data-author="Leaf" data-date="2005-05-25T13:40:47+00:00">

So tanks that use to find this skill "useful" is now useless for them...

Good job QA, let the bitching from tanks/groups begin!!!

</div>

<div class="post" data-post-id="6500" data-author="Alberich" data-date="2005-05-25T13:45:30+00:00">

extra hps are useless?  maybe it's just because I never run in groups, but the logic in that escapes me...

</div>

<div class="post" data-post-id="6501" data-author="13" data-date="2005-05-25T13:51:31+00:00">

that dude fucking pisses me off

</div>

<div class="post" data-post-id="6502" data-author="Leaf" data-date="2005-05-25T13:59:00+00:00">

extra hps are useless?  maybe it's just because I never run in groups, but the logic in that escapes me...[/quote:2bg89bhi]

Ok Alber, before the "new" change.  When a tank would "Warcry" and every1

that joins in this "Warcry" they would get their HP upped.  Example:  You

have 1000hp (Tank), you warcry, attack get a bonus jump to maybe 1050.

Keep crying and killing ur hp gets higher and higher.  So when ur in a group

and a cleric heals you, ur hp is 1050 as a temp "spell". 

NOW, if you have 1000hp and cry, your hp gets 1050 but if u get wacked 

and someone heals you, ur hp goes back to 1000hp.  Skill is "Useless" with

this new change.  It only helps the group, but not the tank who is the one

that is using this skill.

</div>

<div class="post" data-post-id="6506" data-author="12345" data-date="2005-05-25T14:28:08+00:00">

Um.. net effect may appear useless, but in reality, the math works out the same.

Say warcry raises me from 1000 hps to 1050. When I fall to 850 and get healed for 200, I still only got healed 200 hp and the 50 stays as a buffer between me and death, making the extra 50 effectively unused.  Difference now would be that I would have to fall to 800 and get healed to 1000.  My extra 50 hps are getting used first, but I haven't lost anything, since I still only got healed for 200.

You're losing the 50 point buffer between you and death, and gaining 50 hps before you have to start healing.  The extra hps are still there so I can't say this is a nerf, though some tanks may disagree I guess.  The group bonus is still there, which is important because tanks have a dedicated healo and the group doesn't.  More important on some mobs than others, obviously.

I don't see how the skill is useless at all though.  It's essentially just as effective as it's always been.

</div>

<div class="post" data-post-id="6508" data-author="Alberich" data-date="2005-05-25T14:33:36+00:00">

nod.. again, I don't group, and have never really used warcry, but it seems to me that the overall effect now is something similar to the overheals eudaemons used to do (still do maybe?  I haven't bothered much with supps, before or after change, so not real sure).  You can still take an extra hit or so before you need to start healing.  I suppose it's not quite as sweet as having the extra hps added to your max, but it still seems fairly usefull as a 1-time buffer, along the lines of mirrors or an ariel servant.

I am curious though, if your tank has say 1k hps, and warcry gets him up to 1050, then gets whacked during fight, and at start of next fight has say 950 hps, and warcry is done again - will he have 1k hps, or 1050?

</div>

<div class="post" data-post-id="6510" data-author="Leaf" data-date="2005-05-25T14:38:54+00:00">

I don't know if the hp will just add 950 or not.  I believe it wont, unless the

tank is "full".  

Saying that it sucks for tanks, because before they can get a total of yes

+200hp and when they get healed, they would keep the +200.  However

if they wait a tick the hp starts falling again.  Ooo well I'll stop whining.

</div>

<div class="post" data-post-id="6511" data-author="kjartan" data-date="2005-05-25T14:58:47+00:00">

I am curious though, if your tank has say 1k hps, and warcry gets him up to 1050, then gets whacked during fight, and at start of next fight has say 950 hps, and warcry is done again - will he have 1k hps, or 1050?[/quote:39ckppyj]

He'll have 950 hps  + 50 temporary, so if you then heal him he'll have 1050 total.

</div>

<div class="post" data-post-id="6515" data-author="Qa" data-date="2005-05-25T17:43:02+00:00">

instead of raising your max hp, warcry will now give you the same amount of temporary hp.  These will look like they are over your max (310/300 or whatever) but they won't bleed away like over-the-max hp usually do.  They will however go away immediately when the fight ends.  Damage comes off temporary hp until they run out, then off real hp.  Temporary hp cannot be healed.

[/quote:8ca8skby]

This sounds like the original intent of warcry.  KJ, thanks for recognizing that warcry was overpowered, bugged, or not working correctly.  (Whatever you want to call it.)

Flame me all you want, but warcry was not intended to be the font of hundreds of HP for the group.  Warcry was clearly overpowered or not working correctly.  This was a feature/bug that benefitted the players.  *Stare Leaf, 13*  :twisted: 

Just as we would point out a skill/change is bad, we should be responsible characters and point out when a skill/change may not be doing it's intended function, [i:8ca8skby]even though it's good for the characters[/i:8ca8skby].  How else should be expect the immorts to listen to us when we cry foul because of alignment changes?  It is my opinion that this should be a two way street.

Qa

</div>

<div class="post" data-post-id="6516" data-author="Leaf" data-date="2005-05-25T17:46:53+00:00">

Qa go stand in the middle of a 2 way street and lets see which side u end 

up at.   :twisted:  jk

</div>

<div class="post" data-post-id="6518" data-author="13" data-date="2005-05-25T17:50:53+00:00">

It's not as much fun to flame you if you make sense.  Please stop.

</div>

<div class="post" data-post-id="6520" data-author="Weasel" data-date="2005-05-25T18:04:05+00:00">

True Qa, but notice how quickly anything buggy to the player's benefit generally gets removed / adjusted / tweaked / nerfed? The random pops were added to Lyme the other day, and they were popping too often.. that was removed within a couple of hours. I haven't popped any spellbooks since (and when they were popping, it was nearly all new classo stuff anyway) althou the couple of hex pops were nice while they lasted. Supplication was around for a while but unfortunately I never used it until the last couple of days hitting cloud giants, but it's nerfed now. In comparison if it's the other way around it just seems to take forever for adjustments, I guess in the hopes we just accept it. This is a generalization, but heck, I'm still waiting for something to be done regarding the loss of grace. I have been evil since the alignment changes were made, prior to that I was always near the top of good alignment. The only way I'm going to combat this is stop hitting the mobs I want to hit and only hit the mobs the admin dictate I hit, and only with the spells they dictate I use apparently too. Hey I know, why don't they just play the game for me? A least tone the farking thing down! Evil is in the eye of the beholder, so at least make the alignment balance relatively even the way it was before - right now it's a friggin joke. What's the point in having mobs when there is such a biased penalty for hitting them, it achieves one thing only - restricting the entire mud. If anyone can't see the logic in how this is hurting the attraction of this mud then they should go bury their head in the sand and stay there. Please, growth is good, but not growth that is to the detriment of gameplay.

Bah sorry, just pisses me off every time I think about it.

</div>

<div class="post" data-post-id="6521" data-author="Alberich" data-date="2005-05-25T18:12:44+00:00">

I still don't see how this 'dictates how you play'.  For one thing, if you are that dead-set on using the 'good' supps, it takes 1-2 runs for an avatar to change their alignment either direction (might be slightly more for say a tri40, unless they are a thief), so there is that option.  Supplication was put in what, a few months ago?  It didn't exist before that.  Noone considered that 'dictating how you play', so how is it different now?  I'm with you 100% on the grace thing, and protection from evil too for that matter, but supplication is much more than a peri or a eudaemon, and was probably always meant to - the fact that they became so ubuiquitous over a relatively short period of time that not being able to use 1 or 2 specific ones is considered this huge crippling thing probably indicates that it really was overpowered to begin with.

</div>

<div class="post" data-post-id="6523" data-author="Weasel" data-date="2005-05-25T18:29:10+00:00">

If I want to play the game the way I have been and run the same areas I like, then I have no choice but to lose grace and the possible use of eudaemon (not that I hardly ever used supplication as I said). The alternative is to either not hit those areas and run elsewhere instead (ie: dictate how I play and what I hit) OR run some evil area 4 times for every one time I hit the area I normally like to run, just to keep my alignment good so I can use grace like I always did (ie: dictate how I play and what I hit) - this is if I dont even use supplication, I'm still being adversely effected. Why should a player be disadvantaged because the admins decided some other spell the player didn't use was overpowered? How is this NOT dictating play? I'm not dead-set on using supps at all, I just don't think players in my situation should be penalized for it. I don't dent eudaemons where awesomely overpowered and enabled me to run CG much more effectively, but in taking away some of that excess power, why take away other effects that had nothing to do with it? Now do you see my point? I either put up with the loss and play the way I like to play, or I compensate for the loss by changing the way I play and where and what I hit - that is the definition of dictating how one plays.

</div>

<div class="post" data-post-id="6524" data-author="12345" data-date="2005-05-25T18:41:32+00:00">

I think people are focusing too much on the peri and rabbit.  They were quite nice, especially for tankish types, but of the few supplicants I've ever been able to summon and test, the healers were the useful ones.  Mostly because an einhari and lares are horrible followers for a 40 prime.  Much like druid forms tend to suck if it's your forth class.  The peri has some features that manage to make it useful at most levels, which makes it weapon of choice for those with cleric 3rd and 4th.

It's not as much about the peri being overpowered as it is the rest being underpowered... as far as the 'good' ones.  I still need to play more with the evil supplicants, but I've mostly heard they're good for fighting, which makes me think they'll be mostly underpowered for me until I can summon a nightmare or such... Anyone know the level for summoning one offhand?

</div>

<div class="post" data-post-id="6525" data-author="Deju" data-date="2005-05-25T18:53:02+00:00">

Well, I told myself I wouldnt chime in, but this is nuts.  I can't believe that people think that warcry or supplicants are overpowered.

Do you really think that an extra 50hps here or there, or an occasional greater heal are overpowered when we have players who can currently solo 30-40mil mobs without much trouble?

</div>

<div class="post" data-post-id="6526" data-author="Weasel" data-date="2005-05-25T19:09:36+00:00">

ppl can solo a 30-40 mil mob?!? daaaamn!

</div>

<div class="post" data-post-id="6527" data-author="Medios" data-date="2005-05-25T19:22:07+00:00">

I started a very lengthy post here, but decided to delete it before I alienate myself from a few imms that I really like.  Bottom line is theres an idea in someones head for the direction of Sloth.  Voting has been so high for the last few months (mainly due to the veteran chars who love this game) that the playerbase has grown tremendously.  Now with so many new players sloth could weather the loss of the older generation.  Honestly guys, I dont think many admin care who plays as long as there are alot of players.  I would personally rather have one veteran over 5-10 newbs.  However its not my game I just play it.

Mike

PS 

I have a great idea for next time.  When you add new code, mebbe dont make it so powerful.  I believe every player would rather get an increase in a skill than a decrease.  Put something new in, decide its too weak and give it some more power.  Dont put something in and let it sit for months then decide everyone is having too much fun.

</div>

<div class="post" data-post-id="6528" data-author="Leaf" data-date="2005-05-25T20:42:45+00:00">

Voting has been so high for the last few months (mainly due to the veteran chars who love this game) that the playerbase has grown tremendously.  Now with so many new players sloth could weather the loss of the older generation. 

PS 

I have a great idea for next time.  When you add new code, mebbe dont make it so powerful.  I believe every player would rather get an increase in a skill than a decrease.  Put something new in, decide its too weak and give it some more power.  Dont put something in and let it sit for months then decide everyone is having too much fun.[/quote:19zg25j1]

I agree Mikey, the vets love this game so much we voted every day!  With

all these crappy changes look at the "vote" count.  Sure we have +60 every

night, but without the vets voting who's going to take over?  The newbies?

I don't think so, or we would be hitting +60 votes a day.  Newbies don't

care as much as the vets, because we been here for yrs on yrs.  Sooner

or later the vote count well start falling, and less newbies will come.  We

can only HOPE then the Immorts realized what they have done when they

lost the vets and the newbies.

</div>

<div class="post" data-post-id="6530" data-author="impz" data-date="2005-05-25T22:26:16+00:00">

haha, of course people can cycle 30-40 mil xp mobs. I did one 2 run just yesterday for 3-4 repops.

Ask that stupid autolycos..He came in at the last moment and sponged my xp!!!!

</div>

<div class="post" data-post-id="6531" data-author="Weasel" data-date="2005-05-25T22:29:48+00:00">

sheesh.. which mob(s)? I sure as shit have never taken down anything that big on my own.

</div>

<div class="post" data-post-id="6535" data-author="Leaf" data-date="2005-05-26T01:07:20+00:00">

Depends on ur class order.  Harder for old school ppl to kill things down.

However newer nec/dru can kill mobs alot faster.  +3 wraiths, Umber JuJu

Spells up, Shape and kill.  They can kill a big mob with much ease, but can't

kill really fast.  Like stab stab wind wind mobs.

</div>

<div class="post" data-post-id="6554" data-author="impz" data-date="2005-05-26T15:26:11+00:00">

was loitering around ss and ah.

hitted chinchilla guardian, solarine.

Not on some new class, on impz.

Eventual aim: The first newb to solo tiamat.

</div>
