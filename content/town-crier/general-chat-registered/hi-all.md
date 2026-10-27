---
title: "Hi All!"
topic_id: 3019
author: "OldTower"
date: 2009-01-29T18:27:18+00:00
last_activity: 2009-02-01T19:44:04+00:00
last_author: "blackmore"
sticky: false
locked: false
post_count: 10
---

<div class="post" data-post-id="27907" data-author="OldTower" data-date="2009-01-29T18:27:18+00:00" data-subject="Hi All!">

I just got a completely random impulse to type "www.slothmud.org" in my browser to see what's up and if the old MUD was still running. I can't believe how many old names I recognize. I can't even remember how long it's been.

So, how's everybody doing?

Tower

(Former Coder)

</div>

<div class="post" data-post-id="27908" data-author="Yasik2" data-date="2009-01-29T18:34:04+00:00" data-subject="">

o hai thar, Da Bruiser T ! <img src="/images/smilies/icon_e_biggrin.svg" alt=":D" title=":D" width="15" height="15" class="smiley nozoom"> 

long time no see

</div>

<div class="post" data-post-id="27910" data-author="Bazilus" data-date="2009-01-29T18:57:52+00:00" data-subject="Re: Hi All!">

> <strong>OldTower wrote:</strong>
> I just got a completely random impulse to type "www.slothmud.org" in my browser to see what's up and if the old MUD was still running. I can't believe how many old names I recognize. I can't even remember how long it's been.
> 
> 
> 
> So, how's everybody doing?
> 
> 
> 
> Tower
> 
> (Former Coder)

Hey Tower!

Bazilus

</div>

<div class="post" data-post-id="27913" data-author="Weasel" data-date="2009-01-29T19:45:22+00:00" data-subject="">

Hey there. What ever happened to SparkMud? Was that what it was called? I remember trying to logon a few times but to no avail. Hope you're doing well <img src="/images/smilies/icon_e_smile.svg" alt=":)" title=":)" width="15" height="15" class="smiley nozoom">

</div>

<div class="post" data-post-id="27914" data-author="OldTower" data-date="2009-01-29T20:26:20+00:00" data-subject="">

Basically the people who had signed on to help build the world lost interest and stopped logging on, and I didn't have time or desire to do it all myself. SparkMUD became a testbed of new coding ideas (like using a sql database for player/object/mob/help files) until I eventually lost interest myself, let the domain name expire and shut it down. I still have everything associated with it except the website which somehow got lost.

> <strong>Weasel wrote:</strong>
> Hey there. What ever happened to SparkMud? Was that what it was called? I remember trying to logon a few times but to no avail. Hope you're doing well <img src="/images/smilies/icon_e_smile.svg" alt=":)" title=":)" width="15" height="15" class="smiley nozoom">

</div>

<div class="post" data-post-id="27915" data-author="jezer" data-date="2009-01-30T01:06:33+00:00" data-subject="">

> <strong>OldTower wrote:</strong>
> Basically the people who had signed on to help build the world lost interest and stopped logging on, and I didn't have time or desire to do it all myself. SparkMUD became a testbed of new coding ideas (like using a sql database for player/object/mob/help files) until I eventually lost interest myself, let the domain name expire and shut it down. I still have everything associated with it except the website which somehow got lost.

MySQL is perfect for doing this kind of stuff... It would get rid of all the files, makes the data more secure (from corrupt russian imms <img src="/images/smilies/icon_e_wink.svg" alt=";)" title=";)" width="15" height="15" class="smiley nozoom"> ), and you can use database logins to set permissions. I find MySQL performance is pretty darn fast as well... only annoying thing is the language syntax changes from time to time. It could also be used to update the website... good bye eq list... Also all that library stuff on the website could be converted to tables queried by php (for the website) and sloth (the game) together. Hence all updates would be live in both systems. Unfortunately implementation in a game such as sloth, would probably end up being a minor rewrite as parts would require overhaul or upgrading... imagine redoing all the constants in a database format, heh. I nominate Kjartan to make these changes, while Judge works on cool stuff for avatars <img src="/images/smilies/icon_razz.svg" alt=":P" title=":P" width="15" height="15" class="smiley nozoom"> . If you could make a start on that tomorrow... thank you <img src="/images/smilies/icon_twisted.svg" alt=":twisted:" title=":twisted:" width="15" height="15" class="smiley nozoom">

</div>

<div class="post" data-post-id="27916" data-author="OldTower" data-date="2009-01-30T04:32:52+00:00" data-subject="">

> <strong>jezer wrote:</strong>
> > <strong>OldTower wrote:</strong>
> > Basically the people who had signed on to help build the world lost interest and stopped logging on, and I didn't have time or desire to do it all myself. SparkMUD became a testbed of new coding ideas (like using a sql database for player/object/mob/help files) until I eventually lost interest myself, let the domain name expire and shut it down. I still have everything associated with it except the website which somehow got lost.
> 
> 
> 
> 
> 
> MySQL is perfect for doing this kind of stuff... It would get rid of all the files, makes the data more secure (from corrupt russian imms <img src="/images/smilies/icon_e_wink.svg" alt=";)" title=";)" width="15" height="15" class="smiley nozoom"> ), and you can use database logins to set permissions. I find MySQL performance is pretty darn fast as well... only annoying thing is the language syntax changes from time to time. It could also be used to update the website... good bye eq list... Also all that library stuff on the website could be converted to tables queried by php (for the website) and sloth (the game) together. Hence all updates would be live in both systems. Unfortunately implementation in a game such as sloth, would probably end up being a minor rewrite as parts would require overhaul or upgrading... imagine redoing all the constants in a database format, heh. I nominate Kjartan to make these changes, while Judge works on cool stuff for avatars <img src="/images/smilies/icon_razz.svg" alt=":P" title=":P" width="15" height="15" class="smiley nozoom"> . If you could make a start on that tomorrow... thank you <img src="/images/smilies/icon_twisted.svg" alt=":twisted:" title=":twisted:" width="15" height="15" class="smiley nozoom">

You pretty much hit the nail on the head. Massive benefits and web integration to the database (something I started to do, but lost when the website code got lost). Also allowed administrative change access via a web-based tool also. I was doing thing like editing help files from the website. Or better yet, hello creating an area via web tool!

You're also right in that it required a major rewrite. Something I could do starting from scratch, but trying it on a live game is not a good idea.

Anyway, I didn't really pop in to talk shop, just thought I'd send a wave to everybody. My second daughter is due in just over a week so I'm feeling pretty good. And scared. <img src="/images/smilies/icon_e_smile.svg" alt=":)" title=":)" width="15" height="15" class="smiley nozoom">

</div>

<div class="post" data-post-id="27924" data-author="Sind" data-date="2009-01-30T16:44:06+00:00" data-subject="">

Hey there T, long time no see <img src="/images/smilies/icon_e_smile.svg" alt=":)" title=":)" width="15" height="15" class="smiley nozoom">

So was free time killing successful w/o mud coding? <img src="/images/smilies/icon_e_smile.svg" alt=":)" title=":)" width="15" height="15" class="smiley nozoom">

ps and cmon, slothmud web client for masses!

</div>

<div class="post" data-post-id="27932" data-author="Weasel" data-date="2009-01-30T22:54:53+00:00" data-subject="">

> <strong>OldTower wrote:</strong>
> Anyway, I didn't really pop in to talk shop, just thought I'd send a wave to everybody. My second daughter is due in just over a week so I'm feeling pretty good. And scared. <img src="/images/smilies/icon_e_smile.svg" alt=":)" title=":)" width="15" height="15" class="smiley nozoom">

Hey gratz Tower! Good luck with the demon spawn! <img src="/images/smilies/icon_twisted.svg" alt=":twisted:" title=":twisted:" width="15" height="15" class="smiley nozoom">

</div>

<div class="post" data-post-id="27965" data-author="blackmore" data-date="2009-02-01T19:44:04+00:00" data-subject="">

Hey Matt, ltns. Congratz on your spawn to be. Send me an email. dean.wagner@expensewire.com.

</div>
