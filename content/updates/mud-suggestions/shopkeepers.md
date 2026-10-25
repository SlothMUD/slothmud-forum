---
title: "Shopkeepers"
topic_id: 631
author: "12345"
date: 2004-11-24T20:40:30+00:00
last_activity: 2004-12-01T09:37:10+00:00
last_author: "Zeizel"
sticky: false
locked: false
post_count: 17
---

<div class="post" data-post-id="3041" data-author="12345" data-date="2004-11-24T20:40:30+00:00">

Idea for reboots.  Reboots are necessary for clearing mob hated lists, cleaning junk off the ground, restocking shopkeeper cash supplies, ect.

The main thing I don't like about reboots is that it clears shopkeeper inventories.  Most folks that have a few characters don't care, but being able to buy equipment from the various shops is a huge bonus to a newbie type who could really use those spiked boots, pearl of the rising tide or mithril axe.

Shopkeepers have a max number of each item they're willing to carry, and we wouldn't want to impede player's abilities to sell things to the shops.  However, it would seem useful if 1 or 2 copies of a few items in each shopkeeper's inventory carried over from crashes/reboots.  Would provide a little variation to shopkeeper's inventories and and shops like the auction house wouldn't load completely empty.  And it might help out a newbie or two.

</div>

<div class="post" data-post-id="3045" data-author="Zeizel" data-date="2004-11-24T21:42:35+00:00">

Even if there's a specific reason for loading shops empty, I think saving the inventory in the auction house would be a great idea.  It's always disappointing to log on and check the shops, only to find out the MUD crashed earlier that day.  Especially with the auction house.

Items for Sale:

------------------

There is nothing for sale

This just doesn't look like something a real shopkeeper would do :-P  If nothing else, stock the auction house with lowbie gear that can /typically/ be found there after people stock it themselves.

</div>

<div class="post" data-post-id="3048" data-author="madmax" data-date="2004-11-25T00:44:53+00:00">

Maybe a compromise might be if that on a crash (not scheduled reboot) that the eq remains in the shops.  

On reboots (scheduled) the shops totally are cleared.  This would still give some control to get rid of all the extra unwanted stuff.

Just a thought.

Madmax

</div>

<div class="post" data-post-id="3049" data-author="Weasel" data-date="2004-11-25T01:02:49+00:00">

There of course is the other side of the coin that if you want to sell off some eq you cant because the shopkeepers have bought so much eq already that they have no cash left to buy more..

</div>

<div class="post" data-post-id="3050" data-author="Zeizel" data-date="2004-11-25T01:16:01+00:00">

True.  Perhaps a happy medium could be found?

</div>

<div class="post" data-post-id="3052" data-author="Altair" data-date="2004-11-25T07:44:09+00:00">

Probably coding the mud to keep stuff on scheduled reboots would be easier than coding it for crashes.

Also, is it really necessary to have a [u:yq8jdai4]daily[/u:yq8jdai4] reboot?

And, are we sure it doesn't affect pop rates? I know, I know... in theory, it doesn't, I know, I know... in theory, you have the same pop chance right on reboot as at any other time, I know I know... but there's stuff I've been cycling and I've gotten one out of over 100 cleanups of the mob that pops it (cleanup= every copy of that mob). I doubt that red and blue ring has a 1:100 pop.

In theory, my mother couldn't have children. I have two younger siblings. Excuse me if I don't have faith in theories.

</div>

<div class="post" data-post-id="3061" data-author="12345" data-date="2004-11-27T02:07:08+00:00">

There of course is the other side of the coin that if you want to sell off some eq you cant because the shopkeepers have bought so much eq already that they have no cash left to buy more..[/quote:319ltguc]

In honesty, I wasn't suggesting that the shopkeeper's cash amount be saved, only some random items from his inventory.  Considering that our creative imms have figured out how to make corpses persistant across crashes and reboots, I don't see this as being too much more difficult.

</div>

<div class="post" data-post-id="3062" data-author="Weasel" data-date="2004-11-27T14:07:59+00:00">

true that.

</div>

<div class="post" data-post-id="3072" data-author="Zeizel" data-date="2004-11-29T17:07:13+00:00">

Also, is it really necessary to have a [u:nh5odu3a]daily[/u:nh5odu3a] reboot?

[/quote:nh5odu3a]

From what I have noticed, there are certain items (in particular the Legendary Golden Trefoil Leaf needed to learn Rapidshift) that only pop n times per reboot.  This is an item that is only available in T&D, and the other day I went to purchase it, but it wasn't there.  If we got rid of the daily reboots, we'd be shooting ourselves in the foot as far as these types of items go.

Of course, this is all based on what I observed during one day.  Maybe I'm flat out wrong?  If so, I'd appreciate suggestions on how to pop the inventory of T&D :-P

</div>

<div class="post" data-post-id="3073" data-author="12345" data-date="2004-11-29T19:32:56+00:00">

Shopkeeper wouldn't be saved like a player would.  Normal inventory would always be loaded, but this would allow additional inventory to persist across crashes and reboots.

This is not intended to reduce the frequencies of crashes or reboots.  Crashes aren't intentional, and therefore mostly unavoidable.  Reboots occur for any number of reasons, most of which only the gods are familiar with.  So items such as the leaf would still be restocked just as often as it normally would.

This is intended only to make our existing reboots/resets less painful.  On another note though, a major feature of this involves identifying objects which are not part of a mob's normal reset list.  Other examples of this would include looted equipment.  This would make it possible for a mob that loots equipment out of a corpse to save the equipment from the corpse (or equipment it stole from a player) to a file and then reload it on reboot. After all, if it works for shopkeepers, why not regular mobs?

Then if you die and a mob loots your cinq and the game crashes, you can still go back and beat the tar out of the mob and get it back, instead of listening to the long list of reasons why it's gone forever and you'll need to go forge another one.

It's not a perfect idea... but it's a start.

</div>

<div class="post" data-post-id="3076" data-author="Altair" data-date="2004-11-30T07:56:16+00:00">

[quote:kwyweyzt]From what I have noticed, there are certain items (in particular the Legendary Golden Trefoil Leaf needed to learn Rapidshift) that only pop n times per reboot. [/quote:kwyweyzt]

Zeizel, that could simply mean "n times per 24 hours of killing the mob" - so "n times out of z times the mob has been killed", so (n/z)*100 % probability of popping. How can you be sure that if we stayed up for 3 days, the item wouldn't pop 3 times as much?

I have got two red and blue rings from the circus after a month of cycling, but that doesn't mean they're set to pop once every two weeks, or once every fifteen reboots.

</div>

<div class="post" data-post-id="3077" data-author="Hotara" data-date="2004-11-30T08:06:50+00:00">

You're assuming that mobs in treasures and dreams are cycleable...

These mobs are not cycleable and therefore item can only be purchased on reboots.

[quote:1g9xshk1]From what I have noticed, there are certain items (in particular the Legendary Golden Trefoil Leaf needed to learn Rapidshift) that only pop n times per reboot. [/quote:1g9xshk1]

Zeizel, that could simply mean "n times per 24 hours of killing the mob" - so "n times out of z times the mob has been killed", so (n/z)*100 % probability of popping. How can you be sure that if we stayed up for 3 days, the item wouldn't pop 3 times as much?

I have got two red and blue rings from the circus after a month of cycling, but that doesn't mean they're set to pop once every two weeks, or once every fifteen reboots.[/quote:1g9xshk1]

</div>

<div class="post" data-post-id="3078" data-author="Altair" data-date="2004-11-30T09:19:34+00:00">

OK, so what's broken is treasures and dreams. But _ONE_ badly designed area is not enough reason to break the rest!

</div>

<div class="post" data-post-id="3081" data-author="12345" data-date="2004-11-30T12:19:40+00:00">

Sounds like the same kind of thing as the Polished Steel Bracelet on Lyme, although I think the bracelet has been fixed to allow you to buy more than one.  The mount dealer on VK can also run out of mounts to sell, but that might be intentional.  Not sure why the leaf would be set to sell out unless it was a bug of some kind.  Then again... who knows.

</div>

<div class="post" data-post-id="3082" data-author="Zeizel" data-date="2004-11-30T13:15:48+00:00">

The leaf is generally very difficult to get.  It costs 50 Drachma, which is quite a bit for a level 25 character (in my opinion, anyway).  It took me roughly 4 days of doing nothing but autoquests to get 40 drachma (I had 10 left over from the Valkyre quests).  It could be that having the leaf only available once per reboot is supposed to be part of the difficulty, although that seems kind of silly...

</div>

<div class="post" data-post-id="3092" data-author="Alana" data-date="2004-12-01T08:44:31+00:00">

If that is supposed to be part of the difficulty, then whomever wants it that way can spank me. Just don't use the wizlists to do it, since my email is ignoring those :)  (leave of absentia, remember)

Golden trefoil can now be bought more than once per reboot.

</div>

<div class="post" data-post-id="3093" data-author="Zeizel" data-date="2004-12-01T09:37:10+00:00">

If that is supposed to be part of the difficulty, then whomever wants it that way can spank me. Just don't use the wizlists to do it, since my email is ignoring those :)  (leave of absentia, remember)

Golden trefoil can now be bought more than once per reboot.[/quote:89rgkchn]

Thank you Alana!

Boy am I glad I hadn't rented the Trefoil yet :-P

</div>
