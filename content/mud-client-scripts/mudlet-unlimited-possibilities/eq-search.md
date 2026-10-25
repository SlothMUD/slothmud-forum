---
title: "EQ Search"
topic_id: 5116
author: "Woody"
date: 2024-12-07T21:38:26+00:00
last_activity: 2024-12-07T21:38:26+00:00
last_author: "Woody"
sticky: false
locked: false
post_count: 1
---

<div class="post" data-post-id="40141" data-author="Woody" data-date="2024-12-07T21:38:26+00:00" data-subject="EQ Search">

Are you sick of typing out EQ searches?

This trigger makes item descriptions in shops clickable links!

perl-regex pattern:

```
^[ *!&]?\d+\s+([a-zA-Z\s'’-]+?)(?=\s*(?:\[\d+\])?(?:\.\.|$))
```

lua:

```
local item_string = matches[2]
local baseURL = "https://eq.slothmud.org/?search="
selectString(item_string, 1)
setLink([[openUrl("]]..baseURL..item_string:gsub(" ", "+")..[[")]], "Search EQ list for: "..item_string)
```

Let me know if you find any item descriptions which don't work.

Woody (Slice)

</div>
