---
title: "Jul-Sep 2008: General Bugs/Improvements"
topic_id: 2932
author: "Judge"
date: 2008-09-24T12:10:47+00:00
last_activity: 2008-09-24T12:10:47+00:00
last_author: "Judge"
sticky: false
locked: false
post_count: 1
---

<div class="post" data-post-id="26453" data-author="Judge" data-date="2008-09-24T12:10:47+00:00" data-subject="Jul-Sep 2008: General Bugs/Improvements">

Here are the code fixes/changes I've made since July up September... this list only includes ones that the player is likely to notice.  Of course there are about 400% more changes than the ones listed below that are to do with the overall maintenance of the system,new/updated procs/immortal commands etc...etc...

[b:lu225pzk]10/7/2008[/b:lu225pzk][list:lu225pzk]

[*:lu225pzk]fixed: druid shifting message. (act_c just isn't suitable in this scenario)[/*:m:lu225pzk]

[*:lu225pzk]fixed: evade capture message for player doing original web[/*:m:lu225pzk]

[*:lu225pzk]Fixed: mobs short being displayed during communications instead of name - my fault when i fixed the druid shift message...grrr bloody druid code[/*:m:lu225pzk]

[*:lu225pzk]Updated: replay can now use abbreviated channel names.. replay goss,replay sa etc[/*:m:lu225pzk]

[*:lu225pzk]Updated: replay buffer from 100 to MAX_ARG=160 as long messages were being truncated[/*:m:lu225pzk]

[*:lu225pzk]Fixed: a bunch of reported typos[/*:m:lu225pzk]

[*:lu225pzk]Fixed: ideas/typos/bugs to be useable whilst shifted[/*:m:lu225pzk]

[*:lu225pzk]Fixed: made sure deathblow damage can kill when mob has extremely low hitpoints e.g. stunned or incap, morted[/*:m:lu225pzk]

[*:lu225pzk]Updated: Perception to use darksight instead of infravision, significantly reduced the chance of blind, and increased its duration from 2 to 4 ticks[/*:m:lu225pzk][/list:u:lu225pzk]

[b:lu225pzk]13/7/2008[/b:lu225pzk][list:lu225pzk]

[*:lu225pzk]Fixed: godtitle crash bugs when used on mortals.[/*:m:lu225pzk][/list:u:lu225pzk]

[b:lu225pzk]17/7/2008[/b:lu225pzk][list:lu225pzk]

[*:lu225pzk]Changed: spellbook messages so that when prerequisites fail they are given a very basic hint.[/*:m:lu225pzk][/list:u:lu225pzk]

[b:lu225pzk]20/7/2008[/b:lu225pzk][list:lu225pzk]

[*:lu225pzk]reworked: all spell/skill help files for a similar look and feel[/*:m:lu225pzk]

[*:lu225pzk]Updated: help file tags to include - "Damage Type:" "Stratum:" "Save Versus:"[/*:m:lu225pzk]

[*:lu225pzk]Updated: skills/spells docs, made certain formatting is good[/*:m:lu225pzk][/list:u:lu225pzk]

[b:lu225pzk]22/7/2008[/b:lu225pzk][list:lu225pzk]

[*:lu225pzk]FIXED: press button in note vendor[/*:m:lu225pzk][/list:u:lu225pzk]

[b:lu225pzk]24/7/2008[/b:lu225pzk][list:lu225pzk]

[*:lu225pzk]fixed: homing scroll problem[/*:m:lu225pzk][/list:u:lu225pzk]

[b:lu225pzk]15/8/2008[/b:lu225pzk][list:lu225pzk]

[*:lu225pzk]fixed: some problems with non-existing items, after reloading the deleted object from rent file - i.e. player lost ALL eq[/*:m:lu225pzk]

[*:lu225pzk]Fixed: player rent file abondoning load if an oject has been deleted.  Loads object 14 (if it exists) instead and restrings it with detail of unloaded object

NOTE: if you get one of these objects normally you can just get rid of it, typically its because a potion/scroll was cloned unecessarily or removing old quest cps

Example: this is how it will appear in your inventory - "deleted game object 4000"[/*:m:lu225pzk][/list:u:lu225pzk]

[b:lu225pzk]31/8/2008[/b:lu225pzk][list:lu225pzk]

[*:lu225pzk]updated: saving of spells - reload now works for ac/regen type spells[/*:m:lu225pzk]

[*:lu225pzk]refactored: shapeshift & unshapeshift[/*:m:lu225pzk]

[*:lu225pzk]fixed: bug where shifting would cause hps to drift around.[/*:m:lu225pzk]

[*:lu225pzk]updated: shapeshift hp bonus based upon players druid class order[/*:m:lu225pzk]

[*:lu225pzk]refactored: innate/bought/class spells so they can use multiple affects to achieve a larger modifier value..e.g. mana=200 hitpoint=400[/*:m:lu225pzk]

[*:lu225pzk]refactored: practice - clearer error messages and now shows any skills transfered to shifted form, shows how many lessons completed[/*:m:lu225pzk]

[*:lu225pzk]fixed: innate spells so they don't shapeshift[/*:m:lu225pzk]

[*:lu225pzk]fixed: some innate spells/skills e.g. wtb on seadragon/climb cobra.[/*:m:lu225pzk]

[*:lu225pzk]updated: avatar shop limits increased for buying hp=400, mana=200, move=200[/*:m:lu225pzk]

[*:lu225pzk]fixed: score - bits missed when shapeshifted, added # of attacks calculation[/*:m:lu225pzk]

[*:lu225pzk]fixed: shapeshift imbues[/*:m:lu225pzk]

[*:lu225pzk]fixed: shapeshift light bug[/*:m:lu225pzk]

[*:lu225pzk]fixed: crash bug with shapeshift and magical lights[/*:m:lu225pzk]

[*:lu225pzk]fixed: shifted forms not being able to accept TEMP items (now they can be given to them)[/*:m:lu225pzk]

[*:lu225pzk]fixed: dispel of new spell types (see above) & shapeshift[/*:m:lu225pzk]

[*:lu225pzk]fixed: teleport spell on staff to work on shifted form[/*:m:lu225pzk]

[*:lu225pzk]fixed: supplicants to be generated if shifting before mob appears[/*:m:lu225pzk]

[*:lu225pzk]added: to imbue stacking of same spell instead of creating a new entry[/*:m:lu225pzk]

[*:lu225pzk]fixed: bug in claninsert where wrong color was  used to terminate the clan symbol[/*:m:lu225pzk]

[*:lu225pzk]fixed: drink bugged message order, when attempting to drink from a non drink container (e.g. a robe).[/*:m:lu225pzk]

[*:lu225pzk]fixed: 'group' list for longer player names.[/*:m:lu225pzk]

[*:lu225pzk]fixed: sacrifice - first checking floor for corpse not inventory (rather than other way around).[/*:m:lu225pzk]

[*:lu225pzk]fixed: clan symbol - so that leader can pick similar symbol to his own clan symbol[/*:m:lu225pzk]

[*:lu225pzk]added: move_bonus based upon dex to move_limit and move_gain[/*:m:lu225pzk]

[*:lu225pzk]added: move_bonus based upon martial classo and levels[/*:m:lu225pzk]

[*:lu225pzk]changed: moved eq/spell +move after other calculations as they were being inflated.[/*:m:lu225pzk]

[*:lu225pzk]added: immortal check to charm spell..in case shifted to something low[/*:m:lu225pzk]

[*:lu225pzk]changed: heightened succor to make 3-5 scrolls instead of a staff. (may add a staff as well..if enough interest)[/*:m:lu225pzk]

[*:lu225pzk]fixed: the mailmain proc to use CLR_TELL for its tells about 40+ entries altered[/*:m:lu225pzk][/list:u:lu225pzk]

[b:lu225pzk]1/9/2008[/b:lu225pzk][list:lu225pzk]

[*:lu225pzk]fixed teach/read spellbook bug..whereby no tool was required (if required)[/*:m:lu225pzk]

[*:lu225pzk]fixed some reception message colours as appropriate[/*:m:lu225pzk][/list:u:lu225pzk]

[b:lu225pzk]2/9/2008[/b:lu225pzk][list:lu225pzk]

[*:lu225pzk]fixed: bug - compact lines reversed[/*:m:lu225pzk]

[*:lu225pzk]fixed: bug - prac unlearned[/*:m:lu225pzk]

[*:lu225pzk]fixed: "upto" in score to "up to"

(bugs from restructuring)[/*:m:lu225pzk]

[*:lu225pzk]added: flurry to count of attacks[/*:m:lu225pzk][/list:u:lu225pzk]

[b:lu225pzk]4/9/2008[/b:lu225pzk][list:lu225pzk]

[*:lu225pzk]reworked: help file indexing so that advice now always shows the first keyword (from the left)[/*:m:lu225pzk]

[*:lu225pzk]updated: advice, output is now correctly sorted[/*:m:lu225pzk]

[*:lu225pzk]updated: shield of thorns spell hitpoints (about +30% maybe should be higher) + added avatar level element[/*:m:lu225pzk]

[*:lu225pzk]fixed: flee spam bug[/*:m:lu225pzk]

[*:lu225pzk]updated: tumbling duration to include avatar level element, (updated help which said lasted 1 round)[/*:m:lu225pzk]

[*:lu225pzk]fixed: bought charisma - wasn'tbeing applied to player[/*:m:lu225pzk]

[*:lu225pzk]fixed: a silly shop message[/*:m:lu225pzk]

[*:lu225pzk]fixed: new char bug - no newbie eq (aded during shapeshift restructure)[/*:m:lu225pzk]

[*:lu225pzk]fixed: shapeshift move bug (when wearing +mv spells/eq) like old hp bug but worse :-)[/*:m:lu225pzk][/list:u:lu225pzk]

[b:lu225pzk]6/9/2008[/b:lu225pzk][list:lu225pzk]

[*:lu225pzk]fixed: bug in bought reduced damage - was reapplying class level reduce damage[/*:m:lu225pzk][/list:u:lu225pzk]

[b:lu225pzk]7/9/2008[/b:lu225pzk][list:lu225pzk]

[*:lu225pzk]fixed: shifters with youth potions[/*:m:lu225pzk]

[*:lu225pzk]fixed: do_reading bug whereby active long duration conjunctions showed as 999[/*:m:lu225pzk]

[*:lu225pzk]fixed: bug in peri move message - it was checking for SPELL_DETECT_MAGIC instead of APPLY_DETECT_MAGIC, so bought spell wasn't working[/*:m:lu225pzk][/list:u:lu225pzk]

[b:lu225pzk]15/9/2008[/b:lu225pzk][list:lu225pzk]

[*:lu225pzk]fixed crash bug in check idling renting of morphed players[/*:m:lu225pzk]

[*:lu225pzk]fixed crash bug in transmute.  Reworked transmute to use the core of shapeshift and unshapeshift...which is more or less rock solid now.[/*:m:lu225pzk]

[*:lu225pzk]fixed the partial name bug in try_tells, changed order to check for partial pc before mob name, the same fix applied to [/*:m:lu225pzk]

[*:lu225pzk]changed: so shapeshifted players may now rent, technically it just unshapeshifts before renting...same underlying problem fixed as for the idling rent[/*:m:lu225pzk]

[*:lu225pzk]fixed: bought undead visage didn't work[/*:m:lu225pzk][/list:u:lu225pzk]

[b:lu225pzk]18/9/2008[/b:lu225pzk][list:lu225pzk]

[*:lu225pzk]changed: get all - to not give an error message to non takeable items[/*:m:lu225pzk]

[*:lu225pzk]added: the gremlin entry to supplication list[/*:m:lu225pzk]

[*:lu225pzk]fixed: unholy strength to not stack with demonic strength[/*:m:lu225pzk]

[*:lu225pzk]fixed: abbreviation of shopkeeper problem when using query[/*:m:lu225pzk]

[*:lu225pzk]changed: mount so dragon align check is less aggresive and same with dragon mount against levels[/*:m:lu225pzk]

[*:lu225pzk]changed: wear item - to show obj short instead of obj name[/*:m:lu225pzk]

[*:lu225pzk]fixed: order during logon of setting hps and loading eq, caused people to have to regen a few hps as the max hp was wrong[/*:m:lu225pzk]

[*:lu225pzk]changed: do_pick so ferret can pick without thief class[/*:m:lu225pzk]

[*:lu225pzk]fixed a practice bug whereby slowfall would be shown instead of slow[/*:m:lu225pzk][/list:u:lu225pzk]

[b:lu225pzk]20/9/2008[/b:lu225pzk][list:lu225pzk]

[*:lu225pzk]added: floor eater species can now drink from containers on the floor (i.e. not just fountains)[/*:m:lu225pzk]

[*:lu225pzk]fixed: circlestab confusing message whereby mob brushed away stab when <= sleep. put a unique message in about not being able to circle around someon[/*:m:lu225pzk]

[*:lu225pzk]reworked: stable so you can sell mounts at 1/2 price, you can buy upto 2 mounts and they will follow you, dismiss will allow them to go back home,rahter than destroying them  To sell they must be following you or you must be mounted..[/*:m:lu225pzk][/list:u:lu225pzk]

[b:lu225pzk]21/9/2008[/b:lu225pzk][list:lu225pzk]

[*:lu225pzk]fixed: detect magic spell to also use APPLY_DETECT_MAGIC as well as AFF_DETECT_MAGIC.[/*:m:lu225pzk]

[*:lu225pzk]fixed: made the supplication spell non-dispellable (the short one used for tracking whether enough sacs done)[/*:m:lu225pzk]

[*:lu225pzk]fixed: reception bug whereby 30 day rent waiver was being ignored (was just being capped at 7days)[/*:m:lu225pzk]

[*:lu225pzk]fixed: shops so that buying stuff will cause a save items/char (the order of events was wrong)[/*:m:lu225pzk]

[*:lu225pzk]fixed: kvp_forge to save char/items after completing a forge success & failure[/*:m:lu225pzk]

[*:lu225pzk]fixed: read/teach/student to save items/char/config after successful completion[/*:m:lu225pzk][/list:u:lu225pzk]

</div>
