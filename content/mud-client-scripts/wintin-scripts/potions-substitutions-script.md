---
title: "Potions Substitutions Script"
topic_id: 3648
author: "Strago"
date: 2011-01-25T15:03:43+00:00
last_activity: 2011-01-25T15:03:43+00:00
last_author: "Strago"
sticky: false
locked: false
post_count: 1
---

<div class="post" data-post-id="32372" data-author="Strago" data-date="2011-01-25T15:03:43+00:00">

This script is a modification of the potions script from the topic [Potions Type Helper](http://www.slothmud.org/forum/viewtopic.php?f=17&t=1974&p=32107&hilit=potion#p32107) for WinTin.net

Make sure to copy and paste the script as there is an escape character in there to ensure that default mud colors are not modified by the substitution.

```
#defgroup {Potions}
#substitute {acrid orange potion} {acrid orange potion (imbuewith 3x flamestrike)[0m}
#substitute {amethyst potion} {amethyst potion (infravision / detect invis / sense life)[0m}
#substitute {aquamarine potion.} {aquamarine potion. (cure minor)[0m}
#substitute {black potion with a red glowing center} {black potion with a red glowing center (dispel magic)[0m}
#substitute {blood red potion} {blood red potion (level 30 refresh)[0m}
#substitute {blue-green potion} {blue-green potion (level 25 cure serious)[0m}
#substitute {bright blue potion} {bright blue potion (lvl 40 greater heal)[0m}
#substitute {bright orange potion} {bright orange potion (+6 to dam for 10 hrs.)[0m}
#substitute {bright red potion} {bright red potion (l15 cure critic)[0m}
#substitute {brown misty potion {succor}} {brown misty potion {succor} (regeneration (level 40))[0m}
#substitute {bubbling green potion} {bubbling green potion (cure critic/invis/phase door)[0m}
#substitute {bubbling maroon potion} {bubbling maroon potion (armor)[0m}
#substitute {bubbling maroon potion} {bubbling maroon potion (level 15 armor)[0m}
#substitute {bubbling violet potion } {bubbling violet potion (lvl 40 knock)[0m}
#substitute {cerise potion} {cerise potion (armor/cure light)[0m}
#substitute {chartreuse potion} {chartreuse potion (l40 remove disaese)[0m}
#substitute {chilled black potion} {chilled black potion (telepathy)[0m}
#substitute {chocolate potion} {chocolate potion (invisibility, remove poison, remove curse)[0m}
#substitute {churning orange potion} {churning orange potion (imbue 3x lvl 40 disintegrate)[0m}
#substitute {clear blue potion} {clear blue potion (fly, water breathing, refresh)[0m}
#substitute {clear potion} {clear potion (cast vision 7 x as lv 25)[0m}
#substitute {clear potion with a lot of dirt sediment} {clear potion with a lot of dirt sediment (stone skin)[0m}
#substitute {clear white potion} {clear white potion (dispel/stone skin/sanc)[0m}
#substitute {cloudy purple potion} {cloudy purple potion (level 15 str)[0m}
#substitute {cloudy red potion} {cloudy red potion (level 35 stone skin)[0m}
#substitute {cold blue potion} {cold blue potion (+40 mana for 1 hr)[0m}
#substitute {creamy pink potion} {creamy pink potion (lvl 25 mindbar x1)[0m}
#substitute {dark yellow potion} {dark yellow potion (5x magic missile (lvl15))[0m}
#substitute {deep blue potion} {deep blue potion (regeneration/refresh/cure serious)[0m}
#substitute {deep purple potion} {deep purple potion (str (level 35))[0m}
#substitute {dull copper potion} {dull copper potion (+5 to hit, 10 hours)[0m}
#substitute {dull gold potion} {dull gold potion (lvl 12 cure light)[0m}
#substitute {dull gold potion} {dull gold potion ()[0m}
#substitute {dull gold potion} {dull gold potion (+5 to hit for 10 hrs)[0m}
#substitute {dull gray potion} {dull gray potion (lloyds beacon x2 at level 35)[0m}
#substitute {effervescent potion} {effervescent potion (det. evil/det. invisible/det. magic)[0m}
#substitute {fizzy ochre potion} {fizzy ochre potion (imbue l40 magic missile x30)[0m}
#substitute {flecked gold potion } {flecked gold potion (bless, strength, stone skin)[0m}
#substitute {frothy violet potion} {frothy violet potion (lvl 40 corona x1)[0m}
#substitute {frothy violet potion} {frothy violet potion (corona)[0m}
#substitute {glimmering green potion} {glimmering green potion (greater heal x3)[0m}
#substitute {glowing golden potion} {glowing golden potion (lvl 45 talshans tribute)[0m}
#substitute {grainy black potion} {grainy black potion (level 35 teleport)[0m}
#substitute {green potion} {green potion (teleport)[0m}
#substitute {green potion} {green potion (blindness & teleport & cure blind)[0m}
#substitute {hissing blue potion} {hissing blue potion (+20 mana for 1 hour)[0m}
#substitute {matte-black potion} {matte-black potion (word of recall/heal)[0m}
#substitute {metallic red potion} {metallic red potion (iron skin)[0m}
#substitute {midnight blue potion} {midnight blue potion (cure normal (1x))[0m}
#substitute {milky lavender potion} {milky lavender potion (l35 perception)[0m}
#substitute {milky white potion} {milky white potion ()[0m}
#substitute {milky white potion} {milky white potion (word of recall)[0m}
#substitute {milky white potion} {milky white potion (word of recall)[0m}
#substitute {moldy orange potion} {moldy orange potion (+3 damage for 10 hrs)[0m}
#substitute {moldy orange potion} {moldy orange potion (+3 dam for 10 hours)[0m}
#substitute {navy blue potion} {navy blue potion (cure light)[0m}
#substitute {olive potion} {olive potion (dispel evil/ curse/ heal)[0m}
#substitute {orange potion} {orange potion ()[0m}
#substitute {orange potion} {orange potion (3x strength)[0m}
#substitute {pale purple potion} {pale purple potion (lvl 25 water breathing)[0m}
#substitute {pale rose potion} {pale rose potion (resist fire/resist cold)[0m}
#substitute {pale violet potion} {pale violet potion (infravision)[0m}
#substitute {pale violet potion} {pale violet potion (level 15 infravision)[0m}
#substitute {pearlescent potion} {pearlescent potion (lvl 44 grace)[0m}
#substitute {potion crackling with magical energy} {potion crackling with magical energy (resistance to all spells targeting the user)[0m}
#substitute {potion of accuracy} {potion of accuracy (+5 to hit)[0m}
#substitute {potion of desperation} {potion of desperation (recall)[0m}
#substitute {potion of destruction} {potion of destruction (bless, +3 damage)[0m}
#substitute {potion of endurance} {potion of endurance (vitality)[0m}
#substitute {potion of flames} {potion of flames (3 casts of hellfire)[0m}
#substitute {potion of insight} {potion of insight (det invis lvl 12)[0m}
#substitute {potion of knitting} {potion of knitting (?)[0m}
#substitute {potion of legendary memory} {potion of legendary memory (bestows lloyd's beacon 6 times)[0m}
#substitute {potion of lesser sanctuary} {potion of lesser sanctuary (sanctuary)[0m}
#substitute {potion of pure darkness} {potion of pure darkness (dark cloak)[0m}
#substitute {potion of refreshment} {potion of refreshment (refresh x2)[0m}
#substitute {potion of speed} {potion of speed (quicken)[0m}
#substitute {potion of stones} {potion of stones (lvl 43 dispel fly)[0m}
#substitute {potion of the essence of a mind flayer} {potion of the essence of a mind flayer (aptitude)[0m}
#substitute {potion of wispy prayers} {potion of wispy prayers (insight)[0m}
#substitute {potion of youth} {potion of youth (subtracts from age)[0m}
#substitute {pungent indigo potion} {pungent indigo potion (fly)[0m}
#substitute {purple potion} {purple potion (cure poison)[0m}
#substitute {radiant white potion} {radiant white potion (imbue with 1x raise dead lvl 40)[0m}
#substitute {red orange potion} {red orange potion ( -100 ac for 3 ticks)[0m}
#substitute {red potion} {red potion (armor)[0m}
#substitute {roiling blue potion} {roiling blue potion (lvl 25 regenatation x1 )[0m}
#substitute {ruby red potion} {ruby red potion (lvl 35 sanctuary x1)[0m}
#substitute {russet potion} {russet potion (+0 to immune_magic for 5 hrs)[0m}
#substitute {rusty red potion} {rusty red potion (apply 0 bonus to immune magic for 10 hrs.)[0m}
#substitute {sea-green potion} {sea-green potion (remove disease/remove poison)[0m}
#substitute {shiny golden potion} {shiny golden potion (+20 to hit for 10 hours)[0m}
#substitute {shiny golden potion} {shiny golden potion (apply a bonus of 20 to the drinker's hitroll for 10 hours.)[0m}
#substitute {silver potion} {silver potion (call lightning/cure critic)[0m}
#substitute {sizzling yellow potion} {sizzling yellow potion (8x lightning bolt (imbued))[0m}
#substitute {slate-grey potion} {slate-grey potion (l25 word of recall)[0m}
#substitute {sloshing blue potion} {sloshing blue potion (adds 150 mana for 1 hour)[0m}
#substitute {smoky green potion} {smoky green potion (remove poison)[0m}
#substitute {sparking yellow potion} {sparking yellow potion (lvl 25 call lightning x3)[0m}
#substitute {sparkling blue potion} {sparkling blue potion (restores 35 mana )[0m}
#substitute {steaming black potion} {steaming black potion (4x demon bind, level 35)[0m}
#substitute {translucent purple potion} {translucent purple potion (level 25 detect invis.)[0m}
#substitute {turquoise potion} {turquoise potion (level 40 cure plague)[0m}
#substitute {vaporous white potion} {vaporous white potion (3x level 20 cure critic)[0m}
#substitute {viscous purple potion} {viscous purple potion (strength)[0m}
#substitute {warm coral potion} {warm coral potion (lev 40 resist webs)[0m}
#substitute {yellow potion} {yellow potion (detect invisibility)[0m}
#defgroup {}
```

</div>
