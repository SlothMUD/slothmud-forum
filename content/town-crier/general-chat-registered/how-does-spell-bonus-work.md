---
title: "How does spell bonus work?"
topic_id: 5103
author: "Vegetable"
date: 2024-05-25T13:20:28+00:00
last_activity: 2024-06-12T05:23:52+00:00
last_author: "Vegetable"
sticky: false
locked: false
post_count: 6
---

<div class="post" data-post-id="40092" data-author="Vegetable" data-date="2024-05-25T13:20:28+00:00" data-subject="How does spell bonus work?">

Hi, I recently added about 30 bonus spell bonus to my mage but see little to no difference in the damage output on my spells (including Disintegrate, Firewind & Frostbolt). 

Is anyone experiencing the same (i heard Fuligin mentioned something similar)? Was wondering if it's worth investing XP and conquest on more spell bonus....

For reference, my current spell bonus 217 (85 spell bonus + 132 bonus spell bonus).

</div>

<div class="post" data-post-id="40093" data-author="Guinex" data-date="2024-05-28T01:26:09+00:00" data-subject="Re: How does spell bonus work?">

I think the best guess on this was that it increases you max possible spell damage.

spell does 100-200 damage

spell with 100 spellbonus does 100-300 damage

</div>

<div class="post" data-post-id="40094" data-author="cnl" data-date="2024-05-28T21:56:34+00:00" data-subject="Re: How does spell bonus work?">

add it to the list of things we don't quite understand. like how exactly and to what damage reduction applies to. :)

</div>

<div class="post" data-post-id="40095" data-author="Driven" data-date="2024-05-29T18:44:24+00:00" data-subject="Re: How does spell bonus work?">

I'll have to look at the code to see if I see anything suspicious, but have you tried removing 30 of your base spell bonus to test whether there is some sort of functional cap being applied under the covers?  In other words, if you changed to 55 spellbonus with your 132 bonus, does your damage output remain the same?  This is the kind of thing I would experiment with.

</div>

<div class="post" data-post-id="40096" data-author="cnl" data-date="2024-06-11T21:25:07+00:00" data-subject="Re: How does spell bonus work?">

it's been a while since i last looked at this closely but based on this convo i spent a lot of time testing how spellbonus works again.

i will say that yes, there are caps and diminishing returns and the affects/caps differs per spell.

it also applies in non intuitive ways. ie. there are cases you may hit cap on max damage but increased spell bonus still pulls up the damage floor and overall average damage done.

even up to over 315 spell bonus i still saw measurable increases in damage even if the max values were not moving.

ultimately spell bonus is just 1 facet of combat.

if you have less spell bonus but can blast for 2/3 rounds vs more spell bonus but have to heal 2/3 rounds and blast 1 - obviously less spell bonus is better in that scenario.

i tend to test different eq sets in a more holistic manner than just looking at counters but most commonly:

a) min # of rounds and avg # of rounds to kill mobs i like to hit

b) how far through an area i can get before running out of mana

c) how much mana did i use

imo when you're solo - being able to reduce the # of rounds is the most meaningful metric unless you're trying to hyper-mile your mana in some way or your eq set is too unsafe.

remember that even with diminishing returns - being able to buy spellbonus is worthwhile because it means you now have flexibility to switch in other eq if you feel the spellbonus isn't bringing much extra to the table and it will have a cumulative affect in groups even when it may not bring much to solo.

</div>

<div class="post" data-post-id="40097" data-author="Vegetable" data-date="2024-06-12T05:23:52+00:00" data-subject="Re: How does spell bonus work?">

I haven't done the testing but just want to add some minor observation that some may have already know. This is what I think is happening but correct me if I'm wrong.

Not sure how to best describe this but here it is:

When your spell/skill kills a mob at low HP (i.e. Mob HP = 200, your spell/skill supposedly did 300) your overall damage will be lower as the counters will think you only did 200 damage on the mob. 

Because of this, I notice my average damage in counter is always lower when solo vs group as I'm always killing squishy/stab-like mob.

So for damage testing, best to test on thick mob to account for all damage done to the mob on the spell/skill. I have not tested my damage with reduced normal spell bonus. Most of my spell bonus upgrades over the past years are from bonus spell bonus. I'll try to test normal spell bonus one I get the time but will be good to see what you found in the codes Driven :) 

I'm not suggesting we change anything, just want to understand how this works. I'll probably wont tweak my gear regardless the outcome of the testing  :lol:

</div>
