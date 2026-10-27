---
title: "Few fixes"
topic_id: 4481
author: "*Splork*"
date: 2015-05-03T03:33:54+00:00
last_activity: 2015-05-26T13:14:00+00:00
last_author: "*Splork*"
sticky: false
locked: false
post_count: 4
---

<div class="post" data-post-id="35888" data-author="*Splork*" data-date="2015-05-03T03:33:54+00:00" data-subject="Few fixes">

\*\* 91038 \*\* Vinjion \*\* fix masterful hammer spell so they aren't worse than 

normal hammers

 \*\* 4686 \*\* ?? \*\* add to immhelp file Fastrepop - Reset times for areas are 

improved by about 35%.

 \*\* 5802 \*\* Sochi \*\* add wanted to the list of cmds u can use while studying

 \*\* 30442 \*\* Mara \*\* allow wanted list updates during reading books. can tell already - not sure what the difference is.

 \*\* 37478 \*\* Juggleblood \*\* char\_exit\_msg should appear yellow, not white, for consistency

 \*\* 2742 \*\* Sochi \*\* give open door a proper confirmation msg other than ok: Also added to close door

 \*\* 86150 \*\* Juggleblood \*\* add ACT2 RAID to immh setm act

 \*\* 85725 \*\* Juggleblood \*\* confirmation message on setr flag: also added setr flags2

 \*\* 85728 \*\* Juggleblood \*\* confirmation msg seto xtraflag

\*\* 19427 \*\* Juggleblood \*\* confirmation msg for setr flag

 \*\* when a player prays for a holy sword and its in use, no message is given.

</div>

<div class="post" data-post-id="35889" data-author="*juggleblood*" data-date="2015-05-05T17:28:20+00:00" data-subject="Re: Few fixes">

!

Man, you guys are doing great things lately. Thanks for all the hard work. I don't have time to be very actively lately, but I'm trying to remember to vote every day.

</div>

<div class="post" data-post-id="35890" data-author="*Splork*" data-date="2015-05-06T13:13:57+00:00" data-subject="Re: Few fixes">

Thanks Juggle,

 Fixed a bug which has probably caused us a ton of odd crashes over the years where a player is listed as having a descriptor and can be seen using commands such as where or users ( for Immortals ) but was not actually in-game. This happened when someone was stuck somewhere inside our creation/login screen and either didn't close their client, browser, or whatever they were using to login with.

\-- There are now timers placed in every location on our creation/login screen. The timers are different depending upon location but should give everyone plenty of time to work their way through it without having their socket closed. However, in those rare occasions where this has happened to someone, it will close their socket and prevent any unfortunate incidents within our game.

Bugs Reported

173\) Tue May 5 18:08:26 2015 Shh 8160 

 wintin reports as in bh inn, by using where, but is not on who list, or is not seen in the inn 

with perception up.

171\) Tue May 5 08:32:58 2015 Taron 132694 

 shows Pagoda of enlightment explored 

2014-11-27 18:28:29 \*\* 72205 \*\* Josiah \*\* this area is not configured for exploration yet.

Combine that one with the fix from last week regarding new area exploration not working and the two biggest bugs remaining on my list should be fixed.

Continue to be on the look out for missing output/strings from the game, as thousands of changes are ongoing behind the scenes and there are bound to be a few hiccups. However, we are now down to 1300 occurrences of sprintfs ( replacing with snprintf's )in our code out of around 7,000 when I started this project. 

I am aware that a few people are getting strange characters upon logging in to the game. Hopefully, all of these changes plus the next round of changes will help us track this one down and stomp it.

Splork

</div>

<div class="post" data-post-id="35915" data-author="*Splork*" data-date="2015-05-26T13:14:00+00:00" data-subject="Re: Few fixes">

Below are a few more fixes going in on today's reboot. There have been reports of some garbled information being displayed when players are communicating with questers, this fix is going in next reboot.

In regards to numbers 116 and 218, some of our builders have created questers which simply share information on other quests they have to offer. These are immediately completed simply by undertaking that quest. There is no room to visit or object to give these creatures. Its a bit confusing and we will try to come up with a more graceful way of accomplishing this.

96\) Thu Apr 23 17:56:27 2015 Feist 80003 

 steal helpfile says you can steal from players 

101\) Fri Apr 24 09:34:49 2015 Fluffy 89312 

 in help forms file basilisk ability petrify should be change to actual use - gaze 

116\) Mon Apr 27 08:00:03 2015 Taron 54317 

 I've typed undertake subdued\_dragon\_corpses at Rumar and she said 'Congratulations, you have 

completed the quest 'subdued\_dragon\_corpses'!' 

117\) Mon Apr 27 08:00:12 2015 Taron 54317 

 You ask Adelina Rumar about 'subdued\_dragon\_corpses'. - Adelina Rumar tells you 'You've already 

completed that task!' 

118\) Mon Apr 27 08:00:32 2015 Taron 54317 

 I haven't given her a single subdued dragon, just a corpse of Fallon and maybe of Malign 

179\) Wed May 6 09:33:12 2015 Josiah 72320 

 gr-hydra popped grv-key-skeleton-orante-carved which causes 'Zone keys do not work on this type 

of door!' error on various doors when it is in inventory 

184\) Thu May 7 22:26:58 2015 Basche 34243 

 no help page for disarm traps 

218\) Fri May 22 22:49:02 2015 Ip 67679 

 WHen i undertake oils and perfumes quests from aukri in this room, i get Aukri tells you 'ff' 

Aukri tells you 'Congratulations, you have completed the q 

219\) Fri May 22 22:49:16 2015 Ip 67679 

 its will not let me actually do the quest 

220\) Fri May 22 23:55:25 2015 Ip 67679 

 ok, got it to work. just have to undertake differently 

223\) Mon May 25 23:14:37 2015 Josiah 10000 

 my grv-fallen-hero-ring is still unapproved. From tower of gr'valdh

</div>
