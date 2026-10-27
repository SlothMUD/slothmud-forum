---
title: "What does the color red mean on spell messages?"
topic_id: 4674
author: "*juggleblood*"
date: 2016-09-25T16:17:35+00:00
last_activity: 2016-09-30T17:00:02+00:00
last_author: "*teker*"
sticky: false
locked: false
post_count: 12
---

<div class="post" data-post-id="37360" data-author="*juggleblood*" data-date="2016-09-25T16:17:35+00:00" data-subject="What does the color red mean on spell messages?">

What does the color red mean on spell messages, exactly?

</div>

<div class="post" data-post-id="37361" data-author="Teron" data-date="2016-09-27T08:24:45+00:00" data-subject="Re: What does the color red mean on spell messages?">

I assume it means that you made a save vs spells against the mob, according to "color set".

Though it also fires on stabs and grips, so I'm not that sure about that.

</div>

<div class="post" data-post-id="37362" data-author="*juggleblood*" data-date="2016-09-27T22:00:04+00:00" data-subject="Re: What does the color red mean on spell messages?">

First, lets avoid confusion in the language. When you blast, you don't save against the mob, the mob saves against you. 

But, I'm not certain the red line means exactly that. I'd really appreciate clarification, i.e. is it that simple, red=failed save, not red=mob saved?

</div>

<div class="post" data-post-id="37363" data-author="Teron" data-date="2016-09-28T12:09:55+00:00" data-subject="Re: What does the color red mean on spell messages?">

Can't you look it up in the code? I mean, the only people, who can answer with 100% certainty, are Teker and Splork.

</div>

<div class="post" data-post-id="37364" data-author="*juggleblood*" data-date="2016-09-28T19:27:45+00:00" data-subject="Re: What does the color red mean on spell messages?">

Nope. Non-coder here. I guess it is that straightforward, red=failed save, but that makes me sad because with my 13 spell saves cap I blast like shit.

</div>

<div class="post" data-post-id="37365" data-author="*teker*" data-date="2016-09-29T03:07:38+00:00" data-subject="Re: What does the color red mean on spell messages?">

The special color on the spell (and now song) messages indicates that the victim of the attack successfully saved and didn't die. The code doesn't specifically say "red" - it looks like it's a user defined color, so maybe it defaults to red.

I have no idea why a skill message (backstab, etc) would have special coloring.

</div>

<div class="post" data-post-id="37366" data-author="Teron" data-date="2016-09-29T06:51:16+00:00" data-subject="Re: What does the color red mean on spell messages?">

Just in case you want to look into the backstab thing, the color there does coincide with the color I chose for the 20th option: spell saves. So it may be as simple as checking, where that color setting is used.

It doesn't happen often.

P.S. Did you mean, "the victim of the spell failed the save"?

</div>

<div class="post" data-post-id="37367" data-author="*teker*" data-date="2016-09-29T14:22:49+00:00" data-subject="Re: What does the color red mean on spell messages?">

> <strong>Teron wrote:</strong>
> P.S. Did you mean, "the victim of the spell failed the save"?

Nope. The code says the color is shown when the victim successfully saves for 1/2 damage and lives. All other situations (mob dies, victim is immortal, mob fails save) use the default color.

</div>

<div class="post" data-post-id="37368" data-author="Teron" data-date="2016-09-29T21:44:31+00:00" data-subject="Re: What does the color red mean on spell messages?">

But that isn't how it works, is it?

We see colors, when our spells do more damage, when mobs fail saves.

I observe this with the exp/damage calculator, however imprecise it is.

And when I put on my -saves gear and a wizard hat, I see more colors.

</div>

<div class="post" data-post-id="37369" data-author="*juggleblood*" data-date="2016-09-30T12:40:11+00:00" data-subject="Re: What does the color red mean on spell messages?">

Teker, you must be reading it wrong. I've done some testing and it's clear that red is the failed save. For example when I magic missile a low level mob, it's red almost every time. But when I blast a level 40 mob I only get a few red. And Mage has done some testing in coliseum and shown that his red lines go up with increased saves.

</div>

<div class="post" data-post-id="37371" data-author="cyprimus" data-date="2016-09-30T15:37:20+00:00" data-subject="Re: What does the color red mean on spell messages?">

Tekkers right. It does less damage with red.

</div>

<div class="post" data-post-id="37372" data-author="*teker*" data-date="2016-09-30T17:00:02+00:00" data-subject="Re: What does the color red mean on spell messages?">

Yeah, you guys are right. The variable name was confusing me - but it should be red when the victim fails to save. It's probably backwards for bard songs right now but I'll get it fixed in the next build.

</div>
