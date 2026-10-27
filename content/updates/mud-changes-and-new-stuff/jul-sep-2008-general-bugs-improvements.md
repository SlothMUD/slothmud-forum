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

Here are the code fixes/changes I've made since July up September... this list only includes ones that the player is likely to notice. Of course there are about 400% more changes than the ones listed below that are to do with the overall maintenance of the system,new/updated procs/immortal commands etc...etc...

<strong>10/7/2008</strong>

- fixed: druid shifting message. (act\_c just isn't suitable in this scenario)
- fixed: evade capture message for player doing original web
- Fixed: mobs short being displayed during communications instead of name - my fault when i fixed the druid shift message...grrr bloody druid code
- Updated: replay can now use abbreviated channel names.. replay goss,replay sa etc
- Updated: replay buffer from 100 to MAX\_ARG=160 as long messages were being truncated
- Fixed: a bunch of reported typos
- Fixed: ideas/typos/bugs to be useable whilst shifted
- Fixed: made sure deathblow damage can kill when mob has extremely low hitpoints e.g. stunned or incap, morted
- Updated: Perception to use darksight instead of infravision, significantly reduced the chance of blind, and increased its duration from 2 to 4 ticks

<strong>13/7/2008</strong>

- Fixed: godtitle crash bugs when used on mortals.

<strong>17/7/2008</strong>

- Changed: spellbook messages so that when prerequisites fail they are given a very basic hint.

<strong>20/7/2008</strong>

- reworked: all spell/skill help files for a similar look and feel
- Updated: help file tags to include - "Damage Type:" "Stratum:" "Save Versus:"
- Updated: skills/spells docs, made certain formatting is good

<strong>22/7/2008</strong>

- FIXED: press button in note vendor

<strong>24/7/2008</strong>

- fixed: homing scroll problem

<strong>15/8/2008</strong>

- fixed: some problems with non-existing items, after reloading the deleted object from rent file - i.e. player lost ALL eq
- Fixed: player rent file abondoning load if an oject has been deleted. Loads object 14 (if it exists) instead and restrings it with detail of unloaded object

NOTE: if you get one of these objects normally you can just get rid of it, typically its because a potion/scroll was cloned unecessarily or removing old quest cps

Example: this is how it will appear in your inventory - "deleted game object 4000"

<strong>31/8/2008</strong>

- updated: saving of spells - reload now works for ac/regen type spells
- refactored: shapeshift \& unshapeshift
- fixed: bug where shifting would cause hps to drift around.
- updated: shapeshift hp bonus based upon players druid class order
- refactored: innate/bought/class spells so they can use multiple affects to achieve a larger modifier value..e.g. mana=200 hitpoint=400
- refactored: practice - clearer error messages and now shows any skills transfered to shifted form, shows how many lessons completed
- fixed: innate spells so they don't shapeshift
- fixed: some innate spells/skills e.g. wtb on seadragon/climb cobra.
- updated: avatar shop limits increased for buying hp=400, mana=200, move=200
- fixed: score - bits missed when shapeshifted, added # of attacks calculation
- fixed: shapeshift imbues
- fixed: shapeshift light bug
- fixed: crash bug with shapeshift and magical lights
- fixed: shifted forms not being able to accept TEMP items (now they can be given to them)
- fixed: dispel of new spell types (see above) \& shapeshift
- fixed: teleport spell on staff to work on shifted form
- fixed: supplicants to be generated if shifting before mob appears
- added: to imbue stacking of same spell instead of creating a new entry
- fixed: bug in claninsert where wrong color was used to terminate the clan symbol
- fixed: drink bugged message order, when attempting to drink from a non drink container (e.g. a robe).
- fixed: 'group' list for longer player names.
- fixed: sacrifice - first checking floor for corpse not inventory (rather than other way around).
- fixed: clan symbol - so that leader can pick similar symbol to his own clan symbol
- added: move\_bonus based upon dex to move\_limit and move\_gain
- added: move\_bonus based upon martial classo and levels
- changed: moved eq/spell +move after other calculations as they were being inflated.
- added: immortal check to charm spell..in case shifted to something low
- changed: heightened succor to make 3-5 scrolls instead of a staff. (may add a staff as well..if enough interest)
- fixed: the mailmain proc to use CLR\_TELL for its tells about 40+ entries altered

<strong>1/9/2008</strong>

- fixed teach/read spellbook bug..whereby no tool was required (if required)
- fixed some reception message colours as appropriate

<strong>2/9/2008</strong>

- fixed: bug - compact lines reversed
- fixed: bug - prac unlearned
- fixed: "upto" in score to "up to"

(bugs from restructuring)
- added: flurry to count of attacks

<strong>4/9/2008</strong>

- reworked: help file indexing so that advice now always shows the first keyword (from the left)
- updated: advice, output is now correctly sorted
- updated: shield of thorns spell hitpoints (about +30% maybe should be higher) + added avatar level element
- fixed: flee spam bug
- updated: tumbling duration to include avatar level element, (updated help which said lasted 1 round)
- fixed: bought charisma - wasn'tbeing applied to player
- fixed: a silly shop message
- fixed: new char bug - no newbie eq (aded during shapeshift restructure)
- fixed: shapeshift move bug (when wearing +mv spells/eq) like old hp bug but worse <img src="/images/smilies/icon_e_smile.svg" alt=":-)" title=":-)" width="15" height="15" class="smiley nozoom">

<strong>6/9/2008</strong>

- fixed: bug in bought reduced damage - was reapplying class level reduce damage

<strong>7/9/2008</strong>

- fixed: shifters with youth potions
- fixed: do\_reading bug whereby active long duration conjunctions showed as 999
- fixed: bug in peri move message - it was checking for SPELL\_DETECT\_MAGIC instead of APPLY\_DETECT\_MAGIC, so bought spell wasn't working

<strong>15/9/2008</strong>

- fixed crash bug in check idling renting of morphed players
- fixed crash bug in transmute. Reworked transmute to use the core of shapeshift and unshapeshift...which is more or less rock solid now.
- fixed the partial name bug in try\_tells, changed order to check for partial pc before mob name, the same fix applied to 
- changed: so shapeshifted players may now rent, technically it just unshapeshifts before renting...same underlying problem fixed as for the idling rent
- fixed: bought undead visage didn't work

<strong>18/9/2008</strong>

- changed: get all - to not give an error message to non takeable items
- added: the gremlin entry to supplication list
- fixed: unholy strength to not stack with demonic strength
- fixed: abbreviation of shopkeeper problem when using query
- changed: mount so dragon align check is less aggresive and same with dragon mount against levels
- changed: wear item - to show obj short instead of obj name
- fixed: order during logon of setting hps and loading eq, caused people to have to regen a few hps as the max hp was wrong
- changed: do\_pick so ferret can pick without thief class
- fixed a practice bug whereby slowfall would be shown instead of slow

<strong>20/9/2008</strong>

- added: floor eater species can now drink from containers on the floor (i.e. not just fountains)
- fixed: circlestab confusing message whereby mob brushed away stab when \<= sleep. put a unique message in about not being able to circle around someon
- reworked: stable so you can sell mounts at 1/2 price, you can buy upto 2 mounts and they will follow you, dismiss will allow them to go back home,rahter than destroying them To sell they must be following you or you must be mounted..

<strong>21/9/2008</strong>

- fixed: detect magic spell to also use APPLY\_DETECT\_MAGIC as well as AFF\_DETECT\_MAGIC.
- fixed: made the supplication spell non-dispellable (the short one used for tracking whether enough sacs done)
- fixed: reception bug whereby 30 day rent waiver was being ignored (was just being capped at 7days)
- fixed: shops so that buying stuff will cause a save items/char (the order of events was wrong)
- fixed: kvp\_forge to save char/items after completing a forge success \& failure
- fixed: read/teach/student to save items/char/config after successful completion

</div>
