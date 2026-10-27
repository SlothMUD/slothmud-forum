---
title: "Regen Mode"
topic_id: 1617
author: "jezer"
date: 2005-12-25T13:51:34+00:00
last_activity: 2005-12-27T22:46:24+00:00
last_author: "Medios"
sticky: false
locked: false
post_count: 7
---

<div class="post" data-post-id="9921" data-author="jezer" data-date="2005-12-25T13:51:34+00:00" data-subject="Regen Mode">

Ok, I've got 945hp's atm so its time to do this regen thing properly! I want to put on my regen gear as fast as I see other people do it... so it was time to build myself a regen script.

I was told that put all - remove all - wear all was what makes the switch to regen mode fast. However when I set about to make this script it became huge. 

I thought to get another container and keep all my regen stuff in that to help make the switch - that way I can add stuff to the regen robe without changing the script, but I swear it is still slower than other peoples.

On a side note, I was thinking it might be easy for some code to be implemented that allows us to tag our eq, so maybe we can switch to regen quicker and safer? Just an idea... anyways...

Please cast your eye over these commands and comment where I can pickup speed, and tell me if I am in danger of being pthiefed well running this script. Bare in mind I store a lot of general junk in my robe as well as the container with my regen stuff. Also, what do you think about removing all eq and just wearing regen, as this could make you extremely vulnerable if you are attacked while regenning?

Regenon...

remove mysteries;get swirling mysteries;remove all;wear orc;wear orc;wear mysteries;put all swirling;remove mysteries;put swirling mysteries;get persecution mysteries;get all persecution;put persecution mysteries;wear all;hold bamboo

Regenoff...

remove mysteries;get persecution mysteries;remove all;wear orc;wear orc;wear mysteries;put all persecution;remove mysteries;put persecution mysteries;get swirling mysteries;get all swirling;put swirling mysteries;wear all

</div>

<div class="post" data-post-id="9923" data-author="Shara" data-date="2005-12-25T22:55:43+00:00" data-subject="">

If you wear a single piece of eq at a time, you get lag. The trick is to use the command "wear all" literally. So put all your stuff away, get all the stuff you want out, and type wear all. <img src="/images/smilies/icon_e_smile.svg" alt=":)" title=":)" width="15" height="15" class="smiley nozoom">

</div>

<div class="post" data-post-id="9924" data-author="Tetsulunathaya" data-date="2005-12-25T23:25:19+00:00" data-subject="">

Heres a chain that should elimate a few 'wear' commands, and speed you up a little. Also, if you plan on not switching out your orcish rings, cursing them can help eliminate a few commands and speed things up (as they won't be removed, so you don't have to get them back out of the robe after the put all command). If you don't want to curse them, you might try get all.orc "swirling/persecution", but its been forever, and I can't remember if that works for getting things out of robes.

Also, this will depend on the size of your additional robes, whether or not your main robe will fit in them (if it won't, you can eleminate the 'get mysteries \*' lines as well).

I'm by no means an expert, but trying to help <img src="/images/smilies/icon_e_smile.svg" alt=":)" title=":)" width="15" height="15" class="smiley nozoom">

Regenon....

> <strong>Quote:</strong>
> Remove All;
> 
> Get swirling mysteries;
> 
> put all swirling;
> 
> get orc swirling; 
> 
> get orc swirling;
> 
> get mysteries swirling;
> 
> put swirling mysteries;
> 
> get persecution mysteries;
> 
> get all persecution;
> 
> put persecution myseries;
> 
> wear all;
> 
> hold bamboo

Regenoff...

> <strong>Quote:</strong>
> remove all;
> 
> get persecution mysteries;
> 
> put all persecution;
> 
> get orc persecution;
> 
> get orc persecution;
> 
> get mysteries persecution;
> 
> put persecution mysteries;
> 
> get swirling mysteries;
> 
> get all swirling;
> 
> put swirling mysteries;
> 
> wear all;

</div>

<div class="post" data-post-id="9928" data-author="Gti" data-date="2005-12-27T04:45:19+00:00" data-subject="">

hi jez,

i'm no expert myself too. but the following tips help:

\- as mentioned, curse items that u are wearing in both regen/tank mode. so when u rem all, they stay worn on ur body.

\- the put all.xxx mysteries or get all.xxx mysteries helps too

\- use 1 robe per set of eq and set a variable for that robe. so when u change robe, u dun need to change all ur script. u just need to update ur variable

\- last of all, if u do take out few robes during eq change, prioritise which robe to put back 1st. so IF unfortunately u get pthiefed, the chances of losing a robe wif most goodies remains lower.

on being pthiefed, not all rooms are safe rooms. to check, u can go in n try push urself out. if u can push urself out, chances that pthief will hang there n push u out when u stand.

</div>

<div class="post" data-post-id="9929" data-author="Vixn" data-date="2005-12-27T07:45:11+00:00" data-subject="">

People often think if room is no-cast that should be the safe room. but it is completly wrong. there are just some exaples of rooms wich people usually consider as safe:

1\. Scribes [BH] - it's no-cast, no-steal room, but you are still pushable, so you'd better rest before re-eqiup.

2\. Dream Weaver's regen bonus room [BH] - good place for pthiefing. re-equip 1e,1n or 1w from this room. Don't have much coins on you if you gonna sleep here.

3\. Ticket seller [AH] - the one who sells ticket to Valk. It's no-cast room, but it isn't no-steal.

4\. Master John's Inn [Island] - it isn't no-steal.

It's very short and incomplete list, I post it only to show there are some few real safe rooms in this world.

</div>

<div class="post" data-post-id="9930" data-author="Gnu" data-date="2005-12-27T08:58:20+00:00" data-subject="">

> <strong>Vixn wrote:</strong>
> 1\. Scribes [BH] - it's no-cast, no-steal room, but you are still pushable, so you'd better rest before re-eqiup.

You'd better never re-equip in BH scribe, since hymn of the morning start works there very well...

</div>

<div class="post" data-post-id="9931" data-author="Medios" data-date="2005-12-27T22:46:24+00:00" data-subject="">

Hymn of the morning star does nothing if your resting, only stands you if sleeping.

> <strong>Vixn wrote:</strong>
> 3\. Ticket seller [AH] - the one who sells ticket to Valk. It's no-cast room, but it isn't no-steal.

This isnt correct. All vk ticket sellers are nosteal and nocast. The ones on BH AH and SS are also outdoors. You can be pushed out of these 3 also so hymn applies if you afk.

Top of the Palisade

 Aisholm's sentinels use a walkway on the palisade to watch the nearby

lands. The walkway only follows the wooden parts of the wall, the fourth

being a single enormous rock. To the west you can see nothing but frozen

tundra. The coast is nearby to the south. The fire that burns on the

seaside tower is clearly visible from here.

Exits: East 

A large, arctic rat eyes you suspiciously from a deep shadow.

A mystical looking dwarf stands ready to sell his tickets.

Uqate the ticket seller glows with a bright light!

\<924hp 727ma 235mv\>

i

l rYou are carrying:

a battered suitcase

\<924hp 727ma 236mv\>

l rat

This rat is almost two feet long! White, thick fur covers its entire

body, and it has long sharp incisors.

An arctic rat is in excellent condition.

You attempt to peek at the inventory:

a lamb shoulder steak

\<924hp 727ma 237mv\>

steal steak rKrok[Clan:The Dogs of War]\> 'lo mike too'

\<924hp 727ma 238mv\>

steal steak rat

No you don't...

\<924hp 727ma 238mv\>

push rat e

You throw yourself against an arctic rat and push him to the east!

An arctic rat leaves east.

\<924hp 727ma 221mv\>

e

Walkway at the Ladder

Exits: East West Down 

A large, arctic rat eyes you suspiciously from a deep shadow.

A soldier looks like he would rather be elsewhere. Preferably indoors.

\<924hp 727ma 220mv\>

steal steak rat

Oops..

An arctic rat misses you with his bite.

Mike

</div>
