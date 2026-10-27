---
title: "script assistance"
topic_id: 3183
author: "sirrico1"
date: 2009-06-28T20:16:20+00:00
last_activity: 2009-06-29T11:14:03+00:00
last_author: "Rigwarl"
sticky: false
locked: false
post_count: 3
---

<div class="post" data-post-id="29605" data-author="sirrico1" data-date="2009-06-28T20:16:20+00:00" data-subject="script assistance">

This is my rescue script and for some reason it does not always rescue on disengages, any ideas? 

\#defgroup {Tank-Rescuer}

\#action {$stb places %0} {rescue $stb;#var rescuee $stb} {G\|Tank-Rescuer} {T\|WT}

\#action {^Your body quickly tightens, as you no longer feel any pain.} {gt DEFIED!!!} {G\|Tank-Rescuer} {T\|WT}

\#action {but nearly cut} {rescue $stb;#var rescuee $stb} {G\|Tank-Rescuer} {T\|WT}

\#alias {altankof} {#show \*\*\*\*\* I R NOT 2nd TANK ANYMORE \*\*\*\*\*;#unac {^$tank is dead! R.I.P.}} {G\|Tank-Rescuer} {T\|WT}

\#alias {altankon} {#show \*\*\*\*\* I R 2nd TANK NOW \*\*\*\*\*;#ac {^$tank is dead! R.I.P.} {gt I R tank now!!;whinet}} {G\|Tank-Rescuer} {T\|WT}

\#alias {rescallof} {gt I will no longer TRY to rescue you wussies...;rescdisof;rescseeof;rescsingof;rescstabof} {G\|Tank-Rescuer} {T\|WT}

\#alias {rescallon} {gt I will now TRY to rescue everybody (SING for it ppl);rescdison;rescseeon;rescsingon;rescstabon} {G\|Tank-Rescuer} {T\|WT}

\#alias {rescdisof} {#unac {disengages himself, and attacks %1!}} {G\|Tank-Rescuer} {T\|WT}

\#alias {rescdison} {#ac {disengages himself, and attacks %1!} {rescue $1;#var rescuee $1};rescfailon} {G\|Tank-Rescuer} {T\|WT}

\#alias {rescfailof} {#unac {You fail the rescue}} {G\|Tank-Rescuer} {T\|WT}

\#alias {rescfailon} {#ac {You fail the rescue} {rescue $rescuee} } {G\|Tank-Rescuer} {T\|WT}

\#alias {rescseeof} {#unac {sees %1, and attacks!}} {G\|Tank-Rescuer} {T\|WT}

\#alias {rescseeon} {#ac {sees %1, and attacks!} {rescue $1;#var rescuee $1}; rescfailon} {G\|Tank-Rescuer} {T\|WT}

\#alias {rescsingof} {#unac {SEEK SHELTER AT ONCE! %1 has begun to sing.}} {G\|Tank-Rescuer} {T\|WT}

\#alias {rescsingon} {#ac {SEEK SHELTER AT ONCE! %1 has begun to sing.} {rescue $1;#var rescuee $1}; rescfailon} {G\|Tank-Rescuer} {T\|WT}

\#alias {rescstabof} {#unac {$stb place %0};#unac {$stb tried %0}} {G\|Tank-Rescuer} {T\|WT}

\#alias {rescstabon} {#ac {$stb place %0} {rescue $stb;#var rescuee $stb}#ac {but nearly cut} {rescue $stb;#var rescuee $stb} ;rescfailon } {G\|Tank-Rescuer} {T\|WT}

\#defgroup {}

</div>

<div class="post" data-post-id="29609" data-author="Mace" data-date="2009-06-29T05:19:21+00:00" data-subject="Gender for weaks!">

Hm, probably because not all mobs disengage 'himself'. <img src="/images/smilies/icon_e_smile.svg" alt=":)" title=":)" width="15" height="15" class="smiley nozoom">

</div>

<div class="post" data-post-id="29612" data-author="Rigwarl" data-date="2009-06-29T11:14:03+00:00" data-subject="">

There tends to be silent disengages too nowadays, where the mob changes target without any notice.

Your disengage triggers would only work if the mob is male, set it as a variable.

Also mobs use the engage skill.

</div>
