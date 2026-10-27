---
title: "odd"
topic_id: 2063
author: "Malison"
date: 2006-09-18T18:55:05+00:00
last_activity: 2006-09-18T21:53:34+00:00
last_author: "*Splork*"
sticky: false
locked: false
post_count: 7
---

<div class="post" data-post-id="14135" data-author="Malison" data-date="2006-09-18T18:55:05+00:00" data-subject="odd">

Last bootup: Mon Sep 18 13:37:34 2006

Current time: Mon Sep 18 13:50:31 2006

[20c 17d 13o 10b] Verin

No idea what happened here, but for a moment between rounds it looked like my maxhp went down by 108. No spell wore off/was recast, no eq was changed, my maxhp just became my maxma for a moment. I didn't have time to check if it changed on score as well or was just a prompt issue.

\<296/300hp 117/192ma 110mv\>

You pierce the fortune hunter hard.

The fortune hunter misses you with his hit.

The fortune hunter misses you with his pound.

The fortune hunter misses you with his crush.

The fortune hunter really needs a good bath! Phew!

\<297/192hp 118/192ma 110mv\>

Ok.

The fortune hunter is scorched by the flames of Hell!

\<297/300hp 106/192ma 110mv\>

The 'regeneration' spell on you is about to wear off.

</div>

<div class="post" data-post-id="14136" data-author="Malison" data-date="2006-09-18T18:58:55+00:00" data-subject="">

7 minutes later...

\<266/300hp 157/192ma 110mv\>

The fortune hunter really needs a good bath! Phew!

Ok.

You feel better!

\<192/192hp 146/192ma 110mv\>

You pierce the fortune hunter hard.

The fortune hunter misses you with his hit.

The fortune hunter misses you with his pound.

The fortune hunter misses you with his crush.

You pierce the fortune hunter hard.

\<192/300hp 147/192ma 110mv\>

This time without being hit my current hp and maxhp dropped to maxma.

\<edit\> And right after finishing writing that, maxhp dropped to maxma again for a sec.

</div>

<div class="post" data-post-id="14138" data-author="Jag" data-date="2006-09-18T19:19:21+00:00" data-subject="Two odd?">

I was in Wyrmlings and I lost 132 hps while doing 3 consecutive cure minors on myself. No mobs were in the room.

\<360hp 94ma 74mv\>

sac

You do not see anything in the corpse.

\<361hp 94ma 74mv\>

You sacrifice the corpse to Blaster.

\<361hp 94ma 74mv\>

sac

You do not see anything in the corpse.

\<361hp 94ma 74mv\>

You sacrifice the corpse to Blaster.

\<361hp 94ma 74mv\>

inv

You are carrying:

a disembodied eye

a purple potion

a red potion [2]

a sapphire qwevri..It has a soft glowing aura!

a backpack

a scroll of identify

iron rations [3]

a scroll of recall

an orange potion [4]

a sprig of nightshade

a thick brightly glowing spellbook

a decomposing brain

a yellow potion

\<362hp 94ma 75mv\>

Ok.

You feel better!

\<376hp 87ma 77mv\>

Ok.

You feel better!

\<124hp 80ma 78mv\>

l

Ok.

You feel better!

\<135hp 72ma 79mv\>

sc

Dragon Throne

 A basalt statue of a dragon dominates this ten-foot-diameter chamber.

Closer examination shows that the statue is actually a throne built for

someone perhaps half man-sized. The walls are carved with other dragon-

themed murals; the only exit is through a carved archway to the south.

Exits: South

\<137hp 72ma 80mv\>

Hc Hi Mud (level: 20)

Your levels: Wa: 20 Mo: 20 Dr: 14 Ne: 7

You are 17 years and 8 months old.

You are a citizen of Valkyre.

You are a devout worshipper of Blaster.

You are starting to get a little peckish.

You are tainted with evil.

You have 137(449) hit, 72(124) mana and 80(107) movement points.

Your armor class is -5.9.

You have 5680 gold coins.

You have twenty-six drachma.

You have 1677941 unused experience points.

You have been playing for 1 days and 17 hours.

Str: 18 / 100, Int: 12, Wis: 14, Dex: 18, Con: 18

You are standing.

You are affected by the following spells:

 Detect Invisible

 Darksight

 Resist Fire

 Resist Cold

 Armor

 Strength

\<137hp 72ma 80mv\>

</div>

<div class="post" data-post-id="14140" data-author="12345" data-date="2006-09-18T19:37:01+00:00" data-subject="">

The game has been up almost 8 days now. Might be starting to flake out.

</div>

<div class="post" data-post-id="14142" data-author="kjartan" data-date="2006-09-18T19:55:47+00:00" data-subject="">

We just put in code that allows mobs to have higher max hp, and it sounds like there may be some bug related to that. We're on it.

</div>

<div class="post" data-post-id="14144" data-author="12345" data-date="2006-09-18T21:12:29+00:00" data-subject="">

Funny bug to watch. Glad I was regenning.

\<1073/1050hp+100 300/300 234/234 -3 -10.4 0 None Down\>

You feel the ship slow as it nears the journey's end.

\<1059/300hp+100 300/300 234/234 -3 -10.4 1 None Down\>

You grouptell: '//Bit// [1059/300] [Pain!: -14] [Need: -759] [Aegis: Down]'

\<1059/300hp+100 300/300 234/234 -3 -10.4 1 None Down\>

The ship lurches as it comes to an abrupt stop against the docks.

\<1050/300hp+100 300/300 234/234 -3 -10.4 2 None Down\>

You grouptell: '//Bit// [1050/300] [Pain!: -9] [Need: -750] [Aegis: Down]'

\<1050/300hp+100 300/300 234/234 -3 -10.4 2 None Down\>

The ships captain bellows out orders in preparation for departure.

\<1050/300hp+100 300/300 234/234 -3 -10.4 3 None Down\>

st

You are already awake...

\<1050/1050hp+100 300/300 234/234 -3 -10.4 3 None Down\>

You are already standing.

</div>

<div class="post" data-post-id="14145" data-author="*Splork*" data-date="2006-09-18T21:53:34+00:00" data-subject="Fixed">

This bug should be fixed(we rebooted), I apologize for not being around earlier to grab it but worked late.

We had to touch an obscene amount of code to make this project work, so I will be amazed if that was the only bug-but lets hope.

Splork

</div>
