---
title: "Corpus Severance"
topic_id: 3511
author: "Thraxas"
date: 2010-09-07T10:10:05+00:00
last_activity: 2010-09-14T15:39:31+00:00
last_author: "Thraxas"
sticky: false
locked: false
post_count: 5
---

<div class="post" data-post-id="31731" data-author="Thraxas" data-date="2010-09-07T10:10:05+00:00" data-subject="Corpus Severance">

Corpus Severance is a fantastic spell:

Cost: 30ma

Level: Ne13 Cl32

Effect: You have %chance to have any character death reported to you with %chance of detail about the death.

Something like:

Death intones 'Thraxas has been killed by a snow bird in Aisholm Town'

The who by what and where have a % chance to be shown if the death is reported so you can also get:

Death intones 'Thraxas has been killed by someone in Aisholm Town'

or even

Death intones 'Someone has been killed by someone somewhere'

This is a spell that gives no benefit to the person casting it but potentially benefits all other players. I keep it up at all times and trigger gossip of anything reported as follows:

zmud Trigger to gossip the report:

^(%w) ({intones}) '(*)'$

gossip Corpus Severance : %3

zmud trigger to show corpus severance is up

^You hear the tolling of a slow bell.$

zmud trigger to show corpus severance has dropped and recast

^You are less in touch with death.$

cast 'corpus severance'

</div>

<div class="post" data-post-id="31735" data-author="Stab" data-date="2010-09-08T00:06:35+00:00" data-subject="Re: Corpus Severance">

Thanks for posting the benefits of keeping corpus up thraxas. My understanding ,gleaned some time ago, is that I get the 'who' part consistantly by name for anyone added to my friends list, a 'someone' for peeps not added. The 'where' part may be a masterful??  use  friends, friends add etc. help friends. Good spell.

Stab

</div>

<div class="post" data-post-id="31750" data-author="Dragoth" data-date="2010-09-13T06:50:37+00:00" data-subject="Re: Corpus Severance">

I would say that its an average spell at best, it only takes 1 person to have a death trigger on channel leave to top this spell, which unlike this so called "good" spell works 100% of the time. 

My problem with this whole concept of death is even if somebody knows you are dead, you then have to actually have someone to be able to rescue you and for the best part of my playtime there is like 10 people online of whom 7 are afk and the other 3 are on valk.

</div>

<div class="post" data-post-id="31755" data-author="Vixn" data-date="2010-09-14T15:10:32+00:00" data-subject="Re: Corpus Severance">

Thraxas had to learn that snow bird is nasty mob. Stop dying in Aisholm Town!

</div>

<div class="post" data-post-id="31756" data-author="Thraxas" data-date="2010-09-14T15:39:31+00:00" data-subject="Re: Corpus Severance">

> **Vixn wrote:**
> Thraxas had to learn that snow bird is nasty mob. Stop dying in Aisholm Town!

Chuckle yeah those snow birds are deadly.

</div>
