---
title: "AC changes"
topic_id: 2275
author: "kjartan"
date: 2007-01-10T17:08:51+00:00
last_activity: 2007-01-10T17:08:51+00:00
last_author: "kjartan"
sticky: false
locked: false
post_count: 1
---

<div class="post" data-post-id="16164" data-author="kjartan" data-date="2007-01-10T17:08:51+00:00" data-subject="AC changes">

We have changed the way AC -11 and lower works, and also have removed the AC cap. Our goal with this is twofold: allow hitroll eq to be valuable again, and allow eq sets that make warriors able to have lower ACs than other classes.

The new AC scheme, like the old one, changes at -10. Previously AC -11 removed about 30% of the hits you would have gotten at AC -10, except that due to a bug, it only did it occasionally and randomly for some mobs in some circumstances - most of the time it was the same as -10.

Under the new system, each full point of AC beyond -10 removes 15% of the hits you would have gotten otherwise, for everybody. These don't add linearly, they add like fire resistance. Thus AC -11 lets through 85%, -12 lets through 85%\*85%, -13 85%\*85%\*85%, etc.

Also, there was previously an effective cap on hitroll. If you could hit AC -10 95% of the time, further hitroll was worthless. Under the new system, further points of hitroll counteract points of opponent AC beyond -10. For example, say you can hit AC -10 exactly 95% of the time and your opponent has AC -11: then you will hit 95%\*85% = 80.75% of the time. But, if you gain a point of hitroll, you will be back to 95% (which is still the maximum hit chance).

We are going to lower some mob ACs in the future to numbers below -11 so that there are mobs that are hard to hit again.

</div>
