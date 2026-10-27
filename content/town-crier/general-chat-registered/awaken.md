---
title: "Awaken"
topic_id: 1586
author: "Rynquald"
date: 2005-12-04T11:11:41+00:00
last_activity: 2005-12-20T22:46:57+00:00
last_author: "kjartan"
sticky: false
locked: false
post_count: 25
---

<div class="post" data-post-id="9730" data-author="Rynquald" data-date="2005-12-04T11:11:41+00:00" data-subject="Awaken">

I might be wrong (it is rather late after all), but i think awaken is slightly bugged, it gves the message "You aren't powerful enough to awaken that kind of plant ... yet." upon trying to awaken 1 slime mold with my prime char (ma/dr/wa/cl lev 9 av).

Guess it could be the help file that's wrong though, not the spell. Thanks for awaken btw, and I'm really not complaning <img src="/images/smilies/icon_e_smile.svg" alt=":)" title=":)" width="15" height="15" class="smiley nozoom">

</div>

<div class="post" data-post-id="9731" data-author="Grue" data-date="2005-12-04T14:28:21+00:00" data-subject="">

Nope you are wrong, read the help file again. It works the same as supplication, ieit counts you level starting with druid. a level 9 avatar dr/cl/ma/wa is a 4x40 beacuse dr is the first class. A level 9 avatar ma/dr/cl/wa is only a 3x40 because the prime class doesn't count, likewise a level 9 avatar ma/cl/dr/wa is a double 40. You'll be able to get a slime mold at level 40 avatar (when you have 4x40 starting with your secondary class) and will never be able to get the last one.

</div>

<div class="post" data-post-id="9732" data-author="Guinex" data-date="2005-12-04T19:17:14+00:00" data-subject="">

Looks to me that slime mold is not the last awaken mob, and should be able to get at your level....

</div>

<div class="post" data-post-id="9734" data-author="Leaf" data-date="2005-12-04T19:56:41+00:00" data-subject="">

3x40 Druid prime here, and can't awaken slime mold.

Also it's interesting that you would need to be located in a forest area.

</div>

<div class="post" data-post-id="9735" data-author="Rynquald" data-date="2005-12-04T20:31:29+00:00" data-subject="">

Thanks for the replys. And that was my point Grue, while my prime class doesn't count so i'm only 3x40 for this, slime mold's a 3x40 mob according to the help file...

</div>

<div class="post" data-post-id="9736" data-author="kjartan" data-date="2005-12-04T23:39:30+00:00" data-subject="">

Ok, there was a bug that was preventing anything higher than 1x40 from being awakened, should be fixed next crash or reboot.

Also, 'order followers' didn't work while shifted even on awakened plants, that also is fixed next crash or reboot. Until then you will just have to order them by name.

And, I added 'order plants' so you can order just your plants in case you have other stuff following you as well.

Oh, and one more druid thing: I have changed it so that instead of dropping into your inventory, any equipment you are wearing when you shift is just incorporated into your form. It will return in the same equipped slot when you shift back. It doesn't do anything for you while you're shifted. (Excepting shiftable equipment, which still behaves as it always did).

</div>

<div class="post" data-post-id="9738" data-author="Pine" data-date="2005-12-05T02:25:50+00:00" data-subject="">

Oh, and one more druid thing: I have changed it so that instead of dropping into your inventory, any equipment you are wearing when you shift is just incorporated into your form. It will return in the same equipped slot when you shift back. It doesn't do anything for you while you're shifted. (Excepting shiftable equipment, which still behaves as it always did).

This is awesome, thanks.

</div>

<div class="post" data-post-id="9739" data-author="Grue" data-date="2005-12-05T05:03:43+00:00" data-subject="">

My mistake sorry, for some reason I read the help file as 4x40 not 3x40. Apologies.

Anyone have any feedback on how good the forms are?

</div>

<div class="post" data-post-id="9740" data-author="Rynquald" data-date="2005-12-05T05:37:27+00:00" data-subject="">

No worries. I've tried all the up to 1x40 forms and they seem pretty weak in general, but alowing that they could be used by a 1x40 druid prime they're nice, nice enough that the slime molds and elder ents will probably be usefull anyway.

Edit: Now that I've tested slime molds, i must say, awaken rocks <img src="/images/smilies/icon_e_smile.svg" alt=":)" title=":)" width="15" height="15" class="smiley nozoom">

</div>

<div class="post" data-post-id="9741" data-author="kjartan" data-date="2005-12-06T04:34:13+00:00" data-subject="">

Ok, I have made it so undead control doesn't affect awakened critters, and also I have made awaken work in rooms with either a hedge maze or a spring (from the garden spell). Changes in next crash or reboot.

</div>

<div class="post" data-post-id="9855" data-author="Shara" data-date="2005-12-18T08:30:50+00:00" data-subject="">

Are there differences in order lag? Do prime druids get one round of lag and all others get two, like necro and their undead?

</div>

<div class="post" data-post-id="9858" data-author="kjartan" data-date="2005-12-18T19:36:23+00:00" data-subject="">

Right now, the lag distribution isn't great, so let me just say how it will be after the next crash or reboot: you will get one round of order lag if you are ordering stuff controlled through your prime class (undead for necros, plants for druids, charms and fams for mages, supps for clerics) and two rounds if you are ordering anything else.

Edit: I just realized that I got them backwards when I made this change. It will work like I say above after next crash or reboot.

</div>

<div class="post" data-post-id="9861" data-author="Shara" data-date="2005-12-18T23:51:27+00:00" data-subject="">

Okies, thanks for clarification <img src="/images/smilies/icon_e_smile.svg" alt=":)" title=":)" width="15" height="15" class="smiley nozoom">

</div>

<div class="post" data-post-id="9873" data-author="Deju" data-date="2005-12-19T21:01:23+00:00" data-subject="Re: Order Lag">

Since this new change has gone in, i have noticed an increase in my order lag for summons and juju. I dont think its 2 full rounds, but it definitely seems longer than 1 round.

I have talked to a couple other necro primes and they have noticed the same thing.

Would you mind taking a quick look at this please?

Thanks,

Deju/Scrugg

Edit: Ahh, i just noticed Kjartan's edit on his post. Thanks Kj! <img src="/images/smilies/icon_e_smile.svg" alt=":)" title=":)" width="15" height="15" class="smiley nozoom">

</div>

<div class="post" data-post-id="9875" data-author="kjartan" data-date="2005-12-20T01:16:13+00:00" data-subject="Re: order lag">

A further change: I cut the lag for familiars in half, because they're so small (based on Wasp's suggestion). So, 1 round for non-mage-primes, half a round for mage-primes. Also in next crash or reboot.

</div>

<div class="post" data-post-id="9876" data-author="Avatar" data-date="2005-12-20T13:47:30+00:00" data-subject="Order Lag">

This makes sense, and at a "tactical" level definitely seems more logical than the old methods of order lag. So I do think it's an improvement.

I still question the "strategic" decision to doubling the lag on non-prime followers. Lag is one of the worst things about playing muds in general. Games should be interactive. Again speaking generally, I've seen other games where certain powerful skills would have a cool-down time, but the character could still do other things.

Speaking more sloth-specific, it seems silly to look at a Wa/Ma vs. a Wa/Ne. The strongest necro ability is to summon undead. Not only does a secondary necro not get juju but also apparently he'll always have less powerful undead followers than a necro prime (even at avatar levels). In addition to that, all of his followers have twice the lag time. The Wa/Ma on the other hand gets all the blasting capability of a Mage prime except for the extra +20 spelldamage cap.

In short, I think the necro followers for non-necro prime characters have already been weakened quite a bit from the overbalancing feature they once were. Especially if the undeads available have been changed recently to follow the class structure like Supplication was built. 

In short, I have two points that I'd like to make:

1\) I have always loved Sloth's multiclass levelling system. I mean, the original system where getting a level 36 in your quad class gave you similar skills / spells as a 36 in any of your other classes (triple attack or firewind or whatever). That reflects a certain philosophy where, with enough practice, a person can become skilled in several classes. The prime-only skills and eq were a step away from that original system, and I have learned to accept those. Some recent changes are further steps from the original system. Specifically the reduced capabilities of supplication and summon / animate as your casting class moves down the classo. I wonder if a character with necromancer quad will ever use the summon capabilities of his class if the strongest undead he'll get will be a zombie or whatever. Compare that to a mage quad that still gets firewind (and frostbolt) or a cleric quad that still gets restoration and raise dead. 

2\) Going back to the lag issue, I'll always argue against inducing lag to players. It's simply frustrating and annoying to be lagged for two rounds. For me, at least, it ruins any fun I normally get while playing. I'm sure that there are other methods to balance followers without adding lag times.

</div>

<div class="post" data-post-id="9877" data-author="12345" data-date="2005-12-20T14:38:27+00:00" data-subject="">

I once played a game that had spell lag. Interesting concept, it prevented you from casting spells, but you could still recall, chat and such. It wasn't too bad to play, but the feature still gives me nightmares. The coder that designed it got married and quit, and I inheritted it because no one else could figure out how to work with it. Granted, it was implemented very poorly, but I swear the tangle of code involved with it was simply scary.

I won't comment on mages until they're done being retooled <img src="/images/smilies/icon_e_smile.svg" alt=":)" title=":)" width="15" height="15" class="smiley nozoom">

</div>

<div class="post" data-post-id="9879" data-author="Driven" data-date="2005-12-20T14:58:07+00:00" data-subject="">

Avatar, I don't think you can equate 2 rounds of lag with not having firewind. Yes, a non-prime necro gets 2 rounds of lag, but you still have a swordwraith. Now I do concede that being a non-prime mage leaves you with no drawbacks when using firewind, but I don't think the answer is to give power back to non-prime necros by removing the lag. I think the correct answer would be increased mana requirements for non-prime mage (or conversely decreased mana requirements for prime mage). I don't have a mage prime, so I don't know if this already exists? Do prime mages cast firewind for less mana? 

I know for a fact that my cleric prime casts restoration with less mana (as Avatar should know also). And so you can't equate non-prime restoration with prime restoration. Is 7 less mana on restoration equal to a round of lag? Hard to say, but I have zero pity for a warrior prime with parry, wraithform, and a swordwraith in-toe that takes 2 rounds of lag to order around.

Another suggestion might be to have a graduated scale of lag. Necro prime has 1 round of lag, secondary/tert has 1.5 rounds, and necro quad has 2 rounds. Shrug. Don't listen to me, my Sloth brain is rotted after being gone for a year <img src="/images/smilies/icon_e_smile.svg" alt=":)" title=":)" width="15" height="15" class="smiley nozoom">

rob

</div>

<div class="post" data-post-id="9881" data-author="Dariel" data-date="2005-12-20T15:20:21+00:00" data-subject="Re: Order Lag">

> <strong>Avatar wrote:</strong>
> In short, I have two points that I'd like to make:
> 
> 
> 
> 1\) I have always loved Sloth's multiclass levelling system. I mean, the original system where getting a level 36 in your quad class gave you similar skills / spells as a 36 in any of your other classes (triple attack or firewind or whatever). That reflects a certain philosophy where, with enough practice, a person can become skilled in several classes. The prime-only skills and eq were a step away from that original system, and I have learned to accept those. Some recent changes are further steps from the original system. Specifically the reduced capabilities of supplication and summon / animate as your casting class moves down the classo. I wonder if a character with necromancer quad will ever use the summon capabilities of his class if the strongest undead he'll get will be a zombie or whatever. Compare that to a mage quad that still gets firewind (and frostbolt) or a cleric quad that still gets restoration and raise dead. 
> 
> 
> 
> 2\) Going back to the lag issue, I'll always argue against inducing lag to players. It's simply frustrating and annoying to be lagged for two rounds. For me, at least, it ruins any fun I normally get while playing. I'm sure that there are other methods to balance followers without adding lag times.

I agree with Avatar on these two points.

</div>

<div class="post" data-post-id="9886" data-author="kjartan" data-date="2005-12-20T17:15:08+00:00" data-subject="">

I guess we could charge mana per order instead of lag. It would probably be a lot, because you don't order them to do stuff that often; it would certainly be more than the mana you can regen in the current lag time. Probably it wouldn't be so much for familiars. I'll talk to the other imms about it.

</div>

<div class="post" data-post-id="9888" data-author="Avatar" data-date="2005-12-20T20:15:54+00:00" data-subject="Classo&#x27;s">

Driven: "Hard to say, but I have zero pity for a warrior prime with parry, wraithform, and a swordwraith in-toe that takes 2 rounds of lag to order around."

I haven't seen first-hand, but I think the necro summon / animate was recently changed to take into consideration the classo of the necro, similar to the way supplication uses the classo of the cleric class. If so, only necro primes would get a swordwraith. A character would get less powerful undead followers as his necro class moves from 1st \> 2nd \> 3rd \> 4th. I'm not aware which undeads each of these can summon. 

So, the necro non-prime has: no juju, lower types of summons, lower undead control gear cap, and 2 rounds of order lag. To me, that means I either play a necro prime (for the undead) or necro non-prime (for wraithform/spectral and never summon).

I'm not saying that I know what the answers are, but perhaps the undead followers have already been tweaked enough that they are not the overpowering force that they once were. If not, maybe they can find other ways to balance them rather than the induced lag. Kjartan suggested one method, maybe we can find others.

Driven: "I think the correct answer would be increased mana requirements for non-prime mage (or conversely decreased mana requirements for prime mage)."

That's kind of the opposite of my point. I'm saying that the difference between having a class 1st, 2nd, 3rd, 4th in a classorder should be limited. I hope the strategic direction for the mud is to emulate the way the mage class currently is (smaller difference based on classo) rather than the way necro currently is (larger difference based on classo). The penalty for having a class chosen later in the classo should be reflected in the xps / coins / time it takes to level. If I just paid 900 million for 40 in a quad class, I would prefer to have similar capabilities that a prime character got for 40 million. It took me longer to get there, but "there" should be the nearly the same.

Supplication doesn't adhere to that strategy, but it was easy to overlook because it's a relatively minor ability compared to the healing spells. A cleric quad can sometimes get a peri follower, and order lag doesn't apply because you don't order them to heal you. Undeads are arguably the major ability for necromancers. If the cleric class had been implemented the way necro undeads work, only cleric primes would get restoration. Then as you moved down the classo secondary clerics would get greater heal, tertiary clerics would get heal, and cleric quads would only have cure critical. 

I'm trying to point out that these reduced capabilities based on class order make Sloth ultimately less fun. (For me, anyway. I'm just posting this as an opinion.)

</div>

<div class="post" data-post-id="9889" data-author="Rynquald" data-date="2005-12-20T20:16:29+00:00" data-subject="">

> <strong>Quote:</strong>
> I guess we could charge mana per order instead of lag. It would probably be a lot, because you don't order them to do stuff that often; it would certainly be more than the mana you can regen in the current lag time. Probably it wouldn't be so much for familiars. I'll talk to the other imms about it.

You see, this is \*exactly\* the kind of thing that happens when people complain about things like ordering followers without considering how it could be worse <img src="/images/smilies/icon_e_smile.svg" alt=":)" title=":)" width="15" height="15" class="smiley nozoom"> (well, it's worse than lag imho)

</div>

<div class="post" data-post-id="9890" data-author="kjartan" data-date="2005-12-20T20:29:10+00:00" data-subject="">

To the extent we have a strategic direction, it is that there should not be many major differences in class abilities as a function of its position in the classo. We have a few prime-only skills and spells, and we aren't planning on adding any more. We are more willing to depower non-prime classes by changing numerical limits like caps and such.

</div>

<div class="post" data-post-id="9891" data-author="12345" data-date="2005-12-20T21:30:59+00:00" data-subject="">

Hmm. I'm not a necro, so I'm not sure what to think about the statement about the lower undeads and no Juju. My thinking seems to change on it depending on whether I think of the Juju as an undead or as prime ability. As an undead, it's a major decrease in power. As a prime ability... well, it's their major prime ability. You can't really adjust for it without reducing the value of the Juju.

I have seen plenty of folks with necro in 3rd and 4th that appear to be sucessful with it... so I'll shut up now...

</div>

<div class="post" data-post-id="9892" data-author="kjartan" data-date="2005-12-20T22:46:57+00:00" data-subject="Re: order lag">

After some discussion among the immortals, we have decided to leave order lag as it is now.

While poking around in the code regarding this, I noticed that rapid shift is semi-broken, in that there is a bug in the code so that it fails to check for it when you 'shape return'. I'll fix that tonight. Ditto for battle shift.

</div>
