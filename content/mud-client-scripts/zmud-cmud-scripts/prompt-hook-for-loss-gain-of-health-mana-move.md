---
title: "Prompt hook for loss/gain of health/mana/move"
topic_id: 2817
author: "Festeringhag"
date: 2008-05-06T02:17:40+00:00
last_activity: 2008-05-06T14:30:08+00:00
last_author: "Weasel"
sticky: false
locked: false
post_count: 8
---

<div class="post" data-post-id="24216" data-author="Festeringhag" data-date="2008-05-06T02:17:40+00:00" data-subject="Prompt hook for loss/gain of health/mana/move">

Prompt code in game:

```
$n(Hp: $h/$H) (Ma: $m/$M) (Mv: $v/$V)>
```

Zmud Code:

```
#CLASS {Prompt}

#VAR Prompt {hpc0hp31maxhp63mac0ma33maxma84hpmax63mamax92mvc-53mv84mvmax84}

#TRIGGER {~(Hp: (%d)/(%d)~) ~(Ma: (%d)/(%d)~) ~(Mv: (%d)/(%d)~)~>} {

 #var prompt.hpc {%eval( @prompt.hp-%1)}

 #var prompt.hp %1

 #var prompt.hpmax %2

 #var prompt.mac {%eval( @prompt.ma-%3)}

 #var prompt.ma %3

 #var prompt.mamax %4

 #var prompt.mvc {%eval( @prompt.hp-%5)}

 #var prompt.mv %5

 #var prompt.mvmax %6

 #PSUB {%2/@prompt.hpc} %x2

 #PSUB {%2/@prompt.hpc} %x4

 #PSUB {%2/@prompt.hpc} %x6

 }

#CLASS 0
```

Original Prompt display:

```
(Hp: 100/200) (Ma: 100/200) (Mv: 100/200)>
```

New Prompt display:

```
(Hp: 100/200/0) (Ma: 100/200/0) (Mv: 100/200/0)>
```

So, when you take 50 damage, your prompt will show:

```
(Hp: 50/200/-50) (Ma: 100/200/0) (Mv: 100/200/0)>
```

Works the same with ma and mv. really useful if you like to see exact numbers.

</div>

<div class="post" data-post-id="24217" data-author="jezer" data-date="2008-05-06T02:26:19+00:00" data-subject="">

Jake! Is that you? <img src="/images/smilies/icon_twisted.svg" alt=":twisted:" title=":twisted:" width="15" height="15" class="smiley nozoom">

</div>

<div class="post" data-post-id="24218" data-author="Festeringhag" data-date="2008-05-06T02:34:31+00:00" data-subject="">

Sorry, no. i'm new to the mud. <img src="/images/smilies/icon_e_smile.svg" alt=":)" title=":)" width="15" height="15" class="smiley nozoom">

</div>

<div class="post" data-post-id="24221" data-author="Weasel" data-date="2008-05-06T04:11:38+00:00" data-subject="">

Double, double toil and trouble;

 Fire burn, and cauldron bubble.

</div>

<div class="post" data-post-id="24226" data-author="Festeringhag" data-date="2008-05-06T06:02:39+00:00" data-subject="">

only change:

 \#PSUB {%2/@prompt.hpc} %x2 

 \#PSUB {%2/@prompt.hpc} %x4 

 \#PSUB {%2/@prompt.hpc} %x6 

to.. 

 \#PSUB {%2/@prompt.hpc} %x2 

 \#PSUB {%2/@prompt.mac} %x4 

 \#PSUB {%2/@prompt.mvc} %x6

</div>

<div class="post" data-post-id="24227" data-author="jezer" data-date="2008-05-06T06:34:50+00:00" data-subject="">

A ball of twine, an old birds nest;

And now this brew is ready to test!

</div>

<div class="post" data-post-id="24228" data-author="jezer" data-date="2008-05-06T07:02:45+00:00" data-subject="">

A dogs nose, a weasels tail

a pirates hook, a dragons scale

![](http://www.hauntedmansion.info/Snow%20White/snow_witch_cauldron.jpg)

Muhahahahaha!

</div>

<div class="post" data-post-id="24232" data-author="Weasel" data-date="2008-05-06T14:30:08+00:00" data-subject="">

a weasel's tail? <img src="/images/smilies/icon_eek.svg" alt=":shock:" title=":shock:" width="15" height="15" class="smiley nozoom"> now that's just wrong.

</div>
