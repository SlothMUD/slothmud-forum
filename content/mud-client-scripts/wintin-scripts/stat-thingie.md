---
title: "stat thingie"
topic_id: 2768
author: "Alberich"
date: 2008-03-23T06:24:20+00:00
last_activity: 2008-03-23T20:55:47+00:00
last_author: "*juggleblood*"
sticky: false
locked: false
post_count: 3
---

<div class="post" data-post-id="23376" data-author="Alberich" data-date="2008-03-23T06:24:20+00:00">

this is what i did instead of cleaning my house this morning :P

you will probably have to fix the formatting a little bit and i do not want any crap about the awful window layout.  I do not know html.  If anyone does and uses this, and makes a nice looking table layout, I would appreciate it if you'd share it with me :)

this will create a little popup window that tracks that status of your spells.

when they fall, it will let you click on them to recast.  It's set up only for the spells i actually care about and could be bothered to track down triggers for this morning, i'm still working on it.  add/change/whatever you  find useful.

after you read in the file just type startstat to start the window and populate it with the default variables.  i have them set to unknown for the most part, you can change as suits

#defgroup {Spelltracker}

#var {strstat} {Str, <c yellow>unknown</c>}

#var {skinstat} {<SEND cas 'iron skin' $me>Skin</SEND>, <c red>Down</c>}

#var {mobistat} {Mobi, <c yellow>unknown</c>}

#var {insstat} {Insight, <c yellow>unknown</c>}

#var {corstat} {Corona, <c yellow>unknown</c>}

#var {stamstat} {Stamina, <c yellow>unknown</c>}

#var {vitstat} {Vitality, <c yellow>unknown</c>}

#var {rejuvstat} {Rejuv, <c yellow>unknown</c>}

#var {sancstat} {Aegis, {<SEND cas 'aegis' $me>Aegis</SEND>, <c ed>Unlit</c>}>

#al {startstat} {statuswin;updatestat;update}

#al {statuswin} {#htmlpopup Status;#sendtowin Status {#table 9 2 <BODY TEXT="#FFFFFF" BGCOLOR="#000000">} {ALIGN=center CELLSPACING=5} } }

#ac {You feel weaker.} {#var {strstat} {<SEND cas 'vigor'>Str</SEND>, <c red>Down</c>};updatestat;update }

#ac {You feel stronger.} {#var {strstat} {Str, <c green>Up</c>};updatestat;update }

#ac {Your skin hardens greatly, becoming almost impenetrable.} {#var {skinstat} {Skin, <c green>IronSkin</c>};updatestat;update }

#ac {You feel less protected.} {#var {skinstat} {<SEND cas 'iron skin' $me>Skin</SEND>, <C red>Down</c>};updatestat;update }

#ac {You feel lethargic.} {#var {mobistat} {<SEND cas 'mobi' $me>Mobi</SEND>, <c red>Down</c>};updatestat;update }

#ac {You feel a burst of energy run through your legs.} {#var {mobistat} {Mobi, <c green>Up</c>};updatestat;update }

#ac {You suddenly feel slightly less healthy...} {#var {rejuvstat} {<SEND cas 'rejuv' $me>Rejuv</SEND>, <c red>Down</c>};updatestat;update }

#ac {Your wounds begin to heal much faster!} {#var {rejuvstat} {Rejuv, <c green>Rejuv</c>};updatestat;update }

#ac {You feel wiser.} {#var {insstat} {Insight, <c green>Up</c>};updatestat;update }

#ac {You feel less wise.} {#var {insstat} {<SEND cas 'insight'>Insight</SEND>, <c red>Down</c>};updatestat;update }

#ac {You feel less sturdy.} {#var {vitstat} {<SEND cas 'vitality'>Vitality</SEND>, <c red>Down</c>};updatestat;update }

#ac {You feel sturdier.} {#var {vitstat} {Vitality, <c green>Up</c>};updatestat;update }

#ac {You feel more magically charged.} {#var {corstat} {Corona, <c green>Up</c>};updatestat;update }

#ac {You feel less magically charged.} {#var {corstat} {<SEND cas 'corona'>Corona</SEND>, <c 

red>Down</c>};updatestat;update }

#ac {You feel less resilient.} {#var {stamstat} {<SEND cas 'stamina'>Stamina</SEND>, <c red>Down</c>};updatestat;update }

#ac {A feeling of increased power courses through your body.} {#var {stamstat} {Stamina, <c 

green>Up</c>};updatestat;update }

#ac {You are surrounded by a radiant light.} {#var {sancstat} {Aegis, <c green>UP</c>};updatestat;update }

#ac {A dark haze precipitates around your body.} {#var {sancstat} Aegis, <c grey>CLOAKED</c>};updatestat;update }

#ac {You go to sleep.} {#var {sleepstat} {Asleep} }

#ac {You wake, and sit up.} {#var {sleepstat} {Awake} }

#ac {You sit down and rest your tired bones} {#var {sleepstat} {Resting} }

#ac {You stop resting, and stand up.} {#var {sleepstat} {Awake} }

#al {updatestat} {#var {totalstat} {$strstat, $skinstat, $mobistat, insstat, $corstat, $stamstat, $vitstat, $rejuvstat, $sancstat} }

#al {update} {#sendtowin Status {#fill $totalstat} }

</div>

<div class="post" data-post-id="23378" data-author="jezer" data-date="2008-03-23T11:12:25+00:00">

Not to take anything away from your script, but I'd thought I'd share how I get around a similar problem. This is an adaption of some stuff I read in the helpfiles.

#defgroup {Readiness}

#alias  {fight} {#cap temp {^<} {A|#loop {$wantedspells} {#select {temp, missing, %%0} {cast '$spellmap[%0]' $me}};#showme $eqmode MODE;};score;#var temp 0} {G|Readiness} {T|WT}

#alias  {miss} {#cap temp {^<} {A|#loop {$preferedspells} {#select {temp, missing, %%0} {#showme Missing: [%0]}};#showme $eqmode MODE;};score;} {G|Readiness} {T|WT}

#variable  {preferedspells} {Strength, Stone Skin, Detect Invisible, Greater Fluidity, Darksight, Shield of Thorns, Fly, Water Breathing, Sanctuary} {G|Readiness}

#variable  {spellmap} {Infravision, Infravision, Strength, Strength, Stone Skin, Stone Skin, Sanctuary, Sanctuary, Sense Life, Sense Life, Detect Invisible, Detect Invisibility, Bless, Bless, Shield of Thorns, Shield of Thorns, Darksight, Darksight, Greater Fluidity, Greater Fluidity, Regeneration, Regeneration} {G|Readiness}{T|WT}

#variable  {wantedspells} {Strength, Stone Skin, Detect Invisible, Greater Fluidity, Darksight, Shield of Thorns} {G|Readiness}{T|WT}

#defgroup {}

Basically, the idea is, you set up the spells you always want to be up in a variable, and you setup there "called" names in another variable. When you type "score" the script grabs the spells that you have up, and it just casts the ones that it did not find. It works a treat... however there is a bug that often causes the script to recast all spells... but that only happens when there is action in the room.

All I have to do is type "fight" and all my spells I needed are cast. I wouldn't recommend you use this unless your going to understand it and adapt it, it's kind of not "copy n paste" ready, if you get what I mean, but it does the job, non the less.

</div>

<div class="post" data-post-id="23383" data-author="*juggleblood*" data-date="2008-03-23T20:55:47+00:00">

Nice

thx Alberich

</div>
