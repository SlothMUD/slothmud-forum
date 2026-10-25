---
title: "Frenzy - Script .NET"
topic_id: 1808
author: "Nightwolf"
date: 2006-03-29T13:44:46+00:00
last_activity: 2006-03-30T09:48:42+00:00
last_author: "Nightwolf"
sticky: false
locked: false
post_count: 3
---

<div class="post" data-post-id="11867" data-author="Nightwolf" data-date="2006-03-29T13:44:46+00:00">

Just started learning Wintin.NET, and tried writing some own scripts.... So i made this frenzy script, with most of the syntax from Jezer's stone skin script, but it somehow does not block me from frenziying again when i am already in frenzy.... 

#defgroup {frenzy}

#alias  {fre} {#if {$vfrenzy = 0} {frenzy}} {G|frenzy}

#action {You are incapable of channeling your anger.} {fre} {G|frenzy}

#action {You begin to channel your anger and enter a state of frenzy.} {#var {vfrenzy} {1}} {G|frenzy}

#action {You calm down and return to a peaceful state of mind.} {#var {vfrenzy} {0};#showme {FRENZY DOWN!}} {G|frenzy}

#gag {You are incapable of channeling your anger.} {G|frenzy}

#gag {You begin to channel your anger and enter a state of frenzy.} {G|frenzy}

#gag {You calm down and return to a peaceful state of mind.}

#highlight {yellow} {FRENZY DOWN!} {G|frenzy}

#var {vfrenzy} {0} {G|frenzy}

#defgroup {}

Thanks, NW

</div>

<div class="post" data-post-id="11875" data-author="*juggleblood*" data-date="2006-03-29T23:28:20+00:00">

a few possibilities:

You have #presub on, which means the gag is killing the action.

or 

Wintin is acting up (happens to me when I do a lot of script window editing). -Restart wintin.

or

You were already frenzied when u started the script and tested it. Which means frenzy didn't get set to 1.

But, it looks right to me. Except for trying to highlight a #showme. I don't 

think you can do that.

</div>

<div class="post" data-post-id="11885" data-author="Nightwolf" data-date="2006-03-30T09:48:42+00:00">

Thanks for the advice, Juggleblood. I disabled presub, which didnt help, I change the script directly in the ws file anyways, and i wasn't frenzied...

But the thing about showme not being highlighted was a very good advice... We talked about it yesterday with Splork, and he said that atm, showme cant be highlighted yet, so it has to be worked around with subs...

so I tested the following script, which works just fine (although it doesn't look as pretty as the first one imho, but that's  

aesthetics :D )

#defgroup {frenzy}

#action  {You are incapable of channeling your anger.} {fre} {G|frenzy}

#action  {FRENZY UP!} {#var {vfrenzy} {1}} {G|frenzy}

#action  {FRENZY DOWN!} {#var {vfrenzy} {0}} {G|frenzy}

#alias  {fre} {#if {$vfrenzy = 0} {frenzy}} {G|frenzy}

#gag {You are incapable of channeling your anger.} {G|frenzy}

#sub  {You begin to channel your anger and enter a state of frenzy.} {FRENZY UP!} {G|frenzy}

#sub  {You calm down and return to a peaceful state of mind.} {FRENZY DOWN!} {G|frenzy}

#highlight  {yellow} {FRENZY DOWN!} {G|frenzy}

#highlight  {yellow} {FRENZY UP!} {G|frenzy}

#variable  {vfrenzy} {0} {G|frenzy}

#defgroup {}

</div>
