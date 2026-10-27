---
title: "Oct-Dec 2007: General Bugs/Improvements"
topic_id: 2931
author: "Judge"
date: 2008-09-24T10:29:45+00:00
last_activity: 2008-09-24T10:29:45+00:00
last_author: "Judge"
sticky: false
locked: false
post_count: 1
---

<div class="post" data-post-id="26451" data-author="Judge" data-date="2008-09-24T10:29:45+00:00" data-subject="Oct-Dec 2007: General Bugs/Improvements">

Be warned the following is a little long, it is a log of the changes I made during this period...obviously I've removed anything that could be considered immortal information or that relates to general improvements to the code...basically stuff that you shouldn't notice.

 

<strong>23/10/2007</strong>

- removed: 'the' article from dismount as it will be contained in the mobs short name
- fixed: \*\*Spud[44188\]: Acme carves up the the corpse of a knight of crystal ... missing fullstop
- Fixed: \*\*Broeggle[15156\]: Ok. You will now try to catch an silvery arrow. - in this case it is a silvery arrow
- Fixed: \*\*Spud[37182\]: A male black dragon looks down in terror as a lone, sharp scale falls to the ground !...no space before exlaimation
- Fixed: \*\*Spud[69279\]: Krok swears vehemently and at great length, singing your eyebrows!..spammage
- Fixed: the warcry plummet message was innacurate (referring to the leader)
- Fixed: \*\*Spud[69200\]: The ship captain shouts 'The ship's been delayed a couple hours because of that idiot Minstrel! We are truly sorry!'...line spammage
- Fixed: \*\*Spud[89312\]: message is wrong, and in wrong order ... Ornate glass bottle disappears suddenly! Truth opens an ornate
- Fixed: \*\*Slice[14049\]: in 'practice unl' for skills 'Unlearned' needs another space before
- Fixed: \*\*Spud[89906\]: the alignment of columns in 'spells' is kinda messy

<strong>24/10/2007</strong>

- fixed: weird unlock message when no door name
- Fixed: updated the apply poison messages. \*\*Slice[66260\]: when extracting poison vial tell player
- fixed message errors in apply poison and examine weapon with poison
- fixed messages: \*\*Verin[37193\]: "Your a dark mace disintegrates and blows away." don't need "a" dark mace
- fixed: \*\*Verin[99164\]: Rub casts 'curse', followed by "Your curse starts going awry, but you concentrate and complete it!"
- Fixed: \*\*Slice[8180\]: info if drachma value show that in identity instead of value
- Fixed: \*\*Slice[8180\]: Red Moran tells you 'I'm too low on drachma right now to buy such things.' The Dream Weaver tells you 'How do I know that isn't stolen? Too risky for m
- Fixed \*\*Spud[9903\]: Your awareness of the surroundings beings to dull...when using kenning...should be begins...or just dulls if it has ended
- Fixed: \*\*Necrad[35851\]: Woooof, you feel exhausted!. - haste down message needs a little fixing

<strong>25/10/2007</strong>

- added: Possesive Prounoun $V its, his, hers, theirs
- added: Present Continuous $R it's, he's, she's, they're
- updated: 11 usages of $E's with $R (only in code)
- Fixed: \*\*Falwell[26403\]: subdue bats, They's still moving, beat them down a little first!
- Fixed: Fixed many his/her in code as $s
- added: add present perfect macro HSTV $V it's\|he's\|she's\|they've
- removed: many extra newline
- Fixed: \*\*Spud[37165\]: With a twist of the wrist, Cocaine rolls a 48.to many new lines
- fixed: \*\*Eta[11211\]: Room or area echo has 'The storm errupts into a violent hurricane flinging debris everywhere.', that should have 'erupts'
- Fixed: \*\*Eta[34295\]: In score stat I see 'Your skill at controlling the undead is a source of amusement for all..' That should have one '.', not two.
- fixed web messages
- Fixed: \*\*Verin[77093\]: Uthral webbing Rub, who has rweb up and is using evape capture to toss them, it says The silk webbing simply falls to the ground, as Rub is already webb
- Fixed: \*\*Verin[26463\]: The silk webbing simply falls to the ground, as Rub is already webbed! the mob was webbed, not Rub, using evade capture
- fixed: \*\*Eta[4211\]: The line 'Your hands glow as you touch Eta' needs an ending period.
- fixed: \*\*Elan[37169\]: Two mirror image of Syl waver into existence.
- Fixed message \*\*Hotara[12147\]: vengeance proc You sense the immediate presense of evil!
- Fixed \*\*Sita[22450\]: lyme mayr needs period: I have work to do don't waste my time. should be: I have work to do. Don't waste my time.
- Fixed: \*\*Risk[43907\]: Your armor of pRetrified bones, should be petrified
- Fixed: \*\*Risk[43907\]: string when petrified armor spell falls

<strong>26/10/2007</strong>

- Fixed: added missing \\n\\r from exa spellbook messages
- fixed: \*\*Polk[89386\]: This item is much to holy! ...nice typo
- fixed: \*\*Tir[2421\]: the Holy Sword of Balrog crumbles to dust!, "the" is not capd
- fixed: \*\*Blade[30425\]: The Grand Magus gossips-- 'Congratulations Blade, has reach his 40th level in his third class!'
- fixed: \*\*Slice[38898\]: A green mist envelops the corpse of a naga. ..should use object colour

<strong>28/10/2007</strong>

- Added: several new liquids
- Fixed: shop item colors
- Fixed: forge list colors and made to look like a shop list
- FIXED: - check taste/sip code for poison and spit out if poisoned.
- FIXed: - Spud[9903\]: reminder to judge .. fix damn 2nd forge same-name issue affecting helm
- Fixed: \*\*Blade[9998\]: A sad little gypsy girl tells you 'I don't of anybody questing around these parts.'
- Fixed: \*\*Cambria[8175\]: The Dream Weaver tells you 'I don't of anybody questing around these parts.'

<strong>30/10/2007</strong>

- added: $h $H honorific

<strong>01/11/2007</strong>

- added: ripples message to room when in peri room with "detect magic"
- added: fail to pick to lock messages
- added: IDEA - walk north bounce into wall - Slice walks headfirst into a wall/door
- updated: min position on various commands
- fixed: copied prompt \& channel during shapeshift

<strong>05/11/2007</strong>

- fixed: drinking and sipping takes on more liquid
- fixed: FULL stomach is now at 34 for eating and drinking

<strong>06/11/2007</strong>

- fixed: a problem with drinnking when full
- added: do\_puke to allow players to become bulemic
- fixed: harder to puke when drunk
- fixed: harder to miss face when drunk
- updated: gorge to include drinking from stuff
- fixed: weight\_change\_object() to prevent negative weight

<strong>07/11/2007</strong>

- Added: liquids LIQ\_GUAVAJUICE, LIQ\_ORANGEJUICE, LIQ\_AXELGREASE, LIQ\_CIDER, LIQ\_VODKA, LIQ\_MIRUVOR, LIQ\_ORCLIQUOR, LIQ\_ENTDRAUGHT
- fixed: vomit now calls do\_puke
- fully implemented affects from drinks
- gorge now operates from the eat\_object function
- fixed: gorge bug, where by if filled the thirst condition first couldn't eat further
- fixed: gorge bug, where by too much was drunk during non-super\_gorge
- fixed: gorge bug, where by entire drink container would be emptied even if not necessary
- fixed: colours in stable shops(mob colour animals)

<strong>08/11/2007</strong>

- fixed: Fixed dreamtalk spell to use decorate\_message
- updated: the drunk messages in score so you can determine how drunk one is
- fixed: made it harder to puke from over indulging
- added: allow drink/eat when you see the message starting to get hungry/thirsty in score
- changed: the fail drink messages slightly
- fixed: reduced chance of missing mouth when drunk

<strong>09/11/2007</strong>

- fixed: incubation of vampirism issue with eating/drinking
- added: white/rose wine and champagne (same stats as redwine but diff colour)
- fixed: increased alcohol level for the spirit drinks

<strong>10/11/2007</strong>

- fixed: When puking a pool of sick appears (is food, if player is poisoned will be poisoned)
- Added: creatures who can eat food directly from the floor
- fixed: tweaked alcoholia and hyperoveractivity to be slightly less aggressive
- fixed: made incubating vampirism message far less prevalent

<strong>11/11/2007</strong>

- fixed: vastly reduced chance of mistell when drunk (considering new scale)
- fixed: mistel chance is now caped at above 30points drunk scale is 0-127
- fixed: Added puke object to drunk drinking
- Fixed: bug in the hunger/thirst not reducing on non-gorging characters
- fixed: During gorge from floor check the object can be picked up
- added: caffeinated coffee/coke/tea and cream

<strong>12/11/2007</strong>

- fixed: bug whereby drunk wouldn't fall below 20 under natural circumstances

<strong>13/11/2007</strong>

- Fixed: crash bug with holy eq and shifted players
- Removed: point check when doing an entrench
- fixed: issue with extracting objects and shapeshifters, shapeshifted player will get a message although their character actually had it.. no one else will see message as obj not in room
- fixed: crash bug on removing holy eq
- fixed: the order of holy item crumble parameters so message doesn't show (NULL)

<strong>15/11/2007</strong>

- added: completed the improved bump message system

<strong>16/11/2007</strong>

- Fixed: the vampire incubation so that incubation ends as soon as the craving message is seen
- added: Finished the improved random bump messages

<strong>18/11/2007</strong>

- FIXED: Ah gossips-- 'shouldnt be able to gorge all the food from suppy, shop'
- fixed: reduced the chance of a mild headache messages in last 5minutes of alcohalia

<strong>19/11/2007</strong>

- fixed: grouptell bug for the leader
- fixed: bug in partial name use in tell
- improved: the partial name useage in try\_tell
- CHANGED: can't toss or be tossed when greased up
- Added: wait state to remove all/wear all dependent on what you wear and remove (some will hate this!)
- changed: Severly lowered the wait state on wear/remove single items (some will love this!) ... Basically this is much fairer
- fixed: breaking wall of flesh after shapeshift return..msg is shown for extracting shapeshift mob

<strong>20/11/2007</strong>

- fixed: issue ezekiel raised regarding stealth and oneself..yup my fault

<strong>22/11/2007</strong>

- Added: springwater, iced water drinks
- Fixed: broken dead tells (my fault)
- Fixed: brothers in valor check on deathgrip and deathtouch
- fixed: nan error in score

<strong>01/12/2007</strong>

- Updated: ask better error handling
- Updated: query better error handling, and improved support for shop/forge
- Updated: clan title checking
- added: title to allow %s which will automatically use clan symbol even when changed
- Fixed: track to use the newly calculated lag and not PULSE\_VIOLENCE. (makes it faster and more useful)
- Added: rum liquid
- Fixed: liquid mixing (mixing diff waters no longer makes slime), also made it more dynamic for future mixing
- Updated: pour/fill/create water to use new mix\_liquids()
- Fixed: poison check when filling from poisoned fountain, allowed filling from carried fountain
- Fixed: can't gorge steal unless you've learnt steal, can't gorge from mobs or immortals
- Fixed: pour to work from carried fountains
- Changed: remove all lag 50%, wear all lag 75%
- Fixed: typo in order skitzofreni is schizophrenia
- Fixed: squirm to work properly with violation/ended of noexits
- Fixed: make\_prompt() \*\*\* Press return \*\*\* to be terminated by CLR\_STATUS
- Fixed: dark cloak to work like a broken darkness again
- Added: brownie supplication
- Changed: query shopkeeper to charge 2k coins if \>20 instead of refusing with a stupid reason
- Fixed: crash bug in sun cycler.. when mob runs out of mana
- Added: kvp\_forge to allow query on nth items in list esp if same result, addiontally shows if cps can be seen in query needs SHOWCPS[n]
- Changed: kvp\_forge list to show same checks as shop list, addiontally shows if cps can be seen in query needs SHOWCPS[n]
- fixed: clan title in "rank who"
- fixed: pouring from container/fountain
- fixed: when removing/wearing eq the maxhp\&maxmana are updated immediately rather than waiting for the fast\_point\_update so that the prompt appears correctly
- fixed: the eq remove/wear lag by using SET\_WAIT\_STATEinstead of WAIT\_STATE which was adding the value...arrrghhh
- fixed: reset of some point values after eq is loaded (caused stacking)

<strong>02/12/2007</strong>

- fixed: a couple of insert of clan symbol which had been forgotten

<strong>03/12/2007</strong>

- added cocktail, holy water, herbal tea

<strong>05/12/2007</strong>

- changed: wear all lag to 50% of total
- added: remove\_many/wear\_many to process removal/wearing of multiple items covered by concise but faster than removing all/wearing all
- Fixed: crash bug where by if title is loaded from pfile as null set it back to untitled

<strong>06/12/2007</strong>

- fixed: crash bug - on removal of ITEM\_TMP objects .. my fault
- fixed: bug - wilo the wisp, spell was assigned to the wrong slot

</div>
