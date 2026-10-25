---
title: "Question re: Pets/Supps"
topic_id: 4109
author: "Nyx"
date: 2013-08-14T00:37:37+00:00
last_activity: 2013-08-23T17:40:51+00:00
last_author: "Magi"
sticky: false
locked: false
post_count: 2
---

<div class="post" data-post-id="34384" data-author="Nyx" data-date="2013-08-14T00:37:37+00:00">

Hi all,

I thought I'd finally post about this "issue" and see if someone else can help me understand this one.

The short story: 

My pet combo is often 2 x dracolich + 1 x eudaemon or nightmare.

I can have this combo _only_ if I supplicate first and animate (or summon undead) after the supplicant has arrived. I cannot supplicate if I have 2 x dracolich up.

I'm not sure why this is the case as my available follower points should allow this combo all the time.

The longer story, with numbers:

What works

You aren't controlling any followers right now. [0.0]

Akasha answers your request!

Flopsy the eudaemon appears in a flash of rainbow light!

Flopsy the eudaemon starts following you.

You could control far more followers than you have now. [**0.8**]

cast 'animate dead' corpse dracolich

cast 'animate dead' corpse dracolich

You probably couldn't control any more followers. [**4.7**]

What doesnt work

(Brilliant Red Aura) An immense skeletal dracolich tests the will of its master.

(Brilliant Red Aura) An immense skeletal dracolich tests the will of its master.

You could probably handle one or two more followers than you have now. [**3.9**]

cast 'supp' eudaemon:

Akasha decides that you have enough followers already.

How many follower points can I have?

cast 'summon undead' 3 banshee

You weave the threads of magic masterfully!

A banshee starts following you.

A banshee starts following you.

A banshee starts following you.

You probably couldn't control any more followers. [**4.8**]

cast 'summon' 6 spectre

Ok.

A spectre starts following you.

A spectre starts following you.

A spectre starts following you.

A spectre starts following you.

A spectre starts following you.

A spectre starts following you.

You probably couldn't control any more followers. [**5.0**]

If you made it this far, thanks for your time and I appreciate any constructive feedback you may have.

</div>

<div class="post" data-post-id="34393" data-author="Magi" data-date="2013-08-23T17:40:51+00:00">

Guess of the day:

I think the issue is that extra control granted by the Control Horde skill can only be used on necro pets.

When casting supplication, the game checks your unmodified pet limit, without recognizing that you 'should' be allowed more since you already have several undead.

When you make an undead pet, it checks against the higher limit, modified by your control horde skill.

</div>
