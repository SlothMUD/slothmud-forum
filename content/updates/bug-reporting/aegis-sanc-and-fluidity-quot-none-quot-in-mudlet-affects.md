---
title: "Aegis, Sanc, and Fluidity = &quot;None&quot; in mudlet affects"
topic_id: 4212
author: "DarkArtist"
date: 2014-03-19T15:43:37+00:00
last_activity: 2014-03-27T00:25:23+00:00
last_author: "DarkArtist"
sticky: false
locked: false
post_count: 3
---

<div class="post" data-post-id="34922" data-author="DarkArtist" data-date="2014-03-19T15:43:37+00:00" data-subject="Aegis, Sanc, and Fluidity = &amp;quot;None&amp;quot; in mudlet affects">

The spells Aegis, Sanc, and Fluidity appear as "None" in MSDPSTRING\_AFFECTS for mudlet users, but a TinyFugue user I spoke to does not have this problem.

And since they have the same name, i.e. "None", fluidity gets over-ridden by sanc or aegis.

Thanks for reading.

</div>

<div class="post" data-post-id="34945" data-author="*Splork*" data-date="2014-03-25T13:41:41+00:00" data-subject="Re: Aegis, Sanc, and Fluidity = &amp;quot;None&amp;quot; in mudlet affects">

I have spent quite some time trying to fix this. The only fix I've been able to come up with is basically a hybrid of the string\_perm\_affects and string\_affects, however the name of the spells are working. The affects in all caps are mostly perm, there are exceptions such as spell shield which reads perm but is not. Armor is reading perm on one setting because its the innate bonus and it reads a timer as it was cast. Kind of confusing!

MSDPSTRING\_AFFECTS = " SPELL\_SHIELD : -1, armor : 1673, god sanctuary : 4159, fluidity : 

3152, BONUS\_REDUCE\_DAMAGE : -1, ARMOR : -1, ",

Would this be acceptable?

</div>

<div class="post" data-post-id="34947" data-author="DarkArtist" data-date="2014-03-27T00:25:23+00:00" data-subject="Re: Aegis, Sanc, and Fluidity = &amp;quot;None&amp;quot; in mudlet affects">

That would be lovely, thank you.

</div>
