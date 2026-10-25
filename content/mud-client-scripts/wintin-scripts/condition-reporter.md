---
title: "Condition Reporter"
topic_id: 3636
author: "Strago"
date: 2011-01-19T15:33:33+00:00
last_activity: 2011-01-19T15:33:33+00:00
last_author: "Strago"
sticky: false
locked: false
post_count: 1
---

<div class="post" data-post-id="32336" data-author="Strago" data-date="2011-01-19T15:33:33+00:00">

This script is a condition reporter, with the health bar colored in red.

The escape character is hidden before the [, you will not see the colors correctly unless you get this character so you must copy and paste from this post instead of simply typing this out, if you want it colorized.

#defgroup {Condition}

#substitute  {awful condition.} {AWEFUL CONDITION [31m[*------][0m} {G|Condition}

#substitute  {big nasty wounds and scratches.} {BIG NASTY WOUNDS [31m[***----][0m} {G|Condition}

#substitute  {bleeding awfully from big wounds.} {MORTALLY WOUNDED [31m[-------][0m} {G|Condition}

#substitute  {excellent condition.} {EXCELLENT CONDITION [31m[*******][0m} {G|Condition}

#substitute  {quite a few wounds.} {FEW WOUNDS [31m[****---][0m} {G|Condition}

#substitute  {few scratches.} {FEW SCRATCHES [31m[******-][0m} {G|Condition}

#substitute  {pretty hurt.} {PRETTY HURT [31m[**-----][0m} {G|Condition}

#substitute  {small wounds and bruises.} {SMALL WOUNDS [31m[*****--][0m} {G|Condition}

#defgroup {}

#substitute  {few scratches.} {FEW SCRATCHES [31m[******-][0m} {G|Condition}

#substitute  {pretty hurt.} {PRETTY HURT [31m[**-----][0m} {G|Condition}

#substitute  {small wounds and bruises.} {SMALL WOUNDS [31m[*****--][0m} {G|Condition}

#defgroup {}

</div>
