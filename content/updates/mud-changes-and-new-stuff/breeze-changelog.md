---
title: "Breeze Changelog"
topic_id: 3811
author: "*Breeze*"
date: 2011-11-05T10:51:48+00:00
last_activity: 2013-04-08T02:21:12+00:00
last_author: "*Breeze*"
sticky: false
locked: false
post_count: 21
---

<div class="post" data-post-id="32972" data-author="*Breeze*" data-date="2011-11-05T10:51:48+00:00" data-subject="Breeze Changelog">

**5 Nov 2011**

```
* Fixed auctioneer bug where buyout price could be lower than starting bid (oops!)
* Amount of Drachm/Honor will be displayed as a number if it exceeds 9999
  + This change honors the 'numformat' setting (show/hide commas in numbers)
  + Thank's Toxis for nagging.. err.. reporting. ;)
* Other changes which are not ready to go live yet (thanks ptesters!)
```

Changes in on commit/compile/reboot by a creator.. (hopefully Sunday!)

</div>

<div class="post" data-post-id="32982" data-author="*Breeze*" data-date="2011-11-15T20:35:27+00:00" data-subject="Breeze Changelog - 15-16 Nov 2011">

**15-16 Nov 2011**

```
New Command:
-------------------
* settings login_time_extras
  + toggles automatically showing time extras upon login

Changes:
-------------------
* 'settings' command has been majorly expanded. 
  + if you have mxp enabled you can now click to toggle a setting
* 'mxpsettings'
  + added a few spaces to get things to line up properly

Other:
-------------------
* commands [list|levels|socials]
  + reformatted to *hopefully* look a bit nicer. (not squished together!)
```

changes in when someone commit's the code and reboots

</div>

<div class="post" data-post-id="33008" data-author="*Breeze*" data-date="2011-11-26T08:48:06+00:00" data-subject="Breeze Changelog - 26 Nov 2011">

```
Changes:
-------------------
* Newbie Graveyard
  + I don't understand how but it seems people are forgetting to loot their tomb's
     even tho it says 
"
 % You have been resurrected by a forgotten god.

 % the forgotten god enters your mind and says, 'Make your way back to the world of the living..'
 % HINT: Don't forget to 'get all tomb' and make your way back to the center
 %          of the graveyard. 'pray' at the altar to get back to the mortal realm.
"
    so effective immediately, if you try to leave your tomb, the mud will force
    you to auto-loot your tomb
```

</div>

<div class="post" data-post-id="33009" data-author="*Breeze*" data-date="2011-11-27T06:48:17+00:00" data-subject="Breeze Changelog - 27 Nov 2011">

```
Changes:
-------------------
* Auctioneer
  + fixed missing lfcr on `status` command when there was nothing to show.
  + added gem item (709) to list of safe tho normally forbidden items
    (have special code added in otherwise we would not be able to sell them
     since they all have the same vnum)
  + fixed message for when the auctioneer refuses to take an item
    (was sending wrong buf to vict.. oops)
```

in whenever someone moves code over and compiles/reboots

</div>

<div class="post" data-post-id="33042" data-author="*Breeze*" data-date="2011-12-06T23:38:56+00:00" data-subject="Breeze Changelog - 06 Dec 2011">

```
Changes:
-------------------
* score
  + new modes : stats2/all/all2
    + score stats2 - bargraph representation of score stats
    + score all - same as score + score stats, but in one command
    + score all2 - same as score + score stats2, but in one command
  + score 2 - has extended information added to it.

The following are now visible in the various score modes..
+ flail damage
+ stab damage
+ circle damage
+ heal bonus
+ spell bonus
+ undead control
+ charisma
+ hand damage

score 2 shows all fields.  score stats2 will only show the fields if you actually have any of the stat.

these command(s) will probably be expanded upon as I get time.

Changes in when someone moves over the code, recompiles and reboots
```

</div>

<div class="post" data-post-id="33088" data-author="*Breeze*" data-date="2011-12-12T17:31:08+00:00" data-subject="Breeze Changelog - 12 Dec 2011">

Most of these changes are live.  Some may require a reboot/repop.

Regards...

```
Typos Fixed
+ "camel" in DoD changed to "a camel"
  - Thanks Zuzu for reporting.
  
+ The wisdom of a long forgotten god shines on your deads for the day.
      changed to
  The wisdom of a long forgotten god shines on your deeds for the day.
  - Thanks Timber for reporting
  
+ 'silver surveyers compass' changed to 'silver surveyors compass' (long/short/keywords)
  - Thanks Alyhs for reporting
  
+ 'ornate glass broach' keywords fixed (ornaGe changed to ornate)
  - Thanks Alris for reporting
  
+ 'Master Dolphiare' changed to 'Mistress Dolphiare'
  - Thanks Zuzu for reporting

+ Shaman AQ - importain = important
  - Thanks Sirius for reporting

+ Shaman AQ - other typos fixed that I noticed while fixing the other.
  - Thanks Me :D
  
+ A page of hymms from the Atharvaveda
    changed to
  A page of hymns from the Atharvaveda
  + added 'hymn' keyword
  - Thanks to Pro for reporting
  
+ Room typo in zone: 'Necropolis of the Undead' fixed.
  - Thanks Rita for reporting
  
+ Rhabdos brew note typo fixed
  - Thanks Joesmoe for reporting
  
+ Fixed various typos on Glarglrm in CG
  - Thanks Taron for reporting
  
+ Lost Cross- gargantuan snake- typos in description fixed.
  - Thanks to Joesmoe for reporting
```

</div>

<div class="post" data-post-id="33111" data-author="*Breeze*" data-date="2011-12-21T00:48:58+00:00" data-subject="Breeze Changelog - 21 Dec 2011">

```
 finger <character>
  + now honors 'numformat' setting
    - Requested by Jedi
  + minor code cleanup

 Newbie Graveyard
  + changed if-elseif spaghetti to switch-case
  + fixed respawning in wrong room on praying to get out (hopefully)
  + set default return to room to 8000 (West Gate on BH) in case something
    goes wrong.
```

Live whenever someone moves over code, recompiles and reboots.

</div>

<div class="post" data-post-id="33139" data-author="*Breeze*" data-date="2012-01-15T08:10:46+00:00" data-subject="Breeze Changelog - 05 Jan 2012">

```
finger <character>
  + fixed comma formatting bug that would cause xp over 2 bil to be 
     shown as -2,147,483,648  (Thanks everyone and their mother for reporting)

Gems: Crysoberyl renamed to Chrysoberyl
  + if you have a Crysoberyl come see me and I will change yours out
     [after code is live] (reported by Cardboard)

Newbie Death (Graveyard):
  + fixed cute bug (reported by Neil)

Automatic Group Name
 + Changed `Apalling` to `Appalling`.
    (Thanks Whatta for reporting)
```

Live whenever someone moves over code, recompiles and reboots.

</div>

<div class="post" data-post-id="33165" data-author="*Breeze*" data-date="2012-02-19T23:56:54+00:00" data-subject="Breeze Changelog - 19 Feb 2012">

```
  * Can no longer see Fahren (Vk) emotes while sleeping (Thanks Juggleblood!)
  * Bullies in Thal shouldn't push you while fighting   (Thanks Juggleblood!)
  * Fixed Winds of Fortune message while on boats if mast breaks.
  * Fixed price on burnished steel shield forge
    (was missing a 0)
  * Changed how % is displayed in graph2 if you are over max
```

</div>

<div class="post" data-post-id="33239" data-author="*Breeze*" data-date="2012-03-22T22:12:43+00:00" data-subject="Breeze Changelog - 22 Mar 2012">

Fixed by someone else

------------------------------------------

Magi - Mother Nature's presence can be felt on the Islan today!

Norks - Mother Nature's presence can be felt on the Islan today! should be Island

Sith - Mother Nature's presence can be felt on the Islan today!

Scaind - Mother Nature's presence can be felt on the Islan today! - Island maybe?

Whatta - "Islan" -> "Island" in Mother Nature's presence can be felt on the Islan today!

Idjit - island-specific Mother Nature's presence config: "Islan" should read "Island"

Fixed

------------------------------------------

Magi - againist in room description, should be against

Magi - room description: tie fling should probably be tiefling.

Valiant - Sight of a Cave-in

Kerri - The Throne Room of the Kuo-Toan Homlet should be spelled Hamlet

Whatta - "An important looking sign with poor grammar hangs from the eastern wall." should be "important-looking"

Unmace - on the wizlist, Isabo and Akasha are both listed twice

Oboe - "The fertility goddess smile down upon the creatures of the Island." should be "smiles"

Zuzu - An Mystica Chimera: proc string "bits into" should be "bites into"

 * Fixed

Not a bug

------------------------------------------

Kein - Lars has typos in his message.

 * thats intentional :)

Requires Compile/Reboot/MOBKill

------------------------------------------

Josiah - quest completion text, 'trully' should be spelled truly.

Spoony tells you, `You are truly grand, Spoony. Thank you for rescuing

Josiah tells you, `You are truly grand, Josiah. Thank you for rescuing

Insomniac - Yuan-ti sathar says, 'Enough of this! i am not in the mood for fighting.' "i" needs capitalizing

Thanks to everyone for reporting

</div>

<div class="post" data-post-id="33241" data-author="*Breeze*" data-date="2012-03-25T14:17:24+00:00" data-subject="Breeze Changelog - 25 Mar 2012">

```
Sadonyx Rune/Gem - Renamed to Sardonyx.
  See me or a 45+ to get your Sadonyx gem replaced with a Sardonyx gem.
  Runes should auto-update
```

```
Updated Help Files 
-----------------------------------
Spirit Watcher  - Added recognized commands         * Zuzu, Me
Control Horde   - Changed level to Av 6 from Av 11  * Thanks Beatrix, Ramza, Whiff
Call Followers  - Changed level to Av 5 from Av 7   * Thanks Beatrix
                - Fixed various typos               * Me
Gem             - Changed Crysoberyl to Chrysoberyl * Thanks Beatrix
                - Changed Sadonyx to Sardonyx       * Thanks Jezer, Zuzu, Qhinn
Unholy Strength - Removed Helpfile                  * Thanks Zuzu
Fluidity        - Various typos fixed               * Thanks Qhinn
Housing         - Added a verb. lol.                * Thanks Pynchon
                - Fixed various typos               * Me
Groups          - Fixed to point to Group helpfile  * Thanks Mud
Knights Prayer  - Updated Mana Cost                 * Me
Leveling Avatar - Changed 5th to 9th                * Thanks Cyprimus, Cizin
crimson scourge - Updated duration                  * Thanks Idjit
G.Lloyds Beacon - Fixed typo in usage               * Thanks Ramza
Strata          - 'Enchancement' to 'Enhancement'   * Thanks Cyprimus
Cleanse         - 'cleanse' instead of 'purity'     * Thanks Cyprimus
Kensai          - Changed level to 40 instead of 26 * Thanks Jagon
                - Various typos                     * Thanks Alris, Me
Ptest           - changed 'the cast' to 'the vast'  * Thanks Venom

Summon Undead Creatures
                - Fixed "funky" mana costs          * Thanks Jedi, Kilgore
 

Note : If a helpfile is wrong, messages like 'fix mem helpfile' are useless.
       Tell me what's wrong and what you think they are so I can verify it 
       and fix it.
```

</div>

<div class="post" data-post-id="33273" data-author="*Breeze*" data-date="2012-04-16T19:09:35+00:00" data-subject="Re: Breeze Changelog - 16 April 2012">

```
Fixes
--------------------
 * GEMS
   * It was possible for aggressive mobs to pop gems from other mobs (non pet mobs).
   * This change was reversed. Disregard.

 * Forges
   * On the few forges that returned coins on poofing, the message showed the incorrect amount of coins.

Changes
--------------------
 * Forges
    * Blown forges no longer take all your items.
      That is, the code will decide which item(s) to keep and which to give back.
      At the moment, it is set to 1 item, but we reserve the right to change that at any time.
      To head off rumors, Item value/stats/etc has nothing to do with which item is chosen.
      It is purely a random chance. 
      NOTE :: 
          THIS OPTION MUST BE ENABLED BY THE IMMORTAL WHO CREATED THE FORGE OR A 45+.
          I plan on asking Juggleblood to look at the forges and decide if any of the current
          forges need the feature enabled, but I do not promise that it will be turned on, on any
          particular forge, and please don't nag the immortals about adding it to your favorite forge.

          This feature was added in because we love you ;)

          Changes in whenever code is moved over, recompiled and mud is rebooted.
```

</div>

<div class="post" data-post-id="33343" data-author="*Breeze*" data-date="2012-06-25T18:12:34+00:00" data-subject="Breeze Changelog [25 Jun 2012]">

```
Changes
--------------------
Previously:
  Could not vault anything with [charm] as a keyword.
Now:
  Anything with [charm] keyword with the exception of [charm-juju] or [sidhe-juju] is vaultable.
  As long as nothing else prevents it from being vaulted. (<nag>Oboe</nag>)

Graveyard - can always loot tomb regardless of laden or not.

Additions
--------------------
score stats2
  Added vsSpell (<nag>Tuk</nag>)

Fixes
--------------------
Graveyard
  newbie + graveyard ac bug fixed (<nag>Dr, Various_Others</nag>)
```

</div>

<div class="post" data-post-id="33369" data-author="*Breeze*" data-date="2012-07-10T20:51:36+00:00" data-subject="Breeze Changelog [10 Jul 2012]">

Typos in Helpfiles

```
Fixed
 Kirah ** moon aura help still says druid prime 40, it's a cleric spell now as well
 Beatrix ** help moon aura - says spell is druid prime but its not :) thanks
 Stun ** 'cornona' should be spelled 'corona' in help enhancement
 Eve ** kensai helpfile shows level requirement as 26, when 'skills monk' shows level 40. thanks
 Tuk ** please fix help, practice and real mana values for greater lloyds beacon spell. Thanks!
```

</div>

<div class="post" data-post-id="33704" data-author="*Breeze*" data-date="2012-11-01T09:46:46+00:00" data-subject="Re: Breeze Changelog">

```
 - Supplication
   * Added 29 new Peri names

 - NOKILL flag for mobs
   * If a mob is flagged as NOKILL (innkeepers/shopkeepers/et al) it will gain
     some innate features (mega high ac, mega high hp, insane +hit and +dam)
     try not to kill these mobs as they will hurt you. (cizin tested unbuffed mob 
     and couldnt kill them)
   * MOB will eventually stop fighting you, but you will fight for 1 or 2 rounds :)

 - PATHS
   * this is a complicated one.  there was a very very very very old bug where some
     mobs wouldn't act properly.  mobs that charge, hunt, shadowkill, et al, unless
     they were killed once.  this should now be fixed.
   * this should also fix the song where the mob comes out to you, the thing where
     you throw stuff at a mob to get it to come to you, and the like.
   * most likely this will fix other stuff which i am not thinking of at the moment,
     so beware.

 - Help Files
   * Tox now has access to fix helpfiles, so feel free to point them out to him, or
     email him anything that needs fixed so we can get helpfiles up to date.
```

</div>

<div class="post" data-post-id="33812" data-author="*Breeze*" data-date="2012-12-02T16:41:47+00:00" data-subject="Re: Breeze Changelog">

Changes for 1 Dec 2012

```
fix:
 - possible to lose your rank/drachma/quest/etc kvp's under certain
   circumstances.
 - double logging of G pops during zone resets
 - mob vs mob gem popping if neither mob is a pet

disabled:
 - tons of useless logging

added:
 - lconfig [lvl 46] - configurable logging (allows us to disable
                      logging of certain debug stuff)
```

</div>

<div class="post" data-post-id="33864" data-author="*Breeze*" data-date="2012-12-25T21:43:38+00:00" data-subject="Re: Breeze Changelog">

```
Fixed:
 - Scroll of Heavenly Light Proc
 - Auctioneer
   * Should properly handle Chrysoberyl now (DO NOT SELL *Crysoberyl*! Have an Immortal switch it out)
Added:
 - A really cool set of proc's for Neptune's new area. :D

Not Fixing:
 - Dice Bag
   * Not going to adjust size.  May make a forge/quest/trade to make it bigger at a later time tho (busy atm).
```

</div>

<div class="post" data-post-id="33866" data-author="*Breeze*" data-date="2012-12-27T19:16:06+00:00" data-subject="Re: Breeze Changelog">

```
Fixed:
 mem
 - 25 int can now `mem` 9 spells as intended.
```

</div>

<div class="post" data-post-id="33869" data-author="*Breeze*" data-date="2012-12-29T19:22:34+00:00" data-subject="Breeze Changelog (29 Dec 2012)">

```
Due to the apparent issues people are having to get out of the newbie graveyard, Neptune and I have added
a special proc that tells you in which direction to go to get out.

Messages appear as so :::
An apparition appears before you beckoning you to follow him to the north.

DO NOT FORGET TO LOOT YOUR TOMB
```

</div>

<div class="post" data-post-id="33870" data-author="*juggleblood*" data-date="2012-12-30T17:01:14+00:00" data-subject="Re: Breeze Changelog">

Fixed shadowwalk from dock to magnolia on Lyme.

</div>

<div class="post" data-post-id="34227" data-author="*Breeze*" data-date="2013-04-08T02:21:12+00:00" data-subject="Re: Breeze Changelog">

**08 Apr 2013**

```
I cannot easily fix the 9 mem thing, due to a combination of things that I will not go into here.
Instead, what I did is if you have 25 INT, and you fail your cast masterful spell check, the mud
will give you a 2nd chance for a masterful spell.  I know its not perfect, but after the mess 
caused last time I tried to fix it, I think I will leave it as is.  

I am still considering what else 25 INT should affect, so feel free to email me your ideas,
but don't expect a timely reply or a reply at all, but I will read and consider your suggestions.

my email of course is breeze@   if you don't know the rest of my email, feel free to ask someone
in game.
```

Love, Breeze

</div>
