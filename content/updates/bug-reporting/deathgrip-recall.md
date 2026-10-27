---
title: "Deathgrip / Recall"
topic_id: 4392
author: "Yasik"
date: 2014-09-13T18:21:59+00:00
last_activity: 2014-09-26T20:59:15+00:00
last_author: "*Breeze*"
sticky: false
locked: false
post_count: 4
---

<div class="post" data-post-id="35436" data-author="Yasik" data-date="2014-09-13T18:21:59+00:00" data-subject="Deathgrip / Recall">

Hello!

I found this a bit unusual, recalling during deathgrip does not release the grip, while it should, I think...

Also, the @@ somehow add blank CR/LF, printing new prompt (green line in the log), but no other text is displayed. I think that doing-nothing CR/LF is not much needed, isnt it?

A lich hates your guts!

A lich slowly fades into existence.

You circle around a lich and expertly put it in a deathgrip.

\<1055hp 472ma 214mv\> +9 -10.4 113,622,005 512,649 indoors The Thordfalan Volcano

You skillfully parry the attack of a lich.

You are brutally massacred by a lich's claw.

You are viciously massacred by a lich's claw.

You are viciously massacred by a lich's bite.

A lich emits a gutteral growl at your intrusion.

\<835hp 474ma 216mv\> +9 -10.4 113,622,005 512,649 indoors The Thordfalan Volcano

You maintain your deathgrip on a lich.

\<837hp 475ma 216mv\> +9 -10.4 113,626,628 512,649 indoors The Thordfalan Volcano

order undead assist Ozzy

A spectre misses a lich with its claw.

A spectre misses a lich with its claw.

A spectre claws a lich very hard.

\<840hp 477ma 218mv\> +9 -10.4 113,626,628 512,649 indoors The Thordfalan Volcano

A spectre misses a lich with its claw.

A spectre misses a lich with its claw.

A spectre misses a lich with its claw.

A spectre misses a lich with its claw.

A spectre misses a lich with its claw.

A spectre misses a lich with its claw.

You are viciously massacred by a lich's claw.

A lich misses you with its claw.

You are viciously massacred by a lich's claw.

You are viciously massacred by a lich's bite.

A lich stomps its enormous feet in rage!

You maintain your deathgrip on a lich.

\<599hp 477ma 219mv\> +9 -10.4 113,629,551 512,649 indoors The Thordfalan Volcano

The 'stone skin' spell on you is about to wear off.

\<602hp 477ma 220mv\> +9 -10.4 113,629,551 512,649 indoors The Thordfalan Volcano

cast 'Word of Recall'

@@

You maintain your deathgrip on a lich.

With a mighty effort, you shake off your exhaustion!

Ok.

West Gate

 This is the west gate of the port city of Bal Harbor. A wide dirt 

roadway leads in between a pair of squarish-looking guard towers into the 

city to the east, and to west disappears into a flat grassy plain. Visible 

to the far west is what appears to be a forest or jungle that rims the 

entire western horizon. To the east, the roadway can be seen to lead into 

a distant town square.

Exits: East West Up 

A large horse-drawn covered wagon is docked here.

The corpse of War is lying here.

A big, important-looking sign titled 'New Player Info' stands here.

The Red Sash City Guard scans intently for intruders and other troublemakers.

The Red Sash City Guard scans intently for intruders and other troublemakers.

The Red Sash City Guard scans intently for intruders and other troublemakers.

A Sergeant in the Red Sash corp observes all the comings and goings of Bal Harbor.

\<605hp 442ma 206mv\> +9 -10.4 113,629,859 512,649 fair Bal Harbor Town

A spectre stops following you.

\<605hp 442ma 206mv\> +9 -10.4 113,629,859 512,649 fair Bal Harbor Town

\<608hp 444ma 208mv\> +9 -10.4 113,629,859 512,649 fair Bal Harbor Town

You release your grip on a lich.

</div>

<div class="post" data-post-id="35437" data-author="Magi" data-date="2014-09-16T17:40:29+00:00" data-subject="Re: Deathgrip / Recall">

Recalling, or using any other method of leaving the room, does release the grip, albeit with a small delay. You cannot maintain a grip (dealing damage) on a creature that's in another room. You'll always release it at the first opportunity.

The timing of the release message is delayed until the next tick of deathgrip activity. Code doesn't happen in realtime, it is broken down into fractions of seconds. To make the message about releasing the grip simultaneous with leaving the room you'd need either:

 \- A super fast check, many times per second, on every player to make sure they haven't left the room of a deathgrip, or 

 \- Custom case handling built into every action that could remove you from a room. (Recall, flee, retreat, dozens of 'current' procs, every mob 'toss' proc, teleport potions, dispelled fly, etc.)

The current implementation of releasing the mob according to the deathgrip timer is the most practical. It does have the odd quirk that if you leave the room but return instantly, your grip won't be broken. I can't think of any way to make that quirk useful to players though <img src="/images/smilies/icon_e_smile.svg" alt=":)" title=":)" width="15" height="15" class="smiley nozoom">

tl;dr Deathgrip's current implementation is fine

\-- Josiah

</div>

<div class="post" data-post-id="35438" data-author="DarkArtist" data-date="2014-09-17T19:44:22+00:00" data-subject="Re: Deathgrip / Recall">

It would be a simple matter to implement a check for deathgrip status everytime a pc teleport function is called. 

I think it fairly fits in the bug category.

</div>

<div class="post" data-post-id="35439" data-author="*Breeze*" data-date="2014-09-26T20:59:15+00:00" data-subject="Re: Deathgrip / Recall">

Bugs it. Someone will get to it eventually

</div>
