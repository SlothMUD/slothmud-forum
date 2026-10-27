---
title: "Gem Descriptions"
topic_id: 5113
author: "Woody"
date: 2024-11-13T09:42:56+00:00
last_activity: 2024-11-13T09:42:56+00:00
last_author: "Woody"
sticky: false
locked: false
post_count: 1
---

<div class="post" data-post-id="40134" data-author="Woody" data-date="2024-11-13T09:42:56+00:00" data-subject="Gem Descriptions">

Are you often confused when looking into your tasseled dice bag?

This trigger will echo the description after each gem name seen.

I'm not great at regex, so this could probably be optimised, but it works for me.

perl regex: ^an? ?(\\w+ \*\\w+ \*\\w+)$

function gem\_description\_get(gem\_name)

 local gem\_description = {}

 gem\_description["Alexandrite"] = "T2, +1 Reduce Damage, body armor"

 gem\_description["Amber"] = "T1, +20 Circle Damage, vambraces, brassards, and phylacteries"

 gem\_description["Amethyst"] = "T2, +2 Weapon Damage, vambraces, brassards, and phylacteries"

 gem\_description["Aquamarine"] = "T2, +5 Mana, cloaks and mantles"

 gem\_description["Aventurine"] = "T3, +1 Damage Reduction, belts"

 gem\_description["Azurite"] = "T2, +1 Dex, torches and other held items"

 gem\_description["Banded Agate"] = "T2, +1 Str, torches and other held items"

 gem\_description["Black Onyx"] = "T3, +1 Damage, one-handed weapons"

 gem\_description["Bloodstone"] = "T1, -3 Saving Poison, rings"

 gem\_description["Blue Quartz"] = "T2, +1 Int, torches and other held items"

 gem\_description["Blue Star Sapphire"] = "T2, +2 Hit, one-handed weapons"

 gem\_description["Bright Green Emerald"] = "T2, +5 Mana, shields"

 gem\_description["Brilliant Green Garnet"] = "T1, -1 Saving Breath, shoes and boots"

 gem\_description["Brown Red Spinel"] = "T2, +5 Mana, body armor"

 gem\_description["Carnelian"] = "T1, -3 Saving Petrification, rings"

 gem\_description["Chalcedony"] = "T1, -2 Saving Breath, rings"

 gem\_description["Champagne Pearl"] = "T2, +1 SysShock, bracers, bracelets, and wristbands"

 gem\_description["Chrysoberyl"] = "T2, +1 SysShock, vambraces, brassards, and phylacteries"

 gem\_description["Chrysoprase"] = "T1, -2 Saving Spell, rings"

 gem\_description["Citrine"] = "T1, +1 Charisma, cloaks and mantles"

 gem\_description["Colorless Sapphire"] = "T3, +2 Weapon Damage, one-handed weapons"

 gem\_description["Coral"] = " T1, +5 Hitpoints, shields"

 gem\_description["Dark Green Spinel"] = "T1, +5 Hitpoints, body armor"

 gem\_description["Deep Blue Spinel"] = "T1, +5 HP Regen, greaves and leggings"

 gem\_description["Emerald"] = "T3, +1 Max Wis, torches and other held items"

 gem\_description["Eye Agate"] = "T1, -2 Saving Spells, cloaks and mantles"

 gem\_description["Fire Opal"] = "T2, +20 Circle Damage, one-handed weapons"

 gem\_description["Freshwater Pearl"] = "T1, -3 Saving Paralysis, rings"

 gem\_description["Golden Yellow Topaz"] = "T2, +1 Hand Damage, bracers, bracelets, and wristbands"

 gem\_description["Gray White Diamond"] = "T3, +4 Heal Bonus, necklaces, amulets, and gorgets"

 gem\_description["Hematite"] = "T2, +1 Wis, torches and other held items"

 gem\_description["Jacinth"] = "T3, -.1 AC, belts"

 gem\_description["Jade"] = "T2, +15 Stab Damage, gloves and gauntlets"

 gem\_description["Jasper"] = "T3, +1 Undead Control, cloaks and mantles"

 gem\_description["Jet"] = "T3, +1 Damage, gloves and gauntlets"

 gem\_description["Lapus Lazuli"] = "T2, +1 Con, torches and other held items"

 gem\_description["Light Blue Iolite"] = "T3, +4 Heal Bonus, belts"

 gem\_description["Malachite"] = "T3, +1 Max Str, torches and other held items"

 gem\_description["Moonstone"] = "T2, +10 Mv Regen, shoes and boots"

 gem\_description["Moss Agate"] = "T1, +1 Charisma, gloves and gauntlets"

 gem\_description["Obsidian"] = "T3, +1 Max Con, torches and other held items"

 gem\_description["Opal"] = "T2, +20 Circle Damage, bracers, bracelets, and wristbands"

 gem\_description["Orange Zircon"] = "T1, +20 Flail Damage, vambraces, brassards, and phylacteries"

 gem\_description["Pale Golden Pearl"] = "T1, +20 Flail Damage, bracers, bracelets, and wristbands"

 gem\_description["Pearl"] = "T1, +5 Hitpoints, shoes and boots"

 gem\_description["Peridot"] = "T1, +10 Moves, body armor"

 gem\_description["Pink Diamond"] = "T3, +4 Heal Bonus, helmets, hats, and the like"

 gem\_description["Purple Star Sapphire"] = "T2, +2 Hit, gloves and gauntlets"

 gem\_description["Quartz"] = "T1, +10 Kick Damage, shoes and boots"

 gem\_description["Red Spinel"] = "T1, +10 Moves, shields"

 gem\_description["Rhodochrosite"] = "T3, +1 Max Dex, torches and other held items"

 gem\_description["Rock Crystal Quartz"] = "T1, -1 Saving Spells, shoes and boots"

 gem\_description["Rose Quartz"] = "T3, +4 Spell Bonus, belts"

 gem\_description["Ruby"] = "T3, +1 Mana Regen, gloves and gauntlets"

 gem\_description["Sardonyx"] = "T2, +10 Mv Regen, greaves and leggings"

 gem\_description["Salmon Pink Garnet"] = "T1, +5 Mv Regen, shoes and boots"

 gem\_description["Sapphire"] = "T3, +4 Spell Bonus, helmets, hats, and the like"

 gem\_description["Silver Pearl"] = "T1, -1 Saving Paralysis, shoes and boots"

 gem\_description["Silvery Blue Pearl"] = "T2, +1 Hand Damage, gloves and gauntlets"

 gem\_description["Smokey Quartz"] = "T3, +4 Heal Bonus, belts"

 gem\_description["Star Ruby"] = "T3, +1 Mana Regen, necklaces, amulets, and gorgets"

 gem\_description["Tiger Eye"] = "T3, +1 Max Int, torches and other held items"

 gem\_description["Tomb Jade"] = "T3, +2 Weapon Damage, bracers, bracelets, and wristbands"

 gem\_description["Tourmaline"] = "T3, +4 Spell Bonus, necklaces, amulets, and gorgets"

 gem\_description["Violet Garnet"] = "T2, -0.1 AC, body armor"

 gem\_description["Water Opal"] = "T3, +15 Stab Damage, one-handed weapons"

 gem\_description["White Opal"] = "T2, +5 Stab Damage, bracers, bracelets, and wristbands"

 gem\_description["Zircon"] = "T2 +10 Kick Damage, greaves and leggings"

 return gem\_description[gem\_name]

end

local gem\_desc = gem\_description\_get(matches[2])

if gem\_desc then

 cecho(" ("..gem\_desc..")")

end

</div>
