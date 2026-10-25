---
title: "Change to Score Graphs (score all2)"
topic_id: 4869
author: "*Breeze*"
date: 2018-08-12T11:54:21+00:00
last_activity: 2018-08-26T10:45:31+00:00
last_author: "*Breeze*"
sticky: false
locked: false
post_count: 2
---

<div class="post" data-post-id="38962" data-author="*Breeze*" data-date="2018-08-12T11:54:21+00:00" data-subject="Change to Score Graphs (score all2)">

Change to the way 

 Damage Reduction / Bonus Damage Reduction

 Heal Bonus / Bonus Heal Bonus

are shown in "score all2"

Previously you would see this..

```
The following bonuses affect you:
   Hit Roll      :      ( 23) [|||||||||||                                       ]
   Damage        :      ( 19) [|||||||||                                         ]
   Damage Red.   : 100% ( 29) [||||||||||||||||||||||||||||||||||||||||||||||||||]
   System Shock  :      (  1) [                                                  ]
   Spell Saves   :  28% ( -6) [||||||||||||||                                    ]
   Hand Damage   :  78% ( 26) [|||||||||||||||||||||||||||||||||||||||           ]
```

now you will see this

```
The following bonuses affect you:
   Hit Roll      :      ( 22) [|||||||||||                                       ]
   Damage        :      ( 17) [||||||||                                          ]
   Damage Red.   :  48% ( 14) [||||||||||||||||||||||||                          ]
  +Damage Red.   :  16 of NOCAP
   System Shock  :      (  1) [                                                  ]
   Spell Saves   :  28% ( -6) [||||||||||||||                                    ]
   Hand Damage   :  78% ( 26) [|||||||||||||||||||||||||||||||||||||||           ]
```

the + means bonus.  so in this case, bonus_damage_reduction.

the only ones that will show up at the moment are +Damage Red.  (bonus damage reduction)

and +Heal Bonus (bonus heal bonus) the reason is that i have to add them in manually and have to research them manually.

notice that in the latter case, the total is actually 1 higher than in the original case.

that was due to a small bug in the way the data is calculated which is why i have to 

research each thing that gets added.

someone please collect all the missing bonuses and decide in which order we should add them in?

do a poll or something.

</div>

<div class="post" data-post-id="38964" data-author="*Breeze*" data-date="2018-08-26T10:45:31+00:00" data-subject="Re: Change to Score Graphs (score all2)">

score all2 / score stats2

 - added missing bonus_X_applies

 - changed the format a little for the bonus_X_applies

 - no input from the mortals taken into account since none replied.

![](http://www.slothmud.org/images/sco_all2.png)

http://www.slothmud.org/images/sco_all2.png

^^ click link to see full image

</div>
