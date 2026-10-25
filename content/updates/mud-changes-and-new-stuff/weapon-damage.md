---
title: "Weapon Damage"
topic_id: 4385
author: "*Splork*"
date: 2014-08-06T22:38:39+00:00
last_activity: 2014-08-06T22:38:39+00:00
last_author: "*Splork*"
sticky: false
locked: false
post_count: 1
---

<div class="post" data-post-id="35411" data-author="*Splork*" data-date="2014-08-06T22:38:39+00:00">

Weapon damage was slightly broken. There was no cap being applied and the MSDP was reading the actual

capped weapon damage value.

Fixes:

* New MSDP variable WEAPON_DAM_CAP added

* Old MSDP variable WEAPON_DAM will now read current weapon damage

* Added new affect APPLY_BONUS_WEAPONDAM in case we decide to add this affect to Equipment

* Cap now applied to weapon damage

Changes are in-game as of this morning's reboot!

Splork

</div>
