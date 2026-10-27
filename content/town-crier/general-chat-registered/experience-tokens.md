---
title: "Experience Tokens"
topic_id: 3050
author: "Weasel"
date: 2009-02-24T19:52:26+00:00
last_activity: 2009-03-14T05:56:03+00:00
last_author: "Weasel"
sticky: false
locked: false
post_count: 12
---

<div class="post" data-post-id="28281" data-author="Weasel" data-date="2009-02-24T19:52:26+00:00" data-subject="Experience Tokens">

I have heard that some kind of informal announcement was made recently that 2bil exp tokens are being removed, and that this change is a work in progress, but can we please get a formal announcement, or at least an interim announcement on the forums, presumably in the 'mud changes' forum?

The reason I ask is that I passed another 2bil exp yesterday but am unable to get an exp token for it at the Lyme mayor:

(<em>level gain</em>

<em>The mayor of Lyme tells you 'I don't see any need to hand those out anymore.'</em>)

Apparently that bit of coding went through prematurely. No worries, but has the exp cap also been removed already (if it still exists), or will I start getting negative experience soon until the change is fully complete? 

The Lyme Mayor is still quoting prices in tokens too, but clearly that will change in time - I'm only concerned here about what may happen in the interim if I gain what was effectively 'too much' experience previously.

Also just wondering if there's any particular reasoning behind the change.. I mean really it's no biggie, so please <strong>don't assume this is a whine session, because it isn't</strong>. The positives are that we have a few less items to carry/vault in terms of tokens, and that we don't have to stop a group to go get an exp token so we don't start getting negative experience (which is rare anyway, but it has happened), but at the same time I personally found the exp tokens provided a sense of achievement, which is not always easy to come by at 5x40 when you don't have levels to gain anymore.. in fact I sometimes think of my continued progress in terms of exp tokens, because there is almost nothing else that is universal between characters after 5x40... perhaps that's just me though.

Of course there may be some other reason for the change, such as a complete overhaul of the entire 5x40 purchasing options and how they work, but again, with no official post, it's hard to know.

Appreciate any feedback.

</div>

<div class="post" data-post-id="28282" data-author="Vixn" data-date="2009-02-24T21:26:26+00:00" data-subject="">

Weasels get no tokens from now on.

Appreciate it!

 <img src="/images/smilies/icon_evil.svg" alt=":evil:" title=":evil:" width="15" height="15" class="smiley nozoom">

</div>

<div class="post" data-post-id="28283" data-author="jezer" data-date="2009-02-24T22:33:04+00:00" data-subject="">

Oh, they are changing tokens? Interesting... I got a few, hope I can still use them before they change it.

</div>

<div class="post" data-post-id="28285" data-author="Toxis" data-date="2009-02-24T23:31:50+00:00" data-subject="">

Exp tokens still work for xp, just leave them in your inventory when buying spells/skills/stats.

\-Tox

</div>

<div class="post" data-post-id="28286" data-author="*juggleblood*" data-date="2009-02-24T23:47:51+00:00" data-subject="">

The logic behind the change is that xp tokens were a way to get around the limitations of the code. Variables weren't big enuff to handle it. So, now that the code can handle larger variables, they are just simplifying the code and eliminating the tokens.

You should have no problems going over 2 bil xp now. XP loss on corpse is capped btw. So you're not going to lose excessive amounts for carrying around all that xp.

The immediate reason for the change is to eliminate some crash bugs that were discovered. There's some pro's and con's with the change, but if it means a few less crashes, I'm all for it.

</div>

<div class="post" data-post-id="28287" data-author="jezer" data-date="2009-02-24T23:55:47+00:00" data-subject="">

Whats the xp loss cap? Don't tell me imm info... cause most thieves will know the next day anyways. <img src="/images/smilies/icon_twisted.svg" alt=":twisted:" title=":twisted:" width="15" height="15" class="smiley nozoom">

EDIT: 

> <strong>Quote:</strong>
> The immediate reason for the change is to eliminate some crash bugs that were discovered.

So Weasels insane amounts of warrior xp was overflowing the buffer and causing the mud to crash! Right! Target Weasel! <img src="/images/smilies/icon_twisted.svg" alt=":twisted:" title=":twisted:" width="15" height="15" class="smiley nozoom">

</div>

<div class="post" data-post-id="28290" data-author="Tap" data-date="2009-02-25T01:47:41+00:00" data-subject="">

No +5 hitpoints for you!

</div>

<div class="post" data-post-id="28420" data-author="Weasel" data-date="2009-03-07T07:49:44+00:00" data-subject="">

erm.. any chance Lyme Mayor can revert back to giving and redeeming exp tokens, at least until the coding changes are fully completed (Mayor still quoting prices in tokens too, even though he wont award them anymore). ie:

<strong>[ \*Hierarch\* ] Shyla would like mayor fixed so i can buy con</strong>

</div>

<div class="post" data-post-id="28422" data-author="*Splork*" data-date="2009-03-07T16:09:10+00:00" data-subject="">

Speak to one of the immortals online if you want to buy something. We can remove the exp and set ur character correctly until the mayor is fixed.

</div>

<div class="post" data-post-id="28423" data-author="Weasel" data-date="2009-03-07T16:39:14+00:00" data-subject="">

Thanks

</div>

<div class="post" data-post-id="28424" data-author="*Splork*" data-date="2009-03-07T21:22:04+00:00" data-subject="">

Ive fixed several players already, if one of you guys needs something please beep me. I will be online all weekend working on sloth related stuff and I will happily take care of mayor business at the same time.

Enjoy,

Splork

</div>

<div class="post" data-post-id="28486" data-author="Weasel" data-date="2009-03-14T05:56:03+00:00" data-subject="">

Hmm.. one of my VBS scripts has lost the plot and I just figured out why.. I use a CLng function in it, but that has a value limit of any number between -2147483648 and 2147483647 (which is 2^31). Since unused exp can now exceed that, I am spitting errors on my client with my statistical scripts. Is this why you had the exp tokens, to work around the CLng limitation? If so, what did you use to replace CLng? 

..Actually never mind, I suppose I can just divide values by 1mil first, and then express everything in millions... yeah that'll work.

</div>
