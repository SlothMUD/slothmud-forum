---
title: "Where to go with coli"
topic_id: 4731
author: "*juggleblood*"
date: 2017-01-22T00:33:48+00:00
last_activity: 2017-01-26T20:01:18+00:00
last_author: "*juggleblood*"
sticky: false
locked: false
post_count: 7
---

<div class="post" data-post-id="37982" data-author="*juggleblood*" data-date="2017-01-22T00:33:48+00:00" data-subject="Where to go with coli">

Several of the rebirths seem to be disappointed that there's no coli for them.  My reasons for closing it to them are two-fold, one is that it creates an unfair playing field and we've been working really hard to accomplish that, the other is that I don't want the scores to get a lot higher, because in my opinion too much honor and drachma comes from coli already. Pushing scores up in every level would make it even more important for rank and drachma gear and some people aren't that interested in doing the coliseum.

So I'm thinking of maybe putting my AH Coliseum into play. I built it a couple years back, it's more or less a clone of the other coliseum but with completely different mobs. It's not fully flushed out yet because I never decided exactly where to go with it. 

My thought is put this one into play for everyone, rebirths included. Thinking maybe make it harder, lower scores, for drachma and making it pop the quest loot (coli loot stuffs). Thinking maybe the quest loot pops when your score reaches a certain thresh-hold and also is a personal best. So for example the min score might be 10, and when you get your 11th 12th ... kills the audience starts throwing this loot at you after the kill. And I'm thinking in this coliseum, you can use any pots you want. So there won't be farming of loot here. People will use the loot to get better scores and besides that they can't farm unless they constantly make new characters to do so, and it wouldn't be worth it.

Or not. I'm open to whatever. I'd be interested in hearing what non-rebirths think about re-births in the existing coli even.

</div>

<div class="post" data-post-id="37983" data-author="*Idjit*" data-date="2017-01-22T05:36:11+00:00" data-subject="Re: Where to go with coli">

I thought about this, for rebirths for the existing coliseum, and what I thought was:

Just to address the specific people who were already like 8x40 when the coliseum was first brought in:

(so they never got a shot at the lower chambers their first run-through).

Single-use passes for each chamber (which would I guess be handed out manually, or it could be automated).  You get -one- shot in each chamber, period, (or a very small number of fixed tries, like 3 or 5 or something) and the pass checks for whether you have ever had a score in the score listings before for that chamber, and checks how many tries you have left, I was initially leaning toward having only one try though.

So for the one-use idea, it would just not let you in if you already have a score for that chamber.

You'd have to have a means for checking the existence of a score, or absence.

Just a thought.

--D

</div>

<div class="post" data-post-id="37984" data-author="*Idjit*" data-date="2017-01-22T05:58:12+00:00" data-subject="Re: Where to go with coli">

Depending how excited you are about the preceding idea, you could tailor the max number of tries and have fewer tries for the lower coliseums (where we are concerned about abuse mostly and where the highest scores would be), and dole out larger # of tries (but still not very many, like 7) for chambers 3x40 and up where a good score for the casual coliseum goer is only 5 to 10 kills anyway against those tougher enemies.  

Zuzu's fairly crunchy, I can't see him getting more than that in the middle chambers while he's still middle-sized.  Can't speak for our beefier rebirthers (should there be any).

Or keep it very simple and only have one run, as I'd said.

--D

</div>

<div class="post" data-post-id="37987" data-author="Gorka" data-date="2017-01-22T09:45:31+00:00" data-subject="Re: Where to go with coli">

I like the coliseum, I like sub games in games. I like the loot, I like how doing something 10000 times teaches you about the game and efficiency. I think the coliseum is a great sub game in sloth. I support all new ideas and expansions.

Doing the coliseum again for me, was an attractive part of re-birthing... I'd be far less likely to go through the short term hassle of rebirth without this. So I support finding a way to let rebirths back in for repeat drachma.

However as a programmer, I'm a little worried that a "second coliseum" will just end up being more maintenance for you JB. As times change, you end up having to make the same changes in both coliseums, and also the same mistakes etc. Two coliseums is a duplication of effort, this will be a burden.

I'm sure MUDL has some severe limitations, but in an ideal world, there would be only one coliseum, and the coliseum adapts to the player circumstances... ie, level, rebirth status, using loot, not using loot by selecting a config. This would mean new ideas could be implemented rapidly, just by changing or writing a new config or by adding new systems to the config.

CONFIG_NAME=SPECIAL_CONFIG

ALLOW_PETS=1

ALLOW_USE=1

ALLOW_QUAFF=1

ALLOW_REBIRTHS=0

FIGHTING_TIME=8mins

HAS_SANCTUARY=1

USE_RANDOM_MOBS=0

LOOT_SYSTEM=POTIONS

DISTRIBUTION_SYSTEM=INCREASE_LOAD_WITH_KILLS

etc

(In each config file you store the high scores for that config for all the levels)

There is a problem linking the "drachma reward" with the number of kills you have at the moment... because these records exist just inside that coliseum config. So if the coliseum was to have different "modes" or "configs" you would need to store high scores for each of the modes. In my opinion the only mode to give drachma, should be the way it is now... but without the effect of astrology. 

I'd suggest two modes... 

1) A tightly controlled mode, which gives the drachma reward as what we have at the moment minus astrology.

2) An any thing goes mode, with randomly generated "gladiators" which load loot as kills get higher.

But my main point is, you don't need two coliseums, you need a strong config based system or else the setup and maintenance and future implementation of ideas will be extremely difficult.

As for coliseum mobs, although having 10-15 static mobs kind of keeps the coliseum "even" for all players, it makes the coliseum a bit static. I'd be inclined just to name each mob "a Gladiator", but give it random and dynamic attributes... players will not be able to script to the mob because of the mob name, they would have to adapt during the fight to the mobs tolerances as they discover them... It makes botting more challenging. If mobs don't have names, I will not know if it's ether, is it fire tolerant, will it reflect my spell? which leads to some excitement. Any competent player at the moment will have an efficient script for each mob name they meet in the coliseum, that should be taken away from them. This is a great idea I feel for the "anything goes mode." Obviously no drachma reward in this mode maybe some loot/coins load as kills pass a certain amount.

Lastly I offer to help you make it, or work with you to design the config system if you need. A good program breaks down into hundreds of little modular sub systems that can be turned off or on by using configs. This is also how I script in sloth mud for everything. Each sub part must be modular and self contained. Each system must be able to be turned off or on depending on the config. New systems can be added later, and added to configs making the whole system more maintainable and expandable. This will save hours in the long run.

</div>

<div class="post" data-post-id="37988" data-author="*juggleblood*" data-date="2017-01-22T13:59:34+00:00" data-subject="Re: Where to go with coli">

The main limitation we have to stick by is that there would be no incentive to run thru it / farm it forever. No forever loot of any kind. It has to be a game to be played for it's limited objectives and then ends.  Otherwise it becomes a botting chamber like before.

As to the design of the coli. Each sign object is basically a self-contained coliseum game. So there isn't one coliseum, there are 12 (Newbie, 0-9, and chaos pit). From my perspective it's easier to not touch (break) the existing coliseum, and instead tinker with a new one.

Regarding a limited number of attempts, I think it would be very unsatisfactory to people for a number of reasons, the randomness of the mobs you draw, the imperfection of the timers, game-side lag spikes, crashes, player side connection loss, etc..

</div>

<div class="post" data-post-id="37993" data-author="Teron" data-date="2017-01-23T15:24:10+00:00" data-subject="Re: Where to go with coli">

I think you overestimate how good rebirths are or will be at the coliseum and how easy it is to get high scores.

You also need to shift your expectations about the maximum number of kills, because you haven't accounted for eqset, maxmana sets and maybe how efficient scripting can be in killing mobs.

Firstly, it takes a huge time investment to:

- polish your scripts

- get the gear

- run the level repeatedly to learn mobs, timings and how to do set switches efficiently.

The difference between a committed character and a newcomer to the coliseum can be 20 kills.

Secondly, the drachma eq rebirths have will gradually let them get maybe 5-10 kills more for each level. This isn't something to write home about, unless you are a mage and your remort bonus greatly affects your scores. Even then, just look at Mage's scores: he had frostbolt, the best mage eq, a remort bonus and still couldn't top some of the early levels, which he did without astrology.

Thirdly, a bigger point is people, who haven't participated in some levels at all. I can't speak for everyone, but I have started in coli at level 5. And I got good at this at level 7. So I'd like to retry the first 6 levels, and maybe the others, too, but even as a remort/rebirth, I doubt I'll be able to top the latter by more, than 5 kills.

So 20dr for repeat entry or 80dr for 1st time level entry, that's a big difference and first time level entry should be the main point of the discussion, rather than repeat entry.

If you are concerned about the scores, then adding (Rebirth #X) after the name would fix the comparison issue. 

Coliseum is a great part of the game, and having rebirthers reenter it isn't that groundbreaking. Removing access to it feels like a penalty.

You could nerf drachma rewards for rebirthers, but let them in and tally their scores with the abovementioned mark. However, nerfing drachma doesn't seem welcoming.

</div>

<div class="post" data-post-id="37997" data-author="*juggleblood*" data-date="2017-01-26T20:01:18+00:00" data-subject="Re: Where to go with coli">

Well so far, players are more in favor of allowing rebirths than not. Not a single person has offered the opinion that it's unfair.

So now that the skills issue for rebirth is sorted, and we are forcing remove all at rebirth, I'm inclined to simply remove the prohibition.

This is the last chance to speak your peace and say it's unfair. If we go this route and let them in, I'm not reversing course or listening to complaints down the road. This is it, rebirths in or rebirths out, speak now or forever hold your peace.

</div>
