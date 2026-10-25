---
title: "Warcry + auto-reporter reports incorrect changes"
topic_id: 5060
author: "Insomnia"
date: 2022-05-22T22:44:36+00:00
last_activity: 2022-05-22T22:44:36+00:00
last_author: "Insomnia"
sticky: false
locked: false
post_count: 1
---

<div class="post" data-post-id="39946" data-author="Insomnia" data-date="2022-05-22T22:44:36+00:00">

Happens literally every time:

```
<1086/1510hp 743/610ma 380/458mv -% -17.4>
A chasme demon hates your guts!
You've got a great feeling about this fight!
A chasme demon makes a strange sound, as you place a thunderbolt in its back.
A chasme demon makes a strange sound, as you place a thunderbolt in its back.
You report 1186/1510 hp. Change: +153. Need: 324. Spells: glowing, greater fluidity.
<1186/1510hp 743/610ma 360/458mv 95% -17.4>
```

Expected: "1239/1510hp" or "Change: +100."

```
<1265/1510hp 661/610ma 457/458mv -% -17.4>
An armanite demon hates your guts!
You've got a great feeling about this fight!
An armanite demon makes a strange sound, as you place a thunderbolt in her back.
You report 1365/1510 hp. Change: +131. Need: 145. Spells: glowing, greater fluidity.
<1365/1510hp 661/610ma 437/458mv 96% -17.4>
```

Expected: "1396/1510hp" or "Change: +100."

</div>
