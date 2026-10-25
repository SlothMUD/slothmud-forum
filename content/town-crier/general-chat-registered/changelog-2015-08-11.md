---
title: "Changelog 2015-08-11"
topic_id: 4508
author: "*teker*"
date: 2015-08-11T15:23:47+00:00
last_activity: 2015-08-24T17:29:57+00:00
last_author: "Dragoth"
sticky: false
locked: false
post_count: 10
---

<div class="post" data-post-id="36026" data-author="*teker*" data-date="2015-08-11T15:23:47+00:00">

There's a kink in shapeshift after the changes.  I'm trying to track it down.  We've disabled the command for now.

</div>

<div class="post" data-post-id="36027" data-author="Dragoth" data-date="2015-08-11T20:40:03+00:00">

For what its worth, me and a few other people have noticed that with shapeshifting disabled the game is now much more responsive (less input lagg) and feels pretty swift

</div>

<div class="post" data-post-id="36028" data-author="*teker*" data-date="2015-08-12T02:05:08+00:00">

I think it's likely that something else is/was broken that is causing the speed-up but no-one has noticed the bug side of it.  I'm hoping the big guys will reboot again in the morning - I have shapeshift fixed along with being able to use the skills again.

The main reason for today's breakage is that I'm rewriting how the mob procs work to give builders more flexibility in how they make mobs.  Still a bunch of work to do but there's only one more really bad change ahead.

I've fixed the fog spell so that it actually works.  Entering a fog room is now -1 to hit for everyone in the room.  If you leave the room or the spell expires you go back to normal hitroll.  I've also fixed this in a way that builders can add new room effects to modify most player statistics.

I went through the typo list and fixed as many as I could.  Some might not make it in tomorrow - depends on what code gets built.  

The ! (repeat) function has been modified so that you can repeat auction commands (among other things).  The main thing here is that the history is only updated if you enter a command.  Your history no longer gets modified if a god forces you to do something or the game scripts force you to do something else behind the scenes.

</div>

<div class="post" data-post-id="36029" data-author="*Breeze*" data-date="2015-08-12T08:48:38+00:00">

pulled code over..

reboot at 0930 mudtime

*Breeze forces you to 'cross fingers'*

</div>

<div class="post" data-post-id="36030" data-author="*teker*" data-date="2015-08-12T14:17:42+00:00">

Game is back up with full shapeshifting ability restored.

</div>

<div class="post" data-post-id="36045" data-author="*teker*" data-date="2015-08-18T00:46:09+00:00">

We went through and fixed a bunch of broken procs today.  Some of the mobs were complaining about broken brains while others were running with bad parameters.  A lot of them were in rampage procs so if you know a mob that rampages, it may have changed today.

</div>

<div class="post" data-post-id="36048" data-author="*Breeze*" data-date="2015-08-19T02:57:22+00:00">

Moved the portal fix/change from Teker to live machine. (see portals bug thread here <LINK_TEXT text="http://www.slothmud.org/forum/viewtopic ... 13&p=36046">http://www.slothmud.org/forum/viewtopic.php?f=7&t=4513&p=36046</LINK_TEXT> )

Innkeepers (and void fairy) shouldn't charge rent for the first hour after reboot.

(not extensively tested)

</div>

<div class="post" data-post-id="36055" data-author="*Breeze*" data-date="2015-08-21T20:16:57+00:00">

we are working on fixing game/website data sharing so you may be unable to login to the website if your password was manually changed by me at your request, at any point.  however any passwords set with the wwwpass command before Aug 20th should work now.

let me know (by email) if you find any funky stuff

the live blog is about a day or so behind but will start to update again whenever we are done with our work (hopefully this weekend sometime)

</div>

<div class="post" data-post-id="36056" data-author="Dragoth" data-date="2015-08-22T11:16:58+00:00">

just a fyi - As soon as shapeshifting got enabled the game returned to its usual slothness.

</div>

<div class="post" data-post-id="36062" data-author="Dragoth" data-date="2015-08-24T17:29:57+00:00">

Gotten a bit quicker after the last 2 reboots. 

Pings have remained constant and I do not change anything client-side, so something must be causing these speed fluctuations serverside.

</div>
