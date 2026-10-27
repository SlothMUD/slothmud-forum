---
title: "MSDP"
topic_id: 4746
author: "*teker*"
date: 2017-03-20T14:51:14+00:00
last_activity: 2017-03-24T20:11:17+00:00
last_author: "Tuck"
sticky: false
locked: false
post_count: 6
---

<div class="post" data-post-id="38137" data-author="*teker*" data-date="2017-03-20T14:51:14+00:00" data-subject="MSDP">

Tuk asked me to take a look at MSDP and I'm starting to go through the list of items he sent me. I'm interested to hear any other requests/issues with the MSDP implementation.

LOCATION updates will be fixed in the next reboot but I have changed the name to CHARACTER\_LOCATION in an attempt to standardize future variable names.

The next reboot will also have CHARACTER\_EQUIPMENT which should replace the various WEAR\_XXX variables. It includes the VNUM, SERIAL (unique item id), and SHORT\_DESCRIPTION along with the same information for clasps and runes.

I've updated the help file and have started moving older variables to an obsolete list at the bottom to indicate which ones will be going away.

</div>

<div class="post" data-post-id="38138" data-author="Gorka" data-date="2017-03-20T15:06:23+00:00" data-subject="Re: MSDP">

Thanks Teker, my WEAR\_WIELD is currently set by the mud as the number 30.

I tried to "remove 30" which the mud replies... "You are not using a '30'."

Any chance you could make the wear/wield/remove commands except the SERIAL number? 

The reason for asking is this... say for example I had 4 loops from Iblis, 2 socketted with weapon damage gems and 2 socketted with flail gems... my eqset will need to distinguish the uniqueness when rummaging through my robe amongst the 4 different loops.

Any chance you could add the spell affects of players in the GROUP variable? Would like to detect if players are cursed, webbed, demon bound, deaf etc.

</div>

<div class="post" data-post-id="38140" data-author="*Breeze*" data-date="2017-03-20T15:54:55+00:00" data-subject="Re: MSDP">

> <strong>Gorka wrote:</strong>
> ..snip..
> 
> Any chance you could make the wear/wield/remove commands except the SERIAL number? 
> 
> ..snip..

\* accept

</div>

<div class="post" data-post-id="38141" data-author="*teker*" data-date="2017-03-21T21:35:40+00:00" data-subject="Re: MSDP">

> <strong>Gorka wrote:</strong>
> Any chance you could make the wear/wield/remove commands except the SERIAL number?

If we were going to build a graphical client with a binary protocol, it would be done. It would be nice to have a simple parser and not be checking for names on everything. I'd prefer not to introduce this into the text commands - it just feels like a half-assed solution.

> <strong>Quote:</strong>
> The reason for asking is this... say for example I had 4 loops from Iblis, 2 socketted with weapon damage gems and 2 socketted with flail gems... my eqset will need to distinguish the uniqueness when rummaging through my robe amongst the 4 different loops.

I believe the eqset code handles this.

> <strong>Quote:</strong>
> Any chance you could add the spell affects of players in the GROUP variable? Would like to detect if players are cursed, webbed, demon bound, deaf etc.

I'm not sure what I'm going to do about the GROUP variable. It already has problems with extremely large groups and I don't like the idea of resending the a lot of the same data over and over. I'll have to look at what's in there but it may make sense to split it into 2 parts - one part that only changes with group member changes and another which updates more often.

</div>

<div class="post" data-post-id="38142" data-author="Gorka" data-date="2017-03-21T22:34:59+00:00" data-subject="Re: MSDP">

> <strong>\*teker\* wrote:</strong>
> If we were going to build a graphical client with a binary protocol, it would be done. It would be nice to have a simple parser and not be checking for names on everything. I'd prefer not to introduce this into the text commands - it just feels like a half-assed solution.

Sure, wearing and removing numbers isn't elegant... what about if socketted gems changed the item names they are socketted to... so for example, I could get loop-tomb-jade from my robe... 

Eqset is a solution in most cases, but there are plenty of instances when you just need to get something from your robe, and it's not to wear it. I'm not sure there is a way to distinguish between multiple items of the same type and the socketted gems currently and if there is, I'd like to know.

</div>

<div class="post" data-post-id="38145" data-author="Tuck" data-date="2017-03-24T20:11:17+00:00" data-subject="Re: MSDP">

Aww, thanks Teker.

Can't wait to test all the changes

</div>
