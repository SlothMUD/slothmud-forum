---
title: "Mudlet lags on long messages"
topic_id: 5029
author: "Insomnia"
date: 2021-08-31T13:08:06+00:00
last_activity: 2021-09-06T18:15:40+00:00
last_author: "cnl"
sticky: false
locked: false
post_count: 4
---

<div class="post" data-post-id="39801" data-author="Insomnia" data-date="2021-08-31T13:08:06+00:00" data-subject="Mudlet lags on long messages">

Am I the only one who gets terrible Mudlet lags when it processes long multi-line output messages? –

- look fury

look shadow

look conquerors

look area (in extra large areas like CK)

Every time I do this, Mudlet hangs for several seconds. Disabling triggers helps, but it's not a solution. Any ideas how to fix this? The built-in Mudlet debug window doesn't show anything helpful.

</div>

<div class="post" data-post-id="39802" data-author="Insomnia" data-date="2021-09-01T04:25:40+00:00" data-subject="Re: Mudlet lags on long messages">

Oh, I've found the problem... It came from a very old trigger for parsing gjobs with a crazy long regexp pattern. Does anyone have a good solution for parsing all group members gjobs?

</div>

<div class="post" data-post-id="39806" data-author="*teker*" data-date="2021-09-04T14:30:09+00:00" data-subject="Re: Mudlet lags on long messages">

I'll add it to MSDP GROUP2

</div>

<div class="post" data-post-id="39811" data-author="cnl" data-date="2021-09-06T18:15:40+00:00" data-subject="Re: Mudlet lags on long messages">

very cool, thanks

 \>

```
lua sendMSDP("REPORT","GROUP2")

<968hp 857ma 349mv -% @15959>
[4:53 pm] (overcast)

lua msdp.GROUP2
{
 Fuligin = {
 CLASS = "Mage",
 HIT_POINTS = {
 CURRENT = "968",
 MAXIMUM = "968"
 },
 JOB = "TombJade",
 LEVELS = "9.40",
 MANA_POINTS = {
 CURRENT = "857",
 MAXIMUM = "857"
 },
 MOVEMENT_POINTS = {
 CURRENT = "349",
 MAXIMUM = "349"
 },
 POSITION = "Leader",
 STATUS = "Ok"
 }
}
```

</div>
