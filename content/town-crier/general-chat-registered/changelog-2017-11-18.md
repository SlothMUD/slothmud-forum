---
title: "Changelog 2017-11-18"
topic_id: 4801
author: "*teker*"
date: 2017-11-19T03:36:28+00:00
last_activity: 2017-11-20T20:29:13+00:00
last_author: "*Breeze*"
sticky: false
locked: false
post_count: 9
---

<div class="post" data-post-id="38489" data-author="*teker*" data-date="2017-11-19T03:36:28+00:00" data-subject="Changelog 2017-11-18">

I've started rewriting some of the spells to make them more friendly when bad arguments are provided. For example:

\- Hermetic resonance rewritten to make sure a valid spell name is entered. Also found rebirth exploit and removed it.

\- Supplication rewritten to make sure a valid supplication type or name was entered.

\- Summon undead rewritten to make sure the summon creature is valid. I also modified it so that if the player gives a number of undead that is too big, the parsing function figures it out and reduces the number. So if I try to summon 3 and I can only summon 2, it summons the 2, charges only the mana required for the 2 and spits out a message that I can't handle any more than 2. It's also smarter with how the total mana cost is calculated - the cost still increases as the number of undead increases but if the total ends up being too much, the spell fails and no mana is deducted. I feel like this breaks realism in some way (like I should still charge mana for attempting) but in the end it's just a better user experience. Also scrolls/wands/charms that cast this spell would still cost mana per undead and that should not be the case any longer.

\- Clan keys should no longer work when non-clan members attempt to use them. Currently Legends is the only clan where I have set the key so we'll have a limited test before we move forward. I ended up rewriting most of the open/close/lock/unlock code for doors so I could create a proc intercept for those commands. There was a bug filed against the skeleton key in the Tower in Grv - I'm curious if the skeleton key works better now.

I'm open to suggestions on other spells that need rewritten to handle bad arguments better.

</div>

<div class="post" data-post-id="38491" data-author="Gorka" data-date="2017-11-19T10:54:58+00:00" data-subject="Re: Changelog 2017-11-18">

Teker, on supplicants one of the most valuable things you could do is actually list what the supplicants do. Recently Sochi told me I can "order banshee wail." I had no idea about this, yet that information totally changed my game as it allowed me to kill some mobs in some dangerous areas. I've never been into pets and I have zero idea what most pets do outside of peri, nightmare and eudaemon. Imagine what it's like for new players... how do they know the commands the pets can do? Is it even documented? Maybe the pet template could have a help command so the player can "order pet list abilities." This could be in play for awakens/supplicants and summons.

</div>

<div class="post" data-post-id="38492" data-author="*Breeze*" data-date="2017-11-19T22:11:42+00:00" data-subject="Re: Changelog 2017-11-18">

If I read the mudl commands for the various supplicants and tell you the commands, are you willing to do the help file for it?

</div>

<div class="post" data-post-id="38493" data-author="Gorka" data-date="2017-11-20T05:00:29+00:00" data-subject="Re: Changelog 2017-11-18">

Sure, I'll give it a crack. First one will be a learning curve.

</div>

<div class="post" data-post-id="38494" data-author="*Breeze*" data-date="2017-11-20T18:13:02+00:00" data-subject="Re: Changelog 2017-11-18">

first set of stuffs... its easier if someone actually summons them so i can check them before they auto-poof.

we should probably add juju etc to the list of stuff to document.

stuff between ( ) is aliases of the same command.

nightmare -- order mare trouble XXXXX

djinn ---- order djinn [blow;(seize grab whirlwind capture catch);(drop free release)] XXXXXXXX

chan chu -- kiss chan

thunderbird ------ flyto enter say tell order board climb

brownie -- rescue XXXXX; squirm [helps you squirm]

</div>

<div class="post" data-post-id="38495" data-author="Gorka" data-date="2017-11-20T18:56:05+00:00" data-subject="Re: Changelog 2017-11-18">

I had no idea a djinn "webs." <img src="/images/smilies/icon_lol.svg" alt=":lol:" title=":lol:" width="15" height="15" class="smiley nozoom"> 

"kiss chan" appears to do nothing. It might be bugged.

</div>

<div class="post" data-post-id="38496" data-author="*Breeze*" data-date="2017-11-20T19:04:08+00:00" data-subject="Re: Changelog 2017-11-18">

try kiss chu 

or just kiss

no idea.

</div>

<div class="post" data-post-id="38497" data-author="Gorka" data-date="2017-11-20T19:26:48+00:00" data-subject="Re: Changelog 2017-11-18">

Krom answers your request!

A chan chu appears in a flash of rainbow light!

A chan chu starts following you.

\<1356hp 274ma 136mv 2702840787xp -9.5ac -%\>

kiss;kiss chan;kiss chu

A chan chu nimbly hops out of the way... you pervert.

\<1356hp 275ma 138mv 2702840787xp -9.5ac -%\>

A chan chu nimbly hops out of the way... you pervert.

\<1356hp 275ma 138mv 2702840787xp -9.5ac -%\>

A chan chu nimbly hops out of the way... you pervert.

\<1356hp 276ma 139mv 2702840787xp -9.5ac -%\>

autoloot off

Autoloot mode is now off.

\<1356hp 286ma 154mv 2702840787xp -9.5ac -%\>

dg wight;str

war

warcry LEEEEEROOOY JEEEENKINS!!!

deathgrip wight;release

You yell 'LEEEEEROOOY JEEEENKINS!!!'

\<1356hp 289ma 159mv 2702840787xp -9.5ac -%\>

A wight prison guard hates your guts!

You can taste the impending victory!

You circle around a wight prison guard and expertly put it in a deathgrip.

@@

\<1496hp 289ma 139mv 2702850687xp -9.5ac 50%\>

With a mighty effort, you shake off your exhaustion!

You release a wight prison guard from your grip.

\<1496hp 290ma 125mv 2702850687xp -9.5ac 50%\>

You land a powerful strike into a wight prison guard's side.

strike

@@

\<1496hp 290ma 125mv 2702865871xp -9.5ac 31%\>

Impossible to use this so soon after a successful second wind!!!

\<1496hp 291ma 126mv 2702865871xp -9.5ac 31%\>

You deal a critical blow to one of a wight prison guard's vital organs.

You viciously massacre a wight prison guard with your hit.

A wight prison guard misses you with its hit.

A wight prison guard looks shocked as it cuts itself on your petrified armor!

A wight prison guard massacres you to small fragments with its slash.

A wight prison guard misses you with its hit.

A wight prison guard massacres you to small fragments with its slash.

A wight prison guard massacres you to small fragments with its slash.

A wight prison guard misses you with its hit.

You deal a critical blow to one of a wight prison guard's vital organs.

You viciously massacre a wight prison guard with your hit.

You brutally massacre a wight prison guard with your hit.

A wight prison guard misses a kick at your groin, you breathe lighter now.

\<1425hp 292ma 128mv 2702883279xp -9.5ac 8%\>

\<1425hp 294ma 131mv 2702883279xp -9.5ac 8%\>

You strike a wight prison guard right in its kidney!

A wight prison guard looks shocked as it sees your fist embedded in its abdomen, then collapses.

A wight prison guard is dead! R.I.P.

You gain 566570 bonus experience!

Total exp for kill is 1603501.

\-------------

MOB : undead wight guard man axe	LVL : 40	AREA : Shadow Keep	XP : 1603501

\-------------

\|

Your blood freezes as you hear a wight prison guard's death cry.

\<1356hp 294ma 131mv 2705054890xp -9.5ac -%\>

kiss;kiss chan;kiss chu

A chan chu nimbly hops out of the way... you pervert.

\<1356hp 299ma 137mv 2705054890xp -9.5ac -%\>

A chan chu nimbly hops out of the way... you pervert.

\<1356hp 299ma 137mv 2705054890xp -9.5ac -%\>

A chan chu nimbly hops out of the way... you pervert.

\<1356hp 299ma 139mv 2705054890xp -9.5ac -%\>

rest

You sit down and rest your tired bones.

</div>

<div class="post" data-post-id="38498" data-author="*Breeze*" data-date="2017-11-20T20:29:13+00:00" data-subject="Re: Changelog 2017-11-18">

yup. thats exactly what its supposed to do.

</div>
