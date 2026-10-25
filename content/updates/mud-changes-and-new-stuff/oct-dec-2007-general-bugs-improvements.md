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

 

 

[b:xhqjlggl]23/10/2007[/b:xhqjlggl][list:xhqjlggl]

[*:xhqjlggl]removed: 'the' article from dismount as it will be contained in the mobs short name[/*:m:xhqjlggl]

[*:xhqjlggl]fixed: **Spud[44188]: Acme carves up the the corpse of a knight of crystal ... missing fullstop[/*:m:xhqjlggl]

[*:xhqjlggl]Fixed: **Broeggle[15156]: Ok.  You will now try to catch an silvery arrow. - in this case it is a silvery arrow[/*:m:xhqjlggl]

[*:xhqjlggl]Fixed: **Spud[37182]: A male black dragon looks down in terror as a lone, sharp scale falls to the ground !...no space before exlaimation[/*:m:xhqjlggl]

[*:xhqjlggl]Fixed: **Spud[69279]: Krok swears vehemently and at great length, singing your eyebrows!..spammage[/*:m:xhqjlggl]

[*:xhqjlggl]Fixed: the warcry plummet message was innacurate (referring to the leader)[/*:m:xhqjlggl]

[*:xhqjlggl]Fixed: **Spud[69200]: The ship captain shouts 'The ship's been delayed a couple hours because of that idiot Minstrel! We are truly sorry!'...line spammage[/*:m:xhqjlggl]

[*:xhqjlggl]Fixed: **Spud[89312]: message is wrong, and in wrong order ... Ornate glass bottle disappears suddenly! Truth opens an ornate[/*:m:xhqjlggl]

[*:xhqjlggl]Fixed: **Slice[14049]: in 'practice unl' for skills 'Unlearned' needs another space before[/*:m:xhqjlggl]

[*:xhqjlggl]Fixed: **Spud[89906]: the alignment of columns in 'spells' is kinda messy[/*:m:xhqjlggl][/list:u:xhqjlggl]

 

[b:xhqjlggl]24/10/2007[/b:xhqjlggl][list:xhqjlggl]

[*:xhqjlggl]fixed: weird unlock message when no door name[/*:m:xhqjlggl]

[*:xhqjlggl]Fixed: updated the apply poison messages. **Slice[66260]: when extracting poison vial tell player[/*:m:xhqjlggl]

[*:xhqjlggl]fixed message errors in apply poison and examine weapon with poison[/*:m:xhqjlggl]

[*:xhqjlggl]fixed messages: **Verin[37193]: "Your a dark mace disintegrates and blows away."   don't need "a" dark mace[/*:m:xhqjlggl]

[*:xhqjlggl]fixed: **Verin[99164]: Rub casts 'curse', followed by "Your curse starts going awry, but you concentrate and complete it!"[/*:m:xhqjlggl]

[*:xhqjlggl]Fixed: **Slice[8180]: info if drachma value show that in identity instead of value[/*:m:xhqjlggl]

[*:xhqjlggl]Fixed: **Slice[8180]: Red Moran tells you 'I'm too low on drachma right now to buy such things.' The Dream Weaver tells you 'How do I know that isn't stolen?  Too risky for m[/*:m:xhqjlggl]

[*:xhqjlggl]Fixed **Spud[9903]: Your awareness of the surroundings beings to dull...when using kenning...should be begins...or just dulls if it has ended[/*:m:xhqjlggl]

[*:xhqjlggl]Fixed: **Necrad[35851]: Woooof, you feel exhausted!. - haste down message needs a little fixing[/*:m:xhqjlggl][/list:u:xhqjlggl]

 

[b:xhqjlggl]25/10/2007[/b:xhqjlggl][list:xhqjlggl]

[*:xhqjlggl]added: Possesive Prounoun $V its, his, hers, theirs[/*:m:xhqjlggl]

[*:xhqjlggl]added: Present Continuous $R it's, he's, she's, they're[/*:m:xhqjlggl]

[*:xhqjlggl]updated: 11 usages of $E's with $R (only in code)[/*:m:xhqjlggl]

[*:xhqjlggl]Fixed: **Falwell[26403]: subdue bats, They's still moving, beat them down a little first![/*:m:xhqjlggl]

[*:xhqjlggl]Fixed: Fixed many his/her in code as $s[/*:m:xhqjlggl]

[*:xhqjlggl]added: add present perfect macro HSTV $V it's|he's|she's|they've[/*:m:xhqjlggl]

[*:xhqjlggl]removed: many extra newline[/*:m:xhqjlggl]

[*:xhqjlggl]Fixed: **Spud[37165]: With a twist of the wrist, Cocaine rolls a 48.to many new lines[/*:m:xhqjlggl]

[*:xhqjlggl]fixed: **Eta[11211]: Room or area echo has 'The storm errupts into a violent hurricane flinging  debris everywhere.', that should have 'erupts'[/*:m:xhqjlggl]

[*:xhqjlggl]Fixed: **Eta[34295]: In score stat I see 'Your skill at controlling the undead is a source of  amusement for all..' That should have one '.', not two.[/*:m:xhqjlggl]

[*:xhqjlggl]fixed web messages[/*:m:xhqjlggl]

[*:xhqjlggl]Fixed: **Verin[77093]: Uthral webbing Rub, who has rweb up and is using evape capture to toss them, it says The silk webbing simply falls to the ground, as Rub is already webb[/*:m:xhqjlggl]

[*:xhqjlggl]Fixed: **Verin[26463]: The silk webbing simply falls to the ground, as Rub is already webbed!  the mob was webbed, not Rub, using evade capture[/*:m:xhqjlggl]

[*:xhqjlggl]fixed: **Eta[4211]: The line 'Your hands glow as you touch Eta' needs an ending period.[/*:m:xhqjlggl]

[*:xhqjlggl]fixed: **Elan[37169]: Two mirror image of Syl waver into existence.[/*:m:xhqjlggl]

[*:xhqjlggl]Fixed message **Hotara[12147]: vengeance proc You sense the immediate presense of evil![/*:m:xhqjlggl]

[*:xhqjlggl]Fixed **Sita[22450]: lyme mayr needs period: I have work to do don't waste my time. should be: I have work to do. Don't waste my time.[/*:m:xhqjlggl]

[*:xhqjlggl]Fixed: **Risk[43907]: Your armor of pRetrified bones, should be petrified[/*:m:xhqjlggl]

[*:xhqjlggl]Fixed: **Risk[43907]: string when petrified armor spell falls[/*:m:xhqjlggl][/list:u:xhqjlggl]

 

[b:xhqjlggl]26/10/2007[/b:xhqjlggl][list:xhqjlggl]

[*:xhqjlggl]Fixed: added missing \n\r from exa spellbook messages[/*:m:xhqjlggl]

[*:xhqjlggl]fixed: **Polk[89386]: This item is much to holy!    ...nice typo[/*:m:xhqjlggl]

[*:xhqjlggl]fixed: **Tir[2421]: the Holy Sword of Balrog crumbles to dust!, "the" is not capd[/*:m:xhqjlggl]

[*:xhqjlggl]fixed: **Blade[30425]: The Grand Magus gossips-- 'Congratulations Blade, has reach his 40th level in his third class!'[/*:m:xhqjlggl]

[*:xhqjlggl]fixed: **Slice[38898]: A green mist envelops the corpse of a naga. ..should use object colour[/*:m:xhqjlggl][/list:u:xhqjlggl]

 

[b:xhqjlggl]28/10/2007[/b:xhqjlggl][list:xhqjlggl]

[*:xhqjlggl]Added: several new liquids[/*:m:xhqjlggl]

[*:xhqjlggl]Fixed: shop item colors[/*:m:xhqjlggl]

[*:xhqjlggl]Fixed: forge list colors and made to look like a shop list[/*:m:xhqjlggl]

[*:xhqjlggl]FIXED: - check taste/sip code for poison and spit out if poisoned.[/*:m:xhqjlggl]

[*:xhqjlggl]FIXed: - Spud[9903]: reminder to judge .. fix damn 2nd forge same-name issue affecting helm[/*:m:xhqjlggl]

[*:xhqjlggl]Fixed: **Blade[9998]: A sad little gypsy girl tells you 'I don't of anybody questing around these parts.'[/*:m:xhqjlggl]

[*:xhqjlggl]Fixed: **Cambria[8175]: The Dream Weaver tells you 'I don't of anybody questing around these parts.'[/*:m:xhqjlggl][/list:u:xhqjlggl]

 

[b:xhqjlggl]30/10/2007[/b:xhqjlggl][list:xhqjlggl]

[*:xhqjlggl]added: $h $H honorific[/*:m:xhqjlggl][/list:u:xhqjlggl]

 

[b:xhqjlggl]01/11/2007[/b:xhqjlggl][list:xhqjlggl]

[*:xhqjlggl]added: ripples message to room when in peri room with "detect magic"[/*:m:xhqjlggl]

[*:xhqjlggl]added: fail to pick to lock messages[/*:m:xhqjlggl]

[*:xhqjlggl]added: IDEA - walk north bounce into wall - Slice walks headfirst into a wall/door[/*:m:xhqjlggl]

[*:xhqjlggl]updated: min position on various commands[/*:m:xhqjlggl]

[*:xhqjlggl]fixed: copied prompt & channel during shapeshift[/*:m:xhqjlggl][/list:u:xhqjlggl]

[b:xhqjlggl]05/11/2007[/b:xhqjlggl][list:xhqjlggl]

[*:xhqjlggl]fixed: drinking and sipping takes on more liquid[/*:m:xhqjlggl]

[*:xhqjlggl]fixed: FULL stomach is now at 34 for eating and drinking[/*:m:xhqjlggl][/list:u:xhqjlggl]

 

[b:xhqjlggl]06/11/2007[/b:xhqjlggl][list:xhqjlggl]

[*:xhqjlggl]fixed:  a problem with drinnking when full[/*:m:xhqjlggl]

[*:xhqjlggl]added: do_puke to allow players to become bulemic[/*:m:xhqjlggl]

[*:xhqjlggl]fixed: harder to puke when drunk[/*:m:xhqjlggl]

[*:xhqjlggl]fixed: harder to miss face when drunk[/*:m:xhqjlggl]

[*:xhqjlggl]updated: gorge to include drinking from stuff[/*:m:xhqjlggl]

[*:xhqjlggl]fixed: weight_change_object() to prevent negative weight[/*:m:xhqjlggl][/list:u:xhqjlggl]

 

[b:xhqjlggl]07/11/2007[/b:xhqjlggl][list:xhqjlggl]

[*:xhqjlggl]Added: liquids LIQ_GUAVAJUICE, LIQ_ORANGEJUICE, LIQ_AXELGREASE, LIQ_CIDER, LIQ_VODKA, LIQ_MIRUVOR, LIQ_ORCLIQUOR, LIQ_ENTDRAUGHT[/*:m:xhqjlggl]

[*:xhqjlggl]fixed: vomit now calls do_puke[/*:m:xhqjlggl]

[*:xhqjlggl]fully implemented affects from drinks[/*:m:xhqjlggl]

[*:xhqjlggl]gorge now operates from the eat_object function[/*:m:xhqjlggl]

[*:xhqjlggl]fixed: gorge bug, where by if filled the thirst condition first couldn't eat further[/*:m:xhqjlggl]

[*:xhqjlggl]fixed: gorge bug, where by too much was drunk during non-super_gorge[/*:m:xhqjlggl]

[*:xhqjlggl]fixed: gorge bug, where by entire drink container would be emptied even if not necessary[/*:m:xhqjlggl]

[*:xhqjlggl]fixed: colours in stable shops(mob colour animals)[/*:m:xhqjlggl][/list:u:xhqjlggl]

[b:xhqjlggl]08/11/2007[/b:xhqjlggl][list:xhqjlggl]

[*:xhqjlggl]fixed: Fixed dreamtalk spell to use decorate_message[/*:m:xhqjlggl]

[*:xhqjlggl]updated: the drunk messages in score so you can determine how drunk one is[/*:m:xhqjlggl]

[*:xhqjlggl]fixed: made it harder to puke from over indulging[/*:m:xhqjlggl]

[*:xhqjlggl]added: allow drink/eat when you see the message starting to get hungry/thirsty in score[/*:m:xhqjlggl]

[*:xhqjlggl]changed: the fail drink messages slightly[/*:m:xhqjlggl]

[*:xhqjlggl]fixed: reduced chance of missing mouth when drunk[/*:m:xhqjlggl][/list:u:xhqjlggl]

 

[b:xhqjlggl]09/11/2007[/b:xhqjlggl][list:xhqjlggl]

[*:xhqjlggl]fixed: incubation of vampirism issue with eating/drinking[/*:m:xhqjlggl]

[*:xhqjlggl]added: white/rose wine and champagne (same stats as redwine but diff colour)[/*:m:xhqjlggl]

[*:xhqjlggl]fixed: increased alcohol level for the spirit drinks[/*:m:xhqjlggl][/list:u:xhqjlggl]

[b:xhqjlggl]10/11/2007[/b:xhqjlggl][list:xhqjlggl]

[*:xhqjlggl]fixed: When puking a pool of sick appears (is food, if player is poisoned will be poisoned)[/*:m:xhqjlggl]

[*:xhqjlggl]Added: creatures who can eat food directly from the floor[/*:m:xhqjlggl]

[*:xhqjlggl]fixed: tweaked alcoholia and hyperoveractivity to be slightly less aggressive[/*:m:xhqjlggl]

[*:xhqjlggl]fixed: made incubating vampirism message far less prevalent[/*:m:xhqjlggl][/list:u:xhqjlggl]

[b:xhqjlggl]11/11/2007[/b:xhqjlggl][list:xhqjlggl]

[*:xhqjlggl]fixed: vastly reduced chance of mistell when drunk (considering new scale)[/*:m:xhqjlggl]

[*:xhqjlggl]fixed: mistel chance is now caped at above 30points drunk scale is 0-127[/*:m:xhqjlggl]

[*:xhqjlggl]fixed: Added puke object to drunk drinking[/*:m:xhqjlggl]

[*:xhqjlggl]Fixed: bug in the hunger/thirst not reducing on non-gorging characters[/*:m:xhqjlggl]

[*:xhqjlggl]fixed: During gorge from floor check the object can be picked up[/*:m:xhqjlggl]

[*:xhqjlggl]added: caffeinated coffee/coke/tea and cream[/*:m:xhqjlggl][/list:u:xhqjlggl]

 

[b:xhqjlggl]12/11/2007[/b:xhqjlggl][list:xhqjlggl]

[*:xhqjlggl]fixed: bug whereby drunk wouldn't fall below 20 under natural circumstances[/*:m:xhqjlggl][/list:u:xhqjlggl]

[b:xhqjlggl]13/11/2007[/b:xhqjlggl][list:xhqjlggl]

[*:xhqjlggl]Fixed: crash bug with holy eq and shifted players[/*:m:xhqjlggl]

[*:xhqjlggl]Removed: point check when doing an entrench[/*:m:xhqjlggl]

[*:xhqjlggl]fixed: issue with extracting objects and shapeshifters, shapeshifted player will get a message although their character actually had it.. no one else will see message as obj not in room[/*:m:xhqjlggl]

[*:xhqjlggl]fixed: crash bug on removing holy eq[/*:m:xhqjlggl]

[*:xhqjlggl]fixed: the order of holy item crumble parameters so message doesn't show (NULL)[/*:m:xhqjlggl][/list:u:xhqjlggl]

[b:xhqjlggl]15/11/2007[/b:xhqjlggl][list:xhqjlggl]

[*:xhqjlggl]added: completed the improved bump message system[/*:m:xhqjlggl][/list:u:xhqjlggl]

 

[b:xhqjlggl]16/11/2007[/b:xhqjlggl][list:xhqjlggl]

[*:xhqjlggl]Fixed: the vampire incubation so that incubation ends as soon as the craving message is seen[/*:m:xhqjlggl]

[*:xhqjlggl]added: Finished the improved random bump messages[/*:m:xhqjlggl][/list:u:xhqjlggl]

 

[b:xhqjlggl]18/11/2007[/b:xhqjlggl][list:xhqjlggl]

[*:xhqjlggl]FIXED: Ah gossips-- 'shouldnt be able to gorge all the food from suppy, shop'[/*:m:xhqjlggl]

[*:xhqjlggl]fixed: reduced the chance of a mild headache messages in last 5minutes of alcohalia[/*:m:xhqjlggl][/list:u:xhqjlggl]

[b:xhqjlggl]19/11/2007[/b:xhqjlggl][list:xhqjlggl]

[*:xhqjlggl]fixed: grouptell bug for the leader[/*:m:xhqjlggl]

[*:xhqjlggl]fixed: bug in partial name use in tell[/*:m:xhqjlggl]

[*:xhqjlggl]improved: the partial name useage in try_tell[/*:m:xhqjlggl]

[*:xhqjlggl]CHANGED: can't toss or be tossed when greased up[/*:m:xhqjlggl]

[*:xhqjlggl]Added: wait state  to remove all/wear all dependent on what you wear and remove (some will hate this!)[/*:m:xhqjlggl]

[*:xhqjlggl]changed: Severly lowered the wait state on wear/remove single items (some will love this!) ... Basically this is much fairer[/*:m:xhqjlggl]

[*:xhqjlggl]fixed: breaking wall of flesh after shapeshift return..msg is shown for extracting shapeshift mob[/*:m:xhqjlggl][/list:u:xhqjlggl]

[b:xhqjlggl]20/11/2007[/b:xhqjlggl][list:xhqjlggl]

[*:xhqjlggl]fixed: issue ezekiel raised regarding stealth and oneself..yup my fault[/*:m:xhqjlggl][/list:u:xhqjlggl]

[b:xhqjlggl]22/11/2007[/b:xhqjlggl][list:xhqjlggl]

[*:xhqjlggl]Added: springwater, iced water drinks[/*:m:xhqjlggl]

[*:xhqjlggl]Fixed: broken dead tells (my fault)[/*:m:xhqjlggl]

[*:xhqjlggl]Fixed: brothers in valor check on deathgrip and deathtouch[/*:m:xhqjlggl]

[*:xhqjlggl]fixed: nan error in score[/*:m:xhqjlggl][/list:u:xhqjlggl]

 

[b:xhqjlggl]01/12/2007[/b:xhqjlggl][list:xhqjlggl]

[*:xhqjlggl]Updated: ask better error handling[/*:m:xhqjlggl]

[*:xhqjlggl]Updated: query better error handling, and improved support for shop/forge[/*:m:xhqjlggl]

[*:xhqjlggl]Updated: clan title checking[/*:m:xhqjlggl]

[*:xhqjlggl]added: title to allow %s which will automatically use clan symbol even when changed[/*:m:xhqjlggl]

[*:xhqjlggl]Fixed: track to use the newly calculated lag and not PULSE_VIOLENCE. (makes it faster and more useful)[/*:m:xhqjlggl]

[*:xhqjlggl]Added: rum liquid[/*:m:xhqjlggl]

[*:xhqjlggl]Fixed: liquid mixing (mixing diff waters no longer makes slime), also made it more dynamic for future mixing[/*:m:xhqjlggl]

[*:xhqjlggl]Updated: pour/fill/create water to use new mix_liquids()[/*:m:xhqjlggl]

[*:xhqjlggl]Fixed: poison check when filling from poisoned fountain, allowed filling from carried fountain[/*:m:xhqjlggl]

[*:xhqjlggl]Fixed: can't gorge steal unless you've learnt steal, can't gorge from mobs or immortals[/*:m:xhqjlggl]

[*:xhqjlggl]Fixed: pour to work from carried fountains[/*:m:xhqjlggl]

[*:xhqjlggl]Changed: remove all lag 50%, wear all lag 75%[/*:m:xhqjlggl]

[*:xhqjlggl]Fixed: typo in order skitzofreni is schizophrenia[/*:m:xhqjlggl]

[*:xhqjlggl]Fixed: squirm to work properly with violation/ended of noexits[/*:m:xhqjlggl]

[*:xhqjlggl]Fixed: make_prompt() *** Press return *** to be terminated by CLR_STATUS[/*:m:xhqjlggl]

[*:xhqjlggl]Fixed: dark cloak to work like a broken darkness again[/*:m:xhqjlggl]

[*:xhqjlggl]Added: brownie supplication[/*:m:xhqjlggl]

[*:xhqjlggl]Changed: query shopkeeper to charge 2k coins if >20 instead of refusing with a stupid reason[/*:m:xhqjlggl]

[*:xhqjlggl]Fixed: crash bug in sun cycler.. when mob runs out of mana[/*:m:xhqjlggl]

[*:xhqjlggl]Added: kvp_forge to allow query on nth items in list esp if same result, addiontally shows if cps can be seen in query needs SHOWCPS[n][/*:m:xhqjlggl]

[*:xhqjlggl]Changed: kvp_forge list to show same checks as shop list, addiontally shows if cps can be seen in query needs SHOWCPS[n][/*:m:xhqjlggl]

[*:xhqjlggl]fixed: clan title in "rank who"[/*:m:xhqjlggl]

[*:xhqjlggl]fixed: pouring from container/fountain[/*:m:xhqjlggl]

[*:xhqjlggl]fixed: when removing/wearing eq the maxhp&maxmana are updated immediately rather than waiting for the fast_point_update so that the prompt appears correctly[/*:m:xhqjlggl]

[*:xhqjlggl]fixed: the eq remove/wear lag by using SET_WAIT_STATEinstead of WAIT_STATE which was adding the value...arrrghhh[/*:m:xhqjlggl]

[*:xhqjlggl]fixed: reset of some point values after eq is loaded (caused stacking)[/*:m:xhqjlggl][/list:u:xhqjlggl]

[b:xhqjlggl]02/12/2007[/b:xhqjlggl][list:xhqjlggl]

[*:xhqjlggl]fixed:  a couple of insert of clan symbol which had been forgotten[/*:m:xhqjlggl][/list:u:xhqjlggl]

 

[b:xhqjlggl]03/12/2007[/b:xhqjlggl][list:xhqjlggl]

[*:xhqjlggl]added cocktail, holy water, herbal tea[/*:m:xhqjlggl][/list:u:xhqjlggl]

 

[b:xhqjlggl]05/12/2007[/b:xhqjlggl][list:xhqjlggl]

[*:xhqjlggl]changed: wear all lag to 50% of total[/*:m:xhqjlggl]

[*:xhqjlggl]added: remove_many/wear_many to process removal/wearing of multiple items covered by concise but faster than removing all/wearing all[/*:m:xhqjlggl]

[*:xhqjlggl]Fixed: crash bug where by if title is loaded from pfile as null set it back to untitled[/*:m:xhqjlggl][/list:u:xhqjlggl]

 

[b:xhqjlggl]06/12/2007[/b:xhqjlggl][list:xhqjlggl]

[*:xhqjlggl]fixed: crash bug - on removal of ITEM_TMP objects .. my fault[/*:m:xhqjlggl]

[*:xhqjlggl]fixed: bug - wilo the wisp, spell was assigned to the wrong slot[/*:m:xhqjlggl][/list:u:xhqjlggl]

</div>
