---
title: "How do you sort items in vaults / keep vaults clean?"
topic_id: 5067
author: "Insomnia"
date: 2022-06-29T14:49:59+00:00
last_activity: 2022-06-29T20:54:49+00:00
last_author: "cnl"
sticky: false
locked: false
post_count: 2
---

<div class="post" data-post-id="39959" data-author="Insomnia" data-date="2022-06-29T14:49:59+00:00">

I have hundreds of vaulted items that –

- don't belong to a eqset (eqsets are stored in a separate room)
- are not Runes or gems
- may be a cp for some useful forge
- may belong to an autoquest line
- may be some high-level item that I may need later
- may be something useful that I do not want to get rid of (e.g. a radiant blue potion)
- with about 50% probability are junk

I would like to sort out what I need and what to discard, group items by category (e.g. put them in same room and add appropriate room names/descriptions) – and ideally do it all in an automated manner.

I wonder if anyone ever tried to solve this combinatorial task?  8) 

My current thoughts are as follows. For every item, I want to check whether it –

- is personal
- is a forge
- is a cp for a forge
- has 6x40+ level restrictions (may add more level categories)
- belongs to an autoquest, and whether I've already completed the autoquest
- is something useful (a radiant blue potion)
- can be turned in for conquest points
- *(is a duplicate of an item from one of the above categories)*

The idea is go through all items and add the respective tags – this should be not too hard to automate.

The next step is to process categories by tags:

- Untagged => most likely, useless, sell to shop, or give away, or junk
- Unique high-level item => keep vaulted
- Unique forges, forge cps, autoquest items => manually go through the list and decide
- Duplicates => try to turn in for conquest points => sell on auction, or sell to shop, or give away, or junk

Then, for what's left, put items with the same tags/belonging to the same forges in the same vault room.

Am I missing anything? Thoughts?  :P

</div>

<div class="post" data-post-id="39960" data-author="cnl" data-date="2022-06-29T20:54:49+00:00">

I use a rather manual approach involving annotations, single purpose vaults and containers in the vaults.

I made an alias and some scripts to reformat the way inventory, eq, shopping lists and vaults are displayed.

I can easily annotate items in game. ie, sub+ potion <red> heals 10 hp would: 

determine full name of 1st item called potion in inventory, and create an entry to annotate the text 'heals 10 hp' in red whenever it's listed. [https://imgur.com/3mNewUJ](https://imgur.com/3mNewUJ)

this is all done by hand. as I've identified things, or forged things or pursued forging things I annotate them.

some of the problem i tackle up front like you do. for example, i have a vault for fx reborn aq items. this is tracked off a list of aqs i keep so only 1 of each needed item goes in. then if i pop extra it goes in a known "junk" vault where i can sell off or spirit or whatever. likewise, i keep forge vaults but with the combination of annotations and putting cps for a single forge in a container like a sack. the annotations make it easy to group them into containers in the first place and to spot duplicates when isolated in a container. 

[https://imgur.com/7n9qqJ2](https://imgur.com/7n9qqJ2)

yes, this is an expensive solution since i "waste" a fair amount of slots on containers but all said it's a trivial amount if you have so much vaults and eq that it's an issue trying to save money on not putting containers is a waste of time.

then there's several vaults i just don't dare go visit because mistakes were made.

</div>
