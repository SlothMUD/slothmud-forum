---
title: "Stabber Wintin.Net"
topic_id: 761
author: "*Splork*"
date: 2005-01-20T20:44:47+00:00
last_activity: 2005-01-20T20:44:47+00:00
last_author: "*Splork*"
sticky: false
locked: false
post_count: 1
---

<div class="post" data-post-id="3852" data-author="*Splork*" data-date="2005-01-20T20:44:47+00:00">

Please change strings if you use this....

#defgroup Stabber

#alias  {astof} {gt AUTO-STAB on follow $leader DISABLED;#unac {^You follow $leader.};#unac {>You follow $leader.}} {G|Stabber}

#alias  {aston} {gt AUTO-STAB on follow $leader ENABLED;#ac {^You follow $leader.} {bc};#ac {>You follow $leader.} {bc}} {G|Stabber}

#alias  {b} {backstab} {G|Stabber}

#alias  {bser} {#var stb $1;#showme --------------------------------;#showme STABBER SET TO: <*- $1 -*>;#cr} {G|Stabber}

#alias  {bsme} {#ac {%0 hates your Guts!} {#unvar target};#var stb Pal;aston;ltton;qston;gt I will now stab when $leader gt's: qstab} {G|Stabber}

#alias  {bsof} {#unac {%0 hates your Guts!};astof;lttof;qstof;gt I will no longer stab when $leader gt's: qstab} {G|Stabber}

#alias  {qston} {#ac {^$leader -- '%0qstab'} {bc}} {G|Stabber}

#alias  {gripoff} {gt AUTO-GRIP on follow $leader DISABLED;#unac {^You follow $leader.};#unac {>You follow $leader.}} {G|Stabber}

#alias  {gripon} {gt AUTO-GRIP on follow $leader ENABLED;#ac {^You follow $leader.} {dtt};#ac {>You follow $leader.} {dtt}} {G|Stabber}

#alias  {go} {gt I R stab $target NOW!!;bf} {G|Stabber}

#alias  {bf} {bac $target;fw} {G|Stabber}

#alias  {qstof} {#unac {^$leader -- '%0qstab'}} {G|Stabber}

#alias  {bc} {bac $target} {G|Stabber}

#alias  {lp} {last player} {G|Stabber}

#alias  {lt} {look $target} {G|Stabber}

#alias  {lt4} {#ac {^$leader -- '%0target %1'} {#var target $1;#show **********=====>>>>> TARGET:[ $1 ] <<<<<=====**********}} {G|Stabber}

#alias  {ltarof} {#unac {^$leader -- '%0target %1'};#unac {^$leader -- ' TARGET: %1'};#unac {^$leader -- '%0Target: %1'}} {G|Stabber}

#alias  {ltaron} {ltaron1;ltaron2;ltaron3} {G|Stabber}

#alias  {ltaron1} {#ac {^$leader -- '%0target %1'} {#var target $1;gt Target accepted: $1}} {G|Stabber}

#alias  {ltaron2} {#ac {^$leader -- ' TARGET: %1'} {#var target $1;gt Target accepted: $1}} {G|Stabber}

#alias  {ltaron3} {#ac {^$leader -- '%0Target: %1'} {#var target $1;gt Target accepted: $1}} {G|Stabber}

#alias  {ltaron4} {#ac {^$leader -- '%0target %1'} {#var target $1;#show *****=====>>>>> TARGET:[ $1 ]}} {G|Stabber}

#alias  {lttof} {gt I will set my own targets now;ltarof} {G|Stabber}

#alias  {ltton} {gt $leader is now able to set my targets;ltaron} {G|Stabber}

</div>
