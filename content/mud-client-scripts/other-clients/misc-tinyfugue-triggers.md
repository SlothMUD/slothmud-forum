---
title: "misc tinyfugue triggers"
topic_id: 3984
author: "raincrab"
date: 2012-12-19T23:10:51+00:00
last_activity: 2012-12-31T01:04:32+00:00
last_author: "blackmore"
sticky: false
locked: false
post_count: 3
---

<div class="post" data-post-id="33854" data-author="raincrab" data-date="2012-12-19T23:10:51+00:00" data-subject="misc tinyfugue triggers">

```
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; config
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

/set charname Raincrab
/set gjob bonyx jet
/set channel russian
/set weapon dagger
/set container sack
/set wcontainer Specialization
/set kcontainer tube
/set gcontainer chest
/set ccontainer backpack
/set drink keg
/set title %s
/set mywarcry WITTY WARCRY GOES HERE

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; aliases
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

/hook send k * = /set target %2 %; /bstab %target
/hook send k = /bstab %target
/hook send lt = look %target
/hook send sac = sac corpse
/hook send gac = get all corpse
/hook send ws = wake %; stand
/hook send bs * = backstab %2
/hook send q * = quaff %2
/hook send mb = man back
/hook send gt * = grouptell %-1
/hook send c * = cast '%-1'
/hook send c = circle
/hook send ss = sing stop
/hook send g = group
/hook send rr = |%;cast 'word of recall'
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; container management
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

; iget/iput uses container in inventory
; wget/wput uses worn container
; kget/kput uses key container inside worn container
; gget/gput uses gem container inside worn container
; cget/cput uses cp container inside worn container

/def iput = put %{*} %container
/def iget = get %{*} %container

/def wget = remove %wcontainer %; get %{*} %wcontainer %; wear %wcontainer
/def wput = remove %wcontainer %; put %{*} %wcontainer %; wear %wcontainer

/def kget = /wget %kcontainer %; get %{*} %kcontainer %; /wput %kcontainer
/def kput = /wget %kcontainer %; put %{*} %kcontainer %; /wput %kcontainer

/def gget = /wget %gcontainer %; get %{*} %gcontainer %; /wput %gcontainer
/def gput = /wget %gcontainer %; put %{*} %gcontainer %; /wput %gcontainer

/def cget = /wget %ccontainer %; get %{*} %ccontainer %; /wput %ccontainer
/def cput = /wget %ccontainer %; put %{*} %ccontainer %; /wput %ccontainer

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; movement
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

/def -mregexp -t"^The (\S+) to the (\S+) seems to be closed\." = \
	open %P1 %P2 %; /set barrier %P1 %; /set barrierdir %P2

/def -mregexp -t"^The (\S+) (\S+)wards seems to be closed\." = \
	open %P1 %P2 %; /set barrier %P1 %; /set barrierdir %P2

/def -mregexp -t"^It seems to be locked\." = \
	pick %barrier %barrierdir
	
/def -mregexp -t"^You board" = /set boat 1 %; where

/def -mregexp -t"^The ship has arrived at*" = \
	/if ({boat} == 1) \
		/if ({sleeping} == 1) \
			wake %; stand %; \
		/endif %; \
		exit %; \
		/set boat 0 %; \
		cast 'word of recall' %; \
	/endif

/def -mregexp -t"^(.+) arrives at the dock, ties up and puts out a plank\." = \
	/if ({boat} == 1) \
		/if ({sleeping} == 1) \
			wake %; stand %; \
		/endif %; \
		exit %; \
		/set boat 0 %; \
	/endif
	
; tracking
/def -mregexp -t"^Tracks to (.+) lead (\S+)ward" = \
	%P2 %; \
	/if ({stab} == 1) \
		/bstab %; \
	/endif

/def -mregexp -t"^The white aura around your body fades\." = \
	/if ({group} == 1) \
		gt *** lites out *** %; \
	/endif %; \
	/if ({autobuff} == 1) \
		/if ({sleeping} == 0) \
			/if ({reading} == 0) \
				cast 'sanctuary' %; \
			/endif %; \
		/endif %; \
	/endif

/def -p1 -mregexp -t"^You start glowing" = \
	/if ({group} == 1) \
		gt *** lites on *** %; \
	/endif

/def -p1 -mregexp -t"^You are surrounded by a radiant light." = \
	/if ({group} == 1) \
		gt *** lites on *** %; \
	/endif

/def -p1 -mregexp -t"^The radiant sphere around your body fades" = \
	/if ({group} == 1) \
		gt *** lites out *** %; \
	/endif

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; spells
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

/def aegis = cast 'aegis'
/def armor = cast 'armor'
/def bset = cast 'lloyds beacon' set
/def bback = cast 'lloyds beacon' return
/def bless = cast 'bless'
/def dark = cast 'darkness' %charname
/def darksi = cast 'darksight'
/def detinv = cast 'detect invis'
/def embalm = cast 'embalm' %{*}
/def feast = cast 'feast'
/def fluid = cast 'fluid'
/def fly = cast 'fly'
/def gate = cast 'gate' %{*}
/def ham = cast 'spiritual hammer'
/def heal = cast 'greater heal' %{*}
/def invis = cast 'invis'
/def locate = cast 'locate' %{*}
/def mfly = cast 'mass fly'
/def mwb = cast 'mass water breath'
/def quake = cast 'earthquake'
/def rec = cast 'word of recall' %; /set target null
/def refresh = cast 'refresh'
/def sanc = cast 'sanctuary'
/def shield = cast 'shield'
/def stone = cast 'stone skin'
/def supp = cast 'supp' %{*}
/def visage = cast 'undead visage'
/def wb = cast 'water breath'
/def web = cast 'web' %target
/def rempois = cast 'remove poison' raincrab
/def resfire = cast 'resist fire'
/def rescold = cast 'resist cold'

/def bro = sing 'brothers'
/def lion = sing 'lion'
/def dreams = sing 'dreams'

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; healing
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

/def in = /set inforheals 1 %; gt im in for heals with %cma mana
/def out = /set inforheals 0 %; gt im out of heals
/def ht = /heal %tank

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; combat
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

/def -mregexp -ag -t"^You miss (.+) with your (.+)"
/def -mregexp -ag -t"^(.+) misses (.+) with (his|her|its) (.+)"

/def -mregexp -t"^You are knocked off your feet*" = stand
/def -mregexp -t"^You try to stand\, but are beaten back" = stand
/def -mregexp -t"^You attempt to (.+) but bounce off" = stand
/def -mregexp -t"^(.+) disarms you with a quick parry\." = wield %weapon

/def -mregexp -t"^Total exp for kill is *" = \
	/set target null %; \
	/if ({autowarcry} == 1) \
		warcry %mywarcry %; \
	/endif

/set hammer 0
/def hammer = \
	/if ({hammer} == 1) \
		rem hammer %; \
		wield %weapon %; \
		/set hammer 0 %; \
	/else \
		rem %weapon %; \
		wield hammer %; \
		/set hammer 1 %; \
	/endif

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; food & drink
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

/set sleeping 0
/set reading 0

/def -mregexp -t"^You are hungry\." = \
	/if ({sleeping} == 1) \
		/let wassleeping 1 %; \
		wake %; stand %; \
	/endif %; \
	/if ({reading} == 0) \
		eat food %; \
	/endif %; \
	/if ({wassleeping} == 1) \
		/let wassleeping 0 %; \
		sleep %; \
	/endif

/def -mregexp -t"^You are starting to get a little peckish\." = \
	/if ({sleeping} == 1) \
		/let wassleeping 1 %; \
		wake %; stand %; \
	/endif %; \
	/if ({reading} == 0) \
		eat food %; \
	/endif %; \
	/if ({wassleeping} == 1) \
		/let wassleeping 0 %; \
		sleep %; \
	/endif
	
/def -mregexp -t"^You are thirsty\." = \
	/if ({sleeping} == 1) \
		/let wassleeping 1 %; \
		wake %; stand %; \
	/endif %; \
	/if ({reading} == 0) \
		drink %drink %; drink %drink %; \
	/endif %; \
	/if ({wassleeping} == 1) \
		/let wassleeping 0 %; \
		sleep %; \
	/endif
	
/def -mregexp -t"^Your throat is starting to get dry\." = \
	/if ({sleeping} == 1) \
		/let wassleeping 1 %; \
		wake %; stand %; \
	/endif %; \
	/if ({reading} == 0) \
		drink %drink %; drink %drink %; \
	/endif %; \
	/if ({wassleeping} == 1) \
		/let wassleeping 0 %; \
		sleep %; \
	/endif
	
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; refills
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

/def -mregexp -t"^A pool of water gushes from a fountain*" = fill %drink
/def -mregexp -t"^A large wishing well\, with a bench*" = fill %drink
/def -mregexp -t"^A large fountain is here gurgling out an*" = fill %drink
/def -mregexp -t"^The large central well of Settlestone*" = fill %drink
/def -mregexp -t"^A stone well stands in the middle of the*" = fill %drink

/def food = c create food %; get food 
/def drink = drink %drink %; drink %drink
/def fill = cast 'create water' %drink
/def refill = fill %drink
/def eat = eat food

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; grouping
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

/def gjob = \
	/set gjob %{*} %; \
	gjob %gjob

/def t = /set target %{*} %; \
	/if ({group} == 1) \
		gt target %target %; \
	/endif

/def group = \
	/if ({group} == 1) \
		/set group 0 %; \
	/else \
		/set group 1 %; \
	/endif

/def leader = /set leader %{*}

/def -mregexp -t"^You now follow (\S+)\." = \
	/set group 1 %; \
	/set leader %P1 %; \
	gjob %gjob

/def -mregexp -t"^The group has disbanded\." = \
	/set group 0 %; \
	/set leader %charname %; \
	group %charname

/def -mregexp -t"^You disband your group\." = \
	/set group 0 %; \
	/set leader %charname %; \
	group %charname

/def -mregexp -t"^(\S+) starts following you\." = \
	/if ({group} == 0) \
		/set group 1 %; \
		gjob %gjob %; \
	/endif
	
/def -mregexp -t"^You are now leading*" = \
	/set group 1 %; \
	/set leader %charname %; \
	gjob %gjob

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; stab
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

/def bstab = /if ({target} !~ "null") backstab %target %; /endif

/def -mregexp -t"You follow*" = \
	/if ({group} == 1) \
		/if ({stab} == 1) \
			/bstab %; \
		/endif %; \
	/endif

/def stab = \
	/if ({stab} == 0) \
		/set stab 1 %; \
		gt stab on %; \
	/else \
		/set stab 0 %; \
		gt stab off %; \
	/endif
	
/def allup = wake %; stand %; gt all up
/def regen = sleep %; gt regen
/def pos = /set position %{*}
/def ass = assist %tank

/def spin = /wget wheel %; spin wheel %; /wput wheel

/def -mregexp -t"^Your front line collapses*" = \
	/if ({position} =~ "back") \
		 man back %; \
	 /endif
	 
/def -mregexp -t"^You stumble as you try to move*" = man back

/def -mregexp -t"^(\S+) yells \'(.+)\'" = \
	/if ({group} == 1) \
		warcry %P2 %; \
	/endif

/def -mregexp -t"^You are covered in sticky webs\!" = \
	/set webbed 1 %; \
	/if ({group} == 1) \
		gt im webbed %; \
	/endif

/def -mregexp -t"^The webs tighten about you\." = squirm
/def -mregexp -t"^You struggle to break free from the webs" = squirm
/def -mregexp -t"You break free of the webs\!" = /set webbed 0

/hook send n = \
	/if ({webbed} == 1) \
		/if ({group} == 1) \
			gt im still webbed %; \
		/endif %; \
		squirm %; \
	/else \
		north %; \
		/if ({stab} == 1) \
			/bstab %; \
		/endif %; \
	/endif

/hook send s = \
	/if ({webbed} == 1) \
		/if ({group} == 1) \
			gt im still webbed %; \
		/endif %; \
		squirm %; \
	/else \
		south %; \
		/if ({stab} == 1) \
			/bstab %; \
		/endif %; \
	/endif

/hook send e = \
	/if ({webbed} == 1) \
		/if ({group} == 1) \
			gt im still webbed %; \
		/endif %; \
		squirm %; \
	/else \
		east %; \
		/if ({stab} == 1) \
			/bstab %; \
		/endif %; \
	/endif

/hook send w = \
	/if ({webbed} == 1) \
		/if ({group} == 1) \
			gt im still webbed %; \
		/endif %; \
		squirm %; \
	/else \
		west %; \
		/if ({stab} == 1) \
			/bstab %; \
		/endif %; \
	/endif

/hook send u = \
	/if ({webbed} == 1) \
		/if ({group} == 1) \
			gt im still webbed %; \
		/endif %; \
		squirm %; \
	/else \
		up %; \
		/if ({stab} == 1) \
			/bstab %; \
		/endif %; \
	/endif

/hook send d = \
	/if ({webbed} == 1) \
		/if ({group} == 1) \
			gt im still webbed %; \
		/endif %; \
		squirm %; \
	/else \
		down %; \
		/if ({stab} == 1) \
			/bstab %; \
		/endif %; \
	/endif

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; group
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

/def -mregexp -t"^(\S+) \-\- \'all up\'" = \
	/if ({leader} =~ {P1}) \
		wake %; stand %; salute %leader %; \
	/endif

/def -mregexp -t"^(\S+) \-\- \'regen\'" = \
	/if ({leader} =~ {P1}) \
		sleep %; \
	/endif
	
/def -mregexp -t"^(\S+) \-\- \'catch\'" = \
	/if ({leader} =~ {P1}) \
		sleep %; \
	/endif
	
/def -mregexp -t"^(\S+) \-\- \'visage\'" = \
	/if ({leader} =~ {P1}) \
			cast 'undead visage' %; \
	/endif
	
/def -mregexp -t"^(\S+) \-\- \'recall\'" = \
	/if ({leader} =~ {P1}) \
			wake %; stand %; salute %leader %; \
	/endif
	
/def -mregexp -t"^(\S+) \-\- \'all up\'" = \
	/if ({leader} =~ {P1}) \
			wake %; stand %; salute %leader %; \
	/endif

/def -mregexp -t"^(\S+) \-\- \'target (.+)\'" = \
	/if ({group} == 1) \
		/if ({leader} =~ {P1}) \
			/set target %P2 %; \
			sneak %; \
			/if ({stab} == 1) \
				/bstab %; \
			/endif %; \
		/endif %; \
	/endif

/def -mregexp -t"^(\S+) \-\- \'qstab\'" = \
	/if ({leader} =~ {P1}) \
		/if ({stab} == 1) \
			/bstab %; \
		/endif %; \
	/endif

/def -mregexp -t"^(\S+) has just entered the portal\." = \
	/if ({leader} =~ {P1}) \
		enter portal %; \
	/endif

/def -mregexp -t"^(\S+) disappears into a large diamond\." = \
	/if ({leader} =~ {P1}) \
		open diamond %; \
	/endif
	
/def -mregexp -t"^(\S+) enters the archway*" = \
	/if ({leader} =~ {P1}) \
		enter archway %; \
	/endif

/def -mregexp -t"^(\S+) enters the glowing archway*" = \
	/if ({leader} =~ {P1}) \
		enter archway %; \
	/endif

/def -mregexp -t"^(\S+) picks up a feather quill from an ink flask*" = \
	/if ({leader} =~ {P1}) \
		sign ledger %; \
	/endif
	
/def -mregexp -t"^(\S+) steps toward the red portal\." = \
	/if ({leader} =~ {P1}) \
		enter red %; \
	/endif
	
/def -mregexp -t"^You feel yourself suddenly dragged through the ether\!" = \
	salute %leader

/def -mregexp -t"^(\S+) heroically rescues (\S+)\." = \
	/if ({P1} =~ {tank}) \
		assist %P1 %; \
	/endif

/def -mregexp -t"^(\S+) circles around (.+) and expertly puts (\S+) in a deathgrip\." = \
	/if ({group} == 1) \
		assist %P1 %; \
	/endif

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; chop
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

/def -mregexp -t"^As you swing your weapon\, it slips and slices through (\S+)\'s neck\!" = \
	gt i chopped %P1 %; get head
	
/def -mregexp -t"^(\S+) wildly swings (.+)\, and accidentally cuts off (\S+) own head\!" = \
	gt %P1 took the easy way out

/def -mregexp -t"^(\S+) wildly swings (.+)\, and accidentally cuts off (\S+)\'s head\!" = \
	gt %P1 chopped %P3 %; highfive %P1

/def -mregexp -t"^As (\S+) hits (.+) with (.+) it shatters into thousands of pieces\." = \
	gt %P1 broke %P3 %; slap %P1
	
/def -mregexp -t"^(\S+) shatters the handle of (\S+) (\S+)\!" = \
	gt %P1 broke %P3 %; slap %P1

/def -mregexp -t"^Your weapon shatters as it hits your victim\." = \
	gt i just broke my chopper %; wield chopper
```

</div>

<div class="post" data-post-id="33874" data-author="Tuck" data-date="2012-12-30T21:13:32+00:00" data-subject="Re: misc tinyfugue triggers">

Good job Rain!

Especially channel name :-)

</div>

<div class="post" data-post-id="33876" data-author="blackmore" data-date="2012-12-31T01:04:32+00:00" data-subject="Re: misc tinyfugue triggers">

I do this for spell macros:

-- if I want myself to be the default, but accepts a target

/def fly = cast 'fly' %{1-%{myname}}

-- if I want the target to be the default, but accepts a target

/def damn = cast 'damnation' %{1-%{target}}

</div>
