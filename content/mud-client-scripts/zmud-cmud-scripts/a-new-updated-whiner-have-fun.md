---
title: "A new, updated whiner!  Have fun"
topic_id: 734
author: "Xandora"
date: 2005-01-09T12:46:05+00:00
last_activity: 2005-01-11T11:28:19+00:00
last_author: "Akasha2"
sticky: false
locked: false
post_count: 6
---

<div class="post" data-post-id="3682" data-author="Xandora" data-date="2005-01-09T12:46:05+00:00">

I have finally completed adapting the whiner to the new custom prompt.  This update includes some nice additions such as color coded decrease in hp, mana and moves, an am/pm clock that counts sloth time in regluar time, and a weather indicator (mostly for druids), as well as the ability to be always on without spamming you.  Also when used in unison with my previous whiner somewhere below this thread, using if(@charname=@tank), it needs no alias to be switched on and off for tanking and soloing.  

Alas, this whiner is designed for Druids mostly (as that is what Xandora is), but will work for anyone.  

Below are two versions of the same script, version 1.0 doesnt use the previously mentioned if(@charname=@tank) script, while version 2.0 does.  The choice is yours.  Enjoy and please, let me know what you think, and if there is anything you'd like to see it do, that it doesn't already.

**NOTE: This scripts are totally self contained and go into one class folder that can be permanently enabled.  No need for on/off toggles.

You might notice the #ALIAS at the beginning of the script, for you druids, just place this alias (newprompt) after your shapeshifting alias to automatically convert your shifted prompt to fit the script every time you shift.  

Version 1.0 (without switch for tanking and soloing)

#ALIAS newprompt {prompt ~<Time ~= $t | $w | $h/$Hhp $m/$Mma $v/Vmv~>}

#TRIGGER {^~<Time = %1 ~| %2 ~| %3~/%4hp %5~/%6ma %7~/%8mv~>} {

#var timeofday %1

#var weather %2

#var curhp %3

#var maxhp %4

#var curma %5

#var maxma %6

#var curmv %7

#var maxmv %8

#math thirdhp @maxhp-(@maxhp/4)

#math halfhp @maxhp/2

#math criticalhp @maxhp/5

#math thirdma @maxma-(@maxma/4)

#math halfma @maxma/2

#math criticalma @maxma/5

#math thirdmv @maxmv-(@maxmv/4)

#math halfmv @maxmv/2

#math criticalmv @maxmv/5

#math diffhp (@curhp-@lasthp)

#math needhp %abs(@maxhp-@curhp)

#math lasthp @curhp

#VAR hitup {20}

#VAR hitdown {-20}

#if (@curhp>@thirdhp) {#var hpcolor green} {#if (@curhp<@thirdhp AND @curhp>@halfhp) {#var hpcolor cyan} {#if (@curhp<@halfhp AND @curhp>@criticalhp) {#var hpcolor yellow} {#if (@curhp<@criticalhp) {#var hpcolor red}}}}

#if (@curma>@thirdma) {#var macolor green} {#if (@curma<@thirdma AND @curma>@halfhp) {#var macolor cyan} {#if (@curma<@halfma AND @curma>@criticalma) {#var macolor yellow} {#if (@curma<@criticalma) {#var macolor red}}}}

#if (@curmv>@thirdmv) {#var mvcolor green} {#if (@curmv>@thirdmv AND @curmv>@halfmv) {#var mvcolor cyan} {#if (@curmv<@halfmv AND @curmv>@criticalmv) {#var mvcolor yellow} {#if (@curmv<@criticalmv) {#var mvcolor red}}}}

#if (@timeofday > 12) {

#math standardtime @timeofday-12

#var ampm am

#var timeofday @standardtime

#SHOW %ansi(white)"~<Time:"@timeofday""@ampm" - "@weather">"

#SUB "~<"%ansi(@hpcolor)@curhp%ansi(white)"/"@maxhp"hp "%ansi(@macolor)@curma%ansi(white)"/"@maxma"ma "%ansi(@mvcolor)@curmv%ansi(white)"mv>"

} {

#if (@timeofday = 0) {

#var timeofday 12

#var ampm am

#SHOW %ansi(white)"~<Time:"@timeofday""@ampm" - "@weather">"

#SUB "~<"%ansi(@hpcolor)@curhp%ansi(white)"/"@maxhp"hp "%ansi(@macolor)@curma%ansi(white)"/"@maxma"ma "%ansi(@mvcolor)@curmv%ansi(white)"mv>"

} {

#var ampm pm

#SHOW %ansi(white)"~<Time:"@timeofday""@ampm" - "@weather">"

#SUB "~<"%ansi(@hpcolor)@curhp%ansi(white)"/"@maxhp"hp "%ansi(@macolor)@curma%ansi(white)"/"@maxma"ma "%ansi(@mvcolor)@curmv%ansi(white)"mv>"

}

}

#if (@diffhp<>0) {#if (@diffhp>@hitup) {#SUB %ansi(white)"<"%ansi(@hpcolor)@curhp%ansi(white)"/"@maxhp"hp ~[+"%ansi(yellow)@diffhp%ansi(white)" Need:"%ansi(yellow)@needhp%ansi(white)"~] "%ansi(@macolor)@curma"/"%ansi(white)@maxma"ma>")}} {#if (@diffhp<@hitdown) {#SUB %ansi(white)"<"%ansi(@hpcolor)@curhp%ansi(white)"/"@maxhp" ~["%ansi(yellow)@diffhp%ansi(white)" Need:"%ansi(yellow)@needhp%ansi(white)"~] "%ansi(@macolor)@curma"/"%ansi(white)@maxma"ma>"}}

}

Version 2.0 (with switch for tanking and soloing)

#ALIAS newprompt {prompt ~<Time ~= $t | $w | $h/$Hhp $m/$Mma $v/Vmv~>}

#TRIGGER {^~<Time = %1 ~| %2 ~| %3~/%4hp %5~/%6ma %7~/%8mv~>} {

#var timeofday %1

#var weather %2

#var curhp %3

#var maxhp %4

#var curma %5

#var maxma %6

#var curmv %7

#var maxmv %8

#math thirdhp @maxhp-(@maxhp/4)

#math halfhp @maxhp/2

#math criticalhp @maxhp/5

#math thirdma @maxma-(@maxma/4)

#math halfma @maxma/2

#math criticalma @maxma/5

#math thirdmv @maxmv-(@maxmv/4)

#math halfmv @maxmv/2

#math criticalmv @maxmv/5

#math diffhp (@curhp-@lasthp)

#math needhp %abs(@maxhp-@curhp)

#math lasthp @curhp

#VAR hitup {20}

#VAR hitdown {-20}

#if (@curhp>@thirdhp) {#var hpcolor green} {#if (@curhp<@thirdhp AND @curhp>@halfhp) {#var hpcolor cyan} {#if (@curhp<@halfhp AND @curhp>@criticalhp) {#var hpcolor yellow} {#if (@curhp<@criticalhp) {#var hpcolor red}}}}

#if (@curma>@thirdma) {#var macolor green} {#if (@curma<@thirdma AND @curma>@halfhp) {#var macolor cyan} {#if (@curma<@halfma AND @curma>@criticalma) {#var macolor yellow} {#if (@curma<@criticalma) {#var macolor red}}}}

#if (@curmv>@thirdmv) {#var mvcolor green} {#if (@curmv>@thirdmv AND @curmv>@halfmv) {#var mvcolor cyan} {#if (@curmv<@halfmv AND @curmv>@criticalmv) {#var mvcolor yellow} {#if (@curmv<@criticalmv) {#var mvcolor red}}}}

#if (@timeofday > 12) {

#math standardtime @timeofday-12

#var ampm am

#var timeofday @standardtime

#SHOW %ansi(white)"~<Time:"@timeofday""@ampm" - "@weather">"

#SUB "~<"%ansi(@hpcolor)@curhp%ansi(white)"/"@maxhp"hp "%ansi(@macolor)@curma%ansi(white)"/"@maxma"ma "%ansi(@mvcolor)@curmv%ansi(white)"mv>"

} {

#if (@timeofday = 0) {

#var timeofday 12

#var ampm am

#SHOW %ansi(white)"~<Time:"@timeofday""@ampm" - "@weather">"

#SUB "~<"%ansi(@hpcolor)@curhp%ansi(white)"/"@maxhp"hp "%ansi(@macolor)@curma%ansi(white)"/"@maxma"ma "%ansi(@mvcolor)@curmv%ansi(white)"mv>"

} {

#var ampm pm

#SHOW %ansi(white)"~<Time:"@timeofday""@ampm" - "@weather">"

#SUB "~<"%ansi(@hpcolor)@curhp%ansi(white)"/"@maxhp"hp "%ansi(@macolor)@curma%ansi(white)"/"@maxma"ma "%ansi(@mvcolor)@curmv%ansi(white)"mv>"

}

}

#if (@diffhp<>0) {#if (@diffhp>@hitup) {#if (@charname=@tank) {grouptell "["\d02@curhp\c03"|"\d04@maxhp\c03"]   "To Full:"<"\d02@needhp\c03">   "HEAL:"<+"\d04@diffhp\c03">"} {#SUB %ansi(white)"<"%ansi(@hpcolor)@curhp%ansi(white)"/"@maxhp"hp ~[+"%ansi(yellow)@diffhp%ansi(white)" Need:"%ansi(yellow)@needhp%ansi(white)"~] "%ansi(@macolor)@curma"/"%ansi(white)@maxma"ma>")}} {#if (@diffhp<@hitdown) {#if (@charname=@tank) {grouptell "["\d02@curhp\c03"|"\d04@maxhp\c03"]   "To Full:"<"\d02@needhp\c03">   "DAMG:"<"\d03@diffhp\c03">"} {#SUB %ansi(white)"<"%ansi(@hpcolor)@curhp%ansi(white)"/"@maxhp" ~["%ansi(yellow)@diffhp%ansi(white)" Need:"%ansi(yellow)@needhp%ansi(white)"~] "%ansi(@macolor)@curma"/"%ansi(white)@maxma"ma>"}}}}

}

Enjoy,

Xandora

</div>

<div class="post" data-post-id="3683" data-author="Akasha2" data-date="2005-01-09T13:15:48+00:00">

If you'll look at this line near the bottom of the script:

#if (@diffhp<>0) {#if (@diffhp>@hitup) {#if (@charname=@tank) {grouptell "["\d02@curhp\c03"|"\d04@maxhp\c03"]   "To Full:"<"\d02@needhp\c03">   "HEAL:"<+"\d04@diffhp\c03">"} {#SUB %ansi(white)"<"%ansi(@hpcolor)@curhp%ansi(white)"/"@maxhp"hp ~[+"%ansi(yellow)@diffhp%ansi(white)" Need:"%ansi(yellow)@needhp%ansi(white)"~] "%ansi(@macolor)@curma"/"%ansi(white)@maxma"ma>"_)_}}

You'll notice a misplaced  )  which I have indicated with underscores in the above example.  This can be safely deleted as it is a typo.  

Sorry for the inconvience.

Xandora

</div>

<div class="post" data-post-id="3695" data-author="13" data-date="2005-01-10T02:01:56+00:00">

[img:wxip9uok]http://images.google.com/imgres?imgurl=http://www.swanksigns.org/images/signs/thumbnails/tn_whiner.jpg&imgrefurl=http://www.swanksigns.org/gallery.asp&h=168&w=202&sz=32&tbnid=f14iP0gdULkJ:&tbnh=82&tbnw=98&start=11&prev=/images%3Fq%3Dwhiner%26hl%3Den%26lr%3D%26sa%3DG[/img:wxip9uok]

</div>

<div class="post" data-post-id="3696" data-author="Akasha2" data-date="2005-01-10T07:26:55+00:00">

Had a chance to test whiner for an extended periond of time tonight.  Seems there was a bug in the #SUB command.  The fix is below:

Replace this part: (just copy/paste it over the previous)

#SHOW %ansi(white)"~<Time:"@timeofday""@ampm" - "@weather">"

#SUB "<"%ansi(@hpcolor)@curhp%ansi(white)"/"%ansi(green)@maxhp%ansi(white)"hp "%ansi(@macolor)@curma%ansi(white)"/"%ansi(green)@maxma%ansi(white)"ma "%ansi(@mvcolor)@curmv%ansi(white)"mv>"

} {

#if (@timeofday = 0) {

#var timeofday 12

#var ampm am

#SHOW %ansi(white)"~<Time:"@timeofday""@ampm" - "@weather">"

#SUB "<"%ansi(@hpcolor)@curhp%ansi(white)"/"%ansi(green)@maxhp%ansi(white)"hp "%ansi(@macolor)@curma%ansi(white)"/"%ansi(green)@maxma%ansi(white)"ma "%ansi(@mvcolor)@curmv%ansi(white)"mv>"

} {

#var ampm pm

#SHOW %ansi(white)"~<Time:"@timeofday""@ampm" - "@weather">"

#SUB "<"%ansi(@hpcolor)@curhp%ansi(white)"/"%ansi(green)@maxhp%ansi(white)"hp "%ansi(@macolor)@curma%ansi(white)"/"%ansi(green)@maxma%ansi(white)"ma "%ansi(@mvcolor)@curmv%ansi(white)"mv>"

}

}

Xandora

</div>

<div class="post" data-post-id="3697" data-author="Akasha2" data-date="2005-01-10T07:49:12+00:00">

Tweaked the prompt whiner a little, made it one line instead of two.

Version 1.1 (with @charname=@tank) switch

#ALIAS newprompt {prompt ~<Time ~= $t | $w | $h/$Hhp $m/$Mma $v/Vmv~>}

#TRIGGER {^~<Time = %1 ~| %2 ~| %3~/%4hp %5~/%6ma %7~/%8mv~>} {

#var timeofday %1

#var weather %2

#var curhp %3

#var maxhp %4

#var curma %5

#var maxma %6

#var curmv %7

#var maxmv %8

#math thirdhp @maxhp-(@maxhp/4)

#math halfhp @maxhp/2

#math criticalhp @maxhp/5

#math thirdma @maxma-(@maxma/4)

#math halfma @maxma/2

#math criticalma @maxma/5

#math thirdmv @maxmv-(@maxmv/4)

#math halfmv @maxmv/2

#math criticalmv @maxmv/5

#math diffhp (@curhp-@lasthp)

#math needhp %abs(@maxhp-@curhp)

#math lasthp @curhp

#VAR hitup {20}

#VAR hitdown {-20}

#if (@curhp>@thirdhp) {#var hpcolor green} {#if (@curhp<@thirdhp AND @curhp>@halfhp) {#var hpcolor cyan} {#if (@curhp<@halfhp AND @curhp>@criticalhp) {#var hpcolor yellow} {#if (@curhp<@criticalhp) {#var hpcolor red}}}}

#if (@curma>@thirdma) {#var macolor green} {#if (@curma<@thirdma AND @curma>@halfhp) {#var macolor cyan} {#if (@curma<@halfma AND @curma>@criticalma) {#var macolor yellow} {#if (@curma<@criticalma) {#var macolor red}}}}

#if (@curmv>@thirdmv) {#var mvcolor green} {#if (@curmv>@thirdmv AND @curmv>@halfmv) {#var mvcolor cyan} {#if (@curmv<@halfmv AND @curmv>@criticalmv) {#var mvcolor yellow} {#if (@curmv<@criticalmv) {#var mvcolor red}}}}

#if (@timeofday > 12) {

#math standardtime @timeofday-12

#var ampm am

#var timeofday @standardtime

#SUB %ansi(white)"~<"@timeofday@ampm" - "%ansi(white)"<"%ansi(@hpcolor)@curhp%ansi(white)"/"@maxhp"hp ~[+"%ansi(yellow)@diffhp%ansi(white)" Need:"%ansi(yellow)@needhp%ansi(white)"~] "%ansi(@macolor)@curma"/"%ansi(white)@maxma"ma "%ansi(@mvcolor)@curmv%ansi(white)"mv - "@weather">"

} {

#if (@timeofday = 0) {

#var timeofday 12

#var ampm am

#SUB %ansi(white)"~<"@timeofday@ampm" - "%ansi(white)"<"%ansi(@hpcolor)@curhp%ansi(white)"/"@maxhp"hp ~[+"%ansi(yellow)@diffhp%ansi(white)" Need:"%ansi(yellow)@needhp%ansi(white)"~] "%ansi(@macolor)@curma"/"%ansi(white)@maxma"ma "%ansi(@mvcolor)@curmv%ansi(white)"mv - "@weather">"

} {

#var ampm pm

#SUB %ansi(white)"~<"@timeofday@ampm" - "%ansi(white)"<"%ansi(@hpcolor)@curhp%ansi(white)"/"@maxhp"hp ~[+"%ansi(yellow)@diffhp%ansi(white)" Need:"%ansi(yellow)@needhp%ansi(white)"~] "%ansi(@macolor)@curma"/"%ansi(white)@maxma"ma "%ansi(@mvcolor)@curmv%ansi(white)"mv - "@weather">"

}

}

#if (@diffhp<>0) {#if (@diffhp>@hitup) {#if (@charname=@tank) {grouptell "["\d02@curhp\c03"|"\d04@maxhp\c03"]   "To Full:"<"\d02@needhp\c03">   "HEAL:"<+"\d04@diffhp\c03">"} {#SUB %ansi(white)"~<Time:"@timeofday@ampm" - "%ansi(white)"<"%ansi(@hpcolor)@curhp%ansi(white)"/"@maxhp"hp ~[+"%ansi(yellow)@diffhp%ansi(white)" Need:"%ansi(yellow)@needhp%ansi(white)"~] "%ansi(@macolor)@curma"/"%ansi(white)@maxma"ma>"}} {#if (@diffhp<@hitdown) {#if (@charname=@tank) {grouptell "["\d02@curhp\c03"|"\d04@maxhp\c03"]   "To Full:"<"\d02@needhp\c03">   "DAMG:"<"\d03@diffhp\c03">"} {#SUB %ansi(white)"~<Time:"@timeofday@ampm" - "%ansi(white)"<"%ansi(@hpcolor)@curhp%ansi(white)"/"@maxhp" ~["%ansi(yellow)@diffhp%ansi(white)" Need:"%ansi(yellow)@needhp%ansi(white)"~] "%ansi(@macolor)@curma"/"%ansi(white)@maxma"ma>"}}}}

}

Version 2.1 (without tank switch)

#ALIAS newprompt {prompt ~<Time ~= $t | $w | $h/$Hhp $m/$Mma $v/Vmv~>}

#TRIGGER {^~<Time = %1 ~| %2 ~| %3~/%4hp %5~/%6ma %7~/%8mv~>} {

#var timeofday %1

#var weather %2

#var curhp %3

#var maxhp %4

#var curma %5

#var maxma %6

#var curmv %7

#var maxmv %8

#math thirdhp @maxhp-(@maxhp/4)

#math halfhp @maxhp/2

#math criticalhp @maxhp/5

#math thirdma @maxma-(@maxma/4)

#math halfma @maxma/2

#math criticalma @maxma/5

#math thirdmv @maxmv-(@maxmv/4)

#math halfmv @maxmv/2

#math criticalmv @maxmv/5

#math diffhp (@curhp-@lasthp)

#math needhp %abs(@maxhp-@curhp)

#math lasthp @curhp

#VAR hitup {20}

#VAR hitdown {-20}

#if (@curhp>@thirdhp) {#var hpcolor green} {#if (@curhp<@thirdhp AND @curhp>@halfhp) {#var hpcolor cyan} {#if (@curhp<@halfhp AND @curhp>@criticalhp) {#var hpcolor yellow} {#if (@curhp<@criticalhp) {#var hpcolor red}}}}

#if (@curma>@thirdma) {#var macolor green} {#if (@curma<@thirdma AND @curma>@halfhp) {#var macolor cyan} {#if (@curma<@halfma AND @curma>@criticalma) {#var macolor yellow} {#if (@curma<@criticalma) {#var macolor red}}}}

#if (@curmv>@thirdmv) {#var mvcolor green} {#if (@curmv>@thirdmv AND @curmv>@halfmv) {#var mvcolor cyan} {#if (@curmv<@halfmv AND @curmv>@criticalmv) {#var mvcolor yellow} {#if (@curmv<@criticalmv) {#var mvcolor red}}}}

#if (@timeofday > 12) {

#math standardtime @timeofday-12

#var ampm am

#var timeofday @standardtime

#SUB %ansi(white)"~<"@timeofday@ampm" - "%ansi(white)"<"%ansi(@hpcolor)@curhp%ansi(white)"/"@maxhp"hp ~[+"%ansi(yellow)@diffhp%ansi(white)" Need:"%ansi(yellow)@needhp%ansi(white)"~] "%ansi(@macolor)@curma"/"%ansi(white)@maxma"ma "%ansi(@mvcolor)@curmv%ansi(white)"mv - "@weather">"

} {

#if (@timeofday = 0) {

#var timeofday 12

#var ampm am

#SUB %ansi(white)"~<"@timeofday@ampm" - "%ansi(white)"<"%ansi(@hpcolor)@curhp%ansi(white)"/"@maxhp"hp ~[+"%ansi(yellow)@diffhp%ansi(white)" Need:"%ansi(yellow)@needhp%ansi(white)"~] "%ansi(@macolor)@curma"/"%ansi(white)@maxma"ma "%ansi(@mvcolor)@curmv%ansi(white)"mv - "@weather">"

} {

#var ampm pm

#SUB %ansi(white)"~<"@timeofday@ampm" - "%ansi(white)"<"%ansi(@hpcolor)@curhp%ansi(white)"/"@maxhp"hp ~[+"%ansi(yellow)@diffhp%ansi(white)" Need:"%ansi(yellow)@needhp%ansi(white)"~] "%ansi(@macolor)@curma"/"%ansi(white)@maxma"ma "%ansi(@mvcolor)@curmv%ansi(white)"mv - "@weather">"

}

}

#if (@diffhp<>0) {#if (@diffhp>@hitup) {#SUB %ansi(white)"~<Time:"@timeofday@ampm" - "%ansi(white)"<"%ansi(@hpcolor)@curhp%ansi(white)"/"@maxhp"hp ~[+"%ansi(yellow)@diffhp%ansi(white)" Need:"%ansi(yellow)@needhp%ansi(white)"~] "%ansi(@macolor)@curma"/"%ansi(white)@maxma"ma>"}} {#SUB %ansi(white)"~<Time:"@timeofday@ampm" - "%ansi(white)"<"%ansi(@hpcolor)@curhp%ansi(white)"/"@maxhp" ~["%ansi(yellow)@diffhp%ansi(white)" Need:"%ansi(yellow)@needhp%ansi(white)"~] "%ansi(@macolor)@curma"/"%ansi(white)@maxma"ma>"}}}

Xandora

</div>

<div class="post" data-post-id="3720" data-author="Akasha2" data-date="2005-01-11T11:28:19+00:00">

Yes, I am never satisfied.  This version is the version I have decided to use myself.  It is simple, straight-forward, a single line, and constantly on, without any unnecessary spam.  It is a long single-line prompt > 59 characters (+/- 5 for hp length) < but it is neatly formatted, with a [+/-hp Need:x] slot right where your eyes would normally be during any particular momment.  Once again, this script is entirely self-contained and needs no on/off toggles to operate, it is always on.

Version 1.2 (w/o (@charname=@tank) switch : see my posts below if you don't know what I mean by this)

#ALIAS newprompt {prompt ~<Time ~= $t | $w | $h/$Hhp $m/$Mma $v/$Vmv~>}

#ALIAS hitup {#SUB %ansi(white)"~<"@timeofday@ampm" - "%ansi(white)"<"%ansi(@hpcolor)@curhp%ansi(white)"/"@maxhp"hp ~["%ansi(yellow)"+"@diffhp%ansi(white)" Need:"%ansi(yellow)@needhp%ansi(white)"~] "%ansi(@macolor)@curma"/"%ansi(white)@maxma"ma "%ansi(@mvcolor)@curmv%ansi(white)"mv> - "@weather">"}

#ALIAS hitdown {#SUB %ansi(white)"~<"@timeofday@ampm" - "%ansi(white)"<"%ansi(@hpcolor)@curhp%ansi(white)"/"@maxhp"hp ~["%ansi(red)@diffhp%ansi(white)" Need:"%ansi(yellow)@needhp%ansi(white)"~] "%ansi(@macolor)@curma"/"%ansi(white)@maxma"ma "%ansi(@mvcolor)@curmv%ansi(white)"mv> - "@weather">"}

#ALIAS nochange {#SUB %ansi(white)"~<"@timeofday@ampm" - "%ansi(white)"<"%ansi(@hpcolor)@curhp%ansi(white)"/"@maxhp"hp ~["%ansi(green)"0"%ansi(white)" Need:"%ansi(green)@needhp%ansi(white)"~] "%ansi(@macolor)@curma"/"%ansi(white)@maxma"ma "%ansi(@mvcolor)@curmv%ansi(white)"mv> - "@weather">"}

#TRIGGER {^~<Time = %1 ~| %2 ~| %3~/%4hp %5~/%6ma %7~/%8mv~>} {

#var timeofday %1

#var weather %2

#var curhp %3

#var maxhp %4

#var curma %5

#var maxma %6

#var curmv %7

#var maxmv %8

#math thirdhp @maxhp-(@maxhp/4)

#math halfhp @maxhp/2

#math criticalhp @maxhp/5

#math thirdma @maxma-(@maxma/4)

#math halfma @maxma/2

#math criticalma @maxma/5

#math thirdmv @maxmv-(@maxmv/4)

#math halfmv @maxmv/2

#math criticalmv @maxmv/5

#math diffhp (@curhp-@lasthp)

#math needhp %abs(@maxhp-@curhp)

#math lasthp @curhp

#var hitup {20}

#var hitdown {-20}

#math changema %abs(@curma-@lastma)

#if (@curhp>@thirdhp) {#var hpcolor green} {#if (@curhp<@thirdhp AND @curhp>@halfhp) {#var hpcolor cyan} {#if (@curhp<@halfhp AND @curhp>@criticalhp) {#var hpcolor yellow} {#if (@curhp<@criticalhp) {#var hpcolor red}}}}

#if (@curma>@thirdma) {#var macolor green} {#if (@curma<@thirdma AND @curma>@halfhp) {#var macolor cyan} {#if (@curma<@halfma AND @curma>@criticalma) {#var macolor yellow} {#if (@curma<@criticalma) {#var macolor red}}}}

#if (@curmv>@thirdmv) {#var mvcolor green} {#if (@curmv>@thirdmv AND @curmv>@halfmv) {#var mvcolor cyan} {#if (@curmv<@halfmv AND @curmv>@criticalmv) {#var mvcolor yellow} {#if (@curmv<@criticalmv) {#var mvcolor red}}}}

#if (@timeofday > 12) {

#math standardtime @timeofday-12

#var ampm am

#var timeofday @standardtime

} {#if (@timeofday = 0) {

#var timeofday 12

#var ampm am

} {#var ampm pm}}

#if (@diffhp=0) {nochange} {#if (@diffhp<>0) {#if (@diffhp<@hitdown) {hitdown} {#if (@diffhp>@hitup) {hitup} {nochange}}}}

}

Version 2.2 (with (@charname=@tank) switch)

#ALIAS newprompt {prompt ~<Time ~= $t | $w | $h/$Hhp $m/$Mma $v/$Vmv~>}

#ALIAS hitup {#if (@charname=@tank) {

grouptell "["\d02@curhp\c03"|"\d04@maxhp\c03"] "To Full:"<"\d02@needhp\c03"> "HEAL:"<+"\d04@diffhp\c03">"

#SUB %ansi(white)"~<"@timeofday@ampm" - "%ansi(white)"<"%ansi(@hpcolor)@curhp%ansi(white)"/"@maxhp"hp ~["%ansi(yellow)"+"@diffhp%ansi(white)" Need:"%ansi(yellow)@needhp%ansi(white)"~] "%ansi(@macolor)@curma"/"%ansi(white)@maxma"ma "%ansi(@mvcolor)@curmv%ansi(white)"mv> - "@weather">"

} {#SUB %ansi(white)"~<"@timeofday@ampm" - "%ansi(white)"<"%ansi(@hpcolor)@curhp%ansi(white)"/"@maxhp"hp ~["%ansi(yellow)"+"@diffhp%ansi(white)" Need:"%ansi(yellow)@needhp%ansi(white)"~] "%ansi(@macolor)@curma"/"%ansi(white)@maxma"ma "%ansi(@mvcolor)@curmv%ansi(white)"mv> - "@weather">"}}

#ALIAS hitdown {#if (@charname=@tank) {

grouptell "["\d02@curhp\c03"|"\d04@maxhp\c03"] "To Full:"<"\d02@needhp\c03"> "DAMG:"<"\d03@diffhp\c03">"

#SUB %ansi(white)"~<"@timeofday@ampm" - "%ansi(white)"<"%ansi(@hpcolor)@curhp%ansi(white)"/"@maxhp"hp ~["%ansi(red)@diffhp%ansi(white)" Need:"%ansi(yellow)@needhp%ansi(white)"~] "%ansi(@macolor)@curma"/"%ansi(white)@maxma"ma "%ansi(@mvcolor)@curmv%ansi(white)"mv> - "@weather">"

} {#SUB %ansi(white)"~<"@timeofday@ampm" - "%ansi(white)"<"%ansi(@hpcolor)@curhp%ansi(white)"/"@maxhp"hp ~["%ansi(red)@diffhp%ansi(white)" Need:"%ansi(yellow)@needhp%ansi(white)"~] "%ansi(@macolor)@curma"/"%ansi(white)@maxma"ma "%ansi(@mvcolor)@curmv%ansi(white)"mv> - "@weather">"}}

#ALIAS nochange {#SUB %ansi(white)"~<"@timeofday@ampm" - "%ansi(white)"<"%ansi(@hpcolor)@curhp%ansi(white)"/"@maxhp"hp ~["%ansi(green)"0"%ansi(white)" Need:"%ansi(green)@needhp%ansi(white)"~] "%ansi(@macolor)@curma"/"%ansi(white)@maxma"ma "%ansi(@mvcolor)@curmv%ansi(white)"mv> - "@weather">"}

#TRIGGER {^~<Time = %1 ~| %2 ~| %3~/%4hp %5~/%6ma %7~/%8mv~>} {

#var timeofday %1

#var weather %2

#var curhp %3

#var maxhp %4

#var curma %5

#var maxma %6

#var curmv %7

#var maxmv %8

#math thirdhp @maxhp-(@maxhp/4)

#math halfhp @maxhp/2

#math criticalhp @maxhp/5

#math thirdma @maxma-(@maxma/4)

#math halfma @maxma/2

#math criticalma @maxma/5

#math thirdmv @maxmv-(@maxmv/4)

#math halfmv @maxmv/2

#math criticalmv @maxmv/5

#math diffhp (@curhp-@lasthp)

#math needhp %abs(@maxhp-@curhp)

#math lasthp @curhp

#var hitup {20}

#var hitdown {-20}

#math changema %abs(@curma-@lastma)

#if (@curhp>@thirdhp) {#var hpcolor green} {#if (@curhp<@thirdhp AND @curhp>@halfhp) {#var hpcolor cyan} {#if (@curhp<@halfhp AND @curhp>@criticalhp) {#var hpcolor yellow} {#if (@curhp<@criticalhp) {#var hpcolor red}}}}

#if (@curma>@thirdma) {#var macolor green} {#if (@curma<@thirdma AND @curma>@halfhp) {#var macolor cyan} {#if (@curma<@halfma AND @curma>@criticalma) {#var macolor yellow} {#if (@curma<@criticalma) {#var macolor red}}}}

#if (@curmv>@thirdmv) {#var mvcolor green} {#if (@curmv>@thirdmv AND @curmv>@halfmv) {#var mvcolor cyan} {#if (@curmv<@halfmv AND @curmv>@criticalmv) {#var mvcolor yellow} {#if (@curmv<@criticalmv) {#var mvcolor red}}}}

#if (@timeofday > 12) {

#math standardtime @timeofday-12

#var ampm am

#var timeofday @standardtime

} {#if (@timeofday = 0) {

#var timeofday 12

#var ampm am

} {#var ampm pm}}

#if (@diffhp=0) {nochange} {#if (@diffhp<>0) {#if (@diffhp<@hitdown) {hitdown} {#if (@diffhp>@hitup) {hitup} {nochange}}}}

}

Xandora

</div>
