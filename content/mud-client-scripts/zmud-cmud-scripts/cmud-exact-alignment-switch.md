---
title: "CMUD: Exact Alignment Switch"
topic_id: 3421
author: "Gladavar"
date: 2010-05-12T06:25:15+00:00
last_activity: 2010-05-12T07:02:43+00:00
last_author: "Gladavar"
sticky: false
locked: false
post_count: 2
---

<div class="post" data-post-id="31148" data-author="Gladavar" data-date="2010-05-12T06:25:15+00:00" data-subject="CMUD: Exact Alignment Switch">

```
#switch (%mud.currentalign > 999) {#var Alignment %insert(.,%mud.currentalign,3)} 
  (%mud.currentalign < -999) {#var Alignment %insert(.,%mud.currentalign,4)}
  {#var Alignment %insert(.,%mud.currentalign,2)}
```

Throw this in a trigger that fires fairly often like one for your prompt and it will capture your exact alignment into the variable @Alignment  .  Assuming you have MXP enabled.  You can then display that variable how ever you want, status window, button caption, echo from alias, or even #sub it to the end of your prompt if you wanted.

</div>

<div class="post" data-post-id="31149" data-author="Gladavar" data-date="2010-05-12T07:02:43+00:00" data-subject="">

```
#switch (%mud.currentalign > 999) {#var Alignment %insert(.,%mud.currentalign,3)} 
  (%mud.currentalign < -999) {#var Alignment %insert(.,%mud.currentalign,4)}
  (%mud.currentalign < -99) {#var Alignment %insert(.,%mud.currentalign,3)}
  {#var Alignment %insert(.,%mud.currentalign,2)}
```

forgot a line when i was pasting this should be right.

</div>
