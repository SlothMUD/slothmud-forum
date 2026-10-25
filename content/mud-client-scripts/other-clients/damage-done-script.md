---
title: "Damage Done Script"
topic_id: 2360
author: "Thraxas"
date: 2007-02-18T22:46:50+00:00
last_activity: 2008-04-10T23:33:15+00:00
last_author: "jezer"
sticky: false
locked: false
post_count: 20
---

<div class="post" data-post-id="16993" data-author="Thraxas" data-date="2007-02-18T22:46:50+00:00">

Up front I'll say I found creating this more fun than the product will be useful.

No one seems to have posted many scripts for a while so I thought I would.

This is a little bit of scripting that I've created and works nicely to whine the actual and exact damage you do in each round of combat

It will accurately calculate the damage done by any anything you do that you get xp for

This includes weapon damage, spell damage, proc damage, chop damage, kicks, bashes, broadsides, flails, deathblows etc.

This does not include damage done by pets

This is inaccurate in last round of battle when mob may not have all the hp to lose that you damage does.

The basis of this script is that xp gained from damage done = mob level * actual damage done

Therefore you need to know mob level, this script works out this calc for all levels and sees which levels show damage as a whole number.

if a decimal is found on the damage done, this level is deemed wrong and discarded for the calcs in the next round, thereby it will iteratively work out the mobs level during combat.

Note: If a mob is level 40 then all whole divisors of 40 (20 10 8 5 4 2 1) could also be right to this method, for this reason I limit the script to looking at mob levels 20+

I've used it sucessfully in my client (AL Client) the bare bones are below and should be enough for you to reconstruct, they rely on you having your current xp in your prompt.

The effect is a whine somthing like:

Damage Report: [20]: 14 [30] 21

where the 20 and 30 are the possible levels the mob could be, this normally starts in round one at 3-5 levels after 3 rounds is reduced down to one, the mobs actual level. (the 14 and 21 are the damage done)

Let me know if you find useful or any additions I could make to it.

Thraxas

alias (triggered at start of fight) _fightstart:

#if (autodam = 1) {_gainreset}

Note: I have a load of other stuff in _fightstart this is only pertinent bit, autodam is a toggle variable to switch whole process on and off.

alias _gainreset:

#set gd[20] = 1;

#set gd[21] = 1;

... etc ...

#set gd[44] = 1;

#set gd[45] = 1

Note: I'd love to use a for loop here but my client dosen't support them

alias (triggered at prompt) _gainprom:

#set myxpprom = (myxp - myxplast)/1; 

Note: myxpprom is xp gain between this and last prompt, myxp is xp shown in prompt this round, myxplast is xp from prompt in previous round

#if (autodam = 1) 

{#set gdrep Damage Report: ;

  #if (myxp > myxplast) 

  {#if (gd[20] = 1) {_gaindam myxplast myxp 20};

   #if (gd[21] = 1) {_gaindam myxplast myxp 21};

... etc ...

   #if (gd[44] = 1) {_gaindam myxplast myxp 44};

   #if (gd[45] = 1) {_gaindam myxplast myxp 45};

  };

  #print $gdrep$

}

alias _gaindam:

#set num1 = %1;

#set num2 = %2;

#set lvl1 = %3;

#set dnum = num2 - num1;

#set dnumdiv = dnum / lvl1;

#set dnummul = dnumdiv * lvl1;

#set ddnum = dnum - dnummul;

#if (ddnum > 0) {#set gd[%3] = 0};

#else {

  #set ddam = dnumdiv;

  #strcat(gdrep," [");

  #strcat(gdrep,lvl1);

  #strcat(gdrep,"]: ");

  #strcat(gdrep,ddam)

}

Additional Notes: 

1. #strcat is a string concatenation function to build a string up with text variables

2. #print sends a string to my client as though its come from the mud

3. #set and #unset are to set variable values

4. #if #else well if you don't know I ain't going to teach you in this post

all other stuff here is standard stuff I think

</div>

<div class="post" data-post-id="17016" data-author="Avatar" data-date="2007-02-20T04:40:00+00:00">

Very nice.

I've had a more basic script performing a similar function, but I like how you determine and discard the unlikely mob levels.

Do you often heal yourself or others during fights?  

I haven't had much time online lately, but I'm interested in trying to implement this using VB script.  My skills aren't up to it yet, so it would be a learning experience.

</div>

<div class="post" data-post-id="17027" data-author="Thraxas" data-date="2007-02-20T18:38:18+00:00">

I've had a more basic script performing a similar function, but I like how you determine and discard the unlikely mob levels.

[/quote:zo4nf7zh]

its there in the script

#if (gd[x] = 1) {_gaindam myxplast myxp x}

is run for each level 20 - 42 where x is the possible mob level

At fight start gd[x] = 1 for every level so the _gaindam script will run for each level,

during each round the following is run for each level being tested:

#set dnum = num2 - num1; 

#set dnumdiv = dnum / lvl1; 

#set dnummul = dnumdiv * lvl1; 

#set ddnum = dnum - dnummul; 

#if (ddnum > 0) {#set gd[%3] = 0}

dnum = xp change in round

dnumdiv = the xp over possible mob level (i.e the possible damage done) note that as this is effectively a unix script the result is an integer i.e. no decimal point always rounded down.

dnummul = the reverse of this calculation this is done to test for a remainer on the division, if dnummul = dnum then there is no remainder.

The point of this is that is there is a remainder then then that cannot possibly be the mob level.

If there is a remainder i.e. ddnum > 0 then set gd[x] to 0, this means that next round this level will be ignored (see above >>> #if (gd[x] = 1) {_gaindam myxplast myxp x})

To labour the point take an example just testing levels 20-25:

in this way 100xp can be gained in round 1:

100/20 = 5 = whole number => level 20 is possible gd[20] stays at 1

100/21 = 4 plus a bit = not a whole number => level 21 is not possible gd[21] is now set to 0

same for lvls 22 23 24,

100/25 = 4 = whole number => level 25 is possible gd[25] stays at 1

the whine looks like Damage Report: [20] 5 [25] 4

in round 2 75 xp is gained:

75/20 = 3 plus a bit = not a whole number => level 20 is no longer possible gd[20] is set to 0

levels 21 - 24 are not tested as gd[21] etc now = 0

75/25 = 3 = whole number => level 25 is possible gd[25] stays at 1

the whine looks like Damage Report: [25] 3

in any subsequent round only lvl 25 is tested

I hope this helps.

Do you often heal yourself or others during fights?  

[/quote:zo4nf7zh]

no I normally run solo with juju pets and eudaemon supplimented with infusions.

</div>

<div class="post" data-post-id="23618" data-author="Assirian" data-date="2008-04-08T09:24:58+00:00">

<859 362 228 309540203>

You massacre a troll warrior to small fragments with your pound.

A troll warrior misses you with his rake.

A troll warrior rakes you very hard.

A troll warrior rakes you extremely hard.

A troll warrior massacres you to small fragments with his rake.

A troll warrior massacres you to small fragments with his rake.

You massacre a troll warrior to small fragments with your pound.

You massacre a troll warrior to small fragments with your pound.

A troll warrior wipes his boots in your face.

<758 362 228 309541485>

309541485-309540203=1485-0203=1282

the mob is about 36 lvl, so damage is ~ 36

but 3 massacres have to deal >= 60 dam!

What is wrong? :)

</div>

<div class="post" data-post-id="23619" data-author="jezer" data-date="2008-04-08T09:54:50+00:00">

the mob is about 36 lvl, so damage is ~ 36

but 3 massacres have to deal >= 60 dam!

What is wrong? :)[/quote:2fbh3xbf]

Whats wrong?!? The new changes to warrior class have made you over powered!  :twisted:

</div>

<div class="post" data-post-id="23620" data-author="Assirian" data-date="2008-04-08T10:23:15+00:00">

[quote:2rcfj09d] The new changes to warrior class have made you over powered![/quote:2rcfj09d]

this one is not wrong :)) this have to be happen.. 8\

</div>

<div class="post" data-post-id="23621" data-author="Thraxas" data-date="2008-04-08T11:21:08+00:00">

Whats wrong?

I believe changes were introduced in one of the last few reboots that introduce a random element into the xp calc tjis script is based on.

whY? no idea, but i'd speculate that either dam knowledge is about to be introduced as a skill, or dam is about to be (or has been) capped and THEYdidn't want us to know.

</div>

<div class="post" data-post-id="23622" data-author="*juggleblood*" data-date="2008-04-08T13:02:29+00:00">

I've never understood the long standing tradition on sloth of obscurring game mechanics. I would guess that this was the purpose in randomizing combat xp.

</div>

<div class="post" data-post-id="23623" data-author="jezer" data-date="2008-04-08T13:16:15+00:00">

I've never understood the long standing tradition on sloth of obscurring game mechanics. I would guess that this was the purpose in randomizing combat xp.[/quote:2p7oh66w]

^gazillion

Last time I said something like this, some imm said, well... ask your question... which I did... only to get an obscured answer.  :roll: 

Freedom of Information all the way!

</div>

<div class="post" data-post-id="23624" data-author="Avatar" data-date="2008-04-08T18:32:53+00:00">

I noticed that change also, it's too bad.  I had a lot of fun watching the fight xps, especially during groups.  It made it more interesting, as a warrior who wasn't usually the tank, to give me something to watch and something to do.  I definitely used the warrior skills (berserk, bash, trip, broadside, stomp) more often when I was paying attention to the xps.

It's unfortunate that we'd purposefully break something that made groups more fun.

Just FYI, I've been offline again but only because my ISP is unreliable this month.  I use a wireless point-to-point connection, but it's based on 900 meg equipment.  Apparently someone has installed similar equipment somewhere between myself and the ISP site which is flooding the ether with 900 meg signals.  The ISP is coming out this weekend to help see what we can do to get me a signal.

Charles

</div>

<div class="post" data-post-id="23626" data-author="Autolycos" data-date="2008-04-08T19:36:44+00:00">

I've never understood the long standing tradition on sloth of obscurring game mechanics. I would guess that this was the purpose in randomizing combat xp.[/quote:2a6m1ljg]

Don't forget the tradition of exsanguinating all the fun out too..

</div>

<div class="post" data-post-id="23627" data-author="Medios" data-date="2008-04-08T21:00:51+00:00">

At least I can take that spammy bull crap out of my prompt now.  I have no idea why the xp was changed.  My first guess is because kick is overpowered.

</div>

<div class="post" data-post-id="23628" data-author="Autolycos" data-date="2008-04-08T21:56:33+00:00">

At least I can take that spammy bull crap out of my prompt now.  I have no idea why the xp was changed.  My first guess is because kick is overpowered.[/quote:gugxl8sq]

lmfao

</div>

<div class="post" data-post-id="23632" data-author="*juggleblood*" data-date="2008-04-09T02:48:07+00:00">

Someone pointed this out for me and I thought I'd share it.

When people started using the damage calculator script, some long standing bugs became evident. Solution? Nerf the damage calculator script. Someone was clearly thinking outside the box on that one.

</div>

<div class="post" data-post-id="23633" data-author="jezer" data-date="2008-04-09T03:07:58+00:00">

[img:2762ne8h]http://www.orbitcast.com/archives/head-in-the-sand.jpg[/img:2762ne8h]

What problem? Where?  :twisted:

</div>

<div class="post" data-post-id="23635" data-author="Yasik2" data-date="2008-04-09T05:40:13+00:00">

[img:1cc23wzx]http://yasik.kiev.ua/4chan/Explanation_I_Demand.jpg[/img:1cc23wzx]

</div>

<div class="post" data-post-id="23648" data-author="Mace" data-date="2008-04-10T12:53:14+00:00">

I guess this change is for the best.

I mean, what kind of game (Final Fantasy) would be successful (World of Warcraft) where you could see your damage as a number?  (Dungeons and Dragons)

</div>

<div class="post" data-post-id="23653" data-author="Thraxas" data-date="2008-04-10T18:07:28+00:00">

Lets think about the profile of the typical mud player:

a bit geeky, likes to write scripts, triggers actions, likes to unpick how the mud works and analyse the intricacies to death (just think out about some of the discussions on the exact formula for stat rolling we used to have), oh and mostly obsessive.

Admittedly not all of us fit all of this profile, but I'd bet most of us are close to it .... now why would someone fitting that profile gain any pleasure, satisfaction, morbid enjoyment, facination, be interested in seeing the exact damage for each hit reported on screen in real time? 

Nice one to add to the tick list:

Player Satisfaction: Debuffed

</div>

<div class="post" data-post-id="23654" data-author="*juggleblood*" data-date="2008-04-10T18:49:45+00:00">

I miss Splork.

</div>

<div class="post" data-post-id="23657" data-author="jezer" data-date="2008-04-10T23:33:15+00:00">

Lets think about the profile of the typical mud player:

a bit geeky, likes to write scripts, triggers actions, likes to unpick how the mud works and analyse the intricacies to death (just think out about some of the discussions on the exact formula for stat rolling we used to have), oh and mostly obsessive.

Admittedly not all of us fit all of this profile, but I'd bet most of us are close to it .... now why would someone fitting that profile gain any pleasure, satisfaction, morbid enjoyment, facination, be interested in seeing the exact damage for each hit reported on screen in real time? 

Nice one to add to the tick list:

Player Satisfaction: Debuffed[/quote:1f0fo9yg]

Good post... 

So we like numb3rs... that's just the way we are! :twisted: 

I for one, can remember many, many times more the amounts on xp mobs, than I can any room description. Numbers rock! Logic and Order rules! And, and... and Bring back the coliseum!  :evil:

</div>
