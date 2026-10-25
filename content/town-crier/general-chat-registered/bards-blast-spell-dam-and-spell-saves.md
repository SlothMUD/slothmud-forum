---
title: "Bards' blast, spell dam and spell saves"
topic_id: 4654
author: "Hung"
date: 2016-07-15T09:54:22+00:00
last_activity: 2016-08-03T04:18:06+00:00
last_author: "Teron"
sticky: false
locked: false
post_count: 21
---

<div class="post" data-post-id="37061" data-author="Hung" data-date="2016-07-15T09:54:22+00:00">

Greetings,

Is bards' blast(flames of midnight, cry of avatars) affected by spell damage and/or spell saves?

I've heard various opinions on subject.

Thanks.

</div>

<div class="post" data-post-id="37075" data-author="*juggleblood*" data-date="2016-07-17T22:47:39+00:00">

My understanding was that spell damage wasn't intended to affect the damage. Only charisma.

</div>

<div class="post" data-post-id="37078" data-author="Teron" data-date="2016-07-18T07:31:37+00:00">

I heard that spell dam doesn't work on bard songs.

-saves also doesn't seem to matter, because I saw no difference from maxing charisma and -saves. I do see a -save proc on a blats song once in a while, maybe once in 20 casts.

</div>

<div class="post" data-post-id="37081" data-author="*teker*" data-date="2016-07-18T21:47:14+00:00">

Different songs have different save types.  It looks to me like the appropriate APPLY_XXX modifier is used when calculating the saves on songs.  Charisma is also used.  Spell bonus is not used when calculating damage.

</div>

<div class="post" data-post-id="37084" data-author="Hung" data-date="2016-07-19T10:23:59+00:00">

Thanks for looking into it, Teker.  Sorry I didnt understand - what is APPLY_XXX modifier?

</div>

<div class="post" data-post-id="37085" data-author="Teron" data-date="2016-07-19T10:42:48+00:00">

When I asked Splork a month or two ago, he actually said that -saves did not apply to blast/channelling bard songs, and he promised to look into it. That's the last time I heard from him.

</div>

<div class="post" data-post-id="37086" data-author="*Splork*" data-date="2016-07-19T11:34:22+00:00">

It was actually quite a few months ago and thats the last anyone heard from me :P

</div>

<div class="post" data-post-id="37087" data-author="*teker*" data-date="2016-07-19T14:13:42+00:00">

> **Quote:**
> Thanks for looking into it, Teker. Sorry I didnt understand - what is APPLY_XXX modifier?

Sorry that's codespeak for items that modify player attributes.  I was trying to say that if an item modifies the appropriate save, it should be taken into account when the bard song is cast.  But...

> **Quote:**
> When I asked Splork a month or two ago, he actually said that -saves did not apply to blast/channelling bard songs, and he promised to look into it.

I just looked at the code again and it turns out it doesn't look at the caster's save modifiers.  It's looking at the victim's save modifiers only.  The caster's charisma is taken into account instead of their saves value.

</div>

<div class="post" data-post-id="37095" data-author="Teron" data-date="2016-07-20T07:11:20+00:00">

> ***teker* wrote:**
> The caster's charisma is taken into account instead of their saves value.

Does it mean that if I have +20 charisma, it thinks I have -20 saves and increases my damage accordingly?

Or the actual "taken into account" could be that I get maybe -2-4 saves out of 20 charisma?

How exactly does it work?

Thanks.

</div>

<div class="post" data-post-id="37097" data-author="*teker*" data-date="2016-07-20T14:39:42+00:00">

> **Teron wrote:**
> Does it mean that if I have +20 charisma, it thinks I have -20 saves and increases my damage accordingly?

1 charisma point is equivalent to -1 saves when it comes to songs.  If the victim fails the save, they take full damage.  If they pass they take less (usually about 50%).  That's the same way most damage spells work.  It's an either/or type situation and not a sliding scale.  There's still some randomness in the damage calculation (die rolls) so you won't see the exact same result each time.

</div>

<div class="post" data-post-id="37105" data-author="Teron" data-date="2016-07-22T06:44:33+00:00">

So, practically, a bard with +20 charisma has pretty high chances of making the saves?

Why am I not seeing the -save color code as often, when fighting level 1 mobs at coliseum, then?

Does it mean that the charisma saves are already taken into account, and the color code is for the regular saves?

Also, if bard is capped at 20 charisma at 1x40, isn't it a bit low? I mean, ma 5th has 19 saves cap. a 5x40 bard has 24 charisma cap.

Thanks a bunch for clarifying this for me/us.

</div>

<div class="post" data-post-id="37134" data-author="*teker*" data-date="2016-07-25T14:49:35+00:00">

> **Teron wrote:**
> So, practically, a bard with +20 charisma has pretty high chances of making the saves?

I would expect it to be the same as a mage with -20 saves.  I haven't spent much time in the coliseum so I'm not sure what sort of success you would expect to see with those numbers.

I don't think the code applies save color to songs.  I don't see it in cry of the avatar, anyway.

> **Quote:**
> Also, if bard is capped at 20 charisma at 1x40, isn't it a bit low? I mean, ma 5th has 19 saves cap. a 5x40 bard has 24 charisma cap.

The cap formulas for saves and charisma are fairly different.  Both are based on class order but saves cap is higher.  Charisma cap rises with number of 40s but saves does not.

</div>

<div class="post" data-post-id="37136" data-author="Teron" data-date="2016-07-26T10:38:11+00:00">

Yeah, I've done the math in [the other bard suggestions thread](http://www.slothmud.org/forum//viewtopic.php?t=4659) and I guess the amount of charisma is ok.

The problem is, though, that bards' -saves eq has no effect on it. Could this be improved?

Thanks.

</div>

<div class="post" data-post-id="37138" data-author="*juggleblood*" data-date="2016-07-26T16:41:50+00:00">

Dude, you're basically asking to nerf cry of the avatar. I don't want my cry to depend on my spellsaves. My spellsaves cap is like 12. Think about it, using charisma for both the save and damage means that the bard can focus on charisma and AC. I think you're crazy for wanting it to depend on spell save. It's a bard song, not a mage spell, hence the term "SPELL_saves".

</div>

<div class="post" data-post-id="37144" data-author="Teron" data-date="2016-07-27T06:18:27+00:00">

I was asking if adding up those saves would work.

If the only way to make it work is to detach charisma and saves (ie, -saves won't be buffed by charisma), then sure, don't do anything.

</div>

<div class="post" data-post-id="37145" data-author="*juggleblood*" data-date="2016-07-27T14:52:28+00:00">

You still dont get it. It is better for the bard that saves don't count. What you are asking for is a penalty. When I'm area blasting stuff, in chaos pit for example, I don't want to have to be geared up in a charisma+saves mode. I want to be geared up in charisma+AC. Even if you come up with some formula that combines charisma and saves, it is ultimately a penalty. What is your bard's spellsave in max_charisma? Why even focus on this issue? I find my cry to be thoroughly satisfying.

</div>

<div class="post" data-post-id="37149" data-author="Teron" data-date="2016-07-28T09:15:06+00:00">

That's precisely the point, I find my cry thoroughly lacking in solo coliseum.

I gear up in max mana (650 total), then max charisma, start blasting, and I'm out of mana with 1 min before the orb, because it costs 30-ish mana and mobs just soak the blasts. That's why my experience there is meek, even compared to a thief without blast.

Ac doesn't help me a whole lot to kill solo mobs faster.

I'd like to be able to use my -saves eq to complement my cry, because right now the damage in coliseum doesn't cut it. I'll probably have to get 38ma or 30 monk to do better and that says something.

On the other hand, bards in the chaos pit do rock, because they possess a mini firestorm at 1x40, and two bards can streamroll the pit like nobody's business. However, the scenario of a bard fighting many similarly-sized mobs outside the chaos pit is very rare.

</div>

<div class="post" data-post-id="37150" data-author="*Breeze*" data-date="2016-07-29T05:17:21+00:00">

I can just about guarantee we will not be adjusting skills/spells/basic game play based on coliseum. 

Coliseum mobs do not necessarily represent the  game.

We did consider redoing the magic system but my concern is that players would see it as "nerfing" instead of balancing.

In the long run it would allow for greater control over skills/spells and we would be able to automatically rank skills aND spells in order of damage/effect, but I don't think we will do it,simply because I don't want to deal with a million questions.  

Maybe we do it for sloth 5. ;)

</div>

<div class="post" data-post-id="37151" data-author="Ker" data-date="2016-07-29T06:03:36+00:00">

Hiiiiiiiiiiiiiiiiiiiiiiiiii Breezy!

</div>

<div class="post" data-post-id="37153" data-author="*Breeze*" data-date="2016-07-29T12:37:11+00:00">

> **Ker wrote:**
> Hiiiiiiiiiiiiiiiiiiiiiiiiii Breezy!

Hey :)

</div>

<div class="post" data-post-id="37164" data-author="Teron" data-date="2016-08-03T04:18:06+00:00">

Just to be clear, Sochi has persuaded me that it won't be coded that -saves would only add to the bard saves, which means, like he says, if there are any changes, it'll only make things worse for the bard.

So consider this case dismissed, as if it wasn't already.

Also, the original stimulus was that help saves says that it helps channelling spells, so I guess it should add that "but not the bard songs".

And no, coliseum is not an isolated small world, it clearly shows which classes - or people - can solo well - with the caveats that they could be geared differently and benefit from their mana thanks to the only-mana-restore in coliseum.

</div>
