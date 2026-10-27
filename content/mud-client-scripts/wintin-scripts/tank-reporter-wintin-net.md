---
title: "Tank Reporter Wintin.NET"
topic_id: 760
author: "*Splork*"
date: 2005-01-20T20:43:44+00:00
last_activity: 2005-12-21T03:57:46+00:00
last_author: "jezer"
sticky: false
locked: false
post_count: 2
---

<div class="post" data-post-id="3851" data-author="*Splork*" data-date="2005-01-20T20:43:44+00:00" data-subject="Tank Reporter Wintin.NET">

Please change strings if you use this...

\#defgroup Tank-Reporter

\#alias {checkwhine} {#if {$hpdelta \< -10} {grep2};#if {$hpdelta \>30} {grep3}} {G\|Tank-Reporter}

\#alias {gt2} {grouptell} {G\|Tank-Reporter} 

\#alias {gt3} {grouptell} {G\|Tank-Reporter} 

\#alias {grep} {gt $me: Hp [ $hp / $maxhp ] \& Ma [$ma/$maxma]} {G\|Tank-Reporter}

\#alias {grep2} {gt2 \<\<: \\\\c09$hpdelta HP\\\\c12 :\>\> HP: [ $hp / $maxhp ] } {G\|Tank-Reporter}

\#alias {grep3} {gt2 \<\<: \\\\c15+$hpdelta HP\\\\c12 :\>\> HP: [ $hp / $maxhp ] } {G\|Tank-Reporter}

\#alias {metank} {gt Prepare to die, I'm gonna tank this now...;#var tank $me;rescallon;whinet} {G\|Tank-Reporter}

\#alias {tankt} {#var tank $1;gt \<\*- $1 -\*\> is gonna get hoyt.} {G\|Tank-Reporter}

\#alias {tarepof} {gt TANK-Reporter: \*\* DISABLED \*\*;#unac {$tank [Lvl %1 Hp %2 Mana %3]}} {G\|Tank-Reporter}

\#alias {tarepon} {gt TANK-Reporter: \*\* ENABLED \*\*;#ac {$tank [Lvl %1 Hp %2 Mana %3]} {gt TANK: $tank with [$2/$tankmax] HP \& [$3] MA}} {G\|Tank-Reporter}

\#alias {whineof} {gt I won't whine anymore when I get hit.;#unac {^\<%0hp %1ma %2mv}} {G\|Tank-Reporter}

\#alias {whineof2} {gt I won't whine anymore when I get hit.;#ac {^\<%0hp %1ma %2mv} {#var hp $0;#var ma $1;#var mv $2} }} {G\|Tank-Reporter}

\#alias {whineron} {#ac {^\<%0hp %1ma %2mv} {#var hp $0;#var ma $1;#var mv $2;#math {hpdelta} {$$0-$$hp};#if {$$0\<$$hp} {checkwhine};#if {$$0\>$$hp} {checkwhine}}} {G\|Tank-Reporter}

\#alias {whinet} {gt I will now tell you when them mobs whack me;whineron} {G\|Tank-Reporter}

\#alias {maxh} {#var maxhp $1;#showme ---------------------------------;#showme SETTING MY HP's TO \<\<: $1 :\>\>;#cr} {G\|Tank-Reporter}

\#alias {maxm} {#var maxma $1;#showme ---------------------------------;#showme SETTING MY MANA TO \<\<: $1 :\>\>;#cr} {G\|Tank-Reporter}

\#variable {hp} {715} {G\|Tank-Reporter}

\#variable {ma} {768} {G\|Tank-Reporter}

\#variable {mv} {190} {G\|Tank-Reporter}

\#variable {hpdelta} {0} {G\|Tank-Reporter}

\#variable {maxhp} {1445} {G\|Tank-Reporter}

To enable the script, simply type metank charactername... If I remember right:-)

</div>

<div class="post" data-post-id="9899" data-author="jezer" data-date="2005-12-21T03:57:46+00:00" data-subject="">

I was going to make my own whiner, but on more careful study of Splork's I realised just how good his actually was! However Splork's whiner incapsulated a whole bunch of things I didn't like or use, with the tank and rescue concept, so here is a mod of Splork's script that acts just as a plain old whiner. 

whineron to start

whineroff to end

\#defgroup {Whiner}

\#alias {checkwhine} {#if {$hpdelta \< -10} {grep2};#if {$hpdelta \>30} {grep3}} {G\|Whiner}

\#alias {grep2} {gt \<\<: \\\\c09$hpdelta HP\\\\c12 :\>\> HP: [ $hp / $maxhp ] } {G\|Whiner}

\#alias {grep3} {gt \<\<: \\\\c15+$hpdelta HP\\\\c12 :\>\> HP: [ $hp / $maxhp ] } {G\|Whiner}

\#alias {maxh} {#var maxhp $1;#showme ---------------------------------;#showme SETTING MY HP's TO \<\<: $1 :\>\>;#cr} {G\|Whiner}

\#alias {maxm} {#var maxma $1;#showme ---------------------------------;#showme SETTING MY MANA TO \<\<: $1 :\>\>;#cr} {G\|Whiner}

\#alias {whineroff} {gt WHINER OFF!;#unac {^\<%0hp %1ma %2mv}} {G\|Whiner}

\#alias {whineron} {gt WHINER ON!;#ac {^\<%0hp %1ma %2mv} {#var hp $0;#var ma $1;#var mv $2;#math {hpdelta} {$$0-$$hp};#if {$$0\<$$hp} {checkwhine};#if {$$0\>$$hp} {checkwhine}}} {G\|Whiner}

\#variable {hp} {873} {G\|Whiner}

\#variable {hpdelta} {0} {G\|Whiner}

\#variable {ma} {147} {G\|Whiner}

\#variable {maxhp} {888} {G\|Whiner}

\#variable {mv} {258} {G\|Whiner}

\#defgroup {}

</div>
