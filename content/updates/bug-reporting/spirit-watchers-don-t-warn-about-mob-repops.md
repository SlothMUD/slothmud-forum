---
title: "Spirit watchers don't warn about mob repops."
topic_id: 4782
author: "Teron"
date: 2017-08-03T18:45:02+00:00
last_activity: 2017-08-22T08:18:11+00:00
last_author: "Teron"
sticky: false
locked: false
post_count: 20
---

<div class="post" data-post-id="38380" data-author="Teron" data-date="2017-08-03T18:45:02+00:00" data-subject="Spirit watchers don&#x27;t warn about mob repops.">

Example:

<1003hp 683ma 370mv> 2913919907 0 - -2.1 +10 storm

TICK IN 10 SECONDS.

save

Saving Songster.

Saving items.

<1003hp 683ma 370mv> 2913919907 0 - -2.1 +10 storm

The lightning has stopped.

Timer now at 60 secs.

save

<1003hp 683ma 370mv> 2913919907 0 - -2.1 +10 raining

Saving Songster.

Saving items.

<1003hp 683ma 370mv> 2913919907 0 - -2.1 +10 raining

TICK IN 10 SECONDS.

save

Saving Songster.

Saving items.

<1003hp 683ma 370mv> 2913919907 0 - -2.1 +10 raining

TICK IN 10 SECONDS.

save

Saving Songster.

Saving items.

<1003hp 683ma 370mv> 2913919907 0 - -2.1 +10 raining

Countess DeNuva utters the words, 'pzfwzhuq candussabruaiqz'

<1003hp 683ma 370mv> 2913919907 0 - -2.1 +10 raining

Cc the muse tells you 'I've found Countess DeNuva at Northern Catwalk, sir!'

stand

play 'dance of the seven luck gods'

res

res

<1003hp 683ma 370mv> 2913919907 0 - -2.1 +10 raining

You stop resting, and stand up.

---------

There was no warning.

There was no global fast repop.

The same thing happens on mobs that are affected by global fast repop.

</div>

<div class="post" data-post-id="38381" data-author="*teker*" data-date="2017-08-04T19:40:12+00:00" data-subject="Re: Spirit watchers don&#x27;t warn about mob repops.">

I've noticed this as well.  I jut checked the code and it looks like there's only a 10% chance that spirit watchers will send the "I sense your target is coming" message.  That check gets run 6 times a minute for 3-4 minutes before the zone reset so you would think it's pretty likely you'd pass the check with that many opportunities.  But it is possible that you would fail the check every time.

</div>

<div class="post" data-post-id="38382" data-author="*teker*" data-date="2017-08-04T19:47:13+00:00" data-subject="Re: Spirit watchers don&#x27;t warn about mob repops.">

I noticed something with the fast repop that needs fixed so I'm fixing that.

</div>

<div class="post" data-post-id="38383" data-author="Teron" data-date="2017-08-06T08:09:50+00:00" data-subject="Re: Spirit watchers don&#x27;t warn about mob repops.">

So a quest spell only has a chance of working?

This isn't the first time I've encountered this.

This is the first time I'm sufficiently annoyed by this "feature".

If you are looking at this, please take a look at how the luck song prevents mobs from repopping.

Thanks.

</div>

<div class="post" data-post-id="38384" data-author="*teker*" data-date="2017-08-06T18:17:44+00:00" data-subject="Re: Spirit watchers don&#x27;t warn about mob repops.">

Ok, I rewrote the algorithm so that a warning should always happen before repop - even when fast repop is on.  You'll have to try it to see if it works better.

For your other issue - are you saying that sometimes the zone repops but the mob in the room doesn't if you're playing dance of the seven luck gods?  Is there a mob in particular you've seen this with?  I'll have to build a bard to see if I can reproduce it.

</div>

<div class="post" data-post-id="38386" data-author="Teron" data-date="2017-08-07T08:05:58+00:00" data-subject="Re: Spirit watchers don&#x27;t warn about mob repops.">

Unfortunately, I forgot most the mobs that behaved like this.

I remember the zeridan leader and Iqzz, but I've just tested that the Lightning Extension doesn't repop with people in it.

I'm sure there was at least one mob like this, though. I guess I'll keep testing.

</div>

<div class="post" data-post-id="38389" data-author="Teron" data-date="2017-08-09T05:33:45+00:00" data-subject="Re: Spirit watchers don&#x27;t warn about mob repops.">

Watcher with fastrepop on the continent works.

Haven't tested luck gods yet.

</div>

<div class="post" data-post-id="38399" data-author="Teron" data-date="2017-08-15T07:16:32+00:00" data-subject="Re: Spirit watchers don&#x27;t warn about mob repops.">

A good number of areas are no repop, so luck gods don't work there.

Instead of debating, whether to make those areas repop with people, how about excluding the bard, who is singing the luck gods, from the people counter, so areas repop with him?

This would keep areas norepop as per design, and would make the bard useful in those areas.

</div>

<div class="post" data-post-id="38400" data-author="Josiah" data-date="2017-08-17T04:35:55+00:00" data-subject="Re: Spirit watchers don&#x27;t warn about mob repops.">

Excluding a bard singing luck gods from 'counting' as a player in the area would be a slick solution if it can be implemented.

If there is a concern that allowing an area to repop with a player inside might break some special quest zones... it can already be done either via Limbo or Linkdead status, so at least it won't make any new exploits.

</div>

<div class="post" data-post-id="38401" data-author="Gorka" data-date="2017-08-17T06:06:27+00:00" data-subject="Re: Spirit watchers don&#x27;t warn about mob repops.">

Why do regular areas (not quest areas) not repop with people in them anyway?  Is there actually a reason that adds to gameplay? Is there actually a point?

The only "benefit" I can think of for this "feature" is that hunting or scanning aggro's could be cleared to kill bigger mobs without getting yourself slaughtered by a surprise re-pop.

It needs to be recognised that if the changes went in that you guys are suggesting bards would no longer be able to clear some areas safely... is that a decision you're actually happy with... would it only lead to other disadvantages for the bard class? I suspect you guys aren't thinking through the whole issue, you've only thought about the advantage of singing for pops. What do other bards think?

Be careful what you wish for...

</div>

<div class="post" data-post-id="38402" data-author="Teron" data-date="2017-08-17T13:31:14+00:00" data-subject="Re: Spirit watchers don&#x27;t warn about mob repops.">

Gorka, re-read what I wrote.

Only bards singing the luck gods song would not count.

Ie:

- bard starts singing

- area repops

- bard checks the mob

- bard recalls or goes to a safe place within the area.

What is the problem here we don't see?

</div>

<div class="post" data-post-id="38404" data-author="Gorka" data-date="2017-08-17T15:28:04+00:00" data-subject="Re: Spirit watchers don&#x27;t warn about mob repops.">

Firstly, I read your post once... I don't need to read it again because I'm stupid.

Secondly, when you say "What is the problem here we don't see?" who is WE? 

It's funny how when I state my opinion and it happens to cross yours, I'm instantly somehow inferior and I need to re-read something, and you insinuate that you speak for a majority... yet if I point out the flaws in the ways you try and compel the people around you to get what you want, it's dismissed as a personal attack. 

Area's that don't repop with people in them is potentially a feature... it means a person does not have to kill all the aggro mobs in area a second time, when they are in there for a prolonged period, trying to kill something else. 

Area's repopping while you are in them might suit you, but it could also effect all bards in another negative way. All I am pointing out is that the change you suggest also has a potential draw back, that needs to be considered.

</div>

<div class="post" data-post-id="38405" data-author="Teron" data-date="2017-08-17T17:07:04+00:00" data-subject="Re: Spirit watchers don&#x27;t warn about mob repops.">

Please point out how exactly this change will negatively affect other bards.

</div>

<div class="post" data-post-id="38406" data-author="Gorka" data-date="2017-08-17T18:31:20+00:00" data-subject="Re: Spirit watchers don&#x27;t warn about mob repops.">

Hypothetical scenario...

Say I was a bad ass Bard, wishing to cycle the mana gator (mage style)... First I need to kill all those crappy eels before I could take on the mana gator. If I was a bard, with the changes you supposed... the bard would probably not have enough time to kill the eels, regen and mage style the mana gator before the eels repopped. If the area remained - no repop with people inside, he could regen in the area, kill the eels and kill the mana gator at his leisure.

I don't think areas not repopping with people in them was meant to be a pain in the ass... It was actually designed to assist players trying to clear an area so aggro's would not repop on them unexpectedly. I'm merely pointing out the problem has two sides. It may well be the imms make a change, maybe they don't, maybe my point is not the same weight as being able to sing luck gods in all areas... But let us consider all things... not just the things that suit us. 

I've been pondering how I can do something like this in DOT in regards to Vain. I don't want to have to kill the aggros in the hallway every repop before I get to Vain, but with your changes... a bard will no longer have that option, everything will repop on him. That is not always an advantage.

</div>

<div class="post" data-post-id="38407" data-author="Gorka" data-date="2017-08-17T22:32:36+00:00" data-subject="Re: Spirit watchers don&#x27;t warn about mob repops.">

> **Teron wrote:**
> how about excluding the bard, who is singing the luck gods, from the people counter, so areas repop with him?

Ok, I think I've made a mistake in my understanding of your position. The bard has to be actively singing Luck Gods not to count, not just be a bard... It's an AND condition. If you read your sentence again it can actually be taken to mean different things. You could be clarifying what a bard can do - sing luck gods, or specifically highlighting a specific bard if there were more than one - the bard who is singing luck gods (because you then mention people which is plural). I see now you probably meant the character is a bard AND it is singing luck gods... but the emphasis of the sentence is placed on "excluding the bard." Using comma's doesn't mean things are happening at the same time, it only implies relationship between the statements. The only reason I picked this up was because Josiah clarified your statement underneath, and the penny dropped you probably meant that both things were true simultaneously at the same time.

If the Bard has to be singing Luck Gods to be excluded from the count then you are right, it doesn't disadvantage bards in any situation. If bards were excluded simply because they were bards, then the situation I describe would be true. 

It might be tricky to determine where this behavior is allowed or not. For example the vampire_slayer quest... just by looking at the room data, there may be no flag to say that this area is a special case where this behavior must be an exception to the new rules. How would the mud know that doing this on EU is ok, but the vampire_slayer quest zone is not ok. It would need a flag to determine when to toggle this new luck gods behavior. The basis for that flag might not exist in the pre existing data. I doubt the imms will accept Josiah's quip about the situation already being exploitable as a reason to turn a blind eye to introducing yet another exploit.

</div>

<div class="post" data-post-id="38408" data-author="Teron" data-date="2017-08-18T09:33:04+00:00" data-subject="Re: Spirit watchers don&#x27;t warn about mob repops.">

> **Gorka wrote:**
> If you read your sentence again it can actually be taken to mean different things. You could be clarifying what a bard can do - sing luck gods, or specifically highlighting a specific bard if there were more than one - the bard who is singing luck gods (because you then mention people which is plural).

The sentence means one and only thing in this context, and I'll do my best to clarify it beyond reasonable doubt.

I never thought studying English in the university and English grammer 5 times over the course of my life would've come ultimately useful, but today is the day.

Sentence:

"how about excluding the bard, who is singing the luck gods, from the people counter"

What we already know: if there is anyone in the area, it doesn't repop. Hence the name, people counter. 

People is used to differentiate between players and mobs, not to denote plurality (people vs a player), because it doesn't repop with 1 player as well.

Note: it also doesn't repop with familiars, so we can rename it to Player Presence Detector.

I'll spare us both the use exact grammar terms and will attempt to describe the syntax as simply as possible.

The complex sentence consists of two parts:

1. how about excluding the bard from the people counter

2. who is singing the luck gods.

1. is the main part, 2. is the subordinate clause, which are separated by a comma, because we need commas to separate subordinate clause from the independent parts of the sentence.

1. how about excluding the bard from the people counter

It can be rephrased to how about you exclude the bard.

> **Gorka wrote:**
> but the emphasis of the sentence is placed on "excluding the bard."

Well caught: this is indeed the main part of the sentence. Hats off to Gorka!

2. who is singing the luck gods

This is a descriptive dependent clause, because it describes the object in part 1: a bard, which one? the one, who is singing luck gods. It can't exist without the object it describes, because it describes one and only thing, the bard. Therefore, the bard can not be excepted from being considered to be singing luck gods.

> **Gorka wrote:**
> Using comma's doesn't mean things are happening at the same time, it only implies relationship between the statements.

comma itself does not denote a time, but the tense a verb is used in does.

"is singing" is in a Present Continuous Tense, which denotes what is happening at the very moment. In the sentence, the moment is that of the repop: the bard is singing, when the area repops - after that he can stop, for what we care (he/she usually does, no point singing luck gods immediately after repop).

Therefore, the suggestion means one, and only thing: to exclude the bard, who is singing luck gods, from the player presence detector.

So far I've used just the English grammar to arrive at the one and only meaning of the sentence. But let's dig deeper to dispel your doubts.

> **Gorka wrote:**
> You could be clarifying what a bard can do - sing luck gods

No, because this is a prime skill - only bards can sing luck gods. I wouldn't even need to mention luck gods, if I wanted to mention a bard prime.

If I wanted to say "a bard, who can sing luck gods" as opposed to a bard, who can't, then I'd have said "a  bard, who has luck gods learned".

> **Gorka wrote:**
> If you read your sentence again it can actually be taken to mean different things. You could be ... specifically highlighting a specific bard if there were more than one - the bard who is singing luck gods

If we place the sentence in the context - which is that right now no players present allow the area to repop - then we see that the bard is opposed to other players, not other bards in the area.

it is not:

- two bard are present, one is singing, one is not

- two bards are present, both are singing

- two bards are present, none are singing.

It is a singing bard vs all the other players for the sake of the context and the suggestion.

The sentence does answer, whether the area repops in the following conditions:

- two bards are present, one is singing, one is not

No, because one is not singing

- two bards are present, both are singing

Yes, because both are singing

- one or more bards are present, none are singing

No, because they aren't singing.

And lastly, if you use the Occam's razor, and use only the information given in the suggestion without assuming anything out of place, then you'll still arrive at the only possible conclusion - which I assume you did.

Therefore, I believe the suggestion should only be understood in one and only way possible: to introduce the code, which would allow the area with a bard, who is singing the luck gods song at the time of the repop, to repop.

Now, about the quest areas.

As far as I remember, the quest areas are made norepop for the same reason as other areas: it makes it easy for others to proceed. In one case, a mob blocks the passage, afair.

I don't see why a bard would need to reset a quest area to slow down his quest progress. 

Of course, it is possible he might want to pop several sets of quest items, but there's the thing: quests can only be completed once. Twice, if you rebirth. I'd say it's a bit farfetched that a bard would get to quest area and sing luck gods just to get quest items for his rebirth.

Even if we assume that a bard would be persistent to do such a thing, this can be easily circumvented by setting quest area repop timer to 20 days or never. It'd save Teker's time to add area specific flags for quest areas. If quest areas have a separate quest-area tag, then it could be updated to never let quest areas repop.

</div>

<div class="post" data-post-id="38409" data-author="Gorka" data-date="2017-08-18T13:08:45+00:00" data-subject="Re: Spirit watchers don&#x27;t warn about mob repops.">

I'm honestly amused... I think I'll stay off the crier for a bit... email the imm's directly if I have any questions or problems lest I disturb the forum Balrog again.

</div>

<div class="post" data-post-id="38410" data-author="*teker*" data-date="2017-08-19T22:11:37+00:00" data-subject="Re: Spirit watchers don&#x27;t warn about mob repops.">

This isn't something that I'll look at changing unless a builder comes to me and wants a particular area to work differently.  I imagine the current behaviors are the way they are because that's how the builder wanted each particular area to play out.  It takes a lot of time and effort to build an area and I don't feel like I should be overriding their designs unless asked to by the builder.

</div>

<div class="post" data-post-id="38411" data-author="Teron" data-date="2017-08-20T07:13:01+00:00" data-subject="Re: Spirit watchers don&#x27;t warn about mob repops.">

This isn't about changing areas, this is about making luck gods work, where it can't now.

some norepop areas were made before the song was introduced, and there are more norepop areas, than people think.

ie, right now, all of the EU extensions are norepop, as well as Air Plane, Tabaxi Wilds, Mercurial Woods - these are just off the top of my head.

I have talked to Neptune about EU, but he said he didn't have time to think about it.

</div>

<div class="post" data-post-id="38413" data-author="Teron" data-date="2017-08-22T08:18:11+00:00" data-subject="Re: Spirit watchers don&#x27;t warn about mob repops.">

Right now a watcher is telling me that the mob is coming, but never tells me, when it does.

</div>
