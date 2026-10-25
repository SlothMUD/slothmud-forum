---
title: "CMUD and other clients: Script to show gem stats in client."
topic_id: 3647
author: "Tuck"
date: 2011-01-25T05:13:44+00:00
last_activity: 2011-01-26T18:25:05+00:00
last_author: "Tuck"
sticky: false
locked: false
post_count: 4
---

<div class="post" data-post-id="32370" data-author="Tuck" data-date="2011-01-25T05:13:44+00:00">

Cmud gemstats: script that show gem stats on-fly. When gem name displayed, stats will be shown near it.

Usage alias: not needed.

**Update: Major fix for multiple gems.**

How to import to CMUD: Open Settings menu, click File / Import XML.

[Download for cmud and other clients here](http://www.magi.biz/archives/59)

</div>

<div class="post" data-post-id="32371" data-author="Tuck" data-date="2011-01-25T06:18:49+00:00">

There will be major update of the script tomorrow since some awful bugs has been found.

Thanks for patience.

</div>

<div class="post" data-post-id="32377" data-author="Tuck" data-date="2011-01-25T19:01:36+00:00">

Update2: Major fix for multiple gems.

</div>

<div class="post" data-post-id="32383" data-author="Tuck" data-date="2011-01-26T18:25:05+00:00">

Some examples of how script working:

who:

```
*Immortals of SlothMUD* 
--------------------------------
[   *Creator*   ] Splork www.slothmud.org

[pri sec ter qua qui hex sep oct]  Players
--------------------------------
[       *Brigand*  Th:8.28       ] Cizin Vain looks around suspiciously ...
[      *Defender*  Wa:6.38       ] Dsfren ~Dragonsworn~ buying/trading Gems
[        *Seer*  Ma:6.38         ] Tuk <<M.A.G.I>> need imm to connect new vault please
[      *Defender*  Wa:5.38       ] Katie voted today, did you?!?
[      *Magician*  Ma:5.20       ] Belion looking for Eye Agate/Silvery Blue Pearl:  -2 SAVING_SPELL    cloaks and mantles:   +20 CIRCLE_DAM bracers, bracelets, and wrist-bands
[       *Ranger*  Wa:4.38        ] Cyprimus <<M.A.G.I>>
[         *Wit*  Ba:4.34         ] Blackmore ...
[       *Animist*  Dr:4.32       ] Roku ~Dragonsworn~
[       *Ranger*  Wa:4.30        ] Stun *
[     *Hierophant*  Cl:4.25      ] Shyla why do i shock people all the time
[      *Myrmidon*  Wa:4.22       ] Sam 
[       *Ranger*  Wa:4.20        ] Taron 
[40m 40d 40c 39n|23w 15o 11t 10b ] Surfnazi *
[40t 40c 40w 38m|22n 20b 14o 14d ] Scaind <~Gangsta Cleric~>
[40w 40o 40t 30c|24b 21m 13n 11d ] War [Legends]
[40t 40d 28b 17c|11m 10o  9w  7n ] Popa <<M.A.G.I>> i'll pay you 5 bucks to sign up
[40b 39w 28c 20d|12n 11m  9t  8o ] Spag Hetti <<M.A.G.I>> (afk)
[40n 27w 21m 12c| 9t  8o  6d  6b ] Breezewood the Frail
[20d 20c 19m 11n| 3b  2w  1o  1t ] Illusion the tiny metamorph
[20w 20n 14c  7m| 4d  3b  2t  1o ] Roth rummaging around
[20t 20c 12d  0 | 0   0   0   0  ] Dip afk mostly
[20w 17c  8o  5m| 1t  0   0   0  ] Apoc just wandering around
[20w 16n 10c  1d| 1m  1b  1o  1t ] Kade the Untitled
[20m 14c  2w  0 | 0   0   0   0  ] Cannon the Titled
[20b 10t  6c  3d| 2w  1m  1n  1o ] Blardy the Untitled
[11w  1n  1c  1m| 0   0   0   0  ] Kici the Untitled
[ 6w  3c  0   0 | 0   0   0   0  ] Angelus the Untitled
[ 5m  2d  0   0 | 0   0   0   0  ] Lamgwin the Untitled
There are 29 visible players.
Highest total since last bootup: 33.
```

group

```
Group 'Some Chop' is led by Shyla and consists of:
  (Point)            Katie [Wa:5.38 1312hp 250ma 453mv] Totem! | Pearl!       :  +5 HPS shoes and boots
  (Front)              War [Wa:3.30 1126hp 218ma 340mv] dex gem                       
  (Front)        Blackmore [Ba:4.34 1055hp 478ma 370mv] v garnet / gaia               
  (Front)            Taron [Wa:4.20  989hp 472ma 332mv] gregor/rhodo/obsidian         
  (Front)            Cizin [Th:8.28 1262hp 419ma 485mv] CK M.Thief / star ruby        
  (Front)           Scaind [Th:3.38  871hp 343ma 330mv] Yao | Water Opal | White Opal :   +15 STAB_DAM  one-handed weapons:   +5 STAB_DAM bracers, bracelets, and wrist-bands
  (Front)         Cyprimus [Wa:4.38 1092hp 381ma 377mv] Well Groomed Man | P G Pearl  :  +5 HPS shoes and boots
  (Front)              Sam [Wa:4.22 1006hp 555ma 320mv] deacon/amethyst/azurite       

 (Leader)            Shyla [Cl:4.25  734hp 746ma 280mv] Ares/Emerald/Br green emerald 
                       Tuk [Ma:6.38  769hp 674ma 305mv] T-EYE C.SAPP G.Lammasu
                      Popa [Th:2.28  783hp 217ma 313mv] Water Opal | Demeter          :   +15 STAB_DAM  one-handed weapons
 (Absent)         Surfnazi [Ma:3.39  651hp 689ma 241mv] ---
```

</div>
