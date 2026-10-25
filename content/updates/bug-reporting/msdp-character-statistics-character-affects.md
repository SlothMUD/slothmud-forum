---
title: "msdp CHARACTER_STATISTICS, CHARACTER_AFFECTS"
topic_id: 5084
author: "cnl"
date: 2023-01-30T21:47:52+00:00
last_activity: 2025-04-25T21:08:29+00:00
last_author: "Hung"
sticky: false
locked: false
post_count: 24
---

<div class="post" data-post-id="40003" data-author="cnl" data-date="2023-01-30T21:47:52+00:00" data-subject="msdp CHARACTER_STATISTICS, CHARACTER_AFFECTS">

These are 2 possibly quite unrelated issues

1) sometimes CHARACTER_STATISTICS goes crazy and reports *A LOT*

See - [https://imgur.com/KCRVzF6](https://imgur.com/KCRVzF6)

each cyan dollar is an individual send of the complete msdp CHARACTER_STATISTICS data.

Here's an alternate view [https://pastebin.com/nZeXL6ib](https://pastebin.com/nZeXL6ib) 

It's sending the complete data multiple times around mob death for some unknown reason.

Also on scepter rewards it often goes crazy : [https://imgur.com/0R6VGuZ](https://imgur.com/0R6VGuZ)

I feel like there are times I've seen it not doing this so perhaps inconsistent. 

EDIT: this only seems to happen if I'm in a group with more than 1 person. if I'm the only one in a group I'm not seeing this crazy sending.

2) sometimes CHARACTER_AFFECTS data stops getting sent to my char. 

BUT - other chars in same group may still be getting it (confirmed)

This only seems to happen on Fuligin and normally around lag time but I don't know what to make of it.

multiple attempts to UNREPORT, REPORT don't fix it. I just have to wait for whatever is lagging it to go away before it will work again. same with restarting mud client - doesn't fix the issue. Will sit will null msdp data in variable till it suddenly starts again. Weird thing is that it only affects my 1 char. But it happens multiple times a day and can last 5 minutes or so or even longer

EDIT2: it also seems like the SEND msdp command doesn't work it just returns an empty string for any given variable. if I'm reading the docs correctly SEND should return the value of named variable 1x vs REPORT which returns them on every change ( in theory). I was thinking of using SEND to generally decrease the reporting on some variables to times when i need them. I suppose if I really wanted it I could manage with tracking and having the relevant handler send UNREPORT on receiving data.

</div>

<div class="post" data-post-id="40006" data-author="cnl" data-date="2023-02-05T08:23:47+00:00" data-subject="Re: msdp CHARACTER_STATISTICS, CHARACTER_AFFECTS">

the freezing of msdp affects seems somehow related to items worn.

by that i mean, when it is occurring, when it's having one of it's freezing episodes for lack of a better term, i can remove some items and msdp.CHARACTER_AFFECTS will resume reporting, and I can wear them again and it will stop reporting. i really can't get my head around because it's not one specific item but for example magma rings don't seem to do anything but removing things like instrument + soc, or the new mage belt from dk vk seem to have an impact where removing them will get regular reports again and wearing them will stop it.

and then after a while the whole thing unfreezes regardless. I'll try get some more detailed tests done next time it locks up.

</div>

<div class="post" data-post-id="40007" data-author="cnl" data-date="2023-02-11T22:13:48+00:00" data-subject="Re: msdp CHARACTER_STATISTICS, CHARACTER_AFFECTS">

```
A cloud of inky darkness envelops Insomnia.
<1312hp 1542ma 296mv -% @76450>
[2:24 pm] (overcast) -8 27341905847 -9.2
get all from ledge
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$
You get gold coins from on a ledge.
There were 4.0K coins.
You split 4.0K coins.  You keep 403 coins.
You get gold coins from on a ledge.
There were 4.0K coins.
You split 4.0K coins.  You keep 411 coins.
You get gold coins from on a ledge.
There were 4.0K coins.
You split 4.0K coins.  You keep 401 coins.
You get gold coins from on a ledge.
There were 5.8K coins.
You split 5.8K coins.  You keep 586 coins.
You get gold coins from on a ledge.
There were 4.0K coins.
You split 4.0K coins.  You keep 404 coins.
You get gold coins from on a ledge.
There were 4.1K coins.
You split 4.1K coins.  You keep 417 coins.
You get gold coins from on a ledge.
There were 4.0K coins.
You split 4.0K coins.  You keep 411 coins.
<1312hp 1542ma 297mv -% @76450>
[2:25 pm] (overcast) -8 27341905847 -9.2
```

rather extreme example in group today. group seemed to pause for 4 seconds while all all the updates to character_statistics came through. that's like 1,310 consecutive sends of the data

here's wireshark capture of a much smaller event just verifying it's actually coming from mud and not mudlet being weird [https://pastebin.com/gCcEwGcE](https://pastebin.com/gCcEwGcE)

EDIT: kind of interesting to note on the Wireshark capture that several of the values bounce back and forth to different values multiple times. Current value for intelligence bounces between 23 and 25, ac bounces between -8.7 and -9.2, and Charisma bonus varies between 2,5,7 and 10

</div>

<div class="post" data-post-id="40050" data-author="*teker*" data-date="2023-06-07T00:55:41+00:00" data-subject="Re: msdp CHARACTER_STATISTICS, CHARACTER_AFFECTS">

When I added those to the game I thought it would be more efficient to send them only when the data changes rather than on a regular interval like the older variables.  It sounds like you're seeing enough problems that maybe they should be switched back.  I took a quick glance at the code and I can understand why some of this may be happening.  I didn't imagine it would be this extreme.

</div>

<div class="post" data-post-id="40051" data-author="cnl" data-date="2023-06-07T16:14:29+00:00" data-subject="Re: msdp CHARACTER_STATISTICS, CHARACTER_AFFECTS">

CHARACTER_STATISTICS is the only one I've seen go crazy with over-reporting with the values bouncing about.

In general - I really like the ones that only report when something has changed.

BEING IN GROUPS or room with BARD SONGS are the primary triggers I see for CHARACTER_STATISTICS.

I kind of implemented my own SEND operation for it where on a timer I can request REPORT, get a valid response, and then UNREPORT till timer hits again.

CHARACTER_AFFECTS just seems to stop reporting sometimes, like it starts undergoing some kind of timeout. 

the number of certain types of eq like artifacts worn and the number of spells up seem to impact whether this will happen. I can trigger it pretty reliably. when it is occurring, switching to my shock gear and back is often enough to get an update or 2 to get through if my spell list has frozen.

</div>

<div class="post" data-post-id="40052" data-author="Gorka" data-date="2023-06-07T18:48:59+00:00" data-subject="Re: msdp CHARACTER_STATISTICS, CHARACTER_AFFECTS">

> ***teker* wrote:**
> When I added those to the game I thought it would be more efficient to send them only when the data changes rather than on a regular interval like the older variables.  It sounds like you're seeing enough problems that maybe they should be switched back.  I took a quick glance at the code and I can understand why some of this may be happening.  I didn't imagine it would be this extreme.

Hey Teker, how far back would you be willing to switch the code...  :twisted: My offer of sharing all the bugs and exploits I found while playing still stands - to the person who might restore the game back to some sort of sanity where risk and reward made it worth playing - in the traditional way "games" are supposed to work. I still maintain the game has become pointless now with free mana, solo epics, death procs and practically free drachma on public holidays. Limitless drachma is free any day if you know how... towards the end, that actually became the most enjoyable part of the game, finding new exploits out of pure boredom, as I had already acquired everything legally... but it just got absurd when illegal exploits couldn't keep up with legal exploits... that's when I quit. It's a joke now... it's sad. I never wanted to see the game ruined like it is. But apart from bothering Idjit about his coin collection, why would I play anymore? Everything I worked for, for years was made available to new players in months, through over powering and sling shotting.

There is a disease on EU that bugs CHARACTER_AFFECTS from memory. I forget which disease. I think some specific mob casted it, so I just stopped killing him on my runs. I suspected it might have been a special/reserved character issue, but it could just be malformed MSDP for that specific disease.

</div>

<div class="post" data-post-id="40142" data-author="*teker*" data-date="2025-01-06T22:49:22+00:00" data-subject="Re: msdp CHARACTER_STATISTICS, CHARACTER_AFFECTS">

Sorry it's been a while.  I've got some free time now so I'm starting to look at the code again.  Crashes and fixing exploits are likely to be my priorities.  Keep in mind that I've traditionally kept away from game play / balance decisions given that my highest mortal is only 4x40.

</div>

<div class="post" data-post-id="40147" data-author="cnl" data-date="2025-02-07T19:48:53+00:00" data-subject="Re: msdp CHARACTER_STATISTICS, CHARACTER_AFFECTS">

did you fix the CHARACTER_STATISTICS behavior? I turned it on for the first time in a long time today and noticed it wasn't going crazy - was just in a 2-man group though I guess I'll have to see in a larger group but if so thanks - that's awesome. i like being able to pulls things from it like AC and SAVES to display so that's great if it's workable again.

</div>

<div class="post" data-post-id="40150" data-author="*teker*" data-date="2025-02-12T15:48:58+00:00" data-subject="Re: msdp CHARACTER_STATISTICS, CHARACTER_AFFECTS">

I did make a code change but I'm not sure that it's live.  The change is to make CHARACTER_STATISTICS report every 0.5 seconds rather than each time the value changes.

I suspect both of these could be spamming at mob death due to warcry.  The affects get updated every time warcry is reissued and each time a group member joins in.  The code removes the existing affect which creates a change and then adds a new affect which creates a second change event.  You'd definitely see the number of events increase with group size.

</div>

<div class="post" data-post-id="40153" data-author="cnl" data-date="2025-02-13T01:20:29+00:00" data-subject="Re: msdp CHARACTER_STATISTICS, CHARACTER_AFFECTS">

huh. something else changed somewhere along the line then???

at least for now the behavior of CHARACTER_STATISTICS appears to be behaving very well

perhaps don't push out the new behavior yet - I'll monitor if it goes crazy again but it's being very minimal on the updates and not doing duplicates or thousands

</div>

<div class="post" data-post-id="40157" data-author="Hung" data-date="2025-03-03T02:37:02+00:00" data-subject="Re: msdp CHARACTER_STATISTICS, CHARACTER_AFFECTS">

Teker,

Since you made some amazing QoL improvements in the past(i.e. eqset), I would like to propose a few more.

Particularly related to the quests. Since the web site quest list seems to be broken. Moreover it would be convenient if all quest info would be available in-game.

So I would like to propose two new commands:

`look quests` - show quests of the current area: quest givers, rewards and whether they were completed by the player already. Hidden quests might be hidden using '*' symbol.

`journal` - show the quests you undertook: quest givers, current state, etc. I heard there's potion of insight that does similar thing. But it costs drachma, which makes no sense.

</div>

<div class="post" data-post-id="40162" data-author="Insomnia" data-date="2025-03-03T10:50:24+00:00" data-subject="Re: msdp CHARACTER_STATISTICS, CHARACTER_AFFECTS">

I like the idea of creating an artifact or a quest item that lets you "look quests" and seeing the mobs in the area that can give you quests. This feels aligned with "look conquerors", "look sceptre" and "look hunters". I don't think it should be given to everyone for free, but be more like Sceptre of Dominion (which is quite challenging to get).

This doesn't sound like anything game-changing. I assume you'd still have to figure out how exactly to complete the quests, and it shouldn't give you any information about quests that you're not eligible to undertake. But it would be a nice addition to the game.

</div>

<div class="post" data-post-id="40163" data-author="Hung" data-date="2025-03-03T11:27:37+00:00" data-subject="Re: msdp CHARACTER_STATISTICS, CHARACTER_AFFECTS">

The problem with such item is that quests are available starting from the level 1 at the valk.

At least vk quests should be seen without any item.

Though frankly I'd allow see them without item even after valk. After all the site quests page allows to see all quests. So I basically want to move that functionality in the game.

</div>

<div class="post" data-post-id="40172" data-author="Insomnia" data-date="2025-03-06T12:10:48+00:00" data-subject="Re: msdp CHARACTER_STATISTICS, CHARACTER_AFFECTS">

> **Quote:**
> I did make a code change but I'm not sure that it's live. The change is to make CHARACTER_STATISTICS report every 0.5 seconds rather than each time the value changes.

I never knew you could deploy changes without rebooting the game. But if that's possible, and if you're making more changes, you might want to know that the past three days have been pretty terrible with lag.

Aubec (gossip): ouch.. bad lag

Squip (gossip): It's lagging all the time.

Aubec (gossip): all the storms moving through i guess

Slice (gossip): the lag has changed recently, seems they have turned off the catchup ticks?

Squip (gossip): I don't know, but it got worse for me (much less predictable)

Slice (gossip): so far today we have lost 1690 ticks, we usually regain them quicte quickly after they are lost.

Slice (gossip): its as if they turned off the speedrun code.

Slice (gossip): I would have thought that required a reboot, but its only happened recently

Belrath (gossip): perhaps teker working on something recards but in midway?

Fuligin (gossip): only seen this today?

Slice (gossip): last few days, can check logs if its important

*(Subduing mobs has become ten times harder and longer. Coincidentally, I’m on vacation and can afford to do it. But if I lose my Hawthorn streak, I’ll probably quit for a while.)*

</div>

<div class="post" data-post-id="40173" data-author="*teker*" data-date="2025-03-09T02:59:47+00:00" data-subject="Re: msdp CHARACTER_STATISTICS, CHARACTER_AFFECTS">

Regarding the code deployment, the changes I've made are not live and can't be live without a reboot.  Usually I let the game reboot/crash on its own rather than introduce an unscheduled reboot.  I see the game has been up for 33 days, so maybe it's time.  The tick "catchup" code hasn't been touched AFAIK.

CHARACTER_AFFECTS appears to be an issue with the MSDP variable exceeding 32k.  That seems really big but maybe some of you have purchased enough that it happens.  I haven't backed out the CHARACTER_STATISTICS changes so they should still go live at reboot.  I wonder if the size of these MSDP variables could be introducing some of the lag that is being seen.

Regarding the quest requests, unfortunately it's not that simple.  The multipart quest chains are all set up as separate quests, so you'd likely get a list of quests that don't make sense or aren't doable because they require an item or something from a previous step that lives in another area.  I do agree that the quest framework needs rewritten - as a player it should be possible to view a list of discovered quests, the quester, the quest status, etc.  Same goes for forges.  I have a design for such a system but it's more likely to make it into a sloth-rewrite rather than the current code base.

</div>

<div class="post" data-post-id="40174" data-author="Hung" data-date="2025-03-09T04:56:41+00:00" data-subject="Re: msdp CHARACTER_STATISTICS, CHARACTER_AFFECTS">

sloth-rewrite? 

Do you mind sharing some details on that project?

Is it just an idea or maybe it had been secretly been developed for a while?

</div>

<div class="post" data-post-id="40175" data-author="*teker*" data-date="2025-03-10T00:42:46+00:00" data-subject="Re: msdp CHARACTER_STATISTICS, CHARACTER_AFFECTS">

I've been thinking about it.  It's probably a multi-year project.

</div>

<div class="post" data-post-id="40176" data-author="Hung" data-date="2025-03-10T08:00:08+00:00" data-subject="Re: msdp CHARACTER_STATISTICS, CHARACTER_AFFECTS">

Well, good luck.

The only advice I could give is to not use C++ for such project. Literally any other language is better for it.

</div>

<div class="post" data-post-id="40179" data-author="cnl" data-date="2025-03-16T18:27:25+00:00" data-subject="Re: msdp CHARACTER_STATISTICS, CHARACTER_AFFECTS">

would it be possible to spread it into 3 separate msdp vars

PERMANENT (bought, class) - only updates very rarely

ITEM-GENERATED - only updates on eq change 

SPELL (spells, aerial servant, magic mirror etc)

this would greatly reduce the data sent but allow people visibility into their perm and eq based bonuses

</div>

<div class="post" data-post-id="40180" data-author="cnl" data-date="2025-03-18T06:30:16+00:00" data-subject="Re: msdp CHARACTER_STATISTICS, CHARACTER_AFFECTS">

just to confirm with the changes that went in Monday reboot both CHARACTER_AFFECTS and CHARACTER_STATISTICS are working for me.

thank you!

</div>

<div class="post" data-post-id="40182" data-author="Hung" data-date="2025-03-24T13:27:49+00:00" data-subject="Re: msdp CHARACTER_STATISTICS, CHARACTER_AFFECTS">

Just a few more QoL suggestions:

1. Show remaining time for  the each spell you are affected in the 'score'.

2. Format big numbers(gold, xp, honor, conquest) by separating thousands with commas. I.e. instead of "You have 1337319366 unused experience points.", show "You have 1,337,319,366 unused experience points."

</div>

<div class="post" data-post-id="40183" data-author="cnl" data-date="2025-03-24T18:52:07+00:00" data-subject="Re: msdp CHARACTER_STATISTICS, CHARACTER_AFFECTS">

1) see "sco affects2" or use the msdp variables

2) see "numformat" command or roll your own formatting with triggers/replacements

</div>

<div class="post" data-post-id="40184" data-author="Hung" data-date="2025-03-24T19:04:00+00:00" data-subject="Re: msdp CHARACTER_STATISTICS, CHARACTER_AFFECTS">

thanks, didnt know those commands.

</div>

<div class="post" data-post-id="40189" data-author="Hung" data-date="2025-04-25T21:08:29+00:00" data-subject="Re: msdp CHARACTER_STATISTICS, CHARACTER_AFFECTS">

Is it possible to add a notification when the entrench ends?

</div>
