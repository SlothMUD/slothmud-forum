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

<div class="post" data-post-id="40134" data-author="Woody" data-date="2024-11-13T09:42:56+00:00">

Are you often confused when looking into your tasseled dice bag?

This trigger will echo the description after each gem name seen.

I'm not great at regex, so this could probably be optimised, but it works for me.

perl regex: ^an? ?(\w+ *\w+ *\w+)$

function gem_description_get(gem_name)

  local gem_description = {}

  

  gem_description["Alexandrite"] = "T2, +1 Reduce Damage, body armor"

  gem_description["Amber"] = "T1, +20 Circle Damage, vambraces, brassards, and phylacteries"

  gem_description["Amethyst"] = "T2, +2 Weapon Damage, vambraces, brassards, and phylacteries"

  gem_description["Aquamarine"] = "T2, +5 Mana, cloaks and mantles"

  gem_description["Aventurine"] = "T3, +1 Damage Reduction, belts"

  gem_description["Azurite"] = "T2, +1 Dex, torches and other held items"

  gem_description["Banded Agate"] = "T2, +1 Str, torches and other held items"

  gem_description["Black Onyx"] = "T3, +1 Damage, one-handed weapons"

  gem_description["Bloodstone"] = "T1, -3 Saving Poison, rings"

  gem_description["Blue Quartz"] = "T2, +1 Int, torches and other held items"

  gem_description["Blue Star Sapphire"] = "T2, +2 Hit, one-handed weapons"

  gem_description["Bright Green Emerald"] = "T2, +5 Mana, shields"

  gem_description["Brilliant Green Garnet"] = "T1, -1 Saving Breath, shoes and boots"

  gem_description["Brown Red Spinel"] = "T2, +5 Mana, body armor"

  gem_description["Carnelian"] = "T1, -3 Saving Petrification, rings"

  gem_description["Chalcedony"] = "T1, -2 Saving Breath, rings"

  gem_description["Champagne Pearl"] = "T2, +1 SysShock, bracers, bracelets, and wristbands"

  gem_description["Chrysoberyl"] = "T2, +1 SysShock, vambraces, brassards, and phylacteries"

  gem_description["Chrysoprase"] = "T1, -2 Saving Spell, rings"

  gem_description["Citrine"] = "T1, +1 Charisma, cloaks and mantles"

  gem_description["Colorless Sapphire"] = "T3, +2 Weapon Damage, one-handed weapons"

  gem_description["Coral"] = " T1, +5 Hitpoints, shields"

  gem_description["Dark Green Spinel"] = "T1, +5 Hitpoints, body armor"

  gem_description["Deep Blue Spinel"] = "T1, +5 HP Regen, greaves and leggings"

  gem_description["Emerald"] = "T3, +1 Max Wis, torches and other held items"

  gem_description["Eye Agate"] = "T1, -2 Saving Spells, cloaks and mantles"

  gem_description["Fire Opal"] = "T2, +20 Circle Damage, one-handed weapons"

  gem_description["Freshwater Pearl"] = "T1, -3 Saving Paralysis, rings"

  gem_description["Golden Yellow Topaz"] = "T2, +1 Hand Damage, bracers, bracelets, and wristbands"

  gem_description["Gray White Diamond"] = "T3, +4 Heal Bonus, necklaces, amulets, and gorgets"

  gem_description["Hematite"] = "T2, +1 Wis, torches and other held items"

  gem_description["Jacinth"] = "T3, -.1 AC, belts"

  gem_description["Jade"] = "T2, +15 Stab Damage, gloves and gauntlets"

  gem_description["Jasper"] = "T3, +1 Undead Control, cloaks and mantles"

  gem_description["Jet"] = "T3, +1 Damage, gloves and gauntlets"

  gem_description["Lapus Lazuli"] = "T2, +1 Con, torches and other held items"

  gem_description["Light Blue Iolite"] = "T3, +4 Heal Bonus, belts"

  gem_description["Malachite"] = "T3, +1 Max Str, torches and other held items"

  gem_description["Moonstone"] = "T2, +10 Mv Regen, shoes and boots"

  gem_description["Moss Agate"] = "T1, +1 Charisma, gloves and gauntlets"

  gem_description["Obsidian"] = "T3, +1 Max Con, torches and other held items"

  gem_description["Opal"] = "T2, +20 Circle Damage, bracers, bracelets, and wristbands"

  gem_description["Orange Zircon"] = "T1, +20 Flail Damage, vambraces, brassards, and phylacteries"

  gem_description["Pale Golden Pearl"] = "T1, +20 Flail Damage, bracers, bracelets, and wristbands"

  gem_description["Pearl"] = "T1, +5 Hitpoints, shoes and boots"

  gem_description["Peridot"] = "T1, +10 Moves, body armor"

  gem_description["Pink Diamond"] = "T3, +4 Heal Bonus, helmets, hats, and the like"

  gem_description["Purple Star Sapphire"] = "T2, +2 Hit, gloves and gauntlets"

  gem_description["Quartz"] = "T1, +10 Kick Damage, shoes and boots"

  gem_description["Red Spinel"] = "T1, +10 Moves, shields"

  gem_description["Rhodochrosite"] = "T3, +1 Max Dex, torches and other held items"

  gem_description["Rock Crystal Quartz"] = "T1, -1 Saving Spells, shoes and boots"

  gem_description["Rose Quartz"] = "T3, +4 Spell Bonus, belts"

  gem_description["Ruby"] = "T3, +1 Mana Regen, gloves and gauntlets"

  gem_description["Sardonyx"] = "T2, +10 Mv Regen, greaves and leggings"

  gem_description["Salmon Pink Garnet"] = "T1, +5 Mv Regen, shoes and boots"

  gem_description["Sapphire"] = "T3, +4 Spell Bonus, helmets, hats, and the like"

  gem_description["Silver Pearl"] = "T1, -1 Saving Paralysis, shoes and boots"

  gem_description["Silvery Blue Pearl"] = "T2, +1 Hand Damage, gloves and gauntlets"

  gem_description["Smokey Quartz"] = "T3, +4 Heal Bonus, belts"

  gem_description["Star Ruby"] = "T3, +1 Mana Regen, necklaces, amulets, and gorgets"

  gem_description["Tiger Eye"] = "T3, +1 Max Int, torches and other held items"

  gem_description["Tomb Jade"] = "T3, +2 Weapon Damage, bracers, bracelets, and wristbands"

  gem_description["Tourmaline"] = "T3, +4 Spell Bonus, necklaces, amulets, and gorgets"

  gem_description["Violet Garnet"] = "T2, -0.1 AC, body armor"

  gem_description["Water Opal"] = "T3, +15 Stab Damage, one-handed weapons"

  gem_description["White Opal"] = "T2, +5 Stab Damage, bracers, bracelets, and wristbands"

  gem_description["Zircon"] = "T2 +10 Kick Damage, greaves and leggings"

  return gem_description[gem_name]

  

end

local gem_desc = gem_description_get(matches[2])

if gem_desc then

  cecho(" ("..gem_desc..")")

end

</div>
