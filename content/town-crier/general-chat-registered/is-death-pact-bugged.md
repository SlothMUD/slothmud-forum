---
title: "Is Death Pact bugged?"
topic_id: 2617
author: "alias"
date: 2007-10-14T14:25:52+00:00
last_activity: 2007-10-20T14:09:35+00:00
last_author: "alias"
sticky: false
locked: false
post_count: 4
---

<div class="post" data-post-id="20852" data-author="alias" data-date="2007-10-14T14:25:52+00:00" data-subject="Is Death Pact bugged?">

This normal for anyone else? its happened to me twice already and I'm about to not use the spell anymore.

\<-33Hp 382Ma 142Mv\> 933,446,796 XP 1,309,468 coins +10 align

Your soul merges with your wounded body. You are a whole again.

You feel much, much better!

You stop following Ker.

Bigwig the eudaemon stops following you.

 24374 bytes received in total, compressed to 1644 bytes by MCCP (93 % saving)

it looks as if it kicked in and then I was dead.

thanx,

Pooka

</div>

<div class="post" data-post-id="20858" data-author="Mace" data-date="2007-10-14T21:25:14+00:00" data-subject="">

Yeah, that happens on the last tick of death pact.

For any coder that wants to fix it, point\_update in limits.c.

The GET\_DEATHTICK if/then should be skipped if the player is no longer dead.

</div>

<div class="post" data-post-id="20934" data-author="kjartan" data-date="2007-10-18T23:17:05+00:00" data-subject="">

Fixed, in next crash or reboot.

Thanks, Mace.

</div>

<div class="post" data-post-id="20949" data-author="alias" data-date="2007-10-20T14:09:35+00:00" data-subject="">

Thank you very much, both of you.

Alias

</div>
