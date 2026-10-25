---
title: "Changes to -saves"
topic_id: 4847
author: "norks"
date: 2018-04-24T08:16:38+00:00
last_activity: 2018-05-13T01:34:02+00:00
last_author: "*teker*"
sticky: false
locked: false
post_count: 14
---

<div class="post" data-post-id="38740" data-author="norks" data-date="2018-04-24T08:16:38+00:00" data-subject="Changes to -saves">

Hello imms

Have any tweaks been made to –saves recently? I’ve notice in a drop over the last couple of weeks. I don’t have any stats or anything to back up my observations but have definitely noticed a change. 

Anyone else noticed anything?

Norks

</div>

<div class="post" data-post-id="38744" data-author="*teker*" data-date="2018-04-24T20:38:57+00:00" data-subject="Re: Changes to -saves">

No changes that I'm aware of.  I gather you think mobs are saving more often?

</div>

<div class="post" data-post-id="38745" data-author="Ezekiel" data-date="2018-04-24T23:36:20+00:00" data-subject="Re: Changes to -saves">

I have noticed this also. It seems like it takes more to blind/faerie fire mobs (multiple, multiple group runs on commonly chopped mobs) on which I've become very familiar of their average rate. In addition, my frostbolts don't seem to be winning the save as much at the same very high saves I've always run with. Dr is the more data driven one and has done some testing with it. Maybe he can shed some light further.

</div>

<div class="post" data-post-id="38746" data-author="Teron" data-date="2018-04-25T15:42:12+00:00" data-subject="Re: Changes to -saves">

Huh, I thought this was just me.

On the mobs I kill often, I noticed -saves work much less. I think it's the real damage, not just the highlight, because I have also the damage approximator (yeah, still no damage shown in fights).

</div>

<div class="post" data-post-id="38747" data-author="norks" data-date="2018-04-25T15:55:48+00:00" data-subject="Re: Changes to -saves">

Hi Teker

Yes that's what i mean. 

As I say I can't back it up and if you say nothing's been changed then fair enough and thank you for checking, but I really have noticed a marked change in the amount of spells I'm getting through the mobs' saves with highlights and extra damage on mobs I hit often.

Norks

</div>

<div class="post" data-post-id="38748" data-author="Gorka" data-date="2018-04-26T05:11:29+00:00" data-subject="Re: Changes to -saves">

I've been watching my casting since Norks reported as I don't cast much on xp runs. I wonder if Norks does have a point. The fact Teker couldn't find the issue straight away, or mentioned that saves wasn't changed, makes me wonder if it's not some other change having an INDIRECT effect on something in the saves formula. For instance perhaps something to mob ac was changed, and indirectly that makes them save more... what I am suggesting is perhaps what we are seeing is a symptom of something else. I only have to do a necrop run to see something doesn't seem normal. I accept that it could just be confirmation bias on my part, but as it happened I did a necrop run a few hours before Norks reported and I had to regen early because the mobs seemed to need an extra firewind to kill them and I distinctly remember thinking that was my crappiest run of necrop ever, but just put it down to bad luck.

</div>

<div class="post" data-post-id="38749" data-author="*teker*" data-date="2018-04-26T15:15:23+00:00" data-subject="Re: Changes to -saves">

Any ideas as to when the change may have occurred?  There is some logging that takes places with saves so we could try to compare something old with something new.

</div>

<div class="post" data-post-id="38750" data-author="Gorka" data-date="2018-04-26T18:57:28+00:00" data-subject="Re: Changes to -saves">

I've parsed my logs and tried to work this out.

Things seemed fine on the 12th of April. (I specifically remember this day - coliseum major heat)

Reboots/Crashes since then have been...

16th April

17th April

21st April

Looking at counter damage in my logs, 21st looks most likely... Norks?

It's hard to work out from my counters, because I am switching eq modes all the time with varying amounts of spell damage...

</div>

<div class="post" data-post-id="38751" data-author="Teron" data-date="2018-04-27T03:15:34+00:00" data-subject="Re: Changes to -saves">

I think Coliseum worked fine.

But definitely 4-5 days by now.

</div>

<div class="post" data-post-id="38752" data-author="norks" data-date="2018-04-27T05:42:08+00:00" data-subject="Re: Changes to -saves">

I think it's been a little longer. Maybe 10 days or so now.

</div>

<div class="post" data-post-id="38765" data-author="Ezekiel" data-date="2018-05-06T08:28:34+00:00" data-subject="Re: Changes to -saves">

Has anything been looked at for this? Save rate is really annoying

</div>

<div class="post" data-post-id="38775" data-author="*teker*" data-date="2018-05-09T19:25:40+00:00" data-subject="Re: Changes to -saves">

What are some good mobs for me to test this on?  Should I test damage spells or specific debuff spells or something else?  What -saves should I test with?  I will get some base line values with the current code and then revert the code server back to 4/1 and see if the logs show anything different.

</div>

<div class="post" data-post-id="38780" data-author="Teron" data-date="2018-05-11T01:08:08+00:00" data-subject="Re: Changes to -saves">

I hit the sahaguin gate guards with -13saves cap, so I notice, when/if they fail.

We mainly speak of blast spells, I believe.

Eze and norks might have other mobs.

</div>

<div class="post" data-post-id="38781" data-author="*teker*" data-date="2018-05-13T01:34:02+00:00" data-subject="Re: Changes to -saves">

My initial tests aren't showing any differences between current code and Jan 1, 2018 code.  Are we sure it's saves and not something else?

</div>
