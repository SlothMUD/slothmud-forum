---
title: "exp loss and level loss changes"
topic_id: 3109
author: "*Splork*"
date: 2009-04-23T22:33:03+00:00
last_activity: 2009-08-03T21:25:50+00:00
last_author: "*Splork*"
sticky: false
locked: false
post_count: 3
---

<div class="post" data-post-id="29037" data-author="*Splork*" data-date="2009-04-23T22:33:03+00:00">

Ive noticed an incredible amount of people losing levels and high amounts of exp at these levels. This ofcourse will change with more clerics gaining the raise dead spell and our players gaining wordly experience and knowledge of the new combat system.

However, checking the code, it appeared to be a flat rate of 30% exp loss on death and a flat rate of 7% chance of level loss at level 15.

I believe this is slightly outdated code and a little bit harsh with the new eight class system.

Changes:

1) Level loss has been pushed to level 25

2) The chance of level loss is now on a sliding scale depending on your total levels. This scale starts low and ends up near the old percentage.

3) The chance of exp loss is now on a sliding scale depending on your total levels. This scale starts low and ends up near the old percentate.

Hope these changes help you guys out some.

Enjoy,

Splork

</div>

<div class="post" data-post-id="29108" data-author="*Splork*" data-date="2009-05-07T22:06:29+00:00">

Exp loss is now capped depending on your total levels for your character.

The previous code had a 30 million exp cap except for when your character started reaching triple 40 and above to which it went much higher.

The exp loss caps now start at 10 mil and go up accordingly.

Splork

</div>

<div class="post" data-post-id="29752" data-author="*Splork*" data-date="2009-08-03T21:25:50+00:00">

The code we started this version of sloth had a 7% chance for everyone to lose level, a 30% loss for exp upon death, and a 30 million exp cap on death at triple 40( from there every quad level added 2 mil exp loss to the cap, and every avatar level added 1 more mil for what could of been a total of 150) We have tinkered with it several times and it is now on a sliding scale. 

Ive lowered everything quite a bit more and this is probably close to the final change on this topic. 

As it stands now exp loss, cap, and chance of level loss goes by total levels of a character. 

Here is the current code for death, level loss, and exp losses and caps.

 Total levels,           % xp loss,                   xp loss cap,         level loss %

< 40                         20                            10 mil                    

< 80                         21                            15                         1 

<100                       22                            18

<120                       23                            20                         2

<140                       24                            22

<160                       25                            25                         3

<180                       26                            32

<200                       27                            40                         4

<220                       28                            50

<240                       29                            60                         5

<260                       30                            70

<280                       30                            80                         6  

<300                       31                            90

<320                       31                            100                       7 

<340                       32                            115

<360                       33                            130                       8  

Adding avatar levels adds 2 mil exp per level to the exp loss cap.

Overall, chance of level loss has been drastically reduced except for a player of max level. 

Percentage of exp has been reduced drastically but catches up to the old percentage at 260 total levels, from there it increases up to 3 more percentage points. However, the caps are quite a bit smaller at the higher levels which should offset the 3% increase by quite a bit.

Exp loss caps are much, much smaller than before. 

Hope this helps, it is a ton better than our old version was where everything was a flat 30% exp loss and 7% chance of level loss. 

Splork

</div>
