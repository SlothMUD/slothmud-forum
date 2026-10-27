---
title: "Changelog 2017-08-17"
topic_id: 4785
author: "*teker*"
date: 2017-08-17T15:16:42+00:00
last_activity: 2017-08-17T15:16:42+00:00
last_author: "*teker*"
sticky: false
locked: false
post_count: 1
---

<div class="post" data-post-id="38403" data-author="*teker*" data-date="2017-08-17T15:16:42+00:00" data-subject="Changelog 2017-08-17">

MSDP GROUP2 and GROUP2\_JSON is hopefully fixed.

I made some changes to MSDP CHARACTER\_AFFECTS and CHARACTER\_AFFECTS\_JSON. They're not quite right but now you can see a couple new things.

1\) Endure pain / defy pain will now show up in the variables. The DURATION field needs fixed but the MODIFY value is COOL\_DOWN. This means you've used endure or defy and can't use it again. Once the cool down period ends, these skills will disappear from MSDP.

2\) Clerics and mages that use backstab or deathgrip know that these skills interfere with aerial servant and mirror image recasts. So now aerial servant and mirror image will show up with COUNT or POINTS = 0 (depending on the spell) and a DURATION indicating how long you have to wait until you can recast. This one is missing the MODIFY value so I'll work on getting that fixed.

The basic idea is to let you know how long you have to wait until you can reuse particular skills/spells. I'm open to putting these in text in one of the score commands somewhere - any suggestions?

</div>
