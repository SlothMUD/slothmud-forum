---
title: "tintin EXP counter"
topic_id: 3417
author: "Samel"
date: 2010-05-05T18:46:07+00:00
last_activity: 2010-05-19T18:25:59+00:00
last_author: "Samel"
sticky: false
locked: false
post_count: 3
---

<div class="post" data-post-id="31091" data-author="Samel" data-date="2010-05-05T18:46:07+00:00">

You need to set your prompt to include exp as one of the fields.  I use a variation on the following:

prompt <$hhp $mma $vmv xp:$x cn:$g ac:$a>

which results in something like:

<395hp 214ma 207mv xp:1152578 cn:14651 ac:-2.1>

The only part we're concerned with is the 'xp:1152578'

This script works once you have levels in all 8 classes .. I'm still working on converting my OOOLD tintin v1.86 scripts as well as adjusting for the new sloth that is and haven't gotten that working without resorting to using a perl or shell script to find and set the right variables.

[code:2hsdm60t]/showme TURNING EXP COUNTER ON;

/alias reset-exp {/var {cntexp} {0}}

/var {cntexp} {0}[/code:2hsdm60t]

This first action will set unused experience from your score.  pretty standard fare, but requires that you type in score every so often.

[code:2hsdm60t]/action {^You have %1 unused experience points.} {

   /var expunused %1;

   domathexp;

}[/code:2hsdm60t]

This second action is the one that requires your prompt to be set.  The benefit of doing it this way is that your $expunused variable is always accurate.  If, however, you don't want to show exp in your prompt, then use the first action above.

[code:2hsdm60t]/action {^<%* xp:%2 cn:%*} {

   /if {$expunused != %2} {

      /math newexp {%2 - $expunused};

      /math cntexp {$cntexp + $newexp};

      /math expunused %2;

   };

}[/code:2hsdm60t]

This alias is the only one you'll ever need to type in - typing 'exp' will show you a table either capped at 20 or 40 of classes you can still gain experience in.

[code:2hsdm60t]/alias exp {

   domathexp;

   /showme $cntexp Experience since reset;

   /if {$Lvl1 <= 20 }{exp2}{exp4}

}

This determines classes and levels in each - as previously noted, this only currently works once you have levels in all 8 classes.

```
/action {^Your levels:  %1: %2 %3: %4 %5: %6 %7: %8 %9: %10 %11: %12 %13: %14 %15: %16} {
   /var pri %1 ;  /var Lvl1 %2 ;  check1;
   /var sec %3 ;  /var Lvl2 %4 ;  check2;
   /var ter %5 ;  /var Lvl3 %6 ;  check3;
   /var qua %7 ;  /var Lvl4 %8 ;  check4;
   /var qui %9 ;  /var Lvl5 %10 ; check5;
   /var hex %11 ; /var Lvl6 %12 ; check6;
   /var sep %13 ; /var Lvl7 %14 ; check7;
   /var oct %15 ; /var Lvl8 %16 ; check8;
}
```

From here on out, we have all 'behind-the-scenes' aliases for calculation purposes.

```
/alias domathexp {
   /math nxtpri {$Lvl1 + 1};
   /math nxtsec {$Lvl2 + 1};
   /math nxtter {$Lvl3 + 1};
   /math nxtqua {$Lvl4 + 1};
   /math nxtqui {$Lvl5 + 1};
   /math nxthex {$Lvl6 + 1};
   /math nxtsep {$Lvl7 + 1};
   /math nxtoct {$Lvl8 + 1};
   /math expneedpri {$ExpLvl1 - $expunused};
   /math expneedsec {$ExpLvl2 - $expunused};
   /math expneedter {$ExpLvl3 - $expunused};
   /math expneedqua {$ExpLvl4 - $expunused};
   /math expneedqui {$ExpLvl5 - $expunused};
   /math expneedhex {$ExpLvl6 - $expunused};
   /math expneedsep {$ExpLvl7 - $expunused};
   /math expneedoct {$ExpLvl8 - $expunused};
}

/alias exp4 {
   /showme (Class)   Unused Exp   Needed / required;
   /if {$Lvl1 != 40} {/showme ($pri$nxtpri) -  $expunused       $expneedpri / $ExpLvl1};
   /if {$Lvl2 != 40} {/showme ($sec$nxtsec) -  $expunused       $expneedsec / $ExpLvl2};
   /if {$Lvl3 != 40} {/showme ($ter$nxtter) -  $expunused       $expneedter / $ExpLvl3};
   /if {$Lvl4 != 40} {/showme ($qua$nxtqua) -  $expunused       $expneedqua / $ExpLvl4};
   /if {$Lvl5 != 40} {/showme ($qui$nxtqui) -  $expunused       $expneedqui / $ExpLvl5};
   /if {$Lvl6 != 40} {/showme ($hex$nxthex) -  $expunused       $expneedhex / $ExpLvl6};
   /if {$Lvl7 != 40} {/showme ($sep$nxtsep) -  $expunused       $expneedsep / $ExpLvl7};
   /if {$Lvl8 != 40} {/showme ($oct$nxtoct) -  $expunused       $expneedoct / $ExpLvl8};
}
/alias exp2 {
   /showme (Class)   Unused Exp   Needed / required;
   /if {$Lvl1 != 20} {/showme ($pri$nxtpri) -  $expunused       $expneedpri / $ExpLvl1};
   /if {$Lvl2 != 20} {/showme ($sec$nxtsec) -  $expunused       $expneedsec / $ExpLvl2};
   /if {$Lvl3 != 20} {/showme ($ter$nxtter) -  $expunused       $expneedter / $ExpLvl3};
   /if {$Lvl4 != 20} {/showme ($qua$nxtqua) -  $expunused       $expneedqua / $ExpLvl4};
   /if {$Lvl5 != 20} {/showme ($qui$nxtqui) -  $expunused       $expneedqui / $ExpLvl5};
   /if {$Lvl6 != 20} {/showme ($hex$nxthex) -  $expunused       $expneedhex / $ExpLvl6};
   /if {$Lvl7 != 20} {/showme ($sep$nxtsep) -  $expunused       $expneedsep / $ExpLvl7};
   /if {$Lvl8 != 20} {/showme ($oct$nxtoct) -  $expunused       $expneedoct / $ExpLvl8};
}
```

/NOP PRIME EXPERIENCE

/alias check1 {

   /if {$Lvl1 == 1}{/var ExpLvl1 {2000}};

   /if {$Lvl1 == 2}{/var ExpLvl1 {4000}};

   /if {$Lvl1 == 3}{/var ExpLvl1 {9000}};

   /if {$Lvl1 == 4}{/var ExpLvl1 {15000}};

   /if {$Lvl1 == 5}{/var ExpLvl1 {20000}};

   /if {$Lvl1 == 6}{/var ExpLvl1 {30000}};

   /if {$Lvl1 == 7}{/var ExpLvl1 {40000}};

   /if {$Lvl1 == 8}{/var ExpLvl1 {80000}};

   /if {$Lvl1 == 9}{/var ExpLvl1 {120000}};

   /if {$Lvl1 == 10}{/var ExpLvl1 {150000}};

   /if {$Lvl1 == 11}{/var ExpLvl1 {200000}};

   /if {$Lvl1 == 12}{/var ExpLvl1 {250000}};

   /if {$Lvl1 == 13}{/var ExpLvl1 {300000}};

   /if {$Lvl1 == 14}{/var ExpLvl1 {400000}};

   /if {$Lvl1 == 15}{/var ExpLvl1 {450000}};

   /if {$Lvl1 == 16}{/var ExpLvl1 {500000}};

   /if {$Lvl1 == 17}{/var ExpLvl1 {550000}};

   /if {$Lvl1 == 18}{/var ExpLvl1 {600000}};

   /if {$Lvl1 == 19}{/var ExpLvl1 {700000}};

   /if {$Lvl1 == 20}{/var ExpLvl1 {800000}};

   /if {$Lvl1 == 21}{/var ExpLvl1 {1000000}};

   /if {$Lvl1 == 22}{/var ExpLvl1 {1500000}};

   /if {$Lvl1 == 23}{/var ExpLvl1 {2000000}};

   /if {$Lvl1 == 24}{/var ExpLvl1 {2500000}};

   /if {$Lvl1 == 25}{/var ExpLvl1 {3500000}};

   /if {$Lvl1 == 26}{/var ExpLvl1 {4700000}};

   /if {$Lvl1 == 27}{/var ExpLvl1 {6000000}};

   /if {$Lvl1 == 28}{/var ExpLvl1 {7300000}};

   /if {$Lvl1 == 29}{/var ExpLvl1 {8600000}};

   /if {$Lvl1 == 30}{/var ExpLvl1 {9900000}};

   /if {$Lvl1 == 31}{/var ExpLvl1 {11000000}};

   /if {$Lvl1 == 32}{/var ExpLvl1 {13000000}};

   /if {$Lvl1 == 33}{/var ExpLvl1 {15000000}};

   /if {$Lvl1 == 34}{/var ExpLvl1 {18300000}};

   /if {$Lvl1 == 35}{/var ExpLvl1 {21500000}};

   /if {$Lvl1 == 36}{/var ExpLvl1 {25000000}};

   /if {$Lvl1 == 37}{/var ExpLvl1 {30000000}};

   /if {$Lvl1 == 38}{/var ExpLvl1 {35000000}};

   /if {$Lvl1 == 39}{/var ExpLvl1 {40000000}};

   /if {$Lvl1 == 40}{/var ExpLvl1 {0}}

}

/NOP SECONDARY EXPERIENCE

/alias check2 {

    /if {$Lvl2 == 0}{/var ExpLvl2 {4000}};

    /if {$Lvl2 == 1}{/var ExpLvl2 {8000}};

    /if {$Lvl2 == 2}{/var ExpLvl2 {16000}};

    /if {$Lvl2 == 3}{/var ExpLvl2 {32000}};

    /if {$Lvl2 == 4}{/var ExpLvl2 {45000}};

    /if {$Lvl2 == 5}{/var ExpLvl2 {70000}};

    /if {$Lvl2 == 6}{/var ExpLvl2 {100000}};

    /if {$Lvl2 == 7}{/var ExpLvl2 {140000}};

    /if {$Lvl2 == 8}{/var ExpLvl2 {280000}};

    /if {$Lvl2 == 9}{/var ExpLvl2 {360000}};

    /if {$Lvl2 == 10}{/var ExpLvl2 {550000}};

    /if {$Lvl2 == 11}{/var ExpLvl2 {800000}};

    /if {$Lvl2 == 12}{/var ExpLvl2 {1000000}};

    /if {$Lvl2 == 13}{/var ExpLvl2 {1200000}};

    /if {$Lvl2 == 14}{/var ExpLvl2 {1600000}};

    /if {$Lvl2 == 15}{/var ExpLvl2 {1800000}};

    /if {$Lvl2 == 16}{/var ExpLvl2 {2000000}};

    /if {$Lvl2 == 17}{/var ExpLvl2 {2200000}};

    /if {$Lvl2 == 18}{/var ExpLvl2 {2400000}};

    /if {$Lvl2 == 19}{/var ExpLvl2 {2800000}};

    /if {$Lvl2 == 20}{/var ExpLvl2 {3200000}};

    /if {$Lvl2 == 21}{/var ExpLvl2 {4000000}};

    /if {$Lvl2 == 22}{/var ExpLvl2 {6000000}};

    /if {$Lvl2 == 23}{/var ExpLvl2 {8000000}};

    /if {$Lvl2 == 24}{/var ExpLvl2 {10000000}};

    /if {$Lvl2 == 25}{/var ExpLvl2 {12000000}};

    /if {$Lvl2 == 26}{/var ExpLvl2 {14800000}};

    /if {$Lvl2 == 27}{/var ExpLvl2 {18000000}};

    /if {$Lvl2 == 28}{/var ExpLvl2 {21000000}};

    /if {$Lvl2 == 29}{/var ExpLvl2 {28000000}};

    /if {$Lvl2 == 30}{/var ExpLvl2 {32000000}};

    /if {$Lvl2 == 31}{/var ExpLvl2 {36000000}};

    /if {$Lvl2 == 32}{/var ExpLvl2 {39000000}};

    /if {$Lvl2 == 33}{/var ExpLvl2 {45000000}};

    /if {$Lvl2 == 34}{/var ExpLvl2 {50800000}};

    /if {$Lvl2 == 35}{/var ExpLvl2 {60500000}};

    /if {$Lvl2 == 36}{/var ExpLvl2 {65000000}};

    /if {$Lvl2 == 37}{/var ExpLvl2 {70000000}};

    /if {$Lvl2 == 38}{/var ExpLvl2 {85000000}};

    /if {$Lvl2 == 39}{/var ExpLvl2 {90000000}};

    /if {$Lvl2 == 40}{/var ExpLvl2 {0}}

}

/NOP TERTIARY EXPERIENCE

/alias check3 {

    /if {$Lvl3 == 0}{/var ExpLvl3 {12000}};

    /if {$Lvl3 == 1}{/var ExpLvl3 {24000}};

    /if {$Lvl3 == 2}{/var ExpLvl3 {48000}};

    /if {$Lvl3 == 3}{/var ExpLvl3 {96000}};

    /if {$Lvl3 == 4}{/var ExpLvl3 {135000}};

    /if {$Lvl3 == 5}{/var ExpLvl3 {210000}};

    /if {$Lvl3 == 6}{/var ExpLvl3 {300000}};

    /if {$Lvl3 == 7}{/var ExpLvl3 {420000}};

    /if {$Lvl3 == 8}{/var ExpLvl3 {840000}};

    /if {$Lvl3 == 9}{/var ExpLvl3 {1080000}};

    /if {$Lvl3 == 10}{/var ExpLvl3 {1650000}};

    /if {$Lvl3 == 11}{/var ExpLvl3 {2400000}};

    /if {$Lvl3 == 12}{/var ExpLvl3 {3000000}};

    /if {$Lvl3 == 13}{/var ExpLvl3 {3600000}};

    /if {$Lvl3 == 14}{/var ExpLvl3 {4800000}};

    /if {$Lvl3 == 15}{/var ExpLvl3 {5400000}};

    /if {$Lvl3 == 16}{/var ExpLvl3 {6000000}};

    /if {$Lvl3 == 17}{/var ExpLvl3 {6600000}};

    /if {$Lvl3 == 18}{/var ExpLvl3 {7200000}};

    /if {$Lvl3 == 19}{/var ExpLvl3 {8400000}};

    /if {$Lvl3 == 20}{/var ExpLvl3 {9600000}};

    /if {$Lvl3 == 21}{/var ExpLvl3 {12000000}};

    /if {$Lvl3 == 22}{/var ExpLvl3 {18000000}};

    /if {$Lvl3 == 23}{/var ExpLvl3 {24000000}};

    /if {$Lvl3 == 24}{/var ExpLvl3 {30000000}};

    /if {$Lvl3 == 25}{/var ExpLvl3 {36000000}};

    /if {$Lvl3 == 26}{/var ExpLvl3 {44400000}};

    /if {$Lvl3 == 27}{/var ExpLvl3 {54000000}};

    /if {$Lvl3 == 28}{/var ExpLvl3 {63000000}};

    /if {$Lvl3 == 29}{/var ExpLvl3 {84000000}};

    /if {$Lvl3 == 30}{/var ExpLvl3 {96000000}};

    /if {$Lvl3 == 31}{/var ExpLvl3 {108000000}};

    /if {$Lvl3 == 32}{/var ExpLvl3 {117000000}};

    /if {$Lvl3 == 33}{/var ExpLvl3 {135000000}};

    /if {$Lvl3 == 34}{/var ExpLvl3 {152400000}};

    /if {$Lvl3 == 35}{/var ExpLvl3 {181500000}};

    /if {$Lvl3 == 36}{/var ExpLvl3 {195000000}};

    /if {$Lvl3 == 37}{/var ExpLvl3 {210000000}};

    /if {$Lvl3 == 38}{/var ExpLvl3 {255000000}};

    /if {$Lvl3 == 39}{/var ExpLvl3 {270000000}};

    /if {$Lvl3 == 40}{/var ExpLvl3 {0}}

}

/NOP QUAD EXPERIENCE

/alias check4 {

   /if {$Lvl4 == 0}{/var ExpLvl4 {40000}};

   /if {$Lvl4 == 1}{/var ExpLvl4 {80000}};

   /if {$Lvl4 == 2}{/var ExpLvl4 {160000}};

   /if {$Lvl4 == 3}{/var ExpLvl4 {320000}};

   /if {$Lvl4 == 4}{/var ExpLvl4 {450000}};

   /if {$Lvl4 == 5}{/var ExpLvl4 {700000}};

   /if {$Lvl4 == 6}{/var ExpLvl4 {1000000}};

   /if {$Lvl4 == 7}{/var ExpLvl4 {1400000}};

   /if {$Lvl4 == 8}{/var ExpLvl4 {2800000}};

   /if {$Lvl4 == 9}{/var ExpLvl4 {3600000}};

   /if {$Lvl4 == 10}{/var ExpLvl4 {5500000}};

   /if {$Lvl4 == 11}{/var ExpLvl4 {8000000}};

   /if {$Lvl4 == 12}{/var ExpLvl4 {10000000}};

   /if {$Lvl4 == 13}{/var ExpLvl4 {12000000}};

   /if {$Lvl4 == 14}{/var ExpLvl4 {16000000}};

   /if {$Lvl4 == 15}{/var ExpLvl4 {18000000}};

   /if {$Lvl4 == 16}{/var ExpLvl4 {20000000}};

   /if {$Lvl4 == 17}{/var ExpLvl4 {22000000}};

   /if {$Lvl4 == 18}{/var ExpLvl4 {24000000}};

   /if {$Lvl4 == 19}{/var ExpLvl4 {28000000}};

   /if {$Lvl4 == 20}{/var ExpLvl4 {32000000}};

   /if {$Lvl4 == 21}{/var ExpLvl4 {40000000}};

   /if {$Lvl4 == 22}{/var ExpLvl4 {60000000}};

   /if {$Lvl4 == 23}{/var ExpLvl4 {80000000}};

   /if {$Lvl4 == 24}{/var ExpLvl4 {100000000}};

   /if {$Lvl4 == 25}{/var ExpLvl4 {120000000}};

   /if {$Lvl4 == 26}{/var ExpLvl4 {148000000}};

   /if {$Lvl4 == 27}{/var ExpLvl4 {180000000}};

   /if {$Lvl4 == 28}{/var ExpLvl4 {210000000}};

   /if {$Lvl4 == 29}{/var ExpLvl4 {280000000}};

   /if {$Lvl4 == 30}{/var ExpLvl4 {320000000}};

   /if {$Lvl4 == 31}{/var ExpLvl4 {360000000}};

   /if {$Lvl4 == 32}{/var ExpLvl4 {390000000}};

   /if {$Lvl4 == 33}{/var ExpLvl4 {450000000}};

   /if {$Lvl4 == 34}{/var ExpLvl4 {508000000}};

   /if {$Lvl4 == 35}{/var ExpLvl4 {605000000}};

   /if {$Lvl4 == 36}{/var ExpLvl4 {650000000}};

   /if {$Lvl4 == 37}{/var ExpLvl4 {700000000}};

   /if {$Lvl4 == 38}{/var ExpLvl4 {850000000}};

   /if {$Lvl4 == 39}{/var ExpLvl4 {900000000}};

   /if {$Lvl4 == 40}{/var ExpLvl4 {0}}

}

/alias check5 {

   /if {$Lvl5 == 0}{/var ExpLvl5 {80000}};

   /if {$Lvl5 == 1}{/var ExpLvl5 {160000}};

   /if {$Lvl5 == 2}{/var ExpLvl5 {320000}};

   /if {$Lvl5 == 3}{/var ExpLvl5 {640000}};

   /if {$Lvl5 == 4}{/var ExpLvl5 {900000}};

   /if {$Lvl5 == 5}{/var ExpLvl5 {1400000}};

   /if {$Lvl5 == 6}{/var ExpLvl5 {2000000}};

   /if {$Lvl5 == 7}{/var ExpLvl5 {2800000}};

   /if {$Lvl5 == 8}{/var ExpLvl5 {5600000}};

   /if {$Lvl5 == 9}{/var ExpLvl5 {7200000}};

   /if {$Lvl5 == 10}{/var ExpLvl5 {11000000}};

   /if {$Lvl5 == 11}{/var ExpLvl5 {16000000}};

   /if {$Lvl5 == 12}{/var ExpLvl5 {20000000}};

   /if {$Lvl5 == 13}{/var ExpLvl5 {24000000}};

   /if {$Lvl5 == 14}{/var ExpLvl5 {32000000}};

   /if {$Lvl5 == 15}{/var ExpLvl5 {36000000}};

   /if {$Lvl5 == 16}{/var ExpLvl5 {40000000}};

   /if {$Lvl5 == 17}{/var ExpLvl5 {44000000}};

   /if {$Lvl5 == 18}{/var ExpLvl5 {48000000}};

   /if {$Lvl5 == 19}{/var ExpLvl5 {56000000}};

   /if {$Lvl5 == 20}{/var ExpLvl5 {64000000}};

   /if {$Lvl5 == 21}{/var ExpLvl5 {80000000}};

   /if {$Lvl5 == 22}{/var ExpLvl5 {120000000}};

   /if {$Lvl5 == 23}{/var ExpLvl5 {160000000}};

   /if {$Lvl5 == 24}{/var ExpLvl5 {200000000}};

   /if {$Lvl5 == 25}{/var ExpLvl5 {240000000}};

   /if {$Lvl5 == 26}{/var ExpLvl5 {296000000}};

   /if {$Lvl5 == 27}{/var ExpLvl5 {360000000}};

   /if {$Lvl5 == 28}{/var ExpLvl5 {420000000}};

   /if {$Lvl5 == 29}{/var ExpLvl5 {560000000}};

   /if {$Lvl5 == 30}{/var ExpLvl5 {640000000}};

   /if {$Lvl5 == 31}{/var ExpLvl5 {720000000}};

   /if {$Lvl5 == 32}{/var ExpLvl5 {780000000}};

   /if {$Lvl5 == 33}{/var ExpLvl5 {900000000}};

   /if {$Lvl5 == 34}{/var ExpLvl5 {1016000000}};

   /if {$Lvl5 == 35}{/var ExpLvl5 {1210000000}};

   /if {$Lvl5 == 36}{/var ExpLvl5 {1300000000}};

   /if {$Lvl5 == 37}{/var ExpLvl5 {1400000000}};

   /if {$Lvl5 == 38}{/var ExpLvl5 {1700000000}};

   /if {$Lvl5 == 39}{/var ExpLvl5 {1800000000}};

   /if {$Lvl5 == 40}{/var ExpLvl5 {0}}

}

/alias check6 {

   /if {$Lvl6 == 0}{/var ExpLvl6 {120000}};

   /if {$Lvl6 == 1}{/var ExpLvl6 {240000}};

   /if {$Lvl6 == 2}{/var ExpLvl6 {480000}};

   /if {$Lvl6 == 3}{/var ExpLvl6 {960000}};

   /if {$Lvl6 == 4}{/var ExpLvl6 {1350000}};

   /if {$Lvl6 == 5}{/var ExpLvl6 {2100000}};

   /if {$Lvl6 == 6}{/var ExpLvl6 {3000000}};

   /if {$Lvl6 == 7}{/var ExpLvl6 {4200000}};

   /if {$Lvl6 == 8}{/var ExpLvl6 {8400000}};

   /if {$Lvl6 == 9}{/var ExpLvl6 {10800000}};

   /if {$Lvl6 == 10}{/var ExpLvl6 {16500000}};

   /if {$Lvl6 == 11}{/var ExpLvl6 {24000000}};

   /if {$Lvl6 == 12}{/var ExpLvl6 {30000000}};

   /if {$Lvl6 == 13}{/var ExpLvl6 {36000000}};

   /if {$Lvl6 == 14}{/var ExpLvl6 {48000000}};

   /if {$Lvl6 == 15}{/var ExpLvl6 {54000000}};

   /if {$Lvl6 == 16}{/var ExpLvl6 {60000000}};

   /if {$Lvl6 == 17}{/var ExpLvl6 {66000000}};

   /if {$Lvl6 == 18}{/var ExpLvl6 {72000000}};

   /if {$Lvl6 == 19}{/var ExpLvl6 {84000000}};

   /if {$Lvl6 == 20}{/var ExpLvl6 {96000000}};

   /if {$Lvl6 == 21}{/var ExpLvl6 {120000000}};

   /if {$Lvl6 == 22}{/var ExpLvl6 {180000000}};

   /if {$Lvl6 == 23}{/var ExpLvl6 {240000000}};

   /if {$Lvl6 == 24}{/var ExpLvl6 {300000000}};

   /if {$Lvl6 == 25}{/var ExpLvl6 {360000000}};

   /if {$Lvl6 == 26}{/var ExpLvl6 {444000000}};

   /if {$Lvl6 == 27}{/var ExpLvl6 {540000000}};

   /if {$Lvl6 == 28}{/var ExpLvl6 {630000000}};

   /if {$Lvl6 == 29}{/var ExpLvl6 {840000000}};

   /if {$Lvl6 == 30}{/var ExpLvl6 {960000000}};

   /if {$Lvl6 == 31}{/var ExpLvl6 {1080000000}};

   /if {$Lvl6 == 32}{/var ExpLvl6 {1170000000}};

   /if {$Lvl6 == 33}{/var ExpLvl6 {1350000000}};

   /if {$Lvl6 == 34}{/var ExpLvl6 {1524000000}};

   /if {$Lvl6 == 35}{/var ExpLvl6 {1815000000}};

   /if {$Lvl6 == 36}{/var ExpLvl6 {1950000000}};

   /if {$Lvl6 == 37}{/var ExpLvl6 {2100000000}};

   /if {$Lvl6 == 38}{/var ExpLvl6 {2550000000}};

   /if {$Lvl6 == 39}{/var ExpLvl6 {2700000000}};

   /if {$Lvl6 == 40}{/var ExpLvl6 {0}}

}

/alias check7 {

   /if {$Lvl7 == 0}{/var ExpLvl7 {240000}};

   /if {$Lvl7 == 1}{/var ExpLvl7 {480000}};

   /if {$Lvl7 == 2}{/var ExpLvl7 {960000}};

   /if {$Lvl7 == 3}{/var ExpLvl7 {1920000}};

   /if {$Lvl7 == 4}{/var ExpLvl7 {2700000}};

   /if {$Lvl7 == 5}{/var ExpLvl7 {4200000}};

   /if {$Lvl7 == 6}{/var ExpLvl7 {6000000}};

   /if {$Lvl7 == 7}{/var ExpLvl7 {8400000}};

   /if {$Lvl7 == 8}{/var ExpLvl7 {16800000}};

   /if {$Lvl7 == 9}{/var ExpLvl7 {21600000}};

   /if {$Lvl7 == 10}{/var ExpLvl7 {33000000}};

   /if {$Lvl7 == 11}{/var ExpLvl7 {48000000}};

   /if {$Lvl7 == 12}{/var ExpLvl7 {60000000}};

   /if {$Lvl7 == 13}{/var ExpLvl7 {72000000}};

   /if {$Lvl7 == 14}{/var ExpLvl7 {96000000}};

   /if {$Lvl7 == 15}{/var ExpLvl7 {108000000}};

   /if {$Lvl7 == 16}{/var ExpLvl7 {120000000}};

   /if {$Lvl7 == 17}{/var ExpLvl7 {132000000}};

   /if {$Lvl7 == 18}{/var ExpLvl7 {144000000}};

   /if {$Lvl7 == 19}{/var ExpLvl7 {168000000}};

   /if {$Lvl7 == 20}{/var ExpLvl7 {192000000}};

   /if {$Lvl7 == 21}{/var ExpLvl7 {240000000}};

   /if {$Lvl7 == 22}{/var ExpLvl7 {360000000}};

   /if {$Lvl7 == 23}{/var ExpLvl7 {480000000}};

   /if {$Lvl7 == 24}{/var ExpLvl7 {600000000}};

   /if {$Lvl7 == 25}{/var ExpLvl7 {720000000}};

   /if {$Lvl7 == 26}{/var ExpLvl7 {888000000}};

   /if {$Lvl7 == 27}{/var ExpLvl7 {1080000000}};

   /if {$Lvl7 == 28}{/var ExpLvl7 {1260000000}};

   /if {$Lvl7 == 39}{/var ExpLvl7 {1680000000}};

   /if {$Lvl7 == 30}{/var ExpLvl7 {1920000000}};

   /if {$Lvl7 == 31}{/var ExpLvl7 {2160000000}};

   /if {$Lvl7 == 32}{/var ExpLvl7 {2340000000}};

   /if {$Lvl7 == 33}{/var ExpLvl7 {2700000000}};

   /if {$Lvl7 == 34}{/var ExpLvl7 {3048000000}};

   /if {$Lvl7 == 35}{/var ExpLvl7 {3630000000}};

   /if {$Lvl7 == 36}{/var ExpLvl7 {3900000000}};

   /if {$Lvl7 == 37}{/var ExpLvl7 {4200000000}};

   /if {$Lvl7 == 38}{/var ExpLvl7 {5100000000}};

   /if {$Lvl7 == 39}{/var ExpLvl7 {5400000000}};

   /if {$Lvl7 == 40}{/var ExpLvl7 {0}}

}

/alias check8 {

   /if {$Lvl8 == 0}{/var ExpLvl8 {320000}};

   /if {$Lvl8 == 1}{/var ExpLvl8 {640000}};

   /if {$Lvl8 == 2}{/var ExpLvl8 {1280000}};

   /if {$Lvl8 == 3}{/var ExpLvl8 {2560000}};

   /if {$Lvl8 == 4}{/var ExpLvl8 {3600000}};

   /if {$Lvl8 == 5}{/var ExpLvl8 {5600000}};

   /if {$Lvl8 == 6}{/var ExpLvl8 {8000000}};

   /if {$Lvl8 == 7}{/var ExpLvl8 {11200000}};

   /if {$Lvl8 == 8}{/var ExpLvl8 {22400000}};

   /if {$Lvl8 == 9}{/var ExpLvl8 {28800000}};

   /if {$Lvl8 == 10}{/var ExpLvl8 {44000000}};

   /if {$Lvl8 == 11}{/var ExpLvl8 {64000000}};

   /if {$Lvl8 == 12}{/var ExpLvl8 {80000000}};

   /if {$Lvl8 == 13}{/var ExpLvl8 {96000000}};

   /if {$Lvl8 == 14}{/var ExpLvl8 {128000000}};

   /if {$Lvl8 == 15}{/var ExpLvl8 {144000000}};

   /if {$Lvl8 == 16}{/var ExpLvl8 {160000000}};

   /if {$Lvl8 == 17}{/var ExpLvl8 {176000000}};

   /if {$Lvl8 == 18}{/var ExpLvl8 {192000000}};

   /if {$Lvl8 == 19}{/var ExpLvl8 {224000000}};

   /if {$Lvl8 == 20}{/var ExpLvl8 {256000000}};

   /if {$Lvl8 == 21}{/var ExpLvl8 {320000000}};

   /if {$Lvl8 == 22}{/var ExpLvl8 {480000000}};

   /if {$Lvl8 == 23}{/var ExpLvl8 {640000000}};

   /if {$Lvl8 == 24}{/var ExpLvl8 {800000000}};

   /if {$Lvl8 == 25}{/var ExpLvl8 {960000000}};

   /if {$Lvl8 == 26}{/var ExpLvl8 {1184000000}};

   /if {$Lvl8 == 27}{/var ExpLvl8 {1440000000}};

   /if {$Lvl8 == 28}{/var ExpLvl8 {1680000000}};

   /if {$Lvl8 == 29}{/var ExpLvl8 {2240000000}};

   /if {$Lvl8 == 30}{/var ExpLvl8 {2560000000}};

   /if {$Lvl8 == 31}{/var ExpLvl8 {2880000000}};

   /if {$Lvl8 == 32}{/var ExpLvl8 {3120000000}};

   /if {$Lvl8 == 33}{/var ExpLvl8 {3600000000}};

   /if {$Lvl8 == 34}{/var ExpLvl8 {4064000000}};

   /if {$Lvl8 == 35}{/var ExpLvl8 {4840000000}};

   /if {$Lvl8 == 36}{/var ExpLvl8 {5200000000}};

   /if {$Lvl8 == 37}{/var ExpLvl8 {5600000000}};

   /if {$Lvl8 == 38}{/var ExpLvl8 {6800000000}};

   /if {$Lvl8 == 39}{/var ExpLvl8 {7200000000}};

   /if {$Lvl8 == 40}{/var ExpLvl8 {0}}

}

[/code:2hsdm60t]

</div>

<div class="post" data-post-id="31092" data-author="Samel" data-date="2010-05-05T19:00:42+00:00">

as an aside to the below script, i use '/' for my tintin command character as that's much easier for me to reach for than a shift-3 (#)

of course, change as you will and feedback is always welcome as well :)

</div>

<div class="post" data-post-id="31165" data-author="Samel" data-date="2010-05-19T18:25:59+00:00">

As an update, if using tintin on unix, replace the /action in the below script with:

[code:22z2b8ev]

/action {^Your levels:%*} {/script ./tt.levels.ksh %0}

[/code:22z2b8ev]

Then, when you execute 'score' your class and level variables are set and properly work no matter how many classes you have levels in.

Here is tt.levels.ksh 

[code:22z2b8ev]#!/bin/ksh

STRING=$*

PRI=$(echo ${STRING} | awk  '{print $3}' | awk -F: '{print $1}')

Lvl1=$(echo ${STRING} | awk '{print $4}')

SEC=$(echo ${STRING} | awk  '{print $5}' | awk -F: '{print $1}')

Lvl2=$(echo ${STRING} | awk '{print $6}')

TRI=$(echo ${STRING} | awk  '{print $7}' | awk -F: '{print $1}')

Lvl3=$(echo ${STRING} | awk '{print $8}')

QUA=$(echo ${STRING} | awk  '{print $9}' | awk -F: '{print $1}')

Lvl4=$(echo ${STRING} | awk '{print $10}')

QUI=$(echo ${STRING} | awk  '{print $11}' | awk -F: '{print $1}')

Lvl5=$(echo ${STRING} | awk '{print $12}')

HEX=$(echo ${STRING} | awk  '{print $13}' | awk -F: '{print $1}')

Lvl6=$(echo ${STRING} | awk '{print $14}')

SEP=$(echo ${STRING} | awk  '{print $15}' | awk -F: '{print $1}')

Lvl7=$(echo ${STRING} | awk '{print $16}')

OCT=$(echo ${STRING} | awk  '{print $17}' | awk -F: '{print $1}')

Lvl8=$(echo ${STRING} | awk '{print $18}')

print "/var pri ${PRI}"

print "/var Lvl1 ${Lvl1}"

[[ -n  ${SEC} ]] && print "/var sec ${SEC}" || print "/var sec --"

[[ -n  ${TRI} ]] && print "/var tri ${TRI}" || print "/var tri --"

[[ -n  ${QUA} ]] && print "/var qua ${QUA}" || print "/var qua --"

[[ -n  ${QUI} ]] && print "/var qui ${QUI}" || print "/var qui --"

[[ -n  ${HEX} ]] && print "/var hex ${HEX}" || print "/var hex --"

[[ -n  ${SEP} ]] && print "/var sep ${SEP}" || print "/var sep --"

[[ -n  ${OCT} ]] && print "/var oct ${OCT}" || print "/var oct --"

[[ -n  ${Lvl2} ]] && print "/var Lvl2 ${Lvl2}" || print "/var Lvl2 0"

[[ -n  ${Lvl3} ]] && print "/var Lvl3 ${Lvl3}" || print "/var Lvl3 0"

[[ -n  ${Lvl4} ]] && print "/var Lvl4 ${Lvl4}" || print "/var Lvl4 0"

[[ -n  ${Lvl5} ]] && print "/var Lvl5 ${Lvl5}" || print "/var Lvl5 0"

[[ -n  ${Lvl6} ]] && print "/var Lvl6 ${Lvl6}" || print "/var Lvl6 0"

[[ -n  ${Lvl7} ]] && print "/var Lvl7 ${Lvl7}" || print "/var Lvl7 0"

[[ -n  ${Lvl8} ]] && print "/var Lvl8 ${Lvl8}" || print "/var Lvl8 0"[/code:22z2b8ev]

</div>
