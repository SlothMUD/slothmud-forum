---
title: "Saves Petri / Poison / Breathe / Para"
topic_id: 5049
author: "Gorka"
date: 2022-03-02T07:52:13+00:00
last_activity: 2023-11-29T07:04:18+00:00
last_author: "*Idjit*"
sticky: false
locked: false
post_count: 4
---

<div class="post" data-post-id="39893" data-author="Gorka" data-date="2022-03-02T07:52:13+00:00" data-subject="Saves Petri / Poison / Breathe / Para">

A long time ago it was asked about the usefulness of the different types of saves in sloth, as it is perceived that almost all the different types of saves, except spell_saves are pretty useless. Some fairly vague answers were given... and now that we have the conquest system, the question has arisen again... should I waste conquest points on buying those extra saves. I've done some research in the nearly 20 year old code leak to try and find some answers.

SAVES_POISON - You'll want this if you are a thief who uses the apply poison skill, against mobs with poison weapon attacks, mobs that hurl darts or other poisonous items, mobs who use stinger tail procs, mobs who use vampiric touch, or in general when you are poisoned.

SAVES_BREATH - You'll want this if you fight mobs with breath attacks, basically any mob/room that has some sort of elemental fire, frost, lightning, gas, acid breath.

SAVES_PETRI - You'll want this against mobs who fear, focus and stun, chill or try to drain you.

SAVES_PARA - This is not available in the extended rebirth shop, as the difference it would add would make most mobs charmable from what I have heard.

In general, all these things are effectively increasing your defensive capabilities against mob/room procs that you encounter frequently. Basically they mean you will take less damage. Given their small cost, and the fact that the game wasn't really designed for you to have as much as what is on offer now days, I would recommend that you buy them as they could potentially offer more value for money in niche situations than you might imagine. I also recommend having grace as a perm spell, and fare thee well can further increase these abilities for everyone in a group.

Given the fact that the new conquest system requires you to kill and subdue every mob in the game... you are going to encounter all the niche situations that these saves defend against. Given the fact you probably have the -3's purchasable from the first rebirth shop, and these saves are often not present on elite equipment, the advantage of buying them using conquest points, would double your current defenses against them. These values often go up against the mobs spells saves, so if the mob has 15 spell saves, and you have -6 saves_poison against a poison attack then you should be an extra 20% more effective in saving some damage. Given the low cost, and the fact you will encounter these niche situations now, I think they are probably worth buying.

SAVES_SPELL - Is by the far one of the most important variables in the game, and as much as possible should be worn in every eq mode you have. For casting -1 saves is also about equivalent to about +5 spell damage on average over many castings.

</div>

<div class="post" data-post-id="39895" data-author="cnl" data-date="2022-03-03T19:53:42+00:00" data-subject="Re: Saves Petri / Poison / Breathe / Para">

If you are a druid using forms you want the saves that go with your attack.

ie, if using breath attack SAVES_BREATH is useful.

when I was a new player the thing that was confusing to me is that these SAVES are used both for your offense and defense for these attack types. so my initial assumption was that spell saves were useless when fighting non-casting mobs but in reality good spell saves can effectively almost double your offensive damage since it's used to calculate the mobs chance of saving against your spells as well.

</div>

<div class="post" data-post-id="40080" data-author="Insomnia" data-date="2023-11-22T11:41:23+00:00" data-subject="Re: Saves Petri / Poison / Breathe / Para">

Just found this post... is there a specific reason why Paralyzation is special? Honestly looks like a bug to me, that I can't get above 3.

```
27)   -1  Save Breath            -   3 of   6 -   5.58 B  /    2.79 M  /  278.79 k
28)   -1  Save Paralyzation      -   3 of   3
29)   -1  Save Petrification     -   3 of   6 -   2.79 B  /    1.39 M  /  139.39 k
30)   -1  Save Poison            -   3 of   6 -   2.79 B  /    1.39 M  /  139.39 k
31)   -1  Save Spell             -   6 of   6
```

</div>

<div class="post" data-post-id="40082" data-author="*Idjit*" data-date="2023-11-29T07:04:18+00:00" data-subject="Re: Saves Petri / Poison / Breathe / Para">

yes there is

paralyzation saves is closely tied to the charm person stuff and so its tightly guarded even for classes predisposed to have charm person to never be allowed to get above like eight or nine.

Even with favorable class bonuses all stacked on top etc

</div>
