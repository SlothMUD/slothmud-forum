---
title: "Wanting to Learn"
topic_id: 257
author: "Gippal"
date: 2004-07-05T15:49:53+00:00
last_activity: 2004-07-08T06:24:33+00:00
last_author: "Gippal"
sticky: false
locked: false
post_count: 6
---

<div class="post" data-post-id="931" data-author="Gippal" data-date="2004-07-05T15:49:53+00:00" data-subject="Wanting to Learn">

I know how to do most of the action and alias np; however I was wondering if there is a good site or even books to teach me how to do more of the math requirements of a whiner or anything else that might require math in it.  When telling me a site remember that I am a dummy.  The wintin site didn't help me at all on these items (so dummy is an understatement).  I don't just want someone to tell me.  I really want to learn because I believe it might help me become a better player.  Thanks for any iformation you give.

</div>

<div class="post" data-post-id="934" data-author="Weasel" data-date="2004-07-05T17:19:58+00:00" data-subject="">

I don't use wintin so can't really help you there, but I'll make a suggestion. The way I learned much of the stuff on my client is by looking at as many other scripts as I could and then try changing things around in them and seeing what effect they have to get an understanding of how the script works. It seemed to work reasonably well for me anyway.  :D

</div>

<div class="post" data-post-id="940" data-author="Calim" data-date="2004-07-06T03:45:01+00:00" data-subject="">

Most whiners work off a simple premise.  It uses the games prompt of <xhp ... etc.  So you set that x to a some variable like say currentHps.  A simple action that reacts on the prompt and sets that value to a variable would be a good first step for a true wintin newbie.  After you have that, you use the same action to first set currentHps to a new variable: oldHps, then set currentHps to the x value from the prompt.  Now its just a matter of subtracting old from current, figure out if that's good news or bad news, and report if you need to.

</div>

<div class="post" data-post-id="945" data-author="Qa" data-date="2004-07-06T14:21:04+00:00" data-subject="">

Ok, I use JMC rather than wintin, but most scripts are fairly interchangable.  While this isn't the best whiner in the mud, it has worked for me on those rare times you want a caster/caster tank. 

It has a few features: it will continually report gains/losses to you through the show command.  It will automatically pick up your maximum hp if you are over 2x40.  (Tweak that action for under 2x40.)  Adjust it however you want it.

To turn it on type 'tankrepon'.  Off is (duh) 'tankrepoff'.  To turn off everything: mereportoff.  -Qa

#nop

#nop

#nop  Tank Reporter (Whiner)

#nop

#variable {oldhit} {0}

#variable {maxhit} {862}

#variable {hit} {0}  

#variable {mana} {0}

#variable {moves} {0}

#variable {oldmana} {0}

#variable {tankrep} {1}

#variable {grouptankrep} {0}

#action {^<%1hp %2ma %3mv} {setval %1 %2} {0}

#alias setval {#math hit %1 ; #math oldhit $hit ; #math mana %2 ; #math oldmana $mana; #math moves %3 ; #if {$tankrep=1} tankreport}

#action {^You have (%0/%1+} {#math {maxhit} $1}

#alias tankrepoff {#math grouptankrep 0}

#alias tankrepon {#math grouptankrep 1}

#alias mereportoff {#math tankrep 0}

#alias tankreport {#if {$hit < $oldhit} {#math change {$oldhit - $hit} ; tankloss} ;  #if {$hit > $oldhit} {#math change {$hit - $oldhit} ; tankgain}}

#alias tankloss {#showme  -------LOSS------- -$change; #if {$grouptankrep=1} {grouptell Ouch!  $hit ($maxhit) ------ LOSS: -$change ------}}

#alias tankgain {#if {$change>5} {#showme +++++++Gain+++++++ +$change; #if {$grouptankrep=1} {grouptell Oh, yeah.  $hit ($maxhit) ++++++ GAIN: +$change ++++++}}}

</div>

<div class="post" data-post-id="946" data-author="Calim" data-date="2004-07-06T16:16:09+00:00" data-subject="">

#defgroup {tank whiner}

#action  {^<%1hp %2ma %3mv>} {rep1 $1 $2 $3} {G|tank whiner}

#alias  {rep1} {#var hpc %1;#var mac %2;#var mvc %3;#pvar 1 hpc;#pvar 2 mac;rep2} {G|tank whiner}

#alias  {rep2} {#math hpdelta {$$hpc-$$hpold};#math madelta {$$mac-$$maold};#math {hpneed} {$$hpm-$$hpc};rep4} {G|tank whiner}

#alias  {rep4} {#if {$$hpdelta>35} {$report That's Better - HP: [$hpc / $hpm]  (\\d06+$hpdelta\\a01) -> NEED(\\d06$$hpneed\\a01);rep6} else {rep5}} {G|tank whiner}

#alias  {rep5} {#if {$$hpdelta<-25} {$report OW! quit it. HP: [$hpc / $hpm]  (\\d02$hpdelta\\a01) -> NEED(\\d02$$hpneed\\a01);rep6} else {rep6}} {G|tank whiner}

#alias  {rep6} {#var hpold $hpc;#var maold $mac} {G|tank whiner}

#alias  {roff} {#var report #showme} {G|tank whiner}

#alias  {ron} {#var report grouptell} {G|tank whiner}

#alias  {tankme} {ron; gt I will now cry like a baby when I get HIT;parry;rescon} {G|tank whiner}

#alias  {res} {rescue $stabber} {G|tank whiner}

#alias  {stabber} {#variable stabber $0} {G|tank whiner}

#alias  {tm} {tankme} {G|tank whiner}

#variable  {hpc} {640} {G|tank whiner}

#variable  {hpm} {1023} {G|tank whiner}

#variable  {hpold} {640} {G|tank whiner}

#variable  {mac} {34} {G|tank whiner}

#variable  {maold} {34} {G|tank whiner}

#variable  {mvc} {178} {G|tank whiner}

#variable  {report} {#showme} {G|tank whiner}

#variable  {hpdelta} {2} {G|tank whiner}

#variable  {madelta} {0} {G|tank whiner}

#variable  {hpneed} {383} {G|tank whiner}

#defgroup {}

This is mine for wintin.net, modified from something Plato posted to the old crier, and tweaked for ingame colors.  Red for pain, purple for heals.  Tweaked also for the change in tick so that I am not reporting every change, only pain greater then 25 and heals greater then 35.  

The report variable switches between #showme and grouptell using ron and roff alias.  

I also added the hpneed variable.  I think this is the most important thing for a whiner.  Healers don't have to do the math in their head, they can just look at that and decide if it is time for them to cast on you.

in the tankme alias, I call rescon, which turns on my auto rescuer.  The mana calculations are also useless to me.

</div>

<div class="post" data-post-id="984" data-author="Gippal" data-date="2004-07-08T06:24:33+00:00" data-subject="">

<P>Thanks for all the advice and help!</P>

</div>
