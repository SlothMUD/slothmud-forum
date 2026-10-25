---
title: "Class Abilities are online again"
topic_id: 2190
author: "broeggle"
date: 2006-11-26T15:21:08+00:00
last_activity: 2006-11-30T02:49:12+00:00
last_author: "Krok"
sticky: false
locked: false
post_count: 17
---

<div class="post" data-post-id="15345" data-author="broeggle" data-date="2006-11-26T15:21:08+00:00" data-subject="Class Abilities are online again">

Hi there, 

as some of you might already noticed, the Class Abilities section is up again.

I think they were removed at the last redesign but now I fixed and recoded some and now they work again.

For those who still don't know that I'm talking about:

Click on the 'Classes' Item in the menu, and then you select your class :)

It shows you which spellbook pops where, on who etc. and you can also search for Spells/Skills/Songs and the according Spellbook, Manual Songbook.

The original code was from 'Isabo'.

A short summary what I did:

- putting the thing into the new layout

- fixed a bunch of security issues, so the db won't be flushed every now and then :)

Was more work than it sounds :)

Still todo: 

- Fix the admin menu, so even some selected mortals may update the db :)

- An other/better colorsheme :)

regards,

broeggle

</div>

<div class="post" data-post-id="15350" data-author="Leaf" data-date="2006-11-26T18:55:37+00:00" data-subject="">

Great job done.  However please change some of the colors...  Its hard on

the eyes.

</div>

<div class="post" data-post-id="15351" data-author="*Splork*" data-date="2006-11-26T21:27:40+00:00" data-subject="">

Colors have been adjusted, let us know what you think.

I will add the missing spells, songs, and skills sometime this week.

Splork

</div>

<div class="post" data-post-id="15352" data-author="Weasel" data-date="2006-11-26T21:36:06+00:00" data-subject="">

looks good cheers

</div>

<div class="post" data-post-id="15357" data-author="Ingold" data-date="2006-11-27T04:54:20+00:00" data-subject="Nice Job">

Could it be possible to change the red also to a bold white, it's a little strong, but nice to see this up again.

</div>

<div class="post" data-post-id="15358" data-author="Krok" data-date="2006-11-27T05:16:09+00:00" data-subject="">

Hurts my eyes bad, but I can survive it, cause now I don't have to open eqlist :)) wooohooo

</div>

<div class="post" data-post-id="15359" data-author="claw" data-date="2006-11-27T10:24:39+00:00" data-subject="">

I'm colorblind red/green and have trouble seeing skill names unless I highlight them or cut and paste the table to notepad.

any chance of a change?

</div>

<div class="post" data-post-id="15360" data-author="Leaf" data-date="2006-11-27T12:09:03+00:00" data-subject="">

I'm also slightly color blind, on green & red.  Which was y I stated the

colors are hard on the eyes.  The name of the skills kinda blends in with the

back ground being the deep red.  Hum... maybe yellow or a sky blue?

</div>

<div class="post" data-post-id="15361" data-author="Krok" data-date="2006-11-27T12:28:10+00:00" data-subject="">

I might be boring, but can't it just be black on white with some color dividers between the spells/skills? I bet everyone can read that.

</div>

<div class="post" data-post-id="15362" data-author="broeggle" data-date="2006-11-27T12:36:36+00:00" data-subject="">

grats, you guys seem to have something 'similar to atypical achromatopsia aka cone monochromat' :)

I tested the site with this really nice color blindness viewer  ([http://colorfilter.wickline.org/](http://colorfilter.wickline.org/)) - and I really have to admin, it's really hard to read with that.  

cast 'cure colorblindness' ClassAbilites :)

We will fix that, perhaps b&w are the best option :)

</div>

<div class="post" data-post-id="15364" data-author="13" data-date="2006-11-27T13:36:30+00:00" data-subject="">

"Sight for weaks!" (tm) Quake

</div>

<div class="post" data-post-id="15369" data-author="*Splork*" data-date="2006-11-28T00:03:31+00:00" data-subject="">

Ive tinkered with it some more.

What are the thoughts now?

I am having an extremely difficult time figuring out how to change the red link color so...

Splork

</div>

<div class="post" data-post-id="15370" data-author="banedon" data-date="2006-11-28T07:11:11+00:00" data-subject="">

Color scheme looks good now.  Only other thing I could think of is possibly make the font size a lil bigger for all of us older farts who are too lazy to use our readin glasses.

</div>

<div class="post" data-post-id="15371" data-author="Weasel" data-date="2006-11-28T08:33:32+00:00" data-subject="">

To change link color, add class="weasel" (for example) to the href tags, so that they all look like this (use search and replace):

{a class="weasel" href="http://whatever"}spellname{/a}

then you can add the following to the stylesheet at themes/SlothIII/style/style.css or whereever it is:

a.weasel:link, a.weasel:visited, a.weasel:active {

   color:#ffffff;

   text-decoration:none;

   }

a.weasel:hover {

   color:#ff0000;

   text-decoration:underline;

   }

..adjust to suit.. that would give you white text that changes to red when you mouse over the text.. text-decoration you can change or do whatever is on existing link css..  it will basically use default link behavior except for whatever you add here..

</div>

<div class="post" data-post-id="15372" data-author="bubba" data-date="2006-11-28T16:51:12+00:00" data-subject="">

Yeah, have to say that red text on black background is hell for colorblind people like me.  You might want to remember that if you're using a tank reporter with red text :-)

</div>

<div class="post" data-post-id="15376" data-author="Gimlet" data-date="2006-11-29T05:53:17+00:00" data-subject="">

Nobody heals tanks no matter what color tags u use in your tank reporter :)

</div>

<div class="post" data-post-id="15388" data-author="Krok" data-date="2006-11-30T02:49:12+00:00" data-subject="">

What's 'healing' btw? :P

</div>
