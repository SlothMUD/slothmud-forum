---
title: "S.M.A.C."
topic_id: 664
author: "Zeizel"
date: 2004-12-08T03:47:23+00:00
last_activity: 2004-12-08T15:51:55+00:00
last_author: "Zeizel"
sticky: false
locked: false
post_count: 2
---

<div class="post" data-post-id="3229" data-author="Zeizel" data-date="2004-12-08T03:47:23+00:00" data-subject="S.M.A.C.">

For any fellow anglers out there, I created for myself the 'fish' and 'nofish' commands. Simply type 'fish' to begin fishing, and 'nofish' to stop automatically fishing (you will still need to 'reelin' your current cast).

Hope \*someone\* finds it usefull, or at least fun <img src="/images/smilies/icon_razz.svg" alt=":-P" title=":-P" width="15" height="15" class="smiley nozoom">

```
#alias {fish} {/action {^You pull your arm back and try to cast out your line, but it gets all tangled up. Try again.} {castout};/action {^You feel a very solid pull on your line!} {reelin;castout};/action {^Your line suddenly jumps to life... FISH ON!!!} {reelin;castout};castout} {G|Fishing}

#alias {nofish} {/unaction {You feel a very solid pull on your line!};/unaction {You pull your arm back and try to cast out your line, but it gets all tangled up. Try again.};/unaction {Your line suddenly jumps to life... FISH ON!!!}} {G|Fishing}
```

</div>

<div class="post" data-post-id="3236" data-author="Zeizel" data-date="2004-12-08T15:51:55+00:00" data-subject="">

I just realized that I forgot to mention my script changes the command character to '/'. (I couldn't stand pressing '#')

If you don't have your script making this change, just replace /action with #action and /unaction with #unaction.

\---------

I also want to point out that I realize this is a very simple script. I was fishing and gossipping the other day, and got a little bored. When a geek gets bored, he's just gotta code \_something\_ <img src="/images/smilies/icon_e_wink.svg" alt=";-)" title=";-)" width="15" height="15" class="smiley nozoom">.

I found myself using this a number of times after I first wrote it, so I thought maybe someone else would be interested.

</div>
