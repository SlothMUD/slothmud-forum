---
title: "cmud/zmud mob pinger."
topic_id: 3416
author: "Gladavar"
date: 2010-05-04T14:33:48+00:00
last_activity: 2010-05-04T14:33:48+00:00
last_author: "Gladavar"
sticky: false
locked: false
post_count: 1
---

<div class="post" data-post-id="31083" data-author="Gladavar" data-date="2010-05-04T14:33:48+00:00" data-subject="cmud/zmud mob pinger.">

Not sure if anyone still uses zmud or not but here is a semi auto pinger i've been using in cmud and made sure it worked in zmud too. wouldn't take much to make it auto if you wanted.

```
ZMUD(v7.21):

#TRIG {^ping (%a) (%d)} {#LOO 1,4 {tell %{i}.%1}} pinger input

CMUD(v3.16b)

#tr {^ping (%a) (%d)} {#loop 1,%2 {tell %{i}.%1 .}}
```

\*!\*After you create the trigger in CMUD go to the editor (ctrl-G) and switch the type to Command Input.\*!\*

To use, on the command line simply type: ping MOBNAME #

Example: Ping dragon 3 would send a tell to 1.dragon 2.dragon 3.dragon

If you wanted it to ping every five minutes you could do:

```
#alarm -05:00 {ping dragon 3}
```

on the command line (should work for both clients)

if you are gonna add this to a timer or ping large numbers it wouldn't be a bad idea to throw a #wait into the loop. I understand the drawbacks of this in zmud though so i'll leave that up to you.

```

```

</div>
