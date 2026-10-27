---
title: "Mob died from bloodloss carry no items/coins"
topic_id: 4048
author: "Yasik"
date: 2013-02-26T04:41:43+00:00
last_activity: 2013-02-28T16:20:02+00:00
last_author: "*Splork*"
sticky: false
locked: false
post_count: 9
---

<div class="post" data-post-id="34089" data-author="Yasik" data-date="2013-02-26T04:41:43+00:00" data-subject="Mob died from bloodloss carry no items/coins">

<strong>Mob dies from blood loss, almost never happens, but where's the loot? No items or coins, is this how it should be or is it bug?</strong>

![](http://dl.dropbox.com/u/72105811/Pics/Bloodloss_rakasha_no_coins.jpg)

</div>

<div class="post" data-post-id="34090" data-author="*juggleblood*" data-date="2013-02-26T09:33:43+00:00" data-subject="Re: Mob died from bloodloss carry no items/coins">

I checked to make sure there were no caches. I couldn't find any reason the mob should load empty.

</div>

<div class="post" data-post-id="34092" data-author="Yasik" data-date="2013-02-26T11:38:50+00:00" data-subject="Re: Mob died from bloodloss carry no items/coins">

I checked too, those mobs never had any caches, coins and eq always loaded on mobs.

I believe this is somehow related that I had summons, who participated in fight and finished this particular mob.

Also, there's times, when Autokill is ON, but I dont finish mob automatically with attacks (must "kill mob" additionally when its stunned/morted), and spells/skills without target says "Nobody here by that name.", as if Autokill is OFF.

On lower levels this problem happens a lot, on higher - rarely.

</div>

<div class="post" data-post-id="34093" data-author="*juggleblood*" data-date="2013-02-26T22:34:01+00:00" data-subject="Re: Mob died from bloodloss carry no items/coins">

One theory is that something interupts the transfer of the coins/objs from the mobile to the corpse, whether it be pet related or autokill.

Or a cache gets created and then somehow destroyed?

Or someone stole all the coins from the mob?

In any case, you'd prolly need to send more details to a coder. You say it happens all the time at low levels, but I make many test chars and haven't run across this yet.

</div>

<div class="post" data-post-id="34097" data-author="Magi" data-date="2013-02-27T22:49:51+00:00" data-subject="Re: Mob died from bloodloss carry no items/coins">

> <strong>Quote:</strong>
> Also, there's times, when Autokill is ON, but I don't finish mob automatically with attacks (must "kill mob" additionally when its stunned/morted), and spells/skills without target says "Nobody here by that name.", as if Autokill is OFF.
> 
> On lower levels this problem happens a lot, on higher - rarely.

This is definately related to pets. Despite autokill being on, you and your pet will both stop fighting if your pet lands the blow that morts a mob.

It is less noticable at high levels because you usually have more pets. You and the first pet are pulled out of the fight, but the remaining pets are still fighting and finish it off.

No idea about the missing coins issue. I have had it happen to me, (rarely) also on bloodloss. To clarify, bloodloss usually doesn't have this affect, but every time I've gotten no coins, it has been after bloodloss.

Other causes of no coins are: someone killed the mob while ptesting, or someone charmed the mob. I think it's nearly impossible to steal every coin from a mob. (Diminishing returns)

Unrelated: Is bloodloss neccessary? Bloodloss instantly or a few seconds after becoming morted happens frequently, mainly griefing newbies who don't deal enough damage to land killing blows. If a mob was immune to bloodloss for the first minute, that'd help the little people.

</div>

<div class="post" data-post-id="34098" data-author="*juggleblood*" data-date="2013-02-28T06:20:02+00:00" data-subject="Re: Mob died from bloodloss carry no items/coins">

I wonder if when pet morts target, mud checks to see if pet has autokill on (which an npc never can), instead of checking player. I'll submit it to the bugs list and someone will take a crack at it when they get a chance.

Sounds like the big prob with bloodloss is the bug u mention. If the follower/autokill bug wasn't confusing the player by ceasing combat after mob is morted by the pet it wouldn't matter so much. Another 10 secs wouldn't hurt either.

</div>

<div class="post" data-post-id="34107" data-author="*Splork*" data-date="2013-02-28T13:00:30+00:00" data-subject="Re: Mob died from bloodloss carry no items/coins">

I made some changes, keep an eye out and see if it has any affects.

If you are not engaged and your pet morts a creature, autokill will not work but if you are engaged and the pet gets last hit, hopefully now you will continue through the fight.

I lowered Bloodloss a few years ago because of the reasons in the previous post but lowered it again.

Changes in next reboot,

Splork

</div>

<div class="post" data-post-id="34108" data-author="Yasik" data-date="2013-02-28T15:11:08+00:00" data-subject="Re: Mob died from bloodloss carry no items/coins">

Made an example log to illustrate the situation. Me and my ghost, few minutes ago - ghost morted the mob, and all fight stopped, so I had to issue a command 'kill mob', while by design of Autokill I shouldn't.

<strong>autokill on</strong>

<strong>Autokill mode is now on.</strong>

\<466hp 117ma 164mv\> [-3] AC: -6.0 EXP: 254,569 COINS: 53,824

<strong>setti</strong>

Verbosity:

 BRIEF: on 

 COMPACT: off

 PROMPT\_CR: off

 CONCISE: off

 SHOWEXITS: on 

 ECHO: on 

 GAG FIGHT: off

 GAG EQ: off

 GAG TITLE: off

Communications:

 GOSSIP: on 

 AUCTION: on 

 NEWBIE: on 

 QUEST: on 

 NOTELL: off

Other:

 ASCII MAP: off

 AUTOLOOT: on 

 AUTOSPLIT: off

 <strong>AUTOKILL: on</strong> 

 AUTOGROUP: on 

 PRIVATE: off

 NUMFORMAT: on 

 LURK: off

 ISNEWBIE: off

 LOGIN\_TIME\_EXTRAS: off

 COMMS ONLY: off

 ROOM COORDS: off

Protocols:

 MCCP: on - V2 (In-\>667179, Out-\>81124, Saved 88%)

 MXP: Unsupported

 MSDP: Unsupported

 ATCP: Unsupported

\<466hp 117ma 164mv\> [-3] AC: -6.0 EXP: 254,569 COINS: 53,824

look

\<466hp 117ma 166mv\> [-3] AC: -6.0 EXP: 254,569 COINS: 53,824

Edge of an Enchanted Forest

 Large sycamore trees rise up to the heavens, gleaming with a soft glow. 

The treetops rustle high above, and this, in combination with mysterious 

twilight, produces an uneasy mood. The tangled growth makes walking an 

exercise in getting branch-slapped and thorn-torn. To the west the travel 

appears slightly easier as the forest floor continues to decline, while an 

absolutely impenetrable wall of sequoia trees blocks the passage southward. 

What resembles the bustling of a city, comes from the south.

Exits: North East 

A band of colorful pink fur has been dropped here on the ground...It has a soft glowing aura!

\*A powerful looking mage wanders about the temple.

<strong>A ghostly form wavers in and out of existence nearby.</strong>

\*A powerful looking mage wanders about the temple.

\*A powerful looking mage wanders about the temple.

A mystical bugbear wanders about the sacred land.

\<466hp 117ma 166mv\> [-3] AC: -6.0 EXP: 254,569 COINS: 53,824

TARGET: bugbear-servant

kill bugbear-servant

A servant of Blaster hates your guts!

order undead assist Yasik

Frenzy

You miss a servant of Blaster with your slash.

\<466hp 117ma 167mv\> [-3] AC: -6.0 EXP: 254,569 COINS: 53,824

You slash a servant of Blaster extremely hard.

A servant of Blaster misses you with his pound.

A servant of Blaster misses you with his pound.

You miss a servant of Blaster with your slash.

\<466hp 117ma 168mv\> [-3] AC: -6.0 EXP: 254,985 COINS: 53,824

A ghost pounds a servant of Blaster very hard.

\<466hp 117ma 169mv\> [-3] AC: -6.0 EXP: 254,985 COINS: 53,824

You slash a servant of Blaster extremely hard.

A ghost misses a servant of Blaster with its pound.

A ghost bites a servant of Blaster hard.

A servant of Blaster misses you with his pound.

A servant of Blaster misses you with his pound.

You slash a servant of Blaster extremely hard.

\<466hp 117ma 170mv\> [-3] AC: -6.0 EXP: 256,365 COINS: 53,824

You slash a servant of Blaster extremely hard.

A ghost pounds a servant of Blaster hard.

A ghost bites a servant of Blaster hard.

A servant of Blaster misses you with his pound.

A servant of Blaster misses you with his pound.

You slash a servant of Blaster very hard.

\<466hp 117ma 172mv\> [-3] AC: -6.0 EXP: 256,481 COINS: 53,824

You begin to channel your anger and enter a state of frenzy.

\<466hp 117ma 173mv\> [-3] AC: -6.0 EXP: 256,481 COINS: 53,824

You slash a servant of Blaster very hard.

A ghost misses a servant of Blaster with its pound.

A ghost misses a servant of Blaster with its bite.

A servant of Blaster misses you with his pound.

A servant of Blaster misses a ghost with his pound.

You slash a servant of Blaster extremely hard.

\<466hp 117ma 174mv\> [-3] AC: -6.0 EXP: 257,140 COINS: 53,824

You slash a servant of Blaster extremely hard.

A ghost misses a servant of Blaster with its pound.

A ghost bites a servant of Blaster hard.

A servant of Blaster pounds a ghost very hard.

A servant of Blaster misses you with his pound.

You massacre a servant of Blaster to small fragments with your slash.

\<466hp 117ma 176mv\> [-3] AC: -6.0 EXP: 257,763 COINS: 53,824

You slash a servant of Blaster extremely hard.

A ghost pounds a servant of Blaster hard.

A ghost misses a servant of Blaster with its bite.

A servant of Blaster misses you with his pound.

A servant of Blaster misses you with his pound.

You slash a servant of Blaster extremely hard.

\<466hp 117ma 178mv\> [-3] AC: -6.0 EXP: 258,874 COINS: 53,824

You miss a servant of Blaster with your slash.

A ghost misses a servant of Blaster with its pound.

A ghost bites a servant of Blaster hard.

A servant of Blaster pounds a ghost very hard.

A servant of Blaster misses you with his pound.

\<466hp 117ma 179mv\> [-3] AC: -6.0 EXP: 258,874 COINS: 53,824

You massacre a servant of Blaster to small fragments with your slash.

A ghost misses a servant of Blaster with its pound.

A ghost bites a servant of Blaster very hard.

A servant of Blaster pounds a ghost hard.

A servant of Blaster misses you with his pound.

You slash a servant of Blaster extremely hard.

\<466hp 117ma 182mv\> [-3] AC: -6.0 EXP: 259,490 COINS: 53,824

You massacre a servant of Blaster to small fragments with your slash.

A ghost pounds a servant of Blaster hard.

A ghost bites a servant of Blaster.

A servant of Blaster pounds a ghost hard.

A servant of Blaster misses you with his pound.

A servant of Blaster utters the words, 'judicandus iafwar'

\<466hp 117ma 183mv\> [-3] AC: -6.0 EXP: 260,120 COINS: 53,824

You massacre a servant of Blaster to small fragments with your slash.

A ghost misses a servant of Blaster with its pound.

A ghost misses a servant of Blaster with its bite.

A servant of Blaster misses a ghost with his pound.

A servant of Blaster misses you with his pound.

You massacre a servant of Blaster to small fragments with your slash.

A servant of Blaster utters the words, 'judicandus iafwar'

\<466hp 117ma 185mv\> [-3] AC: -6.0 EXP: 260,956 COINS: 53,824

You slash a servant of Blaster extremely hard.

A ghost pounds a servant of Blaster hard.

A ghost misses a servant of Blaster with its bite.

A servant of Blaster misses a ghost with his pound.

A servant of Blaster misses a ghost with his pound.

\<466hp 117ma 186mv\> [-3] AC: -6.0 EXP: 261,324 COINS: 53,824

You slash a servant of Blaster extremely hard.

A ghost pounds a servant of Blaster very hard.

A ghost misses a servant of Blaster with its bite.

A servant of Blaster misses you with his pound.

A servant of Blaster misses you with his pound.

You slash a servant of Blaster extremely hard.

\<466hp 117ma 188mv\> [-3] AC: -6.0 EXP: 261,886 COINS: 53,824

look

Edge of an Enchanted Forest

 Large sycamore trees rise up to the heavens, gleaming with a soft glow. 

The treetops rustle high above, and this, in combination with mysterious 

twilight, produces an uneasy mood. The tangled growth makes walking an 

exercise in getting branch-slapped and thorn-torn. To the west the travel 

appears slightly easier as the forest floor continues to decline, while an 

absolutely impenetrable wall of sequoia trees blocks the passage southward. 

What resembles the bustling of a city, comes from the south.

Exits: North East 

A band of colorful pink fur has been dropped here on the ground...It has a soft glowing aura!

\*A powerful looking mage wanders about the temple.

\*A powerful looking mage wanders about the temple.

A ghost is here, fighting a servant of Blaster

\*A powerful looking mage wanders about the temple.

\*A powerful looking mage wanders about the temple.

A servant of Blaster is here, fighting YOU!

\<466hp 117ma 189mv\> [-3] AC: -6.0 EXP: 261,886 COINS: 53,824

You slash a servant of Blaster extremely hard.

<strong>A ghost pounds a servant of Blaster very hard.</strong>

<strong>A servant of Blaster is mortally wounded, and will die soon, if not aided.</strong>

\<466hp 117ma 191mv\> [-3] AC: -6.0 EXP: 262,102 COINS: 53,824

<strong>Kick</strong>

<strong>You don't see that person.</strong>

\<466hp 117ma 192mv\> [-3] AC: -6.0 EXP: 262,102 COINS: 53,824

A servant of Blaster lies immobile on the ground, suffering...

A servant of Blaster is mortally wounded, and will die soon, if not aided.

\<466hp 117ma 196mv\> [-3] AC: -6.0 EXP: 262,102 COINS: 53,824

You calm down and return to a peaceful state of mind.

Frenzy

\<466hp 117ma 197mv\> [-3] AC: -6.0 EXP: 262,102 COINS: 53,824

You begin to channel your anger and enter a state of frenzy.

\<466hp 117ma 198mv\> [-3] AC: -6.0 EXP: 262,102 COINS: 53,824

<strong>Kick</strong>

<strong>You don't see that person.</strong>

\<466hp 117ma 199mv\> [-3] AC: -6.0 EXP: 262,102 COINS: 53,824

<strong>Kick</strong>

<strong>You don't see that person.</strong>

\<466hp 117ma 200mv\> [-3] AC: -6.0 EXP: 262,102 COINS: 53,824

<strong>bash</strong>

<strong>Bash who?</strong>

\<466hp 117ma 201mv\> [-3] AC: -6.0 EXP: 262,102 COINS: 53,824

kill bugbear-servant

You massacre a servant of Blaster to small fragments with your slash.

A servant of Blaster is dead! R.I.P.

You are taking the first steps along the way to redemption.

Total exp for kill is 31478.

Your blood freezes as you hear a servant of Blaster's death cry.

You get a furry wristband from the corpse of a servant of Blaster that's on the ground.

You get gold coins from the corpse of a servant of Blaster that's on the ground.

There were 1200 coins.

</div>

<div class="post" data-post-id="34109" data-author="*Splork*" data-date="2013-02-28T16:20:02+00:00" data-subject="Re: Mob died from bloodloss carry no items/coins">

The change I made must not of worked and the issue is much deeper, such as your character is not the primary person engaged. Changing this will have some unwanted changes, such as you will take more damage than your mobs will.

I am not sure you guys really want this fixed, if the results are what I previously mentioned and figuring out a fix where this does not occur is not going to be easy and will take quite a bit of time and debugging. Time I just do not have atm.

Splork

</div>
