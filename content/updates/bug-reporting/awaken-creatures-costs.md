---
title: "Awaken creatures costs"
topic_id: 4504
author: "Filk"
date: 2015-08-07T07:55:21+00:00
last_activity: 2015-08-08T05:24:24+00:00
last_author: "Filk"
sticky: false
locked: false
post_count: 3
---

<div class="post" data-post-id="36013" data-author="Filk" data-date="2015-08-07T07:55:21+00:00" data-subject="Awaken creatures costs">

Found some glitches in awaken creatures. Nothing important, but could be fixed one day.

1.Case 1 - tangle vine

```
A young treant rustles its supple branches restlessly.
A writhing purple vine crawls slowly across the floor.
A writhing purple vine crawls slowly across the floor.
A writhing purple vine crawls slowly across the floor.
You could probably handle one or two more followers than you have now. [4.0]
```

```
You dismiss a tangle vine.
A tangle vine stops following you.
You could probably handle one or two more followers than you have now. [2.9]
```

\--- Like cost of vine was 1.1

```
You dismiss a tangle vine.
A tangle vine stops following you.
You could control far more followers than you have now. [1.9]
```

\--- But here it seems like exact 1

```
You dismiss a tangle vine.
A tangle vine stops following you.
You could control far more followers than you have now. [0.8]
```

\--- And again its 1.1.

Guess its cost has some float point, which isnt displayed, but counts in calculations. Probably should be made exactly 1.00

2\. Case 2 - just demonstration of slime mold

```
You aren't controlling any followers right now. [0.0]

cast 'awaken' slime mold
You weave the threads of magic masterfully!
Lush new growth springs from the ground all around you!
A giant slime mold starts following you.
You could control far more followers than you have now. [2.0]

cast 'awaken' slime mold
Ok.
Lush new growth springs from the ground all around you!
A giant slime mold starts following you.
You could probably handle one or two more followers than you have now. [4.0]
```

\--- Slime mold cost looks like exact 2.00

3\. Case 3 - elder ent

```
You aren't controlling any followers right now. [0.0]

cast 'awaken' ent
Ok.
Lush new growth springs from the ground all around you!
An elder ent starts following you.
You could control far more followers than you have now. [2.0]

cast 'awaken' ent
Ok.
You wouldn't be able to control it...

cast 'awaken' slime mold
Ok.
You wouldn't be able to control it...
```

\--- Seems elder ent also have some float point in cost.

\--- Maybe should be made exact 2.00. Or at least 2.10 to prevent misunderstanding.

\--- 2.0 looks like more correct number tbh. Ent isnt really strong. Cant move(at least should be). And druids dont have any higher summons. 

\--- Or maybe worth adding some "Great Father Oak Ent" at 8x40, with 3.00 cost and 1.5 times higher stats then ent, as alternate way <img src="/images/smilies/icon_e_smile.svg" alt=":)" title=":)" width="15" height="15" class="smiley nozoom">

4\. Elder ents wasnt able to move before. And should not be able to, due to description.

But now they can for unknown reason.

5\. Quick check showed, that other summoned creatures have similiar problems with floating points.

```
cast 'summon undead' phantom
Ok.
A phantom starts following you.
You could control far more followers than you have now. [1.8]

cast 'summon undead' phantom
Ok.
A phantom starts following you.
You could probably handle one or two more followers than you have now. [3.5]
```

\--- First was 1.8 and second was 1.7 

6\. Not sure if thats a bug. 

```
cast 'summon undead' phantom
Ok.
A phantom starts following you.

dismiss phantom
You try to magically dismiss a phantom... it doesn't work!
```

But nothing about relations of undeads and dismiss command in dismiss description.

Something should be fixed probably. Command or description.

</div>

<div class="post" data-post-id="36015" data-author="*teker*" data-date="2015-08-07T15:44:42+00:00" data-subject="Re: Awaken creatures costs">

A quick glance of the code shows that some of the cost values go out to 2 decimal points but you're only getting one (rounded) decimal point in the display. This is true for the tangle vine - its cost is between 1.0 and 1.1. The elder ent works the same way - its cost is greater than 2.00 even though it shows up as 2.0 in the display.

EDIT: typos

</div>

<div class="post" data-post-id="36016" data-author="Filk" data-date="2015-08-08T05:24:24+00:00" data-subject="Re: Awaken creatures costs">

Well, same as i thought.

Then probably all summoned creatures shoud be checked and truncated to one decimal point.

When somebody will have time for that <img src="/images/smilies/icon_e_smile.svg" alt=":)" title=":)" width="15" height="15" class="smiley nozoom">

</div>
