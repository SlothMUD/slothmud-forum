---
title: "Unholy Aura not firing on mob"
topic_id: 4153
author: "celerra7"
date: 2013-11-17T20:27:02+00:00
last_activity: 2013-11-20T01:36:09+00:00
last_author: "*Splork*"
sticky: false
locked: false
post_count: 3
---

<div class="post" data-post-id="34570" data-author="celerra7" data-date="2013-11-17T20:27:02+00:00" data-subject="Unholy Aura not firing on mob">

I am no longer able to use Unholy Aura spell on any pet or mob, only on myself:

```
Aslan on Newbatia, VK.
Main Street
   Main Street passes between the homes of Newbatia's upper crust.  The air is
warmer here, away from the edge of the floating island.  The solidly-built
red brick houses are set back from the street; the rather barren yards have
a few scattered bushes, but little grass.
Exits: North  South  West  
A gang member saunters by, looking for someone to beat up.
A ghostly form wavers in and out of existence nearby.
A hardworking denizen walks purposefully with long strides.
<538hp 315ma 298mv><-3.7ac 123557952xp 59387gp><+0><_20_>
cast 'unholy aura' member

<538hp 318ma 298mv><-3.7ac 123557952xp 59387gp><+0><_20_>
The sun slowly disappears in the west.
Timer now at 60 secs.

<538hp 318ma 298mv><-3.7ac 123557952xp 59387gp><+0><_21_>
cast 'unholy aura' ghost

<538hp 318ma 298mv><-3.7ac 123557952xp 59387gp><+0><_21_>
cast 'unholy aura' denizen

<538hp 318ma 298mv><-3.7ac 123557952xp 59387gp><+0><_21_>
cast 'unholy aura' clown

<538hp 318ma 298mv><-3.7ac 123557952xp 59387gp><+0><_21_>
cast 'unholy aura'
Ok.
You are consumed by an unholy aura.

<538hp 306ma 298mv><-3.7ac 123557952xp 59387gp><+0><_21_>
score affect
The following spells affect you:
   Unholy Aura                      

<538hp 309ma 298mv><-3.7ac 123557952xp 59387gp><+0><_21_>
```

As noted, I tried on the gang member, the ghost (pet), the denizen, a clown (not present), and then no target.  All commands were sent to the mud, and command prompts received, but nothing happens (no response, no mana drain, nothing) unless the spell is directed at myself.  This is repeatable through cmud, telnet, Flash, and all chars I have.  

Please advise.

</div>

<div class="post" data-post-id="34571" data-author="*juggleblood*" data-date="2013-11-19T21:50:21+00:00" data-subject="Re: Unholy Aura not firing on mob">

Confirmed it's not just you. It's everybody. I'm reporting it up.

</div>

<div class="post" data-post-id="34572" data-author="*Splork*" data-date="2013-11-20T01:36:09+00:00" data-subject="Re: Unholy Aura not firing on mob">

Fixed on reboot

</div>
