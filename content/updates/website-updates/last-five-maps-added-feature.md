---
title: "\"Last Five Maps Added\" feature"
topic_id: 215
author: "Enea"
date: 2004-06-21T13:37:38+00:00
last_activity: 2004-06-21T21:20:36+00:00
last_author: "Enea"
sticky: false
locked: false
post_count: 2
---

<div class="post" data-post-id="818" data-author="Enea" data-date="2004-06-21T13:37:38+00:00" data-subject="&quot;Last Five Maps Added&quot; feature">

Dan suggested this feature, so I've gone & added it.

I had to add a datestamp field to the database to handle it, so it'll be a bit inaccurate until five more maps have been added.  From that point forward, clicking the "Last Five Maps Added" link on the maproom's main page (the one that lists the continents) will give a table containing links & bare-bones descriptions of the last five maps added.

-Enea

</div>

<div class="post" data-post-id="821" data-author="Enea" data-date="2004-06-21T21:20:36+00:00" data-subject="fixed the earlier problem">

I'm basing the 'recentness' of the entries on an autonumber field now, instead of on the datestamp field.  This means it now has them in the correct order & all that.

Enjoy :)

-Enea

</div>
