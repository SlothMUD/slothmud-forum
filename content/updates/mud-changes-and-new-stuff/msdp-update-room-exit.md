---
title: "MSDP Update (room_exit)"
topic_id: 4398
author: "*Splork*"
date: 2014-10-17T18:11:41+00:00
last_activity: 2014-10-17T18:11:41+00:00
last_author: "*Splork*"
sticky: false
locked: false
post_count: 1
---

<div class="post" data-post-id="35455" data-author="*Splork*" data-date="2014-10-17T18:11:41+00:00" data-subject="MSDP Update (room_exit)">

Made a couple of changes this past reboot regarding MSDP. The new room_exit variable looks like the following:

```
ROOM_EXITS = {
    East = {
      STATUS = "C",
      RNUM = "1025"
    },
    West = {
      STATUS = "C",
      RNUM = "1013"
    }
  }
```

It now includes the room numbers of the exits. This should help those OOB automatic mappers such as the one for tintin at http://tintin.sourceforge.net/scripts/msdp_mapper.php

I will announce the other changes soon,

Splork

</div>
