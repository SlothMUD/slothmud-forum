---
title: "Improvement Suggestion"
topic_id: 1385
author: "Avatar"
date: 2005-07-27T20:20:24+00:00
last_activity: 2005-07-29T19:45:36+00:00
last_author: "13"
sticky: false
locked: false
post_count: 18
---

<div class="post" data-post-id="8075" data-author="Avatar" data-date="2005-07-27T20:20:24+00:00" data-subject="Improvement Suggestion">

I'm being picky, I know, but this seems to be very unhelpful:

> <strong>Quote:</strong>
> \>channel who \<enter\>
> 
> 
> 
> You need to supply a valid channel name.

It may be more useful to replay with the channel help text:

> <strong>Quote:</strong>
> \>channel who \<enter\>
> 
> 
> 
> You need to supply a valid channel name.
> 
> Usage: channel \<cmd\> [\<arg1\> [\<arg2\>]]
> 
> \<cmd\> = list, join \<name\> [\<password\>], who [\<name\>],
> 
> lock [\<password\>], off.
> 
> E.g. channel list, channel join \<channel name\> \<password\>
> 
> NOTE: ctalk \<message\> is used to communicate on chosen channel

Even better, my favorite here, you might reply with the channel list results:

> <strong>Quote:</strong>
> channel who \<enter\>
> 
> 
> 
> You need to supply a valid channel name.
> 
> Here are the currently open channels.
> 
> Name #Users Locked?
> 
> \-----------------------------
> 
> hosers 6 No
> 
> holy 1 No
> 
> \~dragonsworn\~ 1 No

Again, I know I'm being picky.

</div>

<div class="post" data-post-id="8076" data-author="Ditheca" data-date="2005-07-27T23:42:49+00:00" data-subject="">

More improvement suggestions!

Gasp! Choke! you are DROWNING!

\<-9hp 467ma 199mv\> [AF A]\> 

The sky starts to cloud up, and the air gets colder.

You received 1 experience points.

You are buffeted by waves of remorse! ... it passes.

You have been KILLED!!

Don't get me started on the whole drowning thing. I mean someone with unmatched magical power (and the ability to turn into a frog at will) can and should slowly die over the course of 15 minutes when he accidentally steps into the water.

Not that that's gonna change <img src="/images/smilies/icon_e_smile.svg" alt=":)" title=":)" width="15" height="15" class="smiley nozoom"> What I really want to see happen is -- Me not becoming evil for the sin of "death" Imagine if the real world was that way... everyone -- no matter how righteous -- goes to hell because dying is evil <img src="/images/smilies/icon_e_smile.svg" alt=":)" title=":)" width="15" height="15" class="smiley nozoom"> go figure.

</div>

<div class="post" data-post-id="8077" data-author="kjartan" data-date="2005-07-28T00:22:58+00:00" data-subject="">

Ok, both items are fixed incor.

Magic and water don't mix - haven't you seen the Wizard of Oz?

</div>

<div class="post" data-post-id="8079" data-author="Ditheca" data-date="2005-07-28T01:00:17+00:00" data-subject="">

I'm melting I'm melting!!!!!!

Thanks Doctor KJ! By the way the suicide alignment bug also applies to dying from poison and a few other behaviors which the mud interprets as a player dealing damage to themselves. Can't think of em at the moment.

</div>

<div class="post" data-post-id="8080" data-author="kjartan" data-date="2005-07-28T01:01:16+00:00" data-subject="">

The fix is to all instances of people damaging themselves, so all that stuff should be covered. And you're welcome.

</div>

<div class="post" data-post-id="8081" data-author="Medios" data-date="2005-07-28T02:53:57+00:00" data-subject="">

Oooh Ooooh I found something. I tried to buy a vaporous potion, and it wouldnt let me. Mutap worked but the id showed this.

7000 a vaporous white potion

You feel informed:

Object 'mutap brew pt vapor vaporious white potion', Item type: POTION

Item is: NOBITS

Weight: 1, Value: 7000, Worn in: TAKE 

Level 20 spells of:

cure critic

cure critic

cure critic

</div>

<div class="post" data-post-id="8082" data-author="kjartan" data-date="2005-07-28T02:58:46+00:00" data-subject="">

And that's fixed too; you'll need to rent and come back on for individual potions of yours to be fixed.

</div>

<div class="post" data-post-id="8083" data-author="Ezekiel" data-date="2005-07-28T04:54:22+00:00" data-subject="Alignment display">

I know this is a bit picky to ask for...but can we at least have the option of switching the alignment in our score to numerical form...i mean i know we can use the prompt...but i like just having my basic prompt and all esle seems like excesss to me. The textual line that describes your status is far less helpful than the numbers anyway. In score 1 and score 2 it is identical. I was hoping maybe this could be changed since it would be a simple benefit, considering almost everything else is in numerical form. When I spoke about it briefly on gosssip it was well supported. Just a thought.

Thanks,

ezekiel

</div>

<div class="post" data-post-id="8085" data-author="13" data-date="2005-07-28T10:32:12+00:00" data-subject="">

Zeke just figure out how the scale works and #sub the messages in your client to whatever you want.

</div>

<div class="post" data-post-id="8087" data-author="Weasel" data-date="2005-07-28T14:07:19+00:00" data-subject="">

yeah.. exept they don't quite match up.. eg: sometimes I was able to cast grace at -3, sometimes I wasn't.. unless that has been fixed now, then it's still a little off. I think maybe grace depends on the message rather than the numerical rating, which insinuates that the message also changes somewhere between -3 and -4, although I haven't tested this further because I really would rather enjoy playing sloth than piss about trying to get my alignment sussed out and avoid hitting a heap of mobs in the mud, some that (last time I checked) did not indicate if they were evil or good until you killed them to find out...

</div>

<div class="post" data-post-id="8088" data-author="12345" data-date="2005-07-28T14:44:29+00:00" data-subject="">

Minor silliness.

The orange potions always try to cast strength on your 3x, but it only ever works once.

Also a suggestion to help Weasel out... a $ code for the prompt that simply displays G N or E. Then he'll know the difference between -3E and -3N.

</div>

<div class="post" data-post-id="8089" data-author="Weasel" data-date="2005-07-28T14:54:59+00:00" data-subject="">

or -3WTF <img src="/images/smilies/icon_e_smile.svg" alt=":)" title=":)" width="15" height="15" class="smiley nozoom">

</div>

<div class="post" data-post-id="8090" data-author="kjartan" data-date="2005-07-28T15:14:18+00:00" data-subject="">

Nah, no alignment readout changes.

</div>

<div class="post" data-post-id="8092" data-author="Avatar" data-date="2005-07-28T19:11:37+00:00" data-subject="orange">

I think the orange potions casting Str 3 times are a leftover from previous generations of Sloth where you actually had to cast strength multiple times to get each +1 from the spell.

</div>

<div class="post" data-post-id="8093" data-author="12345" data-date="2005-07-29T00:10:58+00:00" data-subject="">

It's been around for forever. When I started playing again, Blaster made the comment that he didn't know why everyone, himself included, had never bothered to fix them. One of the major reasons I've always respected the guy. However, they still try to cast 3 times. Since everyone else was suggesting tiny changes, I figured I'd throw it in.

</div>

<div class="post" data-post-id="8094" data-author="kjartan" data-date="2005-07-29T02:16:11+00:00" data-subject="">

Ok, orange is fixed.

</div>

<div class="post" data-post-id="8098" data-author="blackmore" data-date="2005-07-29T13:33:32+00:00" data-subject="">

While we're nitpicking on little things, in score you have a section header that reads "You are affected by the following spells:", and 2 of the spells are "entangled by webs" and "demon bound". These are the only 2 that I've seen that don't show the spell name, they show the consequences of the spell.

Thanks for fixing the orange potion, I bet that's been reported over 100 times by various people.

</div>

<div class="post" data-post-id="8101" data-author="13" data-date="2005-07-29T19:45:36+00:00" data-subject="">

IT FIXES THE ALIGNMENT AND THEN IT PUTS THE LOTION ON ITS SKIN

</div>
