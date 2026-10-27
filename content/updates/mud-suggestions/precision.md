---
title: "precision"
topic_id: 1791
author: "Falsra"
date: 2006-03-21T14:19:11+00:00
last_activity: 2006-03-24T17:42:51+00:00
last_author: "Autolycos"
sticky: false
locked: false
post_count: 11
---

<div class="post" data-post-id="11613" data-author="Falsra" data-date="2006-03-21T14:19:11+00:00" data-subject="precision">

Most of my friends consider sloth to be very complex.

This is a reason they play web based rpg games which do not

require much attention and understanding,( in fact idea of

bulding web based simplified sloth clone is not bad at all ).

From this side i do not want to make a complex sloth even more complex.

From another side i still want to share my thoughts with players and immortals:

Look , when we fight a mob we consider mob only in general, we do not think

mob has or does not have say legs ot head, and we do not care which

part of mob's body we are hitting.

With "presicion" skill we may give some advantages to warriors and monks, letting

them to hit most vulnerable mob's parts. This skill also would make them

read mob descriptions to figure out which parts of body they should hit to do 

most damage.

We can define that a mob may have some parts - head,body,arms,legs,tail,wings.

Each part may have or may not have damage modifier.

Say, all fish-type mobs have no legs,no arms and no wings - only head, body and tail.

Useless to beat them on legs,arms or wings - damage modifier set to zero for arms/legs/wings.

Soldiers may have armored body and head - damage modifier set to say 0.9 

and not armored legs and arms - damage modifier set say to 1.1

Warriors and monks with learned presicion skill may direct their hits to any part of mob

by typing "presicion head" or, say, "precision tail".

Warriors and monks who set "presicion " without params would do their hits randomly.

The same way would act players with unlearned "presicion" skill.

Yes, its a tweaking for players without Wa or Mo in classo, but those players basically

do not rely on physical damage much.

Of course, precision skill would affect followers most of all - followers unable to 

learn this skill and would do thier hits randomly.

But we all agree necromancers are still kinda overpewered - "presicion" skill will bring

some balance into the game from this point of view <img src="/images/smilies/icon_twisted.svg" alt=":twisted:" title=":twisted:" width="15" height="15" class="smiley nozoom"> \*bite me\*

Thank for attn <img src="/images/smilies/icon_e_smile.svg" alt=":)" title=":)" width="15" height="15" class="smiley nozoom">

/falsra

 <img src="/images/smilies/icon_twisted.svg" alt=":twisted:" title=":twisted:" width="15" height="15" class="smiley nozoom"> <img src="/images/smilies/icon_twisted.svg" alt=":twisted:" title=":twisted:" width="15" height="15" class="smiley nozoom">

</div>

<div class="post" data-post-id="11616" data-author="Autolycos" data-date="2006-03-21T14:43:12+00:00" data-subject="">

wow, thats cool.. i never really gave that much thought to a direct battle 1 on 1. but it does make perfect sense.. if i were to fight irl, i would look and concentrate on my opponents most vulnerable spots. 

nicely don Falsra <img src="/images/smilies/icon_e_smile.svg" alt=":)" title=":)" width="15" height="15" class="smiley nozoom">

</div>

<div class="post" data-post-id="11630" data-author="Harlot" data-date="2006-03-21T17:22:03+00:00" data-subject="nice idea but you suggest the following?">

kick \<MOB\> \<target\> ? example being

kick sash body 

punch sash head

or my personal favorite..

flick auto ear

would be interesting additon but the coding would seemingly take forever...maybe not...don't know squat about coding but nice....fresh ideas always welcomed..even more so when they are interesting

 <img src="/images/smilies/icon_razz.svg" alt=":P" title=":P" width="15" height="15" class="smiley nozoom">

</div>

<div class="post" data-post-id="11632" data-author="Autolycos" data-date="2006-03-21T17:28:43+00:00" data-subject="">

sounds good.. but i prefer

poke harlot eye

twist harlot nipple

and the best!

wetwillie harlot ear! <img src="/images/smilies/icon_twisted.svg" alt=":twisted:" title=":twisted:" width="15" height="15" class="smiley nozoom"> 

take dat ya hooch!

</div>

<div class="post" data-post-id="11633" data-author="kjartan" data-date="2006-03-21T17:46:36+00:00" data-subject="">

In D\&D and other tabletop RPGs this mechanic is referred to as "called shots". Generally you have a reduced chance to hit coupled with improved effects. It doesn't fit very well with the vague idea of the "hit point" in D\&D, and so base D\&D doesn't use the mechanic.

We have mob species. So, we could easily code stuff like "all human-type creatures have two legs, two eyes, ..." but anything that required mob-by-mob modification would be very difficult. Which means we could make a fairly crappy implementation of this that was about 80% correct as to which mobs have which body parts, but getting the rest of it right would be an unbelievable pain.

If you tried to hit the wings on a fish, I would be inclined to say "You can't do that, it's a fish" as opposed to just reducing your damage to zero.

Making per-mob effects for the different body parts is probably not going to happen - that's a fair amount of work per mob, and there are a lot of mobs. So, we would need general global effects, like "hitting humans in the head does 2x damage but has 50% reduction of hit chance" or something.

</div>

<div class="post" data-post-id="11636" data-author="Krok" data-date="2006-03-21T18:06:52+00:00" data-subject="">

Erm, necros are overpowered, but our cleric supps would suffer from that :((

</div>

<div class="post" data-post-id="11637" data-author="Autolycos" data-date="2006-03-21T18:09:37+00:00" data-subject="">

QUICK! <img src="/images/smilies/icon_eek.svg" alt=":shock:" title=":shock:" width="15" height="15" class="smiley nozoom"> 

someone run over to Kj's house and unplug his keyboard! <img src="/images/smilies/icon_evil.svg" alt=":evil:" title=":evil:" width="15" height="15" class="smiley nozoom">

</div>

<div class="post" data-post-id="11639" data-author="kjartan" data-date="2006-03-21T18:45:58+00:00" data-subject="">

I'm using a laptop! Muahahahahah!

</div>

<div class="post" data-post-id="11765" data-author="Falsra" data-date="2006-03-24T08:58:40+00:00" data-subject="">

> <strong>\*kjartan\* wrote:</strong>
> In D\&D and other tabletop RPGs this mechanic is referred to as "called shots". Generally you have a reduced chance to hit coupled with improved effects.

I remember the thread about D\&D license and rules, but honestly i do not

remeber either obliged sloth's creators follow D\&D license or not.

If you cannot impelement "precision" idea in another way but only as 

"called shots" with "reduced chance to hit coupled with improved effects"

due D\&D license, then i doubt we need such implementation since

average damage will stay the same.

I meant it might look something like:

\>precision arms

Ok. You are directing your hits to enemy's arms now.

\>kill nose

A bottle nosed dolphin hates your guts!

You miss a bottle nosed dolphin's arms with your pierce.

You miss a bottle nosed dolphin's arms with your pierce.

You miss a bottle nosed dolphin's arms with your pierce.

You miss a bottle nosed dolphin's arms with your pierce.

You miss a bottle nosed dolphin's arms with your pierce.

\>say Oops, i have to figure out its most vulnerable part.

You say 'Oops, i have to figure out its most vulnerable part.'

\> precision

Ok. You hit your enemy randomly.

You massacre a bottle nosed dolphin's head to small fragments with your pierce.

A bottle nosed dolphin misses you with her crush.

A bottle nosed dolphin misses you with her crush.

A bottle nosed dolphin misses you with her crush.

A bottle nosed dolphin misses you with her bite.

You miss a bottle nosed dolphin's wings with your pierce.

You miss a bottle nosed dolphin's legs with your pierce.

You massacre a bottle nosed dolphin's body to small fragments with your pierce.

You brutally massacre a bottle nosed dolphin's tail with your pierce.

\>presicion tail

Ok. You are directing your hits to enemy's tail now.

You brutally massacre a bottle nosed dolphin's tail with your pierce.

A bottle nosed dolphin misses you with her crush.

A bottle nosed dolphin misses you with her crush.

A bottle nosed dolphin misses you with her crush.

A bottle nosed dolphin misses you with her bite.

You brutally massacre a bottle nosed dolphin's tail with your pierce.

You brutally massacre a bottle nosed dolphin's tail with your pierce.

You brutally massacre a bottle nosed dolphin's tail with your pierce.

You brutally massacre a bottle nosed dolphin's tail with your pierce.

<img src="/images/smilies/icon_razz.svg" alt=":P" title=":P" width="15" height="15" class="smiley nozoom">

/falsra

</div>

<div class="post" data-post-id="11768" data-author="kjartan" data-date="2006-03-24T17:14:12+00:00" data-subject="">

Nah, we don't have to follow D\&D's license, and called shots aren't solely a D\&D idea anyway. We sometimes use ideas from D\&D because they have a lot of good ideas.

I think the main problem with precision is that we don't have perfect categorization of mobs by species, and the species themselves don't necessarily specify exactly what parts a creature has (e.g., does a demon necessarily have horns?), so there would be a fair amount of inappropriate targets. The effort to fix this would be so great that it wouldn't ever get fixed.

If precision gave you, say, 2x damage improvement for hitting the right spot with no reduced chance of hitting, then the effect would be that suddenly everybody is doing twice as much melee damage all the time, and we don't want that. (You would spend relatively little time figuring out the vulnerable spot, unless it kept changing, and it's sort of hard to explain why it would change.) If it did 1.1x as much damage, then you would have trouble telling what the right spot was because the messages would almost always be the same for the vulnerable spot or another spot.

</div>

<div class="post" data-post-id="11769" data-author="Autolycos" data-date="2006-03-24T17:42:51+00:00" data-subject="">

i don't know Kj, this does look kinda cool....

\>presicion ego

Ok. You are directing your hits to your enemy's ego now. 

You brutally massacre Clink's ego with your pierce. 

Clink misses you with his crush. 

Clink misses you with his slash. 

Clink misses you with his cleave. 

Clink misses you with his wit. 

You viciously massacre Clink's ego with your pierce. 

You viciously massacre Clink's ego with your pierce.

You viciously massacre Clink's ego with your pierce.

You viciously massacre Clink's ego with your pierce.

lalalala <img src="/images/smilies/icon_twisted.svg" alt=":twisted:" title=":twisted:" width="15" height="15" class="smiley nozoom">

</div>
