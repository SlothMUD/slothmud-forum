---
title: "Save state of loaded EQ to save it through crashes/reboots"
topic_id: 4768
author: "Teron"
date: 2017-06-14T15:05:34+00:00
last_activity: 2018-05-04T14:46:21+00:00
last_author: "Teron"
sticky: false
locked: false
post_count: 34
---

<div class="post" data-post-id="38284" data-author="Teron" data-date="2017-06-14T15:05:34+00:00" data-subject="Save state of loaded EQ to save it through crashes/reboots">

Greetings.

Problem:

We spend hours of time and effort to cycle certain mobs and pop items, ranging from specs to biggest mobs in the areas only to lose loaded items on crashes/reboots. This is greatly disappointing and means that we waste hours of our life for nothing - even if playing a text game is a fruitful pursuit.

It means that to pop the item again, the players not only need to kill an empty mob - right now most mobs appear w/o eq - but spend the same time/effort to pop the item(s) again.

Solution 1:

Save the state of items in use on mobs larger, than 5mil, every repop (ideally, all mobs > 1mil)

When a crash occurs, load that state of eq.

If there were no items, allow the few of the items - mostly books/keys/etc- load on crash/reboot as they do now.

The only exception is choppers we pop: we typically drop them on the ground, since we need tons to lead large groups, especially, if taking into account breaking specs.

Solution 2:

Load items on kill.

It'd help if choppers on the ground remained on the ground as well.

Keeping spellbooks in the libraries might be helpful as well.

To demonstrate the problem, I am and will be posting items with:

- which items were lost and how many of them

- effort required to pop them

- when it happened.

I'll start with:

1. Before June 12th: I spent about 8-12 hours across 3 days to pop 30-40 specs total before they are poofed on crash. I pop another batch, and it crashes again. It crashed 3 times on me, and I kept popping specs, and then it crashed again. I popped them again. I wonder, if this is a sign of a mad addict, than a healthy person.

2. June 12th:

Neptune pre-loaded eq on 150-200mil mobs.

A group of 6-7 spent at least 3-4 hours killing 1 200mil mob per run, which later popped.

There were 5-7 items I knew - about 3 were actually popped, not Neptune-loaded - that were lost in a scheduled reboot 24hr after the quest.

3. June 14th.

Ezekiel and I have spent at least 4-5 hours popping specs, solo, 2man and in a chop group.

About 20+ specs were lost in a scheduled reboot.

A found shaping peri.

4. Every time a crash/reboot happens, the fargate we enable manually is reset and not renewed.

It takes at least 5-9 min for 2+ 9x40 players to regen for the kill, and after the kill.

5. Countless times, when I have killed a big mob, went to bed, only to find that the MUD has crashed/rebooted, while I slept, leaving it a mystery, whether it loaded.

Sometimes I wonder, if I should bother with popping specs or enabling fargate.

Now I wonder, if I should bother cycling eq.

I invite players to share their stories of lost items: please tell us, when the items were lost, the effort required to pop them and how many of the items were lost.

I'd appreciate, if immortals fix this black hole of eq - and I'll be providing feedback as long as this bug lives.

Thank you.

P.S. If someone wants to tell me that popping eq isn't what we play for: play how you want, but do not tell me how to play the game

P.P.S. I'd like to note that some imms do:

- save choppers, if they are on

- re-enable fargate, if they are present - but not always

- enable random extra bonuses.

However, this isn't an imm rule, more a whim, and random extra global bonuses - except gempop - don't compensate for lost pops, only for the loss of aged exp on mobs.

</div>

<div class="post" data-post-id="38285" data-author="Tuck" data-date="2017-06-14T19:47:00+00:00" data-subject="Re: Save state of loaded EQ to save it through crashes/reboo">

easy solution:

just make a room, e.g. south from lyme inn, where all specs/choppers saved upon reboot/crash. or reboot atleast ;)

thanks in advance

</div>

<div class="post" data-post-id="38286" data-author="Gorka" data-date="2017-06-14T22:31:25+00:00" data-subject="Re: Save state of loaded EQ to save it through crashes/reboo">

I sent this is Teker, Jan 4th...

> **Quote:**
> Teker,
> 
> 
> 
> I write to you to suggest the idea of storing a partially saved state of the mud for reloading on crashes or reboots. Probably not a new idea to you... but I thought I'd suggest anyway. The reason I write today was because I had just spent ages killing Iblis when the game crashed... I was literally carving his corpse when it crashed... it's very frustrating.
> 
> 
> 
> My idea is two fold...
> 
> 
> 
> * Store when a mob is dead (Mob Killed Event).
> 
> * Store items loaded by a mob (Mob Spawn Event).
> 
> 
> 
> This way when the mud crashes... if the mob was saved as being dead, it could respawn the mob under the normal eq popping rules... and if the game crashed when the mob had loaded something, that item could be reloaded.
> 
> 
> 
> Now I know databases could slow the performance of the mud... but in this case I suspect it won't... because the saving of this data only occurs on zone resets or on mob deaths. As we would only be storing the mobs that are currently dead... this would be a smaller list than "all mobs in the game at the time." Likewise storing the loaded items... it's also a smaller list, than mobs without items.
> 
> 
> 
> Needless to say how popular this idea would be with players... simply for the reason it's fair to players... well currently nearly every single crash or reboot is a major disadvantage for players...
> 
> 
> 
> In my case today I lost the xp from Iblis, his coins (500k), 30 tokens on the floor of my vault for my newbie, a chance for Iblis to load, and 1mill worth of potions.
> 
> 
> 
> Regards,
> 
> Gorka

There was some talk that doing this might decrease the performance of the mud, but frankly areas only reset every 30mins, and storing that a mob has been killed to a file shouldn't be much more load than the game already does to unload it from memory. There was talk that if the mud crashed these saved state files might be corrupted, but how is that not the same problem with player files... and does/has that even happened?

</div>

<div class="post" data-post-id="38287" data-author="Teron" data-date="2017-06-15T08:56:57+00:00" data-subject="Re: Save state of loaded EQ to save it through crashes/reboo">

Yeah, I don't see how saving state on repops (the mob will be dead just before, alive and empty or alive with item) would strain the database, it's just another point of data that doesn't have to be continuously monitored.

In MMORPGs items pop on death, so you don't have to kill the empty mob twice to get it and don't have to worry about losing pops on crash, because you can kill the mob right away after the crash.

While eqpop-on-death solves the item loss problem, we'll probably miss seeing that green text in the mob's desc, when it repops loaded. Then again, the uncertainty of pop, the randomness of chance to pop the item on its death might give us more motivation to kill mobs, rather than knowing 100% that the mob we are killing is empty.

It'd make killing an eq mob once during exp groups a more viable possibility, which we already do, but then an exp group wouldn't have to kill an unaged mob, if it pops.

Of course, personal items would have to be dropped on the ground outside the corpse, and people will have to eliminate "get all" triggers - I don't even have one, anyway.

</div>

<div class="post" data-post-id="38288" data-author="Gorka" data-date="2017-06-15T09:42:32+00:00" data-subject="Re: Save state of loaded EQ to save it through crashes/reboo">

There is another side to that idea Taron, you won't be able to rally a group together based on the premise that something loaded, and players generally help each other out in those situations. That's not really a bad thing, it's just different.

I certainly hate how the 1st kill is nearly always empty... that's kind of stupid.

</div>

<div class="post" data-post-id="38289" data-author="*Splork*" data-date="2017-06-15T11:46:06+00:00" data-subject="Re: Save state of loaded EQ to save it through crashes/reboo">

At one time, we were saving the states of all creatures which were either A) loaded or B) dead. If the game crashed or rebooted A) the item was either placed back on the creature(if it was over a certain value) or B) the creature had a chance to load that item.

I can't remember what caused that code to stop working or why it stopped working. However, we have discussed this issue and it will be addressed.

</div>

<div class="post" data-post-id="38290" data-author="Teron" data-date="2017-06-15T13:55:25+00:00" data-subject="Re: Save state of loaded EQ to save it through crashes/reboo">

Gorka, you see, mobs don't pop good eq on crashes/reboots, so what you are talking about is:

- a group kills a large mob

- the tank or a few people leave

- someone notices a big mob loaded

- they start calling for help

 1) if they succeed, they get the pop. Hurray!

 2) if they fail or go to sleep, hoping it wouldn't crash, they don't get the item - this happened to me at least twice, because I was dead tired in the early morning.

However, I don't remember anyone calling for help right after crash with, "Help, a mob loaded cool eq on crash, let's get it!" The closest I can think of is Luci, but Luci loads during a house, not with the game.

What you are really talking about is a problem of killing the mob for the 2nd time to get the pop.

This problem - whether waiting for repops, waiting for people or leaving and losing a pop - is completely eliminated by popping eq on death.

Strictly speaking, the game theory dictates that we need a random chance to pop the item, not a certainty, as far as I know.

Splork, I appreciate your chiming in.

It's a good thing that there was once a solution.

As far as I remember, this was manually changed in late S2 or S3, because people were crashing the mud intentionally every 5-20 min to get a pop. One time, there were 3-5 crashes in an hour. This was in the era, when uptime of 5 days was great. and 3-4 days was good.

I guess you need to look at whether players know crashable bugs, and go from there.

Then again, even if there are player-induced bugs, it'd be interesting to trust them and see, whether the players abuse it. I hope that they wouldn't, since Teker tracks down crashes, anyway.

</div>

<div class="post" data-post-id="38291" data-author="*Splork*" data-date="2017-06-15T14:02:34+00:00" data-subject="Re: Save state of loaded EQ to save it through crashes/reboo">

At one time, we had the game coded so that any mob on reboot could load equipment. That is when we had an issue with players purposely crashing the game.

We then manually removed that code and Rita eventually coded the solution that I posted above. With the above mentioned solution, there is no reason to purposely crash the game.

Also, our logs are a million times better now. Anyone caught purposely crashing the game would be wiped immediately .

</div>

<div class="post" data-post-id="38293" data-author="Teron" data-date="2017-06-15T15:51:52+00:00" data-subject="Re: Save state of loaded EQ to save it through crashes/reboo">

Ah good.

Then it'd be great to get it implemented.

I'd appreciate, if you keep us informed.

Also, what do you think about popping eq on death?

Thanks.

</div>

<div class="post" data-post-id="38304" data-author="Teron" data-date="2017-06-25T10:36:05+00:00" data-subject="Re: Save state of loaded EQ to save it through crashes/reboo">

Manual reboot, June 24th.

Lost a pop from the mob that's behind the door, which is unlocked by the song of the luck gods, in the temple of Mnemosyne.

Yeah, I forgot it was loaded to warn Neptune of it, but then I doubt there was enough ppl for that mob.

</div>

<div class="post" data-post-id="38307" data-author="*teker*" data-date="2017-06-27T21:01:23+00:00" data-subject="Re: Save state of loaded EQ to save it through crashes/reboo">

I've written the code to save the list of mobile carried/equipped items at shutdown.  It will go in with the next reboot.  I have not added code to use that list at boot.

Question: What criteria should I use to repop an item?  I'm not going to repop 100% of what is in the file.

</div>

<div class="post" data-post-id="38308" data-author="Gorka" data-date="2017-06-27T21:15:56+00:00" data-subject="Re: Save state of loaded EQ to save it through crashes/reboo">

> ***teker* wrote:**
> Question: What criteria should I use to repop an item?  I'm not going to repop 100% of what is in the file.

I don't follow what you mean here, why not load what was already loaded if the game is going down for reboot?

</div>

<div class="post" data-post-id="38310" data-author="Teron" data-date="2017-06-28T13:16:21+00:00" data-subject="Re: Save state of loaded EQ to save it through crashes/reboo">

I'd load:

- held/worn equipment

- on mobs, larger than 1mil

- on valk, on mobs, larger than 50k

What is the restriction of the load list in your opinion, Teker?

Is there a way to add choppers to the list?

Teker, what do you think of loading eq/items/books on death?

</div>

<div class="post" data-post-id="38312" data-author="*Breeze*" data-date="2017-06-28T18:12:23+00:00" data-subject="Re: Save state of loaded EQ to save it through crashes/reboo">

if he reloads everything, then eventually there would be a bunch of junk loaded on monsters that no one will kill and it will make sloth use up more and more memory.

@teker - make a way to disable that feature? possibly a config that is set before a shutdown so it wont save ..

</div>

<div class="post" data-post-id="38313" data-author="Gorka" data-date="2017-06-28T19:49:18+00:00" data-subject="Re: Save state of loaded EQ to save it through crashes/reboo">

I see what your saying, but find it hard to believe that over time the mud would incrementally load with significantly more items because no one killed since the last reboot, to the point of putting a strain on memory. Is unpopped items on unrun areas really that much of a bigger problem? I mean half the mud hardly gets run, it's not for nothing I am 9x40 and my exploration is on 50%. If it's not being run, it's likely going to be empty anyway. The information in the file will be a good indication of what not to bother loading the first few times, until some filters could be implemented. Why not wait, and see how it pans out so the filters can be properly set. 

The other suggestion is, perhaps there is a way to log  a timestamp when the item loaded... you could clear out the crap by the timestamp if it's a certain age.

</div>

<div class="post" data-post-id="38314" data-author="*Splork*" data-date="2017-06-28T20:56:39+00:00" data-subject="Re: Save state of loaded EQ to save it through crashes/reboo">

The last code used value of item and other flags to exclude saved items.

Hundreds to thousands of items can be loaded at any given time. There is no sense in saving(and loading) small treasures and junk items....

</div>

<div class="post" data-post-id="38315" data-author="Teron" data-date="2017-06-29T07:59:50+00:00" data-subject="Re: Save state of loaded EQ to save it through crashes/reboo">

1. I'm not sure, if I was clear.

I meant held/worn items on mobs, larger than 1mil.

It shouldn't be a whole lot, and, like Gorka said, we are not killing the entire MUD. We are killing mostly same mobs - the issue is for items to stay long enough until we go back and kill them.

2. Some good items have low item value, and relative junk has high value, so it's better to go by item type.

3. I'd just start with some settings, go from there and see, if you can add/remove filters without eating tons of memory.

4. Both issues of not getting an item on repop and having tons of items loaded can be solved by loading items on death. What is your opinion on this?

The only exception I see is personal quest items, because we need to know, whether it loaded beforehand, so the looters are off/on - or there needs to be a separate load mechanism/message for personal items, so they are not looted immediately.

</div>

<div class="post" data-post-id="38316" data-author="Gorka" data-date="2017-06-29T12:28:42+00:00" data-subject="Re: Save state of loaded EQ to save it through crashes/reboo">

It's difficult to determine an item's true value these days by defining conditions based on object attributes.

A lot of cp's have almost no object value, a lot of what is worn is junk. Even food items are used in some quests as well as spellbooks. It would be extremely difficult to set conditions on what reloads based on object attributes without applying rules unfairly.

You could avoid using object attributes and use a timestamp system like I suggested to stop scum settling in your reload file... or you could bite the bullet, and fix object values and types. You could kick the can down the road a bit and just watch for the scum in the bottom of the file while it's worked out.

Ideally object values need fixing, that's the purest solution... also the most work. 

Regarding popping the items on death... solves a lot of problems I agree... but also I have some reservations... it's just so "sloth" that it works the way it does. It would be like a food company changing the recipe of an established product after 20 years... Even though it might be better... you just don't do that. Imagine Coca Cola dumping using sugar out of there regular product. They have been farting around with all these alternatives, but for all it's sugar, the original coke is something I doubt they can ever change or get rid of without massive upset... you don't change legends.

</div>

<div class="post" data-post-id="38317" data-author="*Splork*" data-date="2017-06-29T17:41:34+00:00" data-subject="Re: Save state of loaded EQ to save it through crashes/reboo">

I'm not so sure I like the idea of changing how items are popped. 

I think the new code will solve the majority of issues and concerns which have been raised.

</div>

<div class="post" data-post-id="38318" data-author="*teker*" data-date="2017-06-29T18:55:32+00:00" data-subject="Re: Save state of loaded EQ to save it through crashes/reboo">

I'm hoping that once we get the code in place I can analyze a sample file and try to build rules based on the data.  I'll know a lot more once I can look at a real sample.  I've had an issue pointed out that I hadn't known about, so I'm still working on making the save function function work properly in all cases.

We can currently pop items on death using procs - the prisoner in Castle Zodiac is an example that pops some items normally and atleast one via proc.  One disadvantage of doing this for all mobs is that Wealth and Glory would have to be rewritten as it doesn't know how to handle proc pops (like Maleficent).  Currently all data for pops is stored on the room in which the pop happens - that would also have to change so that the mob can pop the appropriate items after roaming.  It's a little tricky since we can pop multiple identical mobs in the same room but pop different items on them.

</div>

<div class="post" data-post-id="38319" data-author="Teron" data-date="2017-06-30T04:09:29+00:00" data-subject="Re: Save state of loaded EQ to save it through crashes/reboo">

The amount of totally useless worn items is minimal, afaik, since they don't all load at once.

There are several ways to filter, but I imagine all ways to filter have to be factored in, not just one or the other.

Items loading on mobs rather than on death is not Sloth, it's just all or most of the early MUDs, because that was the only way to do it, as far as I know.

The lazy, slothy way would've been to actually load items on death, so we kill mob once to have a chance to pop and get the item, and carry on.

</div>

<div class="post" data-post-id="38336" data-author="Teron" data-date="2017-07-20T14:51:53+00:00" data-subject="Re: Save state of loaded EQ to save it through crashes/reboo">

07/20

Scheduled reboot

a swirling ball of fire

a heavy iron safe

a backgammon board

a book of conflagration

about 13 scimitars, 6 swords, 1 pair of ant mandibles, a few macus.

</div>

<div class="post" data-post-id="38454" data-author="Teron" data-date="2017-10-22T06:47:16+00:00" data-subject="Re: Save state of loaded EQ to save it through crashes/reboo">

21th Oct, crash, 4-5 day uptime

Lost:

a swirling ball of fire on Lucifer

a gaudy hat on Prince Osama

about 13 choppers in my Lyme vault, about same amount in Dragonsworn vault

which is to say, how's progress on this feature development?

Thanks.

</div>

<div class="post" data-post-id="38458" data-author="Teron" data-date="2017-11-02T08:03:42+00:00" data-subject="Re: Save state of loaded EQ to save it through crashes/reboo">

20 scimitars in my vault, at least 5-10 choppers in Dragonsworn vault.

cps from the Cloud Giant fortress on the ground.

</div>

<div class="post" data-post-id="38466" data-author="*teker*" data-date="2017-11-07T19:43:03+00:00" data-subject="Re: Save state of loaded EQ to save it through crashes/reboo">

I've enabled my solution for this in the next reboot.  However, my solution is to the original "problem" which was mobs popping items and then losing them during the reboot.  It is not a "persist items on the ground or in vaults" solution.

That means that the choppers on the ground are going to go away at reboot.  It also means that mobs that normally pop choppers and are carrying one at the reboot are likely to repop with one after the reboot.

</div>

<div class="post" data-post-id="38467" data-author="Gorka" data-date="2017-11-07T19:50:56+00:00" data-subject="Re: Save state of loaded EQ to save it through crashes/reboo">

Will mobs that are down (killed) at the time of a reboot still have no chance to load when the game reboots?

If the reboot is scheduled, will we be able to dump all the choppers on a mob and have them reappear after reboot?

</div>

<div class="post" data-post-id="38468" data-author="*teker*" data-date="2017-11-08T03:19:29+00:00" data-subject="Re: Save state of loaded EQ to save it through crashes/reboo">

1) Yes.  I think it'll remain this way until the higher ups are confident that people can't intentionally crash the game to get hard mobs to repop item.  Or unless we figure out a way to track how long the game was up before the last crash/reboot and do something based on that.

2) No.

</div>

<div class="post" data-post-id="38469" data-author="Gorka" data-date="2017-11-08T06:31:34+00:00" data-subject="Re: Save state of loaded EQ to save it through crashes/reboo">

On point 1, the player still has to kill the mob in the first place to give it a chance to pop on reboot/crash anyway. I don't see the advantage of crashing the game.

</div>

<div class="post" data-post-id="38488" data-author="Gorka" data-date="2017-11-18T15:52:33+00:00" data-subject="Re: Save state of loaded EQ to save it through crashes/reboo">

Today I killed an empty chop mob 30 times, only to have to kill another empty after a reboot because my mob was down at the time of reboot. Can something be done about this? I risk my neck to solo a chop mob and run DoT solo, and to have to kill empties after a reboot because mobs were down is extremely frustrating.

</div>

<div class="post" data-post-id="38499" data-author="*teker*" data-date="2017-11-20T21:53:30+00:00" data-subject="Re: Save state of loaded EQ to save it through crashes/reboo">

Ok, so now I've got code that will log each time the mud boots to the database so I can tell how long it's been since the last boot.  Basically a way to tell if the game has been up a while or if it crashed/rebooted recently.  So now I can do one of two things:

1) Allow mobs to pop equipment normally at boot if the game has been running for a significant amount of time.  I imagine 23hrs is a decent check there.

OR

2) Continue saving the equipment at shutdown (if a normal shutdown or the game hasn't crashed too badly) and try repopping equipment from that list at reboot.

So what should it be?

</div>

<div class="post" data-post-id="38500" data-author="Gorka" data-date="2017-11-20T22:24:47+00:00" data-subject="Re: Save state of loaded EQ to save it through crashes/reboo">

Probably not the smartest idea to ask our opinion Teker, I suspect we will be equally divided. You will probably just need to choose one option yourself in the end. I think the original idea is that when the mud is reloaded, it reloads as much as possible how it was. Option 1 breaks with that idea and it encourages the mud to be crashed in the hope Cthulhu or Flame etc loads on boot and whats already loaded will be lost. Option 2 is the most true to the original idea with one flaw in the fact mobs that are dead at reboot will be empty.

Could there be an option 3?

Mobs that were dead at time of reboot, are respawned with a chance to load.

Mobs that had items at the time of reboot, are reloaded with items they already had.

I don't know how possible it is to keep a list of dead mobs in the same manner you save the eq on the mobs. Option 3 is the purest idea in that, as much as possible the mud would continue in the state it was before reboot. Another thing is that the mobs pop unaged... but seriously how can we complain given what you've done to fix the situation already. Thanks very much.

</div>

<div class="post" data-post-id="38501" data-author="*Splork*" data-date="2017-11-21T13:10:34+00:00" data-subject="Re: Save state of loaded EQ to save it through crashes/reboo">

Option #1 was tried 20 + years ago and led to the game being intentionally crashed. Giving the option for tons of high level equipment to pop, even though the majority of mobs were not cycled or dead at the time of crash/reboot, doesn't make much sense to me!

I actually agree with Gorka,  hidden option #3 would be ideal!

</div>

<div class="post" data-post-id="38682" data-author="Teron" data-date="2018-02-24T04:39:30+00:00" data-subject="Re: Save state of loaded EQ to save it through crashes/reboo">

As far as I know, a high-end pop of lion-hearted armplates was lost in a crash.

It wasn't reloaded.

Also, before the crash, there were 25 or more specs popped by very few people. The crash poofed 75% of them.

I don't see how this seems to be a satisfying solution.

Now, Gorka suggested

> **Quote:**
> Mobs that were dead at time of reboot, are respawned with a chance to load.
> 
> Mobs that had items at the time of reboot, are reloaded with items they already had.

and Splork said

> **Quote:**
> I actually agree with Gorka, hidden option #3 would be ideal!

but what actually implemented was:

Mobs that had items at the time of reboot, are respawned with a chance to load.

This also needs to be improved to be a satisfactory change, in my opinion to the original suggestion:

> **Gorka wrote:**
> Mobs that had items at the time of reboot, are reloaded with items they already had.

> **Splork wrote:**
> I actually agree with Gorka, hidden option #3 would be ideal!

</div>

<div class="post" data-post-id="38756" data-author="Teron" data-date="2018-05-04T14:46:21+00:00" data-subject="Re: Save state of loaded EQ to save it through crashes/reboo">

Vault floor:

A huge wickedly curved scimitar leans against the wall. [18]

3 ticks.

crash.

Reboot time.

</div>
