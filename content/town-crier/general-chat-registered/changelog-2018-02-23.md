---
title: "Changelog 2018-02-23"
topic_id: 4836
author: "*teker*"
date: 2018-02-23T23:57:07+00:00
last_activity: 2018-03-13T15:22:52+00:00
last_author: "Teron"
sticky: false
locked: false
post_count: 9
---

<div class="post" data-post-id="38680" data-author="*teker*" data-date="2018-02-23T23:57:07+00:00" data-subject="Changelog 2018-02-23">

New things since my last post:

- Strike shows with gag_fight on.  I've had a couple bugs filed on this but it was requested by a large number of players so it's going to stay in.

- Subdued mobs now have a secondary weight cap that makes them easier to carry.

- Watcher tells should be viewable in replay.

- Mob auctions shouldn't show up with auction turned off

- EU magic rope rooms now on EU (should not poof choppers on EU chop day)

I've left in the code changes to temp item poofing since the weekend chop day seemed to go ok.  Builders can set flags to poof those items in particular rooms (like DoT/ET/etc) and those flags take precedent over the world bonuses.  I have a list of remaining rooms with that flag but it seems like things went well now that the recall spots had their flags cleared.

</div>

<div class="post" data-post-id="38681" data-author="Teron" data-date="2018-02-24T04:28:56+00:00" data-subject="Re: Changelog 2018-02-23">

Can you tell me the use cases, where it's necessary, for those, who *gag fight*, to see strikes?

Why only strikes, why not circlestabs and kicks?

</div>

<div class="post" data-post-id="38683" data-author="*teker*" data-date="2018-02-26T17:55:54+00:00" data-subject="Re: Changelog 2018-02-23">

Or conversely - bash, stomp, flail, etc.  I don't know what the right balance is - I had monks (and atleast one non-monk) filing bugs that they were being accused of botting/not participating.

</div>

<div class="post" data-post-id="38685" data-author="Teron" data-date="2018-02-27T12:29:07+00:00" data-subject="Re: Changelog 2018-02-23">

If, when leading, I want to check if someone is botting, I turn gag fight off for a few rounds or mobs.

It lets me see the strikes and other stuff.

I don't like this option to be a permanent change.

If you want me to gag it with my client, then you are adding a level of complexity for all players, who don't need this feature.

If you want to introduce such a feature without friction, I suggest:

- create an option to gag attacks and to gag melee attacks.

- introduce them according to the gag fight settings of the player

This way, they can enable them selectively and it won't change the visible interface for most of the players.

P.S. A discussion and introduction of the feature would've cleared up most of the ideas. Ie, for me not seeing strikes isn't a problem, and I was once a leader in a group, where a monk was accused of botting.

</div>

<div class="post" data-post-id="38687" data-author="Gorka" data-date="2018-03-04T14:35:33+00:00" data-subject="Re: Changelog 2018-02-23">

One Ass Italiano for the imm that makes gag melee and gag attacks separate commands. I like to see what groupies are up to, defaultly we know that's normally nothing, but as they say... hope is the last to die.

</div>

<div class="post" data-post-id="38690" data-author="Teron" data-date="2018-03-06T13:38:56+00:00" data-subject="Re: Changelog 2018-02-23">

ok, so now I know 2 players/leaders, who needed this feature.

That doesn't seem like "it was requested by a large number of players", though, because I tried finding one, and found one. Now there's two.

The only explanation I heard is that "strike is close to disint on damage".

Ok, add circlestab then.

Then add a command to gag skill attacks.

</div>

<div class="post" data-post-id="38692" data-author="*teker*" data-date="2018-03-06T18:14:04+00:00" data-subject="Re: Changelog 2018-02-23">

I guess the easiest option would be to go back.  What's the best option?  Rename gag fight to gag melee and add gag skill/spell/song?  It seems like bash messages would be useful to see since that's a sort of cumulative skill.  Or maybe not.  Do any other skills/spells work in a similar way?

</div>

<div class="post" data-post-id="38703" data-author="Josiah" data-date="2018-03-12T21:52:33+00:00" data-subject="Re: Changelog 2018-02-23">

> ***teker* wrote:**
> It seems like bash messages would be useful to see since that's a sort of cumulative skill.  Or maybe not.  Do any other skills/spells work in a similar way?

The closest thing I can think of is disintegrate/destruction.  These spells have a chance to lower a mobs constitution, and then start doing serious bonus damage when it hits zero.

I have always thought it curious that gag fight blocks physical attacks but not spell attacks.  In huge groups, the firewind/disintegrate spam can get pretty intense!

I haven't led in a while, so no comment on the micromanaging leaders.

</div>

<div class="post" data-post-id="38706" data-author="Teron" data-date="2018-03-13T15:22:52+00:00" data-subject="Re: Changelog 2018-02-23">

Bash is already shown, but I probably don't need to see, when people fail bashing. Otherwise, it may be helpful - sometimes.

A successful message of stomp is shown.

Stun is shown (Suna isn't).

Kick isn't.

Trip is shown.

Broadside is shown.

Flail is shown.

Why this isn't spammy? because people don't use the above skills with the exception of bash.

We use bash on a number of mobs, and it's critical to bash it. It helps not to bash, when you are the only one bashing, or to start bashing, if 1-2 players are.

Stomping happens even rarer, because it must be the result of collaborative bashing.

Utters from blasts are shown, which, indeed, can be spammy in large groups, especially on epics.

Irrc masterful casts are shown, ie from a thunder clap.

Successful save on a corrosive surge against mob is shown (ie, when it works).

Double disints are shown - this is actually helpful.

Personally, I'd prefer a "gag skills" command that'd gag all the above. After years of killing the same mobs, it's just white noise to me. If you can make a command to:

gag bash

gag allskills

then it might even be better, but probably need more work.

Nice to see you, Josiah!

</div>
