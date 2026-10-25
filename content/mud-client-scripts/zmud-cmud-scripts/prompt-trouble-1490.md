---
title: "prompt trouble"
topic_id: 1490
author: "marushu"
date: 2005-10-11T16:48:21+00:00
last_activity: 2005-10-11T16:48:21+00:00
last_author: "marushu"
sticky: false
locked: false
post_count: 1
---

<div class="post" data-post-id="8995" data-author="marushu" data-date="2005-10-11T16:48:21+00:00" data-subject="prompt trouble">

Was hoping maybe one of talented coders could help me :)

I cannot seem to get my script to capture the prompt correctly.  For some reason it does not store anything inside the variables.  Any help would be greatly appreciated.

[code:1bhuz2ek]#CLASS {Prompt} {enable}

#VAR hp {}

#VAR maxhp {}

#VAR ma {}

#VAR maxma {}

#VAR mv {}

#VAR maxmv {}

#TRIGGER {^~<(%1)/(%2)hp (%3)/(%4)ma (%5)/(%6)mv~>} {

  #VAR hp %1

  #VAR maxhp %2

  #VAR ma %3

  #VAR maxma %4

  #VAR mv %5

  #VAR maxmv %6

  } "" {nocr|prompt}

#CLASS 0

[/code:1bhuz2ek]

</div>
