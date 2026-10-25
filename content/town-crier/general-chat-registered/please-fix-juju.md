---
title: "Please fix Juju"
topic_id: 4050
author: "Dragoth"
date: 2013-02-28T09:11:13+00:00
last_activity: 2013-03-05T00:48:02+00:00
last_author: "*Splork*"
sticky: false
locked: false
post_count: 11
---

<div class="post" data-post-id="34100" data-author="Dragoth" data-date="2013-02-28T09:11:13+00:00">

summon juju is playing up sometimes, been happening for awhile, not sure why..

<873hp 864ma 284mv>summon juju

You gaze deeply into the obsidian charm, attempting to draw out the juju's essence from within.

As the glow within the charm begins to fade the floor splits and two large arms appear from the crack.

<873hp 792ma 285mv>summon juju

A vicious Ju-Ju Zombie crumbles to dust!

You gaze deeply into the obsidian charm, attempting to draw out the juju's essence from within.

As the glow within the charm begins to fade the floor splits and two large arms appear from the crack.

<873hp 737ma 296mv>A vicious Ju-Ju Zombie crumbles to dust!

<873hp 751ma 303mv>save

summon juju

Saving Anrok.

Saving items.

<873hp 764ma 310mv><[-87]md>

You gaze deeply into the obsidian charm, attempting to draw out the juju's essence from within.

As the glow within the charm begins to fade the floor splits and two large arms appear from the crack.

A vicious Ju-Ju Zombie starts following you.

</div>

<div class="post" data-post-id="34106" data-author="*juggleblood*" data-date="2013-02-28T12:39:15+00:00">

I looked into it.

Issue is that part of the proc is on the charm, and part is on the mob. They don't jive perfectly, so sometimes the mob believes it is masterless and crumbles to dust. It should be a random thing depending on the exact timing of the casting.

It's an old / complicated proc. I will have to tear it apart when I have some time.

</div>

<div class="post" data-post-id="34110" data-author="Magi" data-date="2013-02-28T22:00:11+00:00">

The Juju should only melt when you are Dark cloaked or Urban Stealth'd.

I bet it will never happen while you're using wall of flesh or flesh golem.

An easy fix might be to make pets immune to the stealth affect of dark cloak, which would also allow them to assist dark cloaked players.

</div>

<div class="post" data-post-id="34111" data-author="*juggleblood*" data-date="2013-02-28T23:42:02+00:00">

Huh?

You are saying you know this is how it is? Or you r speculating?

Because that would truly baffle me if it were true. The code doesn't care if the Juju can see it's master or not. Am I not understanding?

</div>

<div class="post" data-post-id="34113" data-author="Magi" data-date="2013-03-01T14:18:19+00:00">

I can only speak from experience playing a necro. I've not looked at the juju zombie code.

I believe dark cloak to be the cause of the problem.  It would be pretty easy to prove me wrong, if I am :)

</div>

<div class="post" data-post-id="34114" data-author="*juggleblood*" data-date="2013-03-02T00:53:12+00:00">

I take your word for it. I'm just surprised.

I had my newbie on last night and it godrained. I went to rent and Shelda was giving me the don't see you message because of the dark cloak. It was an interesting coincidence that u had just mentioned the issue. I went outside the inn and killed a mob and stepped back in and I was fine.

Now I just tried testing Juju with dark cloak and renting with dark cloak. Neither was any problem. If I could replicate it, I'd have something better to bug a coder about. R u able to replicate it?

</div>

<div class="post" data-post-id="34119" data-author="Magi" data-date="2013-03-04T03:16:36+00:00">

Dark cloak stealth effect is a % chance the mob won't see you correctly.  Stand at an innkeeper and type 'offer' twenty times.  5 or 10% of the time (never tested the exact number) he'll give you the 'I can't see you' message.

If dark cloak is the cause of the juju problem, it would be failing the same 5-10% of the time.  It should be easy to replicate as long as you repeat the summoning it enough times.

</div>

<div class="post" data-post-id="34120" data-author="*juggleblood*" data-date="2013-03-04T06:09:17+00:00">

Thanks for that. Using the offer command helped me figure it out. Strangely enough, the key to the fix is detect magic. I noticed Shayne the innkeeper never does the can't see you because you are dark cloaked thing. The only diff between him and Shelda was detect magic and voila, that was the issue.

So I'm applying detect magic to the Juju's and I think that should resolve it.

I'm also applying it to the innkeepers (that I remember).

</div>

<div class="post" data-post-id="34122" data-author="Magi" data-date="2013-03-04T14:13:56+00:00">

That's amazing! Nice work.

I may start carrying potions of detect magic for my pets so they can assist me properly :)

</div>

<div class="post" data-post-id="34123" data-author="*juggleblood*" data-date="2013-03-04T22:21:20+00:00">

Gimme a list of your most oft used pets and I'll make sure they have it innately.

</div>

<div class="post" data-post-id="34124" data-author="*Splork*" data-date="2013-03-05T00:48:02+00:00">

All animates and summons will be born with detect magic now.

In on reboot,

Splork

</div>
