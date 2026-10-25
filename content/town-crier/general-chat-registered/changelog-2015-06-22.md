---
title: "Changelog 2015-06-22"
topic_id: 4493
author: "*teker*"
date: 2015-06-22T14:37:53+00:00
last_activity: 2015-06-24T12:35:07+00:00
last_author: "Ker"
sticky: false
locked: false
post_count: 7
---

<div class="post" data-post-id="35956" data-author="*teker*" data-date="2015-06-22T14:37:53+00:00">

Drop all.keyword works now

Remove all.keyword works now

Remove #.keyword works now

To remove ambiguity between players and mobiles, using 0.keyword should always look for/find the player.  This should keep players from sanc'ing/healing mobs when they don't mean to.

I've also done some performance tuning with a particularly active part of the code.  It should help _if_ the recent lag issues have been CPU related.  More tweaks to come once I am able to analyze the counters from the current boot cycle.

</div>

<div class="post" data-post-id="35957" data-author="*teker*" data-date="2015-06-23T02:15:09+00:00">

Forgot to mention that I updated greater refresh - it should default to self if no target is specified.

I'm also working on memorize and ioun stones.  Would be curious to know what spells people typically memorize other than damage spells and gate.  That way I can test the new code before the rest of you do.

</div>

<div class="post" data-post-id="35958" data-author="Marvel" data-date="2015-06-23T13:45:04+00:00">

I used to memorize mirror image, haste, and reflection as well.

</div>

<div class="post" data-post-id="35959" data-author="Ker" data-date="2015-06-23T14:41:59+00:00">

Would be great if we could check spells memorized asleep. This has been on debate for eons.

There are also skills/spells in the shapeshifted forms that could use this change, in regards to default cast without syntax.

Thanks.

Dr

</div>

<div class="post" data-post-id="35961" data-author="*Breeze*" data-date="2015-06-23T20:03:05+00:00">

> **Ker wrote:**
> Would be great if we could check spells memorized asleep. 
> 
> 
> 
> -snip-
> 
> 
> 
> Dr

Teker already added that. Should be live

</div>

<div class="post" data-post-id="35962" data-author="*teker*" data-date="2015-06-23T20:18:52+00:00">

> ***Breeze* wrote:**
> Teker already added that. Should be live

Ooops, it is live accidentally.  "mem" and "mem clear" will both work while sleeping.

</div>

<div class="post" data-post-id="35963" data-author="Ker" data-date="2015-06-24T12:35:07+00:00">

Awesomeeeeeeeee <3

Dr

</div>
