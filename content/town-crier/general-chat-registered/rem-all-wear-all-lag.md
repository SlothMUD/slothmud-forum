---
title: "Rem All / Wear All lag"
topic_id: 2645
author: "Yasik"
date: 2007-11-22T04:41:37+00:00
last_activity: 2007-12-31T13:51:16+00:00
last_author: "Alberich"
sticky: false
locked: false
post_count: 52
---

<div class="post" data-post-id="21367" data-author="Yasik" data-date="2007-11-22T04:41:37+00:00" data-subject="Rem All / Wear All lag">

Does anyone exept me suffer a \~2-3 sec lag after these commands?

In case that was put by coders on purpose, will there be a skill or something that reduces the lag?

</div>

<div class="post" data-post-id="21369" data-author="jezer" data-date="2007-11-22T05:21:31+00:00" data-subject="">

It's your brain trying to catch up with the computer. Try using pen and paper.

</div>

<div class="post" data-post-id="21372" data-author="Teron" data-date="2007-11-22T13:20:09+00:00" data-subject="">

\- sadly, this isn't Yasik's hallucination

\- I'd appreciate an absense of lag in the spirit of making the game tolerable to play, though. Having a skill or a payment to remove the lag doesn't make sense, though, unless yer a vampiric stripper, maybe.

</div>

<div class="post" data-post-id="21374" data-author="Weasel" data-date="2007-11-22T16:12:04+00:00" data-subject="">

Yeah noticed it too. As far as I can tell, it serves no purpose whatsoever other than to annoy.

</div>

<div class="post" data-post-id="21376" data-author="Malison" data-date="2007-11-22T18:57:58+00:00" data-subject="">

\*conjecture\*

Guessing it's a return to the ridiculous 'realism' idea brought up awhile back (I believe originally used by Kjartan) - it \*would\* take longer to take all your stuff off than any individual piece. Of course, we aren't here for realism, and it's a nuisance <img src="/images/smilies/icon_e_sad.svg" alt=":(" title=":(" width="15" height="15" class="smiley nozoom">

</div>

<div class="post" data-post-id="21377" data-author="Vixn" data-date="2007-11-22T19:33:26+00:00" data-subject="">

hm concerning 'real' realism... bring my other eight fngers back, please

 <img src="/images/smilies/icon_cool.svg" alt="8)" title="8)" width="15" height="15" class="smiley nozoom">

</div>

<div class="post" data-post-id="21378" data-author="Weasel" data-date="2007-11-22T19:41:14+00:00" data-subject="">

> <strong>Vixn wrote:</strong>
> hm concerning 'real' realism... bring my other eight fngers back, please
> 
> 
> 
> <img src="/images/smilies/icon_cool.svg" alt="8)" title="8)" width="15" height="15" class="smiley nozoom">

lol yeah, bring it! would solve all my AC concerns, hehe.

</div>

<div class="post" data-post-id="21380" data-author="Liar" data-date="2007-11-22T22:14:04+00:00" data-subject="">

Though that 'wear all lag' is really annoying, and realisim is not what we really need in game, yet from the point of realism i cant agree with you Vixn. Are all of your fingers exactly same? Rings probably considered to being same size, thats why you wear one for each hand.

</div>

<div class="post" data-post-id="21381" data-author="Yasik" data-date="2007-11-22T23:52:22+00:00" data-subject="">

Poor newbie druids, who ever will try to use shiftable eq...

W/o Rapid shift (which is kinda tricky to get learned in addition to 50 drachma per sb!) and w/o Shapeshift Mastery (which is needed to get to those levels) is would be a real pain...

</div>

<div class="post" data-post-id="21383" data-author="Teron" data-date="2007-11-23T08:15:22+00:00" data-subject="">

You can wear rings on 6 out of 10 \*hand\* fingers. If you try hard, you can wear on 8/10 or even on leg fingers, ankles, some stuff on bisceps and stuff. 

I don't think its for realism, prolly just to hurt someone taking advantage of their regen gear, esp fast aliases that takes great skill to write.

</div>

<div class="post" data-post-id="21384" data-author="Weasel" data-date="2007-11-23T08:38:57+00:00" data-subject="">

I'm an old school Warrior prime - our natural running regen absolutely sucks so we regularly have to stop and change eq to regen. The lag is really only minor and lasts just a few extra seconds, but somehow it annoyed the shit out of me enough tonight that I rented.

Again, would some immort kindly explain what the point of that lag is? Or is there some problem with the server that can't handle that much info going through at once and throttles it.. which I doubt.

</div>

<div class="post" data-post-id="21388" data-author="13" data-date="2007-11-23T15:04:19+00:00" data-subject="">

is this thread for real?

</div>

<div class="post" data-post-id="21389" data-author="Weasel" data-date="2007-11-23T15:17:01+00:00" data-subject="">

> <strong>13 wrote:</strong>
> is this thread for real?

no, it isn't, now just shut up and bend over.

 <img src="/images/smilies/icon_twisted.svg" alt=":twisted:" title=":twisted:" width="15" height="15" class="smiley nozoom">

</div>

<div class="post" data-post-id="21409" data-author="Judge" data-date="2007-11-25T16:32:18+00:00" data-subject="">

Apologies for not communicating the details of this change earlier, here are some details if you haven't already figured it out. - Judge

The logic is quite simple and has nothing to do with realism as several players have mentioned, but is has all to do with balance:

1\. Previously "remove all" and "wear all" could be done with 0 wait state. you could essentially change all your eq 5x in 5 seconds.

2\. Previously "remove item" and "wear item" caused huge lag, and cumulatively was extremely painful.

3\. Now - All items have an equal wait time whether removed as a single item or removed en-masse. E.g. curse 10 items, and remove all will remove 8 items with the same wait state as removing those same 8 items individually. 

4\. Now - the wait times are more balanced over all, slightly higher for "all", BUT for single item removal/wearing the times have been significantly reduced.

Remember not all players have the luxury of being able to removal all \& wear all. Yes there will need to be some rejigging of some peoples change eq scripts to improve the speed of eq change. i.e. as a general rule where you have currently used remove all, the needs to be replaced with an explicit remove \<item\> for each item you wish to replace. Wear all wont need to be refined.

PS keep an eye out for various techniques that could speed up eq change. The first that should arrive is the "brownie" from supplication.

<strong>OLD wait states for wear/remove</strong>

For changing all equipment

 {0, 0} - wear/remove all

and for individual items

 {1, 4} LIGHT

 {4, 4} FINGER\_R

 {4, 4} FINGER\_L

 {8, 8} NECK\_1

 {8, 8} NECK\_2

 {12, 12} BODY 

 {6, 8} HEAD

 {12, 12} LEGS

 {12, 12} FEET

 {6, 8} HANDS

 {12, 12} ARMS

 {12, 12} SHIELD

 {12, 12} ABOUT

 {12, 12} WAISTE 

 {4, 4} WRIST\_R

 {4, 4} WRIST\_L

 {5, 4} WIELD

 {1, 4} HOLD

 {135, 144} = TOTAL for 18 items

approximately 34seconds, 36seconds (for 18 items)

<strong>NEW wait states for all types of wear/remove</strong>

 {0, 0} LIGHT

 {1, 1} FINGER\_R

 {1, 1} FINGER\_L

 {2, 1} NECK\_1 

 {2, 1} NECK\_2

 {3, 1} BODY

 {1, 1} HEAD

 {2, 1} LEGS

 {2, 1} FEET

 {1, 1} HANDS

 {2, 1} ARMS

 {2, 1} SHIELD

 {2, 1} ABOUT 

 {2, 1} WAISTE

 {1, 1} WRIST\_R

 {1, 1} WRIST\_L

 {1, 0} WIELD

 {0, 0} HOLD

 {26, 15} = TOTAL for 18 items

approximately 6seconds, 4seconds (for 18 items)

</div>

<div class="post" data-post-id="21410" data-author="Weasel" data-date="2007-11-25T16:51:50+00:00" data-subject="">

Thanks for the explanation. Probably not possible, but is there any way concise / brief can still cut out all the eq change spam when players are using item by item eq changes rather than remove all / wear all?

</div>

<div class="post" data-post-id="21411" data-author="van" data-date="2007-11-25T18:32:47+00:00" data-subject="">

My apologies if I sound a little pissy; I'll blame it partly on quitting smoking (one week cigarette free!). But mainly, I can't for the life of me see how this improves the game, either for the players or for the "balance" we're apparently going for here. There's been a lot of really awesome changes going in lately, for which I've been really grateful.

But at a time of declining player base, is it really necessary to put in such a truly annoying change that (to this player at least) has no positive material effect on the game?

Perhaps someone can answer the questions below.

> <strong>Judge wrote:</strong>
> The logic is quite simple and has nothing to do with realism as several players have mentioned, but is has all to do with balance:

Ok, I'm seriously confused. Is there some character out there who has been accumulating drachma in the tens of thousands, running 50 mil coins an hour, and getting 5x40 in a day because they changed their equipment too fast? Hyperbole aside, what was the "unbalance" that required this?

> <strong>Quote:</strong>
> Remember not all players have the luxury of being able to removal all \& wear all.

Um, what? Someone want to fill me in on this? Is wear all/remove all now a class-specific command? 

If balance is the issue, why not just remove all lag from eq changes? Or, taking this to the next logical step, shouldn't there be lag from taking objects out of sacks? I mean, it takes a while to find something in a golden sack right? Then this would "balance" the people who use take all/get all from containers vs. the people who spam the group with 36 put/get commands (it's fun, try it). I spend loads more time changing eq than the people who use get all/wear all. It's not because I'm too lazy to write scripts, it's clearly unbalanced!

> <strong>Quote:</strong>
> i.e. as a general rule where you have currently used remove all, the needs to be replaced with an explicit remove \<item\> for each item you wish to replace.

makes no sense with

> <strong>Quote:</strong>
> Now - All items have an equal wait time whether removed as a single item or removed en-masse.

If the items have an equal wait time (or slightly higher for all), why bother changing our scripts at all? We can spam people even more for a 2 ms gain?

I think I go balance myself at work. But as a parting note, in the ss group last night, I counted over 50 references from players to how irritating the new lag was. Perhaps some of those players can more politely explain their irritation than I can.

Oh, and if you smoke, I hope you die of lung cancer. (Well, not really, I just hate you right now :)) 

Patrick

</div>

<div class="post" data-post-id="21412" data-author="Weasel" data-date="2007-11-25T18:42:24+00:00" data-subject="">

Good luck with the giving up smoking d00d - I went cold turkey and stopped 3 years ago without so much as a puff since (I was near a packet a day for a long time prior to that). The worst part is when you're out socially like at a pub or something, or stressed a bit and needing that 5 minute break.. 

Again, good luck, it ain't easy, but the longer you go without, the easier it gets. I started chewing gum for a while as a distraction which helped in those early stages and the rough patches. Expect to put on some weight too.

The good news is that you'll save a sh\*tload of money - well, if you live in NYC you do anyway, where it was over $10 a pack 3 years ago, and apparently near $15 a pack now..

p.s. the eq change spam in groups is going to get ridiculous, which is why I mentioned tweaking the concise / brief commands somehow, but I doubt anything can be done there.

</div>

<div class="post" data-post-id="21413" data-author="Vixn" data-date="2007-11-25T20:04:01+00:00" data-subject="">

> <strong>van wrote:</strong>
> ...whines skipped.... 
> 
> 
> 
> shouldn't there be lag from taking objects out of sacks?
> 
> 
> 
> Patrick

great idea! I'll put another one ---\> non-caster classoes could have some troubles with recite recalls. Like they started to recite, got wrong and have to start from the beginning. Just for 'balance' sake.

 <img src="/images/smilies/icon_cool.svg" alt="8)" title="8)" width="15" height="15" class="smiley nozoom">

</div>

<div class="post" data-post-id="21416" data-author="alias" data-date="2007-11-26T01:10:14+00:00" data-subject="">

Don't make me think on the mud, everyone knows I'm not good at it and I come here to relax not rack my brain how to recite a recall, change eq the fastest, or sort stuff in my bag.

realism is for those who don't get enough of that sort of thing in real life.

I come here for fantasy.

Alias

</div>

<div class="post" data-post-id="21418" data-author="Yinao" data-date="2007-11-26T13:47:22+00:00" data-subject="">

> <strong>Quote:</strong>
> Yes there will need to be some rejigging of some peoples change eq scripts to improve the speed of eq change.

Horsecock I will just spam the group for an extra 4 seconds or wtf ever it is and they can wait 4 seconds longer

 <img src="/images/smilies/icon_rolleyes.svg" alt=":roll:" title=":roll:" width="15" height="15" class="smiley nozoom"> <img src="/images/smilies/icon_rolleyes.svg" alt=":roll:" title=":roll:" width="15" height="15" class="smiley nozoom"> <img src="/images/smilies/icon_rolleyes.svg" alt=":roll:" title=":roll:" width="15" height="15" class="smiley nozoom"> <img src="/images/smilies/icon_rolleyes.svg" alt=":roll:" title=":roll:" width="15" height="15" class="smiley nozoom"> <img src="/images/smilies/icon_rolleyes.svg" alt=":roll:" title=":roll:" width="15" height="15" class="smiley nozoom"> <img src="/images/smilies/icon_rolleyes.svg" alt=":roll:" title=":roll:" width="15" height="15" class="smiley nozoom"> <img src="/images/smilies/icon_rolleyes.svg" alt=":roll:" title=":roll:" width="15" height="15" class="smiley nozoom"> <img src="/images/smilies/icon_rolleyes.svg" alt=":roll:" title=":roll:" width="15" height="15" class="smiley nozoom"> <img src="/images/smilies/icon_rolleyes.svg" alt=":roll:" title=":roll:" width="15" height="15" class="smiley nozoom"> <img src="/images/smilies/icon_rolleyes.svg" alt=":roll:" title=":roll:" width="15" height="15" class="smiley nozoom"> <img src="/images/smilies/icon_rolleyes.svg" alt=":roll:" title=":roll:" width="15" height="15" class="smiley nozoom"> <img src="/images/smilies/icon_rolleyes.svg" alt=":roll:" title=":roll:" width="15" height="15" class="smiley nozoom"> <img src="/images/smilies/icon_rolleyes.svg" alt=":roll:" title=":roll:" width="15" height="15" class="smiley nozoom"> <img src="/images/smilies/icon_rolleyes.svg" alt=":roll:" title=":roll:" width="15" height="15" class="smiley nozoom"> <img src="/images/smilies/icon_rolleyes.svg" alt=":roll:" title=":roll:" width="15" height="15" class="smiley nozoom"> <img src="/images/smilies/icon_rolleyes.svg" alt=":roll:" title=":roll:" width="15" height="15" class="smiley nozoom"> <img src="/images/smilies/icon_rolleyes.svg" alt=":roll:" title=":roll:" width="15" height="15" class="smiley nozoom"> <img src="/images/smilies/icon_rolleyes.svg" alt=":roll:" title=":roll:" width="15" height="15" class="smiley nozoom"> <img src="/images/smilies/icon_rolleyes.svg" alt=":roll:" title=":roll:" width="15" height="15" class="smiley nozoom"> <img src="/images/smilies/icon_rolleyes.svg" alt=":roll:" title=":roll:" width="15" height="15" class="smiley nozoom"> <img src="/images/smilies/icon_rolleyes.svg" alt=":roll:" title=":roll:" width="15" height="15" class="smiley nozoom"> <img src="/images/smilies/icon_rolleyes.svg" alt=":roll:" title=":roll:" width="15" height="15" class="smiley nozoom"> <img src="/images/smilies/icon_rolleyes.svg" alt=":roll:" title=":roll:" width="15" height="15" class="smiley nozoom"> <img src="/images/smilies/icon_rolleyes.svg" alt=":roll:" title=":roll:" width="15" height="15" class="smiley nozoom"> <img src="/images/smilies/icon_rolleyes.svg" alt=":roll:" title=":roll:" width="15" height="15" class="smiley nozoom">

</div>

<div class="post" data-post-id="21420" data-author="13" data-date="2007-11-26T15:32:02+00:00" data-subject="">

it's kind of gay, but I don't think it makes much of a difference.

I'm behind this statement:

> <strong>Quote:</strong>
> I come here for fantasy.

</div>

<div class="post" data-post-id="21423" data-author="Vixn" data-date="2007-11-26T19:49:45+00:00" data-subject="">

> <strong>alias wrote:</strong>
> I come here for fantasy.
> 
> Alias

last player fantasy

Fantasy's last logon was Sun Sep 9 12:13:31 2007

[ 1w 0d 0o 0t] Fantasy the Untitled

Sorry, she's busy right now.

</div>

<div class="post" data-post-id="21425" data-author="Weasel" data-date="2007-11-26T20:01:39+00:00" data-subject="">

horsecock? <img src="/images/smilies/icon_eek.svg" alt=":shock:" title=":shock:" width="15" height="15" class="smiley nozoom">

</div>

<div class="post" data-post-id="21426" data-author="Weasel" data-date="2007-11-26T20:06:07+00:00" data-subject="">

I have proof that one can 'remove all' instantly, and it's certainly a LOT faster than removing item by item:

http://www.youtube.com/watch?v=6ELiTfyqOqg

So now you have the proof, please return our unlagged remove all command. The same applies for wear all - just play the vid backwards.

Thank you.

</div>

<div class="post" data-post-id="21437" data-author="Avatar" data-date="2007-11-27T17:46:04+00:00" data-subject="EQ changes">

That's an interesting change, and I can see how it makes sense to someone approaching this logically. 

Unfortunately, from my point of view, lag isn't fun. Lag should be something that we are forced to deal with when our connection sucks, but it shouldn't be inflicted on us by the game itself. If changing eq needs to be balanced, we should look for some other method to balance it rather than lag. Of course, these are just my opinions.

</div>

<div class="post" data-post-id="21456" data-author="resouh" data-date="2007-11-28T15:58:51+00:00" data-subject="">

How many of these are fun to see while trying to play a game?

Loading...............

Saving................

Loading New Area.............

Disc Error...............

Changing EQ...................

People wait in reality.......lines, traffic, etc. Lets all work together to create a wait free universe:)

Resouh

</div>

<div class="post" data-post-id="21458" data-author="Autolycos" data-date="2007-11-28T19:59:38+00:00" data-subject="">

<strong>Let's ask someone else about lag...</strong>

<strong>pretty much answers it all..</strong>

![](http://www.xgenco.com/stuff/vader_faggotry.jpg)

</div>

<div class="post" data-post-id="21459" data-author="Weasel" data-date="2007-11-28T20:37:32+00:00" data-subject="">

LOL

</div>

<div class="post" data-post-id="21460" data-author="Tap" data-date="2007-11-28T22:55:00+00:00" data-subject="">

I can't wait till kill lag goes ingame. After each kill you will have to "pause" to regain strength to continue forward. Also, killing should have a chance of causing you to catch a nasty disease. Think about it, all the inter-species blood being spilled can't be good to get on ones self.

</div>

<div class="post" data-post-id="21461" data-author="Autolycos" data-date="2007-11-29T00:05:00+00:00" data-subject="">

oh... dont forget the extreme exhaustion after a long fight.

or maybe, ADD disorders that cause you to start a quest then walk away to buy rations.. 

oooh lets not forget obsesive compulsive disorders that makes 

you want to clean a room everytime someone feasts or drops things.

\*do your part to make the game more retarded!\* <img src="/images/smilies/icon_twisted.svg" alt=":twisted:" title=":twisted:" width="15" height="15" class="smiley nozoom">

</div>

<div class="post" data-post-id="21462" data-author="Alberich" data-date="2007-11-29T00:16:10+00:00" data-subject="">

{weasel}

hrmm.. you mean like the stablag i get when i splork a mob, the poisoning from failed applies, or haste falling mid-run?

oh.. wait... you meant for the other classes too.... 

{/weasel}

</div>

<div class="post" data-post-id="21463" data-author="Weasel" data-date="2007-11-29T00:25:55+00:00" data-subject="">

exactly. 

btw, the majority of us are not nocturnal, and if we are, we still need to sleep at some stage, so the mud server should be in sleep mode for 8 hours a day during the evenings, or whatever it deems to be the evening.

</div>

<div class="post" data-post-id="21464" data-author="Tap" data-date="2007-11-29T01:36:52+00:00" data-subject="">

I disagree, a super strain of cyber-cocaine could perpetually keep the machine up and running. Nasty habit could involve so many coins/drachma being 'used' to keep buying or ugh-oh! system crashes and has to enter virtual rehab for 12 RL hours.

 <img src="/images/smilies/icon_eek.svg" alt=":shock:" title=":shock:" width="15" height="15" class="smiley nozoom">

</div>

<div class="post" data-post-id="21465" data-author="Tap" data-date="2007-11-29T01:41:20+00:00" data-subject="">

Also, port 6104 could be introduced as split personality and/or junkie gf/bf who would require same amount og attention. Only you couldnt be logged onto both ports at once. And um...mil exp would only count if same amount ran on both ports. in 2008, we could introduce port 6105 as the red-head stepchild. this port would be the precusor to Sloth IV: The Quest for Piece

</div>

<div class="post" data-post-id="21466" data-author="Weasel" data-date="2007-11-29T02:11:39+00:00" data-subject="">

Rescues, stabs and spells should not fail - in the interests of political correctness, the message should just say 'deferred success'.

While we're at it, in order to promote harmony and non-aggression to our young and impressionable players, and in the interests of general safety, all offensive weapons should be removed from the game.

</div>

<div class="post" data-post-id="21467" data-author="Alberich" data-date="2007-11-29T03:17:31+00:00" data-subject="">

> <strong>Weasel wrote:</strong>
> Rescues, stabs and spells should not fail - in the interests of political correctness, the message should just say 'deferred success'.

laugh

</div>

<div class="post" data-post-id="21468" data-author="Autolycos" data-date="2007-11-29T04:41:36+00:00" data-subject="">

> <strong>Tap wrote:</strong>
> the precusor to Sloth IV: The Quest for Piece

lmfao!

</div>

<div class="post" data-post-id="21469" data-author="13" data-date="2007-11-29T07:26:38+00:00" data-subject="">

![](http://www.xgenco.com/stuff/vader_faggotry.jpg)

![](http://www.xgenco.com/stuff/vader_faggotry.jpg)![](http://www.xgenco.com/stuff/vader_faggotry.jpg)

![](http://www.xgenco.com/stuff/vader_faggotry.jpg)![](http://www.xgenco.com/stuff/vader_faggotry.jpg)

![](http://www.xgenco.com/stuff/vader_faggotry.jpg)![](http://www.xgenco.com/stuff/vader_faggotry.jpg)

![](http://www.xgenco.com/stuff/vader_faggotry.jpg)![](http://www.xgenco.com/stuff/vader_faggotry.jpg)

![](http://www.xgenco.com/stuff/vader_faggotry.jpg)![](http://www.xgenco.com/stuff/vader_faggotry.jpg)

![](http://www.xgenco.com/stuff/vader_faggotry.jpg)![](http://www.xgenco.com/stuff/vader_faggotry.jpg)

![](http://www.xgenco.com/stuff/vader_faggotry.jpg)![](http://www.xgenco.com/stuff/vader_faggotry.jpg)

best ever!!!!!!!!

</div>

<div class="post" data-post-id="21474" data-author="Autolycos" data-date="2007-11-29T16:01:07+00:00" data-subject="">

<img src="/images/smilies/icon_e_wink.svg" alt=":wink:" title=":wink:" width="15" height="15" class="smiley nozoom">

</div>

<div class="post" data-post-id="21477" data-author="Vixn" data-date="2007-11-29T19:12:52+00:00" data-subject="">

add one minute lag right after this string:

Welcome to the land of Sloth III. May your visit here be... Interesting.

argh, I still feel good

LAG ME MORE!

</div>

<div class="post" data-post-id="21480" data-author="Weasel" data-date="2007-11-29T21:07:34+00:00" data-subject="">

Oh, and Vista-like prompts, just for completedness:

SlothMUD tells you -- "your client just told us to throw a firewind at flame. Is this correct?"

y

SlothMUD tells you -- "are you sure?"

y

SlothMUD tells you -- "really? it's a pretty big mob.."

y

y

y

y-

You are dead! R.I.P.

</div>

<div class="post" data-post-id="21481" data-author="Autolycos" data-date="2007-11-29T22:31:27+00:00" data-subject="">

lmfao... so true

</div>

<div class="post" data-post-id="21483" data-author="Yasik" data-date="2007-11-29T23:08:04+00:00" data-subject="">

> <strong>Vixn wrote:</strong>
> add one minute lag right after this string:
> 
> Welcome to the land of Sloth III. May your visit here be... Interesting.

I think the msg should be corrected this way:

Welcome to the LAG of Sloth III. May your visit here be... Interesting.

</div>

<div class="post" data-post-id="21486" data-author="Alberich" data-date="2007-11-29T23:31:52+00:00" data-subject="">

on a similar note

since being drunk now makes the game very unfun to play (to say the least), and there doesn't seem to be a way to not have feast summon ale/wine/etc, does anyone know if cleanse will fix? or can we maybe start having coffee shops in town to sober yourself up? <img src="/images/smilies/icon_razz.svg" alt=":P" title=":P" width="15" height="15" class="smiley nozoom">

</div>

<div class="post" data-post-id="21487" data-author="13" data-date="2007-11-30T04:40:45+00:00" data-subject="">

what happens from being drunk now?

</div>

<div class="post" data-post-id="21488" data-author="Weasel" data-date="2007-11-30T05:01:03+00:00" data-subject="">

> <strong>13 wrote:</strong>
> what happens from being drunk now?

for you? no change.

</div>

<div class="post" data-post-id="21489" data-author="Yinao" data-date="2007-11-30T05:11:16+00:00" data-subject="">

> <strong>Weasel wrote:</strong>
> > <strong>13 wrote:</strong>
> > what happens from being drunk now?
> 
> 
> 
> for you? no change.

 <img src="/images/smilies/icon_eek.svg" alt=":shock:" title=":shock:" width="15" height="15" class="smiley nozoom"> Rofl, classic <img src="/images/smilies/icon_lol.svg" alt=":lol:" title=":lol:" width="15" height="15" class="smiley nozoom">

</div>

<div class="post" data-post-id="21508" data-author="Weasel" data-date="2007-12-01T17:01:14+00:00" data-subject="">

Seems rem all lag has been toned down a little bit, thanks.

hmm.. but wear all not?

</div>

<div class="post" data-post-id="21819" data-author="Weasel" data-date="2007-12-30T05:09:39+00:00" data-subject="">

well.. seems like there's a limit to how much you can wear or remove - but the limit is because of a command character limit.. anyone hit this limit on large eq changes like regen mode? Managed to fit it all in using smaller eq item names, but that then opens it up to error.. 

Coders - would slightly extending the character limit per command be out of the question?

</div>

<div class="post" data-post-id="21820" data-author="firebrand" data-date="2007-12-30T14:29:41+00:00" data-subject="">

can anyone reasonably explain to me why lag has to be the penalty "answer" to commands, spells, skills, etc for chars? and if you want to talk "balance", why don't mobs suffer the same lags, penalties, lost concs and whatevers that chars suffer? why can't we have a variety of effects that the game randomly selects, with lag being only one of them? and don't give me the realism argument. there is nothing real about this FANTASY game. we come here to ESCAPE realism, not be mired down with more of the same. okay, i grant you that there are warriors and clerics and etc in real life - hell i am friends irl with several druids (and no, we are not going off on a religious tangent here. i am just making a statement)- but not a single one of them can shapeshift....and no, i am not saying take shifting out of game. i am just pointing out that we come here to have fun and relax, not put ourselves through more frustration, otherwise what is the point of coming here at all? \*steps off soapbox\*

"it seems you feel our work is not beneficial to the public" --rachael --\> blade runner

</div>

<div class="post" data-post-id="21823" data-author="jezer" data-date="2007-12-31T04:56:28+00:00" data-subject="">

I think the remove all and wear all lag should be shorter for male characters. Find me a women that can get changed quicker than a guy? <img src="/images/smilies/icon_twisted.svg" alt=":twisted:" title=":twisted:" width="15" height="15" class="smiley nozoom">

</div>

<div class="post" data-post-id="21824" data-author="Alberich" data-date="2007-12-31T13:51:16+00:00" data-subject="">

snicker

\+1

</div>
