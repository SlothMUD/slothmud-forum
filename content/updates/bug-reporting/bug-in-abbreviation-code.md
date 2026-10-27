---
title: "bug in abbreviation code"
topic_id: 830
author: "Blastem"
date: 2005-02-11T21:20:15+00:00
last_activity: 2005-02-12T00:58:14+00:00
last_author: "Blastem"
sticky: false
locked: false
post_count: 3
---

<div class="post" data-post-id="4391" data-author="Blastem" data-date="2005-02-11T21:20:15+00:00" data-subject="bug in abbreviation code">

The abbreviation code needs a check for an exact match before it looks for abbreviations. This is a problem I've noticed in a number of ways examples are :

\<475hp 438ma 130mv\>

tell ben test.

You tell Benq 'test.'

\<475hp 438ma 130mv\>

both chars were on at the time. Sometimes it works other times it will hit the wrong char.

another problem is this:

Blastem's homunculus is scuttling about here.

A lady lounges in a chair wearing some light leather armor.

A man in chainmail plays with a thin dagger.

\<485hp 463ma 112mv\>

cast 'firewind' lady

Ok.

Lady-watcher the homunculus hates your guts!

Winds of Flame pour from your hands, killing lady-watcher the homunculus instantly.

Lady-watcher the homunculus is dead! R.I.P <img src="/images/smilies/icon_e_sad.svg" alt=":(" title=":(" width="15" height="15" class="smiley nozoom">

A check to see if an exact match is available before using an abbreviation would fix these issues. 

Love the work you guys are doing keep up the good work <img src="/images/smilies/icon_e_smile.svg" alt=":)" title=":)" width="15" height="15" class="smiley nozoom">

thanks for everything

</div>

<div class="post" data-post-id="4393" data-author="*Splork*" data-date="2005-02-11T23:01:02+00:00" data-subject="">

This should be fixed on reboot, sorry for the problem it was causing.

A few other small changes:

1\) Shops now have a legend in them

2)Lockers now have similar msgs to vaults

3)blind mobs will no longer magically regain their eyesight and assist their fellow friends

Enjoy,

Splork

</div>

<div class="post" data-post-id="4394" data-author="Blastem" data-date="2005-02-12T00:58:14+00:00" data-subject="">

Thanks <img src="/images/smilies/icon_e_biggrin.svg" alt=":D" title=":D" width="15" height="15" class="smiley nozoom">

</div>
