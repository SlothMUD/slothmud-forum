---
title: "Changelog 2017-11-07: Clan changes"
topic_id: 4798
author: "*teker*"
date: 2017-11-06T15:13:43+00:00
last_activity: 2017-11-19T03:39:03+00:00
last_author: "*teker*"
sticky: false
locked: false
post_count: 13
---

<div class="post" data-post-id="38463" data-author="*teker*" data-date="2017-11-06T15:13:43+00:00" data-subject="Changelog 2017-11-07: Clan changes">

Reboot coming tomorrow morning. The main change is that I'm moving the clan data from files to database. That means I'll be performing an import shortly before the reboot. I would suggest that you refrain from making changes to your clan (adding/removing members, changing recall spots, etc) in the last few hours before that reboot.

The clan command syntax will be changing slightly and I'll try to get the help file updated either today or shortly after the reboot.

</div>

<div class="post" data-post-id="38464" data-author="*teker*" data-date="2017-11-07T16:17:19+00:00" data-subject="Re: Changelog 2017-11-07: Clan changes">

These changes are now live. Please let me know if there are any issues.

Now that the data is in a more manageable form, what types of things are missing from clans? One of my goals is to complete clan vaults so that they have a key that can only be used by current clan members. What else?

</div>

<div class="post" data-post-id="38465" data-author="Gorka" data-date="2017-11-07T17:44:27+00:00" data-subject="Re: Changelog 2017-11-07: Clan changes">

Thanks for all the stuff you do to this game Teker. I can't ever recall a coder being so active with improving how the game runs in the structural way you deal with things.

I tried to think of improvements to the clan system, but nothing really sprang to mind. I did wonder why vault inn keepers/banks/fountains and food shops were removed though?

</div>

<div class="post" data-post-id="38473" data-author="*teker*" data-date="2017-11-10T15:40:24+00:00" data-subject="Re: Changelog 2017-11-07: Clan changes">

Thanks for the compliment.

I'm not sure when the things you mention were removed - there are currently unused variables for a clan motto, description, board, innkeeper, and shopkeeper.

The motto/description would be fairly easy edits but I'm not sure where you would see them in the game.

I may have removed boards when I rewrote the vault code. I see boards in some of the immortal rooms used as to-do lists but the general feeling I get is that people use off-mud ways of communication rather than using boards.

I'm not sure what purpose the innkeeper and shopkeeper would provide.

There are also clasps for some of the clans but I don't think I've ever noticed one in game. They appear to be custom items without any bonuses. I don't think there's a method for mortal players to edit items like these so it would either require immortal interaction or some new framework that allows players to restring items.

</div>

<div class="post" data-post-id="38474" data-author="Gorka" data-date="2017-11-10T16:15:17+00:00" data-subject="Re: Changelog 2017-11-07: Clan changes">

1\) Boards were hardly used in the end of s3, I think they are a waste of time.

2\) It can be useful to buy food in your vault sometimes, as well as bank your coins.

3\) Clan clasps cost money and had no effect, I've never seen anyone with one either.

Maybe clan clasps could give an Aura, or something colorful to add to the player aesthetics or description. Of course it would be nice if clan clasp did offer some improvement, but I'm too scared to go there lest we start the "my clan is better than your clan" crap among players. 

I'm really keen to see more vault improvements, maybe runes that unlock something in your vault, or improvements purchased with xp/drachma or experience. Could vaults increase size to 175? This way I could dump my entire robe in a locker, log in another char and pickup my robe. I talked to Breeze about enabling more ma regen in the vaults, I thought a price between 20-50m per point was fair, but 300m was a bit out of the question. The end of the game is near for me, I doubt I will continue to play without ways to improve.

</div>

<div class="post" data-post-id="38476" data-author="*Breeze*" data-date="2017-11-10T21:24:41+00:00" data-subject="Re: Changelog 2017-11-07: Clan changes">

boards -- require reboot unless pre-configured before purchase by an immortal.

innkeepers -- adding a new innkeeper requires a mud reboot.

bank -- pretty sure requires reboot also. not 100% sure though

ma regen -- so i override splorks wishes.. which i verrrry rarely do..

 (we talked about maxes years ago and agreed to leave as is)... 

feel free to email splork and ask for a new price.

clan clasps -- were never meant to have stats. 

we are talking (internally) about ways to continue past avatar 9.40

but these things are things that take time/research to make sure nothing breaks.

</div>

<div class="post" data-post-id="38477" data-author="Teron" data-date="2017-11-12T00:45:51+00:00" data-subject="Re: Changelog 2017-11-07: Clan changes">

Teker, I see the following use for innkeeper/shopkeepers:

You finish run.

Go regen in your vault with maxed regen or deposit popped eq in your vault.

Sell junk to shopkeeper in vault.

Decide to rent.

Log in and appear in your vault.

Buy food/recalls from shopkeeper.

</div>

<div class="post" data-post-id="38480" data-author="*Idjit*" data-date="2017-11-16T22:23:35+00:00" data-subject="Re: Changelog 2017-11-07: Clan changes">

The question with shopkeepers is, if we allow shopkeepers in vaults, will we be even more fragmented into keeping things just in clan vaults, like chop weapons already are (I wasn't going to discuss that, but this thread forced my hand). If you sell garbage just to your clan vault, how does it then trickle out to the regular shops if at all, so that a newbie can purchase it? How does this promote interaction?

This brings up a few ideas anyway about whether we should actually have a bunch of items that -only- load in the shop and -only- on reboot, that are fairly low level (the only thing currently like this that springs to mind is the Plumwood Recorder in the music shop on SS, which is there on occasion but nowhere near all the time). So that people coming into the game as level 1's shortly after reboot don't see default leather gear in there all by itself and assume that we don't spend much effort on our equipment, if the only things in there are utterly boring default gear. When in fact we have an extremely robust selection of equipment.

Perhaps we could enlist the treasure types in a new way for this, as far as shops selecting a small amount of random variation on reboot from the type lists. Either existing categories or reserved 'shop-categories' with some sort of keyword like....shop, in them.

</div>

<div class="post" data-post-id="38481" data-author="*Idjit*" data-date="2017-11-16T22:26:22+00:00" data-subject="Re: Changelog 2017-11-07: Clan changes">

What I proposed originally with food shops in clan, or even personal vaults, was merely to be able to buy-from them, customized food items that the clan members come up with like fried or hardboiled eggs, or anything else that seems off the wall. Not as an outlet to wall off the 'sell' function away from the general use continents where other people outside clans could buy things. Unless, as I referenced before, Teker creates a 'pipeline' where a bunch of this stuff "makes its way" to the shops in the towns. With a certain acceptable loss rate so that it's not 1:1 and we don't overload our system memory etc.

</div>

<div class="post" data-post-id="38482" data-author="*teker*" data-date="2017-11-16T23:37:56+00:00" data-subject="Re: Changelog 2017-11-07: Clan changes">

I'm fairly hesitant to create custom mobiles or items for clans because there's no security model in the game to allow mortals to modify mobiles and/or items. All the editing commands are immortal only and these would have to be changed along with some sort of security model to allow players to edit things in their vaults and clan officers to modify things in the clan vaults (which technically don't exist yet). I haven't even looked at what it takes to build a shop - 20 years ago shops were stored in text files and required a reboot to set up a new shop but I have no idea if Sloth has improved upon that.

Bottom line is that it currently would involve a builder to customize these things so you could certainly pester one to see if they want to set this stuff up for your clan. Otherwise it's going to be a pretty decent chunk of work to code.

</div>

<div class="post" data-post-id="38483" data-author="*Idjit*" data-date="2017-11-17T00:03:35+00:00" data-subject="Re: Changelog 2017-11-07: Clan changes">

Oh I would think an immort would still be involved in building the clan sammich or hamburger or whatever. I wasn't exactly envisaging new Template objects. There would be some sort of nominal fee for setting up one new food item, and then an immort would add it.

Shops are easily enough created with the variation of the forge mob kvp proc (see immh forge).

As to fountains, I submitted an "help room fountain" help file complete with a pricing structure for the different liquid types but it promptly disappeared after being proposed.

Before people get too excited the fanciest liquid on the help file was probably Milk and Root Beer, the things which are available in limited supply in bottles at SS and BH Bars/Taverns.

We'd likely never establish a clan fountain that filled, say, miruvor or ent draught. Sorry!

</div>

<div class="post" data-post-id="38485" data-author="Gorka" data-date="2017-11-17T08:19:05+00:00" data-subject="Re: Changelog 2017-11-07: Clan changes">

When I made the off the cuff remark about food and water in vaults, I was referring to Iron rations and a fountain. Maybe recalls as well. I wasn't talking about the customization of food templates. Selling items in clan vaults was not my suggestion either... I think they should be sold publicly.

I would much prefer teker spent time stopping broadside from dumping me on my ass, than being able to buy Zuzu's favourite recipe of cheese and potato bake in his monkey vault... <img src="/images/smilies/icon_twisted.svg" alt=":twisted:" title=":twisted:" width="15" height="15" class="smiley nozoom">

Might I add I already have enough issues selling my junk items publicly let alone privately, due to shop keepers running out of coins. It's still an issue.

One other thing though, if Teker is reading this... how do I clan add my alts without multi playing?

</div>

<div class="post" data-post-id="38490" data-author="*teker*" data-date="2017-11-19T03:39:03+00:00" data-subject="Re: Changelog 2017-11-07: Clan changes">

> <strong>Gorka wrote:</strong>
> how do I clan add my alts without multi playing?

I don't think you can. There's another issue regarding clan membership - the player can get added to a clan without wanting to. Maybe a better way would be to "clan invite" someone and to require them to "clan accept" or "clan decline" the invitation when logged in.

</div>
