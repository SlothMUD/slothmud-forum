---
title: "Weapon Related Stuff"
topic_id: 563
author: "12345"
date: 2004-11-02T13:05:45+00:00
last_activity: 2004-11-02T15:22:30+00:00
last_author: "12345"
sticky: false
locked: false
post_count: 3
---

<div class="post" data-post-id="2525" data-author="12345" data-date="2004-11-02T13:05:45+00:00" data-subject="Weapon Related Stuff">

Weapons are becoming more in depth lately. For instance, two-handed weapons get increased bonuses, some weapons proc, and other are just weapons. (Did I also hear something about warriors and blunted weapons?) 

Would it be possible to create an improved identify scroll or something similar? Basically looking for something that would identify procs. Such as the effect and/or approximate damage/damage type and percent chance of firing. A help file on the different weapon types and bonuses might also be useful.

Or perhaps such things already exist and I'm just silly? <img src="/images/smilies/icon_e_biggrin.svg" alt=":D" title=":D" width="15" height="15" class="smiley nozoom">

</div>

<div class="post" data-post-id="2526" data-author="Alberich" data-date="2004-11-02T13:23:59+00:00" data-subject="">

I do not know that proc dam would get shown regardless, as alot of procs are spells, and there is nothing in most spells helpfiles about damage.

that said, it would be really cool if even just masterful identify would tell you if something was a proc weapon, and/or what it's proc is,or make a seperate id scroll (although since masterful identify currently only has 1 purpose, and is very very rarely needed, it would be nice to give it added effect)

</div>

<div class="post" data-post-id="2527" data-author="12345" data-date="2004-11-02T15:22:30+00:00" data-subject="">

I'll agree to a certain extent about proc spells. I don't think they're straight spells in most cases, though it's entirely possible I'm wrong. However, I'm not familiar with a cone of cold spell in game, and weapons that spew out demons and emerald rays don't seem to be strictly spell related. This would seem more along the lines of:

proc = is\_wielding(ch)-\>proc

if (percent()\<proc-\>percent) {

 dam = dice(proc-\>no\_dice, proc-\>dam\_dice) + proc-\>dam\_plus;

 damage(ch, victim, dam, 0, WEAR\_NONE);

 send\_to\_char(ch, proc-\>ch\_dam\_message);

 send\_to\_char(victim, proc-\>target\_dam\_message);

 act(proc-\>room\_dam\_message, ch, NULL, victim, TO\_NOTVICT);}

Or something similar... I understand that spells are secret and have been since the creation of the game, but procs seem genuinely disconnected from actual spells. Also, we know how often spells fire (roughly 95%), so this isn't exactly asking for something overpowered either...

That said, I think the masterful suggestion is a great idea. The only real issue I have with it is that only high level bards and Avatars have the identify spell. Since we have wonderful folks like Shyla and Blackmore, this may be acceptable, but otherwise, it begs the addition of a scroll.

</div>
