---
title: "Newbatia Changes"
topic_id: 4638
author: "*Idjit*"
date: 2016-05-19T04:26:21+00:00
last_activity: 2016-06-04T21:54:56+00:00
last_author: "*juggleblood*"
sticky: false
locked: false
post_count: 11
---

<div class="post" data-post-id="36930" data-author="*Idjit*" data-date="2016-05-19T04:26:21+00:00" data-subject="Newbatia Changes">

Our newbies will see a modest amount of changes.

-Newbatia town now has a higher mob population, triple in some cases.

-Newbatia mobs on an infrequent basis, will now drop hints about nearby areas on Valkyre.

-in each town (not just VK), the Cleric guildmasters slowly drop hints about the location of the temples on that continent.

-in each town (not just VK), the Warrior guildmasters slowly drop hints about Degrance's Army and how to join up.

The chats are set to a low percentage so it takes a fair number of minutes (if only one mob is in a room, almost 15 minutes) before a hint is dropped.

The idea was to have just enough to pique newbies' interest and not have a stream of spam.

In each town, the town quester now gives a scrolling lecture about what drachma IS and WHY we would want to spend it.  (In BH, Regis gives the lecture but Hawthorn doesn't.  I wanted to see how well this was received first, and it seemd odd to put the lecture on both of them).

</div>

<div class="post" data-post-id="36931" data-author="Teron" data-date="2016-05-19T14:57:36+00:00" data-subject="Re: Newbatia Changes">

That's a good idea, although in BH town I still get bombarded with these messages roughly every tick. 

Maybe limit them to one message about a certain area per day or to players under 3x40? I really don't need to be reminded about every area there is, unless you give me a grenade.

</div>

<div class="post" data-post-id="36932" data-author="*Idjit*" data-date="2016-05-20T02:50:47+00:00" data-subject="Re: Newbatia Changes">

Thinker procs have a level check but only if the say's or emotes are given in a rigid order.

It won't let me level restrict them AND give a random-order like I want.

</div>

<div class="post" data-post-id="36933" data-author="*Idjit*" data-date="2016-05-20T03:11:54+00:00" data-subject="Re: Newbatia Changes">

In response to these comments the quester lectures, which -are- in a rigid order, have been set to max-level 20.  I am currently pondering what i'll do for the wandering town mobs in BH.

</div>

<div class="post" data-post-id="36934" data-author="*Idjit*" data-date="2016-05-20T03:37:26+00:00" data-subject="Re: Newbatia Changes">

I have applied myself to the problem and written an every_arrival() function in MUDL that functions as follows:

If character level 19 and below enters the room, the thinker is turned on.

If character level 20 and higher enters the room, the thinker is turned off.

So, Taron, it may be just your misfortune if a newbie happens to come sailing through your room while you're standing there.

But I think that will be kind of rare?  Your initial arrival will have turned it off though, to start with...

(also, when you're actively running a group such that you'd have a last person arriving that's lower than 20, asserting that you'd have a newbie in tow in the back line which is also not that common, you tend to be the kind of leader anyway who convocates direct from area to area and doesn't stop in town to be spammed in the first place -- if you're in town -alone- preparing to run from recall to an area, your arrival --should-- shut off the thinker of something standing at West gate. I'm not entirely certain recall teleports will count as directional arrivals though within the every_arrival calling form.  Breeze would know more than I would on this subject..but you tend to run from recall to your next area within 3 seconds anyway?...).  

So, at any rate, this will be a significant improvement if not exactly perfect.

Due to the number of mobs that now drop hints (five or six? in BH now), I may miss adding the every_arrival to some of them.

Just incrementally remind me which ones and ill add it.

--D

</div>

<div class="post" data-post-id="36935" data-author="Yasik" data-date="2016-05-20T05:35:05+00:00" data-subject="Re: Newbatia Changes">

Changes are great.

After 'graduating' from Colledge, newbs dont know what to do and where to go - they told me exactly that during occasional chats.

Best place to level up on Valk for level 5 is Burbalangs (Hi, Brad!), but newbs are not aware about where it is.

Other areas are somewhat too dangerous for a while.

Now newbs can hunt exp in town, then explore away when they feel ready. Olde good days have returned.

Also, and I **MUST** outline this especially : spelling, grammar, and punctuation is fine, which is quite rare nowadays. The Comma Thief is pleased.

</div>

<div class="post" data-post-id="36938" data-author="*Idjit*" data-date="2016-05-21T02:10:20+00:00" data-subject="Re: Newbatia Changes">

(One of) the town mobs already mentions Burbalangs now, per my recent chat proc updates.

I forget which.

--D

</div>

<div class="post" data-post-id="36940" data-author="Teron" data-date="2016-05-21T06:48:19+00:00" data-subject="Re: Newbatia Changes">

Thanks for the update.

I think that mobs can mention areas depending on area level, though I'm not sure when you should stop advertising the BH Volcano, maybe tri40.

It's fine, if mobs start talking, when a newb walks into a room, where I'm standing.

</div>

<div class="post" data-post-id="36946" data-author="Firebrand420" data-date="2016-06-01T18:01:25+00:00" data-subject="Re: Newbatia Changes">

So why not have the thinker proc tied to the Is_newbie flag? Folks can turn off the messages by turning off the Is_newbie flag.

</div>

<div class="post" data-post-id="36948" data-author="*Idjit*" data-date="2016-06-04T21:20:04+00:00" data-subject="Re: Newbatia Changes">

That would require New Hardcoded Code.

The thinker procs by themselves do not.

--D

</div>

<div class="post" data-post-id="36949" data-author="*juggleblood*" data-date="2016-06-04T21:54:56+00:00" data-subject="Re: Newbatia Changes">

Cool beans.

Regarding Burbalangs: it is still a little out of reach of a very low newb. I wouldn't direct them there, as they'll get slaughtered by the burbalang that splits in 2. This fall I plan on better incorporating the fens. When newbs reach the end of the newbie university they can enter stream and arrive in the fens near Dale Tanner. Future plans include some more guided activities around there for the super newbs. If Tox wanted to adapt Burbalangs to a lower level, then we could send them there, but it's pretty solid as it is. That would be up to him if he wanted to rebalance it for lower. 

Perhaps there could be forewarning for really low newbs about to enter it or perhaps there could be an npc adventurer who takes them into the Burbalangs and aids them.

</div>
