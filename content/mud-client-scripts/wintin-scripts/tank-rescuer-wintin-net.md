---
title: "Tank Rescuer Wintin.NET"
topic_id: 759
author: "*Splork*"
date: 2005-01-20T20:41:57+00:00
last_activity: 2006-08-16T05:25:25+00:00
last_author: "Weasel"
sticky: false
locked: false
post_count: 7
---

<div class="post" data-post-id="3850" data-author="*Splork*" data-date="2005-01-20T20:41:57+00:00">

Please change strings if anyone uses this...

#defgroup Tank-Rescuer

#action  {$stb places %0} {rescue $stb;#var rescuee $stb} {G|Tank-Rescuer}

#action  {but nearly cut} {rescue $stb;#var rescuee $stb} {G|Tank-Rescuer}

#action  {^$tank is dead! R.I.P.} {gt I R tank now!!;whinet} {G|Tank-Rescuer}

#action  {disengages himself, and attacks %1!} {rescue $1;#var rescuee $1} {G|Tank-Rescuer}

#action  {sees %1, and attacks!} {rescue $1;#var rescuee $1} {G|Tank-Rescuer}

#action  {SEEK SHELTER AT ONCE! %1 has begun to sing.} {rescue $1;#var rescuee $1} {G|Tank-Rescuer}

#action  {$stb place %0} {rescue $stb;#var rescuee $stb} {G|Tank-Rescuer}

#action  {You fail the rescue} {rescue $rescuee} {G|Tank-Rescuer}

#alias  {rescallof} {gt I will no longer TRY to rescue you wussies...;rescdisof;rescseeof;rescsingof;rescstabof} {G|Tank-Rescuer}

#alias  {rescallon} {gt I will now TRY to rescue everybody (SING for it ppl);rescdison;rescseeon;rescsingon;rescstabon} {G|Tank-Rescuer}

#alias  {rescdisof} {#unac {disengages himself, and attacks %1!}} {G|Tank-Rescuer}

#alias  {rescdison} {#ac {disengages himself, and attacks %1!} {rescue $1;#var rescuee $1} ;rescfailon} {G|Tank-Rescuer}

#alias  {rescfailof} {#unac {You fail the rescue}} {G|Tank-Rescuer}

#alias  {rescfailon} {#ac {You fail the rescue} {rescue $rescuee} } {G|Tank-Rescuer}

#alias  {rescseeof} {#unac {sees %1, and attacks!}} {G|Tank-Rescuer}

#alias  {rescseeon} {#ac {sees %1, and attacks!} {rescue $1;#var rescuee $1}; rescfailon} {G|Tank-Rescuer}

#alias  {rescsingof} {#unac {SEEK SHELTER AT ONCE! %1 has begun to sing.}} {G|Tank-Rescuer}

#alias  {rescsingon} {#ac {SEEK SHELTER AT ONCE! %1 has begun to sing.} {rescue $1;#var rescuee $1}; rescfailon} {G|Tank-Rescuer}

#alias  {rescstabof} {#unac {$stb place %0};#unac {$stb tried %0}} {G|Tank-Rescuer}

#alias  {rescstabon} {#ac {$stb place %0} {rescue $stb;#var rescuee $stb}#ac {but nearly cut} {rescue $stb;#var rescuee $stb} ;rescfailon } {G|Tank-Rescuer}

#alias  {altankof} {#show ***** I R NOT 2nd TANK ANYMORE *****;#unac {^$tank is dead! R.I.P.}} {G|Tank-Rescuer}

#alias  {altankon} {#show ***** I R 2nd TANK NOW *****;#ac {^$tank is dead! R.I.P.} {gt I R tank now!!;whinet}} {G|Tank-Rescuer}

</div>

<div class="post" data-post-id="13711" data-author="bibbidi" data-date="2006-08-14T14:32:22+00:00">

General

Someone was gossiping a request for rescue trigger phrases earlier today, I thought I'd already posted them, but now I look at them I realise why I didn't:

1. Splork seems to have covered it already in this thread

2. My scripts are not what I'd call perfect, but they are the scripts I use when tanking, and seem to work ok.

I'll post them now to start the ball rolling and see if we can perhaps get some better ones by the end of it.

Some of them are unanchored and need improving, I'd welcome fullly anchored trigger phrases to do that. (Although answers to that are probably in Splorks post)

Toggling

I find toggling on and off useful, wintin does this better than my client but the way I do it is I have a toggle variable gr_res, only if this is set to 1 do any of these scripts do anything.

Designating group stabber:

I use the variable gr_stab to denote the name of a stabber I will attempt to rescue, this prevents rescueing non group members (or mobs) you come across.

Retries

When I attempt a rescue I denote the 'victim' i.e. someone who needs rescueing I tag them as gr_vic this aids retrying failed rescues.

Overkill

These scripts will on occasion try to rescue more than once, I don't see this is an issue as it dosen't take much movement to attempt to rescue someone not engaged.

Better more than less here.

Client

These are not wintin scripts, I use AL Client, but you should be able easily modify, or use as a base to write your own.

(In my client ^ anchors a trigger)

Backstabbing

^%0 tried to backstab %1

^%0 places %1

#set dum %0;

#if (stricmp(gr_stab,dum) == 0) 

{#if (gr_res=1) {#set gr_vic %0;rescue %0}}

Note: stricmp is a string comparison function

Failed Backstab ???

but nearly cut

(severly unanchored and needs improvement) 

#if (gr_res=1)

{#unset gr_vic;#strcat(gr_vic,gr_stab);rescue $gr_vic$}

Requested Rescue

^SEEK SHELTER AT ONCE! %1 has begun to sing.

#if (gr_res=1)

{#set gr_vic %1;rescue %1}

Retry Rescue

^You fail the rescue

#if (gr_res=1)

{rescue $gr_vic$}

Mob Engages Party Member

(not the best triggers as 1. unanchored and 2. has potential to rescue non party members ... suggestions on a postcard please)

disengages himself, and attacks %1!

sees %1, and attacks!

#if (gr_res=1)

{#set gr_vic %1;rescue %1}

Deathgrip

(Again unanchored and 1st trigger probably unnecessary as I think you only need to rescue a gripper when grip ends but I've never played a monk so not sure, also need to be tied to designated gripper)

expertly touches and maintains his deathgrip

smartly steps out

#if (gr_res=1)

{#unset gr_vic;#strcat(gr_vic,gr_stab);rescue $gr_vic$}

</div>

<div class="post" data-post-id="13712" data-author="12345" data-date="2006-08-14T21:21:58+00:00">

I'll post mine, also far from perfect.  I honestly ignore things such as the stabber and gripper vars, partly because I shut my rescuer off when not needed and partly because in thousands of rescues, I've rescued maybe 2 people by mistake.  Both were pretty cool about it if I remember.

Worst thing I can say about these is that I will occasionally try to rescue 'you' (me).

Also, I have an option to perform an action before rescuing.  In this case, Damnation.  Can frequently be dangerous to use, but it has an on/off switch and I often find it useful.

Script is for Wintin 2.04 and yes.... I run Dragonmount a lot.

[code:3erpl78p]#defgroup Tank Rescues

#action  {^%1 circles around} {#if {$imtank=1}{#if {$damnvar = 1}{cast 'damn' $target};rescue $$1;#var rescuee $$1}} {G|Tank Rescues} {T|WT}

#action  {^%1 places %2 in the back} {#if {$imtank=1}{#if {$damnvar = 1}{cast 'damn' $target};rescue $$1;#var rescuee $$1}} {G|Tank Rescues} {T|WT}

#action  {^%1 reaches out with} {#if {$imtank=1}{#if {$damnvar = 1}{cast 'damn' $target};rescue $$1;#var rescuee $$1}} {G|Tank Rescues} {T|WT}

#action  {^%1 smartly steps out of %2's deathgrip.} {#if {$imtank=1}{#if {$damnvar = 1}{cast 'damn' $target};rescue $$2;#var rescuee $$2}} {G|Tank Rescues} {T|WT}

#action  {^%1 tried to backstab} {#if {$imtank=1}{#if {$damnvar = 1}{cast 'damn' $target};rescue $$1;#var rescuee $$1}} {G|Tank Rescues} {T|WT}

#action  {^SEEK SHELTER AT ONCE! %1 has begun to sing.} {#if {$imtank=1}{rescue $$1;#var rescuee $$1}} {G|Tank Rescues} {T|WT}

#action  {^Tiamat the dragon queen is here, fighting %1} {#if {$imtank=1}{rescue $$1;#var rescuee $$1}} {G|Tank Rescues} {T|WT}

#action  {^You fail the rescue} {#if {$imtank=1}{rescue $rescuee}} {G|Tank Rescues} {T|WT}

#action  {disengages himself, and attacks %1!} {#if {$imtank=1}{rescue $$1;#var rescuee $$1}} {G|Tank Rescues} {T|WT}

#action  {growls at %1 and attacks!} {#if {$imtank=1}{rescue $$1;#var rescuee $$1}} {G|Tank Rescues} {T|WT}

#action  {lets %1's hands go through} {#if {$imtank=1}{#if {$damnvar = 1}{cast 'damn' $target};rescue $$1;#var rescuee $$1}} {G|Tank Rescues} {T|WT}

#action  {sees %1, and attacks!} {#if {$imtank=1}{rescue $$1;#var rescuee $$1}} {G|Tank Rescues} {T|WT}

#alias  {+damn} {gt I will Damn before Rescue!!;#var damnvar 1} {G|Tank Rescues} {T|WT}

#alias  {+tank} {gt All Rescues Enabled (SING for Rescue!!);#var imtank 1} {G|Tank Rescues} {T|WT}

#alias  {-damn} {gt I will not Damn before Rescue!!;#var damnvar 0} {G|Tank Rescues} {T|WT}

#alias  {-tank} {gt \\\\d02All Rescues Disabled\\\\a01;#var imtank 0} {G|Tank Rescues} {T|WT}

#variable  {damnvar} {1} {G|Tank Rescues}

#variable  {imtank} {0} {G|Tank Rescues}

#variable  {rescuee} {Agemo} {G|Tank Rescues}[/code:3erpl78p]

</div>

<div class="post" data-post-id="13713" data-author="Mustang" data-date="2006-08-15T11:40:50+00:00">

it might be quite bad to use {^%1 places...blahblah} as a trigger for rescuers

besides the fact that the use of a wildcard %1 negates having a anchor^, it would be bad if u were running through an area with group and some other person/group is stabbing around.

also, instead of having #if {$tankmode=1} or aliases that sets certain triggers to work, why not just use the #enable and #disable group functions?

</div>

<div class="post" data-post-id="13714" data-author="12345" data-date="2006-08-15T22:42:45+00:00">

Honestly, I'm kinda against setting vars.  Mostly because as a leader I'm already keeping track of a bunch of stuff and I tend to switch people around very fluidly based on whatever plan I have rattling around in my head at the moment.  Resucing someone by mistake hasn't happened nearly enough that I'm concerned about it.  Then again, I'm not a total newbie either.

As far as the enable/disable thing, my triggers have various switches within them.  Sometimes I'll damn before rescue, sometimes I'll web after grip, sometimes I'll swim naked in a vat of lime jello while singing the Chech national anthem....  I built most of these to work under Wintin 95 and have converted them as I've upgraded.  This method seems to upgrade well and I understand it, so it's what i use.

</div>

<div class="post" data-post-id="13715" data-author="Mustang" data-date="2006-08-16T03:10:28+00:00">

i wasn't refering to u being a newbie :)

i was refering to people who might use your script

</div>

<div class="post" data-post-id="13716" data-author="Weasel" data-date="2006-08-16T05:25:25+00:00">

sometimes I'll swim naked in a vat of lime jello while singing the Chech national anthem....  [/quote:2ecn1me5]

That was YOU ??  :shock: 

..btw, your 'Chech' accent was all farked up...

</div>
