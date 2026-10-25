---
title: "Time to Next Tick Display -NET"
topic_id: 1761
author: "*juggleblood*"
date: 2006-03-03T14:12:58+00:00
last_activity: 2006-03-04T20:42:11+00:00
last_author: "Weasel"
sticky: false
locked: false
post_count: 9
---

<div class="post" data-post-id="11028" data-author="*juggleblood*" data-date="2006-03-03T14:12:58+00:00" data-subject="Time to Next Tick Display -NET">

This will make a counter at the lower right of your wintin terminal that counts down the seconds until the tick.

This is useful for making spell counters because the variable time2next updates every 2 seconds, so you can make sanc counters that are completely accurate, which I will post next by the way.

#defgroup ticker

#nop These help keep it accurate...you probably want to add more

#action  {^It starts to rain} {#tickset} {G|ticker}

#action  {^The day has begun} {tickset} {G|ticker}

#action  {^The eastern sky starts to brighten} {tickset} {G|ticker}

#action  {^Your fly spell just} {tickset} {G|ticker}

#alias  {subtick} {#math {timesincetick} {$timesincetick-60};tickcheck} {G|ticker}

#alias  {tick} {timesincetick;tickcheck} {G|ticker}

#alias  {tickcheck} {#if {$timesincetick>59}{subtick} else {#math {time2next} {60-$timesincetick}}} {G|ticker}

#alias  {tickrep} {tick;#showme  {Next tick in $time2next seconds}} {G|ticker}

#alias  {tickset} {#var lastticktime $time} {G|ticker}

#alias  {timesincetick} {#math timesincetick {$time-$lastticktime}} {G|ticker}

#timer {ticker} {*:*:*2} {tick} {G|ticker}

#panel 1 {Time to Tick}

#pvar 2 time2next

</div>

<div class="post" data-post-id="11030" data-author="*juggleblood*" data-date="2006-03-03T15:07:03+00:00" data-subject="correction">

Make this correction

#al {tickcheck} {#if {$timesincetick>59}{subtick} else {#math {time2next} {60-$timesincetick}[b:3rci5p5b];#if {$time2next=60}{tickset}[/b:3rci5p5b]}

and add these

#al tickstop {#untimer ticker}

#al tickstart {#timer ticker {*:*:*2} {tick}}

*don't forget to add more triggers to automatically set the tick, for example, weather, daylight, spells ending, etc.. Just don't use hunger or thirst because they display in your score.

Cheers

</div>

<div class="post" data-post-id="11043" data-author="Krok" data-date="2006-03-03T21:33:58+00:00" data-subject="">

TICK IN 10!!! CATCH!!

</div>

<div class="post" data-post-id="11061" data-author="*juggleblood*" data-date="2006-03-04T17:32:37+00:00" data-subject="">

Ok... I was learned a few things, such as:

1. spells don't end on tick...don't trigger them to tickset

2. sanc has a variable duration...counter past 1 min is useless

Question:

Is there even any point to a tickcounter nemore since you gain hp during the miniticks?

</div>

<div class="post" data-post-id="11062" data-author="Weasel" data-date="2006-03-04T17:43:35+00:00" data-subject="">

mobs still operate on the tick system, so it's good for knowing when repops will occur and also I guess can be used to start killing a mob just after a tick so it doesn't get bonus hp midway through fight if another tick lapses...

</div>

<div class="post" data-post-id="11063" data-author="*Splork*" data-date="2006-03-04T18:25:09+00:00" data-subject="">

Actually mob actions no longer work according to the old tick system. Mob actions are mostly random now...

Enjoy,

Splork

</div>

<div class="post" data-post-id="11064" data-author="12345" data-date="2006-03-04T19:34:32+00:00" data-subject="">

The mini ticks were designed to make ticks useless, yes.  A real quick search of my memory seems to think that boats still come and go on actual ticks.  Don't recall if areas repop on ticks or not.  The game operates on about 6 different tick systems though, so trying to wrap your head around everything is pretty difficult.

The messages that say whatever spell is about to fall is your best measurement.  If it didn't fail occasionally, it'd be perfect.

</div>

<div class="post" data-post-id="11065" data-author="Weasel" data-date="2006-03-04T20:38:53+00:00" data-subject="">

Actually mob actions no longer work according to the old tick system. Mob actions are mostly random now...

Enjoy,

Splork[/quote:36r0lan2]

oop ok, thanks for the info.. guess my tick counter is completely useless now :)

I have a heap of tick message triggers like weather and area sounds etc.. deleting all those will cut out about half of my triggers hehe.

</div>

<div class="post" data-post-id="11066" data-author="Weasel" data-date="2006-03-04T20:42:11+00:00" data-subject="">

hmm.. but still useful for mob pingers, yes? Are repop times still tick based along with weather, sunrise etc? ..or at least repop duration constant within an area..

</div>
