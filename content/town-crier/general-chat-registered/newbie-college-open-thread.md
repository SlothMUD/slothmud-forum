---
title: "Newbie College Open Thread"
topic_id: 4577
author: "*juggleblood*"
date: 2016-01-16T17:25:30+00:00
last_activity: 2016-01-17T20:54:25+00:00
last_author: "*juggleblood*"
sticky: false
locked: false
post_count: 9
---

<div class="post" data-post-id="36482" data-author="*juggleblood*" data-date="2016-01-16T17:25:30+00:00">

Since the other thread is an announcement which players can't respond to, I've opened this thread for discussion.

Regarding some issues that have been raised:

*The color code problems are fixed.

*The trainer procs are working, but I am currently working on a proc which addresses the problem of when a newbie accepts training and then quits game.

*Considering adjusting doors so that trainer doesn't autoclose door to hall behind you when you enter.

*Trainers need a message for when player enters but another player is currently training.

*Splorks temple is currently broken after the move. Working with coders to get it back working.

*Will reduce # of scorpions required for win and increase scorpion spawning.

*The catacomb rooms below the school contain some helpful class information, but it is not complete. Accepting player submissions. See the bard information as a template.

*Grotley message corrected to 500 gold per goblin.

</div>

<div class="post" data-post-id="36484" data-author="*juggleblood*" data-date="2016-01-16T17:46:50+00:00">

*Regarding newbies appearing in BH after graveyard, I think I'll leave it like that, but I've added  messages teaching about hometown command when they appear at west gate:

You have appeared in the Town of Bal Harbor on Thordfalan.

To return to your hometown, use the hometown command.

</div>

<div class="post" data-post-id="36485" data-author="Teron" data-date="2016-01-16T18:19:10+00:00">

Mention that a newbie will get some prize on 100% completion and give it to them after he finishes all trainers in any order. This way, he knows he's done and can leave the college.

</div>

<div class="post" data-post-id="36488" data-author="*juggleblood*" data-date="2016-01-16T18:33:46+00:00">

*Trainer vars should adjust accordingly when trainee quits now.

Will add procs to deal with newbie garbage on floor.

Will get to adjusting the door protocols in a bit.

</div>

<div class="post" data-post-id="36491" data-author="Dragoth" data-date="2016-01-16T19:10:19+00:00">

1) Problem: When i connect to the game for the first time there is no indication what continent a newbie should start at. 

Solution:Adding a hint at character creation would be nice

Edit: I must be blind, completely missed it when i started a newbie, but the message is there! Or maybe putting it below the choices would be more obvious.

That's how it is now:

What is your sex (M/F) ? male

You now must select your hometown.

If you don't know, pick 1. Newbatia.

Here are the hometown choices:

   Town Name:                 On Continent:

------------------------------------------------------------------------------

1. Newbatia                   Valkyre  

2. Aisholm                    Thule       

3. Bal Harbor                 Thordfalan   

4. Settlestone                Niebelung     

Enter your choice: 

Proposed:

You now must select your hometown.

Here are the hometown choices:

   Town Name:                 On Continent:

------------------------------------------------------------------------------

1. Newbatia                   Valkyre  

2. Aisholm                    Thule       

3. Bal Harbor                 Thordfalan   

4. Settlestone                Niebelung     

Enter your choice: 

(If you don't know what to pick, select 1 for Newbatia.)

------

2) Problem: When you enter the game at newbatia, there is no indication how to even get to newbie school, you start at the gate and can completely miss the school if you dont go up. 

Solution:Make new character start at A glowing transportation chamber where the sign is, not at South Gate as it is now.

3) Problem: being mortally wounded as a newbie, i got wounded at trifids and kept lying there without any messages to tell me what to do next, this could get boring fast, adding a message on choices the first time a person goes below -1 hp would be helpful, it could also be a good time to teach newbs about raise dead and getting healed while mortally wounded.

*Edit*

Found the death sherpa which teaches the exact thing. Dying before getting to sherpa should get addressed in the same fashion/ or maybe dying before getting to sherpa should get your raised. 

-----------------

4)

A halfling gardener says 'The trifids are destroying the roses!'

A halfling gardener says 'Do you think you could eliminate them for me?'

ask gardener about trifid

You ask a halfling gardener about 'trifid'.

A halfling gardener tells you 'Sorry, I don't know anything about that.'

<27hp 70ma 129mv>

ask gardener about quest

You ask a halfling gardener about 'quest'.

A halfling gardener tells you 'Sorry, I don't know anything about that.'

-------------------------

So I killed trifids but he just kept repeating the same thing over and over again.

Imho this would be a good time to teach newbs about how undertake and ask about quest commands work, 

Putting a sign at Halfling gardener that explains these commands and a small quest that rewards a tri token for a trifid corpse wouldnt be out of place i think..

-------------

5)

A Medical Station

   A small room on the interior of the building is equipped with cots,

splints, bandages and some alchemical supplies.  One corner of the room has

glass cabinets full of different-colored potion vials.  The main corridor

lies west through a door-less half-arch.

Exits: West  

Educational posters detail the affects of some common potions.

A young elven female is sorting through her alchemical supplies.

To see items for sale, type list.

<27hp 70ma 119mv>

l poster

You see nothing special..

<27hp 70ma 118mv>

l potions

The poster details some widely available potions.

Gold Potion  A very minor potion of health

Red Potion   A potion of armor

Purple Potion   A potion of remove poison

I think people are more likely to use look poster than potions.

</div>

<div class="post" data-post-id="36496" data-author="*Splork*" data-date="2016-01-17T13:12:00+00:00">

> **Quote:**
> You now must select your hometown.
> 
> If you don't know, pick 1. Newbatia.
> 
> Here are the hometown choices:
> 
> Town Name: On Continent:
> 
> ------------------------------------------------------------------------------
> 
> 1. Newbatia Valkyre 
> 
> 2. Aisholm Thule 
> 
> 3. Bal Harbor Thordfalan 
> 
> 4. Settlestone Niebelung 
> 
> Enter your choice:

Nods, you just missed it but we could be a bit more clearer by using the method JB just utilized with the new newbie zone of changing the color of key terms or messages.

We do list Newbatia as the #1 option because we feel those people that might not know or missed the message are more apt to choose the first option( we have no stats to prove this ).

Also, if send a question mark here, you will be given more information and it is further stated

> **Quote:**
> If you aren't familiar with Sloth Mud, you should pick Newbatia as your home.
> 
> Newbatia is in an area targeted at new players.

There was a time where we considered only allowing players to choose VK but we quickly decided against that. Experienced levels can level a newbie up quite quickly on the other continents...

Also, we should do a better job of letting a new player know that they can enter ? at any choice and get further information by restating it often or emphasizing that phrase upon initial login, or both!

</div>

<div class="post" data-post-id="36501" data-author="*juggleblood*" data-date="2016-01-17T16:14:29+00:00">

Added keywords to the poster at the nursing station. 

Will flesh out trifids / gardener.

Will work on a proc that checks for morted players throughout the school (already exists in training room) and maybe drags the nurse to them or drags them to nurse.

However, we probably do need something for when newbies mort outside the school. I agree that if you're brand new, being morted is confusing and seems stupid. Perhaps a message encouraging them to quit out.

</div>

<div class="post" data-post-id="36503" data-author="*juggleblood*" data-date="2016-01-17T16:42:24+00:00">

*Doors fixed to no longer shut behind you when you enter the room with trainer, but there's still some shutting and opening involved when you engage in/complete training.

*Feral kobold xp in wand training room reduced so as not to cap the player.

*Added (look sign) in bright green to the sign description at south gate of vk

A large sign has information for newbies. (look sign)

</div>

<div class="post" data-post-id="36504" data-author="*juggleblood*" data-date="2016-01-17T20:54:25+00:00">

*Reduced scorpion count to 5 and made sure plenty spawn. Trainer cures poisoned player.

</div>
