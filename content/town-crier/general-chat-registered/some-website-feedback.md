---
title: "Some website feedback"
topic_id: 1663
author: "Grue"
date: 2006-01-17T18:28:06+00:00
last_activity: 2006-01-19T20:45:42+00:00
last_author: "Clink"
sticky: false
locked: false
post_count: 17
---

<div class="post" data-post-id="10168" data-author="Grue" data-date="2006-01-17T18:28:06+00:00">

Few things

a) This may be an ie only thing, but whenever you roll the mouse over the logo that spans the top of the screen e.g. going from the site to any of the manus at the top, it flashes white and redownloads. It's no biggie, but it get annoying after a while.

b) A home button in the list on the left would be nice.

</div>

<div class="post" data-post-id="10169" data-author="Deju" data-date="2006-01-17T18:48:36+00:00">

If you click anywhere on the top "Slothmud III" image, it links to the home page... i suspect this is probably why there is no "home" link on the left-side list.

</div>

<div class="post" data-post-id="10170" data-author="Clink" data-date="2006-01-17T19:00:31+00:00">

What version of ie?  I use 6.0.29 and don't see what you describe.

</div>

<div class="post" data-post-id="10171" data-author="12345" data-date="2006-01-17T19:55:13+00:00">

I have 6.0.28000....

I get it to.  When you mouseover the panorama.jpg it flashes white for a second.  It doesn't do it just once either, it happens every time the mouse is over it.

I'm also using my work machine, which is Windows 2000, but the resources are good enough that it shouldn't be speed, memory or connection related.

I scanned the source and from my meager understanding, didn't see anything that might account for it.  The header on the old site never gave me this type of affect though.

Of interesting note, if you move the cursor off the banner while it's flashing, the message that appears in the status bar at the bottom says:

Downloading picture [<LINK_TEXT text="http://www.slothmud.org/themes/Andergas ... norama.jpg">http://www.slothmud.org/themes/Andergast/images/panorama.jpg</LINK_TEXT>](http://www.slothmud.org/themes/Andergast/images/panorama.jpg)

Again, not sure why a mouseover would cause a complete refresh of that window... but that appears to be exactly what it does.

</div>

<div class="post" data-post-id="10172" data-author="blackmore" data-date="2006-01-17T21:16:41+00:00">

I'm not seeing the flashing image, though when I mouse over the image, I do get a series of hyphens that go across the center of the image.  One shows up under the dragon's tail, the others are across horizontally from that one.  They're not a big deal, I just thought I'd point it out.

</div>

<div class="post" data-post-id="10174" data-author="12345" data-date="2006-01-17T21:40:22+00:00">

Yeah, at home and using IE 6.0.29, I got the same thing as blackmore.  Probably wouldn't have noticed if Blackmore hadn't mentioned it :)

</div>

<div class="post" data-post-id="10176" data-author="Grue" data-date="2006-01-17T22:06:53+00:00">

6.0.29 with sp2 running on Windows XP sp2 here on a Dell notebook, and it is very noticeable on this machine.

Also notice if I try log in at teh forum it fails still, have to log in from the bottom left.

</div>

<div class="post" data-post-id="10178" data-author="Weasel" data-date="2006-01-17T22:30:00+00:00">

ditto here.. looking at coding.. using a mix of css and tables might be the issue.. IE is a friggin pain at times with css..

[code:svjhofla]

<td colspan="5">

&lt;div id="header" onclick="location.href='http://www.slothmud.org'"title="SlothMUD's Home";><a href="http://www.slothmud.org/">

<table width="100%" class="panorama" height="140">

&lt;STYLE>

.panorama{ cursor:pointer; }

&lt;/STYLE>

						<tr>

....etc

[/code:svjhofla]

Just use a normal html href tag for the link should solve it ...also didn't see a closing tag for that td colspan, but was only a quick look..

</div>

<div class="post" data-post-id="10182" data-author="*Splork*" data-date="2006-01-17T22:55:09+00:00">

My IE and Firefox, the top shows up correctly. So unless somebody can email me a fix I won't be able to track down the bug. Maybe Clink can look at it when he gets a chance. The problem I have been running into is one set of code works for IE, and an entire different set works for Firefox. So basically I just hacked the hell out of it until it looked correctly in the browsers I have been using to test it with...

We are trying to clean up the site, so I removed the home link and added the clickable top picture. Hopefully we will figure out how to fix the image problem....

Also, I am using IE 6.028 sp1 because sp2 screwed up my dual core system. Maybe it has something to do with the sp2 shrugs...

</div>

<div class="post" data-post-id="10195" data-author="12345" data-date="2006-01-18T13:34:16+00:00">

Ok, I'm back at work again.  IE 6.0.28 and SP1 to boot.  Still flashing, and now I notice the dashes as well... though on an interesting note, they appear to be colored to blend into the background.

So all I can really say is that it doesn't seem to be a SP2 issue.

</div>

<div class="post" data-post-id="10203" data-author="Weasel" data-date="2006-01-18T19:04:05+00:00">

Is there a [/div] tag somewhere for the [div id="header" ...] tag there in that first table? Can't spot it..

..seem to have that panorama as an inline style, as a table class, and as a div class.. probably confusing the poor little MS browser.. heh. 

Maybe just set that area as a div id with the background as the panarama.jpg in the style sheet, then create a transparent 1px by 1px gif and in that space use it as the link to the homepage with the gif resized to width 100% and height 140px..

 ie:

in the css place something like this:

[code:2guj48p3]

#headspace {

	margin: 0px auto;

	height: 140px;

	background: url("http://path_to/panarama.gif");

	}

[/code:2guj48p3]

and in the page code place this:

[code:2guj48p3]

<div id="headspace">

<a href="http://www.slothmud.org"><img src="http://path_to/transparent.gif" width="100%" height="142" border="0" alt="home" /></a>

</div>

[/code:2guj48p3]

yes?

</div>

<div class="post" data-post-id="10211" data-author="*Splork*" data-date="2006-01-18T20:20:44+00:00">

Weasel's stuff was way over my head, but I think I found the bug anyways due to his work...

Please check and see if it still shows up odd for those of you who this affected...

Thanks Weasel,

Splork

</div>

<div class="post" data-post-id="10212" data-author="12345" data-date="2006-01-18T20:31:42+00:00">

My work computer shows perfect.  Nice!  :D

</div>

<div class="post" data-post-id="10215" data-author="Grue" data-date="2006-01-18T22:17:22+00:00">

Fixed for me. Thanks muchly Splork.

</div>

<div class="post" data-post-id="10217" data-author="12345" data-date="2006-01-18T23:18:55+00:00">

Shows perfect at home as well, very nice :)

</div>

<div class="post" data-post-id="10225" data-author="Blastem" data-date="2006-01-19T19:20:57+00:00">

[<LINK_TEXT text="http://www.slothmud.org/index.php?modul ... unc=search">http://www.slothmud.org/index.php?module=pnAuction&func=search</LINK_TEXT>](http://www.slothmud.org/index.php?module=pnAuction&func=search)

Error! Called unknown function: pnAuction_user_search()

search broke :)

</div>

<div class="post" data-post-id="10230" data-author="Clink" data-date="2006-01-19T20:45:42+00:00">

Search never worked, but it didn't quite give this ugly of a response.  I'll just take the links with missing features off the site when I get home.

Clink

</div>
