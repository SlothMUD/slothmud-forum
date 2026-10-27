---
title: "How do _you_ carry multiple sets of equipment?"
topic_id: 4559
author: "*teker*"
date: 2015-12-22T18:03:37+00:00
last_activity: 2015-12-23T09:09:13+00:00
last_author: "Teron"
sticky: false
locked: false
post_count: 11
---

<div class="post" data-post-id="36345" data-author="*teker*" data-date="2015-12-22T18:03:37+00:00" data-subject="How do _you_ carry multiple sets of equipment?">

I'm about 90% of the way through some new code that will make it easier to switch between different sets of equipment. The last part I need to figure out is what to do with items that are removed as a result of wearing new gear. So for players that carry around multiple sets of equipment: How do you manage them as far as containers go? I tend to just shove everything into my cloak all together. Do you guys do the same? Or do you put different outfits in different containers? Like I said, I've got an easy way to wear new gear - the question is what to do with the old equipment that comes off as a result.

</div>

<div class="post" data-post-id="36346" data-author="Sam" data-date="2015-12-22T18:24:28+00:00" data-subject="Re: How do _you_ carry multiple sets of equipment?">

HI, personally I use different containers,

a separate container for each set for permament storage and one container for temporary storage.

</div>

<div class="post" data-post-id="36347" data-author="Filk" data-date="2015-12-22T18:37:00+00:00" data-subject="Re: How do _you_ carry multiple sets of equipment?">

Just keeping everything in one main robe. Just to avoid problems when item exists in multiple eq sets at same time.

Would be lovely to have some command in which you specify a container first, and then items you want wear from that container. With automatical removing current equiped item, which is auto moved into that container.

Most ppl use different containers just because you can get everything from it at once with 'get all from robe'. If moving items from container and back to it will be auto, then there will be no real need in multiple robes from different sets.

Like

switcheq robe item1 item2 item3 item4...itemN

With result displaying only to you in form of

You wear item1 and put old-equiped-item into robe

You wear item2 and put old-equiped-item into robe

No item3 in robe to wear it

You wear item4 and put old-equiped-item into robe

etc.

And other ppl should just see single message about you switching some eq...

Maybe that command even should ignore, that robe is weared on you atm and still works in that way <img src="/images/smilies/icon_e_smile.svg" alt=":)" title=":)" width="15" height="15" class="smiley nozoom">

</div>

<div class="post" data-post-id="36348" data-author="alris" data-date="2015-12-22T18:45:07+00:00" data-subject="Re: How do _you_ carry multiple sets of equipment?">

Concerning eq sets, separate robe for each set, robe keyword essential. Each robe contains its own set, all the robes with equip are inside the robe i am currently wearing. Nothing else, only robes in current robe.

Something like that?

By the way, will this new feature properly switch clasps? largely missing detach/attach all, so anything in this direction would be very welcome.

</div>

<div class="post" data-post-id="36349" data-author="*teker*" data-date="2015-12-22T19:27:30+00:00" data-subject="Re: How do _you_ carry multiple sets of equipment?">

> <strong>Quote:</strong>
> And other ppl should just see single message about you switching some eq...

This will depend on the player's GAG\_EQ flag.

> <strong>Quote:</strong>
> By the way, will this new feature properly switch clasps?

I hadn't thought about swapping clasps or removable runes. This probably won't happen in version 1 but I'll make some changes to make it easier to implement in the future.

Does anyone use multiple containers of the same type to store different sets? For instance, 2 golden sacks where each contains a different set? The current code flips the item list backwards at rent and probably at death so it seems like this would be confusing.

</div>

<div class="post" data-post-id="36350" data-author="Dragoth" data-date="2015-12-22T19:30:59+00:00" data-subject="Re: How do _you_ carry multiple sets of equipment?">

I use a mix- 

1\) separate containers for partial but important sets that need to be switched quickly (like healbonus or charisma)

2\) one huge container (sack) for all the random crap and eq sets which consist of only a few items and is rarely used (like shock set and spelldam set) 

3\) one main robe to store both regen and solo modes, as only one of those is used at one time.

</div>

<div class="post" data-post-id="36351" data-author="alris" data-date="2015-12-22T20:16:45+00:00" data-subject="Re: How do _you_ carry multiple sets of equipment?">

> <strong>\*teker\* wrote:</strong>
> I hadn't thought about swapping clasps or removable runes.

Thats probably a mistype, but we don't swap runes on changing eq sets, right?

using 2 same named items for storing - i dont and doubt anyone would, as indeed it would be confusing for the reasons you mentioned. And restrings are now not that easy as before.

Also, for changing clasps - for me thats slowest part of changing sets, as doing "rem all, put all robe, get robe robe, get all robe, put 2.robe robe, wear all " in itself is pretty fast and simple. But many clasps are used in all sets and i have to add command for each one to detach, attach, etc

</div>

<div class="post" data-post-id="36352" data-author="*teker*" data-date="2015-12-22T22:05:10+00:00" data-subject="Re: How do _you_ carry multiple sets of equipment?">

> <strong>Quote:</strong>
> Thats probably a mistype, but we don't swap runes on changing eq sets, right?

I had heard that some equipment (maybe the 3x40 gear?) allowed you to remove runes but since I haven't leveled a mortal to that point I'm not sure. At any rate, the code I'm writing will handle this case if the game already allows for it. If it doesn't already allow for it, nothing new will happen.

</div>

<div class="post" data-post-id="36353" data-author="cyprimus" data-date="2015-12-22T22:45:11+00:00" data-subject="Re: How do _you_ carry multiple sets of equipment?">

I do not keep a lot of eq sets, just one or two for each alt.. and yeah, separate contianers with unique names.

Shapeshift also flops inventory..

Would like to be able to create an eq set... and do it like shapeshift to change... ie eqshift healbonus.. where i have assigned what heal bonus i have to slot, and what container it goes in and old goes too. would be hard to code.. but worthwhile imo.

runes can be removed only from drach and 3x40 gear from what i was told... never done it myself.. think any forger mob can unsocket from those items for a fee.

between my 4 highest alts i prolly have 10-12 clasps tops.. i rarely change them.

Thanks! great changes!

</div>

<div class="post" data-post-id="36354" data-author="Yasik" data-date="2015-12-23T04:26:43+00:00" data-subject="Re: How do _you_ carry multiple sets of equipment?">

I carry 4 modes (AC, mana regen, +dam, rent) in one robe, which is AC-\<worn\_about\> at the same time.

I do not switch robes and weapon during eq change, but may start doing so in the future.

Also, may add undead\_control mode, in very distant future, but I doubt it since if I cant solo something - I'll just bring friends instead.

The change is simple:

```
rem all
put all.mr-eq into robe
get all.ac-eq from robe
wear all
```

For 4 modes, only six scripts needed; for 5 modes, it will be ten.

</div>

<div class="post" data-post-id="36355" data-author="Teron" data-date="2015-12-23T09:09:13+00:00" data-subject="Re: How do _you_ carry multiple sets of equipment?">

I use the following containers:

\- one main robe with junk and other containers

\- a container - usually a 500maxweight robe - with a unique keyword for each set, including regen

\- a container in the inv for immediately useful junk, such as potions, and items that are in several sets.

Unfortunately, my regen container is a regen robe, so when I'm in regen, the stuff in my main robe isn't accessible.

However, I use an alias that sets variables for all items in my sets: dam rings, ac rings, ac robe, etc

and another regen alias that:

\- sets variables for current gear: ring, body, belt, etc

\- allows me to wear uc gear in ac and in regen with the same alias

\- allows me to switch between regen/ac with the same alias.

When I change items, I use:

\- rem item1 item2

\- rem item7 item8

get regen container from robe

get all from regen container

put ac items in regen container (I have an alias that takes up to 9 items and puts them in one container)

wear item1 item2 etc

wear item7 item8 etc

Some people use a script with temp containers and put all, which is faster, but requires having a clean inv and a few more commands to get/put temp containers. Alris's one can be a good example.

When I used rem all/wear all, I liked having a prime druid bag of resplendent lillies that you couldn't wear, so your inv container (a golden sack) wouldn't replace your ac held low item on wear all.

I do hope it's something like Cyprimus suggested: we can have several ingame sets of eq that you specify and can wear with one command, like it's done in most MMORPGs. So if it is so, then we can specify a container for each set as well - hopefully the code can detect where in the inv/robes the container is, so it puts the items there anyway.

Thanks.

</div>
