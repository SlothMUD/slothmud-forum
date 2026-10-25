---
title: "2021.09.18 recent changes"
topic_id: 5034
author: "*teker*"
date: 2021-09-18T20:15:03+00:00
last_activity: 2021-10-09T01:12:12+00:00
last_author: "Insomnia"
sticky: false
locked: false
post_count: 9
---

<div class="post" data-post-id="39822" data-author="*teker*" data-date="2021-09-18T20:15:03+00:00">

Hopefully you're seeing MXP back to where it was previously.

I've made some updates to EQSET to try to get clasps into containers and to handle situations better when a clasp changes position.  Let me know if you're still seeing equipment left in inventory that shouldn't be there.

Some changes were made to EYE OF THE BEHOLDER to prevent shopkeepers and guild masters from being moved around (especially those in safe rooms).  I tried not to nerf legitimate uses.  Let us know if you think you have a legitimate use that doesn't work any more.

</div>

<div class="post" data-post-id="39823" data-author="cnl" data-date="2021-09-19T00:25:04+00:00">

MXP behavior seems to be normal again - people I spoke to report no more weird symbols on login and I don't see mxp tags showing up on channel command. The MXP parser in mudlet is broken though, as detailed in another post, so I personally recommend mudlet players not to use MXP at all. Thanks for getting the fixes for this and vault issue so quickly out there.

The eqset changes will be great. I have gotten used to using eqset stow to fix any stranded items - it works really well at finding these items and stowing them.

Eqset in general is really awesome, it was complete game changer when I learned how to use it.

There is another weirdness on eqset that seems it may be just a display issue I will mention because it may be indicative of some other problem. I went through all my eqsets and set the same container (black and red robes) using eqset setcontainer black-red all - but if I use eqset show it lists half the items as having container as [ Inventory ] now. BUT - it still stows them in the correct container (black and red robes). They only started displaying like this after I had rented and returned at least once, when I first set them I'm pretty sure they all showed the correct container. 

Regarding the eye of the beholder change, I suppose it's an impossible task being an imm but my feedback on this is that I don't see this as a change that should be fixed. Moving guildmasters around isn't a big deal nor is the occasional attempt to snipe a shopkeeper game-breaking in my opinion, unless we're talking about drachma shopkeepers. It'll just be one less interesting thing to do. Maybe there's some kind of rampant abuse I'm not aware of, or perhaps my idea of rampant abuse just differs from yours :)

thanks

</div>

<div class="post" data-post-id="39824" data-author="Ezekiel" data-date="2021-09-19T06:29:44+00:00">

I second that about eye of the beholder. Finding 'features' within the game is part of the fun, especially at end game for characters. You have people botting in groups for 100+B a week and 50M gold, but those at the keyboard that are active are the ones that get features that they've found nerfed? I mean, I understand if someone is abusing it for something game breaking. But if something is discovered that is harmless, what's the difference? Say for instance you were able to eye out Neptune's City of Dis mobs from their safe zones to make the kill/chop go more quickly (these safe zone mobs are intended to be killed). A change to safe zone mobs blanketly because it had happened to be noticed that a safe zone mob was moved, it changes the intent of some mobs that are in safe zones that are meant to be wooed out. i.e. Elzeard. That mob is designed to take some effort to be able to adequately kill, even though in a safe zone. Again, I've no issue with changing game breaking 'features'...but even if someone, say moved a guildmaster and killed it... it would show back up on repop no? That's not really game breaking. If one safe zone mob was being moved and someone was abusing/game-breaking, I'd hope that that singular mob would be changed based on the circumstance. I don't know the whole backstory though, but as someone at that end stage, finding these features within the game are the only new discoveries the veterans have left to give them that sense of 'ah-ha' as a new player on Valk would. To nerf these things on a blanket level based on room type or more than just circumstantially just gives us a feeling of a great part of the game being taken away and demotivates us to find even more features.... at end game more boredom and less things to be interested in.

Just my two cents,

Thanks- Zeke

</div>

<div class="post" data-post-id="39825" data-author="*teker*" data-date="2021-09-19T16:16:49+00:00">

I was more concerned with shopkeepers and guildmasters being moved and not killed.  That will break some shops and make it difficult for new players to figure out where to level.

</div>

<div class="post" data-post-id="39826" data-author="cnl" data-date="2021-09-19T18:00:00+00:00">

Protecting newbies from confusion makes sense as a goal but I don't think that's a thing that's actually happening. I've been playing for a year but I'm not familiar with a single instance of a newbie not being able to find a shopkeeper or guild master because they've been moved about with eye.

Most guild masters and shop keepers already have protections against eye. No-one is singing them out on Valk and most can't even be sung out as I've found trying to hit some Spirit of Conquest targets.

If you do find a mob you can sing out, you're typically moving them a single room, often one that someone has to walk through to get where they normally are. If you don't web them they tend to wander back to their original rooms on their own pretty quickly, and I think once web wears off they do that anyway. At any rate that's what happened with one I sung out and was unable to kill. There's hunt, track and where to help people find them and if nothing else it will lead to some speculative interactions on the social channels and some 9x40s coming to take a look.

I do remember the first shopkeeper I saw killed and it was really exciting to realize hey - you can learn tricks and ways and find mobs and achieve something like this against a mob that seemed unassailable. You can make plans and try different strategies. It's interesting. Ultimately it's more an achievement than a way to get xp or gold since there's more efficient ways to get either or both.

And since most shop keepers / guildmasters don't respond to eye for whatever reason, there are already per room or per mob protections of some kind that can be applied if needed.

</div>

<div class="post" data-post-id="39827" data-author="cnl" data-date="2021-09-20T17:25:17+00:00">

some initial testing post reboot on the assumption the changes went in with the reboot.

I notice that I still end up with eq items in inventory but I will detail

I have 2 eqsets : shock (using burnished shield + prismatic blade), blast (using sphairai)

If I use eqset switch shock, eqset switch blast all is good

If I use eqset wear shock, eqset wear blast I end up with burnished shield in inventory

kind of odd. in the past I've ended up with other clasps in inventory and couldn't duplicate that today but I'm not sure I know the steps to make that happen.

I do use wear extensively to assemble sets out of incomplete parts. Wear is awesome, especially to allow different weapons to be used with the same set of armor.

Personally the way I get around this is when I change eqsets I flag a var eqset_unresolved = true, then as part of same routine as non-combat spell maintenance will do eqset stow until I hit "You're not carrying anything that has a set container." which will flag it as resolved. I override sell/drop with aliases so that i can't sell/drop until eqsets are resolved as well. No accidents so far. :) 

I suppose it's possible the changes aren't deployed as well :)

</div>

<div class="post" data-post-id="39828" data-author="Gorka" data-date="2021-09-22T05:20:34+00:00">

Teker,

Is there a way, or could there be a switch or something, when using "eqset deposit," that it only puts items in the vaults that are not also in other sets? (Especially the clasps)

To me the eqset deposit command isn't useful because it deposits items used in other sets, but it would be great if it could avoid that.

</div>

<div class="post" data-post-id="39829" data-author="cnl" data-date="2021-09-22T16:59:10+00:00">

It's kind of a kludge and would be a maintenance headache, but you could create an eqset that has just the items you want to store sans any clasps etc.

so you have your "extra_saves" set, but also a stripped down "extra_saves_storage" set which only contains items that will be vaulted and has all clasps etc removed from it.

Then you would first eqset switch extra_saves_storage and then deposit it to "clean" the eqset before storage.

I imagine at your level eq sets don't change that often so should be doable if not ideal.

</div>

<div class="post" data-post-id="39836" data-author="Insomnia" data-date="2021-10-09T01:12:12+00:00">

So can we get a different fix for whatever you tried to fix with changing eye of the beholder?

I am working on new game maps, for which I want to collect as much information about mobs as possible, and the changes prevent me from doing it... not that knowing the exp/coins/number of attacks/procs of guildmasters is of any real use, but it's exactly what Ezekiel and Fuligin said – I think that the very idea that someone collected this data will further motivate other players to explore new things, try new strategies, and eventually get more fun from the game.

> **Quote:**
> Ultimately it's more an achievement than a way to get xp or gold since there's more efficient ways to get either or both

Totally agree with this!

> **Quote:**
> even if someone, say moved a guildmaster and killed it... it would show back up on repop no? That's not really game breaking.

Not only this – eye of the beholder is level 33, and cannot be used on Valkyre. So I don't think there is any real problem for newbies...

</div>
