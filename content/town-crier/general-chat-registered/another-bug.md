---
title: "Another bug"
topic_id: 2415
author: "Marchessa_red_witch"
date: 2007-03-26T00:57:02+00:00
last_activity: 2007-05-05T14:46:32+00:00
last_author: "13"
sticky: false
locked: false
post_count: 50
---

<div class="post" data-post-id="17473" data-author="Marchessa_red_witch" data-date="2007-03-26T00:57:02+00:00" data-subject="Another bug">

Pannalal has had enough: he attacks you!

1-\> 1025/1025/+43hp 164/375/+25ma 109/205/+28mv +8/+9 

2-\> -11.0ac 1211069576xp 44786gp +10align 8:28 am fair Ah.Hellwell

bs pan

You can't backstab a fighting person, too alert!

1-\> 1025/1025/+43hp 164/375/+25ma 110/205/+28mv +8/+9 

2-\> -11.0ac 1211069576xp 44786gp +10align 8:28 am fair Ah.Hellwell

rem bolt

You stop using a thunderbolt.

1-\> 1025/1025/+43hp 164/375/+25ma 110/205/+28mv +6/+6 

2-\> -11.0ac 1211069576xp 44786gp +10align 8:28 am fair Ah.Hellwell

wield sword

You wield Brilliant Sword of Valor.

1-\> 1025/1025/+43hp 165/375/+25ma 110/205/+28mv +7/+8 

2-\> -11.0ac 1211069576xp 44786gp +10align 8:29 am fair Ah.Hellwell

Ok.

1-\> 1025/1025/+43hp 165/375/+25ma 110/205/+28mv +7/+8 

2-\> -11.0ac 1211069576xp 44786gp +10align 8:29 am fair Ah.Hellwell

dise

You don't seem to be fighting anyone right now.

1-\> 1025/1025/+43hp 165/375/+25ma 110/205/+28mv +7/+8 

2-\> -11.0ac 1211069576xp 44786gp +10align 8:30 am fair Ah.Hellwell

The bug here is that backstab bounces because I am in combat, but combat hasn't actually started for the purposes of the disengage. 

This bug could actually be exploited - since the mob doesn't hate yet - could somehow bail out and try again - though since this is a script I didn't. 

Expected behavior - if mob "attacks" and bounces backstab, then other noncombat actions should be prevented as well...

</div>

<div class="post" data-post-id="17474" data-author="Rynquald" data-date="2007-03-26T02:08:15+00:00" data-subject="">

That prompt is scary...

</div>

<div class="post" data-post-id="17475" data-author="Atwell" data-date="2007-03-26T02:18:13+00:00" data-subject="Re: Another bug">

This isn't actually a bug.

> <strong>Marchessa\_red\_witch wrote:</strong>
> Pannalal has had enough: he attacks you!
> 
> 1-\> 1025/1025/+43hp 164/375/+25ma 109/205/+28mv +8/+9 
> 
> 2-\> -11.0ac 1211069576xp 44786gp +10align 8:28 am fair Ah.Hellwell
> 
> bs pan
> 
> You can't backstab a fighting person, too alert!

As the message says: he is fighting someone, specifically you, but...

> <strong>Marchessa\_red\_witch wrote:</strong>
> dise
> 
> You don't seem to be fighting anyone right now.

you are not yet fighting him. After the first round, you will be fighting him as well. The game is working as designed here.

</div>

<div class="post" data-post-id="17476" data-author="Medios" data-date="2007-03-26T03:23:57+00:00" data-subject="">

The same thing occurs if you try to dispel. Sometimes the mob will attack you but it pauses for a few seconds before the first round. You cannot stab or disengage, only flee. The mob does not hate because you haven't hit it yet. I believe one of the monk skills will still work, possibly death touch.

Mike

</div>

<div class="post" data-post-id="17478" data-author="Marchessa_red_witch" data-date="2007-03-26T10:59:27+00:00" data-subject="Re: Another bug">

> <strong>Atwell wrote:</strong>
> This isn't actually a bug. The game is working as designed here.

I will wait for a immort to say that before writing script that exploit the behavior.

</div>

<div class="post" data-post-id="17479" data-author="Marchessa_red_witch" data-date="2007-03-26T11:23:36+00:00" data-subject="All the information I need">

> <strong>Rynquald wrote:</strong>
> That prompt is scary...

in one place.

</div>

<div class="post" data-post-id="17481" data-author="Shazuko" data-date="2007-03-26T15:46:34+00:00" data-subject="">

I was recently cycling crimson appie, and after my dispel, i was always able to get a curse in...didn't try to grip though, but it seems theres a few seconds there to do something if your quick...never got that 'you are already in combat' mssg until he was actually on me...\*shrug\*

\<Shazuko Roku Ryuu\>

\<Shazuko Six Dragons\>

\<\~Chaos\~\>

</div>

<div class="post" data-post-id="17485" data-author="alias" data-date="2007-03-26T18:55:22+00:00" data-subject="">

You cant backstab a wounded mob, most people would have actually hit the mob in the first round and made it wounded so as not to be able to backstab,

Speaking of which i need more -hitroll eq so i can get a second chance.

Marchessa, damn no wonder u miss a lot of the game that prompt is almost as long as the list of brads alts.

Alias

</div>

<div class="post" data-post-id="17486" data-author="Marchessa_red_witch" data-date="2007-03-26T19:20:55+00:00" data-subject="">

> <strong>alias wrote:</strong>
> You cant backstab a wounded mob, most people would have actually hit the mob in the first round and made it wounded so as not to be able to backstab,
> 
> 
> 
> Alias

Read the excerpt again, there was no backstab, let alone a whiff.

</div>

<div class="post" data-post-id="17487" data-author="Autolycos" data-date="2007-03-26T19:55:36+00:00" data-subject="">

> <strong>alias wrote:</strong>
> Marchessa, damn no wonder u miss a lot of the game that prompt is almost as long as the list of brads alts.Alias

come on todd... thats silly.. that prompt would have to print out on 125 pages of standard 8 1/2 x 11.

but seriously.. that prompt is friggen whacked <img src="/images/smilies/icon_mad.svg" alt=":x" title=":x" width="15" height="15" class="smiley nozoom">

</div>

<div class="post" data-post-id="17489" data-author="Marchessa_red_witch" data-date="2007-03-26T20:10:37+00:00" data-subject="prompt score bug">

1-\> $h/$H/$Bhp $m/$M/$Rma $v/$V/$bmv $I/$D $n2-\> $aac $xxp $ggp $Aalign $Q $w $c.$Z

Just for the record.

Text mudding lives.

</div>

<div class="post" data-post-id="17490" data-author="Guinex" data-date="2007-03-26T20:11:48+00:00" data-subject="">

I have read that about six times, and i am unable to see anything wrong with it.

</div>

<div class="post" data-post-id="17491" data-author="tincts" data-date="2007-03-26T20:14:08+00:00" data-subject="">

With regards to "has had enough; he attacks!!". There are plenty of dispel mobs. Ya go dispel dispel south. North. Dispel dispel south. North. and so on as long as you feel like it. He'll "have enough" each time, but as long as you get out before he hits you, you can wonder back in again and keep teasing him without being smacked.

</div>

<div class="post" data-post-id="17493" data-author="Marchessa_red_witch" data-date="2007-03-26T20:39:35+00:00" data-subject="Script">

> <strong>tincts wrote:</strong>
> With regards to "has had enough; he attacks!!". There are plenty of dispel mobs. Ya go dispel dispel south. North. Dispel dispel south. North. and so on as long as you feel like it. He'll "have enough" each time, but as long as you get out before he hits you, you can wonder back in again and keep teasing him without being smacked.

I've written a script that does \|; $exit if the mob attacks, and recycles to the backstab proc. Am testing it on poor old pannalal.

If that's what the game is supposed to do... might as well automate it.

Personally, if i were the immorts I would set the hate flag, so that if you come back in it fast aggros - which means either stealth or one of the monk skills to get the grip/stab in.

</div>

<div class="post" data-post-id="17495" data-author="Rynquald" data-date="2007-03-26T21:30:09+00:00" data-subject="">

As far as I know the only way mobs hate you is if you try to do them some damage, and as you allmost pointed out yourself, everyone that can stab/grip can just sneak/presage anyway.

</div>

<div class="post" data-post-id="17497" data-author="Marchessa_red_witch" data-date="2007-03-26T21:42:10+00:00" data-subject="Sneak doesn&#x27;t">

avoid mobs that hate you, stealth is much higher level and has a 40mv cost - that is, as it stands, recycling costs almost nothing - no backstab happened merely the cost of walking out and back in again - which is all most always trivial. Which is why I now have a script that checks whether I want to recycle in the event of a blown dispel, and walks back out leaving me to decide how to go back in. 

Presage has a chance to fail, and grip isn't as good as stab, so having the ability to recycle at a lower level makes sense.

Essentially the mob action was intended to prevent combining the first action (study or a dispel that triggered the attack) with the second - stab specifically. As it is currently implemented, it does not do that. In fact, the mob is less dangerous than if it has simply gone aggro - and while Pannalal is slow agrro, he is, in fact, aggro. Had the attack trigger simply had him swing his claw, then walking out would not have worked.

If this is the intention - that is, have people write a trigger - ok. But somehow I think not, instead, the mob action was meant to impose a cost on the character. Currently, in almost all cases, it does not.

</div>

<div class="post" data-post-id="17499" data-author="Medios" data-date="2007-03-26T22:14:56+00:00" data-subject="">

So Marchessa is saying that sneak does not work against hated mobs? I would have to disagree, the rate of sneakiness might be lower but it still works afaik. Stealth is surefire, sneak is not. Bot scripts are lame, playing sloth has made my hand eye coordination go way up with the keyboard. My typing has improved greatly in the last 5 years. The only triggers I use have to do with irritating stuff like eating food, grouptells about aegis down, prot order, exiting boats, etc. Using scripts all the time would take away from my gaming experience. Its sad you guys script every command.

Mike

</div>

<div class="post" data-post-id="17500" data-author="Autolycos" data-date="2007-03-26T22:46:01+00:00" data-subject="">

> <strong>Medios wrote:</strong>
> Using scripts all the time would take away from my gaming experience. Its sad you guys script every command.

i absofuckinlutely agree..

</div>

<div class="post" data-post-id="17503" data-author="Marchessa_red_witch" data-date="2007-03-27T00:14:48+00:00" data-subject="Scripts Work">

> <strong>Medios wrote:</strong>
> Its sad you guys script every command.
> 
> 
> 
> Mike

Ok, you'll try to move silently for a while.

1-\> 987/987/+43hp 339/346/+25ma 117/206/+28mv +7/+9 

2-\> -11.0ac 39268958xp 597821gp +10align 4:53 pm overcast Ah.Hellwell

Inside the Hut of a Madman!

Exits: West 

You see Pannalal here.

1-\> 987/987/+43hp 339/346/+25ma 114/206/+28mv +7/+9 

2-\> -11.0ac 39268958xp 597821gp +10align 4:53 pm overcast Ah.Hellwell

Ok.

You feel a spell unravel! Success!

You feel a spell unravel! Success!

Pannalal has had enough: he attacks you!

1-\> 987/987/+43hp 334/346/+25ma 114/206/+28mv +7/+9 

2-\> -11.0ac 39268958xp 597821gp +10align 4:53 pm overcast Ah.Hellwell

You can't backstab a fighting person, too alert!

1-\> 987/987/+43hp 334/346/+25ma 114/206/+28mv +7/+9 

2-\> -11.0ac 39268958xp 597821gp +10align 4:54 pm overcast Ah.Hellwell

Outside a Small Hut

Exits: East West Up 

Standing upright in a corner is a granite tablet. [2]..It emits a faint humming sound!

1-\> 987/987/+43hp 334/346/+25ma 112/206/+28mv +7/+9 

2-\> -11.0ac 39268958xp 597821gp +10align 4:54 pm overcast Ah.Hellwell

sneak;e;bs pan

Ok, you'll try to move silently for a while.

1-\> 987/987/+43hp 344/346/+25ma 123/206/+28mv +7/+9 

2-\> -11.0ac 39268958xp 597821gp +10align 5:18 pm overcast Ah.Hellwell

Inside the Hut of a Madman!

Exits: West 

You see Pannalal here.

1-\> 987/987/+43hp 344/346/+25ma 120/206/+28mv +7/+9 

2-\> -11.0ac 39268958xp 597821gp +10align 5:18 pm overcast Ah.Hellwell

Pannalal hates your guts!

Pannalal makes a strange sound, as you place a thunderbolt in his back.

Pannalal makes a strange sound, as you place a thunderbolt in his back.

1-\> 987/987/+43hp 344/346/+25ma 100/206/+28mv +7/+9 

2-\> -11.0ac 39278358xp 597821gp +10align 5:18 pm overcast Ah.Hellwell

"Attacks you means"... ummm nothing in most cases

In fact to show you how lame not hating is...

You see Pannalal here.

1-\> 987/987/+43hp 365/376/+25ma 114/206/+28mv +9/+9 

2-\> -11.0ac 50964341xp 93280gp +10align 12:29 am overcast Ah.Hellwell

Ok.

You feel a spell unravel! Success!

You feel a spell unravel! Success!

You feel a spell unravel! Success!

You feel a spell unravel! Success!

You feel a spell unravel! Success!

You feel a spell unravel! Success!

Pannalal has had enough: he attacks you!

1-\> 987/987/+43hp 361/376/+25ma 114/206/+28mv +9/+9 

2-\> -11.0ac 50964341xp 93280gp +10align 12:29 am overcast Ah.Hellwell

You can't backstab a fighting person, too alert!

1-\> 987/987/+43hp 361/376/+25ma 114/206/+28mv +9/+9 

2-\> -11.0ac 50964341xp 93280gp +10align 12:29 am overcast Ah.Hellwell

Outside a Small Hut

Exits: East West Up 

Standing upright in a corner is a granite tablet. [2]..It emits a faint humming sound!

1-\> 987/987/+43hp 361/376/+25ma 111/206/+28mv +9/+9 

2-\> -11.0ac 50964341xp 93280gp +10align 12:29 am overcast Ah.Hellwell

You calm down and return to a peaceful state of mind.

1-\> 987/987/+43hp 376/376/+25ma 136/206/+28mv +9/+9 

2-\> -11.0ac 50964341xp 93280gp +10align 1:23 am overcast Ah.Hellwell

killpan

Parry mode is now on.

1-\> 987/987/+43hp 376/376/+25ma 155/206/+28mv +9/+9 

2-\> -11.0ac 50964341xp 93280gp +10align 2:02 am overcast Ah.Hellwell

You yell 'SANGREAL!'

1-\> 987/987/+43hp 376/376/+25ma 155/206/+28mv +9/+9 

2-\> -11.0ac 50964341xp 93280gp +10align 2:02 am overcast Ah.Hellwell

You begin to channel your anger and enter a state of frenzy.

1-\> 987/987/+43hp 376/376/+25ma 155/206/+28mv +9/+9 

2-\> -11.0ac 50964341xp 93280gp +10align 2:02 am overcast Ah.Hellwell

You are not using it.

1-\> 987/987/+43hp 376/376/+25ma 157/206/+28mv +9/+9 

2-\> -11.0ac 50964341xp 93280gp +10align 2:07 am overcast Ah.Hellwell

You do not seem to have the 'thunderbolt'.

1-\> 987/987/+43hp 376/376/+25ma 157/206/+28mv +9/+9 

2-\> -11.0ac 50964341xp 93280gp +10align 2:07 am overcast Ah.Hellwell

It's already open!

1-\> 987/987/+43hp 376/376/+25ma 157/206/+28mv +9/+9 

2-\> -11.0ac 50964341xp 93280gp +10align 2:07 am overcast Ah.Hellwell

Ok, you'll try to move silently for a while.

1-\> 987/987/+43hp 376/376/+25ma 157/206/+28mv +9/+9 

2-\> -11.0ac 50964341xp 93280gp +10align 2:08 am overcast Ah.Hellwell

Inside the Hut of a Madman!

Exits: West 

You see Pannalal here.

1-\> 987/987/+43hp 376/376/+25ma 154/206/+28mv +9/+9 

2-\> -11.0ac 50964341xp 93280gp +10align 2:08 am overcast Ah.Hellwell

You weave the threads of magic masterfully!

You managed to dispel the 'water breathing' spell!

You managed to dispel the 'resist cold' spell!

You managed to dispel the 'resist fire' spell!

You managed to dispel the 'regeneration' spell!

You managed to dispel the 'detect invisibility' spell!

You managed to dispel the 'armor' spell!

You managed to dispel the '' spell!

You are slapped by Pannalal.

1-\> 987/987/+43hp 371/376/+25ma 154/206/+28mv +9/+9 

2-\> -11.0ac 50964341xp 93280gp +10align 2:08 am overcast Ah.Hellwell

Pannalal hates your guts!

You've got a good feeling about this fight...

Pannalal makes a strange sound, as you place a thunderbolt in his back.

Pannalal makes a strange sound, as you place a thunderbolt in his back.

That's right, he slaps me the second time in. The mobs are bringing an emote to a knife fight.

</div>

<div class="post" data-post-id="17504" data-author="Rynquald" data-date="2007-03-27T00:54:25+00:00" data-subject="">

> <strong>Quote:</strong>
> Had the attack trigger simply had him swing his claw, then walking out would not have worked.

Would it really matter if you had to flee instead of walk out to have the mob not hate you?

</div>

<div class="post" data-post-id="17506" data-author="Marchessa_red_witch" data-date="2007-03-27T01:24:56+00:00" data-subject="Differences">

Flee doesn't always work. This is a straight move.

Flee goes any direction, which means with few doors, a greater chance of failure, and with more, a greater chance of ending up someplace you don't want to be.

Flee has lag. Move has almost none.

Flee goes several rooms. Move goes the one room you want to go.

A mob that hated wouldn't have just slapped on the second time in.

And so on.

If the gods are happy with "had enough" being, essentially, no different from push- except if you are lagged and the trigger doesn't fire fast enough, or some exceptional circumstance of the mob - far be it from me to complain. However, the rules are if you exploit a bug, you can be wiped. I've reported the bug, had it confirmed by others, written an exploit and await further word from on high.

If they are happy with the status quo on this, so am I.

</div>

<div class="post" data-post-id="17509" data-author="Shazuko" data-date="2007-03-27T04:37:45+00:00" data-subject="">

I never left the room, even when it 'had enough'...once i actually counted the seconds and got to 2-onethousand (2.5). Seems like i coulda gripped it if I wanted...just didnt because of the type of mob...I guess what you all are saying is that there is a difference between casting another spell and doing a physical attack on a mob thats 'had enough'??

On a side note, presage added to sneak/stealth can help alot...its worked for me several times on some very hateful mobs...

\<Shazuko Roku Ryuu\>

\<Shazuko Six Dragons\>

\<\~Chaos\~\>

</div>

<div class="post" data-post-id="17510" data-author="Mike" data-date="2007-03-27T10:06:20+00:00" data-subject="">

March, soon enough you will find out that it is not 100% garantee that your bot trigger will work. If you cast dispel at the end of the round, mob will hit you right after you dispel him, so all you'll get is a few Its not impossible messages. 

Its so good you start notice things like that after becoming tard, but spaming crier with such things is just silly. Do you really think imms dont play mortal chars and dont know about "bugs" like that? Maybe you start whine about dispel doesnt have cast lag or clearing mobs hated list?

</div>

<div class="post" data-post-id="17511" data-author="13" data-date="2007-03-27T12:32:53+00:00" data-subject="">

Fleeing isn't necessary. What you need to do is type w. Then go back in after like 1/2 seconds and start the fight as you wish. No-one's guts are hated until someone gets hit. That prompt plus all this talk of scripting just confirms my already-formed opinion. You kids today rely too much on clients and shit..it's sad.

</div>

<div class="post" data-post-id="17512" data-author="Marchessa_red_witch" data-date="2007-03-27T13:07:01+00:00" data-subject="Improve the odds">

> <strong>Mike wrote:</strong>
> March, soon enough you will find out that it is not 100% garantee that your bot trigger will work. If you cast dispel at the end of the round, mob will hit you right after you dispel him, so all you'll get is a few Its not impossible messages. 
> 
> Its so good you start notice things like that after becoming tard, but spaming crier with such things is just silly. Do you really think imms dont play mortal chars and dont know about "bugs" like that? Maybe you start whine about dispel doesnt have cast lag or clearing mobs hated list?

Sync starting you attack run with the mud. I learned that ages ago.

The trigger will fail because of net lag more than because of combat round timing. 

Again, the "attacks" out come is virtually null. There are a few, a very, very, very few cases where it does mean somthing, and it will come up in odd circumstances - mostly involving lag, not game mechanics.

I've reported the behavior, others have confirmed it, I've written and tested an exploit of it. If the immorts are happy with the status quo, then that's up to them.

</div>

<div class="post" data-post-id="17513" data-author="Avatar" data-date="2007-03-27T13:43:26+00:00" data-subject="summary?">

This is all opinion, of course. This isn't a bug, it's the way the game works. If you have better ideas, there's an IDEAS command in-game. I guess that most of us would rather see more people use the in-game commands for bugs and ideas rather than posting to the crier. Again, just an opinion.

Charles

</div>

<div class="post" data-post-id="17514" data-author="Marchessa_red_witch" data-date="2007-03-27T13:51:44+00:00" data-subject="Summary">

1\. it is exploitable, and is widely exploited.

2\. It is a very minor, rather than major bug

3\. It is easily fixable by just having the mob react in this case the way it would react to blind or other non-combat ending spells.

4\. Whether the immorts want to do something about it is up to them.

I will also note that the "ideas" line is nowhere near large enough to post an example of the bug, the exploit, and proof the exploit works in the wild.

I will further note that anyone who wasn't aware of the behavior and is reading this thread now knows about it.

</div>

<div class="post" data-post-id="17515" data-author="alias" data-date="2007-03-27T14:09:54+00:00" data-subject="">

If you feel its a bug why did you post it here and not just report it on bugs?

</div>

<div class="post" data-post-id="17516" data-author="Marchessa_red_witch" data-date="2007-03-27T14:17:13+00:00" data-subject="As explained">

I didn't fit in bugs and takes too long to explain.

I don't think it deserves being pkilled for either.

</div>

<div class="post" data-post-id="17517" data-author="13" data-date="2007-03-27T15:05:45+00:00" data-subject="">

There's just something about Marchessa that gets under my skin.

</div>

<div class="post" data-post-id="17519" data-author="Mosaix" data-date="2007-03-27T16:53:13+00:00" data-subject="">

I agree with aaron, there is a element of uncomfort when you read her stuff.

I dont understand half the time where marchessa is coming from.

Maybe just likes to argue.

This thread reads like this to me....

Marchessa - i hate to report this but the sky is blue

Mudder - ok we know the sky is blue

Marchessa - no really the sky is blue and you guys dont realize it, i dont want to be the one getting wiped for finding out the sky is blue.

Mudder - well the imms know the sky is blue, and dont worry about it.

Marchessa - well again the sky is blue, and you need to pay attention to it, dont say i didnt warn you about the sky being blue, and until you realize that the sky is blue its your own undoing, and it needs to be fixed, just because I said so.

So........Essesntially its an argument in circles about stuff that the objective apperas to be to drive everyone bonkers.

After reading this thread is about all I can begin to comprehend about Marchessa's thought process.

Really cut it out i think, and have fun and just mud. Put all that energy into finishing drachma autos or something.

Mosaix

</div>

<div class="post" data-post-id="17522" data-author="Weasel" data-date="2007-03-27T17:51:27+00:00" data-subject="">

<img src="/images/smilies/icon_eek.svg" alt=":shock:" title=":shock:" width="15" height="15" class="smiley nozoom"> OMG the sky is blue???

</div>

<div class="post" data-post-id="17523" data-author="Marchessa_red_witch" data-date="2007-03-27T17:57:14+00:00" data-subject="Obviously">

> <strong>Weasel wrote:</strong>
> <img src="/images/smilies/icon_eek.svg" alt=":shock:" title=":shock:" width="15" height="15" class="smiley nozoom"> OMG the sky is blue???

You haven't been to China much recently, the sky isn't often blue in the major cities.

</div>

<div class="post" data-post-id="17525" data-author="Autolycos" data-date="2007-03-27T18:14:43+00:00" data-subject="Re: Obviously">

> <strong>Marchessa\_red\_witch wrote:</strong>
> You haven't been to China much recently, the sky isn't often blue in the major cities.

Marchessa messages are typically boring, cryptic, and often undecypherable snippets of geek code that are used to inform another mudder that he or she has screwed something up. Often, this is completely and incorrectly viewed as the fault more often than not, that it lies with the immorts for failing to check said codes on his or her reports, and or had been checked, doublechecked, signed in triplicate, sent in, sent back, queried, lost, found, subjected to public inquiry, lost again, and finally buried in soft peat and recycled as firelighters.

"Of course," the Guide continues, "at this point you are left with only two options. (Two if you suddenly, and for no good reason whatsoever, decide to irritate a mudder by feeding his or her grandmother to the Ravenous Bugblatter Beast of Traal.)

"Your first option: Panic, which as we all know is not entirely always a good idea.

RIP (c) Douglas Adams

</div>

<div class="post" data-post-id="17532" data-author="Mosaix" data-date="2007-03-27T18:40:28+00:00" data-subject="">

Marchessa's answer to the sky is blue, truly sums it up.

She's not really evil, just dont let her read any poetry to you....avoid the poetry at all costs, its he 3rd worst in the galaxy.

No, no no, the presidental prisoner release form is blue....this is a regular prisoner release form.....

Mosaix

</div>

<div class="post" data-post-id="17533" data-author="Weasel" data-date="2007-03-27T19:12:31+00:00" data-subject="">

bloody Vogons...

</div>

<div class="post" data-post-id="17534" data-author="Autolycos" data-date="2007-03-27T20:17:03+00:00" data-subject="">

It was only then that we realized that marchessa was a dreadful shade of burnt umber and that she was hanging gracefully mid air in the very same way that bricks don't....

</div>

<div class="post" data-post-id="17535" data-author="Medios" data-date="2007-03-27T21:01:39+00:00" data-subject="">

To put it simply. Most of the smart mudders knew about this years ago. It is not a bug, its a feature. A long time ago mobs would do nothing if you dispelled them. This slap and attack proc was put in to keep players on their toes. You cannot just go in and spam 100 dispels and the backstab. Now you need to pay attn or write a bot script to mud for you.

Mike

</div>

<div class="post" data-post-id="17538" data-author="12345" data-date="2007-03-27T21:33:58+00:00" data-subject="">

In other news, I've discovered that you can put stuff in your robe and wear it. This is great, because it allows you to pick up more stuff! I picked up all kinds of stuff today... like iron rations, regen gear, Auto's viginity, and cps! They're in my robe! I even wrote a script to take things out of my robe and wear them, and put other stuff in the robe! I've found this makes the game much easier. The imms should take a look at this.

I think we can let this die...

</div>

<div class="post" data-post-id="17541" data-author="13" data-date="2007-03-27T22:32:53+00:00" data-subject="">

You guys rock <img src="/images/smilies/icon_e_smile.svg" alt=":)" title=":)" width="15" height="15" class="smiley nozoom">

</div>

<div class="post" data-post-id="17547" data-author="Weasel" data-date="2007-03-27T23:26:08+00:00" data-subject="">

<img src="/images/smilies/icon_eek.svg" alt=":shock:" title=":shock:" width="15" height="15" class="smiley nozoom"> You can put stuff in your robe??? AND the sky is blue??? This is all just a little too much for me to take in one day - I think I'd better find some nice quiet corner and go whimper in it for a while.

</div>

<div class="post" data-post-id="17551" data-author="alias" data-date="2007-03-28T00:07:55+00:00" data-subject="">

No way you found Auto's virginity, I took that from him a long time ago.

</div>

<div class="post" data-post-id="17552" data-author="Gimlet" data-date="2007-03-28T01:30:29+00:00" data-subject="">

hey marchessa wrote scripts to travel back in time to chop in 1984 before choppers even existed, who are we to argue with her?

on another note, why the hell do ppl need to be informed of the continent and area they are in via their prompt? If u can't even remember what area/continent you're on, maybe you have bigger issues than mobs hating your guts

</div>

<div class="post" data-post-id="17560" data-author="banedon" data-date="2007-03-28T03:35:44+00:00" data-subject="">

> <strong>Gimlet wrote:</strong>
> on another note, why the hell do ppl need to be informed of the continent and area they are in via their prompt?

The one reason I can think of is the occasional transcontinental group that forms sometimes during a fargate. It can get a lil confusing after the 4th or 5th intercontinental convo.

Just my $.02, flame away

</div>

<div class="post" data-post-id="17562" data-author="Gimlet" data-date="2007-03-28T04:37:06+00:00" data-subject="">

yeah, but is that information so vital u need to know every single round which continent you are on?

</div>

<div class="post" data-post-id="17563" data-author="Weasel" data-date="2007-03-28T04:52:16+00:00" data-subject="">

hmm.. I guess you could log that info and extract a list of the room names and corresponding areas, which could come in very handy when trying to locate eq, spellbooks etc...

</div>

<div class="post" data-post-id="17568" data-author="13" data-date="2007-03-28T12:57:08+00:00" data-subject="">

Mosaix wins though.

</div>

<div class="post" data-post-id="18289" data-author="freakna" data-date="2007-05-04T18:35:42+00:00" data-subject="">

Well personaly I love knowing where I am. I don't know why but I seem to take the wrong turn all the time and I end up in some realy stupid places. Or ill phase door or cast 'fortune' and get teleported somewhere. Yep, that was funny. Buffing up for battle. About to go in.. The next thing I new a dragon was eating me. Where did all the zombie's go? Oh shit! So yes very usful for asking for a sos.

</div>

<div class="post" data-post-id="18290" data-author="Gimlet" data-date="2007-05-05T00:36:06+00:00" data-subject="">

> <strong>freakna wrote:</strong>
> Well personaly I love knowing where I am. I don't know why but I seem to take the wrong turn all the time and I end up in some realy stupid places. Or ill phase door or cast 'fortune' and get teleported somewhere. Yep, that was funny. Buffing up for battle. About to go in.. The next thing I new a dragon was eating me. Where did all the zombie's go? Oh shit! So yes very usful for asking for a sos.

That's coz you're a friggin noob

</div>

<div class="post" data-post-id="18292" data-author="13" data-date="2007-05-05T14:46:32+00:00" data-subject="">

if you didxnt mud from a goddamn palm pilot or sidekick or something you might know where you were

stupid

</div>
