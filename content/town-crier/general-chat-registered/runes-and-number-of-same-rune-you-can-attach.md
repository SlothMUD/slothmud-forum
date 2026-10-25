---
title: "runes and number of same rune you can attach"
topic_id: 3828
author: "Angels"
date: 2011-12-14T19:12:25+00:00
last_activity: 2011-12-17T14:23:53+00:00
last_author: "*juggleblood*"
sticky: false
locked: false
post_count: 8
---

<div class="post" data-post-id="33091" data-author="Angels" data-date="2011-12-14T19:12:25+00:00" data-subject="runes and number of same rune you can attach">

When runes first went in we where told you could only attach one of a given max stat. That is one rhodo or one emerald etc...

> **element wrote:**
> I think socketing shouldn't be "reversible", but you should be able to destroy the socketed rune at a fee.  
> 
> 
> 
> Also, I think high-end forges or elite eq should have 2 rune sockets (of course you can't socket 2 of the same runes) this would really help people in the long term....nobody wants to re-forge a piece of eq they took 6mths to make, because a better rune comes along

so in my opinion anyone able to socket two of the same rune should be posting it as a bug and not abusing it.

</div>

<div class="post" data-post-id="33095" data-author="Slowdraw" data-date="2011-12-15T18:18:38+00:00" data-subject="Re: runes and number of same rune you can attach">

I'm somewhat confused by this post. What's the purpose of the quote you used? Is that your being 'told you could only attach one of a given max stat.' that you mentioned? If so, there are a couple of flaws with using that quote.

1. I'm pretty sure that was just a suggestion from element(sorry if I'm mistaken, but I'm pretty sure element has nothing to do with the inner workings of runes) on how to make people start socketing more runes.

2. I'm pretty sure that element's statement of '(of course you can't socket 2 of the same runes)' was only talking about the suggestion of being able to put two runes in one piece of gear(because two of the same rune could double the amount of a specific bonus potentially), and not some sort of generalized statement about not being able to use more than one of a given rune.

3. Seeing as players aren't required to read the entire forum history before they start playing, I would hope there were some sort of in game documentation of any rules the game has. You might be better off quoting that documentation instead of a forum post that(as far as I can tell) doesn't have anything to do with your claim.

Anyway, I've never put very much effort into leveling, so I've only gotten to pretty low max levels. Because of that I've not looked into runes too much, and could be completely wrong about the whole thing. I would think that one of the many immortals I've seen posting on rune related topics would have said something if there was a rule about only having one of a given max stat from a rune at any time, seeing as people have obviously not been following that rule.

</div>

<div class="post" data-post-id="33096" data-author="*juggleblood*" data-date="2011-12-15T22:47:40+00:00" data-subject="Re: runes and number of same rune you can attach">

It's really not such a big deal. Angels is correct and the issue will be corrected. 

It's a bug issue, not a 'rules' issue. This is not a witch hunt. The code will be corrected when the coders get a chance to address it. 

Let's not make this into more than it is. Obviously we would prefer that people report things like this right away if they know it's a bug. If they don't realize it's a bug, then they can't be expected to report it. We won't get into a debate over what somebody knew. We'll simply fix it and move on.

</div>

<div class="post" data-post-id="33097" data-author="Angels" data-date="2011-12-16T05:04:11+00:00" data-subject="Re: runes and number of same rune you can attach">

Thanks Juggleblood. My post was to bring the topic to light..not set blame anywhere. I only posted as a few people have tried to convince me i could use two emerald runes for max wisdom. And I clearly remember being told at the beginning of runes that this was not to be the case. Unfortunately the only thing I could find on the crier to confirm the idea was elements post. 

If this thread caused anyone any hardships I am sorry. I just wanted to have a public place that could be located later where I was either confirmed or corrected on my thoughts.

Thankyou again for setting the matter to rest.

I would like to know if this applies to only max stat runes or all runes in general. 

That is no two ring runes that are the same name?

</div>

<div class="post" data-post-id="33099" data-author="Slowdraw" data-date="2011-12-16T17:19:52+00:00" data-subject="Re: runes and number of same rune you can attach">

Ah, I wasn't trying to make a big deal about it.(or start a witch hunt) I was just trying to explain my confusion and ended up doing so in a less than concise manner. As a bonus Angels now has a very straightforward quote to use instead of the one from element.

</div>

<div class="post" data-post-id="33100" data-author="*juggleblood*" data-date="2011-12-16T23:46:40+00:00" data-subject="Re: runes and number of same rune you can attach">

Best we confirm with Breeze, Krom, or Splork in regard to your question. Maybe you should shoot them an email.

</div>

<div class="post" data-post-id="33101" data-author="*Breeze*" data-date="2011-12-17T00:39:57+00:00" data-subject="Re: runes and number of same rune you can attach">

Hmm..

The question isn't really a yes/no question , rather it is 2 questions.

Q 1) Is it allowed (by the rules)

Q 2) Is it allowed (by the code)

So the answers are :

A 1) When Splork put in the rune code, he never intended any MAX_STAT to be doubled.

     and he stated that somewhere (which I am not searching for at this time)

A 2) The code allows it due to a slight bug which is now fixed.

When an mob/object is created, the immortal who created the mob/object has the 

option to add premade PROC's which allow the mob/object to do fun things.  

Probably the most well known Object PROCs are Vorpal (aka Choppers) and

MUDL (used everywhere!).

Runes and Clasps are unique in that they are equipped onto other objects rather

than worn.  As such, they are handled a bit differently.

What was happening is, the code was checking if the object was a clasp and if

it was a clasp then it would execute the clasp PROC and then finish.  If it

wasn't a clasp, then it would stop there.  The code was never checking to see

if the object was a Rune.  This is now fixed.

As to limits per rune/per character, that is solely up to Splork, and is

simply just a setting on the Rune PROC.

Since the Rune PROC was never executing, the PROC would never check to 

make sure that the rules/limits were enforced/exceeded.

The PROC now executes, so said limits are enforced.

Having said that, AFAIK, the only Runes that have per rune/per character limits 

are the MAX_STATS ones.

After this code goes live, those of you who socketed 2 MAX_STATS runes of the same

kind can go to any Mob that forges and unsocket the rune from the equipment, assuming

the equipment is x40/drachma.  Otherwise contact a **45+** immortal and they may be

able to help you.

Regards,

  ***Breeze***

</div>

<div class="post" data-post-id="33102" data-author="*juggleblood*" data-date="2011-12-17T14:23:53+00:00" data-subject="Re: runes and number of same rune you can attach">

You rock Breeze. Thx.

</div>
