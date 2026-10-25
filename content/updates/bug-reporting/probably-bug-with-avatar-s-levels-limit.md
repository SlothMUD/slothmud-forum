---
title: "Probably bug with avatar's levels limit"
topic_id: 4416
author: "Filk"
date: 2014-12-01T06:46:02+00:00
last_activity: 2014-12-02T20:02:12+00:00
last_author: "*Splork*"
sticky: false
locked: false
post_count: 8
---

<div class="post" data-post-id="35533" data-author="Filk" data-date="2014-12-01T06:46:02+00:00">

Situation:

My levels:  Dr: 40 Cl: 40 Ma: 40 Ne: 40 Ba: 40 Mo: 40 Wa: 30 Th: 25 Av: 27 

When trying to level: Apirana the Master Avatar tells you 'Thou art too puny to level here. Begone!!

I found on forum, that limit rule now is avatar level for each 5 totals after 4x40.

I have now: 40(8 levels) + 40(8 levels) + 30(6 levels) +25(5 levels) + 27(5 levels)  = 32 av level. Shold be.

But it seems, game ignores current 5 av levels i should get from avatar totals.

That ruins my dream of getting relocation without 7x40 :(

Can that be fixed please? 

Or explain current logic of that limit, so i will know, what i missing.

</div>

<div class="post" data-post-id="35534" data-author="*Breeze*" data-date="2014-12-01T07:19:10+00:00">

Why would we count avatar levels as part of avatar level leveling restriction.

Only classes 5-8 count

</div>

<div class="post" data-post-id="35538" data-author="Filk" data-date="2014-12-01T07:41:21+00:00">

Because if not count avatar levels, then how you can get av level beyound 32? Which is 4x40 8 levels each.

</div>

<div class="post" data-post-id="35539" data-author="*Breeze*" data-date="2014-12-01T08:56:10+00:00">

avatar level logic straight from the code.

```
if (#40s is less than 8)
{
 if (#40s is less than 4 || (((class5+class6+class7+class8)/5) <= avatar levels))
 {
   // too puny to level
 }
}
```

in your case,

```
 

(40+40+30+25)/5
135/5 = 27

if (#40s < 8)
{
 if (#40s < 4 || (27 <= 27))
 {
 // too puny
 }
}
```

so its not a bug but working as intended.

</div>

<div class="post" data-post-id="35540" data-author="Filk" data-date="2014-12-01T10:50:21+00:00">

Nods. I see.

From that logic, i will get relocation only on 7.35

Wish it were sum(class5-class9)/5, since av levels are also levels that should be count in totals :)

Sad, but ok. Thanks for explanation.

</div>

<div class="post" data-post-id="35541" data-author="*Splork*" data-date="2014-12-02T02:30:04+00:00">

Code works exactly as it was intended.  We started out with 5 levels for every 40 starting at 4x40 ( or somewhere around there) players whined and we gave in. However, we did not want players relocating everywhere at 8x40, we wanted it to be close to the end of the game. We are happy with this equation and it will not be changed.

Splork

</div>

<div class="post" data-post-id="35542" data-author="Magi" data-date="2014-12-02T16:34:16+00:00">

Avatar levels before 8x40 was initially suggested by a player. The immorts deserve a mountain of credit for accepting that suggestion and implementing it so well.  I don't think I would have made it to 8x40 without aegis, greater refresh, and call followers.

The boating game has also been significantly eased by the addition of fargate wands, continent-specific fargate days, clan recalls, and intercontinental portals on every* continent.  (* there might not be one on Valkyrie)

</div>

<div class="post" data-post-id="35543" data-author="*Splork*" data-date="2014-12-02T20:02:12+00:00">

Oops, after reading my post again, Magi is correct. There were no leveling of avatar levels until one reached 8x40. It was too much  on players and the compromised to what it is today which most of us think is pretty fair.

Thanks Magi!

</div>
