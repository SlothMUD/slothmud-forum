---
title: "Mob Follower bug fixes( charms, pets, etc ) and helpfiles"
topic_id: 3844
author: "*Splork*"
date: 2012-01-21T01:56:52+00:00
last_activity: 2012-01-21T01:56:52+00:00
last_author: "*Splork*"
sticky: false
locked: false
post_count: 1
---

<div class="post" data-post-id="33141" data-author="*Splork*" data-date="2012-01-21T01:56:52+00:00" data-subject="Mob Follower bug fixes( charms, pets, etc ) and helpfiles">

Bug Fixes regarding followers

1) Group count was off when a player's followers got the final blow

    * This may affect experience and honor( Was tested and does not

      seem to but... )

2) When a player's follower gets the final blow, that mob will be

   added to their kill history. Since the wipe, this has been bugged

   and followers have not been adding their kills to their master's

   kill history. 

3) There was a bug causing experience issues regarding followers getting 

   the last blow on a creature. When this happened, it appeared to be giving

   less experience than when a PC was getting the final blow. After debugging 

   the issue all day, I came across the fact that the experience was being

   dealt in two entirely different functions when the two instances occurred.

   Inside one of the functions, I had increased 'aged experience" of a mob

   by nearly 40-50%. This was inside the function where the PC was getting the 

   last blow. Inside the other function, "aged experience" was not updated to 

   the new bonus causing the experience to be lower when a follower got the last kill.

   I have updated the code so that both functions are identical in this regard

   and hope this solves the issue mentioned in this thread:

   [http://www.slothmud.org/forum/viewtopic.php?f=28&t=3789](http://www.slothmud.org/forum/viewtopic.php?f=28&t=3789)

Helpfiles added/updated:

1) saves

2) saves_spell

3) extras

4) barehanded accuracy

</div>
