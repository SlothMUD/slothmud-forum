---
title: "still at it :)"
topic_id: 1151
author: "Ditheca"
date: 2005-05-28T19:09:47+00:00
last_activity: 2005-06-08T10:18:58+00:00
last_author: "12345"
sticky: false
locked: false
post_count: 12
---

<div class="post" data-post-id="6638" data-author="Ditheca" data-date="2005-05-28T19:09:47+00:00" data-subject="still at it :)">

You quickly duck aside and use a tigress nymph follower's strength against her in a brutal counterattack!

[b:1tbaq3lf]A tigress nymph follower is mortally wounded, and will die soon, if not aided.[/b:1tbaq3lf]

A tigress nymph follower misses a vilewight with her claw.

A tigress nymph follower misses a vilewight with her claw.

[b:1tbaq3lf]A tigress nymph follower viciously massacres a vilewight with her claw.[/b:1tbaq3lf]

You sigh.

<638hp 92ma 171mv> [ASF A]> 

A vilewight viciously massacres a tigress nymph follower with its claw.

A tigress nymph follower is dead! R.I.P.

You received 1008094 experience points.

Your blood freezes as you hear a tigress nymph follower's death cry.

You cease your counterattack stance.

</div>

<div class="post" data-post-id="6647" data-author="kjartan" data-date="2005-05-29T02:29:58+00:00" data-subject="">

Kjartan sighs.

</div>

<div class="post" data-post-id="6867" data-author="Ditheca" data-date="2005-06-07T09:10:40+00:00" data-subject="*bump* ow!">

You quickly duck aside and use a tigress nymph follower's strength against her in a brutal counterattack! 

A tigress nymph follower is mortally wounded, and will die soon, if not aided. 

A tigress nymph follower misses a you with her claw. 

A tigress nymph follower misses a you with her claw. 

A tigress nymph follower viciously massacres you with her claw.

Funny thing this time is that I had no followers.  It was straight up mage style, and she gave me the beat down after morted.  Bone armor and counterattack are both still having problems.

Thanks for the continued effort here!

Your loyal voting subject,

-- Theca :)

</div>

<div class="post" data-post-id="6873" data-author="13" data-date="2005-06-07T14:56:13+00:00" data-subject="">

Common occurance with monks.  Sucks.  Plz fix.

</div>

<div class="post" data-post-id="6882" data-author="Weasel" data-date="2005-06-07T20:33:29+00:00" data-subject="">

Do you have an old tick counter Ditheca? Just wondering if a tick fell between morting and kill attempt.. mobs regen on old ticks still.. altho I think this still happens occasionally anyway, whether you're a monk or any other class.

</div>

<div class="post" data-post-id="6883" data-author="kjartan" data-date="2005-06-07T20:58:20+00:00" data-subject="">

Maybe we need a wakeup message for when mobs regen from down to up.  That seems like it would clear up what was actually going on here.  Also, it's the sort of thing your character would probably notice, that the dragon just got back up and here he comes.

I'll put in something like that, and also see if I can figure out why my earlier fix isn't stopping these attacks.

</div>

<div class="post" data-post-id="6884" data-author="Avatar" data-date="2005-06-07T21:23:47+00:00" data-subject="Attacks">

I doubt it's tick-regen related.  His latest example seems to be within 1 round of an attack.

charles

</div>

<div class="post" data-post-id="6885" data-author="**Jake**" data-date="2005-06-07T22:11:26+00:00" data-subject="heh">

They "wake up" when stunned, not mortally wounded. :)

--

Jake

</div>

<div class="post" data-post-id="6897" data-author="kjartan" data-date="2005-06-08T02:57:19+00:00" data-subject="">

Ah.  My last attempt to fix this was botched.  Should be fixed after the next crash or reboot.  (the specific problem I fixed was, if a mob got taken out in the middle of his attack sequence he went ahead and finished the sequence.)

</div>

<div class="post" data-post-id="6898" data-author="Vixn" data-date="2005-06-08T03:35:05+00:00" data-subject="Re: heh">

They "wake up" when stunned, not mortally wounded. :)

--

Jake[/quote:2nnmaepe]

First, in my opinion it should be usual the mortally wounded person still has abillity to fight. It wasn't stunned, it just get lots of wound and one or more of this wounds SOON (but not yet) will bring this person to dead (mortally wounds). And stunned person couldn't attack till It'll return to normal (unstunned) state.

And second It could be a fine part of battle. ie phoenix must have abillity to uprise from ash and be ready to fight again (in compliance with legends). And followers of 'the dark lord' could wake up after 'mortally wounds' and return to fight as undeads.

But now It's just a bug and must be fixed. Thanks KJ. 

Vixn

___________

wake up, dead man, it's time to wake up (c) mad season.

</div>

<div class="post" data-post-id="6899" data-author="kjartan" data-date="2005-06-08T03:41:18+00:00" data-subject="">

Those are fine ideas, but the way to do them is not to leave in some bug that lets anybody who is stunned, mortally wounded, or whatever, finish their attack sequence.

I am all for phoenixes, undead that don't die, wild boars that keep fighting til -10 hp, or whatever.  We already have code in place to make it possible to do all that without any intervention from me - any imm who can make mobs can do it.

</div>

<div class="post" data-post-id="6907" data-author="12345" data-date="2005-06-08T10:18:58+00:00" data-subject="">

Careful what you wish for, we've already had code that brought undeads back to life if you didn't perform 'last rites'.  I can't count the number of times a newbie killed the mummy king and had it follow them back to town after they had recalled.  Watching mobs marauding around town is always interesting.

</div>
