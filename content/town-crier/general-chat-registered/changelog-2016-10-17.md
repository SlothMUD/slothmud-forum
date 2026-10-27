---
title: "Changelog 2016-10-17"
topic_id: 4679
author: "*teker*"
date: 2016-10-17T14:26:59+00:00
last_activity: 2016-10-22T23:58:28+00:00
last_author: "*Splork*"
sticky: false
locked: false
post_count: 16
---

<div class="post" data-post-id="37403" data-author="*teker*" data-date="2016-10-17T14:26:59+00:00" data-subject="Changelog 2016-10-17">

The rank command should show correct information now.

Some skills couldn't be used on mobs with \> 100% hit points. They can now.

Sending a message when dispel good/evil are blocked by mindbar. I didn't realize this happens but if you have mindbar up you can't have these spells cast on yourself.

I rewrote the practice command to show the classes based on your class order and to exclude classes where nothing matches. This should compact the display a bit for people who keep up on their spell books.

I changed eqset to show more error messages outside of debug mode. Mostly things like containers being full when trying to put gear away. I haven't experienced the things that I'm seeing in the bugs so I'm wondering if players just aren't getting error messages when things go wrong.

I added to the target code so that mobs that are targeted show "[Target]" when they do most actions. Things like "The guard [Target] breaks free of the webs!" or "The guard [Target] panics, and attempts to flee." I thought it would make it easier for script writers to build triggers without having to save the target in the client. I had to rewrite a bunch of the code for showing mobs/players in room (ie "Steve is standing here") so let me know if anything looks strange. Have any of the groups been using these commands? Are they helpful?

</div>

<div class="post" data-post-id="37404" data-author="*teker*" data-date="2016-10-17T16:24:54+00:00" data-subject="Re: Changelog 2016-10-17">

Ok, we've found a bug where sometimes mobs are shown as "someone" when you can see them. I'll have it fixed for tomorrow morning.

</div>

<div class="post" data-post-id="37405" data-author="Teron" data-date="2016-10-17T18:41:37+00:00" data-subject="Re: Changelog 2016-10-17">

As a leader, I have started using the target command almost immediately, once you've reintroduced it, but I don't know how many of my followers use it.

I didn't notice any positive or negative changes in groups. I only saw ppl die through the use of bad targets, imperfect triggers or bizarre manual skills that gripped mobs that weren't targeted (and attacking Lucifer, when the target was "priest"), so I guess they died, because they weren't using the target command.

I do find it awkward to pretype:

backstab target

cast 'firewind'

cast 'firewind'

only to attempt a backstab with a sword, fail and then to wind the target.

P.S. I've heard a complaint that the word [Target] is spammy, so perhaps a toggle option to stop it from showing would help (maybe when using "concise").

</div>

<div class="post" data-post-id="37406" data-author="Gorka" data-date="2016-10-18T05:47:59+00:00" data-subject="Re: Changelog 2016-10-17">

I can't think of one new change that's been implemented that hasn't been called spammy by some dork. Remember what happened when someone called auctioneer spammy... now it takes a whole minute of senseless waiting to list items, because some dork said it was being spammy... if I shall ever find the dork that said this I will... I will... <img src="/images/smilies/icon_evil.svg" alt=":evil:" title=":evil:" width="15" height="15" class="smiley nozoom"> <img src="/images/smilies/icon_twisted.svg" alt=":twisted:" title=":twisted:" width="15" height="15" class="smiley nozoom"> 

The irony is the "spam" actually helps us create triggers and actions better by providing us with keywords and phrases we can filter for, so we don't create bum triggers. So the irony is, if you want to build better triggers to some degree we need better spam.

Just yesterday I tried to build something new where I use the last of my available mana when I jump into my max mana mode... because I was watching the msdp.MANA change event the trigger can fire multiple times during the course of an eq change as mana recharges... as there is no message to say when the eq change is complete I had to give up my idea... as I was spamming myself during the eq change.

It's a catch 22, often "spam" is helpful. There is always the gag command in our clients for dorks, I wish they would use it. More spam please! (Especially at the beginning and end of significant commands.)

A good example is the lost concentration message, it doesn't say what you lost con on... so you have to put your spells in arrays, count success messages etc in order to figure out what needs recasting... if it said you lost concentration on your \<spell\>! Wow, now we can do something with it. But no doubt some dork will find the extra word spammy and complain... <img src="/images/smilies/icon_rolleyes.svg" alt=":roll:" title=":roll:" width="15" height="15" class="smiley nozoom">

As a person who likes to mess with scripts for the hell of it, even if that does mean accidentally gripping the lyme bank keeper... (and God knows he deserved it <img src="/images/smilies/icon_twisted.svg" alt=":twisted:" title=":twisted:" width="15" height="15" class="smiley nozoom">) when I saw those extra targetting messages tekker put in, I was actually pleased as I could now put new events on those phrases.

</div>

<div class="post" data-post-id="37407" data-author="*teker*" data-date="2016-10-18T16:25:08+00:00" data-subject="Re: Changelog 2016-10-17">

So the "someone" problems should be fixed but it looks like my fixes for practice didn't make it in for some reason. I'll try to figure out why.

If there are folks that are getting annoyed with the [Target] tag, speak up and I can look at making it a toggle option. I could do the same with the backstab/spell issue Taron mentioned above or I could just remove that option so that spells/skills without specified targets only default to fighting. It just depends on how you guys want it to work and who speaks up.

</div>

<div class="post" data-post-id="37408" data-author="Teron" data-date="2016-10-19T15:54:06+00:00" data-subject="Re: Changelog 2016-10-17">

1\. Gorka does have a point.

For example, the visible mob name isn't always the target, e.g., target may be god in Olympus, and yet I do need triggers that fire, when actions are performed by or to the target.

For example, I need a trigger that detects anyone hitting a target \* hard:

%1\*@target\*hard -\> rescue %1

But then I get

The guardian hits you very hard -\> rescue the.

So, I'd say that a toggle option would be useful, though I don't know how many more ppl (will) find it spammy.

Another thing: I'd prefer it to read [target], because capitalization isn't required, unless it starts the sentence in the room mob list. It just looks so [<strong>T</strong>arget] out of place.

2\. I am not sure that how you implemented target is to blame for how I fail to stab mobs. I'm 99% sure it's user error, which can be fixed by a pipe (but not a steel one) and relearning the old habits (and paying more attn to the weapons).

You see, one of the major ways to use target is stab blast, so if a person can't engage with "cast 'firewind'", then this whole concept is much less useful (the only other case remaining would be a similar mob walking in the room). You could make it only work with fighting \*targets\*, but then I guess people won't change their "start the fight" aliases and habits.

So let's leave this point as is for now, and if I discover something out of place, I'll let you know.

2\. 

> <strong>Gorka wrote:</strong>
> A good example is the lost concentration message, it doesn't say what you lost con on... so you have to put your spells in arrays, count success messages etc in order to figure out what needs recasting... if it said you lost concentration on your \<spell\>! Wow, now we can do something with it. But no doubt some dork will find the extra word spammy and complain... <img src="/images/smilies/icon_rolleyes.svg" alt=":roll:" title=":roll:" width="15" height="15" class="smiley nozoom">

Now this I wholeheartedly support as I'm sure others, too.

I've had a hard time figuring out how to specify, which spell is being cast, because I definitely need it to recast, and I don't want to make it very slow.

For example, when I do a spell check, I type score, enable a trigger class and the spells that aren't up are cast in a quick pretype-like succession. There's no way to know, which one I lost conc on. Even if it doesn't involve a response from a trigger, it is still sometimes annoying to calculate, how many successful spells went in after you lost conc, so you can recast the one you did. And Kjartan forbid you miscalculate and recast a 42ma spell that's already up.

Of course, I could do a second spell check, but it's slower, than a trigger on a "you lost conc on petrified armor".

3\. About the auctioneer. Why not just cut the reports from the token auctioneer, and accept batches at both of them? Rarely does someone sell absurd amount of items on the actual auction for it to be very spammy. Usually, the amount of items is 1-3, rarely 5 (though you could run your own statistics to check that).

P.S. Not trying to hijack the thread, just mentioning ideas.

</div>

<div class="post" data-post-id="37409" data-author="Gorka" data-date="2016-10-19T16:56:15+00:00" data-subject="Re: Changelog 2016-10-17">

I suspect in the past the lost con message was generic to stop botters.

However...

\* I think botting is the least of sloth's worries at the moment, with the declining player base.

\* Botters bot because the game is a grind/boring... so they eventually leave anyway. 

\* It's very complicated but it's possible to keep an array of all spells you cast, and check them off your list with the success messages and recast those that fail.

\* msdp.AFFECTS lists your spells, no need to type score these days to see whats up in order to recast. In fact msdp has made botting far easier, yet it didn't change player behavior, they were already bots beforehand anyway. It's a text based game... what can you do? 

\* Half the "attraction" and "skill" in playing sloth is actually scripting and triggers anyway. Find me an avatar who plays without scripts. The scripting is a key component of the game giving player game satisfaction.

But anyways, my overall point is Spam is good. If you don't like it, gag it in your client. Personally I can't get enough of the stuff. More spam please, less lags.

</div>

<div class="post" data-post-id="37410" data-author="*teker*" data-date="2016-10-19T18:12:34+00:00" data-subject="Re: Changelog 2016-10-17">

I got in late this morning but the targeting code should be re-enabled now. I don't plan on rebooting for a while unless there's something else majorly broken. The practice code should be displaying the right information now.

> <strong>Quote:</strong>
> I am not sure that how you implemented target is to blame for how I fail to stab mobs.

I think the issue you're having is that when you cast firewind, it sees that you're not fighting, so it sends the spell at the target. Previously if you did this, the spell would fail (without mana loss) due to not specifying a target. I could certainly change this back so that you'd have to specifically type "cast 'firewind' target" to start a fight with the target rather than "cast 'firewind'". It's more to type but if you're running a script it doesn't make any difference. You'll notice the same thing happens with backstab - if you type backstab without any arguments and you're not fighting and your target is in the room - it will attempt to backstab your target.

I can certainly change the tag to "[target]" and add a toggle for it.

I can also change the lost concentration line to something like "You lose your concentration while casting/singing/playing 'spell/song'".

I've been thinking about the auctioneer . It would be pretty easy to add queuing to the messages but the increased run-times have created another problem - sometimes the token auctioneers get full. There's a hardcoded limit for the number of simultaneous auctions and if one person can consign a whole bunch of items really fast it is more likely the auctions will be full most of the time. I'm not sure if the hardcoded limit is there for a significant reason or if it was more of a guess to the maximum number needed. It doesn't seem fair to me that a small number of players could fill up the auction houses so that no one could use them.

</div>

<div class="post" data-post-id="37411" data-author="Gorka" data-date="2016-10-19T20:37:05+00:00" data-subject="Re: Changelog 2016-10-17">

The auction lag problem is actually a symptom of a greater problem. There would be no problem with the auction system, without listing tokens... tokens are about the only items we sell in bulk.

The greater problem is actually coins, it's a grind at the moment, everything with leveling has increased in coins, but if anything coins are harder to come by than say in s3, and there are no good coin mobs if you group a lot, which means your exp increases at a faster rate than your coins ever will. 

Token's have a good value, and they are plentiful these days, some of us are using token income to bridge this gap, however they are actually hard to offload, and with the lack of newbie's there is an oversupply and they sit around with several of us dependent on there income to stay a float. Because they cost too much to rent, we abuse the token auction as like a "second storage."

Today after your reboot, there were a max amount of tokens in all available shops within at least 10 seconds of us getting back in... this is how desperate the situation is. I missed out on selling mine by tenths of a second in the "log in scramble."

The auction problem, isn't really an auction problem, it's a token problem caused by a shop keeper problem caused by a gold problem.

I'm trying to diversify my income sources these days because clearly being dependent on token income is a recipe for disaster.

I think if you solve the shopkeeper problem or the token problem, the auction problem simply wouldn't even matter as most objects would be sold one at a time. However limiting the token auction without addressing the real issues might create a little bit of fallout.

There is a mesh of connecting issues here... not sure just changing auctioneer will change anything, it also risks making the situation worse.

If you changed the spell fail message, that to most players would be probably the most useful change made to sloth since the eqset command.

</div>

<div class="post" data-post-id="37412" data-author="*juggleblood*" data-date="2016-10-19T20:49:07+00:00" data-subject="Re: Changelog 2016-10-17">

Please change this thread so that players can not post to it. It would read much better as a clean record of changes. Also please delete existing player comments.

@Gorka It is absurd to complain about not being able to depend on token sales for income, when no one but you is trying to do that. No one is forcing you to spend so much time in the coliseum. You could go out and solo for coins like everybody else.

</div>

<div class="post" data-post-id="37413" data-author="Gorka" data-date="2016-10-19T20:55:53+00:00" data-subject="Re: Changelog 2016-10-17">

> <strong>\*juggleblood\* wrote:</strong>
> @Gorka It is absurd to complain about not being able to depend on token sales for income, when no one but you is trying to do that. No one is forcing you to spend so much time in the coliseum. You could go out and solo for coins like everybody else.

This is what I am doing... and no, I am not the only one making money from tokens. There are at least 3 others, I just have the biggest mouth. <img src="/images/smilies/icon_twisted.svg" alt=":twisted:" title=":twisted:" width="15" height="15" class="smiley nozoom">

</div>

<div class="post" data-post-id="37415" data-author="*juggleblood*" data-date="2016-10-19T21:01:34+00:00" data-subject="Re: Changelog 2016-10-17">

This would be like arguing that xerxes wasn't enough coins because if you're only killing xerxes then you don't have enough coins to level. There are no mobs, only xerxes!

(If you don't get that joke, you weren't around for that epoch.)

</div>

<div class="post" data-post-id="37420" data-author="cyprimus" data-date="2016-10-20T02:59:58+00:00" data-subject="Re: Changelog 2016-10-17">

I agree with gokra.. we have an overabundance of exp!

Nerf it!

\*hides\* \*crud, no dark cloak\* \*lurks in vault...\*

</div>

<div class="post" data-post-id="37431" data-author="Teron" data-date="2016-10-22T18:21:33+00:00" data-subject="Re: Changelog 2016-10-17">

Teker, I guess engaging on "backstab target" or "cast 'firewind' target" would work. After all, it's not "backstab guard".

Thanks.

P.S. Even though moving offtopic posts to other threads would work, I don't see why we can't discuss changelogs here. Feedback is good, right?

</div>

<div class="post" data-post-id="37432" data-author="*juggleblood*" data-date="2016-10-22T18:30:50+00:00" data-subject="Re: Changelog 2016-10-17">

Feedback is great sure, but it would be nice to be able to read a clear listing of game changes without all the player banter mixed in. Just a thread with a list of changes by that immortal.

</div>

<div class="post" data-post-id="37439" data-author="*Splork*" data-date="2016-10-22T23:58:28+00:00" data-subject="Re: Changelog 2016-10-17">

I'd recommend posting to "Game Changes and New Stuff" for game additions by Immortals. If I remember right, that's for Immortals only and players can start new threads here regarding when they are looking for discussion...

</div>
