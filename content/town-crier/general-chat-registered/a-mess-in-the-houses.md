---
title: "a mess in the houses?"
topic_id: 4826
author: "Teron"
date: 2018-01-25T15:16:38+00:00
last_activity: 2018-01-26T04:53:22+00:00
last_author: "Teron"
sticky: false
locked: false
post_count: 8
---

<div class="post" data-post-id="38638" data-author="Teron" data-date="2018-01-25T15:16:38+00:00" data-subject="a mess in the houses?">

Ezekiel said that there are less Winter houses for mages and I said that's rubbish.

But look:   

Minor, House of Battle, begins in 15 hours, lasts 94 minutes.

   Minor, House of Dark Shades, begins in 16 hours, lasts 113 minutes.

   Minor, House of the Winter Wolf, begins in 39 hours, lasts 36 minutes.

   Minor, House of the Frost Giant, begins in 39 hours, lasts 196 minutes.

   Minor, House of the Old Forces, begins in 42 hours, lasts 195 minutes.

   Minor, House of the Grand Struggle, begins in 46 hours, lasts 196 minutes.

   Minor, House of the Spring, begins in 49 hours, lasts 195 minutes.

   Minor, House of Nature, begins in 52 hours, lasts 196 minutes.

Can any imms plz check if Winter and Winter Wolf houses are given same time as other houses?

Thanks

</div>

<div class="post" data-post-id="38639" data-author="Gorka" data-date="2018-01-25T16:14:48+00:00" data-subject="Re: a mess in the houses?">

I have a theory...

Given we know sloth astrology is modeled on a real world working system, some of the houses will have shorter or longer rotation periods based on where they are from the center point or axis. It could be the frost houses are on the outer.

Just a guess...

EDIT:

A quick search of my sloth logs revealed that some houses do indeed occur more frequently like nature and spring.

</div>

<div class="post" data-post-id="38640" data-author="*Breeze*" data-date="2018-01-25T18:52:44+00:00" data-subject="Re: a mess in the houses?">

to head off any questions,

the only person who truly understands the way houses/astrology/orrery is probably Kjartan.

i have looked at it multiple times, but i have no idea how, nor the desire to modify it, 

so don't ask for changes.  the math involved is way over my head. 

best i can figure, there is sloth-world in the middle, being orbited by 4 planets ...

however, here is almost 3 years worth of astrology. 

use it, run stats on it, whatever you want.

Enjoy.

https://pastebin.com/iae2n6Cj

</div>

<div class="post" data-post-id="38641" data-author="Gorka" data-date="2018-01-25T19:29:21+00:00" data-subject="Re: a mess in the houses?">

Thanks Breeze!

The mind boogles with the possibilities of using that information... But to address Ezekiel's gut feeling here is a list of the house occurrence frequency in the data Breeze posted... 

House of Winter, begins in	77 times

House of the Great Master, Twivel, begins in	79 times

House of the Winter Wolf, begins in	132 times

House of the Ancient Darkness, begins in	134 times

House of the Frost Giant, begins in	173 times

House of Long Shadows, begins in	177 times

House of Shadows, begins in	193 times

House of the Old Forces, begins in	205 times

House of the Grand Struggle, begins in	236 times

House of Dark Shades, begins in	245 times

House of the Spring, begins in	258 times

House of Battle, begins in	272 times

House of Nature, begins in	312 times

House of Heat, begins in	317 times

House of the Sun, begins in	373 times

House of the Dragon, begins in	427 times

Other useful things can be calculated with this data, such as average house time, average time before a house reoccurs... best times to coliseum... so many things... If I crunch the numbers I'll post here for all to benefit.

</div>

<div class="post" data-post-id="38642" data-author="Gorka" data-date="2018-01-25T20:08:40+00:00" data-subject="Re: a mess in the houses?">

So I just SQL'ed the crap out of that data...

SELECT HOUSE, SUM(`FOR`) AS MINS, AVG(`FOR`) AS AVG_LENGTH FROM ast 

WHERE `TYPE` LIKE 'Major'

GROUP BY HOUSE

ORDER BY MINS

"HOUSE"	"MINS"	"AVG_LENGTH"

"House of the Great Master, Twivel "	"577"	"115.4000"

"House of Winter "	"618"	"103.0000"

"House of the Winter Wolf "	"2706"	"246.0000"

"House of the Ancient Darkness "	"2956"	"184.7500"

"House of the Frost Giant "	"3847"	"174.8636"

"House of Long Shadows "	"3869"	"168.2174"

"House of Dark Shades "	"4076"	"131.4839"

"House of Shadows "	"4171"	"160.4231"

"House of the Grand Struggle "	"4370"	"128.5294"

"House of the Old Forces "	"4756"	"139.8824"

"House of the Spring "	"5205"	"144.5833"

"House of the Dragon "	"5295"	"139.3421"

"House of Nature "	"5935"	"144.7561"

"House of Battle "	"6520"	"163.0000"

"House of the Sun "	"7302"	"162.2667"

"House of Heat "	"7599"	"135.6964"

SELECT HOUSE, SUM(`FOR`) AS MINS, AVG(`FOR`) AS AVG_LENGTH FROM ast 

WHERE `TYPE` LIKE 'Minor'

GROUP BY HOUSE

ORDER BY MINS

"HOUSE"	"MINS"	"AVG_LENGTH"

"House of Winter "	"7862"	"110.7324"

"House of the Great Master, Twivel "	"8826"	"119.2703"

"House of the Winter Wolf "	"19095"	"157.8099"

"House of the Ancient Darkness "	"22737"	"192.6864"

"House of Long Shadows "	"32526"	"211.2078"

"House of the Frost Giant "	"32528"	"215.4172"

"House of the Old Forces "	"33292"	"194.6901"

"House of Shadows "	"37206"	"222.7904"

"House of the Grand Struggle "	"37272"	"184.5149"

"House of the Spring "	"38612"	"173.9279"

"House of Dark Shades "	"42713"	"199.5935"

"House of Battle "	"44723"	"192.7716"

"House of Nature "	"49643"	"183.1845"

"House of Heat "	"51050"	"195.5939"

"House of the Sun "	"58044"	"176.9634"

"House of the Dragon "	"73020"	"187.7121"

SELECT HOUSE, SUM(`FOR`) AS MINS, AVG(`FOR`) AS AVG_LENGTH FROM ast 

WHERE `TYPE` LIKE '%'

GROUP BY HOUSE

ORDER BY MINS

"HOUSE"	"MINS"	"AVG_LENGTH"

"House of Winter "	"8480"	"110.1299"

"House of the Great Master, Twivel "	"9403"	"119.0253"

"House of the Winter Wolf "	"21801"	"165.1591"

"House of the Ancient Darkness "	"25693"	"191.7388"

"House of the Frost Giant "	"36375"	"210.2601"

"House of Long Shadows "	"36395"	"205.6215"

"House of the Old Forces "	"38048"	"185.6000"

"House of Shadows "	"41377"	"214.3886"

"House of the Grand Struggle "	"41642"	"176.4492"

"House of the Spring "	"43817"	"169.8333"

"House of Dark Shades "	"46789"	"190.9755"

"House of Battle "	"51243"	"188.3934"

"House of Nature "	"55578"	"178.1346"

"House of Heat "	"58649"	"185.0126"

"House of the Sun "	"65346"	"175.1903"

"House of the Dragon "	"78315"	"183.4075"

If you need to know something, let me know.

</div>

<div class="post" data-post-id="38643" data-author="Gorka" data-date="2018-01-25T20:55:59+00:00" data-subject="Re: a mess in the houses?">

Hey Gorka... got any more useless information...? Sure..!

My theory is the movement of sloths "4 planets" that Breeze alluded to, that cause conjunctions, probably follow irregular but elliptical shaped paths around sloth, probably moving at different speeds... Looking at this data it could actually be that the conjunctions in one complete system cycle is extremely large, or might even vary every single time. Although there are strong patterns, the calculation of conjunctions probably hinges on many many variables to the extent that the period of conjunctions and when they appear would almost appear random without knowledge of the scaling of the variables, which are probably calculated using geometric equations. KJ was probably a literal genius.

</div>

<div class="post" data-post-id="38644" data-author="*Breeze*" data-date="2018-01-25T21:27:08+00:00" data-subject="Re: a mess in the houses?">

> **Gorka wrote:**
> KJ was probably a literal genius.

Agreed.

</div>

<div class="post" data-post-id="38645" data-author="Teron" data-date="2018-01-26T04:53:22+00:00" data-subject="Re: a mess in the houses?">

Thank you, Breeze, for posting the data.

Thank you Gorka for varifying the assumption.

It seems I was both right and wrong, when I said that the Twivel house happened fewer times. Winter Wolf happens more often, but Winter doesn't.

</div>
