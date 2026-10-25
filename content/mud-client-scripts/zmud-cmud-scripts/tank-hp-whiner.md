---
title: "Tank HP whiner"
topic_id: 1055
author: "slice"
date: 2005-04-30T11:43:46+00:00
last_activity: 2005-04-30T11:43:46+00:00
last_author: "slice"
sticky: false
locked: false
post_count: 1
---

<div class="post" data-post-id="5883" data-author="slice" data-date="2005-04-30T11:43:46+00:00">

A tank hitpoint whiner, some of the features are:

[list:1khtqeaa]

Captures your current state from prompt - [i:1khtqeaa]hitpoint, mana, move, armour[/i:1khtqeaa]

Minimum hp variation whine - [i:1khtqeaa]hitpointreport[/i:1khtqeaa]

Percentage colour highlights - [i:1khtqeaa]colHealRedFlash, colHealRed, colHealYellow, colPerc [/i:1khtqeaa]

Variable Whine activation e.g. gt, ct, say, emote - [i:1khtqeaa]command [/i:1khtqeaa]

Score will update your max values - [i:1khtqeaa]hitpointmax, manamax, movemax[/i:1khtqeaa]

[/list:u:1khtqeaa]

You may need to modify your prompt or the trigger condition to match your own prompt, if you change the trigger conditions especially the order of the hp, ma, mv you'll need to fix the code.  Also remember to switch off "expand vars", copy and paste the code into [b:1khtqeaa]zMUD Editor [/b:1khtqeaa]and click on [b:1khtqeaa]Send[/b:1khtqeaa].

Some downsides are that it isn't efficient, you could remove the variables like move, mana which you aren't using.

You may also wish to change your prompt to hold the max move, mana, hitpoint values so that the score trigger wouldn't be necessary.

The percentage colours idea is such that at green > 70% - usually no need to heal, amber 30-70% - heal now, red 10-30% - emergency heal now, flashing red <10% - about to die.  You can adjust your color percentages to your taste.  I used percentages as so many factors cause ones hps to vary.

Note: if you have problems running the script through aMUD editor you'll need to manually create the triggers and aliases.

[code:1khtqeaa]

#CLASS "mystats"

#VARIABLE whinemode 0

#VARIABLE hitpoint 0

#VARIABLE hitpointold 0

#VARIABLE hitpointmax 0

#VARIABLE hitpointpercent 0

#VARIABLE hitpointdiff 0

#VARIABLE hitpointreport 20

#VARIABLE mana 0

#VARIABLE manaold 0

#VARIABLE manamax 0

#VARIABLE manapercent 0

#VARIABLE move 0

#VARIABLE moveold 0

#VARIABLE movemax 0

#VARIABLE movepercent 0

#VARIABLE armour 0

#VARIABLE command grouptell

#VARIABLE colHealRedFlash 10

#VARIABLE colHealRed 30

#VARIABLE colHealYellow 70

#VARIABLE colPerc \d03

#TRIGGER {^<(%d)hp (%d)ma (%d)mv (%n).(%d)ac>$} {#var hitpoint %1;#var mana %2;#var move %3;#var armour %4;#var command grouptell;#var hitpointreport 20;#var colHealRedFlash 10;#var colHealRed 30;#var colHealYellow 70;#var colPerc \d03;#MATH manapercent (@mana * 100 / @manamax);#MATH hitpointpercent (@hitpoint * 100 / @hitpointmax);#MATH movepercent (@move * 100 / @movemax);#MATH hitpointdiff (@hitpoint - @hitpointold);#IF (@hitpointpercent < @colHealYellow) {#var colPerc \d04};#IF (@hitpointpercent < @colHealRed) {#var colPerc \d02};#IF (@hitpointpercent < @colHealRedFlash) {#var colPerc \a06\d02};#IF (@hitpointpercent > 100) {#var colPerc \a02\d03};#IF (@whinemode = 1 & @hitpoint < @hitpointold - @hitpointreport) {@command \d02---- Owww! @hitpointdiff~hp ---- \c02~[@hitpoint/@hitpointmax~]@colPerc @hitpointpercent~%\a01\c02};#IF (@whinemode = 1 & @hitpoint > @hitpointold + @hitpointreport) {@command \d03++++ Ahhh! +@hitpointdiff~hp ++++ \c02~[@hitpoint/@hitpointmax~]@colPerc @hitpointpercent~%\a01\c02};#var hitpointold @hitpoint;#var manaold @mana;#var moveold @move} "" {prompt|notrig}

#TRIGGER {^You have ~((%d)/(%d)(%n)~) hit, ~((%d)/(%d)(%n)~) mana and ~((%d)/(%d)(%n)~) movement points.} {#var hitpointmax %2;#var manamax %5;#var movemax %8} "" {case|notrig}

#ALIAS whineon {#var whinemode 1;grouptell ENABLED: My own personal hitpoint whiner.}

#ALIAS whineoff {#var whinemode 0;grouptell DISABLED: I will no longer complain about being hit.}

#CLASS 0

[/code:1khtqeaa]

</div>
