---
title: "CMUD: EXP Tracker"
topic_id: 3423
author: "Gladavar"
date: 2010-05-13T04:40:29+00:00
last_activity: 2012-08-26T17:34:44+00:00
last_author: "kalidor"
sticky: false
locked: false
post_count: 6
---

<div class="post" data-post-id="31152" data-author="Gladavar" data-date="2010-05-13T04:40:29+00:00" data-subject="CMUD: EXP Tracker">

This is my setup for tracking Exp across classes in CMUD.  Due to a previous bug, you need  v3.17 or later for this to work fully. Once installed type score to set the buttons up.

This will throw 9 gauges across the top of your main session window which will then fill to show how close to a level you are in each class.  Each button's caption will automatically be set to the class and level of that class once you type score.

First you need a trigger for your prompt that will pull your current exp out and store it in     @EXP_Current    .   Once you have that put the following code into the script text box of that trigger and save.

```
  
// Class 1
#switch (@class1Level = 1) {#var Class1ExpNeeded 2000;#var Class1GoldNeeded 150}
  (@class1Level = 2) {#var Class1ExpNeeded 4000;#var Class1GoldNeeded 200}
  (@class1Level = 3) {#var Class1ExpNeeded 9000;#var Class1GoldNeeded 250}
  (@class1Level = 4) {#var Class1ExpNeeded 15000;#var Class1GoldNeeded 300}
  (@class1Level = 5) {#var Class1ExpNeeded 20000;#var Class1GoldNeeded 540}
  (@class1Level = 6) {#var Class1ExpNeeded 30000;#var Class1GoldNeeded 780}
  (@class1Level = 7) {#var Class1ExpNeeded 40000;#var Class1GoldNeeded 1020}
  (@class1Level = 8) {#var Class1ExpNeeded 80000;#var Class1GoldNeeded 1260}
  (@class1Level = 9) {#var Class1ExpNeeded 120000;#var Class1GoldNeeded 1500}
  (@class1Level = 10) {#var Class1ExpNeeded 150000;#var Class1GoldNeeded 2400}
  (@class1Level = 11) {#var Class1ExpNeeded 200000;#var Class1GoldNeeded 3300}
  (@class1Level = 12) {#var Class1ExpNeeded 250000;#var Class1GoldNeeded 4200}
  (@class1Level = 13) {#var Class1ExpNeeded 300000;#var Class1GoldNeeded 5100}
  (@class1Level = 14) {#var Class1ExpNeeded 400000;#var Class1GoldNeeded 6000}
  (@class1Level = 15) {#var Class1ExpNeeded 450000;#var Class1GoldNeeded 8400}
  (@class1Level = 16) {#var Class1ExpNeeded 500000;#var Class1GoldNeeded 10800}
  (@class1Level = 17) {#var Class1ExpNeeded 550000;#var Class1GoldNeeded 13200}
  (@class1Level = 18) {#var Class1ExpNeeded 600000;#var Class1GoldNeeded 15600}
  (@class1Level = 19) {#var Class1ExpNeeded 700000;#var Class1GoldNeeded 18000}
  (@class1Level = 20) {#var Class1ExpNeeded 800000;#var Class1GoldNeeded 21600}
  (@class1Level = 21) {#var Class1ExpNeeded 1000000;#var Class1GoldNeeded 25200}
  (@class1Level = 22) {#var Class1ExpNeeded 1500000;#var Class1GoldNeeded 28800}
  (@class1Level = 23) {#var Class1ExpNeeded 2000000;#var Class1GoldNeeded 32400}
  (@class1Level = 24) {#var Class1ExpNeeded 2500000;#var Class1GoldNeeded 36000}
  (@class1Level = 25) {#var Class1ExpNeeded 3500000;#var Class1GoldNeeded 43200}
  (@class1Level = 26) {#var Class1ExpNeeded 4700000;#var Class1GoldNeeded 50400}
  (@class1Level = 27) {#var Class1ExpNeeded 6000000;#var Class1GoldNeeded 57600}
  (@class1Level = 28) {#var Class1ExpNeeded 7300000;#var Class1GoldNeeded 64800}
  (@class1Level = 29) {#var Class1ExpNeeded 8600000;#var Class1GoldNeeded 72000}
  (@class1Level = 30) {#var Class1ExpNeeded 9900000;#var Class1GoldNeeded 100800}
  (@class1Level = 31) {#var Class1ExpNeeded 11000000;#var Class1GoldNeeded 129600}
  (@class1Level = 32) {#var Class1ExpNeeded 13000000;#var Class1GoldNeeded 158400}
  (@class1Level = 33) {#var Class1ExpNeeded 15000000;#var Class1GoldNeeded 187200}
  (@class1Level = 34) {#var Class1ExpNeeded 18300000;#var Class1GoldNeeded 216000}
  (@class1Level = 35) {#var Class1ExpNeeded 21500000;#var Class1GoldNeeded 302400}
  (@class1Level = 36) {#var Class1ExpNeeded 25000000;#var Class1GoldNeeded 388800}
  (@class1Level = 37) {#var Class1ExpNeeded 30000000;#var Class1GoldNeeded 475200}
  (@class1Level = 38) {#var Class1ExpNeeded 35000000;#var Class1GoldNeeded 561600}
  (@class1Level = 39) {#var Class1ExpNeeded 40000000;#var Class1GoldNeeded 648000}
  (@class1Level = 40) {#var Class1ExpNeeded Maxed;#var Class1GoldNeeded Maxed}

// Class 2  
#switch (@class2Level = 0) {#var Class2ExpNeeded 4000;#var Class2GoldNeeded 200}
  (@class2Level = 1) {#var Class2ExpNeeded 8000;#var Class2GoldNeeded 300}
  (@class2Level = 2) {#var Class2ExpNeeded 16000;#var Class2GoldNeeded 400}
  (@class2Level = 3) {#var Class2ExpNeeded 32000;#var Class2GoldNeeded 500}
  (@class2Level = 4) {#var Class2ExpNeeded 45000;#var Class2GoldNeeded 600}
  (@class2Level = 5) {#var Class2ExpNeeded 70000;#var Class2GoldNeeded 1200}
  (@class2Level = 6) {#var Class2ExpNeeded 100000;#var Class2GoldNeeded 1800}
  (@class2Level = 7) {#var Class2ExpNeeded 140000;#var Class2GoldNeeded 2040}
  (@class2Level = 8) {#var Class2ExpNeeded 280000;#var Class2GoldNeeded 2520}
  (@class2Level = 9) {#var Class2ExpNeeded 360000;#var Class2GoldNeeded 3000}
  (@class2Level = 10) {#var Class2ExpNeeded 550000;#var Class2GoldNeeded 4800}
  (@class2Level = 11) {#var Class2ExpNeeded 800000;#var Class2GoldNeeded 6600}
  (@class2Level = 12) {#var Class2ExpNeeded 1000000;#var Class2GoldNeeded 8400}
  (@class2Level = 13) {#var Class2ExpNeeded 1200000;#var Class2GoldNeeded 10200}
  (@class2Level = 14) {#var Class2ExpNeeded 1600000;#var Class2GoldNeeded 12000}
  (@class2Level = 15) {#var Class2ExpNeeded 1800000;#var Class2GoldNeeded 16800}
  (@class2Level = 16) {#var Class2ExpNeeded 2000000;#var Class2GoldNeeded 21660}
  (@class2Level = 17) {#var Class2ExpNeeded 2200000;#var Class2GoldNeeded 26400}
  (@class2Level = 18) {#var Class2ExpNeeded 2400000;#var Class2GoldNeeded 31200}
  (@class2Level = 19) {#var Class2ExpNeeded 2800000;#var Class2GoldNeeded 36000}
  (@class2Level = 20) {#var Class2ExpNeeded 3200000;#var Class2GoldNeeded 43200}
  (@class2Level = 21) {#var Class2ExpNeeded 4000000;#var Class2GoldNeeded 50400}
  (@class2Level = 22) {#var Class2ExpNeeded 6000000;#var Class2GoldNeeded 57600}
  (@class2Level = 23) {#var Class2ExpNeeded 8000000;#var Class2GoldNeeded 64800}
  (@class2Level = 24) {#var Class2ExpNeeded 10000000;#var Class2GoldNeeded 72000}
  (@class2Level = 25) {#var Class2ExpNeeded 12000000;#var Class2GoldNeeded 86400}
  (@class2Level = 26) {#var Class2ExpNeeded 14800000;#var Class2GoldNeeded 100800}
  (@class2Level = 27) {#var Class2ExpNeeded 18000000;#var Class2GoldNeeded 115200}
  (@class2Level = 28) {#var Class2ExpNeeded 21000000;#var Class2GoldNeeded 129600}
  (@class2Level = 29) {#var Class2ExpNeeded 28000000;#var Class2GoldNeeded 144000}
  (@class2Level = 30) {#var Class2ExpNeeded 32000000;#var Class2GoldNeeded 201600}
  (@class2Level = 31) {#var Class2ExpNeeded 36000000;#var Class2GoldNeeded 259200}
  (@class2Level = 32) {#var Class2ExpNeeded 39000000;#var Class2GoldNeeded 316800}
  (@class2Level = 33) {#var Class2ExpNeeded 45000000;#var Class2GoldNeeded 374400}
  (@class2Level = 34) {#var Class2ExpNeeded 50800000;#var Class2GoldNeeded 432000}
  (@class2Level = 35) {#var Class2ExpNeeded 60500000;#var Class2GoldNeeded 604800}
  (@class2Level = 36) {#var Class2ExpNeeded 65000000;#var Class2GoldNeeded 777600}
  (@class2Level = 37) {#var Class2ExpNeeded 70000000;#var Class2GoldNeeded 950400}
  (@class2Level = 38) {#var Class2ExpNeeded 85000000;#var Class2GoldNeeded 1124000}
  (@class2Level = 39) {#var Class2ExpNeeded 90000000;#var Class2GoldNeeded 1297000}
  (@class2Level = 40) {#var Class2ExpNeeded Maxed;#var Class2GoldNeeded Maxed}

// Class 3
#switch   (@class3Level = 0) {#var Class3ExpNeeded 12000;#var Class3GoldNeeded 300}
  (@class3Level = 1) {#var Class3ExpNeeded 24000;#var Class3GoldNeeded 450}
  (@class3Level = 2) {#var Class3ExpNeeded 48000;#var Class3GoldNeeded 600}
  (@class3Level = 3) {#var Class3ExpNeeded 96000;#var Class3GoldNeeded 750}
  (@class3Level = 4) {#var Class3ExpNeeded 135000;#var Class3GoldNeeded 900}
  (@class3Level = 5) {#var Class3ExpNeeded 210000;#var Class3GoldNeeded 1620}
  (@class3Level = 6) {#var Class3ExpNeeded 300000;#var Class3GoldNeeded 2340}
  (@class3Level = 7) {#var Class3ExpNeeded 420000;#var Class3GoldNeeded 3060}
  (@class3Level = 8) {#var Class3ExpNeeded 840000;#var Class3GoldNeeded 3780}
  (@class3Level = 9) {#var Class3ExpNeeded 1080000;#var Class3GoldNeeded 4500}
  (@class3Level = 10) {#var Class3ExpNeeded 1650000;#var Class3GoldNeeded 9600}
  (@class3Level = 11) {#var Class3ExpNeeded 2400000;#var Class3GoldNeeded 13200}
  (@class3Level = 12) {#var Class3ExpNeeded 3000000;#var Class3GoldNeeded 12600}
  (@class3Level = 13) {#var Class3ExpNeeded 3600000;#var Class3GoldNeeded 15300}
  (@class3Level = 14) {#var Class3ExpNeeded 4800000;#var Class3GoldNeeded 18000}
  (@class3Level = 15) {#var Class3ExpNeeded 5400000;#var Class3GoldNeeded 25500}
  (@class3Level = 16) {#var Class3ExpNeeded 6000000;#var Class3GoldNeeded 32400}
  (@class3Level = 17) {#var Class3ExpNeeded 6600000;#var Class3GoldNeeded 39600}
  (@class3Level = 18) {#var Class3ExpNeeded 7200000;#var Class3GoldNeeded 46800}
  (@class3Level = 19) {#var Class3ExpNeeded 8400000;#var Class3GoldNeeded 54000}
  (@class3Level = 20) {#var Class3ExpNeeded 9600000;#var Class3GoldNeeded 64800}
  (@class3Level = 21) {#var Class3ExpNeeded 12000000;#var Class3GoldNeeded 75600}
  (@class3Level = 22) {#var Class3ExpNeeded 18000000;#var Class3GoldNeeded 86400}
  (@class3Level = 23) {#var Class3ExpNeeded 24000000;#var Class3GoldNeeded 97200}
  (@class3Level = 24) {#var Class3ExpNeeded 30000000;#var Class3GoldNeeded 108000}
  (@class3Level = 25) {#var Class3ExpNeeded 36000000;#var Class3GoldNeeded 129600}
  (@class3Level = 26) {#var Class3ExpNeeded 44400000;#var Class3GoldNeeded 151200}
  (@class3Level = 27) {#var Class3ExpNeeded 54000000;#var Class3GoldNeeded 172800}
  (@class3Level = 28) {#var Class3ExpNeeded 63000000;#var Class3GoldNeeded 194400}
  (@class3Level = 29) {#var Class3ExpNeeded 84000000;#var Class3GoldNeeded 216000}
  (@class3Level = 30) {#var Class3ExpNeeded 96000000;#var Class3GoldNeeded 302400}
  (@class3Level = 31) {#var Class3ExpNeeded 108000000;#var Class3GoldNeeded 388800}
  (@class3Level = 32) {#var Class3ExpNeeded 117000000;#var Class3GoldNeeded 475200}
  (@class3Level = 33) {#var Class3ExpNeeded 135000000;#var Class3GoldNeeded 561600}
  (@class3Level = 34) {#var Class3ExpNeeded 152400000;#var Class3GoldNeeded 648000}
  (@class3Level = 35) {#var Class3ExpNeeded 181500000;#var Class3GoldNeeded 907200}
  (@class3Level = 36) {#var Class3ExpNeeded 195000000;#var Class3GoldNeeded 1265000}
  (@class3Level = 37) {#var Class3ExpNeeded 210000000;#var Class3GoldNeeded 1426000}
  (@class3Level = 38) {#var Class3ExpNeeded 255000000;#var Class3GoldNeeded 1685000}
  (@class3Level = 39) {#var Class3ExpNeeded 270000000;#var Class3GoldNeeded 1944000}
  (@class3Level = 40) {#var Class3ExpNeeded Maxed;#var Class3GoldNeeded Maxed}

// Class 4
#switch   (@class4Level = 0) {#var Class4ExpNeeded 40000;#var Class4GoldNeeded 400}
  (@class4Level = 1) {#var Class4ExpNeeded 80000;#var Class4GoldNeeded 600}
  (@class4Level = 2) {#var Class4ExpNeeded 160000;#var Class4GoldNeeded 800}
  (@class4Level = 3) {#var Class4ExpNeeded 320000;#var Class4GoldNeeded 1000}
  (@class4Level = 4) {#var Class4ExpNeeded 450000;#var Class4GoldNeeded 1200}
  (@class4Level = 5) {#var Class4ExpNeeded 700000;#var Class4GoldNeeded 2160}
  (@class4Level = 6) {#var Class4ExpNeeded 1000000;#var Class4GoldNeeded 3120}
  (@class4Level = 7) {#var Class4ExpNeeded 1400000;#var Class4GoldNeeded 4080}
  (@class4Level = 8) {#var Class4ExpNeeded 2800000;#var Class4GoldNeeded 5040}
  (@class4Level = 9) {#var Class4ExpNeeded 3600000;#var Class4GoldNeeded 6000 }
  (@class4Level = 10) {#var Class4ExpNeeded 5500000;#var Class4GoldNeeded 9600}
  (@class4Level = 11) {#var Class4ExpNeeded 8000000;#var Class4GoldNeeded 13200}
  (@class4Level = 12) {#var Class4ExpNeeded 10000000;#var Class4GoldNeeded 16800}
  (@class4Level = 13) {#var Class4ExpNeeded 12000000;#var Class4GoldNeeded 20400}
  (@class4Level = 14) {#var Class4ExpNeeded 16000000;#var Class4GoldNeeded 24000}
  (@class4Level = 15) {#var Class4ExpNeeded 18000000;#var Class4GoldNeeded 33600}
  (@class4Level = 16) {#var Class4ExpNeeded 20000000;#var Class4GoldNeeded 43200}
  (@class4Level = 17) {#var Class4ExpNeeded 22000000;#var Class4GoldNeeded 52800}
  (@class4Level = 18) {#var Class4ExpNeeded 24000000;#var Class4GoldNeeded 62400}
  (@class4Level = 19) {#var Class4ExpNeeded 28000000;#var Class4GoldNeeded 72000}
  (@class4Level = 20) {#var Class4ExpNeeded 32000000;#var Class4GoldNeeded 86400}
  (@class4Level = 21) {#var Class4ExpNeeded 40000000;#var Class4GoldNeeded 100800}
  (@class4Level = 22) {#var Class4ExpNeeded 60000000;#var Class4GoldNeeded 115200}
  (@class4Level = 23) {#var Class4ExpNeeded 80000000;#var Class4GoldNeeded 129600}
  (@class4Level = 24) {#var Class4ExpNeeded 100000000;#var Class4GoldNeeded 144000}
  (@class4Level = 25) {#var Class4ExpNeeded 120000000;#var Class4GoldNeeded 172800}
  (@class4Level = 26) {#var Class4ExpNeeded 148000000;#var Class4GoldNeeded 201600}
  (@class4Level = 27) {#var Class4ExpNeeded 180000000;#var Class4GoldNeeded 230400}
  (@class4Level = 28) {#var Class4ExpNeeded 210000000;#var Class4GoldNeeded 259200}
  (@class4Level = 29) {#var Class4ExpNeeded 280000000;#var Class4GoldNeeded 288000}
  (@class4Level = 30) {#var Class4ExpNeeded 320000000;#var Class4GoldNeeded 403200}
  (@class4Level = 31) {#var Class4ExpNeeded 360000000;#var Class4GoldNeeded 518400}
  (@class4Level = 32) {#var Class4ExpNeeded 390000000;#var Class4GoldNeeded 633600}
  (@class4Level = 33) {#var Class4ExpNeeded 450000000;#var Class4GoldNeeded 748800}
  (@class4Level = 34) {#var Class4ExpNeeded 508000000;#var Class4GoldNeeded 864000}
  (@class4Level = 35) {#var Class4ExpNeeded 605000000;#var Class4GoldNeeded 1200000}
  (@class4Level = 36) {#var Class4ExpNeeded 650000000;#var Class4GoldNeeded 1550000}
  (@class4Level = 37) {#var Class4ExpNeeded 700000000;#var Class4GoldNeeded 1900000}
  (@class4Level = 38) {#var Class4ExpNeeded 850000000;#var Class4GoldNeeded 2247000}
  (@class4Level = 39) {#var Class4ExpNeeded 900000000;#var Class4GoldNeeded 2592000}
  (@class4Level = 40) {#var Class4ExpNeeded Maxed;#var Class4GoldNeeded Maxed}

// Class 5
#switch   (@class5Level = 0) {#var Class5ExpNeeded 80000;#var Class5GoldNeeded 500}
  (@class5Level = 1) {#var Class5ExpNeeded 160000;#var Class5GoldNeeded 750}
  (@class5Level = 2) {#var Class5ExpNeeded 320000;#var Class5GoldNeeded 1000}
  (@class5Level = 3) {#var Class5ExpNeeded 640000;#var Class5GoldNeeded 1250}
  (@class5Level = 4) {#var Class5ExpNeeded 900000;#var Class5GoldNeeded 1500}
  (@class5Level = 5) {#var Class5ExpNeeded 1400000;#var Class5GoldNeeded 2700}
  (@class5Level = 6) {#var Class5ExpNeeded 2000000;#var Class5GoldNeeded 3900}
  (@class5Level = 7) {#var Class5ExpNeeded 2800000;#var Class5GoldNeeded 5100}
  (@class5Level = 8) {#var Class5ExpNeeded 5600000;#var Class5GoldNeeded 6300}
  (@class5Level = 9) {#var Class5ExpNeeded 7200000;#var Class5GoldNeeded 7500 }
  (@class5Level = 10) {#var Class5ExpNeeded 11000000;#var Class5GoldNeeded 12000}
  (@class5Level = 11) {#var Class5ExpNeeded 16000000;#var Class5GoldNeeded 16500}
  (@class5Level = 12) {#var Class5ExpNeeded 20000000;#var Class5GoldNeeded 21000}
  (@class5Level = 13) {#var Class5ExpNeeded 24000000;#var Class5GoldNeeded 25500}
  (@class5Level = 14) {#var Class5ExpNeeded 32000000;#var Class5GoldNeeded 30000}
  (@class5Level = 15) {#var Class5ExpNeeded 36000000;#var Class5GoldNeeded 42000}
  (@class5Level = 16) {#var Class5ExpNeeded 40000000;#var Class5GoldNeeded 54000}
  (@class5Level = 17) {#var Class5ExpNeeded 44000000;#var Class5GoldNeeded 66000}
  (@class5Level = 18) {#var Class5ExpNeeded 48000000;#var Class5GoldNeeded 78000}
  (@class5Level = 19) {#var Class5ExpNeeded 56000000;#var Class5GoldNeeded 90000}
  (@class5Level = 20) {#var Class5ExpNeeded 64000000;#var Class5GoldNeeded 108000}
  (@class5Level = 21) {#var Class5ExpNeeded 80000000;#var Class5GoldNeeded 126000}
  (@class5Level = 22) {#var Class5ExpNeeded 120000000;#var Class5GoldNeeded 144000}
  (@class5Level = 23) {#var Class5ExpNeeded 160000000;#var Class5GoldNeeded 162000}
  (@class5Level = 24) {#var Class5ExpNeeded 200000000;#var Class5GoldNeeded 180000}
  (@class5Level = 25) {#var Class5ExpNeeded 240000000;#var Class5GoldNeeded 216000}
  (@class5Level = 26) {#var Class5ExpNeeded 296000000;#var Class5GoldNeeded 252000}
  (@class5Level = 27) {#var Class5ExpNeeded 360000000;#var Class5GoldNeeded 288000}
  (@class5Level = 28) {#var Class5ExpNeeded 420000000;#var Class5GoldNeeded 324000}
  (@class5Level = 29) {#var Class5ExpNeeded 560000000;#var Class5GoldNeeded 360000}
  (@class5Level = 30) {#var Class5ExpNeeded 640000000;#var Class5GoldNeeded 504000}
  (@class5Level = 31) {#var Class5ExpNeeded 720000000;#var Class5GoldNeeded 648000}
  (@class5Level = 32) {#var Class5ExpNeeded 780000000;#var Class5GoldNeeded 792000}
  (@class5Level = 33) {#var Class5ExpNeeded 900000000;#var Class5GoldNeeded 936000}
  (@class5Level = 34) {#var Class5ExpNeeded 1016000000;#var Class5GoldNeeded 1080000}
  (@class5Level = 35) {#var Class5ExpNeeded 1210000000;#var Class5GoldNeeded 1512000}
  (@class5Level = 36) {#var Class5ExpNeeded 1300000000;#var Class5GoldNeeded 1944000}
  (@class5Level = 37) {#var Class5ExpNeeded 1400000000;#var Class5GoldNeeded 2376000}
  (@class5Level = 38) {#var Class5ExpNeeded 1700000000;#var Class5GoldNeeded 2808000}
  (@class5Level = 39) {#var Class5ExpNeeded 1800000000;#var Class5GoldNeeded 3240000}
  (@class5Level = 40) {#var Class5ExpNeeded Maxed;#var Class5GoldNeeded Maxed}

// Class 6
#switch (@class6Level = 0) {#var Class6ExpNeeded 120000;#var Class6GoldNeeded 1200}
  (@class6Level = 1) {#var Class6ExpNeeded 240000;#var Class6GoldNeeded 1800}
  (@class6Level = 2) {#var Class6ExpNeeded 480000;#var Class6GoldNeeded 2400}
  (@class6Level = 3) {#var Class6ExpNeeded 960000;#var Class6GoldNeeded 3000}
  (@class6Level = 4) {#var Class6ExpNeeded 1350000;#var Class6GoldNeeded 3600}
  (@class6Level = 5) {#var Class6ExpNeeded 2100000;#var Class6GoldNeeded 6480}
  (@class6Level = 6) {#var Class6ExpNeeded 3000000;#var Class6GoldNeeded 9360}
  (@class6Level = 7) {#var Class6ExpNeeded 4200000;#var Class6GoldNeeded 12240}
  (@class6Level = 8) {#var Class6ExpNeeded 8400000;#var Class6GoldNeeded 15120}
  (@class6Level = 9) {#var Class6ExpNeeded 10800000;#var Class6GoldNeeded 18000 }
  (@class6Level = 10) {#var Class6ExpNeeded 16500000;#var Class6GoldNeeded 28800}
  (@class6Level = 11) {#var Class6ExpNeeded 24000000;#var Class6GoldNeeded 39600}
  (@class6Level = 12) {#var Class6ExpNeeded 30000000;#var Class6GoldNeeded 50400}
  (@class6Level = 13) {#var Class6ExpNeeded 36000000;#var Class6GoldNeeded 61200}
  (@class6Level = 14) {#var Class6ExpNeeded 48000000;#var Class6GoldNeeded 72000}
  (@class6Level = 15) {#var Class6ExpNeeded 54000000;#var Class6GoldNeeded 100800}
  (@class6Level = 16) {#var Class6ExpNeeded 60000000;#var Class6GoldNeeded 129600}
  (@class6Level = 17) {#var Class6ExpNeeded 66000000;#var Class6GoldNeeded 158400}
  (@class6Level = 18) {#var Class6ExpNeeded 72000000;#var Class6GoldNeeded 187200}
  (@class6Level = 19) {#var Class6ExpNeeded 84000000;#var Class6GoldNeeded 216000}
  (@class6Level = 20) {#var Class6ExpNeeded 96000000;#var Class6GoldNeeded 259200}
  (@class6Level = 21) {#var Class6ExpNeeded 120000000;#var Class6GoldNeeded 302400}
  (@class6Level = 22) {#var Class6ExpNeeded 180000000;#var Class6GoldNeeded 345600}
  (@class6Level = 23) {#var Class6ExpNeeded 240000000;#var Class6GoldNeeded 388800}
  (@class6Level = 24) {#var Class6ExpNeeded 300000000;#var Class6GoldNeeded 432000}
  (@class6Level = 25) {#var Class6ExpNeeded 360000000;#var Class6GoldNeeded 518400}
  (@class6Level = 26) {#var Class6ExpNeeded 444000000;#var Class6GoldNeeded 604800}
  (@class6Level = 27) {#var Class6ExpNeeded 540000000;#var Class6GoldNeeded 691200}
  (@class6Level = 28) {#var Class6ExpNeeded 630000000;#var Class6GoldNeeded 777600}
  (@class6Level = 29) {#var Class6ExpNeeded 840000000;#var Class6GoldNeeded 864000}
  (@class6Level = 30) {#var Class6ExpNeeded 960000000;#var Class6GoldNeeded 1209600}
  (@class6Level = 31) {#var Class6ExpNeeded 1080000000;#var Class6GoldNeeded 1555200}
  (@class6Level = 32) {#var Class6ExpNeeded 1170000000;#var Class6GoldNeeded 1900800}
  (@class6Level = 33) {#var Class6ExpNeeded 1350000000;#var Class6GoldNeeded 2246400}
  (@class6Level = 34) {#var Class6ExpNeeded 1524000000;#var Class6GoldNeeded 2592000}
  (@class6Level = 35) {#var Class6ExpNeeded 1815000000;#var Class6GoldNeeded 3628800}
  (@class6Level = 36) {#var Class6ExpNeeded 1950000000;#var Class6GoldNeeded 4665600}
  (@class6Level = 37) {#var Class6ExpNeeded 2100000000;#var Class6GoldNeeded 5702400}
  (@class6Level = 38) {#var Class6ExpNeeded 2550000000;#var Class6GoldNeeded 6739200}
  (@class6Level = 39) {#var Class6ExpNeeded 2700000000;#var Class6GoldNeeded 7776000}
  (@class6Level = 40) {#var Class6ExpNeeded Maxed;#var Class6GoldNeeded Maxed}

// Class 7
#switch (@class7Level = 0) {#var Class7ExpNeeded 240000;#var Class7GoldNeeded 1400}
  (@class7Level = 1) {#var Class7ExpNeeded 480000;#var Class7GoldNeeded 2100}
  (@class7Level = 2) {#var Class7ExpNeeded 960000;#var Class7GoldNeeded 2800}
  (@class7Level = 3) {#var Class7ExpNeeded 1920000;#var Class7GoldNeeded 3500}
  (@class7Level = 4) {#var Class7ExpNeeded 2700000;#var Class7GoldNeeded 4200}
  (@class7Level = 5) {#var Class7ExpNeeded 4200000;#var Class7GoldNeeded 7560}
  (@class7Level = 6) {#var Class7ExpNeeded 6000000;#var Class7GoldNeeded 10920}
  (@class7Level = 7) {#var Class7ExpNeeded 8400000;#var Class7GoldNeeded 14280}
  (@class7Level = 8) {#var Class7ExpNeeded 16800000;#var Class7GoldNeeded 17640}
  (@class7Level = 9) {#var Class7ExpNeeded 21600000;#var Class7GoldNeeded 21000 }
  (@class7Level = 10) {#var Class7ExpNeeded 33000000;#var Class7GoldNeeded 33600}
  (@class7Level = 11) {#var Class7ExpNeeded 48000000;#var Class7GoldNeeded 46200}
  (@class7Level = 12) {#var Class7ExpNeeded 60000000;#var Class7GoldNeeded 58800}
  (@class7Level = 13) {#var Class7ExpNeeded 72000000;#var Class7GoldNeeded 71400}
  (@class7Level = 14) {#var Class7ExpNeeded 96000000;#var Class7GoldNeeded 84000}
  (@class7Level = 15) {#var Class7ExpNeeded 108000000;#var Class7GoldNeeded 117600}
  (@class7Level = 16) {#var Class7ExpNeeded 120000000;#var Class7GoldNeeded 151200}
  (@class7Level = 17) {#var Class7ExpNeeded 132000000;#var Class7GoldNeeded 184800}
  (@class7Level = 18) {#var Class7ExpNeeded 144000000;#var Class7GoldNeeded 218400}
  (@class7Level = 19) {#var Class7ExpNeeded 168000000;#var Class7GoldNeeded 252000}
  (@class7Level = 20) {#var Class7ExpNeeded 192000000;#var Class7GoldNeeded 302400}
  (@class7Level = 21) {#var Class7ExpNeeded 240000000;#var Class7GoldNeeded 352800}
  (@class7Level = 22) {#var Class7ExpNeeded 360000000;#var Class7GoldNeeded 403200}
  (@class7Level = 23) {#var Class7ExpNeeded 480000000;#var Class7GoldNeeded 453600}
  (@class7Level = 24) {#var Class7ExpNeeded 600000000;#var Class7GoldNeeded 504000}
  (@class7Level = 25) {#var Class7ExpNeeded 720000000;#var Class7GoldNeeded 604800}
  (@class7Level = 26) {#var Class7ExpNeeded 888000000;#var Class7GoldNeeded 705600}
  (@class7Level = 27) {#var Class7ExpNeeded 1080000000;#var Class7GoldNeeded 806400}
  (@class7Level = 28) {#var Class7ExpNeeded 1260000000;#var Class7GoldNeeded 907200}
  (@class7Level = 29) {#var Class7ExpNeeded 1680000000;#var Class7GoldNeeded 1008000}
  (@class7Level = 30) {#var Class7ExpNeeded 1920000000;#var Class7GoldNeeded 1411200}
  (@class7Level = 31) {#var Class7ExpNeeded 2160000000;#var Class7GoldNeeded 1814400}
  (@class7Level = 32) {#var Class7ExpNeeded 2340000000;#var Class7GoldNeeded 2217600}
  (@class7Level = 33) {#var Class7ExpNeeded 2700000000;#var Class7GoldNeeded 2620800}
  (@class7Level = 34) {#var Class7ExpNeeded 3048000000;#var Class7GoldNeeded 3024000}
  (@class7Level = 35) {#var Class7ExpNeeded 3630000000;#var Class7GoldNeeded 4233600}
  (@class7Level = 36) {#var Class7ExpNeeded 3900000000;#var Class7GoldNeeded 5443200}
  (@class7Level = 37) {#var Class7ExpNeeded 4200000000;#var Class7GoldNeeded 6652800}
  (@class7Level = 38) {#var Class7ExpNeeded 5100000000;#var Class7GoldNeeded 7862400}
  (@class7Level = 39) {#var Class7ExpNeeded 5400000000;#var Class7GoldNeeded 9072000}
  (@class7Level = 40) {#var Class7ExpNeeded Maxed;#var Class7GoldNeeded Maxed}

// Class 8
#switch (@class8Level = 0) {#var Class8ExpNeeded 320000;#var Class8GoldNeeded 1600}
  (@class8Level = 1) {#var Class8ExpNeeded 640000;#var Class8GoldNeeded 2400}
  (@class8Level = 2) {#var Class8ExpNeeded 1280000;#var Class8GoldNeeded 3200}
  (@class8Level = 3) {#var Class8ExpNeeded 2560000;#var Class8GoldNeeded 4000}
  (@class8Level = 4) {#var Class8ExpNeeded 3600000;#var Class8GoldNeeded 4800}
  (@class8Level = 5) {#var Class8ExpNeeded 5600000;#var Class8GoldNeeded 8640}
  (@class8Level = 6) {#var Class8ExpNeeded 8000000;#var Class8GoldNeeded 12480}
  (@class8Level = 7) {#var Class8ExpNeeded 11200000;#var Class8GoldNeeded 16320}
  (@class8Level = 8) {#var Class8ExpNeeded 22400000;#var Class8GoldNeeded 20160}
  (@class8Level = 9) {#var Class8ExpNeeded 28800000;#var Class8GoldNeeded 24000}
  (@class8Level = 10) {#var Class8ExpNeeded 44000000;#var Class8GoldNeeded 38400}
  (@class8Level = 11) {#var Class8ExpNeeded 64000000;#var Class8GoldNeeded 52800}
  (@class8Level = 12) {#var Class8ExpNeeded 80000000;#var Class8GoldNeeded 67200}
  (@class8Level = 13) {#var Class8ExpNeeded 96000000;#var Class8GoldNeeded 81600}
  (@class8Level = 14) {#var Class8ExpNeeded 128000000;#var Class8GoldNeeded 96000}
  (@class8Level = 15) {#var Class8ExpNeeded 144000000;#var Class8GoldNeeded 134400}
  (@class8Level = 16) {#var Class8ExpNeeded 160000000;#var Class8GoldNeeded 172800}
  (@class8Level = 17) {#var Class8ExpNeeded 176000000;#var Class8GoldNeeded 211200}
  (@class8Level = 18) {#var Class8ExpNeeded 192000000;#var Class8GoldNeeded 249600}
  (@class8Level = 19) {#var Class8ExpNeeded 224000000;#var Class8GoldNeeded 288000}
  (@class8Level = 20) {#var Class8ExpNeeded 256000000;#var Class8GoldNeeded 345600}
  (@class8Level = 21) {#var Class8ExpNeeded 320000000;#var Class8GoldNeeded 403200}
  (@class8Level = 22) {#var Class8ExpNeeded 480000000;#var Class8GoldNeeded 460800}
  (@class8Level = 23) {#var Class8ExpNeeded 640000000;#var Class8GoldNeeded 518400}
  (@class8Level = 24) {#var Class8ExpNeeded 800000000;#var Class8GoldNeeded 576000}
  (@class8Level = 25) {#var Class8ExpNeeded 960000000;#var Class8GoldNeeded 691200}
  (@class8Level = 26) {#var Class8ExpNeeded 1184000000;#var Class8GoldNeeded 806400}
  (@class8Level = 27) {#var Class8ExpNeeded 1440000000;#var Class8GoldNeeded 921600}
  (@class8Level = 28) {#var Class8ExpNeeded 1680000000;#var Class8GoldNeeded 1036800}
  (@class8Level = 29) {#var Class8ExpNeeded 2240000000;#var Class8GoldNeeded 1152000}
  (@class8Level = 30) {#var Class8ExpNeeded 2560000000;#var Class8GoldNeeded 1612800}
  (@class8Level = 31) {#var Class8ExpNeeded 2880000000;#var Class8GoldNeeded 2073600}
  (@class8Level = 32) {#var Class8ExpNeeded 3120000000;#var Class8GoldNeeded 2534400}
  (@class8Level = 33) {#var Class8ExpNeeded 3600000000;#var Class8GoldNeeded 2995200}
  (@class8Level = 34) {#var Class8ExpNeeded 4064000000;#var Class8GoldNeeded 3456000}
  (@class8Level = 35) {#var Class8ExpNeeded 4840000000;#var Class8GoldNeeded 4838400}
  (@class8Level = 36) {#var Class8ExpNeeded 5200000000;#var Class8GoldNeeded 6220800}
  (@class8Level = 37) {#var Class8ExpNeeded 5600000000;#var Class8GoldNeeded 7603200}
  (@class8Level = 38) {#var Class8ExpNeeded 6800000000;#var Class8GoldNeeded 8985600}
  (@class8Level = 39) {#var Class8ExpNeeded 7200000000;#var Class8GoldNeeded 10368000}
  (@class8Level = 40) {#var Class8ExpNeeded Maxed;#var Class8GoldNeeded Maxed}

// Avatar Class 
#switch (@AvatarLevel = 0) {#var AvatarExpNeeded 110000000;#var AvatarGoldNeeded 1000000}
  (@AvatarLevel = 1) {#var AvatarExpNeeded 140000000;#var AvatarGoldNeeded 1075000}
  (@AvatarLevel = 2) {#var AvatarExpNeeded 180000000;#var AvatarGoldNeeded 1150000}
  (@AvatarLevel = 3) {#var AvatarExpNeeded 220000000;#var AvatarGoldNeeded 1225000}
  (@AvatarLevel = 4) {#var AvatarExpNeeded 260000000;#var AvatarGoldNeeded 1300000}
  (@AvatarLevel = 5) {#var AvatarExpNeeded 300000000;#var AvatarGoldNeeded 1375000}
  (@AvatarLevel = 6) {#var AvatarExpNeeded 340000000;#var AvatarGoldNeeded 1450000}
  (@AvatarLevel = 7) {#var AvatarExpNeeded 380000000;#var AvatarGoldNeeded 1525000}
  (@AvatarLevel = 8) {#var AvatarExpNeeded 420000000;#var AvatarGoldNeeded 1600000 }
  (@AvatarLevel = 9) {#var AvatarExpNeeded 460000000;#var AvatarGoldNeeded 1675000}
  (@AvatarLevel = 10) {#var AvatarExpNeeded 500000000;#var AvatarGoldNeeded 1750000}
  (@AvatarLevel = 11) {#var AvatarExpNeeded 550000000;#var AvatarGoldNeeded 1825000}
  (@AvatarLevel = 12) {#var AvatarExpNeeded 600000000;#var AvatarGoldNeeded 1900000}
  (@AvatarLevel = 13) {#var AvatarExpNeeded 650000000;#var AvatarGoldNeeded 1975000}
  (@AvatarLevel = 14) {#var AvatarExpNeeded 700000000;#var AvatarGoldNeeded 2050000}
  (@AvatarLevel = 15) {#var AvatarExpNeeded 750000000;#var AvatarGoldNeeded 2125000}
  (@AvatarLevel = 16) {#var AvatarExpNeeded 800000000;#var AvatarGoldNeeded 2200000}
  (@AvatarLevel = 17) {#var AvatarExpNeeded 850000000;#var AvatarGoldNeeded 2275000}
  (@AvatarLevel = 18) {#var AvatarExpNeeded 900000000;#var AvatarGoldNeeded 2350000}
  (@AvatarLevel = 19) {#var AvatarExpNeeded 950000000;#var AvatarGoldNeeded 2425000}
  (@AvatarLevel = 20) {#var AvatarExpNeeded 1050000000;#var AvatarGoldNeeded 2500000}
  (@AvatarLevel = 21) {#var AvatarExpNeeded 1100000000;#var AvatarGoldNeeded 2575000}
  (@AvatarLevel = 22) {#var AvatarExpNeeded 1200000000;#var AvatarGoldNeeded 2650000}
  (@AvatarLevel = 23) {#var AvatarExpNeeded 1300000000;#var AvatarGoldNeeded 2725000}
  (@AvatarLevel = 24) {#var AvatarExpNeeded 1400000000;#var AvatarGoldNeeded 2875000}
  (@AvatarLevel = 25) {#var AvatarExpNeeded 1500000000;#var AvatarGoldNeeded 2875000}
  (@AvatarLevel = 26) {#var AvatarExpNeeded 1600000000;#var AvatarGoldNeeded 2950000}
  (@AvatarLevel = 27) {#var AvatarExpNeeded 1700000000;#var AvatarGoldNeeded 3025000}
  (@AvatarLevel = 28) {#var AvatarExpNeeded 1800000000;#var AvatarGoldNeeded 3100000}
  (@AvatarLevel = 29) {#var AvatarExpNeeded 1900000000;#var AvatarGoldNeeded 3175000}
  (@AvatarLevel = 30) {#var AvatarExpNeeded 2000000000;#var AvatarGoldNeeded 3250000}
  (@AvatarLevel = 31) {#var AvatarExpNeeded 2100000000;#var AvatarGoldNeeded 3325000}
  (@AvatarLevel = 32) {#var AvatarExpNeeded 2100000000;#var AvatarGoldNeeded 3400000}
  (@AvatarLevel = 33) {#var AvatarExpNeeded 2100000000;#var AvatarGoldNeeded 3475000}
  (@AvatarLevel = 34) {#var AvatarExpNeeded 2100000000;#var AvatarGoldNeeded 3550000}
  (@AvatarLevel = 35) {#var AvatarExpNeeded 2100000000;#var AvatarGoldNeeded 3625000}
  (@AvatarLevel = 36) {#var AvatarExpNeeded 2100000000;#var AvatarGoldNeeded 3700000}
  (@AvatarLevel = 37) {#var AvatarExpNeeded 2100000000;#var AvatarGoldNeeded 3775000}
  (@AvatarLevel = 38) {#var AvatarExpNeeded 2100000000;#var AvatarGoldNeeded 3850000}
  (@AvatarLevel = 39) {#var AvatarExpNeeded 2100000000;#var AvatarGoldNeeded 3925000}
  (@AvatarLevel = 40) {#var AvatarExpNeeded Maxed;#var AvatarGoldNeeded Maxed}
```

</div>

<div class="post" data-post-id="31153" data-author="Gladavar" data-date="2010-05-13T04:51:47+00:00" data-subject="">

Now for the actual gauges.  Copy the following code into a text file and save as a .xml  then use the Import XML option in CMUD's package editor and import that file into your session. Once imported and saved set @MyChar to the name of your character.  This should fire an inclueded trigger when you level that will send score to the mud and update everything with the new values.

```
<class name="Levels" id="71">
  <trigger priority="720" id="72">
    <pattern>^Your levels:%s(%w):%s(%d)%s(%w):%s(%d)%s(%w):%s(%d)%s(%w):%s(%d)%s(%w):%s(%d)%s(%w):%s(%d)%s(%w):%s(%d)%s(%w):%s(%d)%s</pattern>
    <value>#var Class1 %1
#var Class1Level %2
#var Class2 %3
#var Class2Level %4
#var Class3 %5
#var Class3Level %6
#var Class4 %7
#var Class4Level %8
#var Class5 %9
#var Class5Level %10
#var Class6 %11
#var Class6Level %12
#var Class7 %13
#var Class7Level %14
#var Class8 %15
#var Class8Level %16
</value>
  </trigger>
  <class name="Class 2" id="151">
    <button type="Gauge" autosize="false" width="100" height="25" autopos="false" left="104" top="2" color="lime" gaugelowcol="red" gaugebackcol="red" priority="1110" id="111">
      <caption>@class2 @Class2Level</caption>
      <value><![CDATA[#cr
#show %ansi(bright,cyan)Total Level Cost: %ansi(bright,red)%format("&1.0n",@Class2ExpNeeded)
#show %ansi(bright,cyan)Needed EXP: %if(%eval(@Class2ExpNeeded - @EXP_Current) <= 0,%ansi(bright,green)%format("&1.0n",%eval(@Class2ExpNeeded - @EXP_Current)),%ansi(bright,red)%format("&1.0n",%eval(@Class2ExpNeeded - @EXP_Current)))
#show %ansi(bright,cyan)Gold Requred:%ansi(bright,yellow)@Class2GoldNeeded 
#cr]]></value>
      <expr>@EXP_Current/1000</expr>
      <gaugemax>@Class2ExpNeeded/1000</gaugemax>
      <gaugelow>0</gaugelow>
    </button>
    <var name="Class2" id="170"/>
    <var name="Class2ExpNeeded" id="171">4000</var>
    <var name="Class2GoldNeeded" id="172">200</var>
    <var name="Class2Level" id="173">0</var>
  </class>
  <class name="Class 1" id="152">
    <button type="Gauge" variable="@Exp_current" autosize="false" width="100" height="25" autopos="false" left="2" color="lime" gaugelowcol="red" gaugebackcol="red" priority="1060" id="106">
      <caption>@class1 @Class1Level</caption>
      <value><![CDATA[#cr
#show %ansi(bright,cyan)Total Level Cost: %ansi(bright,red)%format("&1.0n",@Class1ExpNeeded)
#show %ansi(bright,cyan)Needed EXP: %if(%eval(@Class1ExpNeeded - @EXP_Current) <= 0,%ansi(bright,green)%format("&1.0n",%eval(@Class1ExpNeeded - @EXP_Current)),%ansi(bright,red)%format("&1.0n",%eval(@Class1ExpNeeded - @EXP_Current)))
#show %ansi(bright,cyan)Gold Requred:%ansi(bright,yellow)@Class1GoldNeeded 
#cr]]></value>
      <expr>@EXP_Current/1000</expr>
      <gaugemax>@Class1ExpNeeded/1000</gaugemax>
      <gaugelow>0</gaugelow>
    </button>
    <var name="Class1" id="166"/>
    <var name="Class1ExpNeeded" type="Integer" id="167">800000</var>
    <var name="Class1GoldNeeded" usedef="true" id="168">
      <value>21600</value>
      <default>k</default>
    </var>
    <var name="Class1Level" id="169">0</var>
  </class>
  <class name="Class 3" id="153">
    <button type="Gauge" autosize="false" width="100" height="25" autopos="false" left="206" top="2" color="lime" gaugelowcol="red" gaugebackcol="red" priority="1190" id="119">
      <caption>@class3 @Class3Level</caption>
      <value><![CDATA[#cr
#show %ansi(bright,cyan)Total Level Cost: %ansi(bright,red)%format("&1.0n",@Class3ExpNeeded)
#show %ansi(bright,cyan)Needed EXP: %if(%eval(@Class3ExpNeeded - @EXP_Current) <= 0,%ansi(bright,green)%format("&1.0n",%eval(@Class3ExpNeeded - @EXP_Current)),%ansi(bright,red)%format("&1.0n",%eval(@Class3ExpNeeded - @EXP_Current)))
#show %ansi(bright,cyan)Gold Requred:%ansi(bright,yellow)@Class3GoldNeeded 
#cr]]></value>
      <expr>@EXP_Current/1000</expr>
      <gaugemax>@Class3ExpNeeded/1000</gaugemax>
      <gaugelow>0</gaugelow>
    </button>
    <var name="Class3" id="174"/>
    <var name="Class3ExpNeeded" id="175">12000</var>
    <var name="Class3GoldNeeded" id="176">300</var>
    <var name="Class3Level" id="177">0</var>
  </class>
  <class name="Class 4" id="154">
    <button type="Gauge" autosize="false" width="100" height="25" autopos="false" left="308" top="2" color="lime" gaugelowcol="red" gaugebackcol="red" priority="1180" id="118">
      <caption>@class4 @Class4Level</caption>
      <value><![CDATA[#cr
#show %ansi(bright,cyan)Total Level Cost: %ansi(bright,red)%format("&1.0n",@Class4ExpNeeded)
#show %ansi(bright,cyan)Needed EXP: %if(%eval(@Class4ExpNeeded - @EXP_Current) <= 0,%ansi(bright,green)%format("&1.0n",%eval(@Class4ExpNeeded - @EXP_Current)),%ansi(bright,red)%format("&1.0n",%eval(@Class4ExpNeeded - @EXP_Current)))
#show %ansi(bright,cyan)Gold Requred:%ansi(bright,yellow)@Class4GoldNeeded 
#cr]]></value>
      <expr>@EXP_Current/1000</expr>
      <gaugemax>@Class4ExpNeeded/1000</gaugemax>
      <gaugelow>0</gaugelow>
    </button>
    <var name="Class4" id="178"/>
    <var name="Class4ExpNeeded" id="179">40000</var>
    <var name="Class4GoldNeeded" id="180">400</var>
    <var name="Class4Level" id="181">0</var>
  </class>
  <class name="Class 5" id="155">
    <button type="Gauge" autosize="false" width="100" height="25" autopos="false" left="410" top="2" color="lime" gaugelowcol="red" gaugebackcol="red" priority="1170" id="117">
      <caption>@class5 @Class5Level</caption>
      <value><![CDATA[#cr
#show %ansi(bright,cyan)Total Level Cost: %ansi(bright,red)%format("&1.0n",@Class5ExpNeeded)
#show %ansi(bright,cyan)Needed EXP: %if(%eval(@Class5ExpNeeded - @EXP_Current) <= 0,%ansi(bright,green)%format("&1.0n",%eval(@Class5ExpNeeded - @EXP_Current)),%ansi(bright,red)%format("&1.0n",%eval(@Class5ExpNeeded - @EXP_Current)))
#show %ansi(bright,cyan)Gold Requred:%ansi(bright,yellow)@Class5GoldNeeded 
#cr]]></value>
      <expr>@EXP_Current/1000</expr>
      <gaugemax>@Class5ExpNeeded/1000</gaugemax>
      <gaugelow>0</gaugelow>
    </button>
    <var name="Class5" id="182"/>
    <var name="Class5ExpNeeded" type="Integer" id="183">80000</var>
    <var name="Class5GoldNeeded" id="184">500</var>
    <var name="Class5Level" id="185">0</var>
  </class>
  <class name="Class 6" id="156">
    <button type="Gauge" autosize="false" width="100" height="25" autopos="false" left="512" top="2" color="lime" gaugelowcol="red" gaugebackcol="red" priority="1160" id="116">
      <caption>@class6 @Class6Level</caption>
      <value><![CDATA[#cr
#show %ansi(bright,cyan)Total Level Cost: %ansi(bright,red)%format("&1.0n",@Class6ExpNeeded)
#show %ansi(bright,cyan)Needed EXP: %if(%eval(@Class6ExpNeeded - @EXP_Current) <= 0,%ansi(bright,green)%format("&1.0n",%eval(@Class6ExpNeeded - @EXP_Current)),%ansi(bright,red)%format("&1.0n",%eval(@Class6ExpNeeded - @EXP_Current)))
#show %ansi(bright,cyan)Gold Requred:%ansi(bright,yellow)@Class6GoldNeeded 
#cr]]></value>
      <expr>@EXP_Current/1000</expr>
      <gaugemax>@Class6ExpNeeded/1000</gaugemax>
      <gaugelow>0</gaugelow>
    </button>
    <var name="Class6" id="186"/>
    <var name="Class6ExpNeeded" id="187">120000</var>
    <var name="Class6GoldNeeded" id="188">1200</var>
    <var name="Class6Level" id="189">0</var>
  </class>
  <class name="Class 7" id="158">
    <button type="Gauge" autosize="false" width="100" height="25" autopos="false" left="614" top="2" color="lime" gaugelowcol="red" gaugebackcol="red" priority="1150" id="115">
      <caption>@class7 @Class7Level</caption>
      <value><![CDATA[#cr
#show %ansi(bright,cyan)Total Level Cost: %ansi(bright,red)%format("&1.0n",@Class7ExpNeeded)
#show %ansi(bright,cyan)Needed EXP: %if(%eval(@Class7ExpNeeded - @EXP_Current) <= 0,%ansi(bright,green)%format("&1.0n",%eval(@Class7ExpNeeded - @EXP_Current)),%ansi(bright,red)%format("&1.0n",%eval(@Class7ExpNeeded - @EXP_Current)))
#show %ansi(bright,cyan)Gold Requred:%ansi(bright,yellow)@Class7GoldNeeded 
#cr]]></value>
      <expr>@EXP_Current/1000</expr>
      <gaugemax>@Class7ExpNeeded/1000</gaugemax>
      <gaugelow>0</gaugelow>
    </button>
    <var name="Class7" id="190"/>
    <var name="Class7ExpNeeded" id="191">240000</var>
    <var name="Class7GoldNeeded" id="192">1400</var>
    <var name="Class7Level" id="193">0</var>
  </class>
  <class name="Class 8" id="159">
    <button type="Gauge" autosize="false" width="100" height="25" autopos="false" left="716" top="2" color="lime" gaugelowcol="red" gaugebackcol="red" priority="1140" id="114">
      <caption>@class8 @Class8Level</caption>
      <value><![CDATA[#cr
#show %ansi(bright,cyan)Total Level Cost: %ansi(bright,red)%format("&1.0n",@Class8ExpNeeded)
#show %ansi(bright,cyan)Needed EXP: %if(%eval(@Class8ExpNeeded - @EXP_Current) <= 0,%ansi(bright,green)%format("&1.0n",%eval(@Class8ExpNeeded - @EXP_Current)),%ansi(bright,red)%format("&1.0n",%eval(@Class8ExpNeeded - @EXP_Current)))
#show %ansi(bright,cyan)Gold Requred:%ansi(bright,yellow)@Class8GoldNeeded 
#cr]]></value>
      <expr>@EXP_Current/1000</expr>
      <gaugemax>@Class8ExpNeeded/1000</gaugemax>
      <gaugelow>0</gaugelow>
    </button>
    <var name="Class8" id="194"/>
    <var name="Class8ExpNeeded" type="Integer" id="195">320000</var>
    <var name="Class8GoldNeeded" id="196">1600</var>
    <var name="Class8Level" id="197">0</var>
  </class>
  <class name="Class Avatar" id="160">
    <button type="Gauge" variable="@Exp_current" autosize="false" width="100" height="25" autopos="false" left="818" color="lime" gaugelowcol="red" gaugebackcol="red" priority="1130" id="150">
      <caption>Avatar: @AvatarLevel</caption>
      <value><![CDATA[#cr
#show %ansi(bright,cyan)Total Level Cost: %ansi(bright,red)%format("&1.0n",@AvatarExpNeeded)
#show %ansi(bright,cyan)Needed EXP: %if(%eval(@AvatarExpNeeded - @EXP_Current) <= 0,%ansi(bright,green)%format("&1.0n",%eval(@AvatarExpNeeded - @EXP_Current)),%ansi(bright,red)%format("&1.0n",%eval(@AvatarExpNeeded - @EXP_Current)))
#show %ansi(bright,cyan)Gold Requred:%ansi(bright,yellow)@AvatarGoldNeeded 
#cr]]></value>
      <expr>@EXP_Current/1000</expr>
      <gaugemax>@AvatarExpNeeded/1000</gaugemax>
      <gaugelow>0</gaugelow>
    </button>
    <var name="Avatar" id="162"/>
    <var name="AvatarExpNeeded" id="163">110000000</var>
    <var name="AvatarGoldNeeded" id="164">1000000</var>
    <var name="AvatarLevel" id="165">0</var>
  </class>
  <trigger priority="2150" id="215">
    <pattern>^(*) says '(%w) is ready for the next level'</pattern>
    <value>#if (%2 =~ @MyChar) {#send score}</value>
  </trigger>
  <var name="MyChar" id="216">kodiak</var>
</class>
```

</div>

<div class="post" data-post-id="31154" data-author="Gladavar" data-date="2010-05-13T05:03:18+00:00" data-subject="">

One additional feature I forgot to mention.  If you click any of the gauges it will show you the the total cost of that level on one line.  The next line will display the amount of exp you actually need to complete that level in red and if you have enough to level the amount will turn green and be a negative number.  And on a third and final line the amount of gold required will be displayed all colored to stand out.

This has only been tested in game up to 3x20 but I ran some values off line and everything appeared to work fine for the latter classes/levels.

Hope you like it and if you have any questions feel free to ask.

P.S.

This is set up for avatar too but since i'm not one I have no way to tell how the Avatar values will need to be captured.  Hopefully it will just be a simple addition to the main class values trigger.  If anyone could post a sample score for an avatar character I would greatly appreciate it.

</div>

<div class="post" data-post-id="31155" data-author="Gladavar" data-date="2010-05-13T12:28:58+00:00" data-subject="">

Here is a screen shot of the tracker's layout.

<LINK_TEXT text="
http://i282.photobucket.com/albums/kk2 ... acker.png
">
http://i282.photobucket.com/albums/kk270/Fizgar/SSforxptracker.png
</LINK_TEXT>

</div>

<div class="post" data-post-id="32714" data-author="Gladavar" data-date="2011-07-05T04:07:27+00:00" data-subject="Re: CMUD: EXP Tracker">

Nothing new to see in any of the posts I edited.  Somewhere along the lines the code tags got funky and made the reading ugly, so I edited all the posts to fix the tags.

</div>

<div class="post" data-post-id="33517" data-author="kalidor" data-date="2012-08-26T17:34:44+00:00" data-subject="Re: CMUD: EXP Tracker">

works pretty well couple things that I noticed though.

The gold for every level has been doubled by code I am guessing since this table was written. Also some of the exp needed is off. So need an updated table hopefully the community has one someplace??

Also I'll be damned if I can get the Score to update anything at all. Played with the trigger, still no luck.

</div>
