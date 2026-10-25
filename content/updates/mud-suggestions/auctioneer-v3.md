---
title: "Auctioneer v3"
topic_id: 4870
author: "*Breeze*"
date: 2018-08-28T18:23:25+00:00
last_activity: 2018-09-30T13:39:17+00:00
last_author: "*Breeze*"
sticky: false
locked: false
post_count: 8
---

<div class="post" data-post-id="38965" data-author="*Breeze*" data-date="2018-08-28T18:23:25+00:00">

I am currently redoing the auctioneer..

Any feature requests?

Note : I plan on fixing the issue where uncollected stuff stays there forever.. Not sure if I should make him reauction it or ship it for fee, junk it or sell it or what..

Plan on adding lots /batches of same item

Plan on adding the auction fee which is on the help file sign

Plan on a new command called suggest

and a new mode of consigning called

"consign token suggest 237" 

"consign token suggest max" 

"consign token 1234 2345 max"

Suggest will set the prices or show what the suggested prices are. Min will probably be suggested-10%

Suggested is average price item sells /sold for. 

Max is max length of time for auction. 

Not sure if I add search filter again. 

Writing from my mobile so can't make post more coherent atm.

</div>

<div class="post" data-post-id="38966" data-author="Driven" data-date="2018-08-28T20:59:26+00:00">

I love these ideas.  Please add a batch cancel of all items you currently have on auction... this is particularly useful at token auctioneers when a friend want to roll and you want to give him your tokens you have on auction.  

Could we also add prepaid wanted ads to the auctioneer?  As in, I want Aventurines and am willing to pay 20m per gem.  I want 4 Avents and so I put up 4 wanted ads for Aventurines, paying 20m.  So I would actually pay the auction price at the time of putting up the wanted ad.  If I wanted to cancel my ad I can and get my 20m back per ad.  Someone comes along, sees the wanted ad and can sell an Aventurine instantly.  Next time I come along and type "collect" I get the Aventurine.  Thoughts?

</div>

<div class="post" data-post-id="38967" data-author="*Breeze*" data-date="2018-08-29T03:44:03+00:00">

The only problem there is that if there is anything with a similar then it could be abused..

Since all gem are same vnum that's probably doable but for general eq no.. 

But let me think on it...

</div>

<div class="post" data-post-id="38968" data-author="Teron" data-date="2018-08-30T14:43:29+00:00">

These changes have been in the air for ages.

Batch consign/cancel would rock.

Batch cancel also helps for when you return in a week, cancel all your stuff, then relist it.

Wanted ad is a good idea as well: people could post eq they need and people might pop it.

</div>

<div class="post" data-post-id="38969" data-author="Ezekiel" data-date="2018-08-30T20:07:57+00:00">

Agreed with Driven and T. Please enable at least batch cancels for hexes/octs/gems, if not a cancel all function. Wanted ads seem like a great idea. It would then give the auctioneer full functionality to cover what the auction board thread used to actually do.

About eq left sitting accumulating at auctioneer...if you make him reconsign it..you'll have a lot of chars that log in, consign something for the short while they're logged, then don't log on for a month and it'll clog up the list. Just my thought.

I also think it's kind of silly to allow stockpiles of token storage at meditation chambers by keeping them highly bid. The med chambers end up being used as storage rather than sale. Maybe by taking away the auctioneer holding the eq on expiration, it will solve this problem. Kind of like shipping, if you don't 'collect' within a certain amount of time, you start being gradually charged for the auctioneer holding.

People used to actually sell tokens to shop and newbs could get them at an affordable price. Currently people just hoard for their friends or far-away alts because..well, why not, when it's cost free to auction and store.

Thanks for all the hard work!

-Zeke

</div>

<div class="post" data-post-id="38970" data-author="Teron" data-date="2018-09-01T14:17:26+00:00">

One other thing: gem trades.

Same as selling gem or putting out an ad for a gem in exchange for gold, but except the other gems.

Say, I want to trade a Rhodo for a Jet or Malachite.

I consign the rhodo with jet and malachite in the details and no other trade offer returns rhodo to the other person.

Of course, this can get complicated:

- trading a rhodo for 2 gray white diamonds

- trading a rhodo for a White Opal and 10mil gold

- trading a rhodo and a tomb jade for 3 aventurines and 30mil gold.

Still, an automated system for gem trading would ease the process and show the interested parties, what kind of gems are up for trade.

</div>

<div class="post" data-post-id="38978" data-author="*Breeze*" data-date="2018-09-25T18:41:58+00:00">

Not so (QUICK) update

> **Teron wrote:**
> These changes have been in the air for ages.
> 
> Batch consign/cancel would rock.
> 
> Batch cancel also helps for when you return in a week, cancel all your stuff, then relist it.
> 
> 
> 
> Wanted ad is a good idea as well: people could post eq they need and people might pop it.

- batch consign - probably not.. unless you mean batch consign lots .. 5x of same item, etc..

- batch cancel - probably yes. mostly on the yes side.

- wanted - not sure. will think on it.  would be low on priority list though.

> **Teron wrote:**
> One other thing: gem trades.
> 
> 
> 
> Same as selling gem or putting out an ad for a gem in exchange for gold, but except the other gems.
> 
> 
> 
> Say, I want to trade a Rhodo for a Jet or Malachite.
> 
> I consign the rhodo with jet and malachite in the details and no other trade offer returns rhodo to the other person.
> 
> 
> 
> Of course, this can get complicated:
> 
> - trading a rhodo for 2 gray white diamonds
> 
> - trading a rhodo for a White Opal and 10mil gold
> 
> - trading a rhodo and a tomb jade for 3 aventurines and 30mil gold.
> 
> 
> 
> Still, an automated system for gem trading would ease the process and show the interested parties, what kind of gems are up for trade.

trades - too difficult to implement, given that all gem's are the same basic vnum. - will think on alternatives.

> **Ezekiel wrote:**
> Agreed with Driven and T. Please enable at least batch cancels for hexes/octs/gems, if not a cancel all function. Wanted ads seem like a great idea. It would then give the auctioneer full functionality to cover what the auction board thread used to actually do.

see above for answers to those..

> **Ezekiel wrote:**
> About eq left sitting accumulating at auctioneer...if you make him reconsign it..you'll have a lot of chars that log in, consign something for the short while they're logged, then don't log on for a month and it'll clog up the list. Just my thought.
> 
> 
> 
> I also think it's kind of silly to allow stockpiles of token storage at meditation chambers by keeping them highly bid. The med chambers end up being used as storage rather than sale. Maybe by taking away the auctioneer holding the eq on expiration, it will solve this problem. Kind of like shipping, if you don't 'collect' within a certain amount of time, you start being gradually charged for the auctioneer holding.
> 
> 
> 
> People used to actually sell tokens to shop and newbs could get them at an affordable price. Currently people just hoard for their friends or far-away alts because..well, why not, when it's cost free to auction and store.
> 
> 
> 
> Thanks for all the hard work!
> 
> 
> 
> -Zeke

that will be fixed with v3 auctioneer.

the process will be something like this

consign item

win auction or item not sold, it gets assigned to the person to collect (either the buyer or the seller)

if not picked up after X time, it gets automatically re-auctioned @ x% of the price / time, but this time the seller is the auctioneer.  if it doesnt sell or doesnt get picked up.. again, it is moved to a special list of stuffs

that i can just collect from and put in goody bag as prize for quest (ala old style sloth quest prizes)

X and x% are to be determined, but will be reasonable..

...

"suggest" command - not started - may be implemented as "consign suggest"

"status" command - alias for "lots"

"lots" command - the new code changes the "lots" display a bit by combining some stuff and massaging some other stuff.  maybe i make a screenie when i get to work (i am coding it on my work vm)

"cancel" command - not started but its easy enough. will be

cancel lot# or cancel all

wont be supporting cancel 1 2 4 7 9 11 etc..

consign lots is not yet done, but its what i am working on atm.

"consign" command - now has 2 formats..

consign ["lot quantity" | item] min [buyout | -1] time

examples ..

consign 1 hex-token, min 12, buyout 23, 235 hours

"consign hexagonal 12 23 235"

or

consign 97 hex-tokens, 1200 min, 2300 buyout, 235 hours

consign lot 97 hexagonal 1200 2300 235

still considering if i want to implement the auction fee or not that was supposed to go into v1 

but i never got around to finishing.

MSDP ... toying around with making auction info available via MSDP ..

already have a working example..

data (when viewed with the command "lua msdp") looks something like this (rebuilding from memory)

```
AUCTIONS = {
  AUC_1 = {
    REMAIN_TIME_MIN = "1",
    REMAIN_TIME_HOUR = "2",
    REMAIN_TIME_DAY = "3",
    ITEM_VNUM = "709",
    ITEM_DESC = "A Rhodochrosite",
    CURRENT = "1234123",
    SELLER = "ME",
    BIDDER = "YOU"
  },
  AUC_2 = {
    REMAIN_TIME_MIN = "1",
    REMAIN_TIME_HOUR = "2",
    REMAIN_TIME_DAY = "3",
    ITEM_VNUM = "709",
    ITEM_DESC = "A Rhodochrosite",
    CURRENT = "1234123",
    SELLER = "YOU",
    BIDDER = "ME"
  }
}
```

 separating if you are the buyer or seller is left as an exercise for the user 

(i already did it in my test mudlet script)

</div>

<div class="post" data-post-id="38986" data-author="*Breeze*" data-date="2018-09-30T13:39:17+00:00">

because, who doesnt like screenies ?

new output of "lots" and "status" command.

(image: /[http://www.slothmud.org/images/v3auc.PNG](http://www.slothmud.org/images/v3auc.PNG))

full image at [http://www.slothmud.org/images/v3auc.PNG](http://www.slothmud.org/images/v3auc.PNG)

sample of what i did with the MSDP data (not sure if i leave in or not.....)

(image: /[http://www.slothmud.org/images/v3auc_msdp.PNG](http://www.slothmud.org/images/v3auc_msdp.PNG))

full image at [http://www.slothmud.org/images/v3auc_msdp.PNG](http://www.slothmud.org/images/v3auc_msdp.PNG)

</div>
