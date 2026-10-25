---
title: "Stone Skin Watcher .NET"
topic_id: 1588
author: "jezer"
date: 2005-12-07T13:40:15+00:00
last_activity: 2005-12-07T13:40:15+00:00
last_author: "jezer"
sticky: false
locked: false
post_count: 1
---

<div class="post" data-post-id="9746" data-author="jezer" data-date="2005-12-07T13:40:15+00:00">

#defgroup {Stoneskin}

#action  {The 'stone skin' spell on you is about to wear off.} {$output 60 SECS ON STONE SKIN!} {G|Stoneskin}

#action  {You feel less protected.} {#var stone 0;$output STONE SKIN DOWN!} {G|Stoneskin}

#action  {You feel your skin become much, much stronger.} {#timer Stone +$sstime {$output STONE SKIN WARNING!};$output STONE SKIN UP!;#var stone 1} {G|Stoneskin}

#alias  {stone} {#if {$stone = 0} {cast 'stone' $me}} {G|Stoneskin}

#gag  {The 'stone skin' spell on you is about to wear off.} {G|Stoneskin}

#gag  {You feel less protected.} {G|Stoneskin}

#gag  {You feel your skin become much, much stronger.} {G|Stoneskin}

#highlight  {b yellow} {60 SECS ON STONE SKIN!} {G|Stoneskin}

#highlight  {b yellow} {STONE SKIN DOWN!} {G|Stoneskin}

#highlight  {b yellow} {STONE SKIN UP!} {G|Stoneskin}

#highlight  {b yellow} {STONE SKIN WARNING!} {G|Stoneskin}

#variable  {stone} {0} {G|Shortcuts}

#variable  {sstime} {22:30} {G|Stoneskin}

#variable  {me} {jezer} {G|Shortcuts}

#variable  {output} {grouptell} {G|Shortcuts}

#defgroup {}

</div>
