---
title: "Message-window?"
topic_id: 950
author: "achazia"
date: 2005-03-17T09:44:41+00:00
last_activity: 2006-03-29T00:13:25+00:00
last_author: "Rajil"
sticky: false
locked: false
post_count: 9
---

<div class="post" data-post-id="5128" data-author="achazia" data-date="2005-03-17T09:44:41+00:00">

Hi!

As far as I can understand there should be a way in zmud to catch all

speaking to a separate window? Anyone knows how to do that?

/Achazia

</div>

<div class="post" data-post-id="5148" data-author="Blastem" data-date="2005-03-17T15:20:02+00:00">

#TRIG {tells you} {#cap tells;#beep;#gag} tells

This will open a window called tells and put the lines in it and beeps when someone tells you something. 

Blastem

</div>

<div class="post" data-post-id="5161" data-author="achazia" data-date="2005-03-18T06:50:36+00:00">

Hi!

Thanks a lot for your answer!

Is it possible to catch all speaking to this window. Like the channels

and "say" also?

/Achazia

</div>

<div class="post" data-post-id="5168" data-author="karl" data-date="2005-03-18T11:44:53+00:00">

Here is the script that I use.  It doesn't capture 'says' but you should be able to do that from this example.

[code:36lzwdo2]

#CLASS {CaptureChannels}

#TRIGGER {^(%w) tells you '} {#PLAY C:\Windows\System32\oobe\images\clickerx.wav;#SUBSTITUTE {~[%time("hh:mm:ss")~] %1 tells you '};#CAPTURE Channels;#GAG;#CLASS GrabChannel 1}

#TRIGGER {^(%w) ({gossips|gossip|newbies|newbie|auctions|auction|shouts|shout})--} {#PLAY C:\Windows\System32\oobe\images\clickerx.wav;#SUBSTITUTE {~[%time("hh:mm:ss")~] %1 %2--};#CAPTURE Channels;#GAG;#CLASS GrabChannel 1}

#TRIGGER {^(%w)[chat]> '*'} {#CW "[chat]>" 159}

#CLASS 0

[/code:36lzwdo2]

</div>

<div class="post" data-post-id="5884" data-author="slice" data-date="2005-04-30T11:56:04+00:00">

This is what i use for my capture, it's also useful for immortals as well.

I also deliberately don't capture says & grouptells by choice.  But you could easily add those if you wished.  I like Karl's idea of adding the time of the tell as well that'd be useful

[code:2r1w4pn8]#CLASS {talk} {enable}

#TRIGGER {BEEPS} {#PLAY ChatBeep.wav} "" {case|notrig}

#TRIGGER {^(*) tells you '*'$} {#CAPTURE tell;#GAG;#IF (@afkmode = 1) {tell %1 I am sorry @me is away right now, you may leave a message here};#rem tell %1 E-mail: @me~@erkenbrand.demon.co.uk;#rem tell %1 ICQ: 1820796}}

#TRIGGER {^%w has joined channel: *.$} {#CO green;#CAPTURE tell;#GAG}

#TRIGGER {^%w has left this channel: *$} {#CO red;#CAPTURE tell;#GAG}

#TRIGGER {^%w~[*~]~> '*'$} {#CAPTURE tell;#GAG}

#TRIGGER {^* -> '*'$} {#CAPTURE tell;#GAG}

#TRIGGER {^(*) gossips-- '*'$} {#CAPTURE tell;#GAG}

#TRIGGER {^(*) auctions-- '*'$} {#CAPTURE tell;#GAG}

#TRIGGER {^You gossip-- '*'$} {#CAPTURE tell;#GAG}

#TRIGGER {^You tell (*) '*'$} {#CAPTURE tell;#GAG}

#TRIGGER {^You auction-- '*'$} {#CAPTURE tell;#GAG}

#TRIGGER {^(*) quests-- '*'$} {#CAPTURE tell;#GAG}

#TRIGGER {^You quest-- '*'$} {#CAPTURE tell;#GAG}

#TRIGGER {^(*) newbies-- '*'$} {#CAPTURE tell;#GAG}

#TRIGGER {^You newbie-- '*'$} {#CAPTURE tell;#GAG}

#TRIGGER {^You page the gods with '*'$} {#CAPTURE tell;#GAG}

#TRIGGER {^(*) pages with '*'$} {#CAPTURE tell;#GAG}

#CLASS 0[/code:2r1w4pn8]

</div>

<div class="post" data-post-id="8819" data-author="Ryvral" data-date="2005-09-25T06:07:09+00:00">

when someone sends a long message part of it gets lost as it doesn't auto scroll down..

Anyway to fix this?

</div>

<div class="post" data-post-id="11856" data-author="Rajil" data-date="2006-03-28T18:40:34+00:00">

If there's still anyone using zMUD ...

Using the channel splitter, I can only log one window.  :( 

It's either the main window where the room descriptions are or the channels window where i direct all channels. How can I log both windows?

</div>

<div class="post" data-post-id="11859" data-author="Blastem" data-date="2006-03-28T23:37:53+00:00">

do you want them to log to the same file or diff files?

#ali log {:tell:#LOG {%time(mm-dd-yy)tell.txt};:channel:#LOG {%time(mm-dd-yy)CHANNEL.txt}}

This will log tell window and channel window to tell.txt and channel.txt

hope this helps

Blastem

</div>

<div class="post" data-post-id="11860" data-author="Rajil" data-date="2006-03-29T00:13:25+00:00">

Thanks! :D

</div>
