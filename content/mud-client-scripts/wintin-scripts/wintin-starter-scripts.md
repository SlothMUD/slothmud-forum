---
title: "Wintin Starter scripts"
topic_id: 1802
author: "*Splork*"
date: 2006-03-27T16:02:09+00:00
last_activity: 2006-06-07T19:39:56+00:00
last_author: "Shara"
sticky: false
locked: false
post_count: 8
---

<div class="post" data-post-id="11833" data-author="*Splork*" data-date="2006-03-27T16:02:09+00:00" data-subject="Wintin Starter scripts">

Here is a small sampling of a few of my groups for wintin.NET

This ought to give a new user the basic idea of how to use this program, if not simply copy the syntax and replace it with your own.

WARNING- the substitutes and highlights do not represents sloth's colors or strings. Please be well aware of this. I would hate for someone to use this and then think sloth is cheesy because my sample scripts suck.

I should probably explain the variables group...

 A user should type me <charactername> when they log in. Then the $me variable is used all over my scripts so that it works with all my characters-not just one.

The tank, lead, leads, tar and target variables are just that. If you join a group, type leads <leadername>, tank <tankname> etc. This is so that you do not need to create new aliases and actions everytime you join a group. Examples: 

#action  {$leader-%all up} {wake;stand;#bell}

#alias { cast 'heal'$tank}

#alias {cast 'firewind'$target}

#defgroup {Variables}

#alias  {conta} {#var cont $1;#showme -----------------------------------;#showme CONTAINER SET TO <<: $1 :>>;#cr} {G|Variables}

#alias  {lead} {#var leader $1;gt <*- $1 -*> is leading the rebel alliance.} {G|Variables}

#alias  {leads} {#var leader $1;#showme -------------------------------;#showme LEADER SET TO <*- $1 -*>;#cr} {G|Variables}

#alias  {me} {#var me $1;#showme -------------------------------------;#showme PLAYER IS SET TO <*- $1 -*>;#cr} {G|Variables}

#alias  {tanks} {#var tank $1;#showme ----------------------------------;#showme SETTING TANK TO: <*- $1 -*>;#cr} {G|Variables}

#alias  {tar} {#var target $1;#showme ---------------------------------;#showme TARGET SET TO: <*- $1 -*>;#cr} {G|Variables}

#alias  {target} {#var target $0;#showme *****=====>>>>>target $0<<<<<=====*****} {G|Variables}

#defgroup {}

#defgroup {General}

#alias  {gt} {grouptell} {G|Grouptells}

#action  {$leader-%all up} {wake;stand;#bell} {G|General}

#action  {%1 tells you} {#bell} {G|General}

#action  {You are hungry.} {eat food} {G|General}

#action  {You are thirsty.} {#2 drink water} {G|General}

#alias  {ast} {assist $tank} {G|General}

#alias  {rr} {recite recall} {G|General}

#defgroup {}

#defgroup {Subs}

#substitute  {%0again - blood all over} {$0again - shit all over!} {G|Subs}

#substitute  {%0brutally massacred%1} {$0BRUTALLY *** SPLATTERED ***$1} {G|Subs}

#substitute  {%0extremely hard.} {%0EXTREMELY HARD.} {G|Subs}

#substitute  {%0hard.} {%0HARD.} {G|Subs}

#substitute  {%0in the solar plexus} {$0in the butt!} {G|Subs}

#substitute  {%0massacre %1} {$0** SPLATTER ** $1} {G|Subs}

#substitute  {%0massacres %1} {$0** SPLATTERS ** $1} {G|Subs}

#substitute  {%0massive blow %1} {$0** MASSIVE BLOW ** $1} {G|Subs}

#substitute  {%0utters the words, %1} {$0babbles, $1} {G|Subs}

#substitute  {%0very hard.} {%0VERY HARD.} {G|Subs}

#substitute  {%0viciously massacred%1} {$0VICIOUSLY *** SPLATTERED ***$1} {G|Subs}

#substitute  {is engulfed in flames!} {.} {G|Subs}

#substitute  {is hit by a torrent of freezing cold air.} {.} {G|Subs}

#substitute  {The detect invisible wears off.} {*****====>> WARNING: I CAN'T SEE INVIS ANYMORE <<====*****} {G|Subs}

#defgroup {}

#defgroup {Colors}

#highlight  {red} {***************=====>>>>> WARNING: APTITUDE RAN OUT <<<<<=====***************} {G|Colors}

#highlight  {red} {***************=====>>>>> WARNING: CORONA RAN OUT <<<<<=====***************} {G|Colors}

#highlight  {red} {***************=====>>>>> WARNING: STAMINA RAN OUT <<<<<=====***************} {G|Colors}

#highlight  {red} {************========>>>>> WARNING: VITALITY RAN OUT <<<<<========************} {G|Colors}

#highlight  {red} {**********=====>>>>> TARGET:[ $0 ] <<<<<=====**********} {G|Colors}

#highlight  {red} {**********>>>>>>>>>> WARNING: MOBILITY IS OUT <<<<<<<<<<**********} {G|Colors}

#highlight  {red} {********=======>>>> SPELL OUT: [ RESIST WEBS ] <<<<<=======********} {G|Colors}

#highlight  {magenta} {******======>>>>>PREDICTION has FALLEN<<<<<======******} {G|Colors}

#highlight  {green} {******=====>>>>>COUNTER-ATTACK HAS FADED<<<<<=====******} {G|Colors}

#highlight  {red} {******====>> WARNING: WATERBREATH IS OUT <<====*****} {G|Colors}

#highlight  {red} {*****====>> WARNING: BLESS RAN OUT <<====*****} {G|Colors}

#highlight  {red} {*****====>> WARNING: FLY IS OUT <<====*****} {G|Colors}

#highlight  {red} {*****====>> WARNING: I CAN'T SEE INVIS ANYMORE <<====*****} {G|Colors}

#highlight  {red} {*****====>> WARNING: I CAN'T SENSE HIDDEN LIFE <<====*****} {G|Colors}

#highlight  {red} {*****====>> WARNING: I'M A WEAKLING <<====*****} {G|Colors}

#highlight  {red} {*****====>> WARNING: MY SKIN IS SOFT <<====*****} {G|Colors}

#highlight  {red} {*****====>> WARNING: REJUVENATION IS GONE <<====*****} {G|Colors}

#highlight  {magenta} {^You auction-- '%0} {G|Colors}

#highlight  {cyan} {a few scratches.} {G|Colors}

#highlight  {cyan} {awful condition.} {G|Colors}

#highlight  {cyan} {big nasty wounds and scratches.} {G|Colors}

#highlight  {cyan} {bleeding awfully from big wounds.} {G|Colors}

#highlight  {red} {BRUTALLY} {G|Colors}

#defgroup {}

#defgroup {Spells}

#alias  {damt} {cast 'damnation' $target} {G|Spells}

#alias  {dark} {cast 'darkness'flight} {G|Spells}

#alias  {db} {cast 'demon bind' $target} {G|Spells}

#alias  {death} {cast 'death pact'} {G|Spells}

#alias  {dems} {cast 'demonic strength'} {G|Spells}

#alias  {des} {cast 'destruction'} {G|Spells}

#alias  {dest} {cast 'destruction'$target} {G|Spells}

#alias  {det} {cast 'detect invis'$me} {G|Spells}

#alias  {dis} {cast 'disintegrate'} {G|Spells}

#alias  {dise} {disengage} {G|Spells}

#alias  {dm} {cast 'dispel magic'} {G|Spells}

#alias  {ds} {cast 'darksight'$me} {G|Spells}

#defgroup {}

WINDOWS 

#window {tell} {tells you '|You tell}

#window {wiznet} {-> '}

#window {clan} {[Clan:Hosers]> '}

#window {hosers} {[hosers]> '}

#window {gossip} {gossips-- '|You gossip-- '}

#window {auction} {auctions-- '|You auction-- '}

#window {quest} {quests-- '|You quest-- '}

#window {newbie} {newbies-- '|You newbie-- '}

I hope these help, the vast majority of our players us wintin or wintin.NET

Please contribute if you can to helping others learn this program...

Enjoy,

Splork

</div>

<div class="post" data-post-id="11850" data-author="12345" data-date="2006-03-27T22:28:38+00:00" data-subject="">

This falls in with Splorks $me var.  I'm lazy.  Too lazy in fact to use wintin's autoconnect feature.  I just use the below script and it automatically connects me and sets $me to whoever it is.  Remember that it's best to type the name in as a capitol.

Usage: sloth Name

#defgroup Connect

#alias  {sloth} {#var me $1;#ses slothmud.org 6101} {G|Connect}

#action  {^   Make your choice:} {1} {G|Connect}

#action  {^ Previous connection terminated, press return to reconnect...} {1;startup} {G|Connect}

#action  {^*** PRESS RETURN:} {1} {G|Connect}

#action  {^By what name do you wish to be known?} {$me} {G|Connect}

#action  {^Do you wish to force the connection closed (Y/N)?} {y} {G|Connect}

#action  {^Password accepted.  Press return to continue...} {1} {G|Connect}

#action  {^Password:} {PASSWORD} {G|Connect}

#action  {^Previous connection terminated, press return to reconnect...} {1;startup} {G|Connect}

#action  {^Reconnecting.} {startup} {G|Connect}

#action  {^Welcome to the land of Sloth III. May your visit here be... Interesting.} {startup} {G|Connect}

#alias  {sloth} {#var me $1;#ses slothmud.org 6101} {G|Connect}

#alias  {startup} {group $me; grouptell I NEED A STARTUP SCRIPT!!} {G|Connect}

#variable  {me} {NULL} {G|Connect}

</div>

<div class="post" data-post-id="11865" data-author="12345" data-date="2006-03-29T04:52:50+00:00" data-subject="">

These are some of the most useful scripts I have.  Basically it tracks the protects around me.  Automatically sets whoever I follow as leader.  Stands up when the leader says all up, rests when the leader says regen (you may want to change to sleep) and accepts targets to the $target var.  'lt' is programmed as 'look target' and you can use it as a template to build pretty much any targeted alias or action.

Usage: 

protchain - Displays the protect chain around you 

protover Name - Set this to the person your protectee is protecting. You will automatically protect over if they die. 

lt - look at set target.

#defgroup Group 

#action {^$leader -- '%1target %2'} {#var target $2}{G|Group} 

#action {^$leader -- '%1all up'} {wake;stand} {G|Group} 

#action {^$leader -- '%1regen'} {rest} {G|Group} 

#action {^$protectee is dead! R.I.P.} {protect $nextprotect} {G|Group} 

#action {^%1 begins protecting you.} {#var protector $1;gt $1 is now protecting me! *whew*} {G|Group} 

#action {^%1 is protecting you.} {#var protector $1} {G|Group} 

#action {^But you are a member of no group?!} {group $me} {G|Group} 

#action {^But you are not in a group!} {group $me} {G|Group} 

#action {^You are no longer a member of the group!} {group $me} {G|Group} 

#action {^You are no longer being protected.} {#var protector null;gt No protect! Someone protect $me!} {G|Group} 

#action {^You are no longer protecting %1.} {#var protectee null;gt You're own your own $1. May the gods pity you.} {G|Group} 

#action {^You are protecting %1.} {#var protectee $1} {G|Group} 

#action {^You begin protecting %1.} {#var protectee $1;gt I am now protecting $1.} {G|Group} 

#action {^You feel much, much better!} {gt I'm up, thanks!} {G|Group} 

#action {^You now follow %1.} {#var leader $1} {G|Group} 

#action {^You stop following $leader.} {#var leader $me} {G|Group} 

#alias {lt}{look $target}{G|Group}

#alias {protchain} {gt Protect chain: $protector --> $me --> $protectee} {G|Group} 

#alias {protover} {#var nextprotect $1} {G|Group} 

#variable {leader} {null} {G|Group} 

#variable {nextprotect} {null} {G|Group} 

#variable {protectee} {null} {G|Group} 

#variable {protector} {null} {G|Group} 

#variable {target} {null} {G|Group}

</div>

<div class="post" data-post-id="11866" data-author="jezer" data-date="2006-03-29T06:18:56+00:00" data-subject="">

Some great scripts here... I might post some of my more useful ones to this post later... But I'll leave you with this handy one...

#defgroup Group

#action {Splork tells you} {#bell;botoff;pretendtell;#var splorkon 1}{G|Group}

#action {Splork gossips} {#bell;botoff;pretendgos;suckupdrachscatter;#var splorkon 1}{G|Group}

#action {:)~} {addbradalt} {G|Group}

#action {Shyla gossips} {gos Me!;neededspellbooks;}

#alias {pretendtell} {tell Splork :) no problem.}{G|Group}

#alias {pretendgos} {gos Heya Splork!}{G|Group}

#alias {suckupdrachscatter} {gos 7 drachma from quest item! How about a scatter splork?}{G|Group}

#alias {neededspellbooks} {gos I also need... $neededspellbooks} {G|Group}

#substitute {stfu} {Haha, thats great point you make!}{G|Group}

#substitute {stfu!} {Haha, thats great point you make!}{G|Group}

#substitute {noob} {expert}{G|Group}

#substitute {n00b} {expert}{G|Group}

#substitute {Harlot gossips} {blah, blah, blah, blah, blah, blah}{G|Group}

#gag {Can I get a CR}{M}{G|Group}

#variable {splorkon} {0}{G|Group}

#variable {neededspellbooks} {magic missile} {G|Group}

</div>

<div class="post" data-post-id="12895" data-author="Hobbes" data-date="2006-06-06T16:50:36+00:00" data-subject="">

I copied the scripts posted by Splork, but none of the #actions are working.  Anyone can help?  Specifically I am trying to get these to work:

#defgroup {Variables}

#alias  {vcry} {#var crier $1;#showme <*- $1 -*> is doing the warcries.} {G|Variables}

#defgroup {}

#defgroup {General}

#action  {$leader-%all up} {wake;stand;#bell} {G|General}

#action  {%1 tells you} {#bell} {G|General}

#action  {^$crier yells '%1'} {warcry $1} {G|General}

#action  {You are hungry.} {eat food} {G|General}

#action  {You are thirsty.} {#2 drink water} {G|General}

</div>

<div class="post" data-post-id="12896" data-author="Rynquald" data-date="2006-06-06T20:06:30+00:00" data-subject="">

#alias {vcry} {#var crier $1;#showme <*- $1 -*> is doing the warcries.} {G|Variables}

#action {^$crier yells '%1'} {warcry $1} {G|General}

Should work fine as long as you don't use an all lower case name, for example, 'vcry splork' won't work, 'vcry Splork' will.

Same with the all up trig, need a leader var, something like;

#alias {leader} {#var {leader} {$1}}

will work fine.

The hungry thing assumes you have food in inv, not in a container, and thirsty has an alias for it's string, changing it to;

#action {You are thirsty.} {drink barrel} {G|General}

where barrel is your water container should fix it.

Can't see anything that would make the tells you bell fail, maybe your volume's down too low to hear it, or bell's disabled in wintin's settings.

</div>

<div class="post" data-post-id="12901" data-author="Gimlet" data-date="2006-06-07T03:01:37+00:00" data-subject="">

#action {^$crier yells '%1'} {warcry $1} {G|General} 

--> this could potentially be troublesome coz some ppl have ' in their warcry and you wouldn't be getting the full warcry in your action :)

</div>

<div class="post" data-post-id="12906" data-author="Shara" data-date="2006-06-07T19:39:56+00:00" data-subject="">

#action {:)~} {addbradalt} {G|Group}

rofl, good one!

I wonder if these are real... :oops:

</div>
