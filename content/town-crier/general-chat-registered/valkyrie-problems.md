---
title: "valkyrie problems"
topic_id: 2306
author: "brand"
date: 2007-01-21T17:34:31+00:00
last_activity: 2007-01-28T02:04:27+00:00
last_author: "Krok"
sticky: false
locked: false
post_count: 8
---

<div class="post" data-post-id="16429" data-author="brand" data-date="2007-01-21T17:34:31+00:00" data-subject="valkyrie problems">

\<63/835hp318/566ma64/215mv\>

Lie still; you are DEAD!!! <img src="/images/smilies/icon_e_smile.svg" alt=":-)" title=":-)" width="15" height="15" class="smiley nozoom">

but i'm not dead yet!

valkyrie heals do not seem to work correctly yet...

</div>

<div class="post" data-post-id="16461" data-author="brand" data-date="2007-01-22T15:05:31+00:00" data-subject="die with hp!">

so i guess the bug is i die with hp when i use the valkyrie as healo.

with about 160hp left is highest for me to die at.

happen to any other clerics?

brand

</div>

<div class="post" data-post-id="16470" data-author="kjartan" data-date="2007-01-22T16:36:00+00:00" data-subject="">

I will look into it; I may have botched the valkyrie's healing so that it still heals you when you are dead, but being healed back up to positive hp doesn't render you non-dead.

</div>

<div class="post" data-post-id="16525" data-author="Mace" data-date="2007-01-25T10:20:24+00:00" data-subject="">

As long as the Valkyrie is being looked at, it also does (last I used it..) two other things:

\- It tries to heal based on its master's group whether they're in the same room or not (one absent group member with low hp causes the valkyrie to blow all its mana)

\- The automatic standing up feature is.. poor. You can't stop the valkyrie from charging in and getting itself killed when you might want to leave it behind for a fight.

</div>

<div class="post" data-post-id="16529" data-author="Avatar" data-date="2007-01-25T13:41:31+00:00" data-subject="Valkryie">

Instead of rest, you could order the Valkyrie to sleep. It should remain asleep until you "wake" it up.

</div>

<div class="post" data-post-id="16530" data-author="Krok" data-date="2007-01-25T14:33:48+00:00" data-subject="">

But it doesn't.

</div>

<div class="post" data-post-id="16555" data-author="kjartan" data-date="2007-01-27T16:43:01+00:00" data-subject="">

I made the Valkyrie not heal people who aren't in-room or are dead. I also made her not auto-wake if asleep.

</div>

<div class="post" data-post-id="16559" data-author="Krok" data-date="2007-01-28T02:04:27+00:00" data-subject="">

Thanks, Kj!

</div>
