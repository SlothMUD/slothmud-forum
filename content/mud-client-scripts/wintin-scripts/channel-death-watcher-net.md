---
title: "Channel Death Watcher .NET"
topic_id: 1595
author: "jezer"
date: 2005-12-12T02:57:07+00:00
last_activity: 2005-12-12T02:57:07+00:00
last_author: "jezer"
sticky: false
locked: false
post_count: 1
---

<div class="post" data-post-id="9763" data-author="jezer" data-date="2005-12-12T02:57:07+00:00" data-subject="Channel Death Watcher .NET">

Heaps simple death checker script for channel droppers.

\#defgroup {Deathcheck}

\#action {%1 has left this channel} {tell $1 Just checking to see if ur ok <img src="/images/smilies/icon_e_smile.svg" alt=":)" title=":)" width="15" height="15" class="smiley nozoom">} {G\|Deathcheck}

\#action {%1 is unable to respond right now.} {ct $1 IS DOWN!!!} {G\|Deathcheck}

\#defgroup {}

Assumes ct is alias for channeltalk.

</div>
