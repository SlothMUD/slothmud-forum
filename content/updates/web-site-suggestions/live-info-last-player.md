---
title: "Live Info: last player"
topic_id: 327
author: "Falsra"
date: 2004-08-04T09:30:36+00:00
last_activity: 2004-08-04T13:49:22+00:00
last_author: "Anon"
sticky: false
locked: false
post_count: 6
---

<div class="post" data-post-id="1255" data-author="Falsra" data-date="2004-08-04T09:30:36+00:00" data-subject="Live Info: last player">

I think MUD software once in N minutes drops WHO and GWHO results into

text files and Live info uses those files. If i right it can be difficult to create, but stil

it would be nice to have a possibility to get last player info though web site.

( you can use sockets and do a real mud login with some test char and execute a command ).

thx

F

</div>

<div class="post" data-post-id="1256" data-author="Ender" data-date="2004-08-04T11:38:05+00:00" data-subject="Last player">

I'd be surprised if this happens. Short of creating a java script that reads the player files directly from the web page (which is entirely possible) the number of changes you'd have to make in-game is pretty impressive. Suffice it to say that it is much easier to implement who and gwho than it would be for last player.

On this same note, has anyone else noticed the advantages the web based versions of who and gwho allow? Just curious.

</div>

<div class="post" data-post-id="1257" data-author="Alberich" data-date="2004-08-04T12:38:18+00:00" data-subject="">

"advantage"? not really, but it's quite cool, to check, see if friends are on who you may want to stop by and chat with (and conversly, if there are people who annoy the hell out of you on, can either log in later, or know you will have to turn off gossip at login <img src="/images/smilies/icon_e_smile.svg" alt=":)" title=":)" width="15" height="15" class="smiley nozoom"> )

would be very cool to have time started viewable from website too, btw <img src="/images/smilies/icon_razz.svg" alt=":P" title=":P" width="15" height="15" class="smiley nozoom">

</div>

<div class="post" data-post-id="1258" data-author="Ender" data-date="2004-08-04T13:05:53+00:00" data-subject="Time Booted">

Agreed. Actually, I \_thought\_ that the time booted was part of who once upon a time... 

With the number of reboots occurring lately, time started is actually becoming critical information... Can the time booted be added to who? This would make it available on the web site by corollary.

</div>

<div class="post" data-post-id="1259" data-author="Falsra" data-date="2004-08-04T13:08:11+00:00" data-subject="">

i did not mean java or java scripts, no way.

php has socket functions ( should be enabled first with configure run ).

those socket functions allow you to set a normal session with slothmud.org:6101 and

execute any normal mortal commands, then store output and send parsed output

to web client and logoff.

it is a way to extend Live info functions without even touching main software, without

external calls , etc. 

F

</div>

<div class="post" data-post-id="1260" data-author="Anon" data-date="2004-08-04T13:49:22+00:00" data-subject="advantage">

An advantage I've noticed is that if you're a newbie without det invis or infravision, you can still head to the website to do a gwho and see all the groups. Also, if a leader is shapeshifted his group disappears on the mud, not sure if that is available on the website though.

</div>
