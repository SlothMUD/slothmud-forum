---
title: "Changelog 2020-02-18"
topic_id: 4952
author: "*teker*"
date: 2020-02-18T18:21:26+00:00
last_activity: 2020-02-18T18:21:26+00:00
last_author: "*teker*"
sticky: false
locked: false
post_count: 1
---

<div class="post" data-post-id="39374" data-author="*teker*" data-date="2020-02-18T18:21:26+00:00" data-subject="Changelog 2020-02-18">

I've retooled the timing for zone resets to try to reduce the lag time we were seeing. Previously the game would queue up the zones and reset one zone every 6 seconds. With the number of zones we have, this was backing up quite a bit so I've changed it to reset one zone every 0.25 seconds. This means that the time between spirit watcher warnings and the actual reset could be a lot quicker than before.

</div>
