---
title: "One question about Undeads"
topic_id: 1417
author: "Gnu"
date: 2005-08-20T06:54:15+00:00
last_activity: 2005-08-20T17:33:16+00:00
last_author: "Gnu"
sticky: false
locked: false
post_count: 5
---

<div class="post" data-post-id="8355" data-author="Gnu" data-date="2005-08-20T06:54:15+00:00">

I have some questions about undeads that one can summon and animate. I have summoned 

phantom. So here is the log of my fight with him.

*****************************************************************************************************

Your blow passes right through a phantom with no effect!

A phantom misses you with its claw.

A phantom misses you with its claw.

A phantom massacres you to small fragments with its claw.

Your blow passes right through a phantom with no effect!

<883hp 368ma 218mv>

score

Pendalf sHmeNdAlF (IcQ # 157142609)  (level: 40)

Your levels:  Ba: 40 Cl: 40 Ma: 40 Ne: 40 Av: 25 

You are 48 years and 5 months old.

You are a citizen of Bal Harbor.

You are a devout worshipper of Enea.

You are an outstanding member of your community.

You have (886/933+41) hit, (370/547+33) mana and (220/230+28) movement points.

Your armor class is -11.0.

You have +5 to hit and +3 on damage.       

You have 44632 gold coins.

You have six hundred and seventy drachma.

You have 70212319 unused experience points.

You have been playing for 103 days and 11 hours.

Str: 15 / 0, Int: 18, Wis: 18, Dex: 18, Con: 17

You are fighting a phantom.

You are affected by the following spells:

   Blindness                                             <---------------------  !!!!!!!!!!!!!!!!!!!!                

   Detect Invisible                 

   Infravision                      

   Darksight                        

   Iron Skin                        

   Stamina                          

   Strength                         

   Vitality                         

<886hp 370ma 220mv>

Your blow passes right through a phantom with no effect!

A phantom misses you with its claw.

A phantom misses you with its claw.

A phantom misses you with its claw.

*****************************************************************************************************

As we can see, I was blinded, but still could see everything, moreover, phantom's blindness

removes only 1 to-hit instead of 3 from regular blind. And of course, phantom's blindness does 

not stack with regular blind. So, here is a question. Is everything ok with phantoms? Or may 

be I missed anything?

On the one hand, it is nice to have (-1) to-hit on mob from the very beginning of fight, on the other 

hand, it concells any possibility to use the full power of blindness. It's is also bad to have blinded 

mob, which can see.

</div>

<div class="post" data-post-id="8356" data-author="13" data-date="2005-08-20T10:23:27+00:00">

agree.

</div>

<div class="post" data-post-id="8357" data-author="kjartan" data-date="2005-08-20T12:23:48+00:00">

I think the problem here is that the phantom's messages were broken.  The message is "A phantom billows cloudy white haze around you, making it difficult to see".  So, it's not supposed to be real blindness.  I fixed the messages.

The other problem is that this effect blocks the 'blindness' spell.  I have fixed that in the code, in next crash or reboot; then a 'blindness' spell will just act as normal (but it still won't stack, it will just replace the phantom blindness with normal blindness).

</div>

<div class="post" data-post-id="8358" data-author="13" data-date="2005-08-20T14:56:54+00:00">

Hot dog :)

</div>

<div class="post" data-post-id="8359" data-author="Gnu" data-date="2005-08-20T17:33:16+00:00">

Thanx, Kj!

</div>
