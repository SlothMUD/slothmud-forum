---
title: "Auctioneer Changes"
topic_id: 4405
author: "*Splork*"
date: 2014-11-03T17:03:18+00:00
last_activity: 2014-11-07T10:49:34+00:00
last_author: "*Breeze*"
sticky: false
locked: false
post_count: 4
---

<div class="post" data-post-id="35487" data-author="*Splork*" data-date="2014-11-03T17:03:18+00:00" data-subject="Auctioneer Changes">

We have made a couple of slight adjustments to the auctioneers:

1\) last hour bids on an item will have the time extended by an hour ( thanks Fluffy )

2\) reroll tokens have their own auction house now, located at the Bal Harbor meditation chambers (this should clear some of the spam created by hundreds of tokens being available)

3\) there is no longer a need to do 'auc lots/auc consign' etc. just 'lots/consign/cancel/etc'

"look sign" in the auction houses to see how to use the auctioneers.

Note: Tokens already consigned at the original auction houses will remain there until sold.

Enjoy,

Splork \& Breeze

</div>

<div class="post" data-post-id="35489" data-author="*Breeze*" data-date="2014-11-04T12:52:01+00:00" data-subject="Re: Auctioneer Changes">

In on reboot::

```
SlothMUD Auctioneer

- New Command:
 "lots searchterm" - to search for a lot by name of seller or by the object description (substring)

- Removed:
 "list" - command (was a clone of lots command)

- Updated:
 "look sign" - for new command "lots searchterm"
 Auctioneer Version String - incremented from 2.3 to 2.4
```

</div>

<div class="post" data-post-id="35491" data-author="*Breeze*" data-date="2014-11-06T14:55:35+00:00" data-subject="Re: Auctioneer Changes">

in now

```
ss/ah/vk/bh reroll chambers are now also token auctioneers!
```

in on reboot:

```
auctioneer version updated to 2.6

auctioneer will notify you if you get outbid on something (assuming you are online)

wider lots/status display for those who have a screen wide enough to see it (and whom have a client that sends the proper NAWS replies)
```

</div>

<div class="post" data-post-id="35493" data-author="*Breeze*" data-date="2014-11-07T10:49:34+00:00" data-subject="Re: Auctioneer Changes">

added:

```
added in an override for wide mode autodetect.

that is, if it is wide and you don't want it wide ever,
or 
if you want it wide but your client doesn't report the right columns for it 
to auto-detect (like straight telnet), we can set a flag on you to 
either enable/disable it permanently.
```

</div>
