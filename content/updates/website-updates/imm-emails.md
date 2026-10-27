---
title: "Imm Emails"
topic_id: 4840
author: "*Breeze*"
date: 2018-03-06T18:06:47+00:00
last_activity: 2018-03-13T04:51:42+00:00
last_author: "*Breeze*"
sticky: true
locked: false
post_count: 3
---

<div class="post" data-post-id="38691" data-author="*Breeze*" data-date="2018-03-06T18:06:47+00:00" data-subject="Imm Emails">

the @slothmud.org emails don't work anymore due to 

things beyond my control, but @slothmud.com do.

if there are enough requests for the events list to 

come back i will add it to @slothmud.com also.

</div>

<div class="post" data-post-id="38704" data-author="Josiah" data-date="2018-03-12T22:04:26+00:00" data-subject="Re: Imm Emails">

Do we have any control over the slothmud.com site? Currently I'm seeing the following:

\<html\>\<head\>\</head\>\<body\>hi\</body\>\</html\>

A redirect to slothmud.org seems like it might be good. No idea how often someone might stumble across it, but I did today!

Redirecting via meta refresh is generally discouraged in favor of a server side redirect, but it still works:

\<html\>\<head\>\<meta http-equiv="refresh" content="0; url=http://www.slothmud.org/" /\>\</head\>\<body\>Redirecting to \<a href="slothmud.org"\>slothmud.org\</a\>\</body\>\</html\>

If we want to get fancy, a server side redirect could include the 301 code for 'moved permanently' which has some impact on SEO.

</div>

<div class="post" data-post-id="38705" data-author="*Breeze*" data-date="2018-03-13T04:51:42+00:00" data-subject="Re: Imm Emails">

Will do it tonight when I get home from work.

</div>
