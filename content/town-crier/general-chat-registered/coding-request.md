---
title: "Coding Request"
topic_id: 2752
author: "*juggleblood*"
date: 2008-03-07T04:55:47+00:00
last_activity: 2008-03-09T00:51:29+00:00
last_author: "jezer"
sticky: false
locked: false
post_count: 11
---

<div class="post" data-post-id="23128" data-author="*juggleblood*" data-date="2008-03-07T04:55:47+00:00" data-subject="Coding Request">

A while ago Splork was taking requests for mxp and prompt. I was wondering if I could ask for 

sector type for prompt: would be cool to instantly know in prompt what kind of terrain you are walking thru.

position for mxp: could do things like #if $position!= 'sleeping' blah blah ..etc

anyone else would use that besides me?

</div>

<div class="post" data-post-id="23130" data-author="Rynquald" data-date="2008-03-07T05:27:42+00:00" data-subject="">

The position thing would be handy, atm you get stuck actioning every string for a position change to reset your own position var. What I do, but it's not as simple as having an MXP var.

</div>

<div class="post" data-post-id="23131" data-author="Akasha" data-date="2008-03-07T06:23:29+00:00" data-subject="">

It's only a handful of position strings you need.

You sit down and rest your tired bones.

You sit down.

You go to sleep.

Then the wake, and stand msgs.

And finally, trying to perform an action while sitting, resting, and sleeping to reset anything that got twisted.

So altogether about 15 strings to manipulate this script. I know <img src="/images/smilies/icon_razz.svg" alt=":P" title=":P" width="15" height="15" class="smiley nozoom"> I use it.

Once you get these strings its a simple trigger folder:

\#trigger{^You sit down.}{#var charpos Sitting}

etc

Aka

</div>

<div class="post" data-post-id="23132" data-author="Rynquald" data-date="2008-03-07T07:07:19+00:00" data-subject="">

I guess it is only a few. Forgot how simple it was, haven't looked at anything but the var for two years <img src="/images/smilies/icon_e_smile.svg" alt=":)" title=":)" width="15" height="15" class="smiley nozoom">

</div>

<div class="post" data-post-id="23148" data-author="*juggleblood*" data-date="2008-03-08T18:27:35+00:00" data-subject="">

I have another coding request. Image that group leader could do this based on your rank in the honor system:

Zukt has ordered you to be silent for 1 hour (tick).

grouptell heh, you almost have as many chars as brad!

You think about your orders and remain silent.

grouptell wtf was that? my orders?

You grouptell-- 'wtf was that? my orders'

You have disobeyed a direct order.

You have been penalized 20 honor.

Honor penalties have been doubled for the next 24 hours (ticks).

grouptell oh, that sucks

You grouptell--'oh, that sucks'

You have disobeyed a direct order.

You have been penalized 40 honor.

Honor penalties have been quadrupled for the next 96 hours(ticks).

or

Shimbo has ordered you to remain posted for 1 hour (tick).

recite recall

You think about your orders and then stay put. 

recite recall

You recite a scroll of recall which dissolves.

You have disobeyed a direct order.

You have been penalized 40 honor.

Honor penalties have been tripled for the next 72 hours(ticks).

</div>

<div class="post" data-post-id="23149" data-author="Weasel" data-date="2008-03-08T18:34:57+00:00" data-subject="">

<img src="/images/smilies/icon_eek.svg" alt=":shock:" title=":shock:" width="15" height="15" class="smiley nozoom"> so a group leader could order me to stfu and cost me honor points if I try to gtell for a heal, or staff, or missed cache, or turn off autolooter, or that I'm webbed, or tank-whining, or whatever? Don't think so yo.. <img src="/images/smilies/icon_razz.svg" alt=":P" title=":P" width="15" height="15" class="smiley nozoom">

How about they play my char for me and tell me later if I had a good time or not? LOL.

</div>

<div class="post" data-post-id="23150" data-author="*juggleblood*" data-date="2008-03-08T18:39:10+00:00" data-subject="">

Yeah, but think what a great incentive that is to get rank. 

order weasel stfu 1

I'm sorry, you may only stfu people below your own rank.

</div>

<div class="post" data-post-id="23151" data-author="Roadrunr" data-date="2008-03-08T18:42:26+00:00" data-subject="">

> <strong>Weasel wrote:</strong>
> <img src="/images/smilies/icon_eek.svg" alt=":shock:" title=":shock:" width="15" height="15" class="smiley nozoom"> so a group leader could order me to stfu and cost me honor points if I try to gtell for a heal, or staff, or missed cache, or turn off autolooter, or that I'm webbed, or tank-whining, or whatever? Don't think so yo.. <img src="/images/smilies/icon_razz.svg" alt=":P" title=":P" width="15" height="15" class="smiley nozoom">
> 
> 
> 
> How about they play my char for me and tell me later if I had a good time or not? LOL.

you didnt now stfu while I get you killed a couple more times because I told all the healers to hold mana and if they heal you they lose honor.

</div>

<div class="post" data-post-id="23153" data-author="Weasel" data-date="2008-03-08T19:33:30+00:00" data-subject="">

LOL.. perhaps I should be a cleric prime

</div>

<div class="post" data-post-id="23155" data-author="Rynquald" data-date="2008-03-08T22:09:56+00:00" data-subject="">

Would you still loose honor if you just killed your leader when you disagreed with their orders? <img src="/images/smilies/icon_e_smile.svg" alt=":)" title=":)" width="15" height="15" class="smiley nozoom">

</div>

<div class="post" data-post-id="23157" data-author="jezer" data-date="2008-03-09T00:51:29+00:00" data-subject="">

Ok, say lets say your a private tank... and your whining after being gagged by your leader...

You are viciously massacred by Alhoon

You are viciously massacred by Alhoon

You are viciously massacred by Alhoon

You are viciously massacred by Alhoon

You are viciously massacred by Alhoon

You are viciously massacred by Alhoon

You are viciously massacred by Alhoon

gt 10hp 200ma 100mv NEEDED [ 900 ]

You have lost 40 honor points...

You are Dead...

You are Diseased...

You Have nothing...

You are Nothing...

You are Demoted...

Press any key to play a better mud!

gt AEGIS will fall in 1 Tick

You have lost 40 honor points...

gt I am now Protecting Mandos

gt Rub my the Gods Protect You

You have lost 40 honor points...

</div>
