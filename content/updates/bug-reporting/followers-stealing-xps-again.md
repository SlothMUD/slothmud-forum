---
title: "Followers stealing xps again"
topic_id: 1377
author: "Blastem"
date: 2005-07-24T17:38:56+00:00
last_activity: 2005-07-26T10:39:12+00:00
last_author: "13"
sticky: false
locked: false
post_count: 9
---

<div class="post" data-post-id="7986" data-author="Blastem" data-date="2005-07-24T17:38:56+00:00" data-subject="Followers stealing xps again">

You pound a centaur ranger very hard.

A wight massacres a centaur ranger to small fragments with its claw.

A wight rakes a centaur ranger extremely hard.

A banshee massacres a centaur ranger to small fragments with her rake.

A banshee massacres a centaur ranger to small fragments with her claw.

A centaur ranger is mortally wounded, and will die soon, if not aided.

A wight rakes a centaur ranger with it poisonous claws!

A centaur ranger is dead! R.I.P.

Your blood freezes as you hear a centaur ranger's death cry.

These are my followers and I'm running solo ... have also had it happen a lot today with Drangr and ifrit... seems like anytime a follower kills with a proc you get no xps for the kill.

Blastem

</div>

<div class="post" data-post-id="7990" data-author="dt" data-date="2005-07-24T20:27:46+00:00" data-subject="Followers for weaks...">

Don't hide behind pets, best to use them to carry bags then give them bragging right.

Monks do IT with their hands!

</div>

<div class="post" data-post-id="7996" data-author="Taki" data-date="2005-07-25T05:24:19+00:00" data-subject="">

same happens with mage familiars. Having a wolverine fam is quite nice for its 4 attacks, but then you miss the kill xp almost always <img src="/images/smilies/icon_e_sad.svg" alt=":(" title=":(" width="15" height="15" class="smiley nozoom"> 

I foresee a quick drop in followers' value... sell your stock options now! <img src="/images/smilies/icon_razz.svg" alt=":P" title=":P" width="15" height="15" class="smiley nozoom">

</div>

<div class="post" data-post-id="8012" data-author="13" data-date="2005-07-25T18:27:36+00:00" data-subject="">

Or maybe Kj can take a look and see if he could fix the proc stealing xp thingy..

</div>

<div class="post" data-post-id="8013" data-author="kjartan" data-date="2005-07-25T19:00:38+00:00" data-subject="">

Familiars deliberately don't give xp.

As far as the other followers, that's definitely a bug. I glanced at the code this weekend and it wasn't immediately obvious why it happened. I'll try to figure it out sometime soon.

</div>

<div class="post" data-post-id="8014" data-author="13" data-date="2005-07-25T19:22:01+00:00" data-subject="">

Thanks dude, we appreciate it.

aa

</div>

<div class="post" data-post-id="8017" data-author="kjartan" data-date="2005-07-26T01:49:47+00:00" data-subject="">

Ok, this should in theory be fixed. Anyway I fixed all the undeads and all the supplication mobs. The ones that were likely to have stolen xp were:

drangr

vampire

wight

vilewight

A number of other mobs had been modified so that their procs never killed anybody do avoid xp stealing; I took this back out since they should share xp properly now. Let me know if the problem persists with undead (summoned or animated) or supplication mobs.

</div>

<div class="post" data-post-id="8023" data-author="Vixn" data-date="2005-07-26T04:23:58+00:00" data-subject="">

Does it mean followers won't steal exp in groups anymore? Or this update is just for soloing?

</div>

<div class="post" data-post-id="8028" data-author="13" data-date="2005-07-26T10:39:12+00:00" data-subject="">

Still for soloers Vix.

</div>
