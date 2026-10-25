---
title: "What's up with prediction?"
topic_id: 2611
author: "blackmore"
date: 2007-10-11T15:44:00+00:00
last_activity: 2007-10-13T12:23:24+00:00
last_author: "Messiaen"
sticky: false
locked: false
post_count: 22
---

<div class="post" data-post-id="20752" data-author="blackmore" data-date="2007-10-11T15:44:00+00:00">

I've been attacked several times while using prediction in the last couple of days, and I've never seen that before.  Was it changed?  It's sort of useful information to know if so...if not, it's broke or something.

</div>

<div class="post" data-post-id="20755" data-author="Malison" data-date="2007-10-11T17:35:12+00:00">

As far as I know, there were always some mobs that ignored prediction and presage.  Hopefully it's not a bug/nerf

</div>

<div class="post" data-post-id="20757" data-author="Weasel" data-date="2007-10-11T17:47:11+00:00">

maybe it now has a % fail rate, just like most other class skills / spells have?

</div>

<div class="post" data-post-id="20760" data-author="kjartan" data-date="2007-10-11T18:11:18+00:00">

Prediction and presage were changed; the changes are explained in the help for the skills.

Now every time you use prediction on a mob, he has a small chance of becoming permanently immune to your prediction.  He is still vulnerable to other people's prediction, and if he's killed and repops then he resets.

</div>

<div class="post" data-post-id="20762" data-author="alias" data-date="2007-10-11T18:25:14+00:00">

The only problem is the "small chance", like a "small chance" to save vs spell, when it checks all the time it will almost always fail. so basically you just took out prediction/presage for "some mobs" (that always make saves). Guess I picked a good time to play an alt for a while.

alias

</div>

<div class="post" data-post-id="20763" data-author="Weasel" data-date="2007-10-11T18:28:03+00:00">

but only for some mobs.. same applies for many classes - you have to find out which mobs you can hit and which you can't, rather than just being able to kill everything without ever getting hit.. where's the challenge in that?

</div>

<div class="post" data-post-id="20766" data-author="alias" data-date="2007-10-11T19:38:05+00:00">

U misunderstand like always Weasel, "some mobs" will probably be everything except kobolds ... good thing thats my main solo area now.

</div>

<div class="post" data-post-id="20767" data-author="Weasel" data-date="2007-10-11T19:51:25+00:00">

Exactly how did I misunderstand? As usual? Explain please. Have you tested every mob in sloth since the changes were made?

I understand you're pissed about the change, but try not to assume it's all-encompassing - been there myself more than once and just ended up getting told to STFU and stop whining.

Presumably the skill was never intended to work the way it was working.. ie: solo any mob in the game.. I'd count myself lucky it remained unfixed for so long..

</div>

<div class="post" data-post-id="20769" data-author="blackmore" data-date="2007-10-11T20:22:02+00:00">

I understand the change, but without knowing what mobs people were soloing and how much of a difference the change makes, I don't know what it really means.  I do know that it means I can no longer safely use prediction to push palace guards away from the sultan when I'm running them, because I got hit by the sultan when I never have before.  If I have to be prepared to recall quickly because it might not work, that's fine as long as I understand why it didn't work.  I have a bigger issue that I had no reason to believe the sultan was going to suddenly attack me because I wasn't aware a change was made.

</div>

<div class="post" data-post-id="20771" data-author="Tap" data-date="2007-10-11T21:43:24+00:00">

Maybe bragging about how much exp you could solo by exploiting a "feature" backfired. Perhaps next time, keep ya yappers shut.

</div>

<div class="post" data-post-id="20773" data-author="kjartan" data-date="2007-10-11T23:59:06+00:00">

I could make it let you have the first few predictions safely; would that address the problem?  Or do you find that you need to use prediction very many times on the same mob?  That last is what we are trying to prevent.  Right now, it will never fail on the first time, so if you use it once per mob you should be safe.

Edit: ok, talked to Annie, I understand what you are doing now.  We'll change it so you can still do the sort of thing you're doing.

</div>

<div class="post" data-post-id="20776" data-author="alias" data-date="2007-10-12T01:58:59+00:00">

That would be nice. I use it mostly for running in to get corpses and deads.

U really shouldnt need to predict more than twice per mob imo.

Thanx for re-looking at this.

alias

</div>

<div class="post" data-post-id="20779" data-author="kjartan" data-date="2007-10-12T02:12:33+00:00">

The further change is that uninjured or almost uninjured mobs won't ever bother figuring out how to defeat your prediction or presage.  This should hopefully reduce the nerfage to just the aspect of it that we wanted to nerf.

This is implemented and should go in sometime soonish; maybe not tomorrow, though.

EDIT: changes are incor.

</div>

<div class="post" data-post-id="20781" data-author="Medios" data-date="2007-10-12T02:16:37+00:00">

Personally I think a good number to start with is 5.  If your using prediction more than 5 times on a mob that hates you, then your probably ready for some hits.

</div>

<div class="post" data-post-id="20783" data-author="blackmore" data-date="2007-10-12T02:18:57+00:00">

Thanks, I appreciate that.  If I understand what you're trying to avoid, you could have it check to see if the mob hates you and key the check off of that as well.  I can understand the desire to clean that up.

</div>

<div class="post" data-post-id="20801" data-author="Avatar" data-date="2007-10-12T13:55:38+00:00">

I certain agree with basing the prediction on the mobs health.  If you're running for example guards at Sultan but not cycling Sultan, the # of predictions that have succeeded shouldn't matter.  If you hit the guards 5 times, then the Sultan ignores your skill and smacks you on #6, that's certainly not cool.

If you're using prediction to cycle the Sultan though, after he gets wounded he should be trying harder to kill you.  If he's injured, he should ignore prediction entirely.

Just my thoughts.

</div>

<div class="post" data-post-id="20821" data-author="kjartan" data-date="2007-10-12T20:21:16+00:00">

Avatar: that's basically where it ended up - except you can still use it for a while against an injured mob, but eventually it will stop working.

</div>

<div class="post" data-post-id="20822" data-author="Leaf" data-date="2007-10-12T20:50:14+00:00">

Lalala sooo who was that Mage that could solo all the big mobs again  :P

</div>

<div class="post" data-post-id="20824" data-author="Medios" data-date="2007-10-12T21:53:20+00:00">

I believe the real one was Evergreen.

</div>

<div class="post" data-post-id="20836" data-author="Messiaen" data-date="2007-10-13T07:10:37+00:00">

Thanks, KJ.

</div>

<div class="post" data-post-id="20837" data-author="Vixn" data-date="2007-10-13T11:54:20+00:00">

Lalala sooo who was that Mage that could solo all the big mobs again  :P[/quote:2uk6cuhd]

Mages still can. We use mirrors. Mage with monk in classo will use prediction because mirrors help if prediction fail.

Monks were nerfed though and that's pity.

</div>

<div class="post" data-post-id="20838" data-author="Messiaen" data-date="2007-10-13T12:23:24+00:00">

Yeah, seems prediction was changed in a very strange way. Can still magestyle for good, but pushing/running is more challenging.

KJ, I'd like to talk to you online about that.

</div>
