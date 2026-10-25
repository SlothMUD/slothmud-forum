---
title: "Two vault features discovered recently"
topic_id: 3959
author: "Yasik"
date: 2012-11-13T11:17:27+00:00
last_activity: 2012-11-16T17:07:03+00:00
last_author: "*Breeze*"
sticky: false
locked: false
post_count: 4
---

<div class="post" data-post-id="33725" data-author="Yasik" data-date="2012-11-13T11:17:27+00:00" data-subject="Two vault features discovered recently">

Hello!

I would like to report two unusual features I believe is not working as it should be. If it's been reported already and you're aware of it, then count this message as friendly reminder.

At first, vault room_name and room_desc still resets itself to original after reboot/crash, and by original I mean room_name given very first time right after pirchasing a hovel. Doestn't matter if changes made by owner or alternate chatacters, it still resets.

At second, while in the vault, can't cast Freshwater spell (outside only), but in the prompt it still says it's 'outside':

![](http://dl.dropbox.com/u/72105811/Pics/Vault_indoors_outside.png)

Not sure what fix is the proper fix, though.

</div>

<div class="post" data-post-id="33726" data-author="*juggleblood*" data-date="2012-11-13T12:20:23+00:00" data-subject="Re: Two vault features discovered recently">

I can tell you that Freshwater checks both for an indoors flag and sector type. Your vault room tells me it's not flagged indoors, thus the weather, but the sector type is invalid for the spell.

The house buying / modification requires a coder to look at (not me), but if you email me any modifications you would like, I can implement them and save.

</div>

<div class="post" data-post-id="33767" data-author="Yasik" data-date="2012-11-16T16:31:24+00:00" data-subject="Re: Two vault features discovered recently">

Thanks, but my vaults no longer need admin intervention.

What I'm sayin' is if you give us the freedom to customize our ingame property, then why it lasts during only 1 uptime? Makes no sense if we must re-enter descs every time mud crashes/reboots.

</div>

<div class="post" data-post-id="33768" data-author="*Breeze*" data-date="2012-11-16T17:07:03+00:00" data-subject="Re: Two vault features discovered recently">

its a freakin bug. it happens. quit nagging.

</div>
