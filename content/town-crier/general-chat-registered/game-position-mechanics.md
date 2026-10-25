---
title: "Game Position Mechanics"
topic_id: 4844
author: "Gorka"
date: 2018-04-07T08:53:06+00:00
last_activity: 2018-04-19T05:13:45+00:00
last_author: "Gorka"
sticky: false
locked: false
post_count: 11
---

<div class="post" data-post-id="38720" data-author="Gorka" data-date="2018-04-07T08:53:06+00:00">

There are some things about the games position variable for a character that I don't agree with... although I suspect its always been this way...

Today while in dark chasm I was resting, when a bush jumped out and attacked me. (As they do like in real life) I display my msdp.POSITION variable in my client... and it was resting. I firewinded the bush, but it said I was resting and I needed to stand up. (All this went on while I was brutally massacring it from a resting position with my sword) The entire fight went on without the game realizing I was in a fighting position. The stupid thing is, you can apparently fight while resting, but you can't rest while you fight, as you get the Rest while you are fighting are you mad message. In my opinion when I am engaged my position should be fighting. I didn't check, but maybe if I am resting, then I am also contemplating, getting the 300hp+ regen while fighting.

Furthermore the game has always been a bit weird when fighting multiple mobs, and the engaged one dies. It's not until the next round that the game recognises what your new target is, so you can hit it with a spell. I notice that my msdp.POSITION variable is also confused at this time. If I am fighting two mobs, and one dies... I should still be fighting, and the game should know my next target... the one trying to kill me... duh... On occasion after the death of the engaged mob, I can also change rooms immediately after death even though I was engaged with multiple mobs.

There is also situations where because your position is not fighting, you can actually move to another room while fighting without disengaging, because the game is convinced your not fighting, even though you are.

Also I don't feel the msdp.POSITION variable is updated quickly enough. If you script something on this variable changing you will see the timing causes issues.

PS score stats2 doesn't reflect my bonus spell bonus either, and it doesn't update the MSDP cap values for my char which should have changed to reflect the bonus.

</div>

<div class="post" data-post-id="38721" data-author="Gorka" data-date="2018-04-07T09:17:07+00:00">

Here's some proof of my resting argument...

You massacre a vampire follower to small fragments with your hit.

A vampire follower looks shocked as it cuts itself on your petrified armor!

You are brutally massacred by a vampire follower's bite.

A vampire follower misses you with its bite.

A vampire follower misses you with its bite.

A vampire follower misses you with its bite.

A vampire follower misses you with its bite.

A vampire follower misses you with its bite.

A vampire follower misses you with its bite.

You are brutally massacred by a vampire follower's bite.

You are brutally massacred by a vampire follower's bite.

A vampire follower misses you with its bite.

You massacre a vampire follower to small fragments with your hit.

You massacre a vampire follower to small fragments with your hit.

You massacre a vampire follower to small fragments with your hit.

<1330hp 547ma 190mv 2122098348xp -13.9ac 82%>

score

Gorka has a hairy mole.  (level: 40)

Your levels:  Wa: 40 Mo: 40 Cl: 40 Ma: 40 Dr: 40 Ne: 40 Ba: 40 Th: 40 Av: 40 

You are 134 years, 1 month, 4 days old.

You are a citizen of Bal Harbor.

You are a devout worshipper of Enea.

You are neutral.

You have completely explored this area.

You've seen 72.3% of the world.

You are widely viewed as pretty trustworthy.

You aren't controlling any followers right now. [0.0]

You have (1338/1476+368) hit, (549/694+62) mana and (192/450+65) movement points.

Your armor class is -13.9.

You have +25 to hit, +21 on damage and up to 4 attacks.

You have 3238269 gold coins.

You have three hundred and ninety-six drachma.

You have 2702499 honor.

You have 2122098348 unused experience points.

You have been playing for 386 days, 23 hours, 18 minutes.

You are a member of Gorklings.

You are well-attuned to the channelling stratum.

Str: 22[19], Int: 20[19], Wis: 20[19], Dex: 21[19], Con: 20[19] (103[95])

**You are resting.**

Your song can affect as many as nine people.

You are affected by the following spells:

   Avatar Sight                     

   Darksight                        

   God Sanctuary                    

   Resist Fire                      

   Avatar Blessing                  

   Resist Cold                      

   Resist Webs                      

   Petrified Armor                  

   Greater Fluidity                 

   Grace                            

   Nature's Restoral                

   Undead Visage                    

<1338hp 549ma 192mv 2122098348xp -13.9ac 82%>

You deal a massive blow to one of a vampire follower's vital organs.

You viciously massacre a vampire follower with your hit.

A vampire follower's bite bounces off your heavy armor.

A vampire follower misses you with its bite.

A vampire follower misses you with its bite.

A vampire follower's bite bounces off your heavy armor.

You are brutally massacred by a vampire follower's bite.

A vampire follower misses you with its bite.

A vampire follower's bite bounces off your heavy armor.

A vampire follower's bite bounces off your heavy armor.

A vampire follower misses you with its bite.

A vampire follower misses you with its bite.

You massacre a vampire follower to small fragments with your hit.

You massacre a vampire follower to small fragments with your hit.

You brutally massacre a vampire follower with your hit.

<1305hp 552ma 196mv 2122101909xp -13.9ac 66%>

rise;n

wake;stand

You are already awake...

<1317hp 554ma 198mv 2122101909xp -13.9ac 66%>

@@

You stop resting, and stand up.

<1317hp 554ma 198mv 2122101909xp -13.9ac 66%>

Upon the Shore

   Firm white sand and small rocks make walking upon this shoreline rather

easy.  The bluish-green salt water gently kisses the sand, causing a ripple

effect to be visible upon the beach.  Nearby to the north, a set of massive

gates can be seen, while strange sounds of suffering and pain can be heard

echoing throughout the area.  A densely growing forest is visible nearby to

the west.

Exits: North  South  West  

The Asheron is docked here.

<1320hp 555ma 198mv 2122101909xp -13.9ac -%>

NOTE: Contemplation does work while "Fight Resting."

NOTE: When the first vampire follower dies, I can also leave the room even though I am engaged (within the next round.)

I have a few proposals...

1) Don't set my position by default when a mob dies... check if I am engaged with other mobs, update target.

2) Set my position as fighting/sitting whenever I am **first engaged**, auto-stand/sit me.

3) Review the role of the sitting position. Maybe fighting while resting, should be sitting... until I stand... also it needs to be noted that sitting also gets contemplation, I checked. It's possible to throw hammers at mobs and rest to gain better regen during the fight. Probably that's not what was intended.

4) I don't understand the point of the sit position outside of fighting, do we need the sit command? Sit command should maybe only be possible while fighting, otherwise it should be resting... it's a bit confusing what these positions are for and what there benefits are. Sit seems redundant outside of fighting off my feet.

</div>

<div class="post" data-post-id="38722" data-author="Gorka" data-date="2018-04-07T10:16:39+00:00">

So I thought to myself, on chop mobs that don't hit much, there would be an advantage to resting while fighting so I could contemplate... so how to get myself resting...???? hmmm

Then it came to me, crappy broadside... always dumps me on my ass... so I set a trigger to rest, when broadside dumped me... sure enough it works... (example below is from bashing though) resting from sitting and contemplating while fighting...

An elder citizen misses you with his hit.

An elder citizen misses you with his hit.

You skillfully parry the attack of an elder citizen.

Your riposte viciously massacres an elder citizen.

An elder citizen misses you with his beat.

You brutally massacre an elder citizen with your slash.

You brutally massacre an elder citizen with your slash.

You brutally massacre an elder citizen with your slash.

You brutally massacre an elder citizen with your slash.

An elder citizen charges and bashes into you!

You are knocked off your feet!

rest

<1475hp 676ma 383mv 2396801911xp -13.9ac 73%>

You rest your tired bones.

<1476hp 680ma 387mv 2396801911xp -13.9ac 73%>

You are viciously massacred by an elder citizen's hit.

An elder citizen misses you with his hit.

An elder citizen's hit bounces off your heavy armor.

An elder citizen's beat bounces off your heavy armor.

You brutally massacre an elder citizen with your slash.

You brutally massacre an elder citizen with your slash.

You brutally massacre an elder citizen with your slash.

You deal a critical blow to one of an elder citizen's vital organs.

You viciously massacre an elder citizen with your slash.

An elder citizen wipes his boots in your face.

My suggestion is to fix this by stopping broadside "ass dumping" so it's not so easy to do this...  :twisted:  :twisted:  :twisted:  :twisted: 

Players effectively have a free disengage, when in the sitting position, because they can rest then leave the room within that round.

There shouldn't be a contemplation and disengage bonus, for fighting while resting. Nor should there be a contemplation bonus for being bashed.

</div>

<div class="post" data-post-id="38723" data-author="*Idjit*" data-date="2018-04-08T14:16:55+00:00">

Have you noticed also Gorka that if you put the hp regen in your prompt, when you've picked up a warcry bonus the hp-regen oscillates between your normal standing regen and the warcry-induced hp regen quite a whole bunch of times back and forth.

</div>

<div class="post" data-post-id="38724" data-author="Gorka" data-date="2018-04-08T17:06:26+00:00">

You sure that's not bloodrage? I'm not sure how it would be possible to separate warcry hp regen and bloodrage if that were the case.

</div>

<div class="post" data-post-id="38726" data-author="*teker*" data-date="2018-04-10T22:01:04+00:00">

I think position fighting was originally designed to be a "fighting stance" rather than a simple indication that you are fighting.  The game automatically switches you into this stance if you attack or if you're standing and something attacks you.

Sitting and resting allow for better regen but you take more damage when hit in these positions.  You could choose to sit instead of rest if you're afraid an aggressive mob might wander in and you don't want to take the full damage penalty of resting.  The only other purpose for sit that I can think of is to put you at a disadvantage when bashed or you fail a skill really badly.  That seems to be what we're using it for.  Sloth also has a "crawling" position but I'm not sure what it's useful for.

So, you can be fighting someone but not in your "fighting stance".  I believe the MSDP variable updates are timely (atleast the CHARACTER_XXX ones).  

Simple changes I can make:

- No longer allowed to sit or rest while fighting - even if not in fighting stance.

- Fix standing from resting so that you can't walk out of a fight afterwards.

- No regen bonuses related to position/contemplation while fighting.

- Include regen bonuses for bloodrage while fighting but not in fighting position.

Do you want me to look at the situation where you're not fighting if you kill a mob at the end of the round?  It seems like this gives you an opportunity to engage the mob of your choice.

Potential "wild" fluctuations in regen may be a result of bloodrage.  The "calculate regen" functions get called in quite a few places in the code and if you have bloodrage the server is performing a skill roll at a non-predictable but fairly frequent interval.  So if you've got your regen in your prompt, it's performing a skill roll every time that prompt shows.  Or when you type score.  Or when the game needs that regen calculation for something else.

I don't see a warcry regen bonus so I'm not sure what you guys are talking about there.  Warcry seems to give bonus HP which allow you to go over your normal HP maximum.

</div>

<div class="post" data-post-id="38727" data-author="Gorka" data-date="2018-04-11T05:39:26+00:00">

> **Quote:**
> Do you want me to look at the situation where you're not fighting if you kill a mob at the end of the round? It seems like this gives you an opportunity to engage the mob of your choice.

Personally, I think so, I want to keep blasting after a mob dies. The game is already making the switch just not fast enough. If players wish to do as you say, most will already have engage. I don't consider this waiting round a feature ... just annoying... a classic example being collections of guards which swarm in most areas, once the first dies, you can't blast the second without specifying the target again for a round.

Im not sure how it's possible to get into the crawling position... but suspect it's used xp'ing between 6-8x40... :lol: I tried typing crawl but it behaved like a social which isn't on the socials list. Is it used for rooms where it says you are too big to squeeze through there?

Your list of things you could look at, looks good, but fixing broadside was strangely absent...  :lol:  :twisted: 

Could the list of what you get from warcry at each level be publicised... in help warcry or the command usage. I didn't expect we got hp regen from warcry as zuzu thought, however if we did we wouldn't know because of bloodrage...  For some unknown reason this information is kept hidden like it's the nuclear launch codes. It doesn't matter if it's public... look at all the concern the counters function created... nothing happened. Same could be said for knowing stat caps for classes. Extremely useful and eventually known anyway.

</div>

<div class="post" data-post-id="38729" data-author="Teron" data-date="2018-04-12T12:05:05+00:00">

Gorka you a wrong that nothing happened from introducing counters.

Yesterday Zaq asked me, why his stab damage was over 700, compared to under 500. I told him that's the thief prime stab damage cap in groups, because damage is mobhp % (though the latter is heresay on my part).

So there, it provided some explanation and clarity for what is happening after stab for thieves.

I call this a positive experience, rather than a neutral experience. Then again, seeing the actual damage, and what exactly contributed to it, would've helped.

More tables for:

- warcry brackets and stats

- bonus caps

- mana/hp/regen per class per position stats (there used to be one in S3, but now we have 4 more classes. Some players level dozens of chars to test this)

would be helpful.

</div>

<div class="post" data-post-id="38730" data-author="Gorka" data-date="2018-04-12T14:17:01+00:00">

My point about "nothing happening" was to do with the supposed "abuse and whining" that was going to ensue if they showed damage. As far as I am aware, that fear did not transpire.

</div>

<div class="post" data-post-id="38734" data-author="Teron" data-date="2018-04-14T08:02:46+00:00">

Yes, and I said about the opposite: it inspired a player to looked into how the game works and become a better player.

</div>

<div class="post" data-post-id="38737" data-author="Gorka" data-date="2018-04-19T05:13:45+00:00">

I see I can't rest while fighting anymore since reboot, so I suspect some changes have gone in... But the targeting thing is still annoying... In the following example I have a script for msdp.CHARACTER_HEALTH. Each time this variable changes I am echoing my position... In this example I am fighting two mobs at the same time, but when the one I am engaged with dies... my position is set to Standing... when in fact I should be Fighting. The issue for me is I want to swap weapons when a mob dies... but not if I am still fighting... and I have no way to do this... as the position is not correct. Also if I output the position immediately on mob death,in 50% of cases it will be Standing and the other 50% will be Fighting. Basically, this position variable is slow to update and nearly always filled with an unusable value.

FightingFighting

You land a powerful strike into a vampire follower's side.

strike

@@

<1291hp 801ma 484mv 1640483851xp -10.2ac 9%>

A giant white shark misses you with his bite.

<1291hp 801ma 484mv 1640483851xp -10.2ac 9%>

With a mighty effort, you shake off your exhaustion!

A vampire follower looks shocked as it sees your fist embedded in its abdomen, then collapses.

A vampire follower is dead! R.I.P.

You gain 420949 bonus experience!

Total exp for kill is 1191367.

Your blood freezes as you hear a vampire follower's death cry.

You get a flask of human blood from the corpse of a vampire follower that's on the ground.

You get gold coins from the corpse of a vampire follower that's on the ground.

There were 666 coins.   :twisted:  :twisted:  :twisted: 

<1294hp 800ma 470mv 1642101403xp -10.2ac -%>

Standing

The 'petrified armor' spell on you is about to wear off.

<1296hp 800ma 471mv 1642101403xp -10.2ac -%>

StandingStanding

A vampire follower looks shocked as it cuts itself on your petrified armor!

A vampire follower massacres you to small fragments with its bite.

A vampire follower misses you with its bite.

A vampire follower misses you with its bite.

A vampire follower massacres you to small fragments with its bite.

A vampire follower massacres you to small fragments with its bite.

A giant white shark misses you with his bite.

A giant white shark misses you with his bite.

A giant white shark misses you with his bite.

A giant white shark looks shocked as he cuts himself on your petrified armor!

A giant white shark hates your guts!

A giant white shark massacres you to small fragments with his bite.

You are brutally massacred by a giant white shark's bite.

You are brutally massacred by a giant white shark's bite.

You brutally massacre a vampire follower with your hit.

You deal a massive blow to one of a vampire follower's vital organs.

You viciously massacre a vampire follower with your hit.

You brutally massacre a vampire follower with your hit.

A giant white shark tears off a large chunk of flesh with his mighty jaws!

|;recall

<1095hp 800ma 474mv 1642117491xp -10.2ac 74%>

FightingFighting

Ok.

Settlestone's Well

   This is an extremely energetic section of the dwarven city of

Settlestone.  Two bustling streets intersect at the site of a ten foot tall

statue of the famed Krodar Thunderhammer.  All four sets of city gates can

be seen from this vantage and hundreds of people walk about nearby.  There

is also a large black stone well in the center of the square.

Exits: North  East  South  West  Up  Down  

A small figurine of a bunny made of chocolate stands here, tempting you.

A piece of paper rolls across the ground with the wind.

A soiled sheet from some notebook shifts here in the wind.

A statue of Krodar Thunderhammer stands tall atop a pedestal.

The large central well of Settlestone is here...It glows violet!

A dusty dwarven warrior walks slowly about the city.

A sturdy dwarven pack mule stands here showing its teeth at you.

A sturdy dwarven pack mule stands here showing its teeth at you.

Scanning around, the dwarven caravan leader keeps an eye on his goods.

Belrath is standing here.

Belrath has a steady blue aura.

Ezekiel is standing here.

Ezekiel glows with a bright light!

Ezekiel has a strong red aura.

A dwarven animal control officer patrols the area.

</div>
