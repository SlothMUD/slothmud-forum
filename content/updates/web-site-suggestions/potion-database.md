---
title: "Potion Database"
topic_id: 5013
author: "*Idjit*"
date: 2021-03-25T02:16:10+00:00
last_activity: 2021-05-07T02:44:00+00:00
last_author: "Gorka"
sticky: false
locked: false
post_count: 9
---

<div class="post" data-post-id="39702" data-author="*Idjit*" data-date="2021-03-25T02:16:10+00:00" data-subject="Potion Database">

It feels like, canned magic (potions and wands/staves/rods) is the last bastion of lack of transparency.

EQlist doesn't sort potions by what spells they are or duration.

I am not the least bit talented enough to build such a database but if we had one, what would we want from it, what fields? I would think gold value, weight, duration, plusses, spell affect, non-spell affect, level of spell

This is just to stoke discussion.

would we pull from a JSON but pull different fields than the ones the EQlist is interested in, or would we manually craft with player submissions? What are the nuts and bolts.

\--Idj

</div>

<div class="post" data-post-id="39703" data-author="*Idjit*" data-date="2021-03-25T02:21:08+00:00" data-subject="Re: Potion Database">

This can go two routes. One where it's a true sister project to the EQlist where it imports real mud data or:

Players hand-building a list.

I feel like, half a dozen really good players that know all the really useful potions anyway, could push out a searchable list that is just a text dump, of like 300-500 potions, in just a few days, even if it was never further updated.

By whomever constitutes a safe pair of hands.

Instead of building a dynamic database asset (which could malfunction)

\--D

</div>

<div class="post" data-post-id="39704" data-author="cnl" data-date="2021-03-25T22:21:43+00:00" data-subject="Re: Potion Database">

Ideally, it would be nice if all things were discoverable in the game.

```
You feel informed:
Object 'potion accuracy crystal flask', Item type: POTION
Item is: MAGIC 
Weight: 1, Value: 20000gold, Worn in: TAKE 
Apply broken magic to the drinker...
The item has 1 additional magical ability.
```

If the identify spell cannot be fixed then maybe we could say "Apply unknown magic to the drinker..." instead of "broken".

I have a little item annotation script that allows me to add notes to items as I identify them in-game and I like the discovery aspect of it, and also finding new potions on the shop or in the wild without annotations because then I notice them.

That aside, the EQ site currently lists scroll spells, so I'm hopeful that for potions that do have simpler spells attached it's just a parsing issue that the EQ site maintainer hopefully is able to fix. This would be the ideal solution to keep this information in a single place which already has all the pieces to track which mob pops an item and automatically updates.

If there are to be player notes on items I would hope we can find a way to integrate them into the single EQ site - but that's really a big ask.

</div>

<div class="post" data-post-id="39705" data-author="*Breeze*" data-date="2021-03-27T17:52:13+00:00" data-subject="Re: Potion Database">

in theory anything can be fixed...

traditionally, the eqlist is a player driven effort.

when i was a player, i skirted the borders and created the previous eqlist based on what data i had.

when i became an immortal, i updated it best i could with the stuff i had access to, and as soon as someone came by that i thought could handle it, i passed way more control over the raw data that i had.

there is literally a flag for objects that stops items from being in game

that is something i am not willing to overturn

// Q

</div>

<div class="post" data-post-id="39714" data-author="*Idjit*" data-date="2021-05-03T03:46:44+00:00" data-subject="Re: Potion Database">

Fuligin had this to say:

A beaker of bubbling orange liquid	Level 30:stone skin, (none), (none)	

A beaker of iridescent liquid	Level 30:sanctuary, (none), (none)	

A beaker of milky blue liquid	Level 40:dispel magic, (none), (none)	

A beaker of thick orange syrup	Level 30:haste, (none), (none)	

A black heart jewel	Level 40:darkness, dark cloak, tenebrous claw	

A black potion with a red glowing center	Level 40:dispel magic, (none), (none)	

A blue-green potion	Level 25:cure serious, (none), (none)	

A bright blue potion	Level 40:greater heal, (none), (none)	

A bright-orange potion	+6 DAMROLL (10 hr)	

A brilliant white potion	Level 17:sanctuary, (none), (none)	

A bubbling maroon potion	Level 15:armor, (none), (none)	

A cerise potion	Level 15:armor, cure light, (none)	

A chartreuse potion	Level 40:remove disease, (none), (none)	

A chilled black potion	Level 15:telepathy, (none), (none)	

A chunky yellow and brown potion	Level 45:fortune, (none), (none)	

A clear potion	Imbue:vision 7x (Lev 25)	

A cloudy purple potion	Level 30:remove curse, (none), (none)	

A cloudy red potion	Level 35:stone skin, (none), (none)	

A coconut of analgesic draught	Level 30:natures revival, (none), (none)	

A coconut of emetic draught	Level 30:dispel magic, (none), (none)	

A coconut of restorative draught	Level 30:cure critic, (none), (none)	

A coconut of soothing draught	Level 30:fluidity, (none), (none)	

A cold blue potion	+40 MANA (1 hr)	

A cracked stone jar	Level 40:stone skin, (none), (none)	

A creamy pink potion	Level 25:mindbar, (none), (none)	

A crimson potion	Level 40:aegis, (none), (none)	

A dark yellow potion	Imbue:magic missile 5x (Lev 15)	

A deep purple potion	Level 35:mobility, (none), (none)	

A dull copper potion	+5 HITROLL (10 hr)	

A dull gold potion	Level 12:cure light, (none), (none)	

A dull gray potion	Imbue:lloyds beacon 2x (Lev 35)	

A fang of venom	Level 15:poison, (none), (none)	

A flask full of mist	Imbue:wraithform 3x (Lev 40)	

A flask of comradery 

A flask of human blood	Level 40:regeneration, infravision, (none)	

A flask of transparent liquid	Level 40:fluidity, (none), (none)	

A frosty blue potion	Level 40:greater heal, greater heal, greater heal	

A frothy violet potion	Level 40:corona, (none), (none)	

A glimmering green potion	Level 40:restoration, restoration, rejuvenation	

A goblet of the sacred order 

A goo-encrusted stone jar	Level 40:resist cold, (none), (none)	

A grainy black potion	Level 35:teleport, (none), (none)	

A green glass jar of bubbly fluid	Level 20:bone armor, (none), (none)	

A green glass jar of cloudy liquid	Level 20:cure critic, (none), (none)	

A green glass jar of glowing liquid	Level 20:bless, (none), (none)	

A green glass jar of milky liquid	Level 20:regeneration, (none), (none)	

A green glass jar of oil	Level 20:resist fire, (none), (none)	

A green glass jar of roiling fluid	Level 20:resist cold, (none), (none)	

A green glass jar of viscous goo	Level 20:armor, (none), (none)	

A green potion	Level 20:blindness, teleport, cure blind	

A hissing blue potion	+20 MANA (1 hr)	

A jar of molasses	Level 5:silence, (none), (none)	

A metallic red potion	Level 40:iron skin, (none), (none)	

A midnight-blue potion	Level 15:cure normal, (none), (none)	

A milky lavender potion	Level 35:perception, (none), (none)	

A milky white potion	Level 14:word of recall, (none), (none)	

A moldy orange potion	+3 DAMROLL (10 hr)	

A pale purple potion	Level 25:water breathing, (none), (none)	

A pale rose potion	Level 15:resist fire, resist cold, (none)	

A pale violet potion	Level 15:infravision, (none), (none)	

A potion filled with evil intentions 

A potion filled with good intentions 

A potion of accuracy 

A potion of cleansing	Level 12:remove poison, (none), (none)	

A potion of cure critical	Level 20:cure critic, (none), (none)	

A potion of endurance	+2 MAX\_CON (45 hr)	

A potion of greater healing	Level 40:greater heal, (none), (none)	

A potion of greater refresh	Level 40:refresh, refresh, refresh	

A potion of greater refreshment	Level 40:greater refresh, greater refresh, rejuvenation	

A potion of greater restoration	Level 40:restoration, restoration, restoration	

A potion of greater strength	Level 40:strength, (none), (none)	

A potion of healing	Level 40:heal, (none), (none)	

A potion of insight	Level 12:detect invisibility, (none), (none)	

A potion of invulnerability	Level 0:(none), (none), spell shield	

A potion of knitting	Level 12:cure light, (none), (none)	

A potion of lesser refresh	Level 40:refresh, (none), (none)	

A potion of lesser restoration	Level 40:restoration, (none), (none)	

A potion of lesser sanctuary	Level 17:sanctuary, (none), (none)	

A potion of pure darkness	Level 40:aegis, protection from evil, dark cloak	

A potion of remove poison	Level 12:remove poison, (none), (none)	

A potion of stones	Level 43:dispel fly, (none), (none)	

A potion of the frozen heart	Level 45:petrified armor, chill touch, (none)	

A potion of transmutation	Level 46:relocation, (none), (none)	

A potion of turn undead	Level 40:turn undead, cure normal, cure normal	

A potion of wispy prayers	+2 MAX\_INT (45 hr)	

A pungent indigo potion	Level 25:fly, (none), (none)	

A purple potion	Level 12:remove poison, (none), (none)	

A radiant blue potion	+300 MANA (0 hr)	

A radiant white potion	Imbue:raise dead 1x (Lev 40)	

A red herbal infusion	Level 40:wraithform, (none), (none)	

A red potion	Level 12:armor, (none), (none)	

A roiling blue potion	Level 25:regeneration, (none), (none)	

A ruby-red potion	Level 35:sanctuary, (none), (none)	

A russet potion	+0 IMMUNE\_MAGIC (5 hr)	

A sea-green potion	Level 35:remove disease, remove poison, (none)	

A shiny golden potion	+20 HITROLL (10 hr)	

A silky white potion	Level 45:reign of the spider, curse, (none)	

A silver potion	Level 17:call lightning, cure critic, (none)	

A sizzling yellow potion	Imbue:lightning bolt 8x (Lev 40)	

A slate-grey potion	Level 25:word of recall, (none), (none)	

A sloshing blue potion	+150 MANA (1 hr)	

A smelly herbal infusion	Level 40:resist fire, (none), (none)	

A smoky green potion	Level 40:remove poison, (none), (none)	

A sparking yellow potion	Imbue:call lightning 3x (Lev 25)	

A sparkling blue potion	+150 MANA (0 hr)	

A sparkling green potion	Level 10:detect evil, detect invisibility, detect magic	

A steaming black potion	Imbue:demon bind 4x (Lev 35)	

A stone jar of orange paste	Level 40:haste, (none), (none)	

A thick green potion	Level 40:greater heal, greater heal, rejuvenation	

A translucent purple potion	Level 25:detect invisibility, (none), (none)	

A vaporous white potion	Level 20:cure critic, cure critic, cure critic	

A vial of alcohol	Level 41:blindness, (none), (none)	

A vial of blood	Disease: hack, hack	

A vial of citric acid	Level 0:(none), (none), (none)	

A vial of firedrake spittle	Level 14:(none), (none), (none)	

A vial of quickling sweat	Level 0:(none), (none), (none)	

A vial of slime	Level 41:poison, poison, (none)	

A vial of squids ink	Level 41:(none), (none), (none)	

A vial of troll blood	Disease: hack, hack	

A vial of vitreous humor	+25 RESIST\_POISON (5 hr)	

A viscous blue potion	Level 40:heal, heal, (none)	

A viscous purple potion	Level 25:demon bind, (none), (none)	

A warm coral potion	Level 40:resist webs, (none), (none)	

A wineskin dripping green liquid	Level 40:heal, (none), (none)	

A wineskin leaking milky blue fluid	Level 40:dispel magic, (none), (none)	

A wineskin leaking viscous black liquid	Level 40:armor, (none), (none)	

A yellow potion	Level 12:detect invisibility, (none), (none)	

An acrid orange potion	Imbue:flame strike 3x (Lev 25)	

An amethyst potion	Level 35:infravision, detect invisibility, sense life	

An effervescent golden potion	+10 DAMROLL (7 hr)	

An effervescent potion	Level 16:detect evil, detect invisibility, detect magic	

An olive potion	Level 10:dispel evil, curse, heal	

An orange potion	Level 24:detect magic, (none), (none)	

Potion of the essence of a mindflayer	+2 MAX\_WIS (45 hr)	

Potion of the strength of the gods	+1 MAX\_STR (45 hr)	

Some yellow dust	Level 15:curse, (none), (none)

</div>

<div class="post" data-post-id="39715" data-author="cnl" data-date="2021-05-03T05:18:52+00:00" data-subject="Re: Potion Database">

```
| Name | Effect |
|-----------------------------------------|------------------------------------------|
| A beaker of bubbling orange liquid | L30:stone skin |
| A beaker of iridescent liquid | L30:sanctuary |
| A beaker of milky blue liquid | L40:dispel magic |
| A beaker of thick orange syrup | L30:haste |
| A black heart jewel | L40:darkness, dark cloak, tenebrous claw |
| A black potion with a red glowing center| L40:dispel magic |
| A blue-green potion | L25:cure serious |
| A bright blue potion | L40:greater heal |
| A bright-orange potion | +6 DAMROLL (10 hr) |
| A brilliant white potion | L17:sanctuary |
| A bubbling maroon potion | L15:armor |
| A cerise potion | L15:armor, cure light |
| A chartreuse potion | L40:remove disease |
| A chilled black potion | L15:telepathy |
| A chunky yellow and brown potion | L45:fortune *TEMP* |
| A clear potion | Imbue:vision 7x (L25) |
| A cloudy purple potion | L30:remove curse |
| A cloudy red potion | L35:stone skin |
| A coconut of analgesic draught | L30:natures revival |
| A coconut of emetic draught | L30:dispel magic |
| A coconut of restorative draught | L30:cure critic |
| A coconut of soothing draught | L30:fluidity |
| A cold blue potion | +40 MANA (1 hr) |
| A cracked stone jar | L40:stone skin |
| A creamy pink potion | L25:mindbar |
| A crimson potion | L40:aegis |
| A dark yellow potion | Imbue:magic missile 5x (L15) |
| A deep purple potion | L35:mobility |
| A dull copper potion | +5 HITROLL (10 hr) |
| A dull gold potion | L12:cure light |
| A dull gray potion | Imbue:lloyds beacon 2x (L35) |
| A fang of venom | L15:poison |
| A flask full of mist | Imbue:wraithform 3x (L40) |
| A flask of comradery | GROUP bless:4hitroll, -2saving_spell 120h|
| A flask of human blood | L40:regeneration, infravision |
| A flask of transparent liquid | L40:fluidity |
| A frosty blue potion | L40:greater heal x3 |
| A frothy violet potion | L40:corona |
| A glimmering green potion | L40:restoration x2, rejuvenation |
| A goblet of the sacred order | ? bless, ac ? |
| A goo-encrusted stone jar | L40:resist cold |
| A grainy black potion | L35:teleport |
| A green glass jar of bubbly fluid | L20:bone armor |
| A green glass jar of cloudy liquid | L20:cure critic |
| A green glass jar of glowing liquid | L20:bless |
| A green glass jar of milky liquid | L20:regeneration |
| A green glass jar of oil | L20:resist fire |
| A green glass jar of roiling fluid | L20:resist cold |
| A green glass jar of viscous goo | L20:armor |
| A green potion | L20:blindness, teleport, cure blind |
| A hissing blue potion | +20 MANA (1 hr) |
| A jar of molasses | L5:silence |
| A metallic red potion | L40:iron skin |
| A midnight-blue potion | L15:cure normal |
| A milky lavender potion | L35:perception |
| A milky white potion | L14:word of recall |
| A moldy orange potion | +3 DAMROLL (10 hr) |
| A pale purple potion | L25:water breathing |
| A pale rose potion | L15:resist fire, resist cold |
| A pale violet potion | L15:infravision |
| A potion filled with evil intentions | Set alignment -1000 |
| A potion filled with good intentions | Set alignment 1000 |
| A potion of accuracy | bless:-1ac, -2saving_spell 120h |
| A potion of cleansing | L12:remove poison |
| A potion of cure critical | L20:cure critic *TEMP* |
| A potion of endurance | +2 MAX_CON (45 hr) |
| A potion of greater healing | L40:greater heal *TEMP* |
| A potion of greater refresh | L40:refresh x2, refresh *TEMP* |
| A potion of greater refreshment | L40:greater refresh x2, rejuvenation |
| A potion of greater restoration | L40:restoration x2, restoration *TEMP* |
| A potion of greater strength | L40:strength *TEMP* |
| A potion of healing | L40:heal *TEMP* |
| A potion of insight | L12:det invis |
| A potion of invulnerability | L0:spell shield |
| A potion of knitting | L12:cure light |
| A potion of lesser refresh | L40:refresh *TEMP* |
| A potion of lesser restoration | L40:restoration *TEMP* |
| A potion of lesser sanctuary | L17:sanctuary *TEMP* |
| A potion of pure darkness | L40:aegis, prot from evil, dark cloak |
| A potion of remove poison | L12:remove poison *TEMP* |
| A potion of stones | L43:dispel fly |
| A potion of the frozen heart | L45:petrified armor, chill touch *TEMP* |
| A potion of transmutation | L46:relocation |
| A potion of turn undead | L40:turn undead, cure normal x2 |
| A potion of wispy prayers | +2 MAX_INT (45 hr) |
| A pungent indigo potion | L25:fly |
| A purple potion | L12:remove poison |
| A radiant blue potion | +300 MANA (0 hr) |
| A radiant white potion | Imbue:raise dead 1x (L40) |
| A red herbal infusion | L40:wraithform |
| A red potion | L12:armor |
| A roiling blue potion | L25:regeneration |
| A ruby-red potion | L35:sanctuary |
| A russet potion | +0 IMMUNE_MAGIC (5 hr) |
| A sea-green potion | L35:remove disease, remove poison |
| A shiny golden potion | +20 HITROLL (10 hr) |
| A silky white potion | L45:reign of the spider, curse *TEMP* |
| A silver potion | L17:call lightning, cure critic |
| A sizzling yellow potion | Imbue:lightning bolt 8x (L40) |
| A slate-grey potion | L25:word of recall |
| A sloshing blue potion | +150 MANA (1 hr) |
| A smelly herbal infusion | L40:resist fire |
| A smoky green potion | L40:remove poison |
| A sparking yellow potion | Imbue:call lightning 3x (L25) |
| A sparkling blue potion | +150 MANA (0 hr) |
| A sparkling green potion | L10:det evil, det invis, det magic |
| A steaming black potion | Imbue:demon bind 4x (L35) |
| A stone jar of orange paste | L40:haste |
| A thick green potion | L40:greater heal x2, rejuvenation |
| A translucent purple potion | L25:det invis |
| A vaporous white potion | L20:cure critic x3 |
| A vial of alcohol | L41:blindness |
| A vial of blood | Disease: hack x2 |
| A vial of citric acid | L0:(none) |
| A vial of firedrake spittle | L14:(none) |
| A vial of quickling sweat | L0:(none) |
| A vial of slime | L41:poison x2 |
| A vial of squids ink | L41:(none) |
| A vial of troll blood | Disease: hack x2 |
| A vial of vitreous humor | +25 RESIST_POISON (5 hr) *TEMP* |
| A viscous blue potion | L40:heal x2 |
| A viscous purple potion | L25:demon bind |
| A warm coral potion | L40:resist webs |
| A wineskin dripping green liquid | L40:heal |
| A wineskin leaking milky blue fluid | L40:dispel magic |
| A wineskin leaking viscous black liquid | L40:armor |
| A yellow potion | L12:det invis |
| An acrid orange potion | Imbue:flame strike 3x (L25) |
| An amethyst potion | L35:infravision, det invis, sense life |
| An effervescent golden potion | +10 DAMROLL (7 hr) |
| An effervescent potion | L16:det evil, det invis, det magic |
| An olive potion | L10:dispel evil, curse, heal |
| An orange potion | L24:det magic |
| Potion of the essence of a mindflayer | +2 MAX_WIS (45 hr) |
| Potion of the strength of the gods | +1 MAX_STR (45 hr) |
| Some yellow dust | L15:curse |
```

</div>

<div class="post" data-post-id="39716" data-author="Gorka" data-date="2021-05-06T13:26:14+00:00" data-subject="Re: Potion Database">

A potion of transmutation Level 46:relocation, (none), (none)

It's weird outlier things like this that often create exploits. There is a fairly good chance I could use this to do something I can't by regular means, if I cared enough to really put my mind to it, even if the advantage wasn't much. I tend to recall this item is tied up in a quest. An Imm should have a look at this in any case, It also raises the question, are immortals who are not lvl 46 able to create lvl 46 items? But with that said, there are far worser exploits in the game at the moment by 100 times, than lvl 46 relocation.

</div>

<div class="post" data-post-id="39717" data-author="cnl" data-date="2021-05-06T16:46:47+00:00" data-subject="Re: Potion Database">

```
You feel informed:
Object 'potion transmutation *Fuligin*', Item type: POTION
Item is: PERSONAL RESTRUNG 
Weight: 2, Value: 50000gold, Worn in: TAKE 
Level 46 spells of:
relocation
(none)
(none)
The item has 1 additional magical ability.
Only those who are at least experienced magic users, clerics, thieves,
warriors, druids, necromancers, bards, or monks may use this item.
```

The dump of my potion id data probably should have excluded personal items and flagged items with additional magical properties.

This one is tied up in an auto-quest - if memory serves me it relocates you to a fixed special location, it is not an imbue.

</div>

<div class="post" data-post-id="39718" data-author="Gorka" data-date="2021-05-07T02:44:00+00:00" data-subject="Re: Potion Database">

> <strong>cnl wrote:</strong>
> if memory serves me it relocates you to a fixed special location, it is not an imbue.

There are times and situations in the game where being relocated to a fixed special location, actually provides an exploit to regular game mechanics. It can also cause some rooms that use MUDL to glitch. Doing so at Lvl 46 could potentially provide an even bigger exploit. In this specific case it would depend on what continent the special room is located, if it's possible to recall from, and where it returns you to. Would have to check my logs, but in any case, it's a classic exploit possibility in a seemingly over privileged item. Like I said, I've never tested, but it's where one would start looking for sure.

</div>
