---
title: "eating and drinking while asleep"
topic_id: 1687
author: "*juggleblood*"
date: 2006-01-27T11:46:41+00:00
last_activity: 2006-01-27T11:46:41+00:00
last_author: "*juggleblood*"
sticky: false
locked: false
post_count: 1
---

<div class="post" data-post-id="10357" data-author="*juggleblood*" data-date="2006-01-27T11:46:41+00:00">

#defgroup {hunger}

#action  {^You are hungry} {#if {$sleep=1} {wa;yawn;get food $bag; eat food;burp;sleep} else {get food $bag;eat food}} {G|hunger}

#action  {^You are thirsty} {#if {$sleep=1} {wa;drink barrel;hiccup;sleep}; #if {$sleep=0} {drink barrel}} {G|hunger}

#action  {It's empty already} {#if {$sleep=1}{wa;stand;fillerup} else fillerup} {G|hunger}

#alias  {hungoff} {#disable hunger; #showme Hunger and Thirst Disabled} {G|hunger}

#alias {fillerup} {cast 'create water' barrel}{G|hunger}

#defgroup {sleep}

#action  {^You go to sleep} {#var sleep 1} {G|sleep}

#action  {^You wake,} {#var sleep 0} {G|sleep}

Don't forget to set the mybag variable to tell the script the name of the container you keep your food in.

Cheers

</div>
