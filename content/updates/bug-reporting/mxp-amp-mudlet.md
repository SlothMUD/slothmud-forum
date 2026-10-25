---
title: "MXP &amp; Mudlet"
topic_id: 5002
author: "cnl"
date: 2021-01-04T20:42:16+00:00
last_activity: 2025-07-31T01:40:39+00:00
last_author: "cnl"
sticky: false
locked: false
post_count: 8
---

<div class="post" data-post-id="39657" data-author="cnl" data-date="2021-01-04T20:42:16+00:00" data-subject="MXP &amp;amp; Mudlet">

There is a bug where Mudlet does not display store items on list command.

It is caused by the unescaped & (ampersand) chars in the list.

I can't find a good authoritative resource on the MXP specification but I think this issue is at least partially on the SlothMUD side.

Here is a capture of the traffic. 

![](https://raw.githubusercontent.com/wiki/CodeAndLoathing/mudlet-slothmud/images/mxp_capture.png)

<ESC>[6z puts it into lock secure MXP mode. Until terminated with <ESC>[7z all loose "&" should be encoded as "&" - if I'm reading the spec docs correctly.

Possible resolutions ?

- Sloth can encode plain text ampersands inside lock secure MXP blocks as &

- Sloth can switch to using temp secure mode ( <ESC>[4z ), prefixing the individual MXP tags instead of flagging an entire block, maybe each terminated with <ESC>[3z.

Workaround

- Players can disable MXP (can be toggled on/off in sloth by typing mxp). Most variables/data you would get from MXP can be pulled out of MSDP, which works well in Mudlet, however you don't get the clickable links or menu links this way that you would with MXP. (not a huge loss for most players though I'm betting)

Feature request: MSDP variable that contains room description and roomnvum. I don't think adding it to CHARACTER_LOCATION is ideal since a lot of the time I would want to turn it off to reduce data, but sometimes I want to read the room descriptions - such as when mapping or exploring an area.

</div>

<div class="post" data-post-id="39658" data-author="Gorka" data-date="2021-01-04T22:40:23+00:00" data-subject="Re: MXP &amp;amp; Mudlet">

> **cnl wrote:**
> Feature request: MSDP variable that contains room description and roomnvum. I don't think adding it to CHARACTER_LOCATION is ideal since a lot of the time I would want to turn it off to reduce data, but sometimes I want to read the room descriptions - such as when mapping or exploring an area.

Does your roomnvum request differ from msdp.CHARACTER_LOCATION.ROOM.VNUM?

MXP is very bugged at the moment, I have to disable it. If I don't, typing look in a room gives me no room description at all.

Regarding MSDP gripes... Disease often crashes the affects variable to a null value - I suspect probably also a syntax issue. I'm not sure it's disease in general or just slurrrr. This is very annoying on EU, as something weird is up with the diseases there. Another thing the mud does a bad job of is handling fighting multiple enemies. MSDP only reports back info on the one your engaging - not to mention there is a brief second after a fight you can literally just walk out of the room while fighting other mobs.

</div>

<div class="post" data-post-id="39659" data-author="cnl" data-date="2021-01-05T00:06:26+00:00" data-subject="Re: MXP &amp;amp; Mudlet">

I am aware of  msdp.CHARACTER_LOCATION.ROOM.VNUM but I was thinking we could have something like  

msdp.ROOM_DESCRIPTION, containing 

  msdp.ROOM_DESCRIPTION.VNUM

  msdp.ROOM_DESCRIPTION.DESCRIPTION 

You are right this would be partially redundant with CHARACTER_LOCATION in that both would contain room VNUM.

My reason for wanting this redundancy is my current understanding of MSDP in Mudlet is that a variable like  msdp.CHARACTER_LOCATION updates in a relatively atomic manner. ie, all the child properties are updated at once and a single event for the parent being updated is fired.

But if you had a second msdp variable like msdp.ROOM_DESCRIPTION you would have a separate event fire.

If you were trying to link Room VNUM and Description from these 2 different sources, and the msdp.ROOM_DESCRIPTION updated immediately before msdp.CHARACTER_LOCATION updated - you could tie a description to invalid room vnum. Having the room VNUM key both variables but allowing a more descriptive room description variable that can be turned on and off seems like it might be worthwhile.

it is more a theoretical problem I guess than one that has any impact necessarily on game play since really I want to shuttle the room description to a separate window not do anything too complicated with it - still, it would feel cleaner.

</div>

<div class="post" data-post-id="39660" data-author="cnl" data-date="2021-01-05T02:00:04+00:00" data-subject="Re: MXP &amp;amp; Mudlet">

the missing room description issue you describe with MXP is essentially the same issue btw.

it's triggered by an ampersand in an MXP secure block and will continue until it hits a semi-colon. I feel like this is rather daft behavior on Mudlet's part - there should be some kind of sanity check on their ampersand entity parsing.

you can see this behavior play out in the dreamweaver store (which contains a ; in the end text) vs the library which does not. listing at the library (assuming at least one book with a & prefix) will wreck your room descriptions until you encounter a semi-colon.

</div>

<div class="post" data-post-id="39661" data-author="Gorka" data-date="2021-01-05T11:24:23+00:00" data-subject="Re: MXP &amp;amp; Mudlet">

IIRC, there is a way to turn on the Room Num so it shows in the description part when you look in a room. I tried to remember the command but couldn't. Shatterhand/Bandit would probably know it.

It would then be possible, using a trigger, to capture the text between the room num and the "Exits" line of the room description. Then parse out those values individually if you really wanted to capture these two values.

EDIT: Command is "roomvnums on"

Room 25443: Slab of Volcanic Rock

   The ground here has cooled somewhat, and is no longer uncomfortable to

walk upon like the rest of this place.  Steam still rises from the cracks

that are evident.  Each of the splits in the rocks are caused not only by

the gases escaping from below, but also by the rate at which the stone

cooled.  The smooth surface of the slab here reflects the many different

colors of the plane.

Exits: North  West

</div>

<div class="post" data-post-id="39662" data-author="cnl" data-date="2021-01-05T17:36:56+00:00" data-subject="Re: MXP &amp;amp; Mudlet">

that works. thanks

</div>

<div class="post" data-post-id="40193" data-author="*teker*" data-date="2025-07-14T03:56:16+00:00" data-subject="Re: MXP &amp;amp; Mudlet">

The shop listing MXP issue should be fixed at next reboot.

</div>

<div class="post" data-post-id="40195" data-author="cnl" data-date="2025-07-31T01:40:39+00:00" data-subject="Re: MXP &amp;amp; Mudlet">

I tested this and it does appear fixed. thanks!

this was a common source of confusion for people checking out sloth so this is good news.

</div>
