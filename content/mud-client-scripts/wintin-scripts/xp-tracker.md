---
title: "XP tracker"
topic_id: 239
author: "Eagle"
date: 2004-06-29T18:54:04+00:00
last_activity: 2004-08-24T19:02:28+00:00
last_author: "Qa"
sticky: false
locked: false
post_count: 6
---

<div class="post" data-post-id="879" data-author="Eagle" data-date="2004-06-29T18:54:04+00:00" data-subject="XP tracker">

lookin for an xp tracker if someone wants to share<BR>rye_bread80@msn.com<BR>thanks

</div>

<div class="post" data-post-id="880" data-author="Qa" data-date="2004-06-29T19:10:12+00:00" data-subject="">

This is an old-school xp counter.  If you cap, it countas the extra.  If you get healing bonuses or damage bonuses, it doesn't track those.  Oh, and it works with wintin/jmc.  -Qa

#nop

#nop

#nop  Auto clean subroutine & XP counter

#nop

#var {grxpcount} {0}

#var {xpcount} {0}

#nop

#nop  Group XP counter 

#nop

#action {^Total exp for kill is %1.} {save ; sneak ; #math grxpcount {$grxpcount + $1} } {9}

#nop

#nop  XP counter if grouped

#nop

#nop  If leading...

#action {^Total exp for kill is %1.} {save ; sneak ; #math grxpcount {$grxpcount + $1} } {9}

#nop

#nop  If a group member...

#action {^You receive %1 experience} {save ; sneak ; #math xpcount {$xpcount + $1} } {9}

#nop

#nop  Solo XP counter

#nop

#nop  Autosac if not grouped...

#action {^You received %1 experience} {g all corpse; save ; sneak ; #math xpcount {$xpcount + $1} } {2}

#nop

#nop

#nop  Data - Shows information regarding the game status

#nop

#alias {data} {#showme XP since last reset $xpcount ; #if {$grxpcount > 0} #showme Group XP since last reset - $grxpcount}

#alias {zeroxp} {#math xpcount 0 ; #math grxpcount 0}

</div>

<div class="post" data-post-id="882" data-author="Leizu" data-date="2004-06-30T12:38:06+00:00" data-subject="">

This one shows info in 2 buttons, first one with xp I need to level, second one with xp/gold I've got since the last check. Adapt for your needs :)

[code:374y941w]

#KEY F9 {#t+ xp_tracker;score}

#BUTTON 1 {%format("%.n",@xplvl)  (@xpprocent%)} {} {} {} {} {} {} {Size} {109} {16} {Pos} {1} {886} {4} {} {} {}

#BUTTON 2 {%format("%.n",@xprun) / %format("%.n",@coinsrun)} {} {} {} {} {} {} {Size} {109} {16} {Pos} {17} {886} {4} {} {} {}

#TRIGGER {^You have (%d) unused experience points.} {#math xprun %1-@xptotal;#var xptotal %1;#math xpprocent %1/(@tlevel/100);#math xplvl @tlevel-%1;#t- xp_tracker} {xp_tracker} 548

#TRIGGER {^You have (%d) gold coins.} {#math coinsrun %1-@coinstotal;#var coinstotal %1} {xp_tracker} 548

#VAR tlevel {2100000000}

[/code:374y941w]

</div>

<div class="post" data-post-id="903" data-author="Elwood" data-date="2004-07-01T17:47:24+00:00" data-subject="">

what client is that for lei ?

</div>

<div class="post" data-post-id="906" data-author="Leizu" data-date="2004-07-02T02:07:17+00:00" data-subject="">

this one was written for zmud 4.62 I posted it here because it could be very fast adapted for wintin. So I thought it could be useful.

if you have any questions feel free to ask

</div>

<div class="post" data-post-id="1571" data-author="Qa" data-date="2004-08-24T19:02:28+00:00" data-subject="">

Please note that the code I posted below does not work with ".NET"  (Whatever the hell that crap is.)

Frankly, I switched to jmc several years ago.  At that time this code made the migration from Wintin (1.73) to jmc without modification.  I am currently running jmc 3.0, and the code works as is.

-Qa

</div>
