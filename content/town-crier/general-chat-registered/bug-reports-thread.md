---
title: "bug reports thread"
topic_id: 3435
author: "Stab"
date: 2010-05-25T20:24:03+00:00
last_activity: 2010-05-29T19:05:12+00:00
last_author: "Stab"
sticky: false
locked: false
post_count: 16
---

<div class="post" data-post-id="31225" data-author="Stab" data-date="2010-05-25T20:24:03+00:00">

Howdy all, I can't seem to get any links to open off the main page.

I use IE 7 for a browser.

Links will not open either for tabbed browsing or by just plain clicking on link.?? I get an 'Operation Aborted' poppup with the link address included.

I've been gone a week. Auto logon didn't work but I was able to just log on to forums to post. Thankee:)

Stab.

</div>

<div class="post" data-post-id="31228" data-author="*Breeze*" data-date="2010-05-26T09:02:49+00:00">

i am not sure why you cant open the links.  the left side menu is javascript.  do you have javascript disabled ?

i have tested in the latest versions of :

Firefox (ok)

Internet Explorer 8 (ok)

Safari (ok)

Google Chrome  (has css rendering issues)

</div>

<div class="post" data-post-id="31229" data-author="Tuck" data-date="2010-05-26T13:19:26+00:00">

Tested with Opera 9 - working good.

</div>

<div class="post" data-post-id="31230" data-author="Stab" data-date="2010-05-26T23:43:32+00:00">

Yes javascript is enabled. I've gone over many possibilties looking for a culprit. Currently I can open the crier. go figure.:) , the Pirates Clan site, Original Sloth, and Wintin.net. None of the live links nor cartography, library, quests, or site map will open. They start to open but stops and then , I see a blank amber colored template then a message stating that Internet Explorer cannot open the '' siteaddresshere''. (which matches the window url/link exacly). Then............Operation Aborted then the "cannot display webpage page" with typical diagnoses information...   check connect.. more info includes:This problem can be caused by a variety of issues, includes: 

Internet connectivity has been lost. 

The website is temporarily unavailable. 

The Domain Name Server (DNS) is not reachable. 

The Domain Name Server (DNS) does not have a listing for the website's domain.

I'm using IE 7.0.5730.13  

I do see that IE 7.0.RCI has been tested at java site. very top left of slothpage. so that opens also.. Is get another browser my only option? I just like a multi-tabbed page for ease of swithing pages.

Hey Thanks,

I can send a screenshot.??

</div>

<div class="post" data-post-id="31231" data-author="*Breeze*" data-date="2010-05-27T01:41:57+00:00">

benq@slothmud.org :)

as for tabs,

firefox 3.6.x, ie 8 and safari support tabs...

either way will go thru template code again when i get the time.

</div>

<div class="post" data-post-id="31232" data-author="Stab" data-date="2010-05-27T01:57:46+00:00">

hey thanks. you really are on the stick. I tryed upping to IE 8. and ran into some issues. Apparently I don't update enough.. like very rarely. 

I'll get by.:)

</div>

<div class="post" data-post-id="31234" data-author="*Breeze*" data-date="2010-05-27T07:38:54+00:00">

i would still be interested in seeing the screenshot.  i may be able to figure out whats going on and fix it, or tell you what to fix

</div>

<div class="post" data-post-id="31235" data-author="blackmore" data-date="2010-05-27T14:40:55+00:00">

Just a suggestion, try clearing your cache.  It sounds like you're pulling down some wrong files.  There are very few reasons why you would be getting this problem and nobody else, so it has to be something weird with your setup.  My other standard answer is to stop using IE, it's still (even with IE8) the worst POS browser on the market, and all the other options are just as free.

</div>

<div class="post" data-post-id="31237" data-author="Stab" data-date="2010-05-27T18:22:56+00:00">

Good suggestion Blackmore :)  I just got IE 8 and many links open. Some still do not, like maps. I do see that EQ list is being worked on. Some links open after a couple refreshes after getting this screen first...

here goes. um insert image was sorta big. <LINK_TEXT text="http://www.flickr.com/photos/49586927@N ... otostream/">http://www.flickr.com/photos/49586927@N06/4645512066/in/photostream/</LINK_TEXT> so the second one was referred to earlier with Operation aborted deal.

Okies, more later:). back to work. u get bonus pix.:) Our house n hill.

John /Stab

 :oops:  here u go ![](http://farm5.static.flickr.com/4007/4645512066_8562f2eb45.jpg)

![](http://farm5.static.flickr.com/4072/4644892429_f5986a0e53.jpg)

 

Hope they help.

</div>

<div class="post" data-post-id="31240" data-author="Tuck" data-date="2010-05-27T19:46:54+00:00">

omg, you just posted photocopy of your destop!  :roll: 

why not just make a screenshot?

</div>

<div class="post" data-post-id="31241" data-author="Stab" data-date="2010-05-27T22:05:54+00:00">

I guess I was used to my old tektronix 0 scope setup for taking pictures of waveforms for documentation..

the save as would have been far easier but not nearly as much fun.

And one cannot save the windows popup warning like that. dont think.

</div>

<div class="post" data-post-id="31244" data-author="blackmore" data-date="2010-05-28T02:34:26+00:00">

> ***Benq* wrote:**
> Google Chrome  (has css rendering issues)

From what I'm reading, actually Chrome is the only one following the standards on this one, and that's the problem.  It looks like the problem is the left side menu is set to float: left, but the main div is centered with a width of 760px, but is not floating.  What's interesting is that even firebug shows the main area in a different place than it really is.  I think if you add a float: left to middle-big, it would fix it.  I haven't played  with my cached files to prove it, though.

</div>

<div class="post" data-post-id="31247" data-author="*Breeze*" data-date="2010-05-28T04:52:25+00:00">

*should* be fixed thanks to blackmore

</div>

<div class="post" data-post-id="31255" data-author="Stab" data-date="2010-05-28T19:14:30+00:00">

Maybe  I'll try again to get chrome browser successfully installed. Maps are sure handy. My IE 8 is running fine in all modes every where cept here.

JS debugger snagged an undefined line referencing lightbox builders.node . like line 132 ? I tried comparing pages that would and will not load. IE 8 does have some great modes for builders n writers, both of which I am not.

I'm about through with it. happy debugging.

PS. I just got an opera browser and everything works just fine. It flies!

thx Tuk

</div>

<div class="post" data-post-id="31259" data-author="*Breeze*" data-date="2010-05-29T01:20:56+00:00">

should be good now on IE

</div>

<div class="post" data-post-id="31260" data-author="Stab" data-date="2010-05-29T19:05:12+00:00">

Excellent, grats on a great site. Easy to navigate, lots of info.

</div>
