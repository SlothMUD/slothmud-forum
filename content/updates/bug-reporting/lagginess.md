---
title: "Lagginess"
topic_id: 4522
author: "Dragoth"
date: 2015-09-09T08:34:19+00:00
last_activity: 2015-09-10T19:02:36+00:00
last_author: "Dragoth"
sticky: false
locked: false
post_count: 15
---

<div class="post" data-post-id="36080" data-author="Dragoth" data-date="2015-09-09T08:34:19+00:00">

Alright, since I do have some tools at my disposal that can actually analyze this, I wanted to raise this issue and it's been bugging me for awhile now.

This is the connection, this ping test is done using a programm called paping.

For not computer-savvy people, ping is the reaction time of your connectionâ€“how fast you get a response after you've sent out a request. A fast ping means a more responsive connection, especially in applications where timing is everything (like video games). Ping is measured in milliseconds (ms).

![](http://i.imgur.com/8QvDoVJ.jpg)

So we send a signal to a server and receive a response in 216milliseconds on average.

And now this is the ingame log with a timestamp, from which we can clearly see that the actual response time ingame is over double that of my ping. 1000ms is 1 second, so from a 220ms reponse time, we go to almost a second delay from when I type a command in, to the time i get a message back from the mud.

Where is this time lost ?  

hr:mn:sc:mils

11:05:34.964a | <878hp 836ma 312mv>cast 'water breathing' <<=== This is an echo of command input sent to mud

11:05:35.628a | Ok.  <<=== This is response from the mud to my command, which is delayed by 35,628-34,964= 664ms, this is 3x of my actual ping time.

11:05:35.633a | You feel new horizons in substances to be breathed. <<=== This is internal delay between consecutively sent lines 5ms 

Here is more

hr:mn:sc:mils

11:05:35.633a | 

11:05:35.633a | <878hp 826ma 312mv>

11:05:35.906a | ---

11:05:35.906a | <878hp 826ma 312mv>cast 'water breathing'

11:05:36.364a | Ok.

11:05:36.379a | You feel more secure in your water-breathing.

11:05:36.379a | 

11:05:36.379a | <878hp 816ma 312mv>

11:05:36.780a | ---

11:05:36.780a | <878hp 816ma 312mv>cast 'water breathing'

11:05:37.365a | You weave the threads of magic masterfully!

11:05:37.381a | Masterful *water breathing* renewed to [28 minutes and 50 seconds]

11:05:37.381a | You feel more secure in your water-breathing.

11:05:37.381a | 

11:05:37.381a | <878hp 806ma 312mv>

11:05:37.681a | ---

11:05:37.681a | <878hp 806ma 312mv>cast 'water breathing'

11:05:38.365a | Ok.

11:05:38.381a | You feel more secure in your water-breathing.

11:05:38.381a | 

11:05:38.381a | <878hp 797ma 312mv>

11:05:38.617a | ---

11:05:38.617a | <878hp 797ma 312mv>cast 'water breathing'

11:05:39.128a | Ok.

11:05:39.134a | You feel more secure in your water-breathing.

11:05:39.134a | 

11:05:39.134a | <878hp 788ma 312mv>

11:05:39.564a | ---

11:05:39.564a | <878hp 788ma 312mv>cast 'water breathing'

11:05:40.128a | Ok.

11:05:40.134a | You feel more secure in your water-breathing.

11:05:40.137a | 

11:05:40.137a | <878hp 778ma 312mv>

11:05:40.550a | ---

11:05:40.550a | <878hp 778ma 312mv>cast 'water breathing'

11:05:41.128a | Ok.

11:05:41.133a | You feel more secure in your water-breathing.

11:05:41.134a | 

11:05:41.134a | <878hp 769ma 312mv>

11:05:41.381a | ---

11:05:41.381a | <878hp 769ma 312mv>cast 'water breathing'

11:05:41.865a | Ok.

11:05:41.881a | You feel more secure in your water-breathing.

11:05:41.881a | 

11:05:41.881a | <878hp 759ma 312mv>

11:05:43.401a | ---

11:05:43.402a | <878hp 759ma 312mv>think

11:05:43.864a | You think about life, the universe and everything.

11:05:43.864a | 

11:05:43.880a | <878hp 761ma 312mv>

11:05:44.185a | ---

11:05:44.187a | <878hp 761ma 312mv>think

11:05:44.618a | You think about life, the universe and everything.

11:05:44.618a | 

11:05:44.618a | <878hp 761ma 312mv>

11:05:45.105a | ---

11:05:45.106a | <878hp 761ma 312mv>think

11:05:45.627a | You think about life, the universe and everything.

11:05:45.629a | 

11:05:45.630a | <878hp 762ma 312mv>

11:05:45.933a | ---

11:05:45.933a | <878hp 762ma 312mv>think

11:05:46.627a | You think about life, the universe and everything.

11:05:46.629a | 

11:05:46.630a | <878hp 763ma 312mv>

11:05:46.864a | ---

11:05:46.864a | <878hp 763ma 312mv>think

11:05:47.380a | You think about life, the universe and everything.

11:05:47.380a | 

11:05:47.380a | <878hp 763ma 312mv>

11:06:00.806a | <878hp 763ma 312mv>You are hungry.

11:06:00.809a | You are thirsty.

11:06:00.811a | 

11:06:00.813a | <878hp 772ma 312mv>

11:06:06.612a | <878hp 772ma 312mv>save

11:06:07.197a | Saving Crumbs.

11:06:07.199a | Saving items.

11:06:07.200a | 

11:06:07.201a | <878hp 776ma 312mv>

11:06:07.203a | <878hp 776ma 312mv><[-60]md>

11:06:07.203a |

On an unrelated note, I had this error pop up when I disabled mccp compression. 

![](http://i.imgur.com/eW31Udv.jpg)

</div>

<div class="post" data-post-id="36081" data-author="Dragoth" data-date="2015-09-09T08:59:59+00:00">

And just to make sure that this was not normal, i tested this on another mud, which had around 200 players online (which should load the server more ?) 

![](http://i.imgur.com/nLDcSCx.jpg)

The pings are slightly better here as well

Their server location:

![](http://i.imgur.com/dQzNOrG.jpg)

But the response times are just lightning quick

11:45:16.260a | [*Daily Blessing*] [2544/2544hp 1766/1851mn 2876/2876mv 0qt 568tnl] >

11:45:16.713a | ---

11:45:16.713a | think <<=== This is input command 

11:45:16.884a | Think what? <<=== This is reponse from the mud 

16,884-16,713=171ms which is almost exactly the same as the ping time.

11:45:16.884a | 

11:45:16.884a | [*Daily Blessing*] [2544/2544hp 1766/1851mn 2876/2876mv 0qt 568tnl] >

11:45:17.290a | ---

11:45:17.290a | think

11:45:17.508a | Think what?

11:45:17.508a | 

11:45:17.508a | [*Daily Blessing*] [2544/2544hp 1766/1851mn 2876/2876mv 0qt 568tnl] >

11:45:17.914a | ---

11:45:17.914a | think

11:45:18.148a | Think what?

11:45:18.148a | 

11:45:18.148a | [*Daily Blessing*] [2544/2544hp 1766/1851mn 2876/2876mv 0qt 568tnl] >

11:45:18.460a | ---

11:45:18.460a | think

11:45:18.647a | Think what?

11:45:18.647a | 

11:45:18.647a | [*Daily Blessing*] [2544/2544hp 1766/1851mn 2876/2876mv 0qt 568tnl] >

11:45:19.006a | ---

11:45:19.006a | think

11:45:19.273a | Think what?

11:45:19.273a | 

11:45:19.273a | [*Daily Blessing*] [2544/2544hp 1766/1851mn 2876/2876mv 0qt 568tnl] >

11:45:19.648a | ---

11:45:19.648a | think

11:45:19.897a | Think what?

11:45:19.897a | 

11:45:19.897a | [*Daily Blessing*] [2544/2544hp 1766/1851mn 2876/2876mv 0qt 568tnl] >

11:45:20.194a | ---

11:45:20.209a | think

11:45:20.414a | Think what?

11:45:20.414a | 

11:45:20.414a | [*Daily Blessing*] [2544/2544hp 1766/1851mn 2876/2876mv 0qt 568tnl] >

11:45:20.835a | ---

11:45:20.835a | think

11:45:21.022a | Think what?

11:45:21.022a | 

11:45:21.022a | [*Daily Blessing*] [2544/2544hp 1766/1851mn 2876/2876mv 0qt 568tnl] >

11:45:21.397a | ---

11:45:21.397a | think

11:45:21.646a | Think what?

11:45:21.646a | 

11:45:21.646a | [*Daily Blessing*] [2544/2544hp 1766/1851mn 2876/2876mv 0qt 568tnl] >

11:45:21.958a | ---

11:45:21.958a | think

11:45:22.146a | Think what?

11:45:22.146a | 

11:45:22.146a | [*Daily Blessing*] [2544/2544hp 1766/1851mn 2876/2876mv 0qt 568tnl] >

11:45:22.504a | ---

11:45:22.504a | think

11:45:22.770a | Think what?

11:45:22.770a | 

11:45:22.770a | [*Daily Blessing*] [2544/2544hp 1766/1851mn 2876/2876mv 0qt 568tnl] >

11:45:23.097a | ---

11:45:23.097a | think

11:45:23.284a | Think what?

11:45:23.284a | 

11:45:23.284a | [*Daily Blessing*] [2544/2544hp 1766/1851mn 2876/2876mv 0qt 568tnl] >

11:45:23.612a | ---

11:45:23.612a | think

11:45:23.908a | Think what?

11:45:23.908a | 

11:45:23.908a | [*Daily Blessing*] [2544/2544hp 1766/1851mn 2876/2876mv 0qt 568tnl] >

11:45:30.180a | Telnet 201: comm.channel { "chan": "curse", "msg": "<ESC>[1;36m(<ESC>[1;37mCurse<ESC>[1;36m) <ESC>[0;37mMowse raises an eyebrow.<ESC>[0;37m", "player": "Mowse" }

11:45:30.195a | 

11:45:30.195a | (Curse) Mowse raises an eyebrow.

11:45:30.195a | 

11:45:30.195a |

</div>

<div class="post" data-post-id="36082" data-author="Dragoth" data-date="2015-09-09T10:28:32+00:00">

Here is another one just for the sake of it, a mud without a dedicated server and location is a bit closer to where ours is, so pings are comparable. 

![](http://i.imgur.com/TjnoIrN.jpg)

![](http://i.imgur.com/OceyWpr.jpg)

01:15:20.440p | [SAFE]<20hp 100sp 100st> think <<=== Input command

01:15:20.655p | You can't do that here. <<=== Response 20,655-20,440=225ms response time

01:15:20.655p | 

01:15:20.660p | [SAFE]<20hp 100sp 100st> 

01:15:21.075p | ---

01:15:21.075p | [SAFE]<20hp 100sp 100st> think

01:15:21.306p | You can't do that here.

01:15:21.306p | 

01:15:21.311p | [SAFE]<20hp 100sp 100st> 

01:15:21.751p | ---

01:15:21.751p | [SAFE]<20hp 100sp 100st> think

01:15:22.006p | You can't do that here.

01:15:22.006p | 

01:15:22.011p | [SAFE]<20hp 100sp 100st> 

01:15:22.432p | ---

01:15:22.432p | [SAFE]<20hp 100sp 100st> think

01:15:22.657p | You can't do that here.

01:15:22.657p | 

01:15:22.662p | [SAFE]<20hp 100sp 100st> 

01:15:23.097p | ---

01:15:23.097p | [SAFE]<20hp 100sp 100st> think

01:15:23.357p | You can't do that here.

01:15:23.357p | 

01:15:23.362p | [SAFE]<20hp 100sp 100st> 

01:15:23.737p | ---

01:15:23.737p | [SAFE]<20hp 100sp 100st> think

01:15:23.957p | You can't do that here.

01:15:23.957p | 

01:15:23.962p | [SAFE]<20hp 100sp 100st> 

01:15:24.377p | ---

01:15:24.377p | [SAFE]<20hp 100sp 100st> think

01:15:24.607p | You can't do that here.

01:15:24.607p | 

01:15:24.612p | [SAFE]<20hp 100sp 100st> 

01:15:24.962p | ---

01:15:24.962p | [SAFE]<20hp 100sp 100st> think

01:15:25.207p | You can't do that here.

01:15:25.207p | 

01:15:25.212p | [SAFE]<20hp 100sp 100st> 

01:15:25.523p | ---

01:15:25.524p | [SAFE]<20hp 100sp 100st> think

01:15:25.754p | You can't do that here.

01:15:25.754p | 

01:15:25.764p | [SAFE]<20hp 100sp 100st> 

01:15:26.059p | ---

01:15:26.059p | [SAFE]<20hp 100sp 100st> think

01:15:26.305p | You can't do that here.

----

What is wrong with our mud ?

</div>

<div class="post" data-post-id="36083" data-author="*Splork*" data-date="2015-09-09T11:53:18+00:00">

We added tracking of many functions back when we tracked down a huge cause of lag about a decade ago and from what we are seeing, there doesn't appear to be any issues. I've also grepped logs of last 10 days and Crumbs is the only character who even mentions in-game lag. I feel like a cable company rep saying this but this would normally point me to towards something on your end...

I know that we are in the middle of a ton of back-end changes which you guys don't see and some of them should actually be improving the game's performance. So I am not saying there isn't an issue because there is a chance there is.

Teker is actively looking into this and we exchanged quite a few emails yesterday regarding what changes he is making to see if we notice anything.

```
show times
Function Name                  Min      Max      Last
------------------------------------------------------
one_room_reset                 0.000001 0.077849 0.000007
Processing input               0.000003 0.023855 0.000061
Setting socket sets            0.000000 0.000114 0.000000
Processing player input        0.000000 0.000571 0.000001
Processing player inputB       0.000001 0.000521 0.000004
Processing player output       0.000000 0.012360 0.000001
ENTIRE_GAME_LOOP               0.001477 7.458982 0.335458
entering nanny                 0.000006 0.282088 0.182060
PULSE_PLAYER_REGEN             0.000007 0.760189 0.000457
save_char_db                   0.011066 0.112322 0.064748
Processing player input-after  0.000009 1.756860 0.000366
extract_char_1                 0.001777 0.004514 0.002189
extract_char_2                 0.000000 0.000014 0.000001
extract_char_3                 0.000000 0.001543 0.000001
extract_char_4                 0.000000 0.025002 0.000000
extract_char_5                 0.000000 0.000113 0.000000
extract_char_6                 0.001590 0.002702 0.002032
extract_char_7                 0.000000 0.001219 0.000003
extract_char_8                 0.000000 0.000067 0.000000
extract_char_9                 0.000000 0.001477 0.000000
extract_char_10                0.000000 0.000034 0.000001
extract_char_11                0.002996 0.029861 0.003608
extract_char_12                0.000003 0.000070 0.000005
extract_char_13                0.000000 0.000128 0.000000
extract_char_14                0.000000 0.001911 0.000200
extract_char_15                0.000000 0.083666 0.000001
PULSE_VIOLENCE                 0.007984 0.703329 0.013374
PULSE_AUCTION                  0.000013 0.085565 0.000436
PULSE_ZONE                     0.000355 0.215551 0.032732
PULSE_MOBILE                   0.194822 7.041676 0.277037
PULSE_UTILITY                  0.005650 0.039585 0.016326
PULSE_UPDATE_INN               0.000126 0.001160 0.000223
PULSES_PER_MINUTE              0.019847 0.283120 0.058628
zone_enqueue()                 0.000000 0.000017 0.000000
save_website_info_file()       0.002344 0.004512 0.003141
Processing player input-press- 0.000007 0.072857 0.000020
extract_char_16                0.000000 0.050399 0.005797
THREE_MINUTE_PULSE             0.000014 0.000084 0.000021
PLAYER_STATS                   0.010653 0.053986 0.013166
mobstat_save                   0.002840 0.036269 0.004676
FIFTEEN_MINUTE_PULSE           0.235886 1.338819 0.501576
Auto_Save/write_sac_table      0.000001 0.000004 0.000002
update_player_count()          0.000020 0.000038 0.000022
SIXTY_MINUTE_PULSE             0.014516 0.021218 0.016294
Processing player input-extend 0.000008 0.001551 0.000017
All times are in seconds.
Total stats recorded: 45, MAX_STATS: 60
```

To most people this doesn't mean much but to us, who read it everyday, it means quite a bit. Normally when we are experiencing lag, you will see the player input stats high, entire game loop around 15, and mobile activity above 10.

I just wanted you guys to know that we track just about everything and if we have to add more because there is an issue we need to track down, we will.

Splork

</div>

<div class="post" data-post-id="36084" data-author="Dragoth" data-date="2015-09-09T12:43:49+00:00">

Alright so this issue started bothering me a few days ago and the only reason I decided to actually bother with all of this, is because I really felt the game become much more responsive after shapeshifting was disabled due to a bug and after it got enabled the game hasn't been the same to me and in the last few days the lagging got outright bad (despite OK pings) so I thought that's it and decided that it might be a good time to install a second ISP line into this apartment, wanted to do that for some time anyhow.

I was pretty stoked to see 190ms pings with the new ISP, but after I logged in I didn't see much change at all, the game was still pretty sluggish. But it kinda makes sense doesn't it, how can you have laggs when you have good pings ? Doesn't make sense..

Here is the log with the new isp

(image: /[http://i.imgur.com/YxXgZId.jpg](http://i.imgur.com/YxXgZId.jpg))

03:16:01.072p | <888hp 851ma 362mv>

03:16:02.337p | ---

03:16:02.337p | <888hp 851ma 362mv>think

03:16:02.827p | You think about life, the universe and everything.

03:16:02.827p | 

03:16:02.827p | <888hp 851ma 362mv>

03:16:03.407p | ---

03:16:03.407p | <888hp 851ma 362mv>think

03:16:03.827p | You think about life, the universe and everything. <<== 420ms response time!!

03:16:03.827p | 

03:16:03.827p | <888hp 851ma 362mv>

03:16:04.197p | ---

03:16:04.197p | <888hp 851ma 362mv>think

03:16:04.837p | You think about life, the universe and everything.<<== 640ms response time :(

03:16:04.837p | 

03:16:04.837p | <888hp 851ma 362mv>

03:16:05.127p | ---

03:16:05.127p | <888hp 851ma 362mv>think

03:16:05.577p | You think about life, the universe and everything.

03:16:05.577p | 

03:16:05.577p | <888hp 851ma 362mv>

03:16:05.872p | ---

03:16:05.872p | <888hp 851ma 362mv>think

03:16:06.327p | You think about life, the universe and everything.

03:16:06.327p | 

03:16:06.327p | <888hp 851ma 362mv>

03:16:06.582p | ---

03:16:06.582p | <888hp 851ma 362mv>think

03:16:07.077p | You think about life, the universe and everything.

03:16:07.077p | 

03:16:07.077p | <888hp 851ma 362mv>

03:16:07.302p | ---

03:16:07.302p | <888hp 851ma 362mv>think

03:16:07.827p | You think about life, the universe and everything.

03:16:07.827p | 

03:16:07.827p | <888hp 851ma 362mv>

03:16:21.442p | <888hp 851ma 362mv>save

03:16:21.898p | Saving Crumbs.

03:16:21.898p | Saving items.

03:16:21.898p | 

03:16:21.898p | <888hp 851ma 362mv>

03:16:21.898p | <888hp 851ma 362mv><[0]md>

03:16:59.828p | Tiamat the dragon queen`s roar echoes the land as The Goddess Takhisis re-enters this realm!

03:16:59.828p | 

This log also looks a bit better, but it's still miles off from the other muds where we see response times on par with ping times.

Link to desktop image with debugger running

[http://i.imgur.com/1YUyXUu.jpg](http://i.imgur.com/1YUyXUu.jpg)

</div>

<div class="post" data-post-id="36085" data-author="Filk" data-date="2015-09-09T17:07:00+00:00">

I guess that shapeshift off thing could be repeated on test port? And Dragoth could do his test there. Might be some good point too look at things if lag will gone there with that change...

</div>

<div class="post" data-post-id="36087" data-author="Dragoth" data-date="2015-09-10T07:16:13+00:00">

![](http://i.imgur.com/pIECYEb.jpg)

10:08:05.236a | <885hp 815ma 362mv>

10:08:06.999a | ---

10:08:06.999a | <885hp 815ma 362mv>think

10:08:07.483a | You think about life, the universe and everything.

10:08:07.483a | 

10:08:07.483a | <885hp 818ma 362mv>

10:08:09.932a | ---

10:08:09.932a | <885hp 818ma 362mv>think

10:08:10.228a | The press gang leader arrives from the south.

10:08:10.228a | 

10:08:10.228a | <885hp 823ma 362mv>

10:08:10.634a | <885hp 823ma 362mv>You think about life, the universe and everything

10,634-09,932= 702ms command delay with 187ms pings, that is delayed by almost 4 times, a new record ?  Nope!

10:17:19.351a | 

10:17:19.351a | <885hp 836ma 344mv>

10:17:20.225a | ---

10:17:20.225a | <885hp 836ma 344mv>think

10:17:20.755a | You think about life, the universe and everything.

10:17:20.755a | 

10:17:20.755a | <885hp 836ma 344mv>

10:17:22.736a | ---

10:17:22.736a | <885hp 836ma 344mv>think

10:17:23.251a | You think about life, the universe and everything.

10:17:23.251a | 

10:17:23.251a | <885hp 836ma 344mv>

10:17:26.075a | <885hp 836ma 344mv>save

10:17:26.823a | Saving Crumbs. <<=== 748ms delay! 748/187=4.0!! I think we have a winner, for now..

10:17:26.823a | Saving items.

</div>

<div class="post" data-post-id="36088" data-author="Dragoth" data-date="2015-09-10T08:02:51+00:00">

What doesn't make sense to me, is that I've been told that creators pay nearly $1,000 a year to host this game.

With this kind of thing going on, you can run this game on a potato, for free, and it wouldn't make any kind of difference.

[<LINK_TEXT text="http://www.mudconnect.com/resources/Mud ... sting.html">http://www.mudconnect.com/resources/Mud_Resources:Mud_Hosting.html</LINK_TEXT>](http://www.mudconnect.com/resources/Mud_Resources:Mud_Hosting.html)

I see plenty of $10-20 a month hosting options there.

So if this issue is something that we have to live with, you should seriously stop wasting your money on an expensive server.

</div>

<div class="post" data-post-id="36091" data-author="Dragoth" data-date="2015-09-10T10:23:39+00:00">

Here i tested one of the muds that's hosted by a budget hoster [http://www.genesismuds.com/](http://www.genesismuds.com/)

(image: /[http://i.imgur.com/gXFr5Pg.jpg](http://i.imgur.com/gXFr5Pg.jpg))

(image: /[http://i.imgur.com/K2zBZYO.jpg](http://i.imgur.com/K2zBZYO.jpg))

Pings are great and ingame delays are only 2x ping, feels pretty smooth for 10 bucks a month.

</div>

<div class="post" data-post-id="36092" data-author="*Breeze*" data-date="2015-09-10T12:54:32+00:00">

4 points to consider..

#1 a straight out of the box mud and a 20+ year old mud are two different beasts.

#2

as of this writing, sloth is using about 434MB of RAM

that includes the backend database connections, the mud itself, the way mudl works et al.

#3

sloth will most likely never be hosted on a box we don't have control over

if we didn't open source it like someone asked a few months/year ago, why would

we put it on a server someone else controls.

#4

why does it matter what it costs us since we pay and never ask anything of you guys

ping times to that mud you tested

---------------------------------------------

Pinging 216.136.9.5 with 32 bytes of data:

Reply from 216.136.9.5: bytes=32 time=210ms TTL=53

Reply from 216.136.9.5: bytes=32 time=164ms TTL=53

Reply from 216.136.9.5: bytes=32 time=165ms TTL=53

Reply from 216.136.9.5: bytes=32 time=164ms TTL=53

Reply from 216.136.9.5: bytes=32 time=165ms TTL=53

Reply from 216.136.9.5: bytes=32 time=168ms TTL=53

Reply from 216.136.9.5: bytes=32 time=164ms TTL=53

Reply from 216.136.9.5: bytes=32 time=164ms TTL=53

my pingtimes from europe to sloth while streaming netflix

---------------------------------------------------------------------------

Pinging g.slothmud.org [71.19.249.122] with 32 bytes of data:

Reply from 71.19.249.122: bytes=32 time=179ms TTL=56

Reply from 71.19.249.122: bytes=32 time=178ms TTL=56

Reply from 71.19.249.122: bytes=32 time=178ms TTL=56

Reply from 71.19.249.122: bytes=32 time=179ms TTL=56

Reply from 71.19.249.122: bytes=32 time=179ms TTL=56

Reply from 71.19.249.122: bytes=32 time=181ms TTL=56

pinging from rick's house to sloth

------------------------------------------------

PING g.slothmud.org (71.19.249.122) 56(84) bytes of data.

64 bytes from 71.19.249.122: icmp_seq=1 ttl=49 time=101 ms

64 bytes from 71.19.249.122: icmp_seq=2 ttl=49 time=102 ms

64 bytes from 71.19.249.122: icmp_seq=3 ttl=49 time=100 ms

64 bytes from 71.19.249.122: icmp_seq=4 ttl=49 time=101 ms

64 bytes from 71.19.249.122: icmp_seq=5 ttl=49 time=99.7 ms

64 bytes from 71.19.249.122: icmp_seq=6 ttl=49 time=99.8 ms

64 bytes from 71.19.249.122: icmp_seq=7 ttl=49 time=101 ms

64 bytes from 71.19.249.122: icmp_seq=8 ttl=49 time=104 ms

64 bytes from 71.19.249.122: icmp_seq=9 ttl=49 time=101 ms

64 bytes from 71.19.249.122: icmp_seq=10 ttl=49 time=99.6 ms

64 bytes from 71.19.249.122: icmp_seq=11 ttl=49 time=99.4 ms

regardless, ping times isn't a great indicator of health.

traceroute is better, but its not a discussion i care to have.

</div>

<div class="post" data-post-id="36093" data-author="*teker*" data-date="2015-09-10T14:31:52+00:00">

The original diku code that we're still running on breaks time up into 250ms pulses.  That means that users can't execute more than 1 command every 250ms or more than 4 commands per second.  It doesn't matter what the command is - that's the maximum the game will process.  The rest get queued up and are execute "as fast as possible" but never faster than 1 command every 250ms.  That includes hitting enter on a blank line to view your prompt.

Certainly this could be changed.  It would be trivial to change constants and process commands every 125ms or faster.  The problem is that all the stuff going on in the background doesn't always fit in a 125ms pulse.  A lot of the time it doesn't fit in a 250ms pulse.  When the background stuff takes longer you see extra lag.

There are solutions for resolving this.  I've been working on optimizing the mob code and there are certainly other areas that could be improved.  Beyond that you're looking at massive changes - either building a new priority-based event system that breaks up the background tasks into smaller chunks or moving to a multi-threaded environment (if the machine has multiple cores) where different zones run on different threads.

I have no problem working on this sort of thing - but it takes time and a ton of testing.  It also pushes new features back.  In the meantime, you can expect the average latency of a command to be 125ms + your average ping time.  If things are busy in the background, it's going to take longer.

</div>

<div class="post" data-post-id="36094" data-author="Dragoth" data-date="2015-09-10T14:33:37+00:00">

Pings have little relevance to ingame lagg as seen from my log, games with nearly the same pings have very different ingame responses..

This could be due to the game itself being old and having a huge database which is poorly optimized, this could be due to badly written code causing slowdowns, this could be due to a slow server(which is probably not our case).

The first mud that I test after Sloth, has 10 times more players than sloth is one of the oldest and largest muds currently and it has no trouble keeping ingame reponse times inline with it's server ping times, so why is Sloth having those problems.

 

Regarding the server downgrade, that's the worst case scenario if you guys give up on this issue and if the costs of sustaining the mud are too high for what it is, which I've been told is the case(whispers).

But even the money is not a problem, still- why have a powerful and expensive server If the code itself is the bottleneck? It's like having a supercar to only drive around the city.

There are hosters that allow unlimited ram usage and still charge around 20-30 bucks a month.

</div>

<div class="post" data-post-id="36095" data-author="Dragoth" data-date="2015-09-10T14:35:12+00:00">

> ***teker* wrote:**
> The original diku code that we're still running on breaks time up into 250ms pulses.  That means that users can't execute more than 1 command every 250ms or more than 4 commands per second.  It doesn't matter what the command is - that's the maximum the game will process.  The rest get queued up and are execute "as fast as possible" but never faster than 1 command every 250ms.  That includes hitting enter on a blank line to view your prompt.
> 
> 
> 
> Certainly this could be changed.  It would be trivial to change constants and process commands every 125ms or faster.  The problem is that all the stuff going on in the background doesn't always fit in a 125ms pulse.  A lot of the time it doesn't fit in a 250ms pulse.  When the background stuff takes longer you see extra lag.
> 
> 
> 
> There are solutions for resolving this.  I've been working on optimizing the mob code and there are certainly other areas that could be improved.  Beyond that you're looking at massive changes - either building a new priority-based event system that breaks up the background tasks into smaller chunks or moving to a multi-threaded environment (if the machine has multiple cores) where different zones run on different threads.
> 
> 
> 
> I have no problem working on this sort of thing - but it takes time and a ton of testing.  It also pushes new features back.  In the meantime, you can expect the average latency of a command to be 125ms + your average ping time.  If things are busy in the background, it's going to take longer.

Aha, now that is THE revelation.

Thanks Teker!

</div>

<div class="post" data-post-id="36096" data-author="*Splork*" data-date="2015-09-10T17:28:32+00:00">

Great explanation Teker!

I would like to point out that this is nothing new and has been part of our game for over two decades. It has nothing to do with hosting and the majority of us have never seen it as an "issue".

In regards to hosting, we have already decided where we will be hosted if our numbers don't bounce back this winter and we continue a slow decline because you are right, its not worth paying the type of money that we do.

Honestly, if that happens, I really doubt anyone would notice a difference.

Splork

</div>

<div class="post" data-post-id="36097" data-author="Dragoth" data-date="2015-09-10T19:02:36+00:00">

Good call Splork.

But i'll stand by my subjective feelings about the mud being laggier than usual as of late. 

Teker mentions 250ms pulse + ping time, but you can see from my log that i often end up with 800ms delays while having 180-200ms pings and it should be around 450ms.

> **Quote:**
> If things are busy in the background, it's going to take longer.

I guess that's the case here

</div>
