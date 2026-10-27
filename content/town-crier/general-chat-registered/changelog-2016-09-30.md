---
title: "Changelog 2016-09-30"
topic_id: 4675
author: "*teker*"
date: 2016-09-30T14:48:56+00:00
last_activity: 2016-10-01T04:08:18+00:00
last_author: "*Idjit*"
sticky: false
locked: false
post_count: 5
---

<div class="post" data-post-id="37370" data-author="*teker*" data-date="2016-09-30T14:48:56+00:00" data-subject="Changelog 2016-09-30">

I believe I found the bug in the group targeting code so I have re-enabled it. I received some complaints about conflicts with the keyword "leader" and the number of mobs that also have that keyword so I have changed the new group keywords to "groupleader" and "grouppoint".

The rank command now shows more information.

Recite no longer stops singing when the scroll is missing from inventory.

I rewrote the spy command while trying to track down a reported bug. I never got the bug to repro but if you see problems with spy, let me know.

I also rewrote the order command for the same reason. Let me know if you see any issues there.

Previously you would continue reading, studying, etc when attacked by a mobile - now you'll stop when attacked.

Autoloot no longer fires when paralyzed.

Clan recalls now cost mana if attempted while demon bound. I rewrote quite a bit of this code also so let me know if you find issues.

I wrote helper functions for destroying shards when casting spells that use them. The spells no longer destroy all shards in inventory - they stop at the required amount.

Fixed the message when attempting to strike while unlearned.

Restiveness should default to self if no argument provided.

The "tiny potion" was causing problems with quaffing other potions in inventory. This has been fixed. A similar fix was made to the dice bag.

Some other small text message changes. Bard songs now say "Your song" when viewed by the bard. I just realized "god's" has a typo there which I'll get fixed for next time.

</div>

<div class="post" data-post-id="37373" data-author="Gorka" data-date="2016-09-30T17:09:03+00:00" data-subject="Re: Changelog 2016-09-30">

![](http://www.imagefully.com/wp-content/uploads/2015/06/Dog-Say-Hello-Whos-Awesome-Youre-Awesome.jpg)

</div>

<div class="post" data-post-id="37375" data-author="*teker*" data-date="2016-09-30T19:26:12+00:00" data-subject="Re: Changelog 2016-09-30">

Thanks.

Apparently the in-code table for rank is different than what's being used in-game so the rank output isn't accurate at all. I'll try to figure out how to make them match correctly.

</div>

<div class="post" data-post-id="37378" data-author="Teron" data-date="2016-10-01T03:13:37+00:00" data-subject="Re: Changelog 2016-09-30">

thanks for the update, good to see some of my minor bug reports being acted upon <img src="/images/smilies/icon_e_smile.svg" alt=":)" title=":)" width="15" height="15" class="smiley nozoom">

</div>

<div class="post" data-post-id="37379" data-author="*Idjit*" data-date="2016-10-01T04:08:18+00:00" data-subject="Re: Changelog 2016-09-30">

Because I hadn't read the crier at all, I looked at the new ranks and said "cool we're doing the rank reform now".

Too bad <img src="/images/smilies/icon_e_smile.svg" alt=":)" title=":)" width="15" height="15" class="smiley nozoom">

Otherwise, good show Teker.

</div>
