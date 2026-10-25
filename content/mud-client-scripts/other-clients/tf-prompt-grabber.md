---
title: "tf prompt grabber"
topic_id: 3977
author: "raincrab"
date: 2012-12-11T23:26:17+00:00
last_activity: 2012-12-11T23:26:17+00:00
last_author: "raincrab"
sticky: false
locked: false
post_count: 1
---

<div class="post" data-post-id="33837" data-author="raincrab" data-date="2012-12-11T23:26:17+00:00" data-subject="tf prompt grabber">

Someone asked for this on the newbie channel, here it is.

For whatever reason the prompt hook in tf doesnt always trigger regardless if lp is set or whether the prompt ends with a newline.  What does work is just treating the prompt as a trigger, gagging and processing it that way.  In sloth i have my prompt set as 'PROMPT $h/$H $m/$M $v/$V$nPROMPT $g $x $a $I $D $c $Z', splitting the prompt in 2 lines and prefixing each line with 'PROMPT'.

This code will gag the prompt, setup 3 status lines (actually 4, keeping the top one blank to keep a space between status bar and mud output).  Hp/ma/mv variables are colorized, auto reporting from you or others is also gagged, to ungag just remove the '-ag' from the trigger definitions.

```
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; prompt
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

; to set prompt in game do:
; prompt PROMPT $h/$H $m/$M $v/$V$nPROMPT $g $x $a $I $D $c $Z

/set status_pad= 
/set status_height=4

/status_add -c
/status_add -c -r1 stattopleft:32
/status_add -r1 stattopright:-0
/status_add -c -r2 statbottomleft:64
/status_add -r2 statbottomright:-0
/status_add -c -r3 statgroupleft:64

; multiply vars by 1.0 to force floating point division
/def updatestatus = \
	/if (({chp} * 1.0) / {mhp} <= .33) \
		/test hpstat := decode_attr("@{Cbrightred}%chp@{Cgray}/@{Cbrightred}%mhp@{Cgray}hp") %; \
	/endif %; \
	/if (({cma} * 1.0) / {mma} <= .33) \
		/test mastat := decode_attr("@{Cbrightred}%cma@{Cgray}/@{Cbrightred}%mma@{Cgray}ma") %; \
	/endif %; \
	/if (({cmv} * 1.0) / {mmv} <= .33) \
		/test mvstat := decode_attr("@{Cbrightred}%cmv@{Cgray}/@{Cbrightred}%mmv@{Cgray}mv") %; \
	/endif %; \
	/if (({chp} * 1.0) / {mhp} > .33) \
		/test hpstat := decode_attr("@{Cbrightyellow}%chp@{Cgray}/@{Cbrightyellow}%mhp@{Cgray}hp") %; \
	/endif %; \
	/if (({cma} * 1.0) / {mma} > .33) \
		/test mastat := decode_attr("@{Cbrightyellow}%cma@{Cgray}/@{Cbrightyellow}%mma@{Cgray}ma") %; \
	/endif %; \
	/if (({cmv} * 1.0) / {mmv} > .33) \
		/test mvstat := decode_attr("@{Cbrightyellow}%cmv@{Cgray}/@{Cbrightyellow}%mmv@{Cgray}mv") %; \
	/endif %; \
	/if (({chp} * 1.0) / {mhp} > .66) \
		/test hpstat := decode_attr("@{Cbrightgreen}%chp@{Cgray}/@{Cbrightgreen}%mhp@{Cgray}hp") %; \
	/endif %; \
	/if (({cma} * 1.0) / {mma} > .66) \
		/test mastat := decode_attr("@{Cbrightgreen}%cma@{Cgray}/@{Cbrightgreen}%mma@{Cgray}ma") %; \
	/endif %; \
	/if (({cmv} * 1.0) / {mmv} > .66) \
		/test mvstat := decode_attr("@{Cbrightgreen}%cmv@{Cgray}/@{Cbrightgreen}%mmv@{Cgray}mv") %; \
	/endif %; \
	/if (({tchp} * 1.0) / {tmhp} <= .33) \
		/test tstat := decode_attr("@{Cgray}Leader: @{Cbrightgreen}%leader @{Cgray}Tank: @{Cbrightred}%tank @{Cbrightred}%tchp@{Cgray}/@{Cbrightred}%tmhp @{Cbrightgreen}%tspells@{Cgray} Target: @{Cbrightgreen}%target") %; \
	/endif %; \
	/if (({tchp} * 1.0) / {tmhp} > .33) \
		/test tstat := decode_attr("@{Cgray}Leader: @{Cbrightgreen}%leader @{Cgray}Tank: @{Cbrightyellow}%tank @{Cbrightyellow}%tchp@{Cgray}/@{Cbrightyellow}%tmhp @{Cbrightgreen}%tspells@{Cgray} Target: @{Cbrightgreen}%target") %; \
	/endif %; \
	/if (({tchp} * 1.0) / {tmhp} > .66) \
		/test tstat := decode_attr("@{Cgray}Leader: @{Cbrightgreen}%leader @{Cgray}Tank: @{Cbrightgreen}%tank @{Cbrightgreen}%tchp@{Cgray}/@{Cbrightgreen}%tmhp @{Cbrightgreen}%tspells@{Cgray} Target: @{Cbrightgreen}%target") %; \
	/endif %; \
	/test exitstr := decode_attr("@{Cbrightgreen}%exits") %; \
	/set statgroupleft %tstat %; \
	/test statgroupleftlen := strlen(strip_attr(statgroupleft)) %; \
	/status_edit statgroupleft:%{statgroupleftlen} %; \
	/set stattopleft %hpstat %mastat %mvstat %; \
	/test stattopleftlen := strlen(strip_attr(stattopleft)) %; \
	/status_edit stattopleft:%{stattopleftlen} %; \
	/set statbottomright %exitstr %; \
	/set stattopright %loc %cont %; \
	/test stattoprightlen := $[ strlen(strip_attr(stattopright)) * -1 ] %; \
	/set statbottomleft %gold %exp %ac %hit %dam %; \
	/test statbottomleftlen := strlen(strip_attr(statbottomleft)) %; \
	/status_edit statbottomleft:%{statbottomleftlen}

/def -ag -mregexp -t"^PROMPT (\d+) (\d+) (\S+) (\S+) (\S+) (\S+) (.+)" = \
	/test gold := decode_attr("@{Cbrightgreen}%P1@{Cgray}g") %; \
	/test exp := decode_attr("@{Cbrightgreen}%P2@{Cgray}x") %; \
	/test ac := decode_attr("@{Cbrightgreen}%P3@{Cgray}ac") %; \
	/test hit := decode_attr("@{Cbrightgreen}%P4@{Cgray}hit") %; \
	/test dam := decode_attr("@{Cbrightgreen}%P5@{Cgray}dam") %; \
	/test cont := decode_attr("@{Cgray}(@{Cbrightgreen}%P6@{Cgray})") %; \
	/test loc := decode_attr("@{Cbrightgreen}%P7") %; \
	/test prompt("> ") %; \
	/updatestatus

; for lowbies who cant see ac or hit/dam
/def -ag -mregexp -t"^PROMPT (\d+) (\d+)    (\S+) (.+)" = \
	/test gold := decode_attr("@{Cbrightgreen}%P1@{Cgray}g") %; \
	/test exp := decode_attr("@{Cbrightgreen}%P2@{Cgray}x") %; \
	/test ac := decode_attr("@{Cbrightgreen}0@{Cgray}ac") %; \
	/test hit := decode_attr("@{Cbrightgreen}0@{Cgray}hit") %; \
	/test dam := decode_attr("@{Cbrightgreen}0@{Cgray}dam") %; \
	/test cont := decode_attr("@{Cgray}(@{Cbrightgreen}%P6@{Cgray})") %; \
	/test loc := decode_attr("@{Cbrightgreen}%P7") %; \
	/test prompt("> ") %; \
	/updatestatus

/def -ag -mregexp -t"^PROMPT (\S+)/(\S+) (\S+)/(\S+) (\S+)/(\S+)$" = \
	/test chp := strip_attr("%P1") %; \
	/test mhp := strip_attr("%P2") %; \
	/test cma := strip_attr("%P3") %; \
	/test mma := strip_attr("%P4") %; \
	/test cmv := strip_attr("%P5") %; \
	/test mmv := strip_attr("%P6") %; \
	/updatestatus

/def -mregexp -t"^Exits: (.+)  " = \
	/set exits %P1 %; \
	/updatestatus

/def -ag -mregexp -t"^(\S+) reports (\d+)/(\d+) (.+) Spells: (.+)\." = \
	/set tank %P1 %; \
	/set tchp %P2 %; \
	/set tmhp %P3 %; \
	/set tspells %P5 %; \
	/updatestatus

/def -ag -mregexp -t"^(\S+) report (\d+)/(\d+) (.+)" = \
	/set tank %charname %; \
	/set tchp %P2 %; \
	/set tmhp %P3 %; \
	/set tspells= %; \
	/updatestatus
	
/def -mregexp -t"^You are rescued by (\S+)\, you are confused\!" = \
	/set tank %P1 %; assist %P1 %; /updatestatus
```

</div>
