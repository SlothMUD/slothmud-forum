---
title: "Sloth client"
topic_id: 4703
author: "*teker*"
date: 2016-12-03T17:37:54+00:00
last_activity: 2016-12-03T18:09:15+00:00
last_author: "Teron"
sticky: false
locked: false
post_count: 3
---

<div class="post" data-post-id="37615" data-author="*teker*" data-date="2016-12-03T17:37:54+00:00">

I think it would really help new players if we had a Mudlet package they could download to help them with grouping in Sloth.  I've started working on my client scripts recently with the idea that they could be published for new users.  What should they contain?  I've got "man back", some triggers to follow the leader through portals, archways, and some other obstacles.  What else do new players need?

I'm thinking there should be a set of basic triggers for all players and then the package could be expanded to include modules for different classes/group jobs.  I know some of you have pretty extensive UI built, but I'd rather focus on the scripts themselves to start.

</div>

<div class="post" data-post-id="37616" data-author="*Breeze*" data-date="2016-12-03T17:59:40+00:00">

this is as far as I bothered to go

[http://www.slothmud.org/mudlet-tools/](http://www.slothmud.org/mudlet-tools/)

asked for help but no one wanted to. 

it's my basic scripts. .

</div>

<div class="post" data-post-id="37617" data-author="Teron" data-date="2016-12-03T18:09:15+00:00">

That's a nifty idea, though you should remember that Mudlet is only easy for software developers.

Please disable portal jumping from Lyme to other continents in your scripts.

Must have triggers off the top of my head:

1. Update leader on gset transfer

2. Update tank both on "point" and on "group"

3. Assist trigger on tank's rescue (if you are the stabber/gripper, warcry before assisting after your stab+rescue)

4. Switch to a specified (main?) eqset on target after regen.

The rest I wanted everyone to have are here:

[http://www.slothmud.org/forum/viewtopic.php?f=28&t=4642](http://www.slothmud.org/forum/viewtopic.php?f=28&t=4642)

There has already been some effort to provide Mudlet scripts.

1. Splork's(?) files:

[http://www.slothmud.org/mudlet/](http://www.slothmud.org/mudlet/)

2. Breeze's most common scripts:

[http://www.slothmud.org/mudlet-tools/](http://www.slothmud.org/mudlet-tools/)

3. Akaya translated [these Zmud triggers I already made](http://www.slothmud.org/forum/viewtopic.php?f=28&t=4642) [to Mudlet](http://www.slothmud.org/forum/viewtopic.php?f=39&t=4002&start=45#p37003), download the settings .xml here:

[http://www.slothmud.org/forum/download/file.php?id=77](http://www.slothmud.org/forum/download/file.php?id=77)

4. A list of Zmud/Cmud triggers for a great tank:

[http://www.slothmud.org/forum/viewtopic.php?f=16&t=4684](http://www.slothmud.org/forum/viewtopic.php?f=16&t=4684)

If you add the simplest triggers for a tank to Mudlet, that'd be good.

If you do all of them, that'd be awesome and I'd love a copy of that settings file.

Update:

Perhaps a timer would be useful, such as for sanc/aegis.

If needed, the player will then copy/edit it for other spells/occasions.

</div>
