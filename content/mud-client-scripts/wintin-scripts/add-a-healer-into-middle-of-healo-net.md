---
title: "Add a healer into middle of Healo .Net"
topic_id: 1699
author: "*juggleblood*"
date: 2006-01-30T18:05:39+00:00
last_activity: 2006-01-30T18:05:39+00:00
last_author: "*juggleblood*"
sticky: false
locked: false
post_count: 1
---

<div class="post" data-post-id="10435" data-author="*juggleblood*" data-date="2006-01-30T18:05:39+00:00" data-subject="Add a healer into middle of Healo .Net">

Usage:

add <new healer's name>

addafter <previous healer's name>

Script:

#alias  {add} {#var newhealer %0} 

#alias  {addafter} {#loop {$healo}{#if {[%%0]=[%%%0]}{#showme found %%%0;#push healotemp $$$0, $newhealer} else {#push healotemp %%0}};#loop {$@healo}{#cr};#loop {$@healotemp}{#push healo %0};#showme {Healo is now $healo}} 

I think u need to make a null variable for healotemp first tho b4 u start using it.

#var healotemp

Its kind of ugly, but it works well.

Cheers

</div>
