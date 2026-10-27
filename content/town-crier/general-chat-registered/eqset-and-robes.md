---
title: "Eqset and Robes"
topic_id: 4780
author: "Gorka"
date: 2017-07-28T07:35:59+00:00
last_activity: 2017-08-03T14:08:16+00:00
last_author: "Gorka"
sticky: false
locked: false
post_count: 28
---

<div class="post" data-post-id="38347" data-author="Gorka" data-date="2017-07-28T07:35:59+00:00" data-subject="Eqset and Robes">

Maybe I just don't know, maybe I'm doin' it wrong... but I have robe problems.

I've kind of been a 1 robe guy up til now, but wish to enter the interesting world of robe polygamy. Recently I acquired a Homespun Linen Robe, which I added to my regen set, however this leads to my main robe, my cloak of shadows... also my "stuff" robe, sitting in inv, meaning that I can't so much as pick up a post it note without changing my eq mode.

Potentially, the robe I may want to wear for a certain eq mode may also not be a container... and then what happens... I can't pick up a post it note in that mode too?

Am I failing to use eqset correctly... or is there some way we can make this work whether the robe is the stuff container or not, or if the robe is a container or not?

There are all these sexy robes I want to try and I feel like I am stuck using one if I want to be functional.

Teker? What do you think? Is there a solution?

</div>

<div class="post" data-post-id="38348" data-author="*Idjit*" data-date="2017-07-28T21:25:38+00:00" data-subject="Re: Eqset and Robes">

I know you can set robe A to be the defcontainer.

Then you can set robe B's setcontainer to be robe A.

That covers Binary robe systems. (like heal and blast for a C/M).

But we run into trouble, like Gorka said, when I get to robe #3 for chop mode. (wolfskin robe).

It starts giving the "Creates a circle" message.

and then I always have to put, regardless of which robe is called out in the circle message for causing a problem, the robe that came from the last-used set, into the wolfskin robe.

"rem robe;put healer robe;wear robe"

I am wondering if we might move robes into a separate classification within eqsets where "all other robes go into the destination set's designated about-body"

Or some such like. so that we can handle N robes beyond 2.

Food for thought.

\--D

</div>

<div class="post" data-post-id="38349" data-author="Gorka" data-date="2017-07-28T21:56:22+00:00" data-subject="Re: Eqset and Robes">

> <strong>\*Idjit\* wrote:</strong>
> I am wondering if we might move robes into a separate classification within eqsets where "all other robes go into the destination set's designated about-body"

This assumes though that your eqset robe is a container... what if it's not... There are mana regen and mana robes that are not containers, what does one do in these situations?

It seems silly that the issue is not your strength or capacity, it's whether the weight is worn or not. What if it was changed so it's doesn't matter if the weight is worn or sitting in inv. Capacity or Strength effect could remain the same and you could still pickup a post it note if your stuff robe happened to be in inv... Or else make all robes containers... or don't compartmentalize the inventory and robe capacity, have a single capacity and it doesn't matter if that capacity is used by items in the robe or in inventory.

It's just kind of annoying that the robe slot is so inflexible, when there are 140 different robes.

\* Cue size complaint from Taron... \*

![](https://s-media-cache-ak0.pinimg.com/originals/b5/8b/24/b58b24f52571eba9e8c5b685130a599f.jpg)

Taron's Eq Sets.

</div>

<div class="post" data-post-id="38350" data-author="*teker*" data-date="2017-07-28T23:15:24+00:00" data-subject="Re: Eqset and Robes">

I'm open to implementation suggestions. I did limited testing with 3 robes where they work in a circle A -\> B -\>C -\> A and it seemed to work. There are definitely issues when the robes have varying capacity and one won't fit within the other. I tend to split up my gear like this:

Robe A: All blast gear

Robe B: All regen, mana gear

Robe C: All heal, raise gear

For the situation where a robe is not a container - do you have another container equipped at that time? There's nothing special about the robe slot as far as the eqset code goes - you could set up a belt pouch as a container for items. If you're not wearing a container, it's going to be hard to stash all your gear other than leaving it in your inventory.

</div>

<div class="post" data-post-id="38351" data-author="*Idjit*" data-date="2017-07-28T23:51:23+00:00" data-subject="Re: Eqset and Robes">

I solved it

I set myrmidon to use wolfskin

I set wolfskin to use healer

I set healer to use myrmidon

And this seems to have allowed things to be Ternary.

I cycled through all available switches and seemed to be ok.

so it has to fit head to tail apparently.

\--Idj

</div>

<div class="post" data-post-id="38352" data-author="*Idjit*" data-date="2017-07-28T23:55:43+00:00" data-subject="Re: Eqset and Robes">

As regards capacity, we might look at aligning all the robes that are slightly less than 500 capacity for no good particular reason like the Trollskin robe is 400, bumping them all to 500 units.

\--D

</div>

<div class="post" data-post-id="38353" data-author="*Idjit*" data-date="2017-07-29T00:06:33+00:00" data-subject="Re: Eqset and Robes">

I had a thought about weight vs capacity and I wondered if we make "eqset show" more verbose

..

..

Held Ars Magica [ Default ]

Loaded a mithril quarrel [ Default ]

could become

..

..

Held Ars Magica [ Default ] [8] 

Loaded a mithril quarrel [ Default ] [1]

eqset 'regen' non-worn weight total [432] pounds in top-level container(s)

total weight of all items, worn and unworn: [537] pounds

total container capacity [1500]

the [8] and [1] could be the pounds of weight of each individual item

I'm probably saying these diagnostic lines all wrong, but some kind of doohickey could be created

for troubleshooting those containers you mentioned had insufficient capacity, so people could fiddle

with it and balance their stuff between their robes. 

I don't know I'm just brainstorming.

Thing is, you don't really need the weight of the worn stuff. It isn't counting. You need the weight of the -unworn- stuff, so maybe the individual weights in the worn set aren't really relevant.

\--D

</div>

<div class="post" data-post-id="38354" data-author="Gorka" data-date="2017-07-29T04:42:40+00:00" data-subject="Re: Eqset and Robes">

If you messed with eqset show, listing the socketed gem might be nice too.

I'll give the revolving robe thing a go when I get back this afternoon.

There are ma regen and mp non drachma robe options that are containers... Homespun, and Shroud, they are just kind of involved and more difficult forges. I tend to recall the shifting cloak having such a bad pop rate in s3 I got an imm to check it and eventually gave up, I think it's the only time I gave up on a forge (and I soloed my own infernite gauntlets!). Maybe I just have to bite the bullet again.

If what Zuzu says is correct, there are still kind of annoying issues, but at least I can wear different robes.

</div>

<div class="post" data-post-id="38355" data-author="Teron" data-date="2017-07-29T07:15:58+00:00" data-subject="Re: Eqset and Robes">

1\. Zuzu, what happens when you go from myrmidon to healer and back? It should create a loop, as it does for me - I've created the suggested circle myself.

2\. I've just ideased yesterday, that if there is a loop, run it once:

\- put the worn robe in the non-worn container

\- wear the container, if necessary

\- stop executing the loop.

If you wear a non-container robe, like a shifting cloak, as I do, then you are screwed, unless you also use another wearable container. However, it is not an option in a maxmana set - there are no containers with max mana.

3\. I have to remind you that even 500 size is too small for current amount of sets: [we need to at least double robe sizes](http://www.slothmud.org/forum/viewtopic.php?f=30&t=4678) to be able to wear all the sets for each of our classes, and some classes have several sets (ac/weap dam, hit/hit-saves, ac-saves/ac/ac+charisma).

Changing raven's feather robe to 500 or more would make the homespun linen robe forge obsolete, because it requires a cp from a chop mob and a few other Lyme cps, and it costs 7.5mil. I kind of like the name, though.

4\. Making worn eq count would make things worse, unless strength bonus is increased dramatically.

Not counting worn eq means that:

\- worn eq doesn't count

\- anything in worn containers doesn't count, hence robes.

If you make us count all the weight, like it's done in Aardmud, then we'd need to increase weight allowance drastically, both from strength and inv size.

So far, I can see that the loop can be easily(?) fixed.

As for non-container robes, making them containers would work, but would also make some containers obsolete, including the linen robe (there is a +wis +mr non-container).

Maybe allow us to upgrade robes from linen to a shifting linen robe: -0.0 +mr +15ma, 1k container. That'd work for me, and would also decrease item count.

</div>

<div class="post" data-post-id="38356" data-author="Gorka" data-date="2017-07-29T14:08:32+00:00" data-subject="Re: Eqset and Robes">

> <strong>Teron wrote:</strong>
> Not counting worn eq means that:
> 
> \- worn eq doesn't count

\+1

</div>

<div class="post" data-post-id="38357" data-author="Gorka" data-date="2017-07-29T15:03:07+00:00" data-subject="Re: Eqset and Robes">

I'm still lost Teker... how do I do this...

Equipment Set 'ac':

Position Item Container

Light a glowing bauble with \`Gorka\` Cloak of Shadows

Left Finger the titanium ring of glory Cloak of Shadows

Right Finger the titanium ring of glory Cloak of Shadows

Neck 1 ankh of purity Cloak of Shadows

 Clasp a golden oak tree charm Cloak of Shadows

Shoulders guards of the maul titans Cloak of Shadows

 Clasp a golden oak tree charm Cloak of Shadows

Body Adamantine Cuirass of the Anci Cloak of Shadows

 Clasp an emerald serpent brooch Cloak of Shadows

Head a ruby dragonscale helmet Cloak of Shadows

Legs Elven Chain Leggings of the My Cloak of Shadows

Feet gleaming dragonscale sabatons Cloak of Shadows

Hands Adamantite-plated Snakeskin Ga Cloak of Shadows

Arms a set of carved bone armplates Cloak of Shadows

Shield Walls of Jericho Cloak of Shadows

 Clasp a dragon emblem Cloak of Shadows

About Cloak of Shadows Cloak of Shadows

 Clasp a blazing starburst ruby (Hero Cloak of Shadows

Waist Tooled Girdle of Ogre Kings Cloak of Shadows

Left Wrist a rune-carved loop of green ad Cloak of Shadows

 Clasp some stardust Cloak of Shadows

Right Wrist a rune-carved loop of green ad Cloak of Shadows

 Clasp some stardust Cloak of Shadows

Wielded a double bladed battle axe [ Default ]

Held Sacred Relic of the High Palad Cloak of Shadows

\<1441hp 602ma 400mv 11118372097xp -13.5ac -%\>

You are carrying:

a keg of icybrau

a white silk robe

a mithril keychain

a wheel of opportunity..It has a soft glowing aura!

an ornate scrolled post..It emits a faint humming sound!

a large leather backpack

swirling black and red robes

\---------------------------------------

Equipment Set 'regen':

Position Item Container

Light a glowing bauble with \`Gorka\` Cloak of Shadows

Left Finger a wiedzmin ring Cloak of Shadows

Right Finger a wiedzmin ring Cloak of Shadows

Neck 1 a choker of midnight sapphires Cloak of Shadows

Neck 2 a choker of midnight sapphires Cloak of Shadows

Body a gilded corset of crimson and Cloak of Shadows

Head a silver circlet Cloak of Shadows

Legs sandy silk pants Cloak of Shadows

Feet a pair of jade slippers Cloak of Shadows

Hands a set of emerald gauntlets Cloak of Shadows

Arms silver cloth sleeves Cloak of Shadows

Shield a swirling shield of sparks Cloak of Shadows

About a homespun linen robe Cloak of Shadows

 Clasp a blazing starburst ruby (Hero Cloak of Shadows

Waist a clipped feather Cloak of Shadows

Left Wrist a band of ether Cloak of Shadows

 Clasp some stardust Cloak of Shadows

Right Wrist a band of ether Cloak of Shadows

 Clasp some stardust Cloak of Shadows

Wielded a sliver of midnight Cloak of Shadows

Held a runed taffeta pouch Cloak of Shadows

\<1439hp 604ma 402mv 11118372097xp -1.1ac -%\>

You are carrying:

Cloak of Shadows ()socketed Eye Agate Rune() [PROBLEM]

a keg of icybrau

a white silk robe

a mithril keychain

a wheel of opportunity..It has a soft glowing aura!

an ornate scrolled post..It emits a faint humming sound!

a large leather backpack

swirling black and red robes

\---------------------------------------

How have you designed this to work? If my default container is my cloak of shadows which contains all my eqsets... how can I switch to regen mode and not have my cloak of shadows in my inv, but instead inside my Homespun Linen Robe?

</div>

<div class="post" data-post-id="38358" data-author="Teron" data-date="2017-07-29T15:22:54+00:00" data-subject="Re: Eqset and Robes">

wear the ac set

have linen robe in the inv

eqs setc linen shadows

</div>

<div class="post" data-post-id="38359" data-author="Gorka" data-date="2017-07-29T19:11:46+00:00" data-subject="Re: Eqset and Robes">

Thanks Taron, that resolved my issue.

</div>

<div class="post" data-post-id="38360" data-author="*Idjit*" data-date="2017-07-30T00:14:36+00:00" data-subject="Re: Eqset and Robes">

As regards Teker's question about whether for a non-container robe if another non-robe item is equipped that's a container, I'd have to remind us that it's a long standing thematic thing on Sloth, indeed in Diku's in general, that the about-body containers are at least twice the size of the capacity of something like a waist-worn beltpouch or a held-low bag, unless the bag is something crazy like a Portable Hole. The robes are simply conceived as something much bigger than the other varieties, and certainly bigger than a 'trick' container like the boots of radiance.

So even if they did have a non-about-body container equipped, their container-robe isn't going to fit into it.

Asserting that that robe is mostly full of goodies (as it will be for the people concerned enough to raise the issue).

...By a factor of at least 2 to 1.

Did that make sense?

</div>

<div class="post" data-post-id="38364" data-author="*Breeze*" data-date="2017-07-30T05:05:00+00:00" data-subject="Re: Eqset and Robes">

It's a robe, not a Tardis. <img src="/images/smilies/icon_e_wink.svg" alt=";)" title=";)" width="15" height="15" class="smiley nozoom">

</div>

<div class="post" data-post-id="38366" data-author="Gorka" data-date="2017-07-30T06:10:33+00:00" data-subject="Re: Eqset and Robes">

It probably would have been better/easier if items weren't containers at all. Instead players had a bigger/private "on person" inventory were stuff was stored. Item attributes could affect the size of that inventory, but putting items in items wouldn't be a thing. Storage space would not be directly linked with robe size. Certainly gets around the fact that any robe that is not a container is almost completely useless.

I don't know which is worse... a large safe/invisible/formless inventory... or pretending that all those 110 items can actually fit in a robe that I am wearing... what would that even look like? Maybe my joke about Taron's eq modes probably isn't off beat, if you were to consider the size of the objects in our robes that we apparently carry with us.

I guess the smaller and open inventory we have in sloth was partially due to the pthief implementation, or maybe it's just traditional DIKU design. In any case it's one of those issues where to some degree you could argue for change but on the other hand, it's always worked this way - and you just can't sell out some traditions or the game starts to loose it's identity.

</div>

<div class="post" data-post-id="38367" data-author="Teron" data-date="2017-07-31T07:52:21+00:00" data-subject="Re: Eqset and Robes">

1\. I agree that having universal weight limit, regardless whether the item is worn or not would be proper. It even makes more sense.

Aardwolf has this system, where strength defines the total amount and weight of items, but inventory isn't limited to a much smaller amount.

Maybe that's what we need: to <strong>increase inv weight allowance drastically</strong>? It wouldn't fix the mess with the robes, though.

2\. I don't agree that containers should go: there are containers, and it'd be silly not to use them to categorize items, because you can't possible deal with all the 175 items in a single list in the inv.

I'd store my weapons in a chest, and all my scrolls in the dwarvish scroll bag, which is already a thing.

3\. <strong>JB had suggested crafting a keychain type storage for armor</strong>, a Sidhe Extra-Dimensional Portable Armory.

Read the discussion from this post:

[http://www.slothmud.org/forum/viewtopic.php?f=30&t=4678#p37438](http://www.slothmud.org/forum/viewtopic.php?f=30&t=4678#p37438)

It'd have -1 weight and would remove armor from the counted items.

It'd solve the logical issue of fitting items on a character, because 120+ armor items wouldn't be far from requiring a wagon or a pack horse to move.

<strong>It'd solve the robe-putting circle</strong>, because it'd only be used as defaultcontainer, wouldn't be worn and included in any eq set.

4\. Therefore, a temporary solution for players would be to <strong>use a neutral container for robes</strong> that isn't used in any of the sets.

5\. The point of "this has always been this way" is moot - [an appeal to tradition](https://en.wikipedia.org/wiki/Appeal_to_tradition), in fact - because we can and should look how to <strong>make the game better, and also better, than other games</strong>, so players prefer this game, not others.

</div>

<div class="post" data-post-id="38368" data-author="Gorka" data-date="2017-07-31T09:21:29+00:00" data-subject="Re: Eqset and Robes">

> <strong>Teron wrote:</strong>
> 5\. The point of "this has always been this way" is moot - [an appeal to tradition](https://en.wikipedia.org/wiki/Appeal_to_tradition), in fact - because we can and should look how to <strong>make the game better, and also better, than other games</strong>, so players prefer this game, not others.

I agree, Sloth needs surface to surface missiles and tanks, lets be progressive... ya dumb ass liberal, your playing a medieval sword play text based game and now your getting all "progressive!" Your ideology will be the ruin of this world, because liberals are full of contradictions... Liberalism isn't really a belief system, <strong>it's an excuse for people to get things there own way while justifying their own selfishness</strong>... unfortunately I suspect in my lifetime we will find out just what a poisonous ideology liberalism is, albeit too late after it's destroyed humanities identity, meaning and unity. <img src="/images/smilies/icon_evil.svg" alt=":evil:" title=":evil:" width="15" height="15" class="smiley nozoom"> Don't tell me I'm wrong because I'm old fashioned... <img src="/images/smilies/icon_evil.svg" alt=":evil:" title=":evil:" width="15" height="15" class="smiley nozoom"> Maybe I'm smart enough to understand that my forebears might have learned something that I don't understand in their lifetimes. Show some respect young punk! Their is an "essence" that is Sloth, and it's why we are here, and it must be protected. Do you forget we lost half the player base over the change to 8 classes? (Once again libtards were the ones who pressed for this change - how much better the world would be with 8 classes... WHERE ARE THEY NOW?) Whether robe changes, would effect sloth's "essence" is up for debate... but you discrediting something based on "an appeal to tradition" being wrong, is just typical dumb ass subjective liberal arrogance stated as fact.

The reality is Taron, your whole argument is really, "I want bigger robes/storage/capacity!" What's entertaining to me however is how you are trying to pass off your argument... as being progressive, intuitive, ENLIGHTENED and better... but we aren't that dumb Taron, we all know you just want bigger robes, cause your Taron. I think most people accept that the robe and container system is a bit quirky, but just be honest... you have your opinion (that's fine)... don't try and make your opinion out like it's the only factual way, and that other people's ideas are inferior. It's simply not true, and no one is that dumb. Such an attitude generally just tends to tick people off and no one gets anything.

</div>

<div class="post" data-post-id="38370" data-author="Teron" data-date="2017-07-31T15:34:17+00:00" data-subject="Re: Eqset and Robes">

Gorka, we are trying, presumably, to have a civil discussion, so I have to remind you that we are discussing ideas, not persons. So try to stick to that, please. Or is this a dumb libtard idea, too? If so, explain why, albeit in a different thread.

1\. I never mentioned tanks, missiles or anything of the sort. Your argument against them is [a straw man argument](https://en.wikipedia.org/wiki/Straw_man), so I won't really address it.

I did mention a keychain-type item that'd house eq, because:

\- robes already allow for dozens of heavy items to fit in them, which is unrealistic physically, yet the game is designed so that it'd work for players

\- we already have keychains

\- we already have the kangaroo pouch

\- we already have the bag of weapons that nulls the weight of the items we put in it, but not the number of items, which is why the chopper carrier is almost always ladden, if he carries 20-40 choppers

\- we are already carrying 175 items that weigh far more, than a single person can carry, which is already a fact. Oh, look:

> <strong>Gorka wrote:</strong>
> I don't know which is worse... a large safe/invisible/formless inventory... or pretending that all those 110 items can actually fit in a robe that I am wearing... what would that even look like?

\- all these items are powered by magic, which explains how so many unimaginable things can happen.

The next logical step to make is to assume that sidhe magic and smart gnomish engineering would produce an item that combines both of these qualities, albeit in a limited fashion, applying only to armor.

2\. I am also ignoring your blurt about liberalism, because it's another straw man argument.

If you want to argue against it, argue against the solutions that'd fix our eqset and/or weight problems.

Do you want a simpler solution? Suggest it.

Do you want imms to just count all the weight on character and remove weight limit on inventory? Suggest it and insist on it, rather than derail from the subject.

3\. What exactly is the essence of Sloth?

Why can't we move make things better for players within the boundaries of that essence?

I can't find any mention of this on the homepage or in the features, but I remember someone, who shall not be named, say something along the lines of "we are slothy, and we allow players do some things easily". We could all argue, whether this is true, though.

So, what are the maxims/rules that describe the essence of Sloth and where exactly am I not following them in even mentioning the keychain-type armor container?

And you suggested the bigger single inventory, not me:

> <strong>Gorka wrote:</strong>
> Instead players had a bigger/private "on person" inventory were stuff was stored.

I simply said that it's viable - because it's already done elsewhere and it works great, and it can be easily implemented, which means it should be the first to be considered, perhaps.

Though I do think that we could use a magic item, which would actually embody the world, where magic and engineering can solve some of our problems, akin to keychains, teleport items, greater beacons and such, and that'd match the only description of the essence of Sloth that I remember: allowing people to be slothy literally.

4\. If you [read my initial post about robes](http://www.slothmud.org/forum/viewtopic.php?f=30&t=4678#p37399), you'd learn that my robe issue is the direct result of adding more classes, and doing nothing about the robes. It's like buying a powerful engine, but not changing the transmission: the car would be even harder to steer.

If you spend the same effort, as I did, on making eq sets, you'd also run into this problem. 

If you are against an idea that we should have eq sets for the classes we have - since you've just brushed it off, then write it down in that thread, too. However, I know that you are/were building a charisma set for your 7th class, bard, so maybe you \*are\* fine with having eq sets for non-prime classes?

If so, then why do you think the robe sizes is just about me?

I even suspect that you are not far behind me: you'd only need a stab set, an UC set and a raise set to match my gear.

5\. Now, about this being only about me.

> <strong>Gorka wrote:</strong>
> your whole argument is really, "I want bigger robes/storage/capacity!" What's entertaining to me however is how you are trying to pass off your argument... as being progressive, intuitive, ENLIGHTENED and better... but we aren't that dumb Taron, we all know you just want bigger robes, cause your Taron

If you think that I post my ideas to support some image on the forum, then this idea is incorrect.

I actually believe in what I write, Gorka.

Since I've returned, I've put months of my real life time into playing the game. I do many things, and run into problems, which I report via ideas, bugs or the forum, when the issue is major and/or needs a discussion. It's only natural that those, who do not play 9x40 chars or do not have 10+ eq sets - we both have seen 9x40 chars w/o a regen set, do not run into the problems that I face. 

I do not think that my ideas are 100% right, that's why I'm putting them up for discussion, so we find a better solution, because I don't and can't know everything.

When I suggest my ideas, I do try to frame them into the Sloth universe, so we'd see:

\- what led to the idea

\- why this is a problem

\- why the solution shouldn't break the game

\- why the solution would only enhance the previously indescribable essence of the game.

I also think that suggesting actual, precise solutions is easier on the immorts, because they:

\- don't have to spend their time/effort on storytelling the idea

\- can just decide whether it's good or not and implement it

\- are more likely to review and/or accept the idea, presumably.

Immorts, please point out if I'm wrong, so I don't have to spend time on this <img src="/images/smilies/icon_e_biggrin.svg" alt=":D" title=":D" width="15" height="15" class="smiley nozoom">

If I'm wrong there, explain why and suggest better - which is why I'm posting on the forum! Just please do it in a separate thread to avoid thread hijacking and us not discussing the topic at hand: eqset, robes and maybe weight, if it's even related.

When I mentioned that removing containers would be silly, please note that:

\- I attacked the idea, not you, and pointed out a potential issue we'd face

\- it actually goes against what has been done in Sloth, which goes against your argument of saving the Sloth legacy

\- even looking through 80 items on auction is troublesome without a filter, how would we deal with 157 items in our inventory in a single list? there's a problem, but you offered no solution to this.

Furthermore, I don't think anyone is dumb, I think that the combined knowledge and skill of people around here is immense and it should be put to better use via a collaborative effort on the forum to solve the problems we have as easy as squishing an ant with a hammer.

And lastly, I share your passion for the game, and I hope we both agree that we need to address the issues we face, rather than sweep them under the rug.

So, if you don't like my ideas, attack the ideas, not me.

Cheers,

T

</div>

<div class="post" data-post-id="38371" data-author="Gorka" data-date="2017-07-31T16:56:52+00:00" data-subject="Re: Eqset and Robes">

Taron, my point is why can't you just state things honestly... you want more capacity... why do you try to invent some "alternative truth justification" to achieve your aims.

> <strong>Quote:</strong>
> The next logical step to make is to assume that sidhe magic and smart gnomish engineering would produce an item that combines both of these qualities, albeit in a limited fashion, applying only to armor.

Forget the gnomish/magic crap... Teker, Taron would like more space... please consider. There, It's done.

Reminds me of when I was younger and I used to go down to the ball courts with a friend, and using rocks and sticks we'd dislodge the stuck tennis balls and other balls stuck in the wire fence. One day I knocked one out and my friend ran over and picked it up and he said "Can I keep this one, since I touched it first." Why didn't he just say... I like this ball, can I keep it? Instead he added this crappy justification of "touching it first" when he knew I had purposefully and resourcefully done all the work to dislodge that specific ball in order that I could keep it.

This thread was originally about the eqset command, and my issue was resolved. I knew you'd be along to whine about robe issues, and you do have some points... my issue is how you choose to make those points. Your like a woman hinting and whining about something, why can't you just come out and say it... Do you really think Teker and Breeze are incapable of reasoning why you have suggested your ideas... and do you REALLY want to base part of your ideas on some crap about Gnomish magic as part of your massive onslaught as to why anyone would be so stupid enough as to not like your ideas, and how in keeping with the game they are.

For the record, I do find the sloth inventory quirky, and not being able to pick up food a pain in the proverbial. However my robes don't often exceed 120 items... because I am aware of weight issues, I structure some things around this problem to minimize it. I don't know of any other player other than Taron that struggles to keep his worn eq's limited to 175 items.

Yes, I've acquired 4 or 5 items of charisma, but I vault them, and even if I robed them... I'd still have 50 more items to store in my robe.

8 classes, 8 eqsets, 17 slots in a set... = 136. It's pretty reasonable when you consider there are 40 more slots than we need to store other sets and items. As for item weights, well that's the part I find quirky. I don't think weight should matter whether it's worn or not and perhaps the inventory size/capacity is small for picking up crap until I can vault it.

So you want to be able to say what you want to say, get what you want, and not be open to any criticism that comes against your ideas or the manner you make those ideas? How convenient... how liberal...

</div>

<div class="post" data-post-id="38372" data-author="Teron" data-date="2017-07-31T17:56:52+00:00" data-subject="Re: Eqset and Robes">

A minor clarification: I think that preparing an idea makes it easier to get implemented, because imms need less time for it. It does not affect whether to accept the idea or not.

Please show exactly where I am not open to criticism about the robes idea?

I am open to criticism, but I disagree with you, because you left out that:

\- a class may need 2 sets, like ac/wd for warrior

\- sets can be incomplete, yet still take 5-10 items

\- everyone needs mr/maxma and maybe +hit sets for chop, that's 3 extra.

I have 6 full sets that I regularly use with about 5 misc sets with 4-10 items. This alone is at 138-158 items, then there are

\- 20 items in my sack

\- 9 containers in the inv (sack, keychains, magic bags)

\- -int gear in the robe, etc.

I do try to keep my inv and sack clean, but it's only been comfortable since Teker upped the item limit. If I keep popped eq in my robe, it remains in my inv (current weight of default container 466).

And yeah, I prefer to provide all the details about the problem and the solution, because I've had enough ideas rejected on unreasonable grounds without further discussion, so I want to make a point about the problem for it to get noticed and get fixed.

</div>

<div class="post" data-post-id="38373" data-author="Gorka" data-date="2017-07-31T18:40:57+00:00" data-subject="Re: Eqset and Robes">

Sloth is a fantasy game, but it does take on a fair amount of realism from the natural world. It's not uncommon for games to have inventory limits, in fact I can't think of a game I've played off hand that didn't have an inventory limit. Having limits means players need to employ strategy and management, it's supposed to be a feature not a hindrance. 

For me there is some value in tradition, as backwards or as much of a "moot point" that might be for your liberal/pseudo factual sensitivities... 

I think 175 as an item limit is quite reasonable, there have been plenty of containers added to the game to make this more manageable... by making things TARON\_SIZED + 1, I'm hesitant to say that the game would actually gain something, because you are an extreme player, and outlier. 

A game is basically a collection of rules and traditions players enjoy of which there would now be less of, if we just went all liberal with everything and reduced the number of rules and laws. Sloth could loose some of it's flavor. That's what an imm's job is supposed to protect. If everything becomes open and possible, it's like playing a game with cheat codes... satisfying for the first 30mins, but empty afterwards when the struggle was gone. 

Could you even just consider for one minute the game might be better for having the limit, than without it? What if tennis just decided to get rid of it's "advantage" concept at break point... how do you think that would go down? Does it make tennis a better game? Would it be the same? Somethings are there just because they are and we love them and hate them for that reason, but there is no denying it's the struggles players go through that give something it's identity, and it's hard to define why that's important, but I think it is. "Welcome to the Struggle."

</div>

<div class="post" data-post-id="38374" data-author="Teron" data-date="2017-07-31T19:14:46+00:00" data-subject="Re: Eqset and Robes">

I disagree that the point of this game is to suffer unnecessarily by lugging robes in the inv, not being able to pick up food or loot.

There's a difference between soloing 2bil exp and soloing 2bil exp with a robe in your inv.

Oh, by the way, you are trying to tell me that 150 items is normal, but the amount of items on a character isn't directly related to this problem, it's how much they weigh together in a single robe you are wearing (or not).

Other points aren't constructive, so I guess I'll just bow out of this thread.

Cheers,

T

</div>

<div class="post" data-post-id="38375" data-author="Gorka" data-date="2017-07-31T19:32:28+00:00" data-subject="Re: Eqset and Robes">

> <strong>Teron wrote:</strong>
> I disagree that the point of this game is to suffer unnecessarily by lugging robes in the inv, not being able to pick up food or loot.

The point is, you are supposed to manage this limitation, other people can, why can't you? Should the game be changed every time you can't do something, and is everyone else inferior if they don't agree with you?

</div>

<div class="post" data-post-id="38376" data-author="cyprimus" data-date="2017-08-02T16:55:06+00:00" data-subject="Re: Eqset and Robes">

Never had this problem, but reading it and it occurred to me, maybe we could make personal items not count?

Making them part of the special platonic inventory gorka suggested?

</div>

<div class="post" data-post-id="38377" data-author="Gorka" data-date="2017-08-02T20:25:11+00:00" data-subject="Weight Absurdity!!!">

Imms, this is a perfect example of the frustration... 

You stop using Cloak of Shadows.

\<1148hp 543ma 268mv 16504026254xp -8.4ac -%\>

Ok.

You feel informed:

Object 'cloak shadows elite low \*Gorka\*', Item type: CONTAINER

Maxweight: 500

Item is: HUM PERSONAL RESTRUNG 

Weight: 381, Value: 295drachma, Worn in: TAKE ABOUT 

Can affect you as:

 Affects: ARMOR by -5

 Affects: REDUCE\_DAMAGE by 2

 Affects: ARMOR by -1 (a blazing starburst ruby (Hero))

 Affects: HITROLL by 2 (a blazing starburst ruby (Hero))

 Affects: MANA by 20 (a blazing starburst ruby (Hero))

 Affects: HITPOINT by 20 (a blazing starburst ruby (Hero))

 Affects: SAVING\_SPELL by -2 ()Eye Agate Rune()

Only those who are at least adept monks may use this item.

"STAT STRENGTH" STRENGTH STR

See Also: INTELLIGENCE WISDOM DEXTERITY CONSTITUTION 

See Also: STATS STAT ORDER 

Strength (STR) increases the damage of your attacks as well as the

effectiveness of pushing, bashing and also how much equipment you can carry.

Str Hit/Dmg Carry Weight Max Weapon Weight

14 1/1 220 14

15 2/2 230 15

16 2/3 250 16

17 3/3 270 18

18 3/4 310 20

19 4/4 340 40

20 4/5 380 40

21 5/5 400 40

22 5/6 420 40

23 6/6 460 40

24 7/6 500 40

25 7/7 550 40

So I am wearing my robe, but if I drop my robe and have anything less than 21 strength I can't pick up the robe that I was wearing!

Furthermore because I was in regen mode... my default container, cloak of shadows is inside the homespun linen robe. So if my homespun linen robe hits the ground, I am unable to pick it up, <strong>and I am unable to get my strength eq out from the cloak of shadows inside the the linen robe.</strong> The problem becomes recursive... no strength to pick things up, and no way to get the robe out of your cloak to get your strength eq to pick things up... you are completely stuck unless a strong person can lift your cloak from your robe.

I had to ask Zuzu, to get Idjit, to remove the cloak of shadows from the homespun linen robe... to pick up my strength eq, to wear my strength eq, to pick up my robe, when before I dropped my robe, I has happily wearing all this eq.

Furthermore, why are most robes 500 max weight, when most people will need 21 str to even pick that up, anyone that's not a higher level warrior can't even really deal properly with that size anyway.

</div>

<div class="post" data-post-id="38378" data-author="Teron" data-date="2017-08-03T12:07:42+00:00" data-subject="Re: Eqset and Robes">

<strong>Gorka</strong>,

> <strong>Quote:</strong>
> I don't know which is worse... a large safe/invisible/formless inventory... or pretending that all those 110 items can actually fit in a robe that I am wearing?
> 
> 
> 
> Fixing a problem by adjusting strength weight values or finding another solution is too liberal. Liberalism isn't really a belief system, <strong>it's an excuse for people to get things there own way while justifying their own selfishness</strong>.
> 
> 
> 
> Maybe I'm smart enough to understand that your forebears might have learned something that I don't understand in their lifetimes. Show some respect young punk! Their is an "essence" that is Sloth, and it's why we are here, and it must be protected.
> 
> 
> 
> Thus, we need to reduce robe sizes by 2-3 times, so players can't carry way more weight, than their strength allows, because immorts changing strength values, inventory size or item weighs would be too cumbersome and liberal.
> 
> 
> 
> I urge immorts to:
> 
> \- restrict the number of eqsets to 5
> 
> \- limit the number of items per robe to 20
> 
> \- make it impossible to store food in the robes, because storing too much lutefisk is overpowered and must be nerfed for the sake of the Sloth essence we love the game for.
> 
> 
> 
> Forget providing examples, listing help files, explaining the issues you face, so imms would understand the problem better... "Teker, Gorka would like to work with robes easier... please consider". There, It's done. 
> 
> 
> 
> A game is basically a collection of rules and traditions players enjoy of which there would now be less of, if we just went all liberal with everything and reduced the number of rules and laws. Sloth could loose some of it's flavor. That's what an imm's job is supposed to protect. If everything becomes open and possible, it's like playing a game with cheat codes... satisfying for the first 30mins, but empty afterwards when the struggle was gone. 
> 
> 
> 
> New players must:
> 
> \- endure the very first levels
> 
> \- suck at soloing exp
> 
> \- not be able get good eq on their own
> 
> \- cycle the same 5 gold areas until eternity
> 
> \- have trouble managing their robes despite the game having changed so much in 20 years.
> 
> 
> 
> Their is an "essence" that is Sloth, and it's why we are here, and it must be protected.
> 
> 
> 
> For me there is some value in tradition, as backwards or as much of a "moot point" that might be for your newly found liberal/pseudo factual sensitivities... 
> 
> 
> 
> I think that:
> 
> \- 310 weight limit for 18 strength and 500 weight size for robes are quite reasonable
> 
> \- it's insanely easy to roll 3x18 to get 15-18 natural strength
> 
> \- there are high strength druid forms
> 
> \- there have been plenty of containers added to the game to make this more manageable
> 
> \- worn items don't count for weight
> 
> \- it's very easy to manage your item weight, even a child or a new player could do it.
> 
> 
> 
> so... by making the inventory GORKA\_SIZED + 1, I'm hesitant to say that the game would actually gain something, because you are an extreme player, and outlier. 
> 
> 
> 
> You are the only one posting about the problem of picking up robes from the ground, therefore you are the problem, not the game we all love and strive to protect.
> 
> 
> 
> The reality is Gorka, your whole argument is really, "I want more strength/inventory weight/lighter items!" What's entertaining to me however is how you are trying to pass off your argument... as being progressive, intuitive, ENLIGHTENED and better... but we aren't that dumb Gorka, we all know you just want to become stronger to carry more lutefisk, cause your Gorka.
> 
> 
> 
> I think most people accept that the robe and container system is a bit quirky, but just be honest... you have your opinion (that's fine)... don't try and make your opinion out like it's the only factual way, and that other people's ideas are inferior. It's simply not true, and no one is that dumb. Such an attitude generally just tends to tick people off and no one gets anything.
> 
> 
> 
> The point is, you are supposed to manage this limitation, other people - even my characters with default 12 strength - can, why can't you? Should the game be changed every time you can't do something, and is everyone else inferior if they don't agree with you?

This is what it'd look like, if I were attacking you personally. Would you have liked it?

In practice, I think what you are trying to say is that I'm unnecessarily babbling about a user error, not a system error. So I've realized that:

\- I do provide backstory, examples and possible issues precisely to point out that this is a <strong>system</strong> error

\- me noticing a system error doesn't make it a user error, it just makes it an error that few ppl complain about

\- immorts can prioritize to not fixing this, because so few ppl report it

\- or they can run a survey or examine stats on used robe sizes and extrapolate our experience with other players.

I know how to handle extra weight a character can't carry, especially in your case.

Does it lessen your problem? Do you want to get it solved systemically, or you want to be using the workaround forever?

If we assume that:

\- since we have 8 classes, we at least should be able to use a full set of eq for each of them, plus a regen set. That'd put item count to 162 items that weight about 400-500

\- we should be able to manage those items with our natural character strength

\- this is a system problem, and players run to it from time to time, so it needs to be a system solution,

then we could:

\- be less stingy on trying to make players' life miserable by limiting their ability to handle the eq they own, not all their hogged eq

\- increase weight bonuses from strength by x1.5 (or shift weight values up by 4 lines in the help files, however you look at it), thus increasing inventory size

\- add \-item weight X% stats to large containers (backpacks, chests) and robes, from 10% to newbie robes, -50% to avatar robes, to 70-90% for quest robes - they'd still be limited by the container size

\- add container size property to containers, so keychain type container weight can be set to -1, because right now they still weigh their capacities when they are inevitably full (keychain is 45, silk bag 120, flux 15, dwarvish bag 41), which reduces inv capacity for other items.

Now, if I were trying to angry the Gorka with marketing, I'd say that:

\- one of our prime competitors in the TMC top list, Aardwolf, already has solved this problem

\- their solution works

\- if we want to become a better game, we should provide less friction, than we currently have. It doesn't mean no friction: it still should not be possible to hog thousands of items on a person

\- immorts are free to research how other MUDs have solved the expanding weight problem and act accordingly (or conjure/hire imps to do this)

\- WoW, SWTOR and any other MMORPG that wants its players playing introduces larger bags and ways to expand player inventory (not just banks/vaults) every content expansion that happen every 1-2 years.

But I won't, that's for who it may concern.

Cheers,

T

</div>

<div class="post" data-post-id="38379" data-author="Gorka" data-date="2017-08-03T14:08:16+00:00" data-subject="Re: Eqset and Robes">

Ok, that was a lot of writing, so I guess I hit a nerve...

The increased item count to me was something people "want." It's a request. So you ask nicely and leave it... When I was younger the longer I made my justification speech to my parents about why I deserved ice-cream, the less likely I was to get ice-cream, and the more I made it sound like it was my right not a privilege, the more it ticked off my parents. Playing sloth is a privilege not a right... we can only ask, this convincing overpowering defended to the death backstory you try to do is just too much.

The robe weight thing to me is a contradiction. How is it possible to wear that which you can't pick up? The game is violating it's own rules, there is no consistency. I really expect that should be fixed.

The battering I gave you was meant for your own good, albeit it from frustration in the past with myself. An yeah my reaction doesn't solve any problems either, I know... But you'll never win an argument intellectualizing things, and systematically eliminating other people's POV with so called "facts" which belittles an other's view, all you are doing is alienating yourself. This method always looses.

Are you going to keep trying to win arguments quoting from this list...? https://en.wikipedia.org/wiki/List_of_fallacies The only recognition you'll get is that your an a$$hole - believe me... and the more you embrace how right you are, the more blind you'll be when you're wrong. Discussion is fine, but when you say something, you're too much, you try to convert them.

This thread is ugly now. It's a shame. No hard feelings.

</div>
