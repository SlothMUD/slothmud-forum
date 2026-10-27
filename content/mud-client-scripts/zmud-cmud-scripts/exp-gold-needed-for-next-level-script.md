---
title: "Exp/Gold Needed for Next Level Script"
topic_id: 647
author: "karl"
date: 2004-11-30T22:24:42+00:00
last_activity: 2009-06-17T12:21:25+00:00
last_author: "Rigwarl"
sticky: false
locked: false
post_count: 17
---

<div class="post" data-post-id="3084" data-author="karl" data-date="2004-11-30T22:24:42+00:00" data-subject="Exp/Gold Needed for Next Level Script">

I have written a Database in zMUD that contains the EXP/Gold information and then uses the output of the score command to set variables so that when you run a single alias, you are given the proper Exp/Gold for each of your 4 classes, that you need for the next level. It also shows you how much currently unused EXP you have.

If anyone is interested in this I'll post it and the database. Also, if anyone has any suggestions for features for this, please let me know.

</div>

<div class="post" data-post-id="3085" data-author="Nascosto" data-date="2004-11-30T23:55:38+00:00" data-subject="">

just go ahead and post it <img src="/images/smilies/icon_e_smile.svg" alt=":)" title=":)" width="15" height="15" class="smiley nozoom">

I'm always interested to see how other people write scripts anyway

</div>

<div class="post" data-post-id="3091" data-author="Altair" data-date="2004-12-01T08:26:26+00:00" data-subject="">

I'm too lazy for that. Or too focused. I always know which is the next level I want, so I just have a script that captures the cost (yes, I have to go to the guild and ask) and counts xpleft etc etc.

But it's always neat to see the amount of effort and thinking we all go through <img src="/images/smilies/icon_e_biggrin.svg" alt=":D" title=":D" width="15" height="15" class="smiley nozoom">

</div>

<div class="post" data-post-id="3095" data-author="Calim" data-date="2004-12-01T12:18:17+00:00" data-subject="">

Post that thing. That is so cool.

</div>

<div class="post" data-post-id="3102" data-author="karl" data-date="2004-12-01T16:00:34+00:00" data-subject="">

The way this works is:

Everytime time you type score, it updates the STAT\_CurrentEXP and LEVEL\_\* variables with your current info.

Then anytime you want to see what you need to the next level for each class you type tolev.

You'll want to change the tolev alias and replace your 4 class names to show yours, but other then that, that's all there is to it.

```
#TRIGGER {^You have (%d) unused experience points.} {#VAR STAT_CurrentEXP %1}

#TRIGGER {^Your levels: %w: (%d) %w: (%d) %w: (%d) %w: (%d)} {expQuery %1 %2 %3 %4}

#ALIAS expQuery {#VAR myrec { %QUERY( (&Level = %1 + 1), Primary|LevelInfo)};#DBRESET;#VAR LEVEL_Primary { %FORMAT( "&10.0n &10.0n", %db( @myrec, Prime_EXP), %db( @myrec, Prime_Gold))};#VAR myrec { %QUERY( (&Level = %2 + 1), Secondary|LevelInfo)};#DBRESET;#VAR LEVEL_Secondary { %FORMAT( "&10.0n &10.0n", %db( @myrec, Secondary_EXP), %db( @myrec, Secondary_Gold))};#VAR myrec { %QUERY( (&Level = %3 + 1), Tertiary|LevelInfo)};#DBRESET;#VAR LEVEL_Tertiary { %FORMAT( "&10.0n &10.0n", %db( @myrec, Tertiary_EXP), %db( @myrec, Tertiary_Gold))};#VAR myrec { %QUERY( (&Level = %4 + 1), Quad|LevelInfo)};#DBRESET;#VAR LEVEL_Quad { %FORMAT( "&10.0n &10.0n", %db( @myrec, Quad_EXP), %db( @myrec, Quad_Gold))}}

#ALIAS tolev {#SAY Current EXP: %FORMAT( "&15.0n", @STAT_CurrentEXP);#SAY %FORMAT( "&18s&12s", "EXP", "GP");#SAY %FORMAT( &-9s, "Bard") : @LEVEL_Primary;#SAY %FORMAT( &-9s, "Warrior") : @LEVEL_Secondary;#SAY %FORMAT( &-9s, "Mage") : @LEVEL_Tertiary;#SAY %FORMAT( &-9s, "Cleric") : @LEVEL_Quad}
```

Here's the URL where you can download the LevelInfo database.

http://home.earthlink.net/~worgrider/LevelInfo.zip

Just extract the 2 files to your zMUD\\slothmud\\DB directory.

Be sure to do a #DBLOAD LevelInfo and have the Database window open(can be minimized or rolled-up) for it to work.

</div>

<div class="post" data-post-id="3109" data-author="Zenkai" data-date="2004-12-01T22:24:41+00:00" data-subject="">

This is a similiar script that doesn't use database files. 

The script doesn't display coins needed to level (like Karls), but works for avatar characters.

Alias Output:

Unused Xp: 7,546,458

Pri Level: 5,453,542 (58%) Total: 13,000,000

Sec Level: 4,453,542 (62%) Total: 12,000,000

Ter Level: 2,053,542 (78%) Total: 9,600,000

Qua Level: 10,453,542 (41%) Total: 18,000,000

If my character was 40 prime, then the "Pri Level" line would not display.

Alias Output for an Avatar:

Unused Xp: 198,062,256

Ava Level: 351,937,728 (36%) Total: 550,000,000

```
Variable Defaults:

#var xp_variable 0 0

#var pri_xp_variable 0 0

#var sec_xp_variable 0 0

#var ter_xp_variable 0 0

#var qua_xp_variable 0 0

#var av_xp_variable 0 0

-----

Alias: xp

Alias Value:

#show {}

#show {%ansi(2)Unused Xp: %ansi(7)%format("&1.0n",@xp_variable)}

#if (@pri_xp_variable > 1) {#show {%ansi(6)Pri Level: %ansi(7)%format("&1.0n",%eval(@pri_xp_variable-@xp_variable)) %ansi(5)~(%eval((@xp_variable/10)/(@pri_xp_variable/1000))%~) %ansi(6)Total: %ansi(7)%format("&1.0n",@pri_xp_variable)}}

#if (@sec_xp_variable > 1) {#show {%ansi(6)Sec Level: %ansi(7)%format("&1.0n",%eval(@sec_xp_variable-@xp_variable)) %ansi(5)~(%eval((@xp_variable/10)/(@sec_xp_variable/1000))%~) %ansi(6)Total: %ansi(7)%format("&1.0n",@sec_xp_variable)}}

#if (@ter_xp_variable > 1) {#show {%ansi(6)Ter Level: %ansi(7)%format("&1.0n",%eval(@ter_xp_variable-@xp_variable)) %ansi(5)~(%eval((@xp_variable/10)/(@ter_xp_variable/1000))%~) %ansi(6)Total: %ansi(7)%format("&1.0n",@ter_xp_variable)}}

#if (@qua_xp_variable > 1) {#show {%ansi(6)Qua Level: %ansi(7)%format("&1.0n",%eval(@qua_xp_variable-@xp_variable)) %ansi(5)~(%eval((@xp_variable/10)/(@qua_xp_variable/1000))%~) %ansi(6)Total: %ansi(7)%format("&1.0n",@qua_xp_variable)}}

#if (@av_xp_variable > 1) {#show {%ansi(6)Ava Level: %ansi(7)%format("&1.0n",%eval(@av_xp_variable-@xp_variable)) %ansi(5)~(%eval((@xp_variable/10)/(@av_xp_variable/1000))%~) %ansi(6)Total: %ansi(7)%format("&1.0n",@av_xp_variable)}}

-----

Trigger Pattern:

^You have (%d) unused experience points.

Trigger Value:

#var xp_variable %1

-----

Trigger Pattern:

^Your levels: ??: (%d) ??: (%d) ??: (%d) ??: (%d)

Trigger Value:

#var pri_xp_variable %case(%eval(%1+1), 0, 2000, 4000, 9000, 15000, 20000, 30000, 40000, 80000, 120000, 150000, 200000, 250000, 300000, 400000, 450000, 500000, 550000, 600000, 700000, 800000, 1000000, 1500000, 2000000, 2500000, 3500000, 4700000, 6000000, 7300000, 8600000, 9900000, 11000000, 13000000, 15000000, 18300000, 21500000, 25000000, 30000000, 35000000, 40000000, 0)

#var sec_xp_variable %case(%eval(%2+1), 4000, 8000, 16000, 32000, 45000, 70000, 100000, 140000, 280000, 360000, 550000, 800000, 1000000, 1200000, 1600000, 1800000, 2000000, 2200000, 2400000, 2800000, 3200000, 4000000, 6000000, 8000000, 10000000, 12000000, 14800000, 18000000, 21000000, 28000000, 32000000, 36000000, 39000000, 45000000, 50800000, 60500000, 65000000, 70000000, 85000000, 90000000, 0)

#var ter_xp_variable %case(%eval(%3+1), 12000, 24000, 48000, 96000, 135000, 210000, 300000, 420000, 840000, 1080000, 1650000, 2400000, 3000000, 3600000, 4800000, 5400000, 6000000, 6600000, 7200000, 8400000, 9600000, 12000000, 18000000, 24000000, 30000000, 36000000, 44400000, 54000000, 63000000, 84000000, 96000000, 108000000, 117000000, 135000000, 152400000, 181500000, 195000000, 210000000, 255000000, 270000000, 0)

#var qua_xp_variable %case(%eval(%4+1), 40000, 80000, 160000, 320000, 450000, 700000, 1000000, 1400000, 2800000, 3600000, 5500000, 8000000, 10000000, 12000000, 16000000, 18000000, 20000000, 22000000, 24000000, 28000000, 32000000, 40000000, 60000000, 80000000, 100000000, 120000000, 148000000, 180000000, 210000000, 280000000, 320000000, 360000000, 390000000, 450000000, 508000000, 605000000, 650000000, 700000000, 850000000, 900000000, 0)

-----

Trigger Pattern:

^Your levels: ??: %d ??: %d ??: %d ??: %d Av: (%d)

Trigger Value:

#var av_xp_variable %case(%eval(%1+1), 110000000, 140000000, 180000000, 220000000, 260000000, 300000000, 340000000, 380000000, 420000000, 460000000, 500000000, 550000000, 600000000, 650000000, 700000000, 750000000, 800000000, 850000000, 900000000, 950000000, 1050000000, 1100000000, 1200000000, 1300000000, 1400000000, 1500000000, 1600000000, 1700000000, 1800000000, 1900000000, 2000000000, 2100000000, 2100000000, 2100000000, 2100000000, 2100000000, 2100000000, 2100000000, 2100000000, 2100000000, 0)
```

</div>

<div class="post" data-post-id="3449" data-author="Strago" data-date="2004-12-19T22:56:44+00:00" data-subject="">

I liked this script but I didn't like having to type xp to see the info so I use this trigger to link it to scorp

```
Trigger: ^You have (%d) unused experience points.

#var xp_variable %1

#sub {%ansi( 2)Unused Xp: %ansi( 7)%format( "&1.0n", @xp_variable)%cr%ansi( 6)Pri Level: %ansi( 7)%format( "&1.0n", %eval( @pri_xp_variable-@xp_variable)) %ansi( 5)~(%eval( (@xp_variable/10)/(@pri_xp_variable/1000))%~) %ansi( 6)Total: %ansi( 7)%format( "&1.0n", @pri_xp_variable)%cr%ansi( 6)Sec Level: %ansi( 7)%format( "&1.0n", %eval( @sec_xp_variable-@xp_variable)) %ansi( 5)~(%eval( (@xp_variable/10)/(@sec_xp_variable/1000))%~) %ansi( 6)Total: %ansi( 7)%format( "&1.0n", @sec_xp_variable)%cr%ansi( 6)Ter Level: %ansi( 7)%format( "&1.0n", %eval( @ter_xp_variable-@xp_variable)) %ansi( 5)~(%eval( (@xp_variable/10)/(@ter_xp_variable/1000))%~) %ansi( 6)Total: %ansi( 7)%format( "&1.0n", @ter_xp_variable)%cr%ansi( 6)Qua Level: %ansi( 7)%format( "&1.0n", %eval( @qua_xp_variable-@xp_variable)) %ansi( 5)~(%eval( (@xp_variable/10)/(@qua_xp_variable/1000))%~) %ansi( 6)Total: %ansi( 7)%format( "&1.0n", @qua_xp_variable)}
```

The only problem with this (being the whole thing) is not having a level in sec tri quad will mess up the triggers.

</div>

<div class="post" data-post-id="3450" data-author="karl" data-date="2004-12-19T23:11:26+00:00" data-subject="">

I have an update to this script. Shows better output and is liked to Score, and handles not haveing a value for one of your classes levels.

I'll get it posted here this week.

</div>

<div class="post" data-post-id="3455" data-author="Zenkai" data-date="2004-12-20T01:37:48+00:00" data-subject="">

I rather keep the score output as short as possible because of all the spells I have up at tard - the output can get pretty long.

If you want to add coins needed to level to your #sub script, then you could add these lines to the "Your level" triggers:

```
#var pri_coin_variable %case(%eval(%1+1), 0, 150, 200, 250, 300, 540, 780, 1020, 1260, 1500, 2400, 3300, 4200, 5100, 6000, 8400, 10800, 13200, 15600, 18000, 21600, 25200, 28800, 32400, 36000, 43200, 50400, 57600, 64800, 72000, 100800, 129600, 158400, 187200, 216000, 302400, 388800, 475200, 561600, 648000, 0)

#var sec_coin_variable %case(%eval(%2+1), 200, 300, 400, 500, 600, 1200, 1800, 2040, 2520, 3000, 4800, 6600, 8400, 10200, 12000, 16800, 21660, 26400, 31200, 36000, 43200, 50400, 57600, 64800, 72000, 86400, 100800, 115200, 129600, 144000, 201600, 259200, 316800, 374400, 432000, 604800, 777600, 950400, 1123200, 1296000, 0)

#var ter_coin_variable %case(%eval(%3+1), 300, 450, 600, 750, 900, 1620, 2340, 3060, 3780, 4500, 9600, 13200, 12600, 15300, 18000, 25500, 32400, 39600, 46800, 54000, 64800, 75600, 86400, 97200, 108000, 129600, 151200, 172800, 194400, 216000, 302400, 388800, 475200, 561600, 648000, 907200, 1166400, 1425600, 1684800, 1944000, 0)

#var qua_coin_variable %case(%eval(%4+1), 400, 600, 800, 1000, 1200, 2160, 3120, 4080, 5040, 6000, 9600, 13200, 16800, 20400, 24000, 33600, 43200, 52800, 62400, 72000, 86400, 100800, 115200, 129600, 144000, 172800, 201600, 230400, 259200, 288000, 403200, 518400, 633600, 748800, 864000, 1209600, 1555200, 1900800, 2246400, 2592000, 0)

-----

#var av_coin_variable %case(%eval(%1+1), 1000000, 1075000, 1150000, 1225000, 1300000, 1375000, 1450000, 1525000, 1600000, 1675000, 1750000, 1825000, 1900000, 1975000, 2050000, 2125000, 2200000, 2275000, 2350000, 2425000, 2500000, 2575000, 2650000, 2725000, 2800000, 2875000, 2950000, 3025000, 3100000, 3175000, 3250000, 3325000, 3400000, 3475000, 3550000, 3625000, 3700000, 3775000, 3850000, 3925000, 0)
```

And the output could be something like:

Unused Xp: 7,546,458

Pri Level: 5,453,542 (58%) Total Xp: 13,000,000 Total Coin: 158,400

Sec Level: 4,453,542 (62%) Total Xp: 12,000,000 Total Coin: 86,400

Ter Level: 2,053,542 (78%) Total Xp: 9,600,000 Total Coin: 64,800

Qua Level: 10,453,542 (41%) Total Xp: 18,000,000 Total Coin: 33,600

</div>

<div class="post" data-post-id="3741" data-author="Zenkai" data-date="2005-01-12T01:46:31+00:00" data-subject="">

This script works for any class order and any number of classes.

Usage: just type "score" then "xp"

\---

Input:

Your levels: Wa: 34 Ma: 24 Th: 19 Cl: 11 

You have 5000000 unused experience points.

Output--

```
Unused Xp: 5,000,000

Class Level Xp Total Xp Total Coin

------------------------------------------------------------

Pri Wa 35 13,300,000 27% 18,300,000 216,000

Sec Ma 25 5,000,000 50% 10,000,000 72,000

Ter Th 20 3,400,000 59% 8,400,000 54,000

Qua Cl 12 3,000,000 62% 8,000,000 13,200
```

A [Wa 34 Ma 24] shadow character would only display "Pri" and "Sec" lines.

A [Wa 40 Ma 40 Th 19 Cl 11] charcter would only display "Ter" and "Qua" lines.

\---

Input, Avatar Character:

Your levels: Wa: 40 Ma: 40 Th: 40 Cl: 40 Av: 9 

You have 100000000 unused experience points.

Output--

```
Unused Xp: 100,000,000

Class Level Xp Total Xp Total Coin

------------------------------------------------------------

Avatar 10 360,000,000 21% 460,000,000 1,675,000
```

If you wish to install the script just save the following to a text file, then import ASCII script within zMUD.

```
#class {Level_Gain}

#no

#var xp_variable {0} {0}

#var level_variable {0} {0}

#var pri_xp_variable {0} {0}

#var sec_xp_variable {0} {0}

#var ter_xp_variable {0} {0}

#var qua_xp_variable {0} {0}

#var av_xp_variable {0} {0}

#var pri_coin_variable {0} {0}

#var sec_coin_variable {0} {0}

#var ter_coin_variable {0} {0}

#var qua_coin_variable {0} {0}

#var av_coin_variable {0} {0}

#no

#alias xp {

#show {}

#show {%ansi(6)Unused Xp: %ansi(2)%format("&1.0n",@xp_variable)}

#show {}

#show {%ansi(6)"Class Level Xp Total Xp Total Coin"}

#show {%ansi(7)"------------------------------------------------------------"}

#if (@pri_xp_variable > 0) {#show {%ansi(2)Pri %item(@level_variable,1) %format("&2.0n",%eval(%item(@level_variable,2)+1)) %format("&14.0n",%eval(@pri_xp_variable-@xp_variable)) %format("&4.0n",%eval((@xp_variable/10)/(@pri_xp_variable/1000)))% %format("&14.0n",@pri_xp_variable) %format("&14.0n",@pri_coin_variable)}}

#if (@sec_xp_variable > 0) {#show {%ansi(2)Sec %item(@level_variable,3) %format("&2.0n",%eval(%item(@level_variable,4)+1)) %format("&14.0n",%eval(@sec_xp_variable-@xp_variable)) %format("&4.0n",%eval((@xp_variable/10)/(@sec_xp_variable/1000)))% %format("&14.0n",@sec_xp_variable) %format("&14.0n",@sec_coin_variable)}}

#if (@ter_xp_variable > 0) {#show {%ansi(2)Ter %item(@level_variable,5) %format("&2.0n",%eval(%item(@level_variable,6)+1)) %format("&14.0n",%eval(@ter_xp_variable-@xp_variable)) %format("&4.0n",%eval((@xp_variable/10)/(@ter_xp_variable/1000)))% %format("&14.0n",@ter_xp_variable) %format("&14.0n",@ter_coin_variable)}}

#if (@qua_xp_variable > 0) {#show {%ansi(2)Qua %item(@level_variable,7) %format("&2.0n",%eval(%item(@level_variable,8)+1)) %format("&14.0n",%eval(@qua_xp_variable-@xp_variable)) %format("&4.0n",%eval((@xp_variable/10)/(@qua_xp_variable/1000)))% %format("&14.0n",@qua_xp_variable) %format("&14.0n",@qua_coin_variable)}}

#if (@av_xp_variable > 0) {#show {%ansi(2)Avatar %format("&2.0n",%eval(%item(@level_variable,10)+1)) %format("&14.0n",%eval(@av_xp_variable-@xp_variable)) %format("&4.0n",%eval((@xp_variable/10)/(@av_xp_variable/1000)))% %format("&14.0n",@av_xp_variable) %format("&14.0n",@av_coin_variable)}}}

#no

#alias setpri {

#var pri_xp_variable %case(%eval(%1+1), 0, 2000, 4000, 9000, 15000, 20000, 30000, 40000, 80000, 120000, 150000, 200000, 250000, 300000, 400000, 450000, 500000, 550000, 600000, 700000, 800000, 1000000, 1500000, 2000000, 2500000, 3500000, 4700000, 6000000, 7300000, 8600000, 9900000, 11000000, 13000000, 15000000, 18300000, 21500000, 25000000, 30000000, 35000000, 40000000, 0)

#var pri_coin_variable %case(%eval(%1+1), 0, 150, 200, 250, 300, 540, 780, 1020, 1260, 1500, 2400, 3300, 4200, 5100, 6000, 8400, 10800, 13200, 15600, 18000, 21600, 25200, 28800, 32400, 36000, 43200, 50400, 57600, 64800, 72000, 100800, 129600, 158400, 187200, 216000, 302400, 388800, 475200, 561600, 648000, 0)}

#no

#alias setsec {

#var sec_xp_variable %case(%eval(%1+1), 4000, 8000, 16000, 32000, 45000, 70000, 100000, 140000, 280000, 360000, 550000, 800000, 1000000, 1200000, 1600000, 1800000, 2000000, 2200000, 2400000, 2800000, 3200000, 4000000, 6000000, 8000000, 10000000, 12000000, 14800000, 18000000, 21000000, 28000000, 32000000, 36000000, 39000000, 45000000, 50800000, 60500000, 65000000, 70000000, 85000000, 90000000, 0)

#var sec_coin_variable %case(%eval(%1+1), 200, 300, 400, 500, 600, 1200, 1800, 2040, 2520, 3000, 4800, 6600, 8400, 10200, 12000, 16800, 21660, 26400, 31200, 36000, 43200, 50400, 57600, 64800, 72000, 86400, 100800, 115200, 129600, 144000, 201600, 259200, 316800, 374400, 432000, 604800, 777600, 950400, 1123200, 1296000, 0)}

#no

#alias setter {

#var ter_xp_variable %case(%eval(%1+1), 12000, 24000, 48000, 96000, 135000, 210000, 300000, 420000, 840000, 1080000, 1650000, 2400000, 3000000, 3600000, 4800000, 5400000, 6000000, 6600000, 7200000, 8400000, 9600000, 12000000, 18000000, 24000000, 30000000, 36000000, 44400000, 54000000, 63000000, 84000000, 96000000, 108000000, 117000000, 135000000, 152400000, 181500000, 195000000, 210000000, 255000000, 270000000, 0)

#var ter_coin_variable %case(%eval(%1+1), 300, 450, 600, 750, 900, 1620, 2340, 3060, 3780, 4500, 9600, 13200, 12600, 15300, 18000, 25500, 32400, 39600, 46800, 54000, 64800, 75600, 86400, 97200, 108000, 129600, 151200, 172800, 194400, 216000, 302400, 388800, 475200, 561600, 648000, 907200, 1166400, 1425600, 1684800, 1944000, 0)}

#no

#alias setqua {

#var qua_xp_variable %case(%eval(%1+1), 40000, 80000, 160000, 320000, 450000, 700000, 1000000, 1400000, 2800000, 3600000, 5500000, 8000000, 10000000, 12000000, 16000000, 18000000, 20000000, 22000000, 24000000, 28000000, 32000000, 40000000, 60000000, 80000000, 100000000, 120000000, 148000000, 180000000, 210000000, 280000000, 320000000, 360000000, 390000000, 450000000, 508000000, 605000000, 650000000, 700000000, 850000000, 900000000, 0)

#var qua_coin_variable %case(%eval(%1+1), 400, 600, 800, 1000, 1200, 2160, 3120, 4080, 5040, 6000, 9600, 13200, 16800, 20400, 24000, 33600, 43200, 52800, 62400, 72000, 86400, 100800, 115200, 129600, 144000, 172800, 201600, 230400, 259200, 288000, 403200, 518400, 633600, 748800, 864000, 1209600, 1555200, 1900800, 2246400, 2592000, 0)}

#no

#alias setava {

#var av_xp_variable %case(%eval(%1+1), 110000000, 140000000, 180000000, 220000000, 260000000, 300000000, 340000000, 380000000, 420000000, 460000000, 500000000, 550000000, 600000000, 650000000, 700000000, 750000000, 800000000, 850000000, 900000000, 950000000, 1050000000, 1100000000, 1200000000, 1300000000, 1400000000, 1500000000, 1600000000, 1700000000, 1800000000, 1900000000, 2000000000, 2100000000, 2100000000, 2100000000, 2100000000, 2100000000, 2100000000, 2100000000, 2100000000, 2100000000, 0)

#var av_coin_variable %case(%eval(%1+1), 1000000, 1075000, 1150000, 1225000, 1300000, 1375000, 1450000, 1525000, 1600000, 1675000, 1750000, 1825000, 1900000, 1975000, 2050000, 2125000, 2200000, 2275000, 2350000, 2425000, 2500000, 2575000, 2650000, 2725000, 2800000, 2875000, 2950000, 3025000, 3100000, 3175000, 3250000, 3325000, 3400000, 3475000, 3550000, 3625000, 3700000, 3775000, 3850000, 3925000, 0)}

#no

#trigger {^You have (%d) unused experience points.} {

#var xp_variable %1}

#no

#trigger {^Your levels: (%w): (%d) $} {

#var level_variable {%1|%2}

setpri %2}

#no

#trigger {^Your levels: (%w): (%d) (%w): (%d) $} {

#var level_variable {%1|%2|%3|%4}

setpri %2

setsec %4}

#no

#trigger {^Your levels: (%w): (%d) (%w): (%d) (%w): (%d) $} {

#var level_variable {%1|%2|%3|%4|%5|%6}

setpri %2

setsec %4

setter %6}

#no

#trigger {^Your levels: (%w): (%d) (%w): (%d) (%w): (%d) (%w): (%d) $} {

#var level_variable {%1|%2|%3|%4|%5|%6|%7|%8}

setpri %2

setsec %4

setter %6

setqua %8}

#no

#trigger {^Your levels: (%w): (%d) (%w): (%d) (%w): (%d) (%w): (%d) (%w): (%d) $} {

#var level_variable {%1|%2|%3|%4|%5|%6|%7|%8|%9|%10}

setpri %2

setsec %4

setter %6

setqua %8

setava %10}

#no

#class 0
```

To Strago:

If you rather the output be triggered by score, then omit the alias xp and replace this

```
#trigger {^You have (%d) unused experience points.} {

#var xp_variable %1}
```

with the following

```
#trigger {^You have (%d) unused experience points.} {

#var xp_variable %1

#sub {%ansi(2)You have @xp_variable experience points.%if(@pri_xp_variable > 0,%cr%ansi(6)Pri %item(@level_variable,1) %format("&2.0n",%eval(%item(@level_variable,2)+1)): %ansi(7)%format("&1.0n",%eval(@pri_xp_variable-@xp_variable)) %ansi(5)~(%eval((@xp_variable/10)/(@pri_xp_variable/1000))%~) %ansi(6)Total Xp: %ansi(7)%format("&1.0n",@pri_xp_variable) %ansi(6)Total Coin: %ansi(7)%format("&1.0n",@pri_coin_variable))%if(@sec_xp_variable > 0,%cr%ansi(6)Sec %item(@level_variable,3) %format("&2.0n",%eval(%item(@level_variable,4)+1)): %ansi(7)%format("&1.0n",%eval(@sec_xp_variable-@xp_variable)) %ansi(5)~(%eval((@xp_variable/10)/(@sec_xp_variable/1000))%~) %ansi(6)Total Xp: %ansi(7)%format("&1.0n",@sec_xp_variable) %ansi(6)Total Coin: %ansi(7)%format("&1.0n",@sec_coin_variable))%if(@ter_xp_variable > 0,%cr%ansi(6)Ter %item(@level_variable,5) %format("&2.0n",%eval(%item(@level_variable,6)+1)): %ansi(7)%format("&1.0n",%eval(@ter_xp_variable-@xp_variable)) %ansi(5)~(%eval((@xp_variable/10)/(@ter_xp_variable/1000))%~) %ansi(6)Total Xp: %ansi(7)%format("&1.0n",@ter_xp_variable) %ansi(6)Total Coin: %ansi(7)%format("&1.0n",@ter_coin_variable))%if(@qua_xp_variable > 0,%cr%ansi(6)Qua %item(@level_variable,7) %format("&2.0n",%eval(%item(@level_variable,8)+1)): %ansi(7)%format("&1.0n",%eval(@qua_xp_variable-@xp_variable)) %ansi(5)~(%eval((@xp_variable/10)/(@qua_xp_variable/1000))%~) %ansi(6)Total Xp: %ansi(7)%format("&1.0n",@qua_xp_variable) %ansi(6)Total Coin: %ansi(7)%format("&1.0n",@qua_coin_variable))%if(@av_xp_variable > 0,%cr%ansi(6)Avatar %format("&2.0n",%eval(%item(@level_variable,10)+1)): %ansi(7)%format("&1.0n",%eval(@av_xp_variable-@xp_variable)) %ansi(5)~(%eval((@xp_variable/10)/(@av_xp_variable/1000))%~) %ansi(6)Total Xp: %ansi(7)%format("&1.0n",@av_xp_variable) %ansi(6)Total Coin: %ansi(7)%format("&1.0n",@av_coin_variable))}
```

Now the script shouldn't mess up if you don't have levels in sec, ter, or qua class.

</div>

<div class="post" data-post-id="3749" data-author="13" data-date="2005-01-12T14:27:02+00:00" data-subject="">

so all that code just so that you dont have to type 'help tert', look at your score and do basic subtraction ?

seems like a lot of work

</div>

<div class="post" data-post-id="3750" data-author="Strago" data-date="2005-01-12T16:09:56+00:00" data-subject="">

Thanks a lot that looks great, I will test it some when I get home!

</div>

<div class="post" data-post-id="3755" data-author="Strago" data-date="2005-01-12T22:21:06+00:00" data-subject="">

I just installed and ran the script, I have to say it isn really nice! Thanks much.

</div>

<div class="post" data-post-id="29205" data-author="Rigwarl" data-date="2009-05-17T23:59:30+00:00" data-subject="">

Anyone has this updated so it can read if you have 1 level in all classes?

</div>

<div class="post" data-post-id="29348" data-author="norks" data-date="2009-06-10T10:09:17+00:00" data-subject="">

Try this:

based on script by Kanae and data from Zuzu - thanks guys!

```
#CLASS {LEVEL_GAIN}

#ALIAS xp {;#show {};#show {%ansi( 6)Unused Xp: %ansi( 2)%format( "&1.0n", @xp_variable)};#show {};#show {%ansi( 6)"Class Level Xp Total Xp Total Coin"};#show {%ansi( 7)"------------------------------------------------------------"};#if (@pri_xp_variable > 0) {#show {%ansi( 2)Pri %item( @level_variable, 1) %format( "&2.0n", %eval( %item( @level_variable, 2)+1)) %format( "&14.0n", %eval( @pri_xp_variable-@xp_variable)) %format( "&4.0n", %eval( (@xp_variable/10)/(@pri_xp_variable/1000)))% %format( "&14.0n", @pri_xp_variable) %format( "&14.0n", @pri_coin_variable)}};#if (@sec_xp_variable > 0) {#show {%ansi( 2)Sec %item( @level_variable, 3) %format( "&2.0n", %eval( %item( @level_variable, 4)+1)) %format( "&14.0n", %eval( @sec_xp_variable-@xp_variable)) %format( "&4.0n", %eval( (@xp_variable/10)/(@sec_xp_variable/1000)))% %format( "&14.0n", @sec_xp_variable) %format( "&14.0n", @sec_coin_variable)}};#if (@ter_xp_variable > 0) {#show {%ansi( 2)Ter %item( @level_variable, 5) %format( "&2.0n", %eval( %item( @level_variable, 6)+1)) %format( "&14.0n", %eval( @ter_xp_variable-@xp_variable)) %format( "&4.0n", %eval( (@xp_variable/10)/(@ter_xp_variable/1000)))% %format( "&14.0n", @ter_xp_variable) %format( "&14.0n", @ter_coin_variable)}};#if (@qua_xp_variable > 0) {#show {%ansi( 2)Qua %item( @level_variable, 7) %format( "&2.0n", %eval( %item( @level_variable,  SM8) +1)) %format( "&14.0n", %eval( @qua_xp_variable-@xp_variable)) %format( "&4.0n", %eval( (@xp_variable/10)/(@qua_xp_variable/1000)))% %format( "&14.0n", @qua_xp_variable) %format( "&14.0n", @qua_coin_variable)}};#if (@fifth_xp_variable > 0) {#show {%ansi( 2)Fif %item( @level_variable, 9) %format( "&2.0n", %eval( %item( @level_variable, 10)+1)) %format( "&14.0n", %eval( @fifth_xp_variable-@xp_variable)) %format( "&4.0n", %eval( (@xp_variable/10)/(@fifth_xp_variable/1000)))% %format( "&14.0n", @fifth_xp_variable) %format( "&14.0n", @fifth_coin_variable)}};#if (@sixth_xp_variable > 0) {#show {%ansi( 2)Six %item( @level_variable, 11) %format( "&2.0n", %eval( %item( @level_variable, 12)+1)) %format( "&14.0n", %eval( @sixth_xp_variable-@xp_variable)) %format( "&4.0n", %eval( (@xp_variable/10)/(@sixth_xp_variable/1000)))% %format( "&14.0n", @sixth_xp_variable) %format( "&14.0n", @sixth_coin_variable)}};#if (@seventh_xp_variable > 0) {#show {%ansi( 2)Sev %item( @level_variable, 13) %format( "&2.0n", %eval( %item( @level_variable, 14)+1)) %format( "&14.0n", %eval( @seventh_xp_variable-@xp_variable)) %format( "&4.0n", %eval( (@xp_variable/10)/(@seventh_xp_variable/1000)))% %format( "&14.0n", @seventh_xp_variable) %format( "&14.0n", @seventh_coin_variable)}};#if (@eigth_xp_variable > 0) {#show {%ansi( 2)Eig %item( @level_variable, 15) %format( "&2.0n", %eval( %item( @level_variable, 16)+1)) %format( "&14.0n", %eval( @eigth_xp_variable-@xp_variable)) %format( "&4.0n", %eval( (@xp_variable/10)/(@eigth_xp_variable/1000)))% %format( "&14.0n", @eigth_xp_variable) %format( "&14.0n", @eigth_coin_variable)}};#if (@av_xp_variable > 0) {#show {%ansi( 2)Ava %item( @level_variable, 17) %format( "&2.0n", %eval( %item( @level_variable, 18)+1)) %format( "&14.0n", %eval( @av_xp_variable-@xp_variable)) %format( "&4.0n", %eval( (@xp_variable/10)/(@av_xp_variable/1000)))% %format( "&14.0n", @av_xp_variable) %format( "&14.0n", @av_coin_variable)}};#no} "Level_Gain"

#ALIAS setpri {#var pri_xp_variable %case(%eval(%1+1), 0, 2000, 4000, 9000, 15000, 20000, 30000, 40000, 80000, 120000, 150000, 200000, 250000, 300000, 400000, 450000, 500000, 550000, 600000, 700000, 800000, 1000000, 1500000, 2000000, 2500000, 3500000, 4700000, 6000000, 7300000, 8600000, 9900000, 11000000, 13000000, 15000000, 18300000, 21500000, 25000000, 30000000, 35000000, 40000000, 0);#var pri_coin_variable %case(%eval(%1+1), 0, 150, 200, 250, 300, 540, 780, 1020, 1260, 1500, 2400, 3300, 4200, 5100, 6000, 8400, 10800, 13200, 15600, 18000, 21600, 25200, 28800, 32400, 36000, 43200, 50400, 57600, 64800, 72000, 100800, 129600, 158400, 187200, 216000, 302400, 388800, 475200, 561600, 648000, 0)} "Level_Gain"

#ALIAS setsec {#var sec_xp_variable %case(%eval(%1+1), 4000, 8000, 16000, 32000, 45000, 70000, 100000, 140000, 280000, 360000, 550000, 800000, 1000000, 1200000, 1600000, 1800000, 2000000, 2200000, 2400000, 2800000, 3200000, 4000000, 6000000, 8000000, 10000000, 12000000, 14800000, 18000000, 21000000, 28000000, 32000000, 36000000, 39000000, 45000000, 50800000, 60500000, 65000000, 70000000, 85000000, 90000000, 0);#var sec_coin_variable %case(%eval(%1+1), 200, 300, 400, 500, 600, 1200, 1800, 2040, 2520, 3000, 4800, 6600, 8400, 10200, 12000, 16800, 21660, 26400, 31200, 36000, 43200, 50400, 57600, 64800, 72000, 86400, 100800, 115200, 129600, 144000, 201600, 259200, 316800, 374400, 432000, 604800, 777600, 950400, 1123200, 1296000, 0)} "Level_Gain"

#ALIAS setter {#var ter_xp_variable %case(%eval(%1+1), 12000, 24000, 48000, 96000, 135000, 210000, 300000, 420000, 840000, 1080000, 1650000, 2400000, 3000000, 3600000, 4800000, 5400000, 6000000, 6600000, 7200000, 8400000, 9600000, 12000000, 18000000, 24000000, 30000000, 36000000, 44400000, 54000000, 63000000, 84000000, 96000000, 108000000, 117000000, 135000000, 152400000, 181500000, 195000000, 210000000, 255000000, 270000000, 0);#var ter_coin_variable %case(%eval(%1+1), 300, 450, 600, 750, 900, 1620, 2340, 3060, 3780, 4500, 9600, 13200, 12600, 15300, 18000, 25500, 32400, 39600, 46800, 54000, 64800, 75600, 86400, 97200, 108000, 129600, 151200, 172800, 194400, 216000, 302400, 388800, 475200, 561600, 648000, 907200, 1166400, 1425600, 1684800, 1944000, 0)} "Level_Gain"

#ALIAS setqua {#var qua_xp_variable %case(%eval(%1+1), 40000, 80000, 160000, 320000, 450000, 700000, 1000000, 1400000, 2800000, 3600000, 5500000, 8000000, 10000000, 12000000, 16000000, 18000000, 20000000, 22000000, 24000000, 28000000, 32000000, 40000000, 60000000, 80000000, 100000000, 120000000, 148000000, 180000000, 210000000, 280000000, 320000000, 360000000, 390000000, 450000000, 508000000, 605000000, 650000000, 700000000, 850000000, 900000000, 0);#var qua_coin_variable %case(%eval(%1+1), 400, 600, 800, 1000, 1200, 2160, 3120, 4080, 5040, 6000, 9600, 13200, 16800, 20400, 24000, 33600, 43200, 52800, 62400, 72000, 86400, 100800, 115200, 129600, 144000, 172800, 201600, 230400, 259200, 288000, 403200, 518400, 633600, 748800, 864000, 1209600, 1555200, 1900800, 2246400, 2592000, 0)} "Level_Gain"

#ALIAS setfif {#var fifth_xp_variable %case(%eval(%1+1), 80000, 160000, 320000, 640000, 900000, 1400000, 2000000, 2800000, 5600000, 7200000, 11000000, 16000000, 20000000, 24000000, 32000000, 36000000, 40000000, 44000000, 48000000, 56000000, 64000000, 80000000, 120000000, 160000000, 200000000, 240000000, 296000000, 360000000, 420000000, 560000000, 640000000, 720000000, 780000000, 900000000, 1016000000, 1210000000, 1300000000, 1400000000, 1700000000, 1800000000, 0);#var fifth_coin_variable %case(%eval(%1+1), 500, 750, 1000, 1250, 1500, 2700, 3900, 5100, 6300, 7500, 12000, 16500, 21000, 25500, 30000, 42000, 54000, 66000, 78000, 90000, 108000, 126000, 144000, 162000, 180000, 216000, 252000, 288000, 324000, 360000, 504000, 648000, 792000, 936000, 1080000, 1512000, 1944000, 2376000, 2808000, 3240000, 0)} "Level_Gain"

#ALIAS setsix {#var sixth_xp_variable %case(%eval(%1+1), 60000, 120000, 240000, 480000, 960000, 700000, 1350000, 2800000, 9600000, 13500000, 2100000, 3000000, 42000000, 84000000, 16000000, 18000000, 20000000, 22000000, 24000000, 48000000, 32000000, 40000000, 60000000, 80000000, 100000000, 120000000, 148000000, 180000000, 210000000, 280000000, 320000000, 360000000, 390000000, 450000000, 508000000, 605000000, 650000000, 700000000, 850000000, 900000000, 0);#var sixth_coin_variable %case(%eval(%1+1), 1200, 1800, 2400, 3000, 3600, 6480, 9360, 12240, 15120, 18000, 28800, 39600, 50400, 61200, 72000, 100800, 129600, 158400, 187200, 216000, 259200, 302400, 345600, 388800, 432000, 518400, 604800, 691200, 777600, 864000, 1209600, 1555200, 1900800, 2246400, 2592000, 3628800, 4665600, 5702400, 6739200, 7776000, 0)} "Level_Gain"

#ALIAS setsev {#var seventh_xp_variable %case(%eval(%1+1), 240000, 480000, 960000, 1920000, 2700000, 4200000, 6000000, 8400000, 16800000, 21600000, 33000000, 48000000, 60000000, 72000000, 96000000, 108000000, 120000000, 132000000, 144000000, 168000000, 192000000, 240000000, 360000000, 480000000, 600000000, 720000000, 888000000, 1080000000, 1260000000, 1680000000, 1920000000, 2160000000, 2340000000, 2700000000, 3048000000, 3630000000, 3900000000, 4200000000, 5100000000, 5400000000, 0);#var seventh_coin_variable %case(%eval(%1+1), 1400, 2100, 2800, 3500, 4200, 7560, 10920, 14280, 17640, 21000, 33600, 46200, 58800, 71400, 84000, 117600, 151200, 184800, 218400, 252000, 302400, 352800, 403200, 453600, 504000, 604800, 705600, 806400, 907200, 1008000, 1411200, 1814400, 2217600, 2620800, 3024000, 4233600, 5443200, 6652800, 7862400, 9072000, 0)} "Level_Gain"

#ALIAS seteig {#var eigth_xp_variable %case(%eval(%1+1), 320000, 640000, 1280000, 2560000, 3600000, 5600000, 8000000, 11200000, 22400000, 28800000, 44000000, 64000000, 80000000, 96000000, 128000000, 144000000, 160000000, 176000000, 192000000, 224000000, 256000000, 320000000, 480000000, 640000000, 800000000, 960000000, 1184000000, 1440000000, 1680000000, 2240000000, 2560000000, 2880000000, 3120000000, 3600000000, 4064000000, 4840000000, 5200000000, 5600000000, 6800000000, 7200000000, 0);#var eigth_coin_variable %case(%eval(%1+1), 1600, 2400, 3200, 4000, 4800, 8640, 12480, 16320, 20160, 24000, 38400, 52800, 67200, 81600, 96000, 134400, 172800, 211200, 249600, 288000, 345600, 403200, 460800, 518400, 576000, 691200, 806400, 921600, 1036800, 1152000, 1612800, 2073600, 2534400, 2995200, 3456000, 4838400, 6220800, 7603200, 8985600, 10368000, 0)} "Level_Gain"

#ALIAS setava {#var av_xp_variable %case( %eval( %1+1), 110000000, 140000000, 180000000, 220000000, 260000000, 300000000, 340000000, 380000000, 420000000, 460000000, 500000000, 550000000, 600000000, 650000000, 700000000, 750000000, 800000000, 850000000, 900000000, 950000000, 1050000000, 1100000000, 1200000000, 1300000000, 1400000000, 1500000000, 1600000000, 1700000000, 1800000000, 1900000000, 2000000000, 2100000000, 2100000000, 2100000000, 2100000000, 2100000000, 2100000000, 2100000000, 2100000000, 2100000000, 0);#var av_coin_variable %case( %eval( %1+1), 1000000, 1075000, 1150000, 1225000, 1300000, 1375000, 1450000, 1525000, 1600000, 1675000, 1750000, 1825000, 1900000, 1975000, 2050000, 2125000, 2200000, 2275000, 2350000, 2425000, 2500000, 2575000, 2650000, 2725000, 2800000, 2875000, 2950000, 3025000, 3100000, 3175000, 3250000, 3325000, 3400000, 3475000, 3550000, 3625000, 3700000, 3775000, 3850000, 3925000, 0);#no} "Level_Gain"

#VAR xp_variable {0} {0} "Level_Gain"

#VAR level_variable {0} {0} "Level_Gain"

#VAR pri_xp_variable {0} {0} "Level_Gain"

#VAR sec_xp_variable {0} {0} "Level_Gain"

#VAR ter_xp_variable {0} {0} "Level_Gain"

#VAR qua_xp_variable {0} {0} "Level_Gain"

#VAR fifth_xp_variable {0} {0} "Level_Gain"

#VAR sixth_xp_variable {0} {0} "Level_Gain"

#VAR seventh_xp_variable {0} {0} "Level_Gain"

#VAR eigth_xp_variable {0} {0} "Level_Gain"

#VAR av_xp_variable {0} {0} "Level_Gain"

#VAR pri_coin_variable {0} {0} "Level_Gain"

#VAR sec_coin_variable {0} {0} "Level_Gain"

#VAR ter_coin_variable {0} {0} "Level_Gain"

#VAR qua_coin_variable {0} {0} "Level_Gain"

#VAR fifth_coin_variable {0} {0} "Level_Gain"

#VAR sixth_coin_variable {0} {0} "Level_Gain"

#VAR seventh_coin_variable {0} {0} "Level_Gain"

#VAR eigth_coin_variable {0} {0} "Level_Gain"

#VAR av_coin_variable {0} {0} "Level_Gain"

#TRIGGER {^You have (%d) unused experience points.} {#var xp_variable %1} "Level_Gain"

#TRIGGER {^Your levels: (%w): (%d) $} {#var level_variable {%1|%2};setpri %2} "Level_Gain"

#TRIGGER {^Your levels: (%w): (%d) (%w): (%d) $} {#var level_variable {%1|%2|%3|%4};setpri %2;setsec %4} "Level_Gain"

#TRIGGER {^Your levels: (%w): (%d) (%w): (%d) (%w): (%d) $} {#var level_variable {%1|%2|%3|%4|%5|%6};setpri %2;setsec %4;setter %6} "Level_Gain"

#TRIGGER {^Your levels: (%w): (%d) (%w): (%d) (%w): (%d) (%w): (%d) $} {#var level_variable {%1|%2|%3|%4|%5|%6|%7|%8};setpri %2;setsec %4;setter %6;setqua %8} "Level_Gain"

#TRIGGER {^Your levels: (%w): (%d) (%w): (%d) (%w): (%d) (%w): (%d) (%w): (%d) $} {#var level_variable {%1|%2|%3|%4|%5|%6|%7|%8|%9|%10};setpri %2;setsec %4;setter %6;setqua %8;setfif %10} "Level_Gain"

#TRIGGER {^Your levels: (%w): (%d) (%w): (%d) (%w): (%d) (%w): (%d) (%w): (%d) (%w): (%d) $} {#var level_variable {%1|%2|%3|%4|%5|%6|%7|%8|%9|%10|%11|%12};setpri %2;setsec %4;setter %6;setqua %8;setfif %10;setsix %12} "Level_Gain"

#TRIGGER {^Your levels: (%w): (%d) (%w): (%d) (%w): (%d) (%w): (%d) (%w): (%d) (%w): (%d) (%w): (%d) $} {#var level_variable {%1|%2|%3|%4|%5|%6|%7|%8|%9|%10|%11|%12|%13|%14};setpri %2;setsec %4;setter %6;setqua %8;setfif %10;setsix %12;setsev %14} "Level_Gain"

#TRIGGER {^Your levels: (%w): (%d) (%w): (%d) (%w): (%d) (%w): (%d) (%w): (%d) (%w): (%d) (%w): (%d) (%w): (%d) $} {#var level_variable {%1|%2|%3|%4|%5|%6|%7|%8|%9|%10|%11|%12|%13|%14|%15|%16};setpri %2;setsec %4;setter %6;setqua %8;setfif %10;setsix %12;setsev %14;seteig %16} "Level_Gain"

#TRIGGER {^Your levels: (%w): (%d) (%w): (%d) (%w): (%d) (%w): (%d) (%w): (%d) (%w): (%d) (%w): (%d)(%w): (%d) (%w): (%d) $} {#var level_variable {%1|%2|%3|%4|%5|%6|%7|%8|%9|%10|%11|%12|%13|%14|%15|%16|%17|%18};setpri %2;setsec %4;setter %6;setqua %8;setfif %10;setsix %12;setsev %14;seteig %16;setava %18} "Level_Gain"

#CLASS 0
```

</div>

<div class="post" data-post-id="29546" data-author="islq" data-date="2009-06-17T03:18:19+00:00" data-subject="">

something wrong with the xp table of sixth class

</div>

<div class="post" data-post-id="29548" data-author="Rigwarl" data-date="2009-06-17T12:21:25+00:00" data-subject="">

Hey Guys,

To fix the 6th level code, simply press the alias button on zmud and search for setsix

There, paste this modified code

```
#var sixth_xp_variable %case( %eval( %1+1), 120000, 240000, 480000, 960000, 1350000, 2100000, 3000000, 4200000, 8400000, 10800000, 16500000, 24000000, 30000000, 36000000, 48000000, 54000000, 60000000, 66000000, 72000000, 84000000, 96000000, 120000000, 180000000, 240000000, 300000000, 360000000, 444000000, 540000000, 630000000, 840000000, 960000000, 1080000000, 1170000000, 1350000000, 1524000000, 1815000000, 1950000000, 2100000000, 2550000000, 2700000000, 0)

#var sixth_coin_variable %case( %eval( %1+1), 1200, 1800, 2400, 3000, 3600, 6480, 9360, 12240, 15120, 18000, 28800, 39600, 50400, 61200, 72000, 100800, 129600, 158400, 187200, 216000, 259200, 302400, 345600, 388800, 432000, 518400, 604800, 691200, 777600, 864000, 1209600, 1555200, 1900800, 2246400, 2592000, 3628800, 4665600, 5702400, 6739200, 7776000, 0)
```

I realize not everyone must be on Zmud, so here's the EXP/Coins chart in Table format that may be used for Sloth Website.

[http://pastehtml.com/view/090617eBJFfJ30.html](http://pastehtml.com/view/090617eBJFfJ30.html)

I would like to thank Norks for the spreadsheet and Zuzuzuzuzuzzu for compiling the guestimated EXP / Coins chart.

\-Rig

</div>
