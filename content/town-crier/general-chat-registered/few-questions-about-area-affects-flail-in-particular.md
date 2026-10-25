---
title: "Few questions about area affects, flail in particular"
topic_id: 1264
author: "Wintersdark"
date: 2005-06-19T16:55:07+00:00
last_activity: 2005-06-22T13:59:15+00:00
last_author: "Avatar"
sticky: false
locked: false
post_count: 21
---

<div class="post" data-post-id="7335" data-author="Wintersdark" data-date="2005-06-19T16:55:07+00:00" data-subject="Few questions about area affects, flail in particular">

Is it possible to have flail NOT hit your followers?   Before the alignment changes, it was merely a nuisance, but now accidentally smacking your peri is a very, very bad thing if you need to stay good.

Currently, Flail hits only engaged mobs, unless you are unengaged in which case it hits every non-player in the room.  The problem here is this includes followers - making Flail only useful for those who cannot, or do not, have followers and are grouped with the same.  It's very, very easy to have a mob die before the command is processed - either due to lag, command-lag, the mob fleeing, a couple group members firewinding at once, or whatever else.

Being a Warrior Prime skill, it kinda hurts to lose use of it.

I don't mind the danger in accidentally engaging other enemies - that's just a danger inherent in using such an attack, but it shouldn't hit friendly creatures.

Is it at all possible to fix flail to at least not hit followers?

Failing all followers, at the very least not hit your OWN followers? 

I understand this is also a problem for caster characters with area affect spells...   such as poor Shyla having her Pit Fiend get all disgruntled with her :)

</div>

<div class="post" data-post-id="7336" data-author="Weasel" data-date="2005-06-19T19:04:23+00:00" data-subject="">

nods, I've stormed my eudaemon a few times.. back when I was not perma-evil heh..

</div>

<div class="post" data-post-id="7339" data-author="Wintersdark" data-date="2005-06-20T01:08:00+00:00" data-subject="">

nods, I've stormed my eudaemon a few times.. back when I was not perma-evil heh..[/quote:1czt1o45]

*nods*  Back then, it wasn't such a big deal - I mean, accidentally kill your peri/eudaemon?  Just summon another.

Now, if you accidentally kill your peri, you're between evil and neutral and cannot supp another.   Not that that's necesarily a bad thing, but now your choice is either: Just don't use all those skills abilities, or don't use followers.

Seems a waste, really - A warrior prime gets just two things for being warrior prime, parry and flail.  There's not much advantage otherwise, really (that I'm aware of, at any rate).   Seems a shame to prevent them from using one of those simply because of a oddly coded targetting thing.

I mean, my character obviously has some control over the flail attack, as it doesn't hit other players... why can't she not hit her own followers?

</div>

<div class="post" data-post-id="7341" data-author="Yasik" data-date="2005-06-20T01:35:27+00:00" data-subject="">

You know.. i even didnt read the whole post - there is no need in it imho, what can i tell you playing Wa-prime 5+ years here : forget about Flail even exists. This is the most useless skill ingame. Just forget about it. THERE IS -NO- FLAIL SKILL!

You can do much more useful things in that rounds instead of flailing.

</div>

<div class="post" data-post-id="7345" data-author="Wintersdark" data-date="2005-06-20T03:37:34+00:00" data-subject="">

You know.. i even didnt read the whole post - there is no need in it imho, what can i tell you playing Wa-prime 5+ years here : forget about Flail even exists. This is the most useless skill ingame. Just forget about it. THERE IS -NO- FLAIL SKILL!

You can do much more useful things in that rounds instead of flailing.[/quote:3qpye94d]

See, this is why I'm posting it.   Flail doesn't need to be useless, and it shouldn't be.   Being a prime-only skill, it SHOULD be a worthwhile thing to do each round.

I mean, really, just fixing it to not hit followers would be fine....

Or, better yet, have it NOT engage unegaged mobs AT ALL - just hit engaged mobs, or unengaged mobs it is directly targeted at.   That should be pretty simple, shouldn't it?

</div>

<div class="post" data-post-id="7350" data-author="Weasel" data-date="2005-06-20T08:51:48+00:00" data-subject="">

Gotta agree, flail is bollocks. It's handy for initiating a fight with a hidden mob, but sheesh a flail can't even kill a morted fly half the time it's so ineffective and weak. Your point however Wintersdark is valid - eudaemons etc are followers, and a follower means part of a group, therefore they should not be getting hit. I can't help thinking this is just a little oversight by coders, but then again, why have they still not fixed it? ..Yasik 5+ years? err.. nah.

</div>

<div class="post" data-post-id="7365" data-author="guest" data-date="2005-06-20T13:26:07+00:00" data-subject="">

Hi all ...

It has been in my list since i started coding : redesign how area spells choose targets.  Guess that, as a collateral effect, it will change flail too.  Problem is that i have been quite busy with other things and bug fixes, and never started it.  I will eventually get into it, just not sure when.

</div>

<div class="post" data-post-id="7370" data-author="kjartan" data-date="2005-06-20T14:11:24+00:00" data-subject="">

Ok, the powers that be have discussed it and conclude that you are right about flail; we'll fix it so it doesn't hit mobs that are on the "player side".  I can probably take care of this tonight.  I will leave the other area spell issues to Isabo.

</div>

<div class="post" data-post-id="7373" data-author="firebrand" data-date="2005-06-20T14:14:31+00:00" data-subject="">

hmmm never have been sure whether or not this actually works, but is flail currently targettable - i.e. flail target when there is a group of mobs you are fighting or there are several mobs in the room and you only want to flail one of them.  if not, can it be made targettable?

</div>

<div class="post" data-post-id="7383" data-author="Wintersdark" data-date="2005-06-20T20:18:29+00:00" data-subject="">

It is currently targettable, but targetting it just sets the "primary" target - the one that receives full damage as compared to the lesser damage other mobs take.

If unengaged, it hits everything - just that the targetted mob takes full damage.

I wish it would just hit the targetted mob in that case :)

Kj: Thanks, much appreciated :)

</div>

<div class="post" data-post-id="7390" data-author="kjartan" data-date="2005-06-21T00:37:22+00:00" data-subject="">

In next crash or reboot, flail will hit only mobs that aren't following players (including you).  There is still no single-target flail, that's not what flail is for.

</div>

<div class="post" data-post-id="7392" data-author="Shyla" data-date="2005-06-21T03:22:49+00:00" data-subject="">

hmm kjartan while you are working on that is there a reason that area affect spells hit your supplicants?

Shyla

</div>

<div class="post" data-post-id="7393" data-author="kjartan" data-date="2005-06-21T03:35:51+00:00" data-subject="">

The change I made with flail should also fix avalanche, twister, and sunbeam, which use the same method of determining targets.  The other area spells I believe Isabo is going to work on so I shall leave them alone.

</div>

<div class="post" data-post-id="7397" data-author="Avatar" data-date="2005-06-21T10:05:22+00:00" data-subject="">

kjartan:

[quote:2f5sz72d]There is still no single-target flail, that's not what flail is for.[/quote:2f5sz72d]

I can't connect, can someone post the Help file for flail?  I was under the impression that it worked exactly as Wintersdark explained below.

I may have to play with flail again now that the targetting issue is fixed, thanks  :)

</div>

<div class="post" data-post-id="7398" data-author="12345" data-date="2005-06-21T10:08:01+00:00" data-subject="">

This is what's posted on the helps on the web site...

FLAIL

 

Usage: flail [<target>]

Level: 31 warrior prime

Flail is an area attack using the warrior's weapon. The warrior flails

his weapon about and attacks an entire group of enemies, with less

efficiency than if he focused his attacks on just one enemy. If a target

is given, flail does the warrior's full weapon damage to that target, and

half damage to all other enemies in the room. Note that a skill check is

made for each enemy, so the target MAY not be hit while other enemies MAY

be.[/quote:3dhf47n3]

</div>

<div class="post" data-post-id="7439" data-author="Avatar" data-date="2005-06-22T10:26:21+00:00" data-subject="Flailing about">

Now that I read the thread again, I think Kjartan was replying to Firebrand, not Wintersdark.  Looks like it was my misunderstanding this time.

</div>

<div class="post" data-post-id="7446" data-author="Leaf" data-date="2005-06-22T11:48:40+00:00" data-subject="">

Sooo more or less, if a Warrior has a 4d4 +2 +2 weapon and he flails at

a group of Sashs (lets say 4 and 1 is a leader).  He hits all 4 with a total

damage of 18/4 = 4.5 dam?  However if he goes "Flail Leader" the leader

takes a full +18damage???  Seems kinda weak ... Considering the skill

"Kick" does around +20 from what I've been told.

</div>

<div class="post" data-post-id="7447" data-author="12345" data-date="2005-06-22T12:09:14+00:00" data-subject="">

That's like saying double attack is kinda weak.  If you're normal attack is a massacre, you're doing a massacre to the targetted mob and half a massacre to every other mob in the room.  Bonus if you have +flaildam eq.

If you're comparing it to flurry.... well, flurry is safer and allows the use of other commands and is non-prime, but isn't area attack and can't use +flaildam bonuses.  Flail gets stronger with more enemies in the room, but at the same time, you're engaged with more mobs.

I don't know what I think of that.  Strider likes flail, maybe he has a comment.

</div>

<div class="post" data-post-id="7448" data-author="Leaf" data-date="2005-06-22T12:46:17+00:00" data-subject="">

Just trying to find out the damage done by Flail.  Cause at the moment it

doesn't seem much.  However ur right, as in it does add additional damage

compared to not having a extra attack.  I didn't know it gets stronger when

there are more mobs in the room.  I thought the more mobs, the less dam

it will do (which in case will be usless).  

But being a Prime skill, and "kick" does 1/2 of warrior lvl.  +20dam off kick

would still be better then "Flail".

</div>

<div class="post" data-post-id="7458" data-author="Zalasta" data-date="2005-06-22T13:56:17+00:00" data-subject="">

From what I understand, flail does a certain amount of damage to every mob it hits.  That damage is based on how much your normal attack does, but is somewhat less.  It does not, however, divide out among your enemies, it just hits them all.

So lets say you generally massacre for 25 damage on a normal attack.  Flail might do 20 damage to everyone you're fighting.  Or, you could 'flail Mrak' and hit him for 25 and all his birds for 15.  I am of course making those numbers up but qualitatively it should be good.

</div>

<div class="post" data-post-id="7460" data-author="Avatar" data-date="2005-06-22T13:59:15+00:00" data-subject="Flail">

I think you guys are confusing each other.  

An untargetted Flail doesn't actually get stronger with more enemies, it does the same damage to each enemy but total damage goes up just because you've hit more targets.  Similar to Firewind, it does the same damage to each target whether you hit 1 target or 3, but the total damage goes up and it's more "useful" the more mobs you have in the room.

</div>
