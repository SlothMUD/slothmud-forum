---
title: "Protect Down"
topic_id: 1676
author: "*juggleblood*"
date: 2006-01-22T14:11:13+00:00
last_activity: 2006-02-01T21:04:33+00:00
last_author: "*juggleblood*"
sticky: false
locked: false
post_count: 3
---

<div class="post" data-post-id="10285" data-author="*juggleblood*" data-date="2006-01-22T14:11:13+00:00">

This will automatically protect down and will also protect over your protectee if he or she dies.

#defgroup {protect down}

#action  {^$protectee is dead} {#remkey grouplist $protectee;protdown;grouptell $protectee is dead-----------------------------------I will protect over.} {G|protect down}

#action  {consists of:} {#capture {groupcapture}{<%0hp};#match grouplist groupcapture {%0 [} {%0}} {G|protect down}

#alias  {protdown} {group;#var f 0;#loop {$grouplist} {#if {$f=1}{prot %%0;#var f 0;#showme I should be protecting %%0;#var protectee %%0};#if {[%%0]=[Rub]}{#var f 1}}} {G|protect down}

Cheers,

Jugg

</div>

<div class="post" data-post-id="10286" data-author="*juggleblood*" data-date="2006-01-22T14:15:19+00:00">

:? Oh yeah...

Don't forget to put your name in place of 'Rub' in the above script.

</div>

<div class="post" data-post-id="10527" data-author="*juggleblood*" data-date="2006-02-01T21:04:33+00:00">

Problem: the client substitutes the grouplist before it has finished capturing and reformatting it. 

Solution: add a 1 second timer after the groupcapture sequence 

;#timer x +1 {<protecteefigureouter sequence>}

</div>
