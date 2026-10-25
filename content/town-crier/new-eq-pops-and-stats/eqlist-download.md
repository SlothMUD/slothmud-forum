---
title: "eqlist download?"
topic_id: 3848
author: "Stark"
date: 2012-02-08T15:38:18+00:00
last_activity: 2013-12-16T15:56:43+00:00
last_author: "*Breeze*"
sticky: false
locked: false
post_count: 13
---

<div class="post" data-post-id="33147" data-author="Stark" data-date="2012-02-08T15:38:18+00:00" data-subject="eqlist download?">

I'm pretty sure that there used to be a downloadable version of the eqlist, but that it was taken down due to excessive bandwidth abuse.  (if I'm remembering correctly)

Is there any way we could have some way of obtaining a local copy of the eqlist? (in whatever format is relevant)  Even if I just have to e-mail a request to someone.  I'd like to be able to use it to do some fancy filtering, sorting, and script integration that isn't possible with the web only eqlist.

Thanks!  :)

</div>

<div class="post" data-post-id="33148" data-author="Stark" data-date="2012-02-08T18:32:35+00:00" data-subject="Re: eqlist download?">

Found where Breeze commented on the topic from a year old thread:

> **Quote:**
> I would do a complete export weekly or so in xml format which could be downloaded and parsed by the clients but on the old eqlist when i did that people just linked to it directly instead of caching it which caused a ton of traffic since some moron(s) had it automatically look up every item he(they) saw, which downloaded a huge xml file each time.

from <LINK_TEXT text="http://www.slothmud.org/forum/viewtopic ... lit=eqlist">http://www.slothmud.org/forum/viewtopic.php?f=15&t=1908&hilit=eqlist</LINK_TEXT>

Soo... Breeze, any chance we could still get this in a way that can't be abused by stupid people?  :)

</div>

<div class="post" data-post-id="33149" data-author="Spink" data-date="2012-02-08T23:18:07+00:00" data-subject="Re: eqlist download?">

I would also be interested in working with a local copy of eqlist.

I'm currently using a version I cobbled together from the old eqlist interface, but it's rather out of date.

</div>

<div class="post" data-post-id="33189" data-author="celerra7" data-date="2012-03-08T10:58:44+00:00" data-subject="Re: eqlist download?">

I've been working on this idea for a while now.  I've taken blank queries of each category and saved them as HTML.  There seems to be a limitation to either the web or db that won't display all items when doing the blank query to the category ALL.

I've found the table structure in the HTML and parsed through it to get all the pertinent information, then saved into an SDF file.  The problem I run into is not all the query tables are the same - books, potions, and scrolls are different from other eq tables - the MOB and affects/bonus divisions are reversed.

Is there any further action from the im's to either allow a full listing of eq with the blank ALL query, or a weekly or monthly export posted here?

Thanks in advance for any input.  Love the game and keep the freshness going.

</div>

<div class="post" data-post-id="33190" data-author="*Breeze*" data-date="2012-03-09T09:07:34+00:00" data-subject="Re: eqlist download?">

i would be willing to temporarily remove the limit (yes there is a hard limit. i forget what i set it to)

and/or do an xml output of everything thats there.

however, my terms are ::

- if you do anything cool with it you have to show me ;)
- be willing to share whatever you come up with
- don't complain if certain eq is missing (yes there is eq that is set to not load on purpose)
- don't complain if i kill whatever xml interface i come up with due to server load

i did start writing an API for the eqlist which allows you to query the eqlist from a url,

but i didn't finish it due to lack of time, and frankly, i got kind of pissed off when

someone (not even an immortal!) TOLD me that i need to do something else before

doing the API stuff.

I will look at it and see what the current status is, but iirc the api itself is done, just the

xml output needs to be designed along with the 'how to query it' part.

it was something like  

hxxp://[www.slothmud.org/eqlist/API_KEY/Search%20Terms](http://www.slothmud.org/eqlist/API_KEY/Search%20Terms)

to search it.

Regards,

Breeze

</div>

<div class="post" data-post-id="33191" data-author="blackmore" data-date="2012-03-09T15:39:45+00:00" data-subject="Re: eqlist download?">

It sure as hell wasn't me, I would love an api. :)

</div>

<div class="post" data-post-id="33848" data-author="raincrab" data-date="2012-12-17T01:47:07+00:00" data-subject="Re: eqlist download?">

me too

bump

</div>

<div class="post" data-post-id="33948" data-author="celerra7" data-date="2013-01-28T19:50:14+00:00" data-subject="Re: eqlist download?">

I've come back around to looking at this, and I'm running into the limit inside specific categories now.  Sloth provides so many cool items, the XML DB output limit is reached.  

For instance, search LOW for ioun's pulls up the standard 4 (plus some).  But search LOW {blank} returns a nice list, but only the Blue is shown of the standard 4.  Thus I am assuming the DB limit is being hit in output.  

I would also love a list of "known" items and attributes.  Not asking for specials, quest items, undiscovered, etc.  

BTW, thanks to all the work the Imms do!

Bump.

</div>

<div class="post" data-post-id="34517" data-author="celerra7" data-date="2013-10-26T16:59:37+00:00" data-subject="Re: eqlist download?">

Bumping this.

I want to use the eqlist output as part of my client coding.  Still don't mind having to do a blank query per slot and pull from the webpage output, but again, the xml search is hitting a limit in output - example Query Low (no params) doesn't show all iouns available, since coders have given us so many items we can use LOW.

Thanks for any consideration / help with this.

</div>

<div class="post" data-post-id="34637" data-author="*Breeze*" data-date="2013-12-16T06:56:53+00:00" data-subject="Re: eqlist download?">

xml is not gonna happen.

i did do a csv search output from the eqlist that you can download and do whatever you want with, but i am not going to do xml direct queries/output. it is too much work on my side for something that i would just get complaints from anyways, get ticked off and disappear for another year.

i am also considering doing a full eqlist export into json on a weekly basis that you can download and import into your client databases but i don't want people linking their clients directly to the eqlist. causes way too many issues with webhost.

from json you can convert to xml and upload to your own webserver or something.

</div>

<div class="post" data-post-id="34638" data-author="*Breeze*" data-date="2013-12-16T10:40:12+00:00" data-subject="Re: eqlist download?">

json is done. Just need to link it later.

</div>

<div class="post" data-post-id="34639" data-author="celerra7" data-date="2013-12-16T15:50:22+00:00" data-subject="Re: eqlist download?">

Weekly updated export would be awesome.  In no way want to put burden on you or tax the systems we have.  Really appreciate you responding to the bump and finding a solution.  Thanks for all your efforts.

</div>

<div class="post" data-post-id="34640" data-author="*Breeze*" data-date="2013-12-16T15:56:43+00:00" data-subject="Re: eqlist download?">

celerra, feel free to email me and i can send you a copy of the weekly file to get started with til i figure out how to link it to the website. feel free to email me.   all immortals have @slothmud.org emails.

</div>
