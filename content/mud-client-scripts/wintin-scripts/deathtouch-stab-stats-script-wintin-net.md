---
title: "Deathtouch/stab stats script Wintin.NET"
topic_id: 762
author: "*Splork*"
date: 2005-01-20T20:47:35+00:00
last_activity: 2005-01-20T20:47:35+00:00
last_author: "*Splork*"
sticky: false
locked: false
post_count: 1
---

<div class="post" data-post-id="3853" data-author="*Splork*" data-date="2005-01-20T20:47:35+00:00" data-subject="Deathtouch/stab stats script Wintin.NET">

Please change strings if you use this, you can easily make this work for backstabs by changing the trigger strings to the ones that work with those...

\#defgroup Deathtouch

\#alias {bscalcon} {bsinit;bson2;bson3;bson4} {G\|Deathtouch}

\#alias {bser} {#var stb $1;#showme --------------------------------;#showme STABBER SET TO: \<\*- $1 -\*\>;#cr} {G\|Deathtouch}

\#alias {bshitcal} {#math bshits {$bshits+1}} {G\|Deathtouch}

\#alias {bshits} {#var bshits $1} {G\|Deathtouch}

\#alias {bsinit} {bstrys 0;bshits 0;bssplork 0;bsmiss 0} {G\|Deathtouch}

\#alias {bsme} {#ac {%0 hates your Guts!} {#unvar target};#var stb Pal;aston;ltton;qston;gt I will now stab when $leader gt's: qstab} {G\|Deathtouch}

\#alias {bsmiss} {#var bsmiss $1} {G\|Deathtouch}

\#alias {bsmisscal} {#math bsmiss {$bsmiss+1}} {G\|Deathtouch}

\#alias {bsof} {#unac {%0 hates your Guts!};astof;lttof;qstof;gt I will no longer stab when $leader gt's: qstab} {G\|Deathtouch}

\#alias {bson2} {#ac {sees you circling in for the kill, and deftly steps out of the way!} {bstrycal;bsmisscal}} {G\|Deathtouch}

\#alias {bson3} {#ac {goes limp as your deathtouch} {bstrycal;bssplorkcal;bshitcal}} {G\|Deathtouch}

\#alias {bson4} {#ac {You duck under a} {bstrycal;bshitcal}} {G\|Deathtouch}

\#alias {bssho} {bssho1;bssho2;bssho3} {G\|Deathtouch}

\#alias {bssho1} {#showme ---------------------------------------------------------------} {G\|Deathtouch}

\#alias {bssho2} {#showme Touch Records: [ $bshits/$bstrys ] Hits [ $bssplork ] Splorks [ $bsmiss ] Whiffs} {G\|Deathtouch}

\#alias {bssho3} {#showme ---------------------------------------------------------------;#cr} {G\|Deathtouch}

\#alias {bssplork} {#var bssplork $1} {G\|Deathtouch}

\#alias {bssplorkcal} {#math bssplork {$bssplork+1}} {G\|Deathtouch}

\#alias {bstell} {gt Stab Records: [ $bshits/$bstrys ] Hits [ $bssplork ] Splorks [ $bsmiss ] Whiffs} {G\|Deathtouch}

\#alias {bstrycal} {#math bstrys {$bstrys+1}} {G\|Deathtouch}

</div>
