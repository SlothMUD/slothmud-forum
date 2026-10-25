---
title: "engage mob success should be 100% when not engaged"
topic_id: 5059
author: "cnl"
date: 2022-05-13T17:52:02+00:00
last_activity: 2022-05-30T01:29:55+00:00
last_author: "cnl"
sticky: false
locked: false
post_count: 4
---

<div class="post" data-post-id="39945" data-author="cnl" data-date="2022-05-13T17:52:02+00:00">

This is a pretty minor inconvenience, but my suggestion is if using engage to start fighting a mob, and player is not already in combat, I suggest the success rate should be 100%

It makes sense that if switching targets that there should be a failure rate, but sometimes I initiate combat with engage mob when not fighting anyone and it's rather funny that I fail. Maybe Fuligin is pretty near-sighted and attacked the bushes instead? haha

I use engage instead of assist, or sometimes engage just to start battles. I just want status to be fighting but not necessarily be lagged.

Assist gets you a quick hit on the mob but lags you until the next round of combat, engage has you enter combat but take no action until the next round of combat give me a moment to choose an action if wanted.

thanks

</div>

<div class="post" data-post-id="39948" data-author="Driven" data-date="2022-05-28T15:29:25+00:00">

I know failing engage is somewhat annoying, but there is no lag on a failed engage, which means you can just do #3 engage target.  Is there some reason why this doesn't work?  You can build this into your client.  Maybe I'm missing something other than the annoyance factor?

</div>

<div class="post" data-post-id="39949" data-author="cnl" data-date="2022-05-28T19:03:39+00:00">

#3 engage is a good idea, i'll try that.

</div>

<div class="post" data-post-id="39950" data-author="cnl" data-date="2022-05-30T01:29:55+00:00">

I tested this some and although the command has no lag it introduces 500ms of latency. (or 250ms per attempt)

I didn't test that much but ran into a few cases of double failures so the failure % is relatively high.

I'm assuming I'll run into triple failures on occasion 

```
You failed to get your attack in.Engage @:0.4210000038147
<1095hp 2103ma 388mv -% @0>
[12:49 pm] (fair) -10 9646710334
You failed to get your attack in.Engage @:0.64000010490417
<1095hp 2103ma 388mv -% @0>
[12:49 pm] (fair) -10 9646710334
You turn your attacks toward a female citizen [target].Engage @:0.89000010490417
```

I think I'll just settle on a trigger based approach since it may have more latency but most of the time 1st will take anyway

</div>
