---
title: "EQ Dressing Room"
topic_id: 2482
author: "Leaf"
date: 2007-05-10T17:51:13+00:00
last_activity: 2007-05-16T05:42:42+00:00
last_author: "Kong"
sticky: false
locked: false
post_count: 12
---

<div class="post" data-post-id="18462" data-author="Leaf" data-date="2007-05-10T17:51:13+00:00" data-subject="EQ Dressing Room">

Hello,

I wanted to know if the EQ Dressing Room would ever be put back on the

website?  I know it was on the system years ago, but it was kinda out dated

with all the new class eq.  How hard would it be to link the EQ Page to a

new Dressing Room for Stat, AC, HP, MANA, HR, MR, Charisma, Control, 

Spell, Heal, Dam, Hit?

I r no programer ... so I'm just wondering.

</div>

<div class="post" data-post-id="18463" data-author="Messiaen" data-date="2007-05-10T18:39:41+00:00" data-subject="">

Depends on how the eqlist data is stored. If its something like mysql, it would take something like 2 hours to make a dressing room.

</div>

<div class="post" data-post-id="18464" data-author="madmax" data-date="2007-05-10T20:32:36+00:00" data-subject="">

06 Aug 05  We now have an XML version of the eqlist available for use by anyone who desires it. It is available at [http://www.slothmud.org/eqlist/xmlfilter.php](http://www.slothmud.org/eqlist/xmlfilter.php) .

</div>

<div class="post" data-post-id="18466" data-author="Weasel" data-date="2007-05-10T22:44:33+00:00" data-subject="">

ack.. how do you parse those xml files? There's no structural tags at all that I can see..

</div>

<div class="post" data-post-id="18467" data-author="13" data-date="2007-05-11T02:07:40+00:00" data-subject="">

this is from 2004 hrm

</div>

<div class="post" data-post-id="18468" data-author="12345" data-date="2007-05-11T03:52:43+00:00" data-subject="">

Er.. there's not tags?  Try this link:

[http://www.slothmud.org/eqlist/xml.php?eqtype=All](http://www.slothmud.org/eqlist/xml.php?eqtype=All)

</div>

<div class="post" data-post-id="18481" data-author="Avatar" data-date="2007-05-14T12:50:22+00:00" data-subject="Dressing Room">

The tag for "affects" is a text string, which will make it difficult to build anything functional.  If there were tags that looked like:

<Affects STR="0" INT="1" WIS="0" DEX="0" CON="0" HPs="0" MANA="10" /> 

It would be easier to build features that use the eqlist.  Of course we'd need to have flags for UC, Healbonus, Spellbonus, moves, etc.  It would also make it easier for queries to filter on something like spell bonus, which presently could be stored as "spellbonus" or "spell bonus".

</div>

<div class="post" data-post-id="18486" data-author="Clink" data-date="2007-05-14T19:16:40+00:00" data-subject="Re: Dressing Room">

At a high level, if someone wants to build a few php pages within the PostNuke framework, we can get you the data in the format you need.  We can put it turns out to be cool.

PostNuke ain't that hard if you start with the sample modules, it just takes time we don't have right now.

Clink

</div>

<div class="post" data-post-id="18495" data-author="13" data-date="2007-05-15T09:46:10+00:00" data-subject="">

the dressing room is unnecessary

if you cant do math you shouldnt play sloth anyway

</div>

<div class="post" data-post-id="18497" data-author="Thraxas" data-date="2007-05-15T11:45:29+00:00" data-subject="">

[quote:14gcdgg9]the dressing room is unnecessary 

if you cant do math you shouldnt play sloth anyway[/quote:14gcdgg9]

Eliteism by sums? Discrimition by numbers? Prejucide by mathematics?

[quote:14gcdgg9]the flaming is unnecessary 

if you cant do chicken circus training you shouldnt play sloth anyway[/quote:14gcdgg9]

</div>

<div class="post" data-post-id="18500" data-author="Messiaen" data-date="2007-05-15T18:59:40+00:00" data-subject="">

I would gladly do it. The only problem is that I'm working on my graduate paper these days so I don't have much time. In a few weeks I'll gladly do it.

I'm also sure that there's no problem parsing the XML version of eqlist as it is. If that data exists in some better format, its even better, thought.

BTW I agree with AA, and I don't like the way in which Thraxas replies.

</div>

<div class="post" data-post-id="18508" data-author="Kong" data-date="2007-05-16T05:42:42+00:00" data-subject="">

I have to take off my shoes to do math, so STFU

</div>
