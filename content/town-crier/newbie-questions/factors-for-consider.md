---
title: "Factors for consider"
topic_id: 1285
author: "Granty555"
date: 2005-06-22T13:56:34+00:00
last_activity: 2005-06-23T11:15:46+00:00
last_author: "12345"
sticky: false
locked: false
post_count: 12
---

<div class="post" data-post-id="7459" data-author="Granty555" data-date="2005-06-22T13:56:34+00:00" data-subject="Factors for consider">

Hi all,

a little background:

Having not played for a while I logged back on and was checking through my spells and skills when I noticed that I had levelled enough for cure critical to be worth casting (cost down to 16). So I checked the old eq list for the book and saw that the channeler in the temple just e and s of BH had one. I popped in to check out the mob and he had the book (yay!) He was sanced and my "consider" gave me the luck and great eq message.

Now normally "lot of luck" I can handle, "luck and great eq" is touch and go, and "lucky punk" generally kicks my ass. I needed the book obviously so I went to Cats to fix my alignment (damn rainmaster always making me bad, bugger never loads the shield anyway), then summoned a Peri, 3 wraiths and finally my JuJu. I sanced up, spec shielded up, got into my best outfit, focused and hit him with my deathgrip. Well, to cut a long story short, I annihalated this fool in no time at all, with my Peri healing I dont think I ever got below 90% hps! and he was 50k!!!

So how does he get to be luck and great eq? He was a right spaz, managed a couple of feeble spells but that was about it? What factors determine how high something cons???

</div>

<div class="post" data-post-id="7462" data-author="rith" data-date="2005-06-22T14:24:50+00:00" data-subject="">

Shhh, necromancers are overpowered......

</div>

<div class="post" data-post-id="7463" data-author="12345" data-date="2005-06-22T14:31:17+00:00" data-subject="">

I don't know that anyone can tell you exactly how con works.  I do know that it takes several factors into account.  Personally, I think that casting mobs screw it up even more simply because they're so erratic.

Example of Elena in the garden.  Usually if I'm sanced and resist fire, she's not too bad.  She also tends to stick to webs and fireballs.  Since web only works once, the extra webs tend to be wasted attacks and I can handle the fireballs she throws.  Then again, I've had her throw an endless stream of fireballs and I died pretty quick.  I've also had her throw nothing but webs and I barely got touched.  Lightning bolts make intersting mixers.

The bitty mage in Autumnal Forest... cake, unless he casts firewind, then you just die.

Cleric mobs are even worse because you don't know if they'll heal themselves or flamestrike you... or put up resist fire and cold in the middle of battle.  Xp often does not reflect the effort needed, etc.

Best I can tell you for casters: Until you get to know what spells they like to throw, sanc, spellshield, resist fire, resist cold and pay attention.

If anyone else has a better answer, I'll be glad to hear it.  :)

</div>

<div class="post" data-post-id="7464" data-author="Alberich" data-date="2005-06-22T14:44:29+00:00" data-subject="">

consider is worthless after like lvl 5.

as far as I have been able to tell, it depends on mobs class, your class, and relative hps - which all mean nothing.  A mob with 600hps that you can splork, will con as chicken or some such thing for anyone over lvl 40, but will easily hit for 4-500hps/round through sanc with high enough hit/dam rolls.  A mob with 4-5k hps can con as are you mad, but never hits -10 and can be chopped solo if you have the patience.  Best thing to do is fight the mob, if you want to know how big it is.

</div>

<div class="post" data-post-id="7470" data-author="kjartan" data-date="2005-06-22T15:35:09+00:00" data-subject="">

The consider code is extremely complicated, and it doesn't work very well.

Sloth mobs are so complex that I think it would be hard to come up with an algorithm that evaluates consider properly.  A better approach might be to record how combats with that mob went for people of various levels (i.e. victory with little damage, close victory, fled/recalled, slain).  That is a non-trivial thing to code, but I might do it at some point.

</div>

<div class="post" data-post-id="7482" data-author="Ditheca" data-date="2005-06-22T20:37:24+00:00" data-subject="consider suggestion">

The easiest thing I can think of without creating huge databases of battles is this:

consider <mob>

This mob looks sickly/weak/a little thick, fairly thick, pretty thick, very thick, incredibly thick, etc.

It looks like it might tickle its opponents

It could do a little damage

It could do some damage

It could do real damage

It could do a lot of damage

....

It looks like it could rip your head off in a round!

This would be incredibly easy to code (total hp, damroll, could even ignore player levels, and it would save immort time and player lives.  The only question is, is it too good?

</div>

<div class="post" data-post-id="7483" data-author="Alberich" data-date="2005-06-22T20:39:33+00:00" data-subject="">

I think it's kinda fun not knowing if mob will splork you or you splork it :)  makes exploring new areas worthwhile, although it does lead to some interesting self-cr's

leave con as-is, it's usefull for real low-level types, and beyond that.. well.. what's fun without some risk?

</div>

<div class="post" data-post-id="7484" data-author="Ditheca" data-date="2005-06-22T20:49:38+00:00" data-subject="">

I think it'd be nice to know if a mob can hit brutally or not.  I can't count the times I've cast tons of prep spells just to face a mob that attacks 5 times for very hard and gives 20k :)  Of course that happens less and less as I learn the mud.

I posted below because its the solution to a question, not a solution to a problem.  I don't mind consider the way it is now, if only for old times' sake :)

</div>

<div class="post" data-post-id="7485" data-author="Avatar" data-date="2005-06-23T00:06:35+00:00" data-subject="consider still">

Unfortunately even if the mob side of the equation was all figured out we'd still have the PC side to evaluate.

(mob strength) <> (player strength)

Obviously a 2x40 th/ma with good stats is going to be better off against some mobs than a 2x40 cleric.  

I'd go with Ditheca's suggestions, if it's too much information you could maybe narrow it down so there are less available levels of differentiation...but you could present some info about how many hps, how many attacks, how high the +hit / +dam ... then let the player decide whether he's buff enough to take on that mob.  Again I echo Ditheca but it might not be as fun to have all this spelled out in great detail.

</div>

<div class="post" data-post-id="7487" data-author="Taki" data-date="2005-06-23T05:02:56+00:00" data-subject="">

just an example (newbie biased):

wolverine, immature tiger, cobalt tiger (all a bit north of newbatia).

the first has 4 attacks and can easily waste a lowbie, but it cons let's say low and gives very little xp, the second evals low, gives a bit more xp, the third evals quite higher, gives 10 times xp, but its hit ratio/damage done is fairly lower than wolverine's. 

My opinion is that con is highly related to xp given by the kill, not reflecting the other stats (why else a ridable horse would be fairly easy, when that can dispose of most newbies in 1 round? - and i've been told ridable horses give 1 xp...)

Just my impression...

T.

</div>

<div class="post" data-post-id="7492" data-author="firebrand" data-date="2005-06-23T11:00:56+00:00" data-subject="">

hmmm and now we have "perfect match" on mobs that are correctly aligned to help us change our alignment again, but may not necessarily be perfect match combat wise.  i wish we had a command (contemplate, for example) for checking alignment balance and leave consider as is for combat

</div>

<div class="post" data-post-id="7494" data-author="12345" data-date="2005-06-23T11:15:46+00:00" data-subject="">

Me thinks you're confusing alignment and consider.  Alignment wasn't added to consider, consider was added to alignment.

To use Kj's example, if you kill a defenseless little baby, it's an evil act, and will drag (very heavily) on your alignment.  Killing a kobold is not a suitable atonement for such an act.  In order to raise alignment you must kill a mob of suitable size (at least as big as yourself).  The only way of measuring this (poorly) is the consider command which actually compares the player to the mob.  So, if the mob is at least as big as you, it carries more weight in raising your alignment.

That's why you need at least perfect match mobs to raise alignment, you're not considering alignment, you're still considering size.  The only difference is, easy mobs won't raise alignment anymore and any good mob will make you evil quick, fast and in a hurry.

</div>
