---
title: "Automatically assist in warcry"
topic_id: 1626
author: "*Splork*"
date: 2005-12-31T14:48:08+00:00
last_activity: 2005-12-31T14:48:08+00:00
last_author: "*Splork*"
sticky: false
locked: false
post_count: 1
---

<div class="post" data-post-id="9950" data-author="*Splork*" data-date="2005-12-31T14:48:08+00:00" data-subject="Automatically assist in warcry">

Many wintin.net users have requested this because they have been hardcoding the tank's warcry. This is more generic and shouldn't ever have to be changed...

\#alias {vcry} {#var crier $1;#showme \<\*- $1 -\*\> is doing the warcries.} {G\|Groupname}

\#action {^$crier yells '%1'} {warcry $1} {G\|Groupname}

Put these in whatever group you want them in, my action is in General group and the alias is in my variable group.

Then simply type vcry playername(whomever is crying). Whenever they begin their warcry, you will quickly join in with whatever it is they yell.

Enjoy,

Splork

</div>
