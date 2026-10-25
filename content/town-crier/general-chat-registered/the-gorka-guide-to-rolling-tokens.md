---
title: "The Gorka Guide to Rolling Tokens"
topic_id: 4965
author: "Gorka"
date: 2020-04-20T19:58:22+00:00
last_activity: 2020-04-23T11:10:56+00:00
last_author: "Gorka"
sticky: false
locked: false
post_count: 3
---

<div class="post" data-post-id="39438" data-author="Gorka" data-date="2020-04-20T19:58:22+00:00" data-subject="The Gorka Guide to Rolling Tokens">

Using a combination of logged hex and oct token rolls on a test character, and a program I wrote that is a reverse engineer of some old stat rolling source code, I believe I have calculated the probability of achieving stat totals with a good degree of accuracy. This information uses the following assumptions... 

* Four 1d6 die are rolled, the three highest dice are kept and added together. Then 1 is added to the total. If 19 is the total, the total is set to 18.

* The lowest stat that can be rolled on a hex is 5.

* The lowest stat that can be rolled on an oct is 8.

The results show roughly the average number of tokens it will take to roll the total with what type of token. The program was calibrated to roll the total 1000 times in order to calculate the average. However, it's completely possible to roll a total with only 1 token... or it could take thousands more than the average. Multiple executions of the program showed that the deviation between the average tokens grows the higher the total you aim for. It's also an observation that for each extra point in the total you aim for, you effectively about double the number of tokens required to reach that total.

It's also proven that oct's are definitely superior to roll than hexes, however hexes are cheaper. Hence I am lowering the cost of octs from 75k to 60k to make the effectiveness of both tokens roughly the same, as I often have trouble moving one type or the other based on "the superstitions/misinformation" of the player buying them.

People often ask me, what is the minimum amount of tokens I should start rolling with if I wish to get a playable total. I think that absolute minimum should be about 20 tokens to have a good chance to return to something 75 or higher. The other thing to do would be to save some tri tokens and use them in the case you bust.

It would be possible to roll a 90 in theory. Although somewhere around 80k-100k tokens would be required on average. On the other hand, you can buy the stat point in the avatar shop for 10B, which is approximately 10 hours of grouping at avatar levels. (12hrs if the leader is a smoker) How many tokens can you load in that time? My recommendation is that players aim for 82+, as to hold out for any thing higher could lead to frustration due to the diminishing returns. The money I make from selling tokens, probably hasn't covered the costs of the vaults I store them in, but I have probably helped more than 10 players achieve character stats higher than 80.

Hexes

Avg Rolls to roll an 80 : 80

Avg Rolls to roll an 81 : 140

Avg Rolls to roll an 82 : 240

Avg Rolls to roll an 83 : 470

Avg Rolls to roll an 84 : 1000

Avg Rolls to roll an 85 : 2100

Avg Rolls to roll an 86 : 5000

Octs

Avg Rolls to roll an 80 : 70

Avg Rolls to roll an 81 : 120

Avg Rolls to roll an 82 : 210

Avg Rolls to roll an 83 : 420

Avg Rolls to roll an 84 : 820

Avg Rolls to roll an 85 : 1850

Avg Rolls to roll an 86 : 4400

</div>

<div class="post" data-post-id="39440" data-author="Josiah" data-date="2020-04-22T23:52:49+00:00" data-subject="Re: The Gorka Guide to Rolling Tokens">

Those are some interesting assumptions, G. 

Did oct tokens get a new buff while I wasn't looking? I was told they lost their advantage years ago.

Why would 4d6 drop lowest + 1 grant a minimum stat of five? I haven't rolled in years, but I did get a three once on Sloth III.

Anecdotally, your 'number of rolls required' figures are close to my own experience. I expect an 82+ once every two hundredish tokens.

</div>

<div class="post" data-post-id="39441" data-author="Gorka" data-date="2020-04-23T11:10:56+00:00" data-subject="Re: The Gorka Guide to Rolling Tokens">

> **Josiah wrote:**
> Those are some interesting assumptions, G. 
> 
> Why would 4d6 drop lowest + 1 grant a minimum stat of five? I haven't rolled in years, but I did get a three once on Sloth III.

I can say for certain, once upon a time, this was the way rolling worked in sloth... and although holistically the function did change, it doesn't make any sense to tinker with the "4d6 drop lowest" equation part. When I coded my own function, I originally missed the "+1" part... and the number of rolls to get playable was far far higher... For half an hour I was trying to figure out what I'd done wrong in my replication of the old function - as soon as I realized my mistake and added it back in as it originally was, all of a sudden I was replicating the evidence from my tokens rolled in the game. I'm pretty confident about this part.

I recall back in s3 there was a public outcry about re-rolling and something was changed even then. If I was a coder and had to improve things, increase the chances ever so slightly, adjusting that minimum allowable stat code would have been the thing I would have changed, (ie, if roll < 5 then reroll) or the "+1". As you point out  the evidence seems to line up quite well with the formula... although "correlation != causation." 

Would be interested to know if anyone rolls a stat lower than the minimums I stated... please let me know if you do.

In any case, from the players perspective, the important thing to realize is that the rolling formula produces a typical bell curve when plotted graphically... The probability is that most rolls are are going to be average... ((18 - 5) / 2) + 5 + 1) * 5 = 62ish, and the rarest rolls will be towards both extremes, high or low proportionally. Therefore one can assume that the work to stray away from the mean which is going to have the gravity of the rolls, is an exponential factor. Even if the token min changed, the principal is still the same.

</div>
