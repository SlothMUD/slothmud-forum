---
title: "Messages for resisted/saved spells"
topic_id: 1665
author: "Falsra"
date: 2006-01-18T12:48:22+00:00
last_activity: 2006-01-20T03:38:05+00:00
last_author: "12345"
sticky: false
locked: false
post_count: 14
---

<div class="post" data-post-id="10194" data-author="Falsra" data-date="2006-01-18T12:48:22+00:00" data-subject="Messages for resisted/saved spells">

When i fight a mob i see if my hit does 0 damage ( miss, ethereal mob ).

When i cast an offensive spell i see if my spell does 0 damage ( lost conc, immune )

When i fight a mob i see how much damage my successful hit does

( not exactly roll, but still i can see if i hit barely,hard or massacre ).

When i cast an offensive spell i have no idea how much damage my spell does. 

Mob may have f.e. 70% fire resist and still i have no clue to switch to another spell.

Mob may save all my spells and i have no clue to switch to another attunement.

It would be really nice to add messages for resisted and saved spells.

Thanks in advance!

/falsra

</div>

<div class="post" data-post-id="10200" data-author="kjartan" data-date="2006-01-18T17:40:56+00:00" data-subject="">

Hmm, there are supposed to be messages.  I'll look into it.  I think the messages don't kick in until 25% resistance or so.

</div>

<div class="post" data-post-id="10201" data-author="Weasel" data-date="2006-01-18T18:46:47+00:00" data-subject="">

Well if it's not already there, then it's a bloody good idea Falsra.

</div>

<div class="post" data-post-id="10222" data-author="Falsra" data-date="2006-01-19T10:31:36+00:00" data-subject="">

[quote:2x7e4xal]Hmm, there are supposed to be messages. I'll look into it. I think the messages don't kick in until 25% resistance or so.[/quote:2x7e4xal]

I cant say about mobs with natural resistances, but if i wind a mob which has

fire resist on (50%?), i dont get any messages.

And, for me, as for mage prime, even more important thing - we badly

need messages on saved spells  :twisted:

/falsra

</div>

<div class="post" data-post-id="10223" data-author="Avatar" data-date="2006-01-19T16:53:25+00:00" data-subject="Exp tracker">

I almost hesitate to bring this up, because it's pretty messy as a hack.  But, you can add your current exp to the prompt now.  After adding it, it is pretty easy to make an exp tracker similar to a HP whiner, but only notifying yourself (#write or comparable) when the exp value changes.  This would show you fight exp each round of combat as well as exp gained for blasting spells or heal spells.

Of course there are still a lot of variables (saves, resistances, spell damage, etc) but in general if you do more damage to the mob the exp gained for that spell should go up.

</div>

<div class="post" data-post-id="10224" data-author="Leaf" data-date="2006-01-19T18:43:54+00:00" data-subject="">

Chucky thats sounds like alot of work on setting up on tintin.  I have problems

setting up a whiner :)

</div>

<div class="post" data-post-id="10226" data-author="12345" data-date="2006-01-19T19:41:34+00:00" data-subject="">

Actually, it's exactly like setting up a whiner, only easier since the numbers only go up, not down.  It would require a bit of analysis to figure out, I'm sure, but is a cool plan all in all.

</div>

<div class="post" data-post-id="10227" data-author="Leaf" data-date="2006-01-19T19:54:01+00:00" data-subject="">

I'm guessing once I hit 500 post, I'll become an avatar poster like 12345?

</div>

<div class="post" data-post-id="10231" data-author="kjartan" data-date="2006-01-19T21:17:16+00:00" data-subject="">

So you're just sort of blathering to get your post count up, then?

Re: the saving throw messages... yes, that would be nice, but I'd have to write 200 or so "The kobold deftly dodges the worst of your fireball" type messages.  We are not going to have "The kobold makes his save!", ugh.  I might do it sometime.

</div>

<div class="post" data-post-id="10233" data-author="12345" data-date="2006-01-19T21:46:45+00:00" data-subject="">

Me thinks there's an easier way...

We have weapons that do various amounts of damage and we have to figure out for ourselves whether we got a good hit, bad hit or average hit.  We know through experience how often we should expect massacres and how often we should barely hit.

It doesn't seem like it would be overwhelmingly taxing to add a damage message to spells that echos back to the mage only...

ie.

Your firewind spell viciously massacres a kobold youth!

vs.

Your firewind spell brutally massacres a kobold youth!

You could even give it a cute little toggle if they decide it's spam.

You'll probably have to create a few damage classes beyond vicious that are unique to spells though...

</div>

<div class="post" data-post-id="10234" data-author="blackmore" data-date="2006-01-19T22:15:46+00:00" data-subject="">

I think the point Kj is making is there's 200 spells that are affected by saves.  Adjusting the message for firewind would leave 199 more spells that need to have a modified message, unless you do the exact same message for every spell - and I don't think it makes sense to have the save against magic missile say the same as the save against firewind.

There's multiple messages for acid blast.  I assume these messages are save vs damage and failed save vs damage, so the ability seems to exist, it's just taking the time and having the inspiration to write all the damage messages for all the save versions of the spells.

</div>

<div class="post" data-post-id="10236" data-author="kjartan" data-date="2006-01-19T22:18:41+00:00" data-subject="">

In fact, mostly you could do what 12345 suggests, but I don't like it.  It would be producing either identical messages for all spells, or redundant identical messages for all spells if you left the existing spell hit message in place.  The correct way to fix it is to add the buncha messages.  There's probably not really 200, but I bet there's 100.

</div>

<div class="post" data-post-id="10237" data-author="Avatar" data-date="2006-01-19T22:25:35+00:00" data-subject="exp tracking">

I added a personal whiner for exp changes when I noticed that exp was available as a prompt option.  It's 5 minutes or less of work, depending on if you want flexibility to change your prompt often or if you're going to set the prompt and leave it.

I can't say I get a whole lot of benefit other than it's just cool to have on.  I did notice that I try not to send heals between fights any more.  You get heal exp if the tank is engaged.  That few k probably isn't very significant with our mils of exps required to level, but every bit adds up!

</div>

<div class="post" data-post-id="10243" data-author="12345" data-date="2006-01-20T03:38:05+00:00" data-subject="">

In fact, mostly you could do what 12345 suggests, but I don't like it.  It would be producing either identical messages for all spells, or redundant identical messages for all spells if you left the existing spell hit message in place.  The correct way to fix it is to add the buncha messages.  There's probably not really 200, but I bet there's 100.[/quote:1uywt9sy]

Yeah, I was kinda suggesting a format like:

Your <spellname> spell <damage message><dam type> <target>!

While not sexy, neither is the standard fight scroll.  Also, while having a bunch of messages looks sexy, it's not necessarily more informative.  As an example, a question was asked not too long ago by someone who wanted to know what the strongest fire spell they had was, since they had spells in cleric and mage.  With standard damage messages, you actually have an idea how much damage you're really doing instead of a vague idea that the spell did 'a lot of damage' or 'not quite as much damage'.

Either way is an improvement over the current system though.

</div>
