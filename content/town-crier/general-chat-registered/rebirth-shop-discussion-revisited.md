---
title: "Rebirth shop discussion revisited"
topic_id: 4880
author: "*teker*"
date: 2018-11-17T18:19:44+00:00
last_activity: 2019-01-23T04:49:14+00:00
last_author: "Josiah"
sticky: false
locked: false
post_count: 30
---

<div class="post" data-post-id="38999" data-author="*teker*" data-date="2018-11-17T18:19:44+00:00">

I may have some time to put into the shop so lets rehash this and try to figure out an acceptable cost rate.  I have started with Fluffy's previous post that laid out the following costs:

> **Quote:**
> Dam(50 bils starting, 1.47 coef).
> 
> Hand dam (25b starting, 1.2 coef)
> 
> Spell Bonus (5bils starting, 1.037 coef)
> 
> Mana/hp/mv (2.5b starting, 1.018 coef)
> 
> Hit (37.5 starting, 1.47 coef)

Are these reasonable values to start from?  My first reaction is that mana/hp/mv are not equal.

Should there be caps on these stats and if so, what?

What other stats and at what costs?

What perma spells and at what costs?

Previously I put the stats above into a proc with caps that looks like this.

> **Quote:**
> +1   Hit Points      -   0 of 100 -   2.50 B xp    1.2 M gold
> 
>  +1   Mana Points     -   0 of 100 -   2.50 B xp    1.2 M gold
> 
>  +1   Movement Points -   0 of 100 -   2.50 B xp    1.2 M gold
> 
>  +1   Hit Roll        -   0 of  10 -  37.50 B xp   18.8 M gold
> 
>  +1   Damage Roll     -   0 of  10 -  50.00 B xp   25.0 M gold
> 
>  +1   Hand Damage     -   0 of  10 -  25.00 B xp   12.5 M gold
> 
>  +1   Spell Damage    -   0 of  10 -   5.00 B xp    2.5 M gold

I can't remember how the gold numbers were computed but it's a ratio of the xp.

</div>

<div class="post" data-post-id="39000" data-author="*Idjit*" data-date="2018-11-17T22:06:35+00:00">

I for one, if nothing else different happens would like

HP

Mana

Moves

To be open ended but with exponential cost curves.*

I'll start with that.

Thanks

--Idj

*I had seen this on Tsunami II LPMud as early as October 1991 when i first started mudding.

Actually that's a discussion that bleeds into an expansion of the regular 9x40 shop, i just realized that. but i see no reason why rebirthers-in-progress couldn't keep chipping away at mundane things like hp/mana/move max. It still fits.

</div>

<div class="post" data-post-id="39001" data-author="Gorka" data-date="2018-11-18T07:42:47+00:00">

I think the time has probably come just to implement what you think was right from the last time we all discussed the shop specifically Teker. (I just want to see something go in - before the usual class/skill stink derails the discussion) I also favour Idjit's exponential increase ideas, on top of those proposed by myself and some adjustments to that by Fluffy. I would forecast the return of the Gork post Dec 14th if such a shop occurred.

</div>

<div class="post" data-post-id="39003" data-author="Driven" data-date="2018-11-18T23:50:18+00:00">

Gorka had a good proposal here, which is a fair place to start:  

[<LINK_TEXT text="http://www.slothmud.org/forum/viewtopic ... =15#p38849">http://www.slothmud.org/forum/viewtopic.php?f=28&t=4851&start=15#p38849</LINK_TEXT>](http://www.slothmud.org/forum/viewtopic.php?f=28&t=4851&start=15#p38849)

One thing to consider on the cost of AC is that AC applies when in-form, but max_dex does not, so the value of actual AC is higher than max_dex in that regard.  I think the penalty in the original avatar shop was too high... 30b for 0.1 ac is a bit much when max_dex was 50b... I would probably cut the difference, so .1 ac in the rebirth shop should probably be the avatar-shop-equivalent of 20b, which would be 50b in the rebirth shop.

</div>

<div class="post" data-post-id="39004" data-author="cyprimus" data-date="2018-11-19T13:23:37+00:00">

really comes down to are we going to go with unlimited potential, or keep a hard cap of some sort?

hp mana and moves are all the same value depending on build.

i agree with driven, raw ac is too expensive.

I have posted several times about various methods of adding to the shop.. tiers, raw formulas, just to caps.. etc..

Just do something!

LOL.. sorry, been barely active last 6? months.. 

I personally have maxx'ed avvies in ..what 5 classes now.. and i found the numbers for the shop to be fairly accurate, accept for ac.  That is comparison values

What i would keep in mind is, this will determine how the endgame plays out... do you want one class favored, or want all max avvies to look the same in the end.. or all of them to be min/maxing... etc,,' , buy making it unlimited it encourages single characters with no alts for example..

I do not mind either way, just wanna know what to expect down the road.

I suggest limit stats to classo caps,  but let the rest be infinite.

Thanks!

All our heros are mathmaticians!... p

</div>

<div class="post" data-post-id="39005" data-author="norks" data-date="2018-11-19T17:26:12+00:00">

From my perspective, being able to purchase increasingly expensive mana, hp, moves or ac wouldn’t add anything to the game. I probably wouldn’t bother, preferring instead to play another character. What I would find attractive is the chance to buy different spells, skills and abilities either from other prime classes or totally new things.

</div>

<div class="post" data-post-id="39006" data-author="Filk" data-date="2018-11-19T18:34:17+00:00">

I will not touch anything about crossclass things, since its totally diferent changes with global worktime. While we have one active coder - just keep that door closed. For those, who dont want to raise stats, well, another char is working perspective.

About the shop - i agree with Cyp, its all about it to be capped or not. Everything else could be balanced after first question has an answer.

Personally for me - i prefer infinite progression with values that naturally limit that progression on its own, because high numbers require enormous time spent. Every player choose what to invest time on. Should that be 1-2 stats maxed, or everything well rounded, its personal choice. 

When i offered values and coefs Teker mentioned, i had in mind, that missing stats has the same values as stats with similiar cost values in current avatar shop. And i calculated progression coefficients for each such cost iirc.

</div>

<div class="post" data-post-id="39007" data-author="norks" data-date="2018-11-19T20:59:51+00:00">

Well then there’s really no need for a rebirth shop. And there’s really no discussion either. Just add these things to the avatar shop. Or do you have to run through 9x40 twice to buy more mana and hp, etcetera?

</div>

<div class="post" data-post-id="39008" data-author="cyprimus" data-date="2018-11-20T04:43:13+00:00">

The next step is deciding if its a second shop, so the new costs go in after the current shop is maxed, for example, are ppl going to have to pay more for hp now ...or can they still get that first 100 for a bil a pop.

Also, they dont have to be the same for all... for example, max stats should, imo be buyable too classo limit only.

Same could be said for damage reduction etc..  do we want ppl buying bonus spell bonus too infinitude?

maybe other items can be purchased to unlimited amounts.. like hp

My concern on this is i have seen too many broken systems...  eg- either all characters look  the same in the end, cause its only think point efficient, or you get everyone buying one stat forever to abuse..

Main point is realizing that each ability or stat can have its own system, or they can all follow one.

Also, on mana... one thing i have NOT seen ...reduced cast for spells/or spell stacks...   IE- spend to reduce the cost to cast.. cure light... and then cure normal etc.. up to resto or mass heal.. this is obviously subject to considerable abuse as a generic, so you would want to make it spell specific.. 

Next question is.. are we going to try and please everyone, or make a recommended play style? 

For example, presently damage is heavily favored, and many ppl have multiple alts.. Do we want to encourage this, discourage it, or ignore?

What about groups? are we going to have the best ppl never wanting to group cause solo is so much better for them..?  This leads into escalation.... they high end players get more powerful, so mobs are tweeked to deal with them, and the lower end players can never keep up...same deal with ppl that are limited in play time..

OK, done rambling..  for now.. back later for more ...ramblings..

</div>

<div class="post" data-post-id="39009" data-author="Gorka" data-date="2018-11-20T06:25:38+00:00">

On the first topic of a second shop, I think that's a no brainer... the prices are different between rebirth and avatar shop and they work differently, and it's better to keep the systems separate so each could be deactivated if required without messing each other up.

On the second issue of caps vs no caps. It's clear everyone sees this as a sensitive topic, and no one wants to see sloth become unbalanced. It's also difficult to predict what will happen because it's a complex topic with lots of variables complicated by different player styles. I think the safest thing to do is to take the middle road and "turn on the tap slowly" ie, implement caps on the new shop while promising to review them. The system could still be written exponentially, just with a temporary static max limit that can be updated (mainly on the damage stats). I'm suggesting we follow Fluffy's unlimited exponential path but just throttle the improvements for a period of review. We could write 100 posts on this forum about what we think might happen and still be wrong. Let's get in the shallow end of the pool where we can stand, and walk towards the deep end.

I have faith in the likes of Teker and Breeze to review those caps in time. The immortal team at the moment is the best I remember. Well everyone except Idjit... Well, Idjit to I guess...   :twisted:

</div>

<div class="post" data-post-id="39010" data-author="Filk" data-date="2018-11-20T12:55:58+00:00">

> **Gorka wrote:**
> I'm suggesting we follow Fluffy's unlimited exponential path but just throttle the improvements for a period of review.

Sounds good. Keep the formulas, limit dam at 5-10 and other stats accordingly based on their value compared to dam. Maybe excluding hp/ma/mv from limit isnt that terrible as well though. Tune down ac probably also.

</div>

<div class="post" data-post-id="39011" data-author="*teker*" data-date="2018-11-26T18:01:04+00:00">

Ok, so here's my present list with caps lowered to 3 atm:

```
 1)   +1  Max Strength           -   0 of   1 -  50.00 B xp   25.00 M gold
 2)   +1  Max Intelligence       -   0 of   1 -  50.00 B xp   25.00 M gold
 3)   +1  Max Wisdom             -   0 of   1 -  50.00 B xp   25.00 M gold
 4)   +1  Max Dexterity          -   0 of   1 - 125.00 B xp   62.50 M gold
 5)   +1  Max Constitution       -   0 of   1 -  50.00 B xp   25.00 M gold

 6)   +1  Hit Points             -   0 of 100 -   2.50 B xp    1.25 M gold
 7)   +1  Mana Points            -   0 of 100 -   2.50 B xp    1.25 M gold
 8)   +1  Movement Points        -   0 of 100 -   2.50 B xp    1.25 M gold
 9)   +1  Hit Point Regen        -   0 of  40 -   6.25 B xp    3.12 M gold
10)   +1  Mana Point Regen       -   0 of  10 -  25.00 B xp   12.50 M gold
11)   +1  Movement Point Regen   -   0 of  30 -   8.33 B xp    4.17 M gold

12)   +1  Hit Roll               -   0 of   3 -  37.50 B xp   18.75 M gold
13)   +1  Damage Roll            -   0 of   3 -  50.00 B xp   25.00 M gold
14)   +1  Bonus Circle Damage    -   0 of   3 -   5.00 B xp    2.50 M gold
15)   +1  Bonus Flail Damage     -   0 of   3 -   5.00 B xp    2.50 M gold
16)   +1  Bonus Hand Damage      -   0 of   3 -  25.00 B xp   12.50 M gold
17)   +1  Bonus Kick Damage      -   0 of   3 -   5.00 B xp    2.50 M gold
18)   +1  Bonus Spell Damage     -   0 of   3 -   5.00 B xp    2.50 M gold
19)   +1  Bonus Stab Damage      -   0 of   3 -   2.50 B xp    1.25 M gold
20)   +1  Bonus Weapon Damage    -   0 of   3 -  25.00 B xp   12.50 M gold

21) -0.1  Armor Class            -   0 of   3 -  25.00 B xp   12.50 M gold
22)   +1  Bonus Charisma         -   0 of   3 -   5.00 B xp    2.50 M gold
23)   +1  Bonus Damage Reduction -   0 of   3 -  25.00 B xp   12.50 M gold
24)   +1  Bonus Heal Bonus       -   0 of   3 -   5.00 B xp    2.50 M gold
25)   +1  Bonus System Shock     -   0 of   3 -   5.00 B xp    2.50 M gold
26)   +1  Bonus Undead Control   -   0 of   3 -   5.00 B xp    2.50 M gold

27)   -1  Save Breath            -   0 of   3 -   5.00 B xp    2.50 M gold
28)   -1  Save Paralyzation      -   0 of   3 -   5.00 B xp    2.50 M gold
29)   -1  Save Petrification     -   0 of   3 -   2.50 B xp    1.25 M gold
30)   -1  Save Poison            -   0 of   3 -   2.50 B xp    1.25 M gold
31)   -1  Save Spell             -   0 of   3 -  25.00 B xp   12.50 M gold
```

Things I changed:

- Gorka's post had +3 Move Regen and +4 Hit Point Regen and I have changed these to +1 at a fraction of the original cost.

Questions:

- Is the coefficient for scaling identical for items of similar cost?  IE - do I copy the coefficient for Hit Points to all items that have a base cost of 2.5B?

- Do you guys really think that Movement Points are as valuable as Hit Points?  Or that either are as valuable as Mana Points?

</div>

<div class="post" data-post-id="39012" data-author="Gorka" data-date="2018-11-27T06:18:41+00:00">

Nice Teker! That's genuinely exciting to see. Just one thing I noticed.

Spellbonus/Healbonus/Stab/Circle/Flail/Kick should probably have a 10 cap and not 3 in my opinion to start with.

>Is the coefficient for scaling identical for items of similar cost? IE - do I copy the coefficient for Hit Points to all items that have a base cost of 2.5B?

It's probably ok... as there are caps at the moment. Without caps... something players might buy 100 of probably shouldn't have the same coefficient for something they will only buy 5 of - that would be a potential concern. (Even if the original costs were the same) IE, should the coefficient for HP be the same as Save's Petri... mmmm, nnnnaa, maybe not.

>Do you guys really think that Movement Points are as valuable as Hit Points? Or that either are as valuable as Mana Points?

Movement points are valuable to "some." Warriors, Thieves, Monks. I doubt your average scrawny mage is going to buy them. They won't be as valuable as mana points to anyone I would think.

</div>

<div class="post" data-post-id="39013" data-author="Filk" data-date="2018-11-27T15:40:35+00:00">

Seems nice, but i have some observations.

Identical coefs for same base cost - imo its fine. But caps in that case should be proportional. 

Its unfair atm, that some classes get more profit then others from that shop. 

For example 3 bonus spell damage is a joke. While 3 dam is quite big addition.

If we picking damroll as a standart proportion, and its cap set at 3, then other stats should be capped at 150bils of base value.

It will be 30 bonus spell damage(and same for all other 5bils bonuses to secondary stats), 6 for ac, something around 5 for hitroll, 6 for save spell and so on.

Maybe with exclusion for saves. Or actually make saves cost higher(closer to spell saves).

Just as a weird idea. Cap could be incremental overtime. 

Like linear formula to increase each stat cap by some number each year or two. 1 for dam, and equivalent for other stats based on its values compared to dam.

About moves - tbh, i dont think its equal to mana/hp. I am not even sure anybody buying it at current shop at all.

As for me, its should be two times cheaper then mana and hp to make it competitive.

But i could say the same for circle, kick, flail and most of the saves.

</div>

<div class="post" data-post-id="39014" data-author="*Idjit*" data-date="2018-11-27T23:54:47+00:00">

One thing we haven't talked about regarding the rebirth shop (both shops really), is possibly having the costs actually be different for the different prime classes.  Or maybe we did and i'm just crappy at following threads.  If so, sorry.

Like having spellbonus be cheaper for a mage prime than for a monk prime

And handdam be cheaper for a monk prime than for a mage prime

Which would resolve some of the back and forth, for example  Driven might want some of the more muscular bonuses to be cheaper than the proposed costs, but his is a NC view point.

Whereas I might want some of the healbonus and spellbonus things to be cheaper than the proposed costs, but mine is a CA view point.

But

A) it's very hard to set up relative costs as a whole matrix of the whole shop for each prime

B) the discussion is so far advanced now that this just opens another can of worms and the resultant back and forth might be just horrible

C) the general 9x40 shop is already Not Set Up That Way

But if someone had massive hours of time on their hands (which is none of us) and were willing to build whole matrices for each class, it might in the super long run be better I don't know.

Just saying.

--Idj

</div>

<div class="post" data-post-id="39015" data-author="Josiah" data-date="2018-11-29T07:44:02+00:00">

20 base strength??  You have my vote!

</div>

<div class="post" data-post-id="39016" data-author="*teker*" data-date="2018-11-30T22:36:22+00:00">

So it sounds like you want the caps to look like this:

```
12)   +1  Hit Roll               -   0 of   3 -  37.50 B  /   18.75 M
13)   +1  Damage Roll            -   0 of   3 -  50.00 B  /   25.00 M
14)   +1  Bonus Circle Damage    -   0 of  30 -   5.00 B  /    2.50 M
15)   +1  Bonus Flail Damage     -   0 of  30 -   5.00 B  /    2.50 M
16)   +1  Bonus Hand Damage      -   0 of   6 -  25.00 B  /   12.50 M
17)   +1  Bonus Kick Damage      -   0 of  30 -   5.00 B  /    2.50 M
18)   +1  Bonus Spell Damage     -   0 of  30 -   5.00 B  /    2.50 M
19)   +1  Bonus Stab Damage      -   0 of  60 -   2.50 B  /    1.25 M
20)   +1  Bonus Weapon Damage    -   0 of   6 -  25.00 B  /   12.50 M

21) -0.1  Armor Class            -   0 of   3 -  25.00 B  /   12.50 M
22)   +1  Bonus Charisma         -   0 of   3 -   5.00 B  /    2.50 M
23)   +1  Bonus Damage Reduction -   0 of   3 -  25.00 B  /   12.50 M
24)   +1  Bonus Heal Bonus       -   0 of  30 -   5.00 B  /    2.50 M
25)   +1  Bonus System Shock     -   0 of   3 -   5.00 B  /    2.50 M
26)   +1  Bonus Undead Control   -   0 of   3 -   5.00 B  /    2.50 M
```

</div>

<div class="post" data-post-id="39017" data-author="Teron" data-date="2018-12-01T04:19:29+00:00">

I just hope that eventually you figure out coefficients and remove the caps.

That'd allow sticking to a certain classo and playing in it - up to the soft caps, of course.

imho, if a mana point cost 10 coins, then a hp would be worth 4-5 coins and a move would cost 3-4 coins.

</div>

<div class="post" data-post-id="39018" data-author="cyprimus" data-date="2018-12-01T07:43:46+00:00">

was thinking more along the lines of a set price for stat.. then an ever increasing price too raise the cap.. so you could hit classo limits.. relatively fast.. then slowly build past..

</div>

<div class="post" data-post-id="39019" data-author="cyprimus" data-date="2018-12-01T16:44:19+00:00">

sorry, had to go..

just offering alternative ways

base cost for stat... +the multiplier

also.. this will break some systems

eg-just buy damage reduction... 100...i suggest just capping damage reduction at class limit maybe with a + based on the highest possible ingame to not be abusive

Same applies to others.. just think.. whats the worse case if this gets too...whatever number... eg-  resist fire 100 likely is immuned too fire.. not a huge deal..but maybe bad if certain critters in game only do flame damage..etc

think out each option.. set your limit based on balance.. not on what someone wants... etc..

and remember it will stack with eq as well as other bonus' 

Gl!

</div>

<div class="post" data-post-id="39020" data-author="Teron" data-date="2018-12-02T09:29:16+00:00">

Straight multipliers and caps are inefficient.

The way I've seen this done is with increasing logarithmic coefficients - they allow one to invest as much time as he wants into hp, while others get a much smaller amount in a very brief period.

</div>

<div class="post" data-post-id="39021" data-author="Filk" data-date="2018-12-03T08:33:05+00:00">

> ***teker* wrote:**
> So it sounds like you want the caps to look like this:
> 
> 
> 

```
12)   +1  Hit Roll               -   0 of   3 -  37.50 B  /   18.75 M
13)   +1  Damage Roll            -   0 of   3 -  50.00 B  /   25.00 M
14)   +1  Bonus Circle Damage    -   0 of  30 -   5.00 B  /    2.50 M
15)   +1  Bonus Flail Damage     -   0 of  30 -   5.00 B  /    2.50 M
16)   +1  Bonus Hand Damage      -   0 of   6 -  25.00 B  /   12.50 M
17)   +1  Bonus Kick Damage      -   0 of  30 -   5.00 B  /    2.50 M
18)   +1  Bonus Spell Damage     -   0 of  30 -   5.00 B  /    2.50 M
19)   +1  Bonus Stab Damage      -   0 of  60 -   2.50 B  /    1.25 M
20)   +1  Bonus Weapon Damage    -   0 of   6 -  25.00 B  /   12.50 M

21) -0.1  Armor Class            -   0 of   3 -  25.00 B  /   12.50 M
22)   +1  Bonus Charisma         -   0 of   3 -   5.00 B  /    2.50 M
23)   +1  Bonus Damage Reduction -   0 of   3 -  25.00 B  /   12.50 M
24)   +1  Bonus Heal Bonus       -   0 of  30 -   5.00 B  /    2.50 M
25)   +1  Bonus System Shock     -   0 of   3 -   5.00 B  /    2.50 M
26)   +1  Bonus Undead Control   -   0 of   3 -   5.00 B  /    2.50 M
```

Something that looks more like a truth. Though i would raise ac and damage reductions caps to 6 also, they are not balance breaking at this point.

And some stats are missing, so not sure what values are there.

</div>

<div class="post" data-post-id="39022" data-author="Driven" data-date="2018-12-03T18:57:27+00:00">

So maybe something like this?

```
 1)   +1  Max Strength           -   0 of   1 -  50.00 B xp   25.00 M gold
 2)   +1  Max Intelligence       -   0 of   1 -  50.00 B xp   25.00 M gold
 3)   +1  Max Wisdom             -   0 of   1 -  50.00 B xp   25.00 M gold
 4)   +1  Max Dexterity          -   0 of   1 - 125.00 B xp   62.50 M gold
 5)   +1  Max Constitution       -   0 of   1 -  50.00 B xp   25.00 M gold

 6)   +1  Hit Points             -   0 of 100 -   2.00 B xp    1.25 M gold
 7)   +1  Mana Points            -   0 of 100 -   2.50 B xp    1.5  M gold
 8)   +1  Movement Points        -   0 of 100 -   1.50 B xp    1    M gold
 9)   +1  Hit Point Regen        -   0 of  40 -   6.25 B xp    3.12 M gold
10)   +1  Mana Point Regen       -   0 of  10 -  25.00 B xp   12.50 M gold
11)   +1  Movement Point Regen   -   0 of  30 -   8.33 B xp    4.17 M gold

12)   +1  Hit Roll               -   0 of   3 -  37.50 B  /   18.75 M
13)   +1  Damage Roll            -   0 of   3 -  50.00 B  /   25.00 M
14)   +1  Bonus Circle Damage    -   0 of  30 -   5.00 B  /    2.50 M
15)   +1  Bonus Flail Damage     -   0 of  30 -   5.00 B  /    2.50 M
16)   +1  Bonus Hand Damage      -   0 of   6 -  25.00 B  /   12.50 M
17)   +1  Bonus Kick Damage      -   0 of  30 -   5.00 B  /    2.50 M
18)   +1  Bonus Spell Damage     -   0 of  30 -   5.00 B  /    2.50 M
19)   +1  Bonus Stab Damage      -   0 of  60 -   2.50 B  /    1.25 M
20)   +1  Bonus Weapon Damage    -   0 of   6 -  25.00 B  /   12.50 M

21) -0.1  Armor Class            -   0 of   5 -  25.00 B  /   12.50 M
22)   +1  Bonus Charisma         -   0 of   3 -   5.00 B  /    2.50 M
23)   +1  Bonus Damage Reduction -   0 of   5 -  25.00 B  /   12.50 M
24)   +1  Bonus Heal Bonus       -   0 of  30 -   5.00 B  /    2.50 M
25)   +1  Bonus System Shock     -   0 of   3 -   5.00 B  /    2.50 M
26)   +1  Bonus Undead Control   -   0 of   3 -   5.00 B  /    2.50 M

27)   -1  Save Breath            -   0 of   3 -   5.00 B xp    2.50 M gold
28)   -1  Save Paralyzation      -   0 of   3 -   5.00 B xp    2.50 M gold
29)   -1  Save Petrification     -   0 of   3 -   2.50 B xp    1.25 M gold
30)   -1  Save Poison            -   0 of   3 -   2.50 B xp    1.25 M gold
31)   -1  Save Spell             -   0 of   3 -  25.00 B xp   12.50 M gold
```

And then I think a few more perm spells would be amazing.  Here are some thoughts:

```
32)   Greater Fluidity           -   0 of   1 -   65  B xp   32.50 M gold
33)   Resist Webs                -   0 of   1 -   35  B xp   16.50 M gold
34)   Blessing of the Avatar     -   0 of   1 -   20  B xp   10.00 M gold
35)   Improved Haste             -   0 of   1 -   125 B xp   65.00 M gold
36)   Natures Restoral           -   0 of   1 -   35  B xp   15.00 M gold
37)   Rejuvenation               -   0 of   1 -   12.5 B xp  12.00 M gold
```

</div>

<div class="post" data-post-id="39023" data-author="Teron" data-date="2018-12-04T03:07:39+00:00">

It seems suggested caps on saves are low.

Compare 30 spell bonus to 130 spellbonus cap of a mage, that's about 25%.

At -32 saves cap, 3 saves is about 9%.

To match the proportions, it'd make sense to cap saves at 7.

If we look at someone with mage in the late classes:

about 50 spell dam cap, can get 30bsb (60%) more from the shop.

About 10-11 saves cap, can get 3 (30%) saves from the shop.

Again, capping saves at 6-7 would make the increases proportional.

Also, saves are capped.

Maybe there should be bonus -saves.

</div>

<div class="post" data-post-id="39024" data-author="cyprimus" data-date="2018-12-04T10:17:26+00:00">

I would still like to see being able to buy everything up to my classo caps first, all i am seeing on the posts now is over cap bsb etc..

I suggested a single cost for the base.. that is not going over cap.. getting it too your classo limite, and an ever increasing cost for going over cap.

Love too see more perma spells added. Starting with the list above, perhaps perm  water breath... and others that have items in game already...

thanks!

</div>

<div class="post" data-post-id="39025" data-author="cyprimus" data-date="2018-12-04T11:27:57+00:00">

OH, also.. can we get gauranteed masterfuls for spells that are really nice for that?

</div>

<div class="post" data-post-id="39029" data-author="Josiah" data-date="2018-12-10T20:48:21+00:00">

Like Driven, I'd like more options for persistent spells.

Please add perception!  Currently buying Avatar Sight from the mayor is a disaster because it doesn't come with perception.  If not, then I'd like to buy detect invisibility and darksight (without avatar sight).

Other spells I'd like to see that weren't on Driven's list:

Greater Mobility

Grace (should be expensive - this would void alignment restrictions on casting it)

Protection from Good (same)

Greater Fluidity has similar issues to Avatar Sight; it has extra power with a masterful cast.  If the permanent version is only regular strength, tanks may have to avoid taking it.  If the rebirth shop grants the masterful version, it should be extra expensive.

</div>

<div class="post" data-post-id="39035" data-author="cyprimus" data-date="2019-01-02T17:58:35+00:00">

OK, remembered, was going to post about being able to sell back to the shop too

I suggest being able too get the exp, or the gold back.. not both..or not all at least

for example... being able to cash in for 100 percent.. but you have to choose so... 40 percent exp, 60 percent of the coins spent... or any other variation adding up to 100 percent.  So you could get all the exp or all the coins back from a bad purchase... but not 100 percent of both..

</div>

<div class="post" data-post-id="39036" data-author="cyprimus" data-date="2019-01-04T14:50:20+00:00">

OH, would also be exceptionally  nice to be able to get perma corpus.

</div>

<div class="post" data-post-id="39074" data-author="Josiah" data-date="2019-01-23T04:49:14+00:00">

> **Quote:**
> Please add perception! Currently buying Avatar Sight from the mayor is a disaster because it doesn't come with perception. If not, then I'd like to buy detect invisibility and darksight (without avatar sight).

Please disregard that second request.  Apparently detect invisible and darksight are still available from the mayor!  I just got both tonight for 5 million each.

The mayor doesn't list the prices, but still sells them.  Awesome!

</div>
