---
title: "Sanctuary Watcher .NET"
topic_id: 1587
author: "jezer"
date: 2005-12-07T10:56:47+00:00
last_activity: 2006-03-10T17:20:18+00:00
last_author: "Avatar"
sticky: false
locked: false
post_count: 6
---

<div class="post" data-post-id="9744" data-author="jezer" data-date="2005-12-07T10:56:47+00:00">

Ok, after gripping a tough mob only to have my sanctuary fall the very next millisecond... and then dying... I decided it was time to write a sanctuary script for wintin.net. I have seen avatars with them before but the script is not posted anywhere I have found. So if you have a better script by all means post it!!!

#defgroup {Sanctuary}

#action  {The 'sanctuary' spell on you is about to wear off.} {$output 60 SECS ON SANCT!} {G|Sanctuary}

#action  {The white aura around your body fades.} {#var sanct 0;$output SANCT DOWN!} {G|Sanctuary}

#action  {You start glowing.} {#timer Sanct +$time {$output SANCT WARNING!};$output SANCT UP!;#var sanct 1} {G|Sanctuary}

#alias  {sanct} {#if {$sanct = 0} {cast 'sanctuary' $me}} {G|Sanctuary}

#highlight  {b red} {60 SECS ON SANCT!} {G|Sanctuary}

#highlight  {b red} {SANCT DOWN!} {G|Sanctuary}

#highlight  {b red} {SANCT UP!} {G|Sanctuary}

#highlight  {b red} {SANCT WARNING!} {G|Sanctuary}

#variable  {output} {grouptell} {G|Sanctuary}

#variable  {sanct} {0} {G|Sanctuary}

#variable  {time} {3:30} {G|Sanctuary}

#variable  {me} {jezer} {G|Sanctuary}

#defgroup {}

Set the variable me to your player name.

By default the reports are outted to "grouptell". So group urself even if you are solo OR change the output variabe to say or what ever else, otherwise you might not see the warnings!

Using this script will return a sanctuary warning 3 mins and 30 secs into your sanctuary spell. 

If your spellcraft just happens to kick in properly - which you can't count on, it will warn you when you have 60 secs left. 

Using the command "sanct" to sanct yourself will also set a variable stopping you from re-casting it on urself before it drops.

Enjoy,

Jezer

</div>

<div class="post" data-post-id="9745" data-author="jezer" data-date="2005-12-07T13:35:42+00:00">

Small update, bigger eye-catching descriptions and some gags so you don't get double reports.

#defgroup {Sanctuary}

#action  {The 'sanctuary' spell on you is about to wear off.} {$output 60 SECS ON SANCTUARY!} {G|Sanctuary}

#action  {The white aura around your body fades.} {#var sanct 0;$output SANCTUARY DOWN!} {G|Sanctuary}

#action  {You start glowing.} {#timer Sanct +$satime {$output SANCTUARY WARNING!};$output SANCTUARY UP!;#var sanct 1} {G|Sanctuary}

#alias  {sanct} {#if {$sanct = 0} {cast 'sanctuary' $me}} {G|Sanctuary}

#gag  {The 'sanctuary' spell on you is about to wear off.} {G|Sanctuary}

#gag  {The white aura around your body fades.} {G|Sanctuary}

#gag  {You start glowing.} {G|Sanctuary}

#highlight  {b red} {60 SECS ON SANCTUARY!} {G|Sanctuary}

#highlight  {b red} {SANCTUARY DOWN!} {G|Sanctuary}

#highlight  {b red} {SANCTUARY UP!} {G|Sanctuary}

#highlight  {b red} {SANCTUARY WARNING!} {G|Sanctuary}

#variable  {sanct} {1} {G|Sanctuary}

#variable  {satime} {3:30} {G|Sanctuary}

#variable  {me} {jezer} {G|Shortcuts}

#variable  {output} {grouptell} {G|Shortcuts}

#defgroup {}

</div>

<div class="post" data-post-id="10836" data-author="*juggleblood*" data-date="2006-02-22T11:16:28+00:00">

Isn't there a way to make a countdown timer in Wintin that displays in a separate panel and actually counts down the seconds like a clock?

</div>

<div class="post" data-post-id="10837" data-author="Rynquald" data-date="2006-02-22T11:47:22+00:00">

This would require some tweaking to work with Jezer's script, but here's a quick and dirty visual timer for the last 60 seconds of sanc, you could alter it to countdown from the start of sanc of course, but that would assume sanc wasn't affected by masterfulls. Of course doing that would only necessitate the alteration of the 'sanctick' timer to 3 ticks or whatever, and the 'sanctime' variable to 180.

[code:2x47kynz]#action {The 'sanctuary' spell on you is about to wear off.} {#var {sanctime} {60};#timer {sanctick} {+0:1:0} {#untimer {sanctime};grouptell SANCTUARY DOWN!};#timer {sanctime} {*1} {#math {sanctime} {$sanctime-1}}}

#pvar {1} {sanctime}[/code:2x47kynz]

That displays in pvar 1 just as an example (plus as I write this it's the middle of the night and I'm not ingame to test, so it's not polished in any way shape or form) :)

</div>

<div class="post" data-post-id="11128" data-author="*juggleblood*" data-date="2006-03-09T20:01:46+00:00">

Here is a complete script for ne1 who wants it.

It starts counting down based on a duration of 280 seconds which is the average sanc duration. Then it switches to 60 when it gets the warning.

The command sanctell sets the output to grouptell, say, #showme, whatever.

#defgroup sanctuary

#action  {The 'sanctuary' spell on you is about to wear off.} {#var sancstart $time;#var sancduration {60}} {G|sanctuary}

#action  {The white aura around your body fades.} {$sancoutput SANCTUARY DOWN!;#panel 3 unlit;#untimer sanctime;#unpvar 4} {G|sanctuary}

#action  {You start glowing.} {#var sancstart $time;#var sancduration {280};#timer sanctime {*:*:*2} {checksanc};#panel 3 {Sanc Up};#pvar 4 sancremain} {G|sanctuary}

#alias  {checksanc} {#math sanctime {$time-$sancstart};#math sancremain {$sancduration-$sanctime}} {G|sanctuary}

#alias  {sanctell} {#var {sancoutput} {%0}}

</div>

<div class="post" data-post-id="11153" data-author="Avatar" data-date="2006-03-10T17:20:18+00:00">

That's a nice solution Juggleblood.  Good job!

Regards,

Charles

</div>
