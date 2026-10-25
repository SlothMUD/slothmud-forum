---
title: "toggle light"
topic_id: 1892
author: "Weasel"
date: 2006-05-22T22:14:23+00:00
last_activity: 2006-05-24T22:34:08+00:00
last_author: "12345"
sticky: false
locked: false
post_count: 17
---

<div class="post" data-post-id="12641" data-author="Weasel" data-date="2006-05-22T22:14:23+00:00" data-subject="toggle light">

A long shot, but would it be possible to code so that we can toggle our light on/off without having to remove it and thus lose its effects as well? 

ie: lightoff/lighton so can run thru dark areas, but not lose other properties of the light eq.. I mean hell, irl a flashlight doesn't need to be turned on to make it a formidible weapon in a pinch, does it.

   :twisted:

</div>

<div class="post" data-post-id="12642" data-author="kjartan" data-date="2006-05-22T22:56:40+00:00" data-subject="">

One way to do this would be to make it a 'dark cloak' effect (if it isn't already - don't have the code handy to check).

</div>

<div class="post" data-post-id="12643" data-author="Qa" data-date="2006-05-22T23:58:35+00:00" data-subject="">

Wow, KJ that would really rock.

(If it is in place and I didn't know, it's my own fault.  I always thought dark cloak was a sanc thing.)

It seems that my character has always had a 'catch if running through an aggro area' flag on it.  Heck, it even happenned again today - I got splorked for 850hp through -10 AC whilst sneaking.  If dark cloak would solve this, I would use it much more frequently...

Thanks.

Qa

</div>

<div class="post" data-post-id="12646" data-author="kjartan" data-date="2006-05-23T03:13:40+00:00" data-subject="">

Ok, a little examination of the code shows me that there is already a spell for this, the necro spell darkness.  So in the interest of not taking a necro spell and giving it to clerics, we aren't going to do this.  Also no toggleable lights.

</div>

<div class="post" data-post-id="12647" data-author="Weasel" data-date="2006-05-23T03:23:28+00:00" data-subject="">

So in the interest of not taking a necro spell and giving it to clerics, we aren't going to do this.  Also no toggleable lights.[/quote:2x8sv1eu]

Ok, give it to Warriors and Thieves then.  :twisted:

</div>

<div class="post" data-post-id="12648" data-author="Weasel" data-date="2006-05-23T03:27:21+00:00" data-subject="">

..or how about 'extinguish light', but to relight it we have to buy matches or a burning coal or something like that to recharge it..

I'm just clutching at straws here, aren't I.  :(

</div>

<div class="post" data-post-id="12649" data-author="Weasel" data-date="2006-05-23T03:28:31+00:00" data-subject="">

And I know some immorts liked my boomerang idea ages ago. Anyone ever given it another thought?

</div>

<div class="post" data-post-id="12653" data-author="Rajil" data-date="2006-05-23T14:59:59+00:00" data-subject="">

Silly non necros.... tsk tsk tsk

</div>

<div class="post" data-post-id="12657" data-author="Malison" data-date="2006-05-23T21:42:20+00:00" data-subject="">

in the interest of the game's pseudo-reality...

it seems most lights glow because they're magical, whereas the torch you begin the game with or lanterns glow because they're burning.  it would be kind of ridiculous to try to turn off the magical glow except by magic <'darkness'>

and you don't really see many people running around holding torches

</div>

<div class="post" data-post-id="12659" data-author="Vixn" data-date="2006-05-24T04:12:02+00:00" data-subject="">

Ok, a little examination of the code shows me that there is already a spell for this, the necro spell darkness.  So in the interest of not taking a necro spell and giving it to clerics, we aren't going to do this.  Also no toggleable lights.[/quote:3giv9rfi]

following this logic necro and cleric shouldn't be combined in one classo cause spells mix. And I don't believe Master Healer will learn someone who join The Dark Side. mabbe lite and heal won't affect evil person?

</div>

<div class="post" data-post-id="12660" data-author="12345" data-date="2006-05-24T04:31:33+00:00" data-subject="">

Ok, Weasel knew that asking this was setting himself up for disappointment, so this can die I think.  If we follow the current logic, we'll give the dark cloak the darkness affect, and the familiar spell the ability to assume the form of the critter familiared and damn will strike as a firestorm on masterfuls...

So if we can stop while we can still tell one class from another, that'd be nice.

</div>

<div class="post" data-post-id="12664" data-author="kjartan" data-date="2006-05-24T16:23:35+00:00" data-subject="">

Ok, a little examination of the code shows me that there is already a spell for this, the necro spell darkness.  So in the interest of not taking a necro spell and giving it to clerics, we aren't going to do this.  Also no toggleable lights.[/quote:1ggb4ddf]

following this logic necro and cleric shouldn't be combined in one classo cause spells mix. And I don't believe Master Healer will learn someone who join The Dark Side. mabbe lite and heal won't affect evil person?[/quote:1ggb4ddf]

My objection wasn't that a cleric can't cast a necro spell because it's evil - there are already abilities specifically targeted at evil clerics, like the evil supplication mobs - it was like 12345 said: in general we shouldn't give abilities of one class to another class.  One of the nice things about Sloth is that you can have very different characters by picking different classos, and so I don't want to make the classes more similar.

</div>

<div class="post" data-post-id="12666" data-author="Qa" data-date="2006-05-24T20:27:25+00:00" data-subject="">

Ok, KJ, try this:

How about a version of the pearl/dark symbol that is avatar resticted and toggleable?  The pearl/dark symbol is essentially newbie EQ that most of us wear until 5x40 anyway.

I guess I would also ask that 5x40 light also be made toggleable then as well.

Qa

</div>

<div class="post" data-post-id="12667" data-author="kjartan" data-date="2006-05-24T20:50:47+00:00" data-subject="">

Yeah, we could do something like that.

Or, if I (or one of you) could think of a good way of explaining it, a thief skill that lets you hide your light.  Also I would need a good name for the skill.  It seems like the sort of thing a thief would be good at.  It would need to be functionally distinct from the darkness spell, though - I don't want it to be darkness-spell-but-it's-a-skill.  I don't know what else darkness is used for, if anything, other than hiding lights while still wearing the item: if it's not used for anything else, then never mind about the thief skill.  (Could still do the item).

</div>

<div class="post" data-post-id="12668" data-author="Alberich" data-date="2006-05-24T21:00:52+00:00" data-subject="">

av th restricted clasp would even work - common enough to put some sort of shade over a lamp to either direct or lessen the illumination (yes, this means you'd be removing your light from time to time, pthieves, wah wah) but really... a skill wouldn't be plausible... and my thief already has his hands full... what with stabber, poisons, the light, etc etc...

</div>

<div class="post" data-post-id="12670" data-author="Weasel" data-date="2006-05-24T21:58:42+00:00" data-subject="">

Could it be an enhanced property of an existing skill like sneak, for example greater sneak? Although ya wouldn't want it to replace normal sneak because ya obviously wouldn't want to be in the dark every time ya wanted to sneak somewhere..

Making a clasp.. dunno if that's such a good idea, at least not in the held high slot - the only reason I say that is because there are so many clasps available already for that same slot - adding another may just render it unusable... unless you can allow multiple clasps on one item, and I don't think that's gonna happen..

</div>

<div class="post" data-post-id="12672" data-author="12345" data-date="2006-05-24T22:34:08+00:00" data-subject="">

This reminds me of the D&D flashlight.  Cast continual light into a container with a lid and you can flip it open and shut to turn it on and off and carry it around.  Easy solution for a complex problem.

Even your basic old school lantern came with shudders for dimming the light without having to relight it every time you want to use it.  Flip the shudders up, you can see, flip them down, you can't.  I can still hold the lantern and get bonuses, I just can't see anything unless I have darksight or infravision.

If you wanted to be realistic about it, you could easily have a switch for lights.  Some, like torches, are either on or off, they can't be dimmed.  Some, like lanterns, can simply be dimmed or not dimmed as a natural function of the lamp.  Even magical lights can fall into this category depending on how magical and/or functionally built they are.  For instance, a pearl of the rising tide might glow of its own accord, but a symbol of the dark lord will dim according to the wishes of its possessor.  So you would have to lose the +con and +3 mregen to dim a pearl, but the symbol, just dim and maintain the bonuses.

This doesn't seem like it needs a skill at all.  Any idiot can flip a dimmer switch, provided its there in the first place.  Wether they can see or not while its dimmed is another issue entirely.

</div>
