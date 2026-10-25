---
title: "Targeting the Right Thug"
topic_id: 1147
author: "SirRobin"
date: 2005-05-28T06:18:47+00:00
last_activity: 2005-07-21T07:21:07+00:00
last_author: "Wintersdark"
sticky: false
locked: false
post_count: 17
---

<div class="post" data-post-id="6622" data-author="SirRobin" data-date="2005-05-28T06:18:47+00:00">

I think the IDs for the new mobs in Newbatia may need some adjustment. The three I’m speaking of are:

1) an evil thug

2) a young gang member

3) a gang leader

These, of course, are their ‘scanned’ names.

To target #1 I tried ‘thug’, but that apparently applies to all three. Result, I get my behind kicked. Ok, so they are all thugs, I’ll just use ‘evil’. This works on #1 and does not trigger #2. Great I think, until a #3 is in the same cell; oops, ‘evil’ works on him too. Another kicking of my backside.

Thug #1 seems to be the easiest of the three, so I’d like to be able to target him alone if possible.

</div>

<div class="post" data-post-id="6624" data-author="guest" data-date="2005-05-28T07:10:27+00:00">

Hi, Sir ...

Next time you visit one of those evil thug (#1, the one you want) type names thug.  It will show you all keywords the mob has.  So, from there, you can use target evil-thug-whatever-whatever.

</div>

<div class="post" data-post-id="6643" data-author="SirRobin" data-date="2005-05-28T23:55:32+00:00">

Thanks, Isabo, I had forgotten about the Names command.

</div>

<div class="post" data-post-id="6644" data-author="SirRobin" data-date="2005-05-29T00:11:22+00:00">

Ok, I used the Names command to see what each thug would respond too:

Evil thug: thug gang member evil

Young gang member: thug gang young member 

Gang leader: leader thug gang evil

As you can see, there is no one word that references the Evil Thug that does not also reference another one of the thugs. How about adding the name ‘bully’ to the list of names for the Evil Thug?

</div>

<div class="post" data-post-id="6646" data-author="Akasha2" data-date="2005-05-29T01:31:07+00:00">

Ok, I used the Names command to see what each thug would respond too:

Evil thug: thug gang member evil

Young gang member: thug gang young member 

Gang leader: leader thug gang evil

As you can see, there is no one word that references the Evil Thug that does not also reference another one of the thugs. How about adding the name â€˜bullyâ€™ to the list of names for the Evil Thug?[/quote:16r1ipim]

Evil thug:  member-evil-gang

Young gang member: member-thug-gang

Gang leader: leader-thug

</div>

<div class="post" data-post-id="6655" data-author="SirRobin" data-date="2005-05-30T03:32:26+00:00">

Thanks, Evil-member seems to work great!

</div>

<div class="post" data-post-id="6673" data-author="blackmore" data-date="2005-05-30T12:03:06+00:00">

I'm a bit confused as to why you would need to worry about this, but I think I can guess.  You are spamming a spell or skill that requires a target, causing you to hit a 2nd mob after the first has died.

You can stop spamming commands, but there's a more reliable way.  All attack skills and songs only require a target if you are not in combat.  If you are already in combat, you can cast/do your skill without specifying a target, and it will hit the one that you are currently fighting.

</div>

<div class="post" data-post-id="6674" data-author="Aleksey" data-date="2005-05-30T12:15:44+00:00">

Target 3.thug and can spam as much as you want. Whan he down do 2.thug

 Hammering,pushing also helps, some times evil imms creating assister mobs And its nice that thay have key word ,no need remember thair long names.

</div>

<div class="post" data-post-id="6690" data-author="SirRobin" data-date="2005-05-31T03:41:25+00:00">

You were half right, Blackmore, I wasn’t spamming commands, but I had created a variable that all my macro keys referenced so that every attack was targeted.

I didn’t know that once you engaged a mob it stayed targeted internally. Just tried it, and it’s a great advantage. Just one problem: if a mob is mortally wounded then “Strike” alone will not hit him. You get the message “You don’t see that person.” Don’t know if the same thing happens if he is just stunned. Not a big problem, I can probably get around this glitch by setting up another macro key for “Strike $Target” to finish off a mob when this happens.

</div>

<div class="post" data-post-id="6691" data-author="guest" data-date="2005-05-31T05:14:09+00:00">

Hi, Sir.

Turn autokill on. It'll help to kill mortally wounded mobs w/o retargeting.

</div>

<div class="post" data-post-id="6845" data-author="SirRobin" data-date="2005-06-06T13:55:09+00:00">

Regarding the need to target mobs for the final blow, here is an example below (with autokill on):

# <153hp 194ma 119mv>

# 

# You hit an evil thug.

# A ghost pounds an evil thug hard.

# A ghost bites an evil thug hard.

# An evil thug misses you with his hit.

# An evil thug misses a ghost with his crush.

# A ghost pounds an evil thug hard.

# A ghost bites an evil thug hard.

# An evil thug is incapacitated and will slowly die, if not aided.

# A calico kitten leaves south.

# You are hungry.

# An evil thug lies immobile on the ground, suffering...

# An evil thug is mortally wounded, and will die soon, if not aided.

# 

# <154hp 195ma 119mv>

# 

# Strike

# You don't see that person.

# 

# <154hp 195ma 119mv>

# 

# Strike evil-member

# An evil thug looks shocked as he sees your fist embedded in his abdomen, then collapses.

# An evil thug is dead! R.I.P.

This was happening to attacks like Strike and Kick, and to spells. I’m no longer sure how frequently this occurs because I’ve gotten into the habit of using a targeted attack for the final blow when the mob is down. I seem to recall it happening mostly when the mob was mortally wounded instead of stunned or incapacitated, but maybe that was because the mobs sometimes bleed to death if you don’t finish them soon enough, so maybe it’s the same for all three modes. 

If it’s a bug it must not be a big deal for anyone, since it looks like I’m the only one to mention it. Just thought I’d post a final note on the subject for any newbies that might read this thread.

</div>

<div class="post" data-post-id="6846" data-author="12345" data-date="2005-06-06T14:10:05+00:00">

It would seem to be a bug with autokill.  I can tell you from past experience that blindly striking a mob can be dangerous if you're in a place like Blaster's temple where mobs with the same name wander in and out during battle.  For safety, I will normally look at the mob prior to finishing it off to make sure I'm targeting the correct one.  If it's in excellent condition.. it's not the right one.

</div>

<div class="post" data-post-id="6849" data-author="Avatar" data-date="2005-06-06T15:14:36+00:00">

The difference is the necro pet, if the ghost morts the mob I don't think the autokill on your char is happening.

</div>

<div class="post" data-post-id="6851" data-author="SirRobin" data-date="2005-06-06T16:41:31+00:00">

The pet? Interesting possibility. I was going to say that the same thing is happening with my Druid, but I don’t recall if I noticed it before I started using Treants or not. With my Necro I thought I noticed that sometimes, if one of his pets mortally wounded the mob, that the fight would basically stop, but I’d need to go through my logs more thoroughly to find those examples. By basically stop I mean something like this:

Typical pattern:

----------------

Necro hits

Ghost hits

Ghost hits

Skeleton hits

Skeleton hits

Mob hits

Mob hits

Necro hits

Interrupted pattern:

--------------------

Necro hits

Ghost hits and mob mortally wounded

No action from Ghost

No action from Skeleton

No action from Skeleton

No action from Necro

Mob bleeds to death

Again my solution was to do a targeted attack after the mob is wounded.

</div>

<div class="post" data-post-id="6852" data-author="Weasel" data-date="2005-06-06T17:27:27+00:00">

thuck'n fugs  :evil:

</div>

<div class="post" data-post-id="7955" data-author="Taki" data-date="2005-07-20T07:27:22+00:00">

I am supporting the 'pet-theory' since i noticed the same, and even worse annoyances related to pets/followers (cleric's supplicants and necro's undeads, not sure about mage's familiars).

If a pet/follower is the one who strikes the morting hit, then the fight stops - as if everyone else had autokill off. Thus the need to issue a new targeted command to finish the kill. This is even worse if it happens in a group since then the xp is not shared correctly - need to experiment more to see which are the cases.

</div>

<div class="post" data-post-id="7960" data-author="Wintersdark" data-date="2005-07-21T07:21:07+00:00">

It's the pet thing.   If a pet morts a mob, then the fight stops.  I've lost a good number of kills to bloodloss that way, on both of my chars.

It happens, reliably, with animated, summons, supplications, familairs, charmies, everything.

However, if a follower leaves a mob unconcious but NOT mortally wounded, the fight will continue as normal.

It's really rather annoying - the time it takes to look at the target, find the correct one if new mobs have come into the room ect., often leads to death VIA bloodloss - always a piss off when you've worked really hard to kill something big.  

I am supporting the 'pet-theory' since i noticed the same, and even worse annoyances related to pets/followers (cleric's supplicants and necro's undeads, not sure about mage's familiars).

If a pet/follower is the one who strikes the morting hit, then the fight stops - as if everyone else had autokill off. Thus the need to issue a new targeted command to finish the kill. This is even worse if it happens in a group since then the xp is not shared correctly - need to experiment more to see which are the cases.[/quote:3h1tr0gn]

</div>
