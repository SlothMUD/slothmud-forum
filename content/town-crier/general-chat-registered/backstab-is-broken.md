---
title: "Backstab is broken"
topic_id: 4986
author: "Bandit"
date: 2020-10-22T22:18:02+00:00
last_activity: 2021-01-19T16:32:02+00:00
last_author: "Gorka"
sticky: false
locked: false
post_count: 13
---

<div class="post" data-post-id="39587" data-author="Bandit" data-date="2020-10-22T22:18:02+00:00" data-subject="Backstab is broken">

The black dragon queen quickly avoids your backstab, and you nearly cut your finger!

The black dragon queen quickly avoids your backstab, and you nearly cut your finger!

The black dragon queen makes a strange sound, as you place Bloodstained Blade of the Ancients in her back.

Your brutal backstab causes the black dragon queen to writhe in agony, opening up her defenses!

My 8x40 monk with 17 hitroll, 20 dex, 21 str, wielding a dagger and 50% excruciating blow stabs better than my 9x40 thief with 35 hitroll, 25 dex, 25 str, and capped skill.

We've noticed a pattern with warriors that stab in the group. Those that have thief around 7th or 8th in their class order stab really well, landing nearly every third stab. The warriors that moved thief up higher tend to miss quite a bit, much like a thief prime. My monk has thief 8th.

I've always tracked my stabbing as a thief and had plenty of time to observe that making any changes in my character didn't help at all. From pre-reborn to post and capping out my stats it was all the same. Generally I had a 70-80% chance to have the third backstab miss when it would swing at the enemy.

My monk has about a 15-20% chance to miss, and I've calculated Alias quite a bit in groups and he can easily come out an hour or two of groups with a 0% chance to miss.

</div>

<div class="post" data-post-id="39591" data-author="Gorka" data-date="2020-10-25T07:31:54+00:00" data-subject="Re: Backstab is broken">

> <strong>Bandit wrote:</strong>
> We've noticed a pattern with warriors that stab in the group. Those that have thief around 7th or 8th in their class order stab really well, landing nearly every third stab.

I don't count stabs, but I feel quite confident in saying that Tonedeaf's backstabs land just as much as Gorka. Tonedeaf is pretty much doing Gorka's xp run's at the moment. I doubt it's a "warrior specific" problem, more likely to be something else, possibly class position as you mentioned, or possibly group code, or combination of both... hard to say, but doubt it's warrior specific. I think that's more likely to be an observation bias because most players who stab in groups who are not thieves are nearly always warriors. Honestly, I think my bard stabs just as well doing "Gorka things." You could verify this fairly easy by getting another class to stab in a group... just not someone in pyjamas... need a thief 7th or 8th in good gear.

</div>

<div class="post" data-post-id="39592" data-author="Gorka" data-date="2020-10-25T07:49:48+00:00" data-subject="Re: Backstab is broken">

Just grabbed some rough stats from logs for a "Gorka Day" vs a "Tonedeaf Day." Same rates more a less.

Tonedeaf

164 Misses (2 of them were the triple stab)

1493 Hits (128 Excru Blows)

1657 Total

Gorka

270 Misses (1 of them was the triple stab)

3561 Hits (319 Excru Blows)

3831 Total

Tonedeaf has (29 +hit) slightly less than Gorka, max\_dex (22) and max\_str (23) also lower than Gorka. Yet the rates appear so similar you could almost pin the difference more on "random deviation." If any of these stats are actually effecting stab rates, I'd put my money on MAX\_DEX having a insignificant small increase. People tend to be conspiratorial about how the code works, assuming it's devilishly intelligent. If we learned anything about the code leak, it's completely the opposite. In any case I don't believe it's correct to blame warriors specifically, it doesn't appear to be a class bias (more likely something else). Can you post some stats like I have done for Bandit please. Specifically your stab rate to excru blow rate...

Sometimes I get feeling that part of the triple stab formula relating to "hitting" (not triggering) has been implemented backwards. The way to tell would be to get good stab stats/logs from Linx and Stun and post them here... Wouldn't be surprised if we find the rates are actually linear depending on class order... just the wrong way around of what they should be. It would also be an easy coding mistake to make, to make something linear and "progressive" but implement it as linear and "regressive." Stun and Linx's stats could prove this theory... or that the whole thing is something else.

Bandit stated in another thread that triple stab triggers 25% of the time for him... for Gorka/Tonedeaf it's about 9%... so the triggering mechanism appears normal (based on class position), whats abnormal is the hit rate when it fires. Given the fact the "triggering" appears correct, it would certainly help to obfuscate the fact the "hitting" formula was possibly implemented backwards - not to mention the formula was probably tested using a thief as a base, probably not other classes directly. The other possibility I can think of is that perhaps this the formula was not adapted to the 8 class system, or perhaps only in part - leading to the scaling system for the hit rate approaching 100% past the class position of thief 4th.

</div>

<div class="post" data-post-id="39594" data-author="Gorka" data-date="2020-10-25T14:06:45+00:00" data-subject="Re: Backstab is broken">

I calculated my backstab rate differently than Bandit, I calculated my trigger rate, well he is using the "to hit" rate. By using his method, my rate of landing the 3rd backstab would be 99+% for both Tonedeaf and Gorka. Given the codes frequent use of number(0, 100) I assume that perhaps the 1% correlates to the times I roll 100, perhaps a variable is outside the intended range?

</div>

<div class="post" data-post-id="39595" data-author="Bandit" data-date="2020-10-25T14:38:35+00:00" data-subject="Re: Backstab is broken">

Yeah, I wasn't suggesting this was a warrior only thing, but that was some previous speculation that we had. Mostly this comes from the only people that stab in the group are the tank or a thief prime. But, Shatterhand with thief 8th does just as well, as a warrior with thief late in the class order.

Gorka wanted my scripts / triggers for tracking that. Just keep in mind tracking third stab rate while solo is harder, because if you splork a mob in 2 hits of backstab you don't really know if you would have gotten a third stab or not.

Set up some variables:

```
Counters = {}
Counters.Backstab = {}
 Counters.Backstab.attempt = 0
 Counters.Backstab.hit = 0
 Counters.Backstab.miss = 0
 Counters.Backstab.otherMiss = 0
 Counters.Backstab.singleMiss = 0
 Counters.Backstab.doubleMiss = 0
 Counters.Backstab.tripleMiss = 0
	Counters.Backstab.count = 0
	Counters.Backstab.timer = 0
	Counters.Backstab.single = 0
	Counters.Backstab.double = 0
	Counters.Backstab.triple = 0
```

Hit messages (this is one trigger with the code)

```
^(.*) makes a strange sound, as you place (.*) back.$
^(.*) makes a strange sound but is suddenly very silent, as you place
```

Hit code:

```
Counters.Backstab.attempt = Counters.Backstab.attempt + 1
Counters.Backstab.hit = Counters.Backstab.hit + 1

killTimer(Counters.Backstab.timer)
Counters.Backstab.timer = tempTimer(1, [[ countStabs() ]])
Counters.Backstab.count = Counters.Backstab.count + 1
```

Miss messages (this is another trigger with the below code)

```
^(.*) quickly avoids your backstab, and you nearly cut your finger!$
```

Miss code:

```
Counters.Backstab.attempt = Counters.Backstab.attempt + 1
Counters.Backstab.miss = Counters.Backstab.miss + 1

killTimer(Counters.Backstab.timer)
Counters.Backstab.timer = tempTimer(1, [[ countStabs() ]])
Counters.Backstab.count = Counters.Backstab.count + 1

if Counters.Backstab.count == 3 then
 Counters.Backstab.tripleMiss = Counters.Backstab.tripleMiss + 1
elseif Counters.Backstab.count == 2 then
 Counters.Backstab.d[code]
```

oubleMiss = Counters.Backstab.doubleMiss + 1

 Counters.Backstab.otherMiss = Counters.Backstab.otherMiss + 1

else

 Counters.Backstab.singleMiss = Counters.Backstab.singleMiss + 1

 Counters.Backstab.otherMiss = Counters.Backstab.otherMiss + 1

end

Then what I do is just display some values in the "counters" display along with the number of hits/damage as follows:

Trigger on: 

```
"Backstab "
```

, yeah all those spaces, as just a substring and without the double quotes, only shoved them there to show the amount of spaces for copy/paste. Spaces may not really be necessary, but this stops it triggering from anywhere Backstab is in the game.

display code:

```
local value = formatPercentage(Counters.Backstab.hit, Counters.Backstab.attempt)
local totalStabs = Counters.Backstab.single + Counters.Backstab.double + Counters.Backstab.triple

local singlePercent = formatPercentage(Counters.Backstab.single, totalStabs)
local doublePercent = formatPercentage(Counters.Backstab.double, totalStabs)
local triplePercent = formatPercentage(Counters.Backstab.triple, totalStabs)
local tripleMiss = formatPercentage(Counters.Backstab.tripleMiss, Counters.Backstab.triple)
local otherMiss = formatPercentage(Counters.Backstab.otherMiss, Counters.Backstab.single + Counters.Backstab.double)

echo(' ' .. value .. ' \nS: ' .. singlePercent .. ' D: ' .. doublePercent .. ' T: ' .. triplePercent .. 'OMiss: ' .. otherMiss .. ' TMiss: ' .. tripleMiss)
```

And some helper function for formatPercentage I use:

```
function formatPercentage(val1, val2)
	local percentage = (val1 / val2) * 100
	
	return string.format("%2.2f", percentage) .. '%'
end
```

and countStabs

```
function countStabs()
	local count = Counters.Backstab.count
	
	if count == 1 then
 Counters.Backstab.single = Counters.Backstab.single + 1
	elseif count == 2 then
 Counters.Backstab.double = Counters.Backstab.double + 1
	elseif count == 3 then
 Counters.Backstab.triple = Counters.Backstab.triple + 1
	end
	
	Counters.Backstab.count = 0
end
```

</div>

<div class="post" data-post-id="39620" data-author="Driven" data-date="2020-11-20T15:32:50+00:00" data-subject="Re: Backstab is broken">

Ok, I'm determined to fix thieves, and so I ran a test with Maniac, where I had both Razyr and Bandit backstab xerxes 1000 times, and I collected only two stats:

(1) How many actual backstabs landed on Xerxes

(2) The # of times excruciating blow landed.

Razyr is thief oct, whereas Bandit is thief prime.

Run (#1) - Razyr w/+18 hitroll and 21 dex.

\# of Actual Backstabs = 1845, # of Excruciating Blow = 238

Run (#2) - Bandit w/+32 hitroll and 25 dex

\# of Actual Backstabs = 1989, # of Excruciating Blow = 117

Run (#3) - Razyr w/+32 hitroll and 25 dex

\# of Actual Backstabs = 2110, # of Excruciating Blow = 245

Same mob, 1000 times each player executes "backstab xerxes", thief oct lands excruciating blow 2x as often as thief prime.

</div>

<div class="post" data-post-id="39621" data-author="Gorka" data-date="2020-11-20T17:37:15+00:00" data-subject="Re: Backstab is broken">

I don't think there is anyone arguing that triple stab isn't broken.

I reached out to Breeze about it a while back, he's had some laptop issues lately - besides being busy. I do expect it will at some point be fixed.

</div>

<div class="post" data-post-id="39622" data-author="Ker" data-date="2020-11-21T17:46:15+00:00" data-subject="Re: Backstab is broken">

\#makethiefgreatagain! Yay for Maniac!

</div>

<div class="post" data-post-id="39664" data-author="Gorka" data-date="2021-01-06T21:47:31+00:00" data-subject="Re: Backstab is broken">

So I noticed this...

Teker's last logon was Tue Dec 22 12:19:23 2020

And I noticed this since reboot...

TMiss: 84.27%

That's a triple miss rate of 85% up from near 0%... No announcement... is triple stab fixed now? Thanks Mr Teker, and a happy new year to you sir!

Ummm, we need another favour though... the reading command is broken and has been disabled by Breeze and no one can tell astrology. Please? <img src="/images/smilies/icon_cool.svg" alt="8)" title="8)" width="15" height="15" class="smiley nozoom">

</div>

<div class="post" data-post-id="39665" data-author="Gorka" data-date="2021-01-07T06:40:10+00:00" data-subject="Re: Backstab is broken">

Can a thief check their triple stab please and post results here? I talked with Bandit briefly yesterday and a very small test was returning data that showed that prime stab was not changed, only everyone else got a nerf. I'd like to confirm that info.

And what a nerf it was...

I've gone from hitting triple stab 100% of 17% of the time... to hitting it 15% of 17%... hence my true triple stab rate is now... 2.55% down from 17%.

If triple stab is now 2.55% might as well call the skill prime... as everyone else can forget about it.

</div>

<div class="post" data-post-id="39667" data-author="Bandit" data-date="2021-01-07T18:44:40+00:00" data-subject="Re: Backstab is broken">

> <strong>Gorka wrote:</strong>
> Can a thief check their triple stab please and post results here?

Probably not, nobody plays a thief and triple stab is a portion of why we don't play our thief primes anymore.

</div>

<div class="post" data-post-id="39675" data-author="*teker*" data-date="2021-01-19T15:06:41+00:00" data-subject="Re: Backstab is broken">

To clarify what the changes were regarding triple stab/excruciating blow: There was an uninitialized variable in the code for players with thief in class slots 6-8. While I'm sure this appears to be a nerf to those players, I believe the changes are consistent with the intent of the original coder.

There have been other discussions regarding the skill and more changes could be made after considerable thought and discussion.

</div>

<div class="post" data-post-id="39676" data-author="Gorka" data-date="2021-01-19T16:32:02+00:00" data-subject="Re: Backstab is broken">

> <strong>\*teker\* wrote:</strong>
> There have been other discussions regarding the skill and more changes could be made after considerable thought and discussion.

This is one of those dangerous topics - full of grievances, personalities and genuine class problems. A solution that everyone would be happy with is damn near impossible. I'd be pretty surprised if a forum discussion was productive. It will sneak from solo stab, to group stab, to thieves in general, to where's the love for my prime class, to eventually ending needing sloth 5. I think it would be better if you came up with your own plan, got input privately from people and then just did it. If I think about your track record, I'd call your changes conservative, competent, balanced and rational... and your changes to triple stab and warcry were fairly massive nerfs for me - when already monks have possibly surpassed warriors. The chances are your worst ideas would be better than some of the broken systems we got. But I will say that a 85% triple stab skill that triggers 15% of the time but misses 85% of 15% of the time - makes me laugh out loud. My bet is the current code is poorly adapted from the 4 class system. You talked about the intention of how things were coded, and sticking to people original intentions... I'd suggest it would be better to take the intention from the 4th class system than how it's coded now with 8 classes - which was botched, and hence why most of the mud left at s4.

</div>
