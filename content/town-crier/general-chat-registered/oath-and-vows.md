---
title: "Oath and vows"
topic_id: 1839
author: "Mike"
date: 2006-04-08T15:20:37+00:00
last_activity: 2006-06-21T16:13:01+00:00
last_author: "kjartan"
sticky: false
locked: false
post_count: 76
---

<div class="post" data-post-id="12013" data-author="Mike" data-date="2006-04-08T15:20:37+00:00">

Not sure if it is a bug, but it looks strange to me. 

<1013hp 38ma 99mv +5>

You swear a mighty oath of victory over an outpost guard!

<1170hp 38ma 99mv +5>

An outpost guard misses you with his hit.

An outpost guard misses you with his hit.

An outpost guard misses you with his slash.

An outpost guard misses you with his slash.

An outpost guard misses you with his rake.

Rodek massacres an outpost guard to small fragments with his slash.

Rodek massacres an outpost guard to small fragments with his slash.

You massacre an outpost guard to small fragments with your pierce.

You massacre an outpost guard to small fragments with your pierce.

An outpost guard disengages himself, and attacks Rodek![/color:2mrnp4fg]

You've broken your oath of victory! [/color:2mrnp4fg]

It`s not a big deal anyway, but broke my reputation because mob disengage is a bit sucky.  :twisted:

</div>

<div class="post" data-post-id="12014" data-author="brady" data-date="2006-04-08T16:18:22+00:00">

eww look, it's Nelson...sorry to hear about your brother.  :x

</div>

<div class="post" data-post-id="12016" data-author="Rajil" data-date="2006-04-08T18:17:18+00:00">

I'm guessing Oaths no longer crashes the mud?

</div>

<div class="post" data-post-id="12017" data-author="kjartan" data-date="2006-04-08T18:36:57+00:00">

Yeah, it's safe now.  And I will need to fix that disengage thing.  Probably if the mob flees that will also break the oath, need to look at that too.

</div>

<div class="post" data-post-id="12018" data-author="Mike" data-date="2006-04-08T20:43:11+00:00">

You swear a mighty oath of victory over Lrogg!

<946hp 173ma 212mv +9>

Krok swears a mighty oath of victory in this battle!

<948hp 174ma 213mv +9>

Guinex massacres Lrogg to small fragments with his slice.

Krok massacres Lrogg to small fragments with her pierce.

Edd pierces Lrogg extremely hard.

You skillfully parry the attack of Lrogg.

Lrogg misses Guinex with its bite.

Lrogg misses Krok with its whip.

Lrogg misses you with its sting.

Guinex massacres Lrogg to small fragments with his slice.

Guinex massacres Lrogg to small fragments with his slice.

Guinex massacres Lrogg to small fragments with his slice.

You massacre Lrogg to small fragments with your pierce.

You massacre Lrogg to small fragments with your pierce.

Krok massacres Lrogg to small fragments with her pierce.

Krok massacres Lrogg to small fragments with her pierce.

Krok massacres Lrogg to small fragments with her pierce.

Edd pierces Lrogg very hard.

Lrogg breathes, filling the room with a torrent of flames!

You've broken your oath of victory![/color:12dyup65]

Lrogg misses Guinex with its bite.

Guinex's spectral shield drains power from the spell!

You are roasted in the inferno!

You resist most of the damage...

Is it the same thing with disengage or some proc on mob that makes same effect?  :)

</div>

<div class="post" data-post-id="12019" data-author="kjartan" data-date="2006-04-08T20:46:51+00:00">

I can't say I know what happened there.  I'll look into it.  At some point when we have the bugs all out of the oaths, we'll have an amnesty where we forgive everybody their broken oaths.

</div>

<div class="post" data-post-id="12020" data-author="Mike" data-date="2006-04-09T05:48:52+00:00">

Probably if the mob flees that will also break the oath, need to look at that too.[/quote:2mno7b7y]

Ygol the Arch-Lich recoils as Qa's weapon surges with a life of its own!

Ygol the Arch-Lich panics, and attempts to flee.

Ygol the Arch-Lich leaves down.

You've broken your oath of victory!

</div>

<div class="post" data-post-id="12026" data-author="Vixn" data-date="2006-04-09T16:30:19+00:00">

Somebody stop Mike. His only target is to disconsider the idea of 'oaths and vows'. Thanks.

</div>

<div class="post" data-post-id="12029" data-author="kjartan" data-date="2006-04-09T21:13:28+00:00">

The flee and disengage issues should be fixed after the next crash or reboot.  I don't understand what happened with the dragon - if you see that again (after reboot), please let me know.

</div>

<div class="post" data-post-id="12041" data-author="Rajil" data-date="2006-04-10T14:06:03+00:00">

Another one...

[quote:3bwrset1]You massacre a twisted man to small fragments with your hit.

A twisted man is mortally wounded, and will die soon, if not aided.

You've broken your oath of victory!

[/quote:3bwrset1]

</div>

<div class="post" data-post-id="12042" data-author="kjartan" data-date="2006-04-10T15:49:49+00:00">

Ok, I'll fix that, fix will go in tomorrow.

I am working on more oaths; probably at least one new one will go in this week and I have two more planned after that.  I think I am going to split the oath skill into one skill per oath (so what used to be "oaths and vows" will become "oath of victory").

</div>

<div class="post" data-post-id="12043" data-author="Krok" data-date="2006-04-10T16:19:51+00:00">

A pit fiend slashes Captain Morgan extremely hard.

A pit fiend massacres Captain Morgan to small fragments with his slash.

A pit fiend slashes Captain Morgan extremely hard.

A pit fiend slashes Captain Morgan extremely hard.

Captain Morgan misses you with his hit.

You've broken your oath of victory!

Captain Morgan misses you with his hit.

Captain Morgan misses you with his hit.

</div>

<div class="post" data-post-id="12048" data-author="Autolycos" data-date="2006-04-10T17:23:02+00:00">

Next time take a 2nd bottle with you!  :twisted: 

Captain Morgan yells 'the rums gone?  BUT WHY IS THE RUM GONE?'

</div>

<div class="post" data-post-id="12075" data-author="kjartan" data-date="2006-04-11T16:31:14+00:00">

The oath of victory should be fixed now.  Please let me know if there are any more instances of it breaking spontaneously.  (In some circumstances you will neither fulfill nor break the oath, for example if an immortal shows up and stops the combat - in that case it will just end.)

</div>

<div class="post" data-post-id="12148" data-author="Rajil" data-date="2006-04-19T17:08:37+00:00">

I attacked a mob and successfully swore victory. Viscount Durken tossed me out of the room ... I went back in and killed him, but it seemed my oath was nullified.

On the next mob, the vampyric princess who never pops for me... I again successfully swore victory. My pet wraith ended up killing her and I never got the message of completion. Funny, because my pet killed her yesterday, and I got a message of completion then...

Something wrong?

</div>

<div class="post" data-post-id="12150" data-author="kjartan" data-date="2006-04-19T17:34:35+00:00">

As far as the toss, no, if the combat is broken off due to some weirdness like being tossed out of the room, the oath ends, and is counted as neither a success nor a failure.  If you want you can swear victory again once you have reengaged the mob.  I don't really see any other way of handling this, as I don't want people walking around with a bunch of unfulfilled victory oaths but you could have just walked off at that point and never resolved the fight.

As far as the pets, I am guessing that you weren't engaged with the mob?  It wouldn't count as a win if you weren't fighting the mob, it would just end the oath.  I will have a look at changing that; probably it's more reasonable to count it as a win as long as you are in the room.

</div>

<div class="post" data-post-id="12152" data-author="Guinex" data-date="2006-04-19T17:50:06+00:00">

The last time I used oaths a couple of days ago, i was probably four down on the prot chain, and i ended up taking 3/4 of the hits and died.  I saw this happen to a few people in the group, unfortunately i did not save any logs on this.  I can test it again tonight to see if it is still doing so, from what it looks though it is pulling in the new swear with it.

</div>

<div class="post" data-post-id="12154" data-author="kjartan" data-date="2006-04-19T18:08:37+00:00">

Ooh, that's bad!  I'll have a look tonight.  Although possibly you just had bad luck, because oath of protection doesn't do that - it improves your ability to rescue and protect, but it doesn't make other people protecting you more likely to fail.

</div>

<div class="post" data-post-id="12155" data-author="Vixn" data-date="2006-04-19T18:53:04+00:00">

Edd [BH] .. Hereticus ..   (level: 40)

Your levels:  Ma: 40 Cl: 40 Wa: 40 Th: 40 Av: 28 

You are neutral.

<762hp 430ma 159mv 2.9ac +0al>

ask narmer about quests

You ask Narmer about quests.

Narmer tells you 'I'm also looking for a wandering minstrel named (kenji).'

<762hp 437ma 163mv 2.9ac +0al>

ask narmer about kenji

You ask Narmer about kenji.

Narmer tells you 'Sadly, you aren't eligible for this quest because you must be high enough level to learn 'oaths and vows'.'

<762hp 516ma 216mv 2.9ac +0al>

undertake kenji

Narmer tells you 'Sadly, you aren't eligible for this quest because you must be high enough level to learn 'oaths and vows''

what does it mean?

</div>

<div class="post" data-post-id="12156" data-author="Guinex" data-date="2006-04-19T19:06:05+00:00">

I don't think it was just bad luck, it seemed pretty clear what the cause was.  It wasn't just me that it had happened to, and on numerous mobs.

</div>

<div class="post" data-post-id="12157" data-author="Shazuko" data-date="2006-04-19T21:23:52+00:00">

It happened to me and Caldrick as well...at the same time...

Shazuko Roku Ryuu

<Shazuko Six Dragons>

<~Chaos~>

</div>

<div class="post" data-post-id="12161" data-author="kjartan" data-date="2006-04-20T03:14:58+00:00">

Ah, now I remember: that's a feature, not a bug.  Or, let me put it like this: the gods do not value such oaths if you aren't in any danger.

</div>

<div class="post" data-post-id="12162" data-author="12345" data-date="2006-04-20T03:58:11+00:00">

But do the gods value helpfiles?

It's probably already there, but if it isn't, it should be.

</div>

<div class="post" data-post-id="12170" data-author="Guinex" data-date="2006-04-20T06:19:28+00:00">

what does the victory swear have to do with danger?

</div>

<div class="post" data-post-id="12171" data-author="Vixn" data-date="2006-04-20T06:29:14+00:00">

Oaths & vows seems very nice to me cause it bring new power to warriors and old classoes. But do we need ton of oaths that doesn't work?

Does anybody there gonna fix quest so ppl could learn this skill? Or you will just make more and more oaths and vows wich almost nobody can't use? I understand this is skill just added and there should be some testing period, sure skill can be tuned or screwed but I don't understand why KJ and others continues to add new features w/o fixing existent bugs..

Thanks  :twisted:

</div>

<div class="post" data-post-id="12193" data-author="kjartan" data-date="2006-04-20T15:54:41+00:00">

You're the only one who reported that particular bug.  I will have a look at it.  As I'm sure I have said before, we only have the patience for a limited amount of testing before we put in new features, and so some bugs slip through.  Oath of Victory had more than usual, because it is actually a very complicated feature from a code standpoint - before that, the game never really tracked whether you won, lost, or drew a combat.

</div>

<div class="post" data-post-id="12195" data-author="madmax" data-date="2006-04-20T17:17:14+00:00">

Madmax Thanks Enea <*GT*>  (level: 40)

Your levels:  Cl: 40 Ma: 40 Wa: 40 Ne: 40 Av: 26

You ask Narmer about quests.

Narmer tells you 'Disrupt the control of entropic forces over a young warrior's

mind and find the stolen (sword).'

Narmer tells you 'I'm also looking for a wandering minstrel named (kenji).'

<783hp 573+59ma 110mv> -10 <indoors - 294,606,629 XP - 65,554 coins>

ask narmer about kenji

You ask Narmer about kenji.

Narmer tells you 'Sadly, you aren't eligible for this quest because you must be high enough level to learn 'oaths and vows'.'

<783hp 573+59ma 113mv> -10 <indoors - 294,606,629 XP - 65,554 coins>

uptime

Last bootup: Wed Apr 19 20:25:38 2006

Current time: Thu Apr 20 12:15:03 2006

15 hours since bootup.

Seems to be broke for me too.. 

Madmax

</div>

<div class="post" data-post-id="12196" data-author="Vixn" data-date="2006-04-20T18:08:57+00:00">

You're the only one who reported that particular bug.  I will have a look at it.  As I'm sure I have said before, we only have the patience for a limited amount of testing before we put in new features, and so some bugs slip through.  Oath of Victory had more than usual, because it is actually a very complicated feature from a code standpoint - before that, the game never really tracked whether you won, lost, or drew a combat.[/quote:2f07sb6l]

Thanks KJ and sorry for my annoying - I was sure this bug has been reported before but I was wrong. Sorry.

Peace.  :roll:

</div>

<div class="post" data-post-id="12197" data-author="Ditheca" data-date="2006-04-20T19:46:22+00:00">

This happened twice in about 3 minutes.  I killed a mob and got no xps.  I post it here because I think it likely that the oaths and vows code is causing the error.  In both cases I was not fighting the mob until I made the killing blow.

----------------------------------

A crazed man flees to the south!

<541hp 204ma 197mv> -10 [2:SAIF ]

s

t k

Approaching a Fork

Exits: North  South  

A small sapling wrenched from the ground lies tilted in the corner here.

An uncovered wagon is propped up on four roughly equally sized chunks of rock.

A crazed man flails his arms about while speaking in tongues.

<541hp 204ma 197mv> -10 [2:SAIF ]

A crazed fanatic hates your guts!

A crazed fanatic looks shocked as he sees your fist embedded in his abdomen, then collapses.

A crazed fanatic is dead! R.I.P.

Your blood freezes as you hear a crazed fanatic's death cry.

You get gold coins from the corpse of a crazed fanatic that's on the ground.

There were 1593 coins.

--------------

A phantom massacres a young man to small fragments with its claw.

A phantom claws a young man extremely hard.

A phantom massacres a young man to small fragments with its claw.

A phantom massacres a young man to small fragments with its claw.

A phantom claws a young man extremely hard.

A phantom massacres a young man to small fragments with its claw.

A vicious Ju-Ju Zombie massacres a young man to small fragments with its hit.

A vicious Ju-Ju Zombie massacres a young man to small fragments with its hit.

A vicious Ju-Ju Zombie hits a young man extremely hard.

A young man's blow passes right through a phantom with no effect!

A young man's blow passes right through a phantom with no effect!

A young man misses you with his pound.

A young man hates your guts!

You quickly duck aside and use a young man's strength against him in a brutal counterattack!

A young man is dead! R.I.P.

Your blood freezes as you hear a young man's death cry.

You get gold coins from the corpse of a young man that's on the ground.

There were 11392 coins.

</div>

<div class="post" data-post-id="12198" data-author="kjartan" data-date="2006-04-20T20:37:15+00:00">

Ok, I will have a look at that too.  I will probably be able to get to these tonight, US Pacific time.

</div>

<div class="post" data-post-id="12325" data-author="kjartan" data-date="2006-04-22T15:50:51+00:00">

The problem with people learning the skill oath of victory should be fixed next crash or reboot.

</div>

<div class="post" data-post-id="12327" data-author="kjartan" data-date="2006-04-22T20:50:49+00:00">

I don't think the oaths could be causing the missing xp problem; has then continued to happen?

</div>

<div class="post" data-post-id="12328" data-author="Guinex" data-date="2006-04-22T22:39:39+00:00">

Ditheca isn't even a warrior, why he posted that on this thread, well we may never know.

</div>

<div class="post" data-post-id="12330" data-author="Choong" data-date="2006-04-23T01:30:57+00:00">

Is this a wa prime only skill? Coz I when I tried to undertake the auto, it says your are not high level enough to undertake this

</div>

<div class="post" data-post-id="12333" data-author="kjartan" data-date="2006-04-23T03:09:46+00:00">

That's the aforementioned bug - the game hasn't rebooted yet.  After next reboot you should be ok.  It's not prime-only.

</div>

<div class="post" data-post-id="12338" data-author="Vixn" data-date="2006-04-23T16:34:38+00:00">

[quote:1a9nqwzf]<635hp 87ma 175mv -2.1ac -9al>

undertake kenji

Narmer tells you 'Sadly, you aren't eligible for this quest because you must be high enough level to learn 'oaths and vows''

<638hp 93ma 179mv -2.1ac -9al>

time start

Last bootup: Sun Apr 23 15:18:20 2006

Current time: Sun Apr 23 16:30:29 2006

1 hour since bootup.[/quote:1a9nqwzf]

Is it still broken or should we just wait till another reboot?

</div>

<div class="post" data-post-id="12345" data-author="Vixn" data-date="2006-04-24T12:44:37+00:00">

Last bootup: Mon Apr 24 09:30:47 2006

Current time: Mon Apr 24 12:42:02 2006

3 hours since bootup.

<629hp 193ma 178mv -9.4ac -8al>

undertake kenji

Narmer tells you 'Sadly, you aren't eligible for this quest because you must be high enough level to learn 'oaths and vows''

</div>

<div class="post" data-post-id="12348" data-author="kjartan" data-date="2006-04-24T16:51:13+00:00">

Argh.  Well, it worked for me.  I will have to try it with your character.  Probably I can get to it tonight.

</div>

<div class="post" data-post-id="12349" data-author="deucer" data-date="2006-04-24T20:39:44+00:00">

You ask Narmer about kenji.

Narmer tells you 'Sadly, you aren't eligible for this quest because you must be high enough level to learn 'oaths and vows'.'

<662hp 146ma 114mv>

...same thing for Zuuul (ne40 wa40 ma34 th20)  :?

</div>

<div class="post" data-post-id="12350" data-author="kjartan" data-date="2006-04-25T03:58:15+00:00">

Ok, I think it's fixed now.  (I had changed the name of the skill to 'oath of victory', but I forgot to tell Narmer.)

</div>

<div class="post" data-post-id="12351" data-author="Vixn" data-date="2006-04-25T05:44:31+00:00">

Thank a lot. Narmer is just a warrior that's why I don't surprise he can't make a conjecture.

</div>

<div class="post" data-post-id="12356" data-author="Shyla" data-date="2006-04-25T16:32:58+00:00">

hmm since you are answering questions about oath of victory is there any reason it is on my practice unlearned list even though i did the quest when it was first put in?

:) 

shyla

</div>

<div class="post" data-post-id="12359" data-author="kjartan" data-date="2006-04-25T19:13:08+00:00">

That's pretty strange.   (1) does it say 'oaths and vows' or 'oath of victory'?  and (2) can you do the oath?

</div>

<div class="post" data-post-id="12367" data-author="Vixn" data-date="2006-04-26T05:34:09+00:00">

I've done kenji quest yesterday (again thanks a lot KJ!) and now I have learned oath of victory at 100% though my dear friend Lob has it at 85%. He had done this quest some time ago, before it was changed to oath of victory. So he also has this skill in his prac unlearned list but I'm pretty sure that's just because he's a wa-prime dumbass :)

</div>

<div class="post" data-post-id="12372" data-author="Falsra" data-date="2006-04-26T11:12:30+00:00">

oath of victory       - Lvl: 35,           Learned  85%

and i am not wa-prime!  :twisted:

</div>

<div class="post" data-post-id="12379" data-author="Shyla" data-date="2006-04-26T16:34:01+00:00">

<674hp 630ma 153mv>

undertake kenji

Narmer tells you 'You have already completed that task!'

                    Warrior Skills:

oath of victory       - Lvl: 35,           Learned  85%

I have no idea why this is all I am asking is can it be "fixed"

</div>

<div class="post" data-post-id="12380" data-author="kjartan" data-date="2006-04-26T16:39:06+00:00">

Yeah, I will add something to Narmer so that he will up you to 100% if you come to him with 85%.  However, I am going to be out of town for a few days, so probably not til next week.

</div>

<div class="post" data-post-id="12387" data-author="kjartan" data-date="2006-04-27T03:23:07+00:00">

Ok, I found some time to fix it.  If you're at 85, go talk to Narmer, he'll fix you right up.

</div>

<div class="post" data-post-id="12389" data-author="Shyla" data-date="2006-04-27T05:39:25+00:00">

thanks :)

</div>

<div class="post" data-post-id="12582" data-author="Chobbles" data-date="2006-05-18T16:38:13+00:00">

Tiamat the dragon queen misses you with her claw.

Tiamat the dragon queen misses you with her claw.

Tiamat the dragon queen misses you with her bite.

Tiamat the dragon queen misses you with her bite.

Tiamat the dragon queen misses you with her bite.

Tiamat the dragon queen looks shocked as she cuts herself on your bone armor!

You are brutally massacred by Tiamat the dragon queen's bite.

Tiamat the dragon queen spits acid at you!  Your flesh is seared!

Your spell shield absorbs the damage!

Draco utters the words, 'candusghafahuai' (restoration)

The cleansing fires of healing fill your body!

<1029/1029hp 249/311ma 74mv 6:04 am 154410382 indoors>

You grouptell: '( +158 HP ) HP: [ 879/1029 ] Need: [ 150 ]'

<1029/1029hp 250/311ma 74mv 6:05 am 154410382 indoors>

You swear a mighty oath of victory over Tiamat the dragon queen![/color:3j4bjq7w]

A loooong time later (fat tammy, lose some weight!)

.

.

.

Tiamat the dragon queen's bones crunch under a well-aimed attack by Valanthe!

Tiamat the dragon queen misses you with her claw.

Tiamat the dragon queen misses you with her bite.

Tiamat the dragon queen misses you with her bite.

Tiamat the dragon queen misses you with her bite.

You skillfully parry the attack of Tiamat the dragon queen.

Your riposte viciously massacres Tiamat the dragon queen.

You are viciously massacred by Tiamat the dragon queen's hit.

You miss Tiamat the dragon queen with your slash.

You miss Tiamat the dragon queen with your slash.

Tiamat the dragon queen grins at you as she whacks you upside the head!

You've broken your oath of victory![/color:3j4bjq7w]

Based on Kjartan's earlier post regarding tosses and oaths, I was under the impression that being tossed out of a room nullifies any attempt at fulfilling your oath.  Maybe I missed something. So much for unbesmirched. :(

</div>

<div class="post" data-post-id="12609" data-author="kjartan" data-date="2006-05-20T15:34:28+00:00">

Fixed, in next crash or reboot.

</div>

<div class="post" data-post-id="12834" data-author="Mike" data-date="2006-06-01T21:48:41+00:00">

<989hp 305ma 208mv -1>

Truth hits the megalodon extremely hard.

The megalodon misses you with its bite.

You skillfully parry the attack of the megalodon.

Your riposte viciously massacres the megalodon.

The megalodon misses you with its bite.

The megalodon misses you with its bite.

You are viciously massacred by the megalodon's bite.

You massacre the megalodon to small fragments with your slash.

Truth misses the megalodon with her hit.

Truth massacres the megalodon to small fragments with her hit.

Truth massacres the megalodon to small fragments with her hit.

The great maw of the megalodon opens wide...

You are suddenly inside the megalodon' mouth![/color:njigofbi]

You've broken your oath of victory![/color:njigofbi]

You feel very disoriented. 

Inside the Megalodon 

   Stomach acid burns your entire body as the great shark attempts to

digest you whole.  Cramped in these very tight quarters, you are unable to 

perform any but the most simple tasks.  Your only hope is that someone will

vanquish the shark and set you free.

Exits:

</div>

<div class="post" data-post-id="12836" data-author="kjartan" data-date="2006-06-01T22:06:16+00:00">

Ok, I'll have a look at it tonight.  I hope to eventually squash all of these.  Has anybody learned the oath of protection yet?

</div>

<div class="post" data-post-id="12841" data-author="kjartan" data-date="2006-06-02T01:17:29+00:00">

Fixed, incor.

</div>

<div class="post" data-post-id="12844" data-author="madmax" data-date="2006-06-02T02:23:54+00:00">

oath of victory        - Lvl: 35,           Learned 100%

oath of protection    - Lvl: 37,           Learned 100%

</div>

<div class="post" data-post-id="12847" data-author="12345" data-date="2006-06-02T11:21:10+00:00">

Rynquald had protection learned.  Even had some fun learning it.  Think he pretty much broke off using it when we found out he couldn't disengage to reblind/reaegis/etc.  Seems to be a good skill for the top few of the protect chain though.

</div>

<div class="post" data-post-id="12849" data-author="madmax" data-date="2006-06-02T17:40:44+00:00">

That is exactly what I have found for both of them.  It is impossible to disengage and cast.

So I am the same, not using in groups anyway.

Madmax

</div>

<div class="post" data-post-id="13017" data-author="Avatar" data-date="2006-06-18T02:55:15+00:00">

I learned Oath of Protection today, but it still shows in my PR Unlearned list.

                    Warrior Skills:

oath of protection    - Lvl: 37,           Learned  95%

I'm sitting at Narmer now, but I don't know if there's some command needed to have him mod me up to 100%.

I think the problem is that there seem to be two endings for the Oath of Protection Autoquest.  I opted to finish this using the second ending, the one you have to listen for, and it only bumped me to 95% instead of 100%.

Charles (char is Avatar)

</div>

<div class="post" data-post-id="13021" data-author="kjartan" data-date="2006-06-18T04:22:22+00:00">

That's not a bug.

</div>

<div class="post" data-post-id="13022" data-author="marchessa_the_red_witch" data-date="2006-06-18T07:44:18+00:00">

There should be some way for a tank to get the mobs attention from someone who has oath of protection. Rescue, which takes a person out of the fight, clearly isn't it. But what about "engage"?

</div>

<div class="post" data-post-id="13024" data-author="marchessa_the_red_witch" data-date="2006-06-18T08:26:16+00:00">

Druscilla misses you with her claw.

Druscilla misses you with her claw.

You skillfully parry the attack of Druscilla.

Druscilla misses you with her bite.

Druscilla misses you with her claw.

Druscilla bites you very hard.

You slash Druscilla very hard.

You slash Druscilla extremely hard.

823/834/+66hp 315/317/+18ma 188/188 -10align 1:42 am 160513062xp 199292 -9.6ac

toss siYou swear a mighty oath of victory over Druscilla!

1033/834/+66hp 316/317/+18ma 188/188 -10align 1:44 am 160513062xp 199292 -9.6ac

nger e

You grab Druscilla and throw her to the east!

Congratulations, you have fulfilled your oath of victory!

827/834/+42hp 316/317/+18ma 158/188 -10align 1:46 am 160517532xp 199292 -9.6ac

- - -

Tossing the mob should not get you honor - it is against the concept of the idea. I could understand oath of victory barring tossing the mob out - and this is certainly simplest to code. 

But better would be to simply make it so that the oath of victory is still running, but if the character doesn't get back into combat post hase - say 6 mud minutes or so, or does anything that is regenish - sleep, rest, change eq - the oath has failed. Toss is a combat move to do damage, and part of doing ones level best to fulfill the oath, and best would be to treat it that way.

But even putting what MIT students used to call "a screw" into it would be preferable to having a cheap way out.

</div>

<div class="post" data-post-id="13039" data-author="Avatar" data-date="2006-06-19T05:28:01+00:00">

Well, it's interesting to have an autoquest with multiple endings.  Still, I think I think it sucks that we'd punish someone for actually listening to the content of the autoquest, then spending an extra 45 minutes performing the quest.

I can't believe I was chatting about how cool some of the new quests are.

</div>

<div class="post" data-post-id="13040" data-author="marchessa_the_red_witch" data-date="2006-06-19T16:45:24+00:00">

The info in the quest is sufficient to make a good decision about it.

I listened, and while the mud alignment system is... odd ... it is pretty clear.

</div>

<div class="post" data-post-id="13041" data-author="kjartan" data-date="2006-06-19T17:53:09+00:00">

Yes, but now the gods can look at your level in that skill and if it's 98% instead of 100% judge you to be of better character.  From a gameplay standpoint, I'd say it doesn't make any measurable difference: you will blow the oath 1 time in 50, big deal.  And I agree with Marchessa: if all you wanted was to max out the skill, then you could have figured out from the quest info that the "jerk" ending would give you more plusses.  Ain't that just life.

</div>

<div class="post" data-post-id="13042" data-author="Avatar" data-date="2006-06-19T19:28:09+00:00">

I read all the information, and nothing led me to believe that it would be a worse ending.  I spent more time on the quest, found the right mob, made her happy, etc.  I guess it's not worth complaining about, except that the skill still shows up on my unlearned lists.  

I guess that's what I get for listening to a woman. 

Is there any way to reset an autoquest so I can just do it over?

</div>

<div class="post" data-post-id="13043" data-author="kjartan" data-date="2006-06-19T20:35:01+00:00">

I guess it's not worth complaining about, except that the skill still shows up on my unlearned lists.[/quote:245p3re4]

How about I just make that particular skill not show up on your unlearned lists if it's at that percent?

</div>

<div class="post" data-post-id="13044" data-author="Avatar" data-date="2006-06-19T21:35:11+00:00">

That would be fine with me.

</div>

<div class="post" data-post-id="13047" data-author="marchessa_the_red_witch" data-date="2006-06-20T06:16:48+00:00">

Everyone has been set to 98% in the oath now.

</div>

<div class="post" data-post-id="13048" data-author="kjartan" data-date="2006-06-20T13:39:16+00:00">

Well, either way, it will now not show up on prac unlearned unless it's < 98%

</div>

<div class="post" data-post-id="13049" data-author="Medios" data-date="2006-06-20T21:52:41+00:00">

Can someone explain to me what oaths actually does, other than get ppl in my groups killed for no reason?

Mike

</div>

<div class="post" data-post-id="13050" data-author="Avatar" data-date="2006-06-20T22:18:54+00:00">

I'm sorry to bring this up again KJ, but my Oath was set to 95% by the autoquest.  It's still 95%, and still on my unlearned list.

Charles

</div>

<div class="post" data-post-id="13051" data-author="kjartan" data-date="2006-06-20T22:24:39+00:00">

Oh is it 95?  Whoops, I thought it was 98.  I will fix it to show up unlearned, sorry about that.

</div>

<div class="post" data-post-id="13059" data-author="marchessa_the_red_witch" data-date="2006-06-21T06:07:38+00:00">

Oath of victory adds about 200 hps, even going over your max - so I top out at 1080hps when uttering an oath fast against a mob that doesn't hit hard

</div>

<div class="post" data-post-id="13062" data-author="madmax" data-date="2006-06-21T15:42:12+00:00">

KJ - can you fix this one too?

Last bootup: Wed Jun 21 09:30:49 2006

Current time: Wed Jun 21 10:38:46 2006

1 hour since bootup.

prac unl

                    Warrior Skills:

oath of victory       - Lvl: 35,           Learned  98%

</div>

<div class="post" data-post-id="13063" data-author="Weasel" data-date="2006-06-21T15:45:12+00:00">

heh yup.. I was 100% learned, now I'm 98% and it shows up as unlearned.. methinks you tweaked the wrong bit.

</div>

<div class="post" data-post-id="13064" data-author="kjartan" data-date="2006-06-21T16:13:01+00:00">

Argh.  Jeez, I even tested it and everything.  Well, I will try to figure it out some more later.

</div>
