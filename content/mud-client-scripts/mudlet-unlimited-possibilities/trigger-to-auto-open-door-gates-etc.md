---
title: "Trigger to auto open (door, gates, etc)"
topic_id: 4003
author: "Constin"
date: 2013-01-11T18:39:24+00:00
last_activity: 2013-01-11T18:39:24+00:00
last_author: "Constin"
sticky: false
locked: false
post_count: 1
---

<div class="post" data-post-id="33913" data-author="Constin" data-date="2013-01-11T18:39:24+00:00" data-subject="Trigger to auto open (door, gates, etc)">

pattern: ^The (.\*) to the (.\*) seems to be closed.$

command: send("open "..matches[2].." "..matches[3].."\\n")

\*choose perl regex for pattern!

</div>
