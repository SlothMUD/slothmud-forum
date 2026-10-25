---
title: "Fishing script"
topic_id: 2197
author: "bellafea"
date: 2006-11-30T23:45:28+00:00
last_activity: 2006-12-03T17:51:21+00:00
last_author: "12345"
sticky: false
locked: false
post_count: 11
---

<div class="post" data-post-id="15394" data-author="bellafea" data-date="2006-11-30T23:45:28+00:00">

Anyone have a fishing script for zmud they would like to share? if so please post it here.. or message me either way. 

thanks

bella

</div>

<div class="post" data-post-id="15395" data-author="13" data-date="2006-12-01T01:26:58+00:00">

How hard can it be, fish for 5 mins, pay attention to the messages, incorporate them with the appropriate actions..I made mine on wintin in

about 10 minutes.  Are you too lazy to spend ten minutes writing your

own script?

</div>

<div class="post" data-post-id="15396" data-author="Krok" data-date="2006-12-01T02:30:38+00:00">

You need it fishing so rarely, but when you need, all you have to do is write like 5 triggers :) (I remake mine all the time, so I can't share)

</div>

<div class="post" data-post-id="15397" data-author="Nascosto" data-date="2006-12-01T05:13:53+00:00">

and then there are sharks...

</div>

<div class="post" data-post-id="15404" data-author="Corinn" data-date="2006-12-01T14:29:22+00:00">

All this talk about fishing is frightening me... :shock:

</div>

<div class="post" data-post-id="15408" data-author="13" data-date="2006-12-01T17:05:01+00:00">

that sig kills me krok

</div>

<div class="post" data-post-id="15427" data-author="bellafea" data-date="2006-12-03T05:31:52+00:00">

well thanks for the help, didnt expect any.. after all this is sloth where most of the bitter players come to play, you know the type.. 13.. possibly?

</div>

<div class="post" data-post-id="15428" data-author="12345" data-date="2006-12-03T07:59:00+00:00">

Laugh... there's nothing bitter about it.  It's just the sheer ubsurbity of the request.  It's been a while since I used my autofisher, but I used to set it religiously while boating until sharks happened.  You'll need to add a trigger to drop sharks... other than that, your script is a grand total of 4 lines long in wintin.net 2.x:

#defgroup Fishing

#action  {^You feel a very solid pull on your line!} {reelin;castout} {G|Fishing} {T|WT}

#action  {^You pull your arm back and try to cast out your line} {castout} {G|Fishing} {T|WT}

#action  {^You reel in a sand tiger shark! Nice catch!} {drop shark;take shark;junk shark} {G|Fishing} {T|WT}

#action  {^Your line suddenly jumps to life... FISH ON!!!} {reelin;castout} {G|Fishing} {T|WT}

Viola.  Wield a pole and castout.. script does the rest.  You might want to have it put fish in a container or something... I never worried about it though.

</div>

<div class="post" data-post-id="15429" data-author="12345" data-date="2006-12-03T08:00:46+00:00">

Oh, nevermind, it seems I have a trigger to deal with sharks as well.  Simple script indeed.

</div>

<div class="post" data-post-id="15431" data-author="13" data-date="2006-12-03T16:28:20+00:00">

wouldn't you be bitter if you had lost about 2 solid years of playtime to a game you can't stop playing?

</div>

<div class="post" data-post-id="15433" data-author="12345" data-date="2006-12-03T17:51:21+00:00">

Do you know how many games that I have bought that I wished would last 2 years? At least with Sloth I can't say I didn't get my money's worth.

BTW, I just noticed that the shark action should end with another castout after the shark has been junked.

</div>
