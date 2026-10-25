---
title: "Tumbling defense doesn't work"
topic_id: 4833
author: "Dragoth"
date: 2018-02-15T06:05:14+00:00
last_activity: 2018-02-16T06:29:15+00:00
last_author: "Dragoth"
sticky: false
locked: false
post_count: 3
---

<div class="post" data-post-id="38668" data-author="Dragoth" data-date="2018-02-15T06:05:14+00:00" data-subject="Tumbling defense doesn&#x27;t work">

Tumbling defense doesnt seem to work with active Aerial servant (cleric prime).

Although I'm not sure if its a a bug or another cleric handicap, but thought i'd report it anyway.

</div>

<div class="post" data-post-id="38669" data-author="*teker*" data-date="2018-02-15T15:57:13+00:00" data-subject="Re: Tumbling defense doesn&#x27;t work">

This may be part of a biggest question - what order should damage bonuses and reductions be applied?  I looked at this once and was hesitant to mess with it due to the changes in gameplay that would occur.  The short answer to your question is that your aerial servant gets applied before the tumbling defense so you would only see it when your servant is down.

Here's a list of how damage is modified before it is applied to the victim (not all are applicable to a given attack):

Original attack damage roll calculated (weapon, barehand, spell, mob attack, etc)

Add bonus damage for barehanded monk (based on monk level)

Add bonus damage for warrior melee attack (based on warrior level)

Add Berserk skill bonus

Add Frenzy skill bonus

Add Weapon Damage bonus

Add victim Excruciating Pain bonus

Add Focus skill bonus

Check Ethereal

Add Critical Hit or Massive Critical Hit bonus

Subtract damage if victim has Aerial Servant

Add damage if victim is fishing

Subtract victim damage reduction

Subtract damage for tumbling defense, oghams psalm of discipline

Subtract damage for victim shield of thorns

Subtract damage for victim sanctuary/aegis or wall of flesh/flesh golem or shield of faith/morning glory

Subtract damage for victim defy pain or endure pain

Subtract damage for victim fluidity or greater fluidity

Check victim mirror images

Subtract damage for victim spell shield

Check victim reflection

Check victim spectral shield

Check victim resist fire/cold

Apply damage to victim

The order of things doesn't really make sense to me - it seems like things like further from the victim should apply first (attacker bonuses, mirror, wall of flesh, shield of thorns, etc).  Things closer to the victim would apply last (damage reduction, excruciating pain, etc).

In response to your specific question about aerial servant I would ask - should the servant behave like a dumb wall and stand in front of all melee attacks?  Or is its magical nature smart and fast enough to only stand in front of an attack after a tumbling or similar maneuver fails?

The other issue I see is with reflection.  When a spell is reflected the attacker and victim are flipped but the list doesn't get re-run.  So the damage will be reduced if the original victim has sanctuary but not if the original caster has it.  That seems backwards to me - it seems more logical to me that the reflection would occur before sanctuary check and that the caster's sanctuary would be the one that affects the final damage amount.

</div>

<div class="post" data-post-id="38671" data-author="Dragoth" data-date="2018-02-16T06:29:15+00:00" data-subject="Re: Tumbling defense doesn&#x27;t work">

I can dodge and counterattack before aerial servant, so it doesn't make any logical sense that I can't tumble away before he gets hit.

Also, when  a mob misses me its not hitting aerial servant either, so it's most definitely not a self-sufficient separate entity.

So it's either a handicap or an unintended bug. 

And as far as handicaps go, I would posit that aerial servant should be more inline with shield of thorns for the fairness. Clerics are not the most sought-after solo class and I don't see why aerial servant has to be weaker than shield of thorns, given that the are very similar at their core. And having a 3x40 druid myself, I can say for sure that shield of thorns is a much more desirable skill because it has more health, can be used with backstab/deathgrip and has passive damage on top of it.

I understand that the number of people who can deal with game-balancing issues at the moment is extremely short, but I guess this will have to wait until one of them decides this is something worth thinking about.

Thank you for your attention Teker, I greatly appreciate everything you do for this game.

</div>
