---
title: "interrupt command"
topic_id: 685
author: "dezakin"
date: 2004-12-17T23:11:08+00:00
last_activity: 2004-12-19T18:32:35+00:00
last_author: "Corwin"
sticky: false
locked: false
post_count: 7
---

<div class="post" data-post-id="3395" data-author="dezakin" data-date="2004-12-17T23:11:08+00:00" data-subject="interrupt command">

How bout a command that interrupts all the commands on the que and dumps them... for instance:

\#8 kick

hmm crap hp is getting low

interrupt;recite recall

</div>

<div class="post" data-post-id="3398" data-author="madmax" data-date="2004-12-18T00:51:39+00:00" data-subject="">

I think you are more talking about a client command. The mud dosent recognize #8, only kick.

Madmax

</div>

<div class="post" data-post-id="3399" data-author="blackmore" data-date="2004-12-18T01:36:36+00:00" data-subject="">

This would mostly depend on how your client is written whether it would even work on the client or not, but most likely it won't.

If you type #8 kick, meaning kick 8 times, your client sends the command 'kick' 8 times. If you then type interrupt, it's too late - you've already sent 8 kicks to the server, it's just waiting for the commands to make it through. From that point, it's too late to stop anything because it's all in the server's queue waiting for its turn to be processed.

From the server, there would have to be some command that takes precedence over all other commands, no matter how many have been queued up, and I'm betting this is much harder than you would imagine, if not completely impossible.

</div>

<div class="post" data-post-id="3400" data-author="Strago" data-date="2004-12-18T02:30:50+00:00" data-subject="">

It might be a good idea for you to set up a triiger on the client to do the following.

Command: getmykickon

\- Send first kick command

\- set variable kickvar to true

\- Start a tick timer

\- When timer hits the time between kicks and kickvar is true send the next kick

Commad: stopkicking

\- stop tick timer and set kickvar false

so you could type

\>getmykickon

\>stopkicking

\>next command

You could then modify this to accept an arguement for the max number of times to kick.

</div>

<div class="post" data-post-id="3401" data-author="guest" data-date="2004-12-18T03:33:51+00:00" data-subject="">

how lazy to write #8 kick instead of paying attention? the reward of laziness should be appropriate: death. Not whining of mud to be changed to allow for such stupidity.

</div>

<div class="post" data-post-id="3439" data-author="dezakin" data-date="2004-12-19T18:14:30+00:00" data-subject="">

Look, of course people dont now type #8 kick and pray.

often they'll have kicker scripts, and autoblaster scripts, but these can incur some delay... as much as a round of combat.

A round of combat is often too late.

And it shouldnt be that hard to write an interrupt command on the server.

</div>

<div class="post" data-post-id="3440" data-author="Corwin" data-date="2004-12-19T18:32:35+00:00" data-subject="">

yeah, if you cannot stand the heat get outta the kitchen. in other words if you cannot q up 8 kicks dont. i have an auto kicker for sure, i do play a warrior after all. but you have to use your head, both when you write the scripts and when you use them. if you stack 8 kicks you better be ready for something bad to happen. also if your kicking a monster, it shouldn't be able to kill you in 8 rounds of combat. and if you cannot last 8 rounds of combat...well, you should find a diferent skill or spell, cause kick gets you no place fast.

</div>
