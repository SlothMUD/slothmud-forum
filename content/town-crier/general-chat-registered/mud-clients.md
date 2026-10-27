---
title: "MUD Clients"
topic_id: 753
author: "Yasik"
date: 2005-01-19T01:24:18+00:00
last_activity: 2005-01-25T04:49:00+00:00
last_author: "Nascosto"
sticky: false
locked: false
post_count: 5
---

<div class="post" data-post-id="3825" data-author="Yasik" data-date="2005-01-19T01:24:18+00:00" data-subject="MUD Clients">

Greetings, fellas!

Last 2 weeks i spent experimenting with various mud-clients, because i feel limited with capabilities of internal language of my client i used last 4+ years (JMC). Yes, there IS support of Java Script and Visual Basic Script in JMC, but new era arise and i need more and more powerful tools to bring my ideas to life. 

So, heres what i tried and my humble (and probably sometimes incorrect) opinion i have atm (reserve the right to change it):

1\. JMC

Small, fast, stable, free. JS and VBS support. Almost frozen development, poor (from my point of view) internal language, nothing left to explore <img src="/images/smilies/icon_e_smile.svg" alt=":)" title=":)" width="15" height="15" class="smiley nozoom">

2\. MMC

Smaller, faster, more free. Support of Perl-scripts (what can be very powerful tool in professional's hands). At startup loads modules and almost everything can be re-done by modifying these modules. Hard-to-familiarize with, as for me (but thats just me).

3\. WinTin

Forced me to download \~23Mb .Net Framework thing, alil buggish, prints strange symbols on the screen what messes with triggers (i think it can be fixed somewhere in its menus). From first glance good internal language. "Script explorer" feature rocks. 

4\. Zmud

Paradise for programmers <img src="/images/smilies/icon_e_smile.svg" alt=":)" title=":)" width="15" height="15" class="smiley nozoom"> Bigger than others, loads slower, blinks and resizes its window before starts, written in Delphi (booo!). Alot of good features and stuff like automapper, status windows etc. Shareware, 30$.

Refused to run on next day. Cant even see it in Process list - dont know if its Zmud's or our 'favorite' OS' 'feature' <img src="/images/smilies/icon_e_smile.svg" alt=":)" title=":)" width="15" height="15" class="smiley nozoom">

5\. RoA client

A mystery. People say its 'another good client', but i didnt felt it in my case yet. Its still installed, but i getting tired of solving mysteries <img src="/images/smilies/icon_e_smile.svg" alt=":)" title=":)" width="15" height="15" class="smiley nozoom">

6\. MUSH Client

A client i fell in love with. Support of many scripting languages like JS, VBS, Perl, Python, PHP (!) and something enigmatic called LUA, but also rich internal language. Shareware, 20$ (afair). Written in C++ (respect!), therefore fast. Plug-ins supported. Didnt found any negative side yet.

7\. TiniFugue

\*nix-type client, as i'v been told. Tho i found .msi compilation for our 'favorite' OS, it still runs in command\_prompt-like mode. Wont use it, either its good or bad idea :-/

Well, thats all for now. I would be happy to hear your opinion on these clients, their pro's and con's you have already encountered, what do you like and what you dont and mostly important - why. Advanced technical details very appreciated. <img src="/images/smilies/icon_e_smile.svg" alt=":)" title=":)" width="15" height="15" class="smiley nozoom">

PS (for happy MUSH-client users):

Can you guys please post here or email/mudmail/tell/etc to me an example of triggers, that: 

a) Enters char\_name in respond on "By what name do you wish to be known?"

b) Enters password on "Password:"

c) Sends Carriage\_return on "\*\*\* Press return"

Yes, i know there is Auto-login option, it works fine, but only with a) and b), i just dont want to let stupid program do important things instead of me (or my hand-and-brain-written triggers). Yes, i know its a shame for a person who declared himself to be limited by programming language not to be able to make a simple trigger, but i give up - i tried ANY and ALL possible and impossible combinations of trigger\_patterns, regular\_expression and options - its just dont work.

I even studied JMC-logs in hexadecimal mode, trying to see what the server sends to me in that prompt, because somebody told me that server writes something invisible in Telnet session for some purpose, unknown to me.

Strangely, triggers i wrote work fine with my home-compiled CircleMUD 3.1, but not with SlothMUD ...

Well, enough of complaining. I rely on you, the rest is on me. <img src="/images/smilies/icon_e_smile.svg" alt=":)" title=":)" width="15" height="15" class="smiley nozoom">

PPS. Sorry for poor english (i tried my best) and sorry if i posted it in wrong place (i suspect it should be placed in "Client scripts", but i hope here i have more chances to get response). Thanx in advance.

</div>

<div class="post" data-post-id="3826" data-author="Avatar" data-date="2005-01-19T02:00:59+00:00" data-subject="">

There's a little bit of a learning curve when you start to use Mushclient, but once you get a little practice it gets much easier.

To send a blank \<enter\>, you want to send \\r 

The trick is where you want to send it. If you go build your trigger, one of the options (below the color selection drop-down box) is a selection that's called "send to:". You want to select: World(immediate)

Also, when you double click on the trigger it shows in the interface there the number of times this trigger has been matched. So you can create one and if you're having trouble you can sometimes tell if the trigger isn't matching for some reason or if the effect of the trigger isn't working the way you expect it to.

Charles

</div>

<div class="post" data-post-id="3828" data-author="Strago" data-date="2005-01-19T04:48:01+00:00" data-subject="">

I am using 2 right now, tintin++ from work (majority of my mud time) and Zmud at home. After the initial month of using Zmud I turned the automapper off. Once you get your head into the mud and out of graphics you are all set.

I like Zmud because it feel fast, where tt++ has some bad scrolling. Zmud is also easier to interactively program triggers for.

Both have awful scripting langauge syntax.

I guess I am still searching for that perfect client. I am leaning more and more away from zmud and towards TT++ because I can use TT++ from anywhere buy sshing inio my home server.

</div>

<div class="post" data-post-id="3831" data-author="Weasel" data-date="2005-01-19T11:02:55+00:00" data-subject="">

Been using MUSHclient for a couple of years and will certainly be sticking with it. Awesome no-holds-barred client.

</div>

<div class="post" data-post-id="3937" data-author="Nascosto" data-date="2005-01-25T04:49:00+00:00" data-subject="">

\>\> Refused to run on next day. Cant even see it in Process list - dont know if its Zmud's or our 'favorite' OS' 'feature' Smile 

This happened too me when I disabled the LicCtrl service from starting - Zmud won't even start in that case.

</div>
