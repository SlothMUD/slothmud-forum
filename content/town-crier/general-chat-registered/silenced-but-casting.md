---
title: "Silenced but casting?"
topic_id: 5020
author: "Insomnia"
date: 2021-06-09T13:09:36+00:00
last_activity: 2021-06-15T17:19:32+00:00
last_author: "Insomnia"
sticky: false
locked: false
post_count: 3
---

<div class="post" data-post-id="39730" data-author="Insomnia" data-date="2021-06-09T13:09:36+00:00" data-subject="Silenced but casting?">

Not the first time I'm seeing this:

Room 52150: The Door to Bane

 Dark shapes scowl from the walls. Darker shadows play. No sounds

fill the silence, except for the monotonous dripping of water coming from

a place unknown. The low, charred ceiling gives the impression of a slow

descent, though it stays perfectly motionless. A single speck of light,

as if a spark from a fire, wavers aloft just before a thick oaken door.

It casts shadows on the door's surface that spell the word: B A N E.

Exits: [North] South West 

The corpse of the Dead Man is lying here.

(Faint Red Aura) Stakur Jaki, the cleric, stares into otherworldly dimensions.

Stakur Jaki is covered in sticky webs!

Stakur Jaki is protected by an aerial servant.

\<998/1098hp 1279/885ma 443/444mv -%\>

cast 'silence' stakur

Ok.

Stakur Jaki's mouth clams shut!

\<998/1098hp 1264/885ma 443/444mv -%\>

Stakur Jaki utters the words, 'gszrr gpuzre'

A faded green sphere forms around Stakur Jaki.

Is it a bug?

</div>

<div class="post" data-post-id="39732" data-author="Driven" data-date="2021-06-12T18:31:27+00:00" data-subject="Re: Silenced but casting?">

A lot of mobs made by Rita use MUDL to cast spells (instead of using the built-in mage/cleric procs), so the bug is probably that his MUDL doesn't check for silence. I would also bet that hermetic resonance also doesn't work against the spells that those mobs cast. It's a case of the builder trying to be too tricky and just end up creating weird corner cases that shouldn't exist. I can look at the code to determine whether there is a missing check that will fix all of these in one fell swoop.

</div>

<div class="post" data-post-id="39734" data-author="Insomnia" data-date="2021-06-15T17:19:32+00:00" data-subject="Re: Silenced but casting?">

If you'll be fixing something in spells, and procs, and related checks – is it also possible to fix a bug with magic immunity that doesn't work against reflected spells?

id heliotrope

Ok.

You feel informed:

Object 'potion heliotrope', Item type: POTION

Item is: \*\*INVENTORY\*\* 

Weight: 0, Value: 0gold, Worn in: TAKE 

Apply a bonus of 1 to the drinker's IMMUNE\_MAGIC for 15 hours.

\<1083/1093hp 814/869ma 380/443mv -%\>

quaff heliotrope

You quaff a heliotrope potion which dissolves.

\<1088/1093hp 819/869ma 384/443mv -%\>

sco

[ ... ]

 Greater Mobility Alchemical effect, +1 to IMMUNE\_MAGIC

e

cast 'acid shower'

Room 74005: Spiral Steps in the Mud

 Steps cut from large slabs of shiny obsidian have been embedded into the

dark red, muddy hillside. The lake shore meets the water to the south, and

wading is possible. Above and to the north are patches of bright flowers

that line the edge of the southwest greenhouse walls, but it is too steep

to climb directly to them.

Exits: South West 

(Brilliant Red Aura) A short, but menacing drow wizard in dark robes surveys the area.

A drow warlock is surrounded by a glowing green sphere!

A drow warlock is encased in a silvery sphere!

(Brilliant Red Aura) A short, but menacing drow wizard in dark robes surveys the area.

A drow warlock is surrounded by a radiant green sphere!

A drow warlock is encased in a silvery sphere!

\<1093/1093hp 827/869ma 395/443mv -%\>

Ok.

A drow warlock's spell shield absorbs the damage!

The silvery shield around a drow warlock becomes opaque and reflects the spell!

You miss a drow warlock with your acid blast.

You are bathed in a painful stream of burning green acid!

That Really did HURT!

A drow warlock's spell shield absorbs the damage!

The silvery shield around a drow warlock becomes opaque and reflects the spell!

You miss a drow warlock with your acid blast.

You are bathed in a painful stream of burning green acid!

\<651/1093hp 768/869ma 393/443mv 90%\>

retr w

Room 74006: Spiral Steps in the Mud

 The obsidian steps spiral up to the northern entrance of the palace. To

the west, several hundred yards away across the water, is the the market

square of the village. Occasionally there are brief flashes of light from

a portal north of the square, but the portal itself is obscured by several

small buildings.

Exits: North East 

You make a hasty retreat.

\<658/1093hp 774/869ma 396/443mv -%\>

cast 'restor' self

Ok.

Your spell fails.

You absorb the magic.

</div>
