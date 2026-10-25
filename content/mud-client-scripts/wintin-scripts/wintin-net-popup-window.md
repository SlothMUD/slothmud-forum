---
title: "Wintin.net popup window"
topic_id: 3026
author: "Virus"
date: 2009-02-03T02:46:16+00:00
last_activity: 2009-02-03T13:46:58+00:00
last_author: "Virus"
sticky: false
locked: false
post_count: 3
---

<div class="post" data-post-id="27973" data-author="Virus" data-date="2009-02-03T02:46:16+00:00">

Anyone have idea how to do something like "other" window in this screenshot: ![](http://www.wintin.org/Portals/0/screen10.JPG ?)

</div>

<div class="post" data-post-id="27974" data-author="*Splork*" data-date="2009-02-03T03:14:25+00:00">

All of the code is not here but I dont have time to go through my entire script. That is the way annie and my wintin looks. You should be able to get a good idea of the code from the below;

#popup {Other} {OtherWindow}

#clearwin {Other}

#defgroup {}

#nop

#nop *** Other **********************************************************************************************************************************************

#nop

#defgroup {040Other}

#alias {other}   {#clearwin {Other};#loop {1,22} {other%0}}

#alias {other1}  {#sendtowin Other ###################################################}

#alias {other2}  {#sendtowin Other Character      : $me}

#alias {other3}  {#sendtowin Other ###################################################}

#alias {other4}  {#sendtowin Other Leader         : $leader}

#alias {other5}  {#sendtowin Other Tank           : $tank}

#alias {other6}  {#sendtowin Other 2.Tank         : $tankdos}

#alias {other7}  {#sendtowin Other Warcrier       : $warcrier}

#alias {other8}  {#sendtowin Other Stabber        : $stabber}

#alias {other9}  {#sendtowin Other ###################################################}

#alias {other10} {#sendtowin Other Target         : $target}

#alias {other11} {#sendtowin Other ###################################################}

#alias {other12} {#sendtowin Other AutoLoot       : $autoloot     Solo    : $autosolo}

#alias {other13} {#sendtowin Other AutoLoot Money : $automoney     Grouped : $autogrouped}

#alias {other14} {#sendtowin Other AutoInfuse     : $autoinfuse}

#alias {other15} {#sendtowin Other AutoSac        : $autosac}

#alias {other16} {#sendtowin Other AutoSplit      : $autosplit}

#alias {other17} {#sendtowin Other ###################################################}

#alias {other18} {#sendtowin Other Gear           : $gear}

#alias {other19} {#sendtowin Other Weapon         : $weapon}

#alias {other20} {#sendtowin Other ###################################################}

#alias {other21} {#sendtowin Other Beacon         : $beacon}

#alias {other22} {#sendtowin Other ###################################################}

#defgroup {}

#nop

#nop *** Beacon Tracker *************************************************************************************************************************************

#nop

#defgroup {060BeaconTracker}

#var {beacon} {---}

#action {^Beacon set.} {#action {^$me%0- %1} {#unaction {^$me%0- %1};#var {beacon} {$$1};other};where $me}}

#action {^You activate your beacon!} {#var {beacon} {---};other}

#alias {beacon} {#showme Beacon set at : [$beacon]}

#nop

#nop *** Looter *********************************************************************************************************************************************

#nop

#defgroup {070Looter}

#var {autosolo} {1}

#var {autogrouped} {0}

#var {autoloot} {1}

#var {automoney} {0}

#var {autoinfuse} {0}

#var {autosac} {1}

#var {autosplit} {0}

#action {^Total exp for kill is %0.} {#if {$autosolo && $autoloot} {get all corpse};#if {$autosolo && $automoney} {get coins corpse};save}

#action {^You received %0 experience points.} {#if {$autoloot} {get all corpse};#if {$automoney} {get coins corpse};save}

#action {^You receive %0 experience points as your share.} {#if {$autogrouped && $autoloot} {get all corpse};#if {$autogrouped && $automoney} {get coins corpse};save}

#action {^Everything %0 was carrying suddenly drops to the ground.} {#if {$autoloot} {get all};#if {$automoney} {get coins};save}

#action {^There were %0 coins.} {#if {$autosplit} {lsplit $$0}}

#action {^You do not see anything in the corpse.} {#if {$autoinfuse} {cast 'infuse' corpse;give soul $tank};#if {$autosac} {sac corpse}}

#alias {+auto} {+autoloot;+autosac}

#alias {-auto} {-autoloot;-automoney;-autoinfuse;-autosac;-autosplit}

#alias {+solo} {#var {autosolo} {1};#var {autogrouped} {0}}

#alias {+group} {#var {autosolo} {0};#var {autogrouped} {1}}

#alias {+autoloot} {autoloot on;#var {autoloot} {1};-automoney;other}

#alias {-autoloot} {autoloot off;#var {autoloot} {0};other}

#alias {+automoney} {#var {automoney} {1};-autoloot;other}

#alias {-automoney} {#var {automoney} {0};other}

#alias {+autoinfuse} {#var {autoinfuse} {1};-autosac;other}

#alias {-autoinfuse} {#var {autoinfuse} {0};other}

#alias {+autosac} {#var {autosac} {1};-autoinfuse;other}

#alias {-autosac} {#var {autosac} {0};other}

#alias {+autosplit} {#var {autosplit} {1};other}

#alias {-autosplit} {#var {autosplit} {0};other}

#nop

#nop *** Identification *************************************************************************************************************************************

#nop

#defgroup {010Identification}

#variable  {me} {Annie}

#defgroup {110Group}

#var {leader} {Annie}

#alias {setleader} {#var {leader} {$$0};grouptell \\a02\\d07[Group report]\\a10\\c02 Setting leader to $0 ...;other}

#var {tank} {Annie}

#alias {settank} {#var {tank} {$$0};grouptell \\a02\\d07[Group report]\\a10\\c02 Setting tank to $0 ...;other}

#var {tanksancer} {Annie}

#alias {settanksancer} {#var {tanksancer} {$$0};grouptell \\a02\\d07[Group report]\\a10\\c02 Setting tank sancer to $0 ...}

#var {tankdos} {Annie}

#alias {settankdos} {#var {tankdos} {$$0};grouptell \\a02\\d07[Group report]\\a10\\c02 Setting secondary tank to $0 ...;other}

#var {warcrier} {Annie}

#alias {setwarcrier} {#var {warcrier} {$$0};grouptell \\a02\\d07[Group report]\\a10\\c02 Setting warcrier to $0 ...;other}

#var {stabber} {Annie}

#alias {setstabber} {#var {stabber} {$$0};grouptell \\a02\\d07[Group report]\\a10\\c02 Setting stabber to $0 ...}

#var {stabbersancer} {Annie}

#alias {setstabbersancer} {#var {stabbersancer} {$$0};grouptell \\a02\\d07[Group report]\\a10\\c02 Setting stabber sancer to $0 ...;other}

</div>

<div class="post" data-post-id="27975" data-author="Virus" data-date="2009-02-03T13:46:58+00:00">

Cool, thanks much I'll give it a try  :D

</div>
