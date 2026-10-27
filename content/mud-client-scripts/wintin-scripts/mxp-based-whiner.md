---
title: "MXP based Whiner"
topic_id: 1835
author: "*juggleblood*"
date: 2006-04-07T21:58:24+00:00
last_activity: 2006-04-07T21:58:24+00:00
last_author: "*juggleblood*"
sticky: false
locked: false
post_count: 1
---

<div class="post" data-post-id="12002" data-author="*juggleblood*" data-date="2006-04-07T21:58:24+00:00" data-subject="MXP based Whiner">

Please share any mxp based scripts you might have. I'm curious to see them.

Here is a whiner based on mxp. Its a lot simpler than it appears at first glance. A lot of this garbage is color codes. The key is using the optional trigger in the variable command to detect changes in your MXP variables.

\#defgroup mxpwhiner

\#alias {whineoff} {gt \\\\c11 -------------------Whining Disabled---------------------;#var whine 0} {G\|mxpwhiner}

\#alias {whineon} {gt \\\\c11-----------------Whining Enabled ----I'm the Tank ----------------------;#var whine 1} {G\|mxpwhiner}

\#alias {wmsg1} {gt \\\\c15------\> [hp: \\\\c06$CurrentHP \\\\c15/ $MaxHP ma: \\\\c06$CurrentMana \\\\c15/ $MaxMana] \\\\c09[\\\\c11+$deltahp hp\\\\c09] \\\\c06[$lite]} {G\|mxpwhiner}

\#alias {wmsg2} {gt \\\\c04-------\> \\\\c15[hp: \\\\c06$CurrentHP \\\\c15/ $MaxHP ma: \\\\c06$CurrentMana\\\\c15 / $MaxMana] \\\\c09[\\\\c04$deltahp hp\\\\c09] \\\\c06[$lite]} {G\|mxpwhiner}

\#alias {ws} {#showme Whiner Sensitivity set to $0 hp; #var ws $0;#math negws {0-$ws}} {G\|mxpwhiner}

\#variable {CurrentHP} {500} {G\|mxpwhiner}{T\|#math {deltahp}{$CurrentHP-$lasthp};#var lasthp {$CurrentHP};#if {$whine=1}{#if {$deltahp\>$ws}{wmsg1};#if {$deltahp\<$negws}{wmsg2}}}

\#defgroup {}

\* The [$lite] in the message on my scripts shows the type of lite and the time remaining. I just added a line into the sanctuary/aegis counter that sents the $lite variable to 'Sanc:$literemain' to make it show in the whiner.

\-Cheers

</div>
