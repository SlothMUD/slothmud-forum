---
title: "Entrench / Defy"
topic_id: 4597
author: "Yasik"
date: 2016-02-26T11:29:49+00:00
last_activity: 2016-03-01T19:53:58+00:00
last_author: "*Splork*"
sticky: false
locked: false
post_count: 7
---

<div class="post" data-post-id="36645" data-author="Yasik" data-date="2016-02-26T11:29:49+00:00" data-subject="Entrench / Defy">

Hello!

I dont remember if I posted it already, if so, then consider this one as a reminder.

What makes me deeply concerned is absence of message that marks the end of above mentioned skill duration.

Now we the players must make research and script client-side this event.

Really I dont know why there is no message yet. If there is solid reason NOT to, then could you say so we not raise this matter anymore? 

Entrench duration is about 40 seconds, defy pain cooldown - 40 min or so, its not hard to code our own info\_msg, but I can see the trend to make players less code and more play, by moving lots of tasks on server-side (eq sets, for example), so why not give us what we really need long time? Actually, it can save lives being able to re-entrench in time:

You feel relaxed again. //entrench off

The fear of mortality returns to you. //defy pain off

You feel bold enough for greatest challenge. // defy pain cooldown over, skill can be used again

... or whatever you think is better.

Thanks in advance.

</div>

<div class="post" data-post-id="36650" data-author="Teron" data-date="2016-02-26T23:45:29+00:00" data-subject="Re: Entrench / Defy">

Yeah, I already ideased the end-message for entrench.

A message, when once can defy again, would help, too. In fact, a message, when defy ends (You are now vulnerable to attacks) would help as well, if some ppl wish to trigger on it.

Btw, the defy cooldown is definitely not 24 hours it is said in the help. So helpfiles or the cooldown timer need to be fixed as well.

Thanks.

</div>

<div class="post" data-post-id="36662" data-author="Yasik" data-date="2016-02-28T11:05:32+00:00" data-subject="Re: Entrench / Defy">

Also, would be nice to have one-round lag removed so we can re-entrench instantly, just like dispel magic spell works.

Also, yesterday I was bashed while being totally entrenched, so I guess this skill is not 100% solution and it actually can fail from time to time, or it is bugged somehow.

![](http://s19.postimg.org/9vtgt389v/bashed_while_entrenched.jpg)

</div>

<div class="post" data-post-id="36664" data-author="*Splork*" data-date="2016-02-28T15:43:57+00:00" data-subject="Re: Entrench / Defy">

This is normal behavior and we will pass on removing the lag <img src="/images/smilies/icon_mrgreen.svg" alt=":mrgreen:" title=":mrgreen:" width="15" height="15" class="smiley nozoom">

The down message is a good idea though...

</div>

<div class="post" data-post-id="36681" data-author="*juggleblood*" data-date="2016-03-01T01:06:12+00:00" data-subject="Re: Entrench / Defy">

> <strong>Teron wrote:</strong>
> Btw, the defy cooldown is definitely not 24 hours it is said in the help. So helpfiles or the cooldown timer need to be fixed as well.

24 hours = 24 game minutes no?

</div>

<div class="post" data-post-id="36684" data-author="Teron" data-date="2016-03-01T14:18:30+00:00" data-subject="Re: Entrench / Defy">

JB, technically, yes, when it comes to time, 24 game hrs = 24 minutes.

But I have a countdown timer that counts minutes after defy is used and I can't defy after 25 ticks or even 28 ticks, I guess the actual timer is close to 40+.

I've tried it many times after the timer has run, so I don't consider that it has an error.

</div>

<div class="post" data-post-id="36688" data-author="*Splork*" data-date="2016-03-01T19:53:58+00:00" data-subject="Re: Entrench / Defy">

We will adjust the helpfile, the skill is plenty powerful enough <img src="/images/smilies/icon_lol.svg" alt=":lol:" title=":lol:" width="15" height="15" class="smiley nozoom">

</div>
