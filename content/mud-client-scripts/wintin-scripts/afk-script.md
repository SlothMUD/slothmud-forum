---
title: "AFK script"
topic_id: 668
author: "Zeizel"
date: 2004-12-08T23:38:03+00:00
last_activity: 2004-12-09T00:29:21+00:00
last_author: "guest"
sticky: false
locked: false
post_count: 2
---

<div class="post" data-post-id="3241" data-author="Zeizel" data-date="2004-12-08T23:38:03+00:00" data-subject="AFK script">

I know of at least one person who's asked for this, so here it is!

I'd like to point out very quickly that sometimes I MUD from my laptop. My laptop is quite a bit slower then my desktop, and I've noticed it having trouble just keeping up with WinTin. In an effort to reduce CPU load on my laptop, most of my scripts will install and uninstall triggers (or actions, as WinTin calls them) as needed. By minimizing the number of triggers WinTin is actively searching for, I hope to reduce lag as much as possible.

As for this particular script, simply type 'afk \<reason\>' to set your status as AFK, and type 'back' to return your status. 

What this script does:

When first going AFK, you automatically notify your group that you will be afk, and tell them why. The script will also update your title to inform everyone that you are AFK.

While your status is AFK, any private tells to you will be replied to automatically, informing the person that you are AFK (and why). You will also automatically stretch out your arms every tick (assuming you have your tick counter running).

When returning from AFK, you will automatically inform your group of your new status. You will also change your title back to the title you were using before going afk.

To ensure this script runs as 'advertised,' you must have a variable called $charName which contains the name of your character (as it is displayed by the game). As stated above, you must have your tick counter running to benefit from the automatic stretching.

I hope everyone finds this useful!

```
#defgroup {AFK}

#alias {afk} {#var $afk %0;{gt AFK AFK AFK!!! Reason: $afk};{#action {%1 tells you '} {reply [AFK] $afk}};#action {#TICK!!} {stretch};#action {^$charName %0 (level: %1)} {#var $oldTitle %0;#unaction {charName}};score;{title [AFK] $afk}} {G|AFK}

#alias {back} {gt BACK BACK BACK!!!;#unaction {%1 tells you};#unvar {afk};#unaction {#TICK!!};title $oldTitle;#unvar {oldTitle}} {G|AFK}

#defgroup {}
```

</div>

<div class="post" data-post-id="3243" data-author="guest" data-date="2004-12-09T00:29:21+00:00" data-subject="">

Not bad Zeizel, short and to the point. I like it.

</div>
