---
title: "A new skill to help avatars keep spells up."
topic_id: 4148
author: "Dragoth"
date: 2013-11-05T09:03:11+00:00
last_activity: 2013-11-11T02:42:30+00:00
last_author: "Marvel"
sticky: false
locked: false
post_count: 11
---

<div class="post" data-post-id="34542" data-author="Dragoth" data-date="2013-11-05T09:03:11+00:00">

Keeping your spells up when you are an avatar becomes a pretty tedious exercise. I suggest making an avatar skill that would make those spells last forever, but at the cost of your mana regen.

The skill would convert all your spell times on spells that last longer than 10 minutes (to exclude things like aegis and wraithform etc) into mana cost per minutes (i.e stamina lasts 20 minutes and costs 20 mana to cast, which will equal to 1 MR per tick, so you mana regen would go from 100 to 99), but the spell will be constantly up without any need to recast it every 20 minutes.

The skill does not provide any character power, but it reduces the annoyance of constant recasts, pretty much the same ideology as gorge skill. 

Suggested level: 20 avatar

Usage: <skillname> "spellname"

</div>

<div class="post" data-post-id="34544" data-author="Popeye" data-date="2013-11-06T19:35:57+00:00">

I have noticed Sloth steers away from ideas that aid botting, and I think this would fall in that category

</div>

<div class="post" data-post-id="34548" data-author="Sam" data-date="2013-11-07T19:45:43+00:00">

In what way does it aid botting? 

It will even reduce botting in respect of spell recasts. 

And will greatly help those who use telnet, for example.

</div>

<div class="post" data-post-id="34550" data-author="Yasik" data-date="2013-11-08T11:40:14+00:00">

I think it helps botting by removing the nessesity of writing recast scripts, fewer events processing.

Not sure if anyone still using telnet, it is so much inferior to specialized mud clients that barely allows playing aside from just standing at recall and watching whats happening.

Agree that on high levels keep all spells up is a problem, but not the unsolvable problem with proper scripting.

</div>

<div class="post" data-post-id="34555" data-author="Marvel" data-date="2013-11-09T13:12:56+00:00">

> **Yasik wrote:**
> Not sure if anyone still using telnet, it is so much inferior to specialized mud clients that barely allows playing aside from just standing at recall and watching whats happening.

I use telnet (Lore/Rain). On a mobile phone, no less. I've found telnet to be the far superior alternative to a client, but then again I'm already certifiably insane*.

* - You get a Level 1 Captain Insano certificate for leveling a bard prime to avatar.

</div>

<div class="post" data-post-id="34556" data-author="Yasik" data-date="2013-11-09T16:55:27+00:00">

> **Marvel wrote:**
> I use telnet (Lore/Rain). On a mobile phone, no less. I've found telnet to be the far superior alternative to a client, but then again I'm already certifiably insane*.

So, you typing "*cast 'stone skin' lore*" letter by letter every time it falls? On the phone? Other bunch of spells too? And you buff your undead same way, right?

You doing dumb job that wastes your time, which is limited resource. You can do whatever you like, however. Personally, I prefer to concentrate on important stuff rather than routine, that is why scripting languages are invented and implemented.

</div>

<div class="post" data-post-id="34557" data-author="Marvel" data-date="2013-11-09T18:26:21+00:00">

> **Yasik wrote:**
> So, you typing "*cast 'stone skin' lore*" letter by letter every time it falls? On the phone? Other bunch of spells too? And you buff your undead same way, right?

Gee um, wouldn't it be neat if they created some sort of thing stored on the server that let you save these kind of strings? Mmm... couldn't be called 'aliases'. Oh wow. Besides, there's a Sloth fable about some nub who got to 5x20 without using pets, "because pets are dumb and not worth the time".

Mmmkay. [/troll]

</div>

<div class="post" data-post-id="34558" data-author="Yasik" data-date="2013-11-09T18:58:01+00:00">

Just checked - I have 611 aliases, 1353 triggers and 1981 lines of scripts with total size 51848 bytes.

Good luck putting all that on server side's 20 aliases  :P Those are not supporting even 2 commands in 1 alias separated by semicolon.

</div>

<div class="post" data-post-id="34559" data-author="Popeye" data-date="2013-11-09T21:06:16+00:00">

I believe that one should not be able to cast some spells during combat like Sanc/Aegis. Re-casting of this should be down to the individual to type, before, after, or during if you flee. Aliases are as far as one should go with this.

To be honest, I regard scripts on programs that do spells automatically as cheating.

Skills to keep spells up seem to flow with the way of the bard where you sing a spell to keep it going. That would be the only way forward, possibly.

The times I have died, it has mainly been because I have not paid attention, and this is way it has to be. That is a mud game.

</div>

<div class="post" data-post-id="34560" data-author="*Splork*" data-date="2013-11-10T00:42:37+00:00">

A skill such as this probably won't happen. Timing runs with spell casting is a vital part of being a good player. Automating something such as this is simply not a good idea from the Admin's perspective. 

Splork

</div>

<div class="post" data-post-id="34564" data-author="Marvel" data-date="2013-11-11T02:42:30+00:00">

> **Yasik wrote:**
> Just checked - I have 611 aliases, 1353 triggers and 1981 lines of scripts with total size 51848 bytes.
> 
> Good luck putting all that on server side's 20 aliases  :P Those are not supporting even 2 commands in 1 alias separated by semicolon.

Here's the kicker... (and proof that Ozzy is just as big of a nub as we always knew he was). There's 100 server alias slots.

I don't know what all you need all that for. I have roughly 70 aliases (server-based), 0 triggers, 0 scripts, and I don't see the need for much else. Now if this was about something that was actually useful to 100% of the mud, it'd be making warcry joins being an automatic toggle. I don't join warcries because a) I don't care, b) the benefits are too minor to me, and c) I cannot alias the warcry when it's something like warcry AAAAAAAAAAAAAIIIIIIIIIIIIIIIIIYAKHAFKHIHFISHGSHJSHGSJGH!AAA!11oneone111!!!, most warcries are too long/stupid.

I know Shyla has repeatedly asked for this automatic warcry toggle in the past, so I'll repeat it here. That's a far more useful idea. It falls within the scope of making groups better - it's not like it helps prevent botting, it just allows the botters to add it to their scripts, while these of us on telnet just either try to warcry (and misspell it if it's something nonsensical or don't get it in in time) or just choose to ignore them entirely.

</div>
