---
title: "Potion Substitutes - NET"
topic_id: 1760
author: "*juggleblood*"
date: 2006-03-03T11:56:21+00:00
last_activity: 2006-03-03T11:56:21+00:00
last_author: "*juggleblood*"
sticky: false
locked: false
post_count: 1
---

<div class="post" data-post-id="11025" data-author="*juggleblood*" data-date="2006-03-03T11:56:21+00:00" data-subject="Potion Substitutes - NET">

This script substitutes the potion name for the effects, plus a few key words.

The downside is that it eliminates the number of items following the potion

i.e. "A yellow potion [4]" becomes "Detect Invis - Yellow"

I tried to make a script that would display the number too, but then the problem was it didn't work when there was only one.

If you want to, you can add an additional sub to each of these items like so:

\#sub {yellow potion%0}{Detect Invis - Yellow$0}{G\|pot subs}

Here's the script:

\#al potsubson {#enable pot}

\#al potsubsoff {#disable pot}

\#sub {acrid orange potion}{Imbuewith 3x Flamestrike- acrid orange}{G\|pot subs}

\#sub {amethyst potion}{Infravision / Detect Invis / Sense Life- amethyst}{G\|pot subs}

\#sub {aquamarine potion}{Cure Minor- aquamarine}{G\|pot subs}

\#sub {basin of balms	2x}{Cure Critical- basin of balms}{G\|pot subs}

\#sub {beaker of glowing green liquid}{Level 30 Heal- glowing green}{G\|pot subs}

\#sub {beaker of milky blue liquid}{Lvl 40 Dispel Magic- milky blue}{G\|pot subs}

\#sub {black chalice}{Bless/Heal/Sanctuary- black chalice}{G\|pot subs}

\#sub {black heart jewel}{lvl 48 Strength- black heart jewel}{G\|pot subs}

\#sub {black potion with a red glowing center}{Dispel Magic- black with a red glowing}{G\|pot subs}

\#sub {blood red potion}{Level 30 Refresh- blood red}{G\|pot subs}

\#sub {blue-green potion}{Level 25 Cure Serious- blue-green}{G\|pot subs}

\#sub {bright blue potion}{Lvl 40 Greater Heal- bright blue}{G\|pot subs}

\#sub {bright orange potion}{+6 to Dam for 10 Hrs.- bright orange}{G\|pot subs}

\#sub {brown misty potion}{Regeneration (Level 40)- brown misty}{G\|pot subs}

\#sub {bubbling green potion}{Cure critic/Invis/Phase Door- bubbling green}{G\|pot subs}

\#sub {bubbling maroon potion}{armor- bubbling maroon}{G\|pot subs}

\#sub {bubbling violet potion}{ Lvl 40 Knock- bubbling violet}{G\|pot subs}

\#sub {cerise potion}{Armor/Cure Light- cerise}{G\|pot subs}

\#sub {chartreuse potion}{L40 Remove Disease- chartreuse} {G\|pot subs}

\#sub {chilled black potion}{Telepathy- chilled black}{G\|pot subs}

\#sub {chocolate potion}{Invisibility, Remove Poison, Remove Curse- chocolate} {G\|pot subs}

\#sub {clear blue potion}{Fly, Water Breathing, Refresh- clear blue}{G\|pot subs}

\#sub {clear potion with a lot of dirt sediment	}{Stone Skin-clear with dirt}{G\|pot subs}

\#sub {clear white potion}{Dispel/Stone Skin/Sanc- clear white}{G\|pot subs}

\#sub {cloudy purple potion}{	Level 15 Str- cloudy purple}{G\|pot subs}

\#sub {cloudy red potion}{Level 35 Stone Skin- cloudy red}{G\|pot subs}

\#sub {coconut of abrasive draught}{	lvl 30 Shield of Thorns- abrasive draught}{G\|pot subs}

\#sub {coconut of analgesic drought}{Lvl 30 Natures Revival- analgesic drought}{G\|pot subs}

\#sub {coconut of emetic draught}{Level 30 Dispel Magic- emetic draught}{G\|pot subs}

\#sub {coconut of invigorating draught}{L30 Elemental Resistance- invigorating draught}{G\|pot subs}

\#sub {coconut of soothing draught}{	Lvl 30 Fluidity- soothing draught}{G\|pot subs}

\#sub {cold blue potion}{+40 Mana for 1 hr- cold blue}{G\|pot subs}

\#sub {creamy pink potion}{lvl 25 Mindbar x1- creamy pink}{G\|pot subs}

\#sub {dark yellow potion}{5x magic missile (lvl15)- dark yellow}{G\|pot subs}

\#sub {deep blue potion}{Regeneration/Refresh/Cure Serious- deep blue}{G\|pot subs}

\#sub {deep purple potion}{Str (level 35)- deep purple}{G\|pot subs}

\#sub {dogs head}{Curse, Web- dogs head}{G\|pot subs}

\#sub {drop of skunk spray}{Curse- skunk spray}{G\|pot subs}

\#sub {dull copper potion}{+5 to hit, 10 Hours- dull copper} {G\|pot subs}

\#sub {dull gold potion}{cure light wounds- dull gold}{G\|pot subs}

\#sub {dull grey potion}{Lloyds Beacon x2 at Level 35- dull grey}{G\|pot subs}

\#sub {effervescent potion}{Det. Evil/Det. Invisible/Det. Magic- effervescent}{G\|pot subs}

\#sub {elixir of vitality}{Cure Plague- elixir of vitality}{G\|pot subs}

\#sub {flask full of mist}{Wraithform- flask full of mist}{G\|pot subs}

\#sub {flask of holy water}{Dispellable Godsanc- flask of holy water}{G\|pot subs}

\#sub {flask of human blood}{Regeneration, Infravision- human blood}{G\|pot subs} 

\#sub {flask of perfume}{Remove Curse- perfume}{G\|pot subs}

\#sub {flask of transparent liquid}{Fluidity- transparent liquid}{G\|pot subs}

\#sub {flecked gold potion}{ Bless, Strength, Stone Skin- flecked gold}{G\|pot subs}

\#sub {frothy violet potion}{lvl 40 Corona x1- frothy violet}{G\|pot subs}

\#sub {glimmering green potion}{Greater Heal x3- glimmering green}{G\|pot subs}

\#sub {glowing golden potion}{Lvl 45 Talshans Tribute- glowing golden}{G\|pot subs}

\#sub {grainy black potion}{Level 35 Teleport- grainy black}{G\|pot subs}

\#sub {greasy vial}{Resist Webs- greasy vial}{G\|pot subs}

\#sub {green glass jar of bubbly fluids}{lvl 20 Bone Armor- jar of bubbly}{G\|pot subs}

\#sub {green glass jar of cloudy liquid}{lvl 20 Cure Critical- jar of cloudy}{G\|pot subs}

\#sub {green glass jar of glowing liquid}{lvl 20 Bless- jar of glowing}{G\|pot subs}

\#sub {green glass jar of milky liquid}{lvl 20 Regeneration- jar of milky}{G\|pot subs}

\#sub {green glass jar of oil}{lvl 20 Resist Fire- jar of oil}{G\|pot subs}

\#sub {green glass jar of roiling liquid}{lvl 20 Resist Cold- jar of roiling}{G\|pot subs}

\#sub {green glass jar of viscous goo}{lvl 20 Armor- jar of viscous}{G\|pot subs}

\#sub {green potion}{potion of hysterical laughter-green}{G\|pot subs}

\#sub {hissing blue potion}{+20 mana for 1 hour- hissing blue}{G\|pot subs}

\#sub {holy grail}{bless/heal/sanctuary- holy grail}{G\|pot subs}

\#sub {matte-black potion}{Word of Recall/Heal- matte-black}{G\|pot subs}

\#sub {metallic red potion}{Iron Skin- metallic red}{G\|pot subs}

\#sub {midnight blue potion}{	Cure normal (1x)- midnight blue}{G\|pot subs}

\#sub {milky lavender potion}{L35 Perception- milky lavender}{G\|pot subs} 

\#sub {milky white potion}{Word of Recall- milky white}{G\|pot subs}

\#sub {moldy orange potion}{	+3 Damage for 10 Hrs- moldy orange}{G\|pot subs}

\#sub {mutap}{Cure Critic x 3- mutap}{G\|pot subs}

\#sub {navy blue potion}{Cure Light- navy blue}{G\|pot subs}

\#sub {olive potion}{Dispel Evil/ Curse/ Heal- olive potion}{G\|pot subs}

\#sub {orange potion}{3X Strength- orange}{G\|pot subs}

\#sub {pale purple potion}{Lvl 25 Water Breathing- pale purple}{G\|pot subs}

\#sub {pale rose potion}{Resist Fire/Resist Cold- pale rose}{G\|pot subs}

\#sub {pale violet potion}{Level 15 Infravision- pale violet}{G\|pot subs}

\#sub {pearlescent potion}{Lvl 44 Grace- pearlescent}{G\|pot subs}

\#sub {phial of dragon fire}{Talshan- phial of dragon fire}{G\|pot subs}

\#sub {potion crackling with magical energy}{Resistance to ALL spells- crackling}{G\|pot subs}

\#sub {potion of accuracy}{+5 To Hit- accuracy}{G\|pot subs}

\#sub {potion of desperation}{Recall- desperation}{G\|pot subs}

\#sub {potion of destruction}{	Bless, +3 Damage- destruction}{G\|pot subs}

\#sub {potion of endurance}{Vitality- endurance}{G\|pot subs}

\#sub {potion of flames}{3 Casts of Hellfire- flames}{G\|pot subs}

\#sub {potion of insight}{Det Invis lvl 12- insight}{G\|pot subs}

\#sub {potion of knitting}{unknown- knitting potion}{G\|pot subs}

\#sub {potion of legendary memory}{	Bestows Lloyd's Beacon 6 times- legendary memory}{G\|pot subs}

\#sub {potion of lesser sanctuary}{Sanctuary- lesser sanctuary}{G\|pot subs}

\#sub {potion of pure darkness}{Dark Cloak- pure darkness}{G\|pot subs}

\#sub {potion of refreshment}{Refresh x2- refreshment}{G\|pot subs}

\#sub {potion of speed}{Quicken- speed}{G\|pot subs}

\#sub {potion of stones}{lvl 43 dispel fly- stones}{G\|pot subs}

\#sub {potion of the essence of a mind flayer}{Aptitude- essence of a mind flayer}{G\|pot subs}

\#sub {potion of wispy prayers}{Insight- wispy prayers}{G\|pot subs}

\#sub {potion of youth}{Subtracts from age- youth}{G\|pot subs}

\#sub {pungent indigo potion}{Fly- pungent indigo}{G\|pot subs}

\#sub {purple potion}{Cure Poison- purple}{G\|pot subs}

\#sub {radiant white potion}{Imbue with 1x Raise Dead lvl 40- radiant white}{G\|pot subs}

\#sub {red potion}{Armor- red}{G\|pot subs}

\#sub {roiling blue potion}{lvl 25 Regenatation x1- roiling blue}{G\|pot subs}

\#sub {royal jelly}{Cure Light- royal jelly}{G\|pot subs}

\#sub {ruby red potion}{lvl 35 Sanctuary x1- ruby red}{G\|pot subs}

\#sub {russet potion}{	+0 to IMMUNE\_MAGIC for 5 hrs- russet}{G\|pot subs}

\#sub {rusty red potion}{apply 0 bonus to immune magic for 10 hrs- rusty red}{G\|pot subs}

\#sub {sea-green potion}{Remove Disease/Remove Poison- sea-green}{G\|pot subs}

\#sub {shiny golden potion}{+20 To Hit for 10 hours- shiny golden}{G\|pot subs}

\#sub {silver potion}{Call Lightning/Cure Critic- silver(Use Indoors!)} {G\|pot subs}

\#sub {slate-grey potion}{L25 Word of Recall- slate-grey}{G\|pot subs}

\#sub {sloshing blue potion}{Adds 150 Mana for 1 hour- sloshing blue}{G\|pot subs}

\#sub {smoky green potion}{Remove Poison- smoky green}{G\|pot subs}

\#sub {sparking yellow potion}{lvl 25 Call Lightning x3- sparking yellow}{G\|pot subs}

\#sub {sparkling blue potion}{Restores 35 Mana- sparkling blue}{G\|pot subs}

\#sub {sparkling green}{Det. Evil/Det. Invisible/Det. Magic- sparkling green}{G\|pot subs}

\#sub {sparkling vial}{Lvl 40 Dispel Fly- sparkling vial}{G\|pot subs}

\#sub {steaming black potion}{4x Demon Bind, Level 35- steaming black}{G\|pot subs}

\#sub {stree}{Dispel Magic- stree}{G\|pot subs}

\#sub {translucent purple potion}{Level 25 Detect Invis- translucent purple}{G\|pot subs}

\#sub {turquoise potion}{Level 40 Cure Plague- turquoise}{G\|pot subs}

\#sub {vaporous white potion}{3x Level 20 Cure Critic- vaporous white}{G\|pot subs}

\#sub {vial of distilled alcohol}{Disease (level 20)- distilled alcohol}{G\|pot subs}

\#sub {vial of ichor}{Unknown- ichor}{G\|pot subs}

\#sub {vial of salty sea water}{Earthquake/bless/blindness- salty sea water}{G\|pot subs}

\#sub {viscous purple potion}{Strength- viscous purple}{G\|pot subs}

\#sub {warm coral potion}{Lev 40 Resist Webs- warm coral}{G\|pot subs}

\#sub {yellow potion}{Detect Invisibility- yellow}{G\|pot subs}

Cheers

</div>
