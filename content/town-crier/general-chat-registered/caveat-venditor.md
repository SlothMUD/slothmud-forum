---
title: "Caveat Venditor!"
topic_id: 3377
author: "*Chobbs*"
date: 2010-02-09T18:18:26+00:00
last_activity: 2010-03-16T01:03:07+00:00
last_author: "*Splork*"
sticky: false
locked: false
post_count: 5
---

<div class="post" data-post-id="30874" data-author="*Chobbs*" data-date="2010-02-09T18:18:26+00:00" data-subject="Caveat Venditor!">

Mornin' folks,

So yesterday, someone mentioned that we don't have an automatic auction mechanism.  Okay!

Numerous temporary kobold auctioneers are now wandering about the world.  Use auclist to get a list of commands.

Find them, try them out, send bugs and shoop cookies to chobbs@slothmud.org, or post them here.  

Still testing the system, so things are subject to change.  

- Messages will eventually be turned upon the auction channel, so they use 'say' for now.  

- Durations are shortened to facilitate testing.  Would be open to suggestions on how long auctions should run

- Nothing posted will be reimbursed should the system goes wonky.  

Suggestions are appreciated and will be duly considered.  

Remember, send cookies!

Chobbs!

P.S. Thanks for all the folks who have helped me test this in the last few weeks and those few weeks several months ago, notably Elena, Aslan, Acidicus, Strider, Thraxas, and Testbacon

</div>

<div class="post" data-post-id="30902" data-author="*Chobbs*" data-date="2010-02-18T06:05:24+00:00" data-subject="">

Mornin' folks,

More development on the ingame auction system underway.  After discussing things with a few folks, a few changes have been made.  Everything still subject to change.

v0.5b

- You can now consign items without a buyout price.  You will have to wait the full duration, similar to website chop block.  Items with no buyout price cannot be bought out.  You can still post things with buyout prices, as well as how many days you want the auction to run, from 1-3 days

- You can cancel your auctions at any time now, so long as there are no bids on the auction.  If you cancel after 1 hour though, your bidding fee will not be returned.  This may change again.

- Various minor bug fixes with overbidding

- Changed displayed time to real time.  I guess no one translated the 60 days displayed as mud days.  ...yeah...

- Fixed query to properly display messages with folks under lv20

Changes once I get around to them:

- The kobold auctioneers will eventually be moved onto the already present auctioneers on each continent once more debugging has been completed.

- Will try to add an appraise function that tracks previous auctions of that item and suggests a value based on previously completed auctions 

- Zounds of help files once the system is more developed

- More messages.  Auctioneers will probably spam auction channel, they need to earn that commission fee!  I'm considering making a toggle to see these automatic auction messages or not.  

Further suggestions much appreciated.  Auclist at the kobold auctioneers is largely up to date.

Thanks to those who have given this thing a try and have helped to debug this mess.

Chobbs!

</div>

<div class="post" data-post-id="30915" data-author="*Chobbs*" data-date="2010-02-22T11:33:53+00:00" data-subject="">

Mornin' folks,

More fiddling with the ingame auction thing.  

[quote:2ezm3yjc]v0.5d

- added the Appraise function.  see below for details.  Format is still ugly, the information presented isn't final either.

- consigning fee reworked.  The fee to consign an item is now much lower than before, and is now capped.  Upon a successful sale, a final value fee is applied, also capped.  This is done to discourage frivolous auctions.  Fee values are not final.

[/quote:2ezm3yjc]

It dawned upon me (after two weeks...) that it would be helpful to post the commands and what they do.  So in lieu of ingame help files, I give you this monstrous post.

[quote:2ezm3yjc]CONSIGN 

<itemname> <minbid> <optional time, 1-3 days>

<itemname> <minbid> <buyout> <optional time, 1-3 days>

- consigns an item for auction

- confirmation is necessary, or else the auction will not be posted

- if no buyout argument is present, the auction will run its full time unless canceled

LOTS

[no argument]

<all>

<query>

- used to show current auctions

- if no argument is present or 'all', will show you ALL of the current auctions.  Be forwarned, this list is getting large and ignores the lines setting (can't figure out how to get it to respect this.  not yet anyway)

- you can also use lots to search for item by name, type, worn location, &c.  i.e. 'lots head' will show all items up for auction that can be worn on head.  'lots weapon' will show you all weapons.  

Note: lots searches by an item's keywords, not short description.  i.e. if you're looking for "a pair of leather sleeves", searching for "pair" will yield incorrect results

BID

<itemname> <minbid>

- places a bid on an item.  If there is more than one instance of an item, use the unique id to guarantee accuracy.  "Bid 2.token" and the like does NOT work.

- bids CANNOT be canceled (no plans to change this in the future)

- money is drawn immediately from your bank to cover your bid.  you MUST have sufficient funds, else no bid will be placed, so if you cannot place a bid, go deposit your money

- if you are overbid, go back to the auctioneer and he'll return the bid amount

- confirmation required

BUYOUT

<itemname>

- immediately buys an item at the listed buyout price.  If there is no buyout, you cannot buyout the item.  Again, if multiple items are present, use the unique id, for the same reason.  

- money is drawn from what you have on your persons, NOT from the bank

- confirmation required

BIDLIST

- shows you all of your bids, as well as all your posted auctions.  Will probably improve upon this later

CANCEL

[no argument]

<all>

<item>

- if no argument present or 'all', shows all the auctions you can cancel

- cancels an auction you have consigned and have no bids

- if you have waited over an hour to cancel, your bid fee will NOT be returned.  cancellations within the hour will be returned

- confirmation required

RECLAIM

[no argument]

<all>

<item>

- reclaim is defined as an auction that did not sell or have any bids, and whose timers have expired

- you have 5 days to reclaim your item after the auction expires before the item is moved to a shopkeep somewhere

- if no argument present or 'all', shows all items you can reclaim

COLLECT

[no argument]

<all>

<item>

- collect is defined as collecting a bid that you have won, or an auction that has sold.  

- If you are the bidder, the item will be given to you at this time.  

- If you are the seller, the sell fee will be applied here and you will receive the winning bid amount minus the fee.

- if no argument present or 'all', shows all items that you can collect

APPRAISE

<itemname>

- appraise is defined as learning collected data regarding the item to help people get an idea on an appropriate value

- will show you the raw value of the item; shopkeepers buy and sell the item at a % of this value

- will show you how many times this item has been sold either via buyout or bids

- will NOT show you how many times it has been consigned.  data collected in this manner would largely be useless 

- will show the min/max/avg bids and buyouts for the item

- item must be inventory to appraise

- data at this point is largely incomplete, since the system is still in its infancy and has not collected much data yet

- no fee to appraise, but there will probably be one in the distant future

QUERY

[same as normal query]

- see ingame help query.  fee of 2000 still applies

[/quote:2ezm3yjc]

auclist, not auc list, at the kobolds also shows most commands.  Will write help files soon.

Thanks to those who continue to give suggestions and help me debug this thing.

Chobbs!

</div>

<div class="post" data-post-id="30916" data-author="celerra7" data-date="2010-02-22T16:10:55+00:00" data-subject="">

Really like this new system (have purchased from it).  One suggestion is a default sort by ending date/time, with the item closing soonest at top, and most recently added items at bottom (or in the middle somewhere if they have shorter action durations).  But, in essence, having the list be auto sorted by time ending.  Right now there does not seem to be a recognizable sort order.

Thanks for all the hard work - looks and works well.

</div>

<div class="post" data-post-id="30970" data-author="*Splork*" data-date="2010-03-16T01:03:07+00:00" data-subject="Auction help files ingame!">

You may now find all these helpfiles ingame. Please refer to help auction for a full list of helpfiles.

Enjoy

Splork

</div>
