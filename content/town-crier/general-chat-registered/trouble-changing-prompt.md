---
title: "Trouble changing prompt"
topic_id: 2393
author: "banedon"
date: 2007-03-12T17:32:30+00:00
last_activity: 2007-03-13T20:42:30+00:00
last_author: "13"
sticky: false
locked: false
post_count: 6
---

<div class="post" data-post-id="17264" data-author="banedon" data-date="2007-03-12T17:32:30+00:00">

Since I made 2x40 not too long ago, I was going to change my prompt to give me more info than the default hp,ma,mv.  Whenever I try to change it, It is not working at all, for example:

If I try 

prompt <$hhp $mma $vmv $aac>  

Ill get 

<hhp mma vmv aac>  

as what shows up as my prompt.  I've read the help file on the mud, and unless I'm just totally missing the boat, I'm entering things right.  If I'm not please let me know where I'm going wrong.

Thanks in advance.

</div>

<div class="post" data-post-id="17265" data-author="Medios" data-date="2007-03-12T18:20:24+00:00">

You need to figure out how to send text as-is.  With wintin type # then enter.    Otherwise your client is going to send $$ and mess it up.

Mike

</div>

<div class="post" data-post-id="17266" data-author="13" data-date="2007-03-12T18:45:10+00:00">

come kill some shit with us fisher

</div>

<div class="post" data-post-id="17271" data-author="12345" data-date="2007-03-12T21:05:38+00:00">

In wintin.net I send the prompt like so:

prompt <$$h/$$Hhp $$m/$$M $$v/$$V $$A $$a>

The $$ seems to work.

Another cool addition you can do with wintin:

prompt <$$h/$$Hhp $$m/$$M $$v/$$V $$A $$a mDk>

Any sequence of characters that will never happen will work...

Then use your client for something along this line:

#sub {mDk>} {$mobcondvar $sancstat>}

This will allow you to track anything you like in your prompt.  In the example given, I'm tracking what the mob looked like last time I looked at it (useful in high spam) and if my lite is up down or about to fall, etc.

</div>

<div class="post" data-post-id="17277" data-author="banedon" data-date="2007-03-13T04:40:21+00:00">

In wintin.net I send the prompt like so:

prompt <$$h/$$Hhp $$m/$$M $$v/$$V $$A $$a>

[/quote:uvp5w4ms]

Thanks that worked for me

</div>

<div class="post" data-post-id="17280" data-author="13" data-date="2007-03-13T20:42:30+00:00">

you could log in on telnet and change it dude

</div>
