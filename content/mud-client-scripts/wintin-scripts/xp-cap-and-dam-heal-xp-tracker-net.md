---
title: "XP Cap and Dam/Heal XP Tracker --.NET"
topic_id: 1710
author: "*juggleblood*"
date: 2006-02-04T01:17:05+00:00
last_activity: 2006-02-04T01:17:05+00:00
last_author: "*juggleblood*"
sticky: false
locked: false
post_count: 1
---

<div class="post" data-post-id="10555" data-author="*juggleblood*" data-date="2006-02-04T01:17:05+00:00" data-subject="XP Cap and Dam/Heal XP Tracker --.NET">

This is kind of strange the way I set this up. I'd like to see anyone else's scripts that are similar. It figures out if you capped or not and by how much. And it also figures out how much xp you got above and beyond your share of the mob xp for hacking, blasting, or healing.

After each kill in a group this script does a score command. It gags out most of the junk in the score by temporarily activating a group called xpgag. I have a trigger that deactivates this group when I log in. Then it just activates itself as necessary. You'll definitely notice if its on by mistake, cuz your score will be all gagged out-just type xpgagoff.

Its set up to display it as 'damage xp' cuz I'm not a cleric. Fix it as you like.

Also its not set up to be turned on and off. It just always activates when you're a group member (non leader) and get xp. It will give wacky results if you've just leveled or died and lost xp.

You may have to create the initial variables to get it going, but I don't think so.

Enjoy <img src="/images/smilies/icon_e_smile.svg" alt=":)" title=":)" width="15" height="15" class="smiley nozoom">

\#defgroup experience

\#ac {^You receive %0 experience} {save;#var mobxp $0;trigxpcheck;trigxpgag;sc} {G\|experience}

\#al {trigxpcheck} {#ac {^You have %0 unused} {#var xpcurrent $0; #math xpdelta $0-$xpcurrent;#showme {XPdelta is $xpdelta};#if {$xpdelta\<$mobxp} {#math xpcap {$mobxp-$xpdelta};#showme {XPCap is $xpcap}};#if {$xpdelta\>$mobxp} {#math damxp {$xpdelta-$mobxp};#showme {You received $damxp exp points for damage done.}};#if {$damxp=0} {#showme You did no recent damage.}} {O}} {G\|experience}

\#al {trigxpgag} {#ac {(level:} {xpgagon}{O};#ac {^You are affected}{xpgagoff}{O}} {G\|experience}

\#al {xpgagoff} {#disable xpgag} {G\|experience}

\#al {xpgagon} {#enable xpgag} {G\|experience}

\#defgroup xpgag

\#gag {armor} {G\|xpgag}

\#gag {drachma} {G\|xpgag}

\#gag {evil} {G\|xpgag}

\#gag {example} {G\|xpgag}

\#gag {gold} {G\|xpgag}

\#gag {good} {G\|xpgag}

\#gag {levels} {G\|xpgag}

\#gag {movement} {G\|xpgag}

\#gag {neutral} {G\|xpgag}

\#gag {protecting} {G\|xpgag}

\#gag {sleeping} {G\|xpgag}

\#gag {Str} {G\|xpgag}

\#gag {thirsty} {G\|xpgag}

\#gag {throat} {G\|xpgag}

</div>
