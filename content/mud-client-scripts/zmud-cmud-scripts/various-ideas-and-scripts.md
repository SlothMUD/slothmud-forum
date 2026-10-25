---
title: "Various ideas and scripts"
topic_id: 16
author: "*Splork*"
date: 2004-01-31T21:02:23+00:00
last_activity: 2004-11-07T20:08:24+00:00
last_author: "Zenkai"
sticky: false
locked: false
post_count: 12
---

<div class="post" data-post-id="35" data-author="*Splork*" data-date="2004-01-31T21:02:23+00:00" data-subject="Various ideas and scripts">

Always use a ^(an anchor) before your triggers when you need to make a trigger that starts on a new line.  Like when you want to make a trigger for You are hungry.  An anchor is used to keep other players from abusing your scripts.  If you do not use an anchor and you have a trigger on You are hungry you will eat every time You are hungry is on the screen.

<100hp 50ma 125mv>

You are hungry.

<100hp 50ma 125mv>

Sarge gossips -'You are hungry.'

<100hp 50ma 125mv>

Now if you have used your ^ on your trigger for you are hungry you will only try and eat on the first example.  If you do not use the ^ you will eat on the first example and the second of Sarge gossips -'You are hungry.'

An alias is a shortcut so that you do not need to type out a full line of text everytime.  An example of an alias that is often used is:

#ALIAS ws {wake;stand}

Instead of typing wake and then hitting the Enter key and then stand and the Enter key you just hit ws then Enter.

Here are a few useful aliases.

#ALIAS rr {recite recall}

#ALIAS gt {grouptell}

#ALIAS gac {get all corpse}

#ALIAS dt {cast 'detect invisibility'}

--------------------------------------------------------------------------------

 

When ever you get coins from a corpse and this is turned on it will split the coins with everyone in your group.  Even if you are the only one in the group this will split the coins every time you get them from something.

Auto Split:

#TRIGGER {^There were (%d) coins.} {split %1} "autosplit"

#ALIAS autosplitoff {#t- autosplit;gt Autosplit Off!}

#ALIAS autospliton {#t- autosplit;gt Autosplit On!}

--------------------------------------------------------------------------------

During a big battle in the arena or while reading a spellbook you may not want to take the time to eat and drink until a later time.

Auto Eat Drink:

#VAR cont {drink container keyword here} "food"

#VAR fcont {food container keyword here} "food"

#TRIGGER {^You are hungry.}{wake;get food @fcont;eat food} "food"

#TRIGGER {^You are thirsty.} {wake;drink @cont}"food"

#ALIAS cont {#var cont %1}"food"

#ALIAS fcont {#var fcont %1}"food"

#ALIAS autofoodoff {#t- food;gt Auto Eat/Drink Off!}

#ALIAS autofoodon {#t+ food;gt Auto Eat/Drink On!}

--------------------------------------------------------------------------------

Tired of missing tells in the middle of battle or when you are away from the keyboard?

Capture Tells into another window:

#TRIGGER {tells you '} {#CAP tell} "captell"

#ALIAS captellon {#t+ captell}

#ALIAS captelloff {#t- captell}

--------------------------------------------------------------------------------

This Trigger is very useful to a tank.  Just use the maxhps Alias to set your Max hps and turn the whiner on and your all set.

Tank Whiner:

#TRIGGER {^~<(%d)hp (%d)ma (%d)mv>} {#var hp %1;#math curhps {@hp - @oldhps};

#IF {@curhps < 0} { gt Yourname has @hp/@maxhps Ouch! @curhps};

#IF {@curhps > 0} { gt Yourname has @hp/@maxhps Ahh! @curhps};

#var oldhps {@hp}} "whiner" {nocr|prompt}"whiner"

#VAR hp {0} "whiner"

#VAR curhps {0} "whiner"

#VAR oldhps {0} "whiner"

#ALIAS maxhps {#var maxhps %1}"whiner"

#ALIAS whineroff {#t- whiner;gt I will now not whine when hit!!}"whiner"

#ALIAS whineron {#t+ whiner;gt I will now whine when I get hit!!}"whiner"

--------------------------------------------------------------------------------

AutoLooter for when your solo or leading a group:

#TRIGGER {^Total exp for kill is (*)} {get all corpse;sac corpse} "gacsacsolo"

#ALIAS gacsacsolo1 {#t+ gacsacsolo; gt I am now GAC'N and SAC'N!}

#ALIAS gacsacsolo0 {#t- gacsacsolo; gt I am now no longer GAC'N and SAC'N!}

--------------------------------------------------------------------------------

Autolooter for when your in a group:

#TRIGGER {You receive (%d) experience points as your share.} {get all corpse;sac corpse} "gacsac"

#ALIAS gacsac1 {#t+ gacsac; gt I am now GAC'N and SAC'N!}

#ALIAS gacsac0 {#t- gacsac; gt I am now no longer GAC'N and SAC'N!}

--------------------------------------------------------------------------------

Spec Messages

#TRIGGER {^You cut off (*)} {#AD spec 1;specit} "spec"

#VAR spec {0} {_nodef} "spec"

#ALIAS clearspecit {#var spec 0} "spec"

  

#ALIAS specit {#if {@spec = 1} {say CHOP CHOP!};

#if {@spec = 2} {emote watches the limbs fly!};

#if {@spec = 3} {say OH THATS GOTTA HURT!!!!!!!};

#if {@spec = 4} {say IT'S JUST A FLESH WOUND!!};

#if {@spec = 5} {emote stomps on the floor chanting.;emote chants 'WE WILL! WE WILL CHOP YOU!!!';clearspecit}} "spec"

#ALIAS specmessoff {#t- spec;gt I will no longer badmouth the spec mobs}

#ALIAS specmesson {#t+ spec;gt I will now badmouth the spec mobs}

--------------------------------------------------------------------------------

 

HealO

#VAR heal1 0

#VAR heal2 0

#VAR heal3 0

#VAR heal3 0

#VAR heal4 0

#VAR heal5 0

#VAR float1 0

#ALIAS heal1 {#var heal1 %1}

#ALIAS heal2 {#var heal2 %1}

#ALIAS heal3 {#var heal3 %1}

#ALIAS heal4 {#var heal4 %1}

#ALIAS heal5 {#var heal5 %1}

#ALIAS float1 {#var float1 %1}

#ALIAS healorder {gt HEAL ORDER -- @heal1, @heal2, @heal3, @heal4, @heal5 FLOATER: @float1}

#TRIGGER {HEAL0} {healorder} "healo" {case}

 

#ALIAS healoon {t+ healo}

#ALIAS healooff {t- healo}

 

--------------------------------------------------------------------------------

</div>

<div class="post" data-post-id="130" data-author="Teron" data-date="2004-03-18T05:56:09+00:00" data-subject="">

#al pingo 'mb1=%1;mb2=%2;mb3=%3;mb4=%4;mb5=%5;mb6=%6;mb7=%7;mb8=%8;mb9=%9'

#al ping '#IF {@mb1<>""} {tell @mb1 hi};#IF {@mb2<>""} {tell @mb2 hi};#IF {@mb3<>""} {tell @mb3 hi};#IF {@mb4<>""} {tell @mb4 hi};#IF {@mb5<>""} {tell @mb5 hi};#IF {@mb6<>""} {tell @mb6 hi};#IF {@mb7<>""} {tell @mb7 hi};#IF {@mb8<>""} {tell @mb8 hi};#IF {@mb9<>""} {tell @mb9 hi}'

this way, if you do 'pingo demo ivan mandi' it wont be pinging all 10 slots,

but will only ping demo ivan and mandi.

enjoy 

Teron

</div>

<div class="post" data-post-id="2642" data-author="Xandora" data-date="2004-11-07T08:20:38+00:00" data-subject="For all you tanks that don&#x27;t have Tank Scripts: Zmud 7.02">

#CLASS {Tank} {disable}

#TRIGGER {^(%1) disengages (%2), and attacks (%3)!} {#var rescuee %3;rescue @rescuee}

#TRIGGER {^%1 places %2 in the back of %3, resulting in some strange noises and some blood!} {#var rescuee %1;rescue @rescuee}

#TRIGGER {^(%1) sees (%2) and ATTACKS!} {#var rescuee %2;rescue @rescuee}

#TRIGGER {^%1 growls at %2 and attacks!} {#var rescuee %2;rescue @rescuee}

#TRIGGER {^SEEK SHELTER AT ONCE! %1 has begun to sing.} {#var rescuee %1;rescue @rescuee}

#TRIGGER {^%1 tried to backstab %2, but nearly cut %3 own finger.} {#var rescuee %1;rescue @rescuee}

#TRIGGER {^You fail the rescue.} {rescue @rescuee}

#TRIGGER {^%1 avoids %2's clumsy backstab} {#var rescuee %2;rescue @rescuee}

#TRIGGER {^You attempt to bash %1, but bounce off and are sent sprawling!} {stand}

#TRIGGER {^You try to stand, but are beaten back under a hail of blows!} {stand}

#TRIGGER {^Banzai! To the rescue...} {#var rescuee null}

#CLASS 0

</div>

<div class="post" data-post-id="2643" data-author="Xandora" data-date="2004-11-07T08:44:01+00:00" data-subject="Whiner for Zmud 7.05">

This whiner only reports on hp changes of +/- 20.

To operate these whiners, you must have an alias in a class folder that is always enabled like this:

#alias whineron {#t+ whiner;grouptell Whining my Hits}

#alias whineroff {#t- whiner;grouptell Not Whining Hits}

1)  These scripts go in their on seperate class folder, which I will call (whiner).

#CLASS {whiner} {disable}

#ALIAS minushp {#if (@diffhp>@hitup) {grouptell "["\d02@curhp\c03"|"\d04@maxhp\c03"]   "To Full:"<"\d02@needhp\c03">   "HEAL:"<+"\d04@diffhp\c03">"}}}

#ALIAS plushp {#if (@diffhp<@hitdown)  {grouptell "["\d02@curhp\c03"|"\d04@maxhp\c03"]   "To Full:"<"\d02@needhp\c03">   "DAMG:"<"\d03@diffhp\c03">"}}}

#VAR hitup {20}

#VAR hitdown {-20}

#TRIGGER {^~<(%1)hp (%2)ma (%3)mv~>} {#var curhp %1;#math diffhp (@curhp-@lasthp);#math needhp (@maxhp-@curhp);#math lasthp @curhp;#if (@diffhp<>0) {#if (@diffhp>0) {minushp} {plushp}}}

#CLASS 0

2)  This script must go in a class folder that is never disabled:

#TRIGGER {^You have %1~(%2~) hit, %3~(%4~) mana and %5~(%6~) movement points.} {#var maxhp %2;#var maxma %4;#var maxmv %6}

3)  This script looks similiar to the previous one, but it is for 2x40 when you see your regen rate.  This script and the previous one must go in seperate class folders, else one will overwrite the other:

#TRIGGER {^You have ~(%1/%2+%3~) hit, ~(%4/%5+%6~) mana and ~(%7/%8+%9~) movement points.} {#var maxhp %2;#var maxma %5;#var maxmv %8}

4)  AND Finally, the set of scripts below is the same as above except that it works on an #If statement where it considers whether you are the tank (to whine to group) or not the tank (whine only to yourself).  If you perfer to use this one you must set this up:

**note** the setup for this whiner script also uses #s 2 and 3 above as well as the whineron, whineroff aliases at the beginning.

#trigger {^tank %1} {#var tank %1;#show My tank is now: @tank}

#trigger {^char %1} {#var charname %1;#show My name is @charname}

#CLASS {whiner} {disable}

#ALIAS minushp {#if (@diffhp>@hitup) {#if (@charname=@tank) {grouptell "["\d02@curhp\c03"|"\d04@maxhp\c03"]   "To Full:"<"\d02@needhp\c03">   "HEAL:"<+"\d04@diffhp\c03">"} {#show >>>>>----- HITP STATUS: "["@curhp"|"@maxhp"]   "To Full:"<"@needhp">    "HEAL:"<+"@diffhp">"}}}

#ALIAS plushp {#if (@diffhp<@hitdown) {#if (@charname=@tank) {grouptell "["\d02@curhp\c03"|"\d04@maxhp\c03"]   "To Full:"<"\d02@needhp\c03">   "DAMG:"<"\d03@diffhp\c03">"} {#show >>>>>----- HITP STATUS: "["@curhp"|"@maxhp"]   "To Full:"<"@needhp">    "DAMG:"<"@diffhp">"}}}

#VAR hitup {20}

#VAR hitdown {-20}

#TRIGGER {^~<(%1)hp (%2)ma (%3)mv~>} {#var curhp %1;#math diffhp (@curhp-@lasthp);#math needhp (@maxhp-@curhp);#math lasthp @curhp;#if (@diffhp<>0) {#if (@diffhp>0) {minushp} {plushp}}}

#CLASS 0

</div>

<div class="post" data-post-id="2644" data-author="Xandora" data-date="2004-11-07T08:44:55+00:00" data-subject="Both the following ZMUD scripts are for 7.05 (not 7.02)">

See subject

</div>

<div class="post" data-post-id="2645" data-author="Xandora" data-date="2004-11-07T08:58:18+00:00" data-subject="Autostabber for Zmud 7.05">

The following scripts are for an auto backstabber.  This stabber takes into account whether you are actually the stabber, and whether you have *quietmode* on.  The following prereq scripts are required for it to work:

#alias quieton {#var quitemode 1}

#alias quietoff {#var quietmode 0}

#trigger {^stabber %1} {#var stabber %1;#show My stabber is @stabber}

#trigger {^char %1} {#var charname %1;#show I am @charname}

#CLASS {TARGETTER}

#ALIAS back {backstab @target}

#ALIAS et {emote target %1}

#TRIGGER {^gg %1} {#var target %1;#if (@quietmode = 1) {#SHOW The TARGET is now set to: @target} {grouptell target @target}}

#TRIGGER {^@leader -- '(*)qstab'} {#if (@stabber=@charname) {backstab @target}{}}

#TRIGGER {^@leader -- '(*)target %1'} {#var target %1;#if (@stabber=@charname) {grouptell Target: \d02@target\d03}}

#TRIGGER {^You follow @leader.} {#if (@stabber=@charname) {backstab @target}}

#TRIGGER {^You warily lead the way ahead of @leader.} {#if (@stabber=@charname) {backstab @target}}

#TRIGGER {^You grouptell: '2.target %1'} {#var target2 %1}

#TRIGGER {^You emote: @charname target %1} {#var target %1}

#TRIGGER {^Firebrand -- '*tigress*  target %1'} {#if (@leader=Firebrand) {#var target %1} {}}

#TRIGGER {^@leader -- 'target %1'} {#var target %1}

#CLASS 0

If you noticed, Firebrand has her own script.  This is because no matter how hard I tried, I couldnt get my scripts to ignore her grouptell *tigress*.

</div>

<div class="post" data-post-id="2646" data-author="Xandora" data-date="2004-11-07T09:02:48+00:00" data-subject="About the Autostabber script">

I forgot to mention, this autostabber can remain onconstantly because it also doubles as a targetter.  It can stay on all the time because it checks the condition of whether you are stabber or not, if you are not, it doesnt try to stab.

Have a nice day ;)

</div>

<div class="post" data-post-id="2647" data-author="Xandora" data-date="2004-11-07T09:57:36+00:00" data-subject="Opps, Tank Whiner : the forgotten script">

This script needs to be put in with either one of the You have ... scripts from the whiner in the other post:

#TRIGGER {^~<(%1)hp (%2)ma (%3)mv~>} {#var curhp %1;#var curma %2; #var curhp %3}

</div>

<div class="post" data-post-id="2654" data-author="Zenkai" data-date="2004-11-07T15:47:48+00:00" data-subject="spell cipher">

Here is a spell cipher script.

Normal: 

The demon utters the words, 'yufzxuie'

Script Output: 

The demon utters the words, 'yufzxuie' (firewind)

Trigger: 

(*) utters the words, '(*)'

Command:

#if ("%2" = "abrawg ay hpz ablgg") {#sub {%1 utters the words, '%2' (arms of the abyss)}}

#if ("%2" = "abrazak") {#sub {%1 utters the words, '%2' (armor)}}

#if ("%2" = "aiuwahz oculoae") {#sub {%1 utters the words, '%2' (animate dead)}}

#if ("%2" = "aque bragh") {#sub {%1 utters the words, '%2' (acid blast)}}

#if ("%2" = "aque gpaxzf") {#sub {%1 utters the words, '%2' (acid shower)}}

#if ("%2" = "ashuhjoculo") {#sub {%1 utters the words, '%2' (aptitude)}}

#if ("%2" = "azaraiqpz") {#sub {%1 utters the words, '%2' (avalanche)}}

#if ("%2" = "azfuar gzfzaih") {#sub {%1 utters the words, '%2' (aerial servant)}}

#if ("%2" = "azoug") {#sub {%1 utters the words, '%2' (aegis)}}

#if ("%2" = "baiugp jioculoae") {#sub {%1 utters the words, '%2' (banish undead)}}

#if ("%2" = "baiz abrazak") {#sub {%1 utters the words, '%2' (bone armor)}}

#if ("%2" = "bfawbrzg") {#sub {%1 utters the words, '%2' (brambles)}}

#if ("%2" = "candusghafahuai") {#sub {%1 utters the words, '%2' (restoration)}}

#if ("%2" = "candusgugh qare") {#sub {%1 utters the words, '%2' (resist cold)}}

#if ("%2" = "candusgugh xzbg") {#sub {%1 utters the words, '%2' (resist webs)}}

#if ("%2" = "candusgugh yufz") {#sub {%1 utters the words, '%2' (resist fire)}}

#if ("%2" = "candusounsozfahuai") {#sub {%1 utters the words, '%2' (regeneration)}}

#if ("%2" = "candusraqahuai") {#sub {%1 utters the words, '%2' (relocation)}}

#if ("%2" = "candusuoi ay hpz gsuoculof") {#sub {%1 utters the words, '%2' (reign of the spider)}}

#if ("%2" = "canduswazz eugzagz") {#sub {%1 utters the words, '%2' (remove disease)}}

#if ("%2" = "canduswazz judifgz") {#sub {%1 utters the words, '%2' (remove curse)}}

#if ("%2" = "canduswazz saugai") {#sub {%1 utters the words, '%2' (remove poison)}}

#if ("%2" = "candusyfzgp") {#sub {%1 utters the words, '%2' (refresh)}}

#if ("%2" = "candusyjzunsoahuai") {#sub {%1 utters the words, '%2' (rejuvenation)}}

#if ("%2" = "candusyrzqhuai") {#sub {%1 utters the words, '%2' (reflection)}}

#if ("%2" = "diesilla barh") {#sub {%1 utters the words, '%2' (lightning bolt)}}

#if ("%2" = "djuqtunso") {#sub {%1 utters the words, '%2' (quicken)}}

#if ("%2" = "dudaqzshuai") {#sub {%1 utters the words, '%2' (perception)}}

#if ("%2" = "eabrat qraat") {#sub {%1 utters the words, '%2' (dark cloak)}}

#if ("%2" = "eabrat waqz") {#sub {%1 utters the words, '%2' (dark mace)}}

#if ("%2" = "eabratguoph") {#sub {%1 utters the words, '%2' (darksight)}}

#if ("%2" = "eabratizgg") {#sub {%1 utters the words, '%2' (darkness)}}

#if ("%2" = "eawiahuai") {#sub {%1 utters the words, '%2' (damnation)}}

#if ("%2" = "eaxiyufz") {#sub {%1 utters the words, '%2' (dawnfire)}}

#if ("%2" = "efzaw hart") {#sub {%1 utters the words, '%2' (dream talk)}}

#if ("%2" = "eugszr oaae") {#sub {%1 utters the words, '%2' (dispel good)}}

#if ("%2" = "eugszr waouq") {#sub {%1 utters the words, '%2' (dispel magic)}}

#if ("%2" = "eugszr zzur") {#sub {%1 utters the words, '%2' (dispel evil)}}

#if ("%2" = "euguihzofahz") {#sub {%1 utters the words, '%2' (disintegrate)}}

#if ("%2" = "fido") {#sub {%1 utters the words, '%2' (bless)}}

#if ("%2" = "gaiqhjabral") {#sub {%1 utters the words, '%2' (sanctuary)}}

#if ("%2" = "ghaiz gtui") {#sub {%1 utters the words, '%2' (stone skin)}}

#if ("%2" = "ghaiz ha yrzgp") {#sub {%1 utters the words, '%2' (stone to flesh)}}

#if ("%2" = "ghawuia") {#sub {%1 utters the words, '%2' (stamina)}}

#if ("%2" = "ghcandusiohp") {#sub {%1 utters the words, '%2' (strength)}}

#if ("%2" = "gjibzaw") {#sub {%1 utters the words, '%2' (sunbeam)}}

#if ("%2" = "gjwwai") {#sub {%1 utters the words, '%2' (summon)}}

#if ("%2" = "gjwwai pafoculo") {#sub {%1 utters the words, '%2' (summon hord)}}

#if ("%2" = "gjwwai jioculoae") {#sub {%1 utters the words, '%2' (summon undead)}}

#if ("%2" = "gpaqtuio ofags") {#sub {%1 utters the words, '%2' (shocking grasp)}}

#if ("%2" = "gpuzre ay hpafig") {#sub {%1 utters the words, '%2' (shield of thorns)}}

#if ("%2" = "gpuzre ay yauhp") {#sub {%1 utters the words, '%2' (shield of faith)}}

#if ("%2" = "gqflbuhz") {#sub {%1 utters the words, '%2' (scrybite)}}

#if ("%2" = "gruugz oculoae") {#sub {%1 utters the words, '%2' (raise dead)}}

#if ("%2" = "grzzs") {#sub {%1 utters the words, '%2' (sleep)}}

#if ("%2" = "gsabrat gpaxzf") {#sub {%1 utters the words, '%2' (spark shower)}}

#if ("%2" = "gszqhgrur gpuzre") {#sub {%1 utters the words, '%2' (spectral shield)}}

#if ("%2" = "gszrr gpuzre") {#sub {%1 utters the words, '%2' (spell shield)}}

#if ("%2" = "gsufuh xahqpzf") {#sub {%1 utters the words, '%2' (spirit watcher)}}

#if ("%2" = "gsufuhjar pawwzf") {#sub {%1 utters the words, '%2' (spiritual hammer)}}

#if ("%2" = "gunsogz ruyz") {#sub {%1 utters the words, '%2' (sense life)}}

#if ("%2" = "gurunsoqz") {#sub {%1 utters the words, '%2' (silence)}}

#if ("%2" = "hargpaig culabjhz") {#sub {%1 utters the words, '%2' (talshans tribute)}}

#if ("%2" = "hargpaig euabrzfuz") {#sub {%1 utters the words, '%2' (talshans diablerie)}}

#if ("%2" = "hiqahz abyzqh") {#sub {%1 utters the words, '%2' (locate object)}}

#if ("%2" = "hjfi jioculoae") {#sub {%1 utters the words, '%2' (turn undead)}}

#if ("%2" = "hunsozbfajg qrax") {#sub {%1 utters the words, '%2' (tenebrous claw)}}

#if ("%2" = "huozf unsoejgruiqz") {#sub {%1 utters the words, '%2' (tiger endurance)}}

#if ("%2" = "hzrzsafh") {#sub {%1 utters the words, '%2' (teleport)}}

#if ("%2" = "hzrzsahpl") {#sub {%1 utters the words, '%2' (telepathy)}}

#if ("%2" = "iahjcandusg canduszuzar") {#sub {%1 utters the words, '%2' (natures revival)}}

#if ("%2" = "iahjcandusg yawuruabra") {#sub {%1 utters the words, '%2' (natures familiar)}}

#if ("%2" = "jioculoae zugaoz") {#sub {%1 utters the words, '%2' (undead visage)}}

#if ("%2" = "jiparl ghcandusiohp") {#sub {%1 utters the words, '%2' (unholy strength)}}

#if ("%2" = "jiparl kadagru") {#sub {%1 utters the words, '%2' (unholy aura)}}

#if ("%2" = "judicandus dies") {#sub {%1 utters the words, '%2' (cure light)}}

#if ("%2" = "judicandus gzfuajg") {#sub {%1 utters the words, '%2' (cure serious)}}

#if ("%2" = "judicandus iafwar") {#sub {%1 utters the words, '%2' (cure normal)}}

#if ("%2" = "judicandus nose") {#sub {%1 utters the words, '%2' (cure blind)}}

#if ("%2" = "judicandus qfuhuq") {#sub {%1 utters the words, '%2' (cure critical)}}

#if ("%2" = "judicandus wuiaf") {#sub {%1 utters the words, '%2' (cure minor)}}

#if ("%2" = "judifgz") {#sub {%1 utters the words, '%2' (curse)}}

#if ("%2" = "mosailla paieg") {#sub {%1 utters the words, '%2' (burning hands)}}

#if ("%2" = "noselacri") {#sub {%1 utters the words, '%2' (blindness)}}

#if ("%2" = "oaaebzffl") {#sub {%1 utters the words, '%2' (goodberry)}}

#if ("%2" = "oabraoculoi") {#sub {%1 utters the words, '%2' (garden)}}

#if ("%2" = "oahz") {#sub {%1 utters the words, '%2' (gate)}}

#if ("%2" = "oculoahp saqh") {#sub {%1 utters the words, '%2' (death pact)}}

#if ("%2" = "oculoahpxahqp") {#sub {%1 utters the words, '%2' (deathwatch)}}

#if ("%2" = "oculoghfjqhuai") {#sub {%1 utters the words, '%2' (destruction)}}

#if ("%2" = "oculoinfra eugzagz") {#sub {%1 utters the words, '%2' (detect disease)}}

#if ("%2" = "oculoinfra oaae") {#sub {%1 utters the words, '%2' (detect good)}}

#if ("%2" = "oculoinfra saugai") {#sub {%1 utters the words, '%2' (detect poison)}}

#if ("%2" = "oculoinfra uizuguburuhl") {#sub {%1 utters the words, '%2' (detect invisibility)}}

#if ("%2" = "oculoinfra waouq") {#sub {%1 utters the words, '%2' (detect magic)}}

#if ("%2" = "oculoinfra zzur") {#sub {%1 utters the words, '%2' (detect evil)}}

#if ("%2" = "oculowai buie") {#sub {%1 utters the words, '%2' (demon bind)}}

#if ("%2" = "oculowai hajqp") {#sub {%1 utters the words, '%2' (demon touch)}}

#if ("%2" = "ofaqz") {#sub {%1 utters the words, '%2' (grace)}}

#if ("%2" = "ofzahzf candusyfzgp") {#sub {%1 utters the words, '%2' (greater refresh)}}

#if ("%2" = "ofzahzf pzar") {#sub {%1 utters the words, '%2' (greater heal)}}

#if ("%2" = "ofzahzf yrjueuhl") {#sub {%1 utters the words, '%2' (greater fluidity)}}

#if ("%2" = "orawajf") {#sub {%1 utters the words, '%2' (glamour)}}

#if ("%2" = "pzar") {#sub {%1 utters the words, '%2' (heal)}}

#if ("%2" = "pzfwzhuq xabrae") {#sub {%1 utters the words, '%2' (hermatic ward)}}

#if ("%2" = "pzrrghfutz") {#sub {%1 utters the words, '%2' (hellstrike)}}

#if ("%2" = "pzrryufz") {#sub {%1 utters the words, '%2' (hellfire)}}

#if ("%2" = "qafaia") {#sub {%1 utters the words, '%2' (corona)}}

#if ("%2" = "qahijf gsfal") {#sub {%1 utters the words, '%2' (colour spray)}}

#if ("%2" = "qaihfar xzahpzf") {#sub {%1 utters the words, '%2' (control weather)}}

#if ("%2" = "qarr diesilla") {#sub {%1 utters the words, '%2' (call lightning)}}

#if ("%2" = "qfuwgai gqajfoz") {#sub {%1 utters the words, '%2' (crimson scourge)}}

#if ("%2" = "qfzahz xahzf") {#sub {%1 utters the words, '%2' (create water)}}

#if ("%2" = "qfzahz yaae") {#sub {%1 utters the words, '%2' (create food)}}

#if ("%2" = "qpabraw dudasabru") {#sub {%1 utters the words, '%2' (charm person)}}

#if ("%2" = "qpaui diesilla") {#sub {%1 utters the words, '%2' (chain lightning)}}

#if ("%2" = "qpfaiag uiqaihahuai") {#sub {%1 utters the words, '%2' (chronos incantation)}}

#if ("%2" = "qpurr hajqp") {#sub {%1 utters the words, '%2' (chill touch)}}

#if ("%2" = "qraguio xzazz") {#sub {%1 utters the words, '%2' (closing weave)}}

#if ("%2" = "rhileg bzaqai") {#sub {%1 utters the words, '%2' (lloyds beacon)}}

#if ("%2" = "rzhpabraol") {#sub {%1 utters the words, '%2' (lethargy)}}

#if ("%2" = "saggaoz") {#sub {%1 utters the words, '%2' (passage)}}

#if ("%2" = "sfahzqhuai yfaw zzur") {#sub {%1 utters the words, '%2' (protection from evil)}}

#if ("%2" = "sfugwahuq gsfal") {#sub {%1 utters the words, '%2' (prismatic spray)}}

#if ("%2" = "sfzgzfzz yaae") {#sub {%1 utters the words, '%2' (preserve food)}}

#if ("%2" = "sjfuhl") {#sub {%1 utters the words, '%2' (purity)}}

#if ("%2" = "spagz eaaf") {#sub {%1 utters the words, '%2' (phase door)}}

#if ("%2" = "tiaqt") {#sub {%1 utters the words, '%2' (knock)}}

#if ("%2" = "ufai gtui") {#sub {%1 utters the words, '%2' (iron skin)}}

#if ("%2" = "uiguoph") {#sub {%1 utters the words, '%2' (insight)}}

#if ("%2" = "uiyfazuguai") {#sub {%1 utters the words, '%2' (infravision)}}

#if ("%2" = "uiyjgz gajr") {#sub {%1 utters the words, '%2' (infuse soul)}}

#if ("%2" = "uizuguburuhl") {#sub {%1 utters the words, '%2' (invisibility)}}

#if ("%2" = "unsoqpaih xzasai") {#sub {%1 utters the words, '%2' (enchant weapon)}}

#if ("%2" = "unsozfol efaui") {#sub {%1 utters the words, '%2' (energy drain)}}

#if ("%2" = "uoculoihuyl") {#sub {%1 utters the words, '%2' (identify)}}

#if ("%2" = "uqz ghafw") {#sub {%1 utters the words, '%2' (ice storm)}}

#if ("%2" = "uqz grul") {#sub {%1 utters the words, '%2' (ice ray)}}

#if ("%2" = "waai kadagru") {#sub {%1 utters the words, '%2' (moon aura)}}

#if ("%2" = "waburuhl") {#sub {%1 utters the words, '%2' (mobility)}}

#if ("%2" = "wagg uizuguburuhl") {#sub {%1 utters the words, '%2' (mass invisibility)}}

#if ("%2" = "wagg xahzf bfzahpuio") {#sub {%1 utters the words, '%2' (mass water breathing)}}

#if ("%2" = "wagg xzb") {#sub {%1 utters the words, '%2' (mass web)}}

#if ("%2" = "wagg yrl") {#sub {%1 utters the words, '%2' (mass fly)}}

#if ("%2" = "waouq fasz") {#sub {%1 utters the words, '%2' (magic rope)}}

#if ("%2" = "waouq raihzfi") {#sub {%1 utters the words, '%2' (magic lantern)}}

#if ("%2" = "waouq wuggurz") {#sub {%1 utters the words, '%2' (magic missile)}}

#if ("%2" = "wuffaf uwaoz") {#sub {%1 utters the words, '%2' (mirror image)}}

#if ("%2" = "wuiebabra") {#sub {%1 utters the words, '%2' (mindbar)}}

#if ("%2" = "wzhzaf gxabraw") {#sub {%1 utters the words, '%2' (meteor swarm)}}

#if ("%2" = "xafe ay candusqarr") {#sub {%1 utters the words, '%2' (word of recall)}}

#if ("%2" = "xafe ay saui") {#sub {%1 utters the words, '%2' (word of pain)}}

#if ("%2" = "xahzf bfzahpuio") {#sub {%1 utters the words, '%2' (water breathing)}}

#if ("%2" = "xarr ay yrzgp") {#sub {%1 utters the words, '%2' (wall of flesh)}}

#if ("%2" = "xart ay hpz qpzzhap") {#sub {%1 utters the words, '%2' (walk of the cheetah)}}

#if ("%2" = "xgruuhpyafw") {#sub {%1 utters the words, '%2' (wraithform)}}

#if ("%2" = "xuieg ay yafhjiz") {#sub {%1 utters the words, '%2' (winds of fortune)}}

#if ("%2" = "xukabraeg zlz") {#sub {%1 utters the words, '%2' (wizards eye)}}

#if ("%2" = "xurr a hpz xugs") {#sub {%1 utters the words, '%2' (will o the wisp)}}

#if ("%2" = "xzatunso") {#sub {%1 utters the words, '%2' (weaken)}}

#if ("%2" = "xzb") {#sub {%1 utters the words, '%2' (web)}}

#if ("%2" = "yafhjiz") {#sub {%1 utters the words, '%2' (fortune)}}

#if ("%2" = "yafqz yuzre") {#sub {%1 utters the words, '%2' (force field)}}

#if ("%2" = "yao") {#sub {%1 utters the words, '%2' (fog)}}

#if ("%2" = "yawuruabra") {#sub {%1 utters the words, '%2' (familiar)}}

#if ("%2" = "yazfuz yufz") {#sub {%1 utters the words, '%2' (faerie fire)}}

#if ("%2" = "yfzgpxahzf") {#sub {%1 utters the words, '%2' (freshwater)}}

#if ("%2" = "yfzzkz") {#sub {%1 utters the words, '%2' (freeze)}}

#if ("%2" = "yrawz ghfutz") {#sub {%1 utters the words, '%2' (flame strike)}}

#if ("%2" = "yrjueuhl") {#sub {%1 utters the words, '%2' (fluidity)}}

#if ("%2" = "yrl") {#sub {%1 utters the words, '%2' (fly)}}

#if ("%2" = "yufzbarr") {#sub {%1 utters the words, '%2' (fireball)}}

#if ("%2" = "yufzghafw") {#sub {%1 utters the words, '%2' (firestorm)}}

#if ("%2" = "yufzxuie") {#sub {%1 utters the words, '%2' (firewind)}}

#if ("%2" = "yzabra") {#sub {%1 utters the words, '%2' (fear)}}

#if ("%2" = "yzagh") {#sub {%1 utters the words, '%2' (feast)}}

#if ("%2" = "zabrahpdjatz") {#sub {%1 utters the words, '%2' (earthquake)}}

#if ("%2" = "zawsufuq hajqp") {#sub {%1 utters the words, '%2' (vampiric touch)}}

#if ("%2" = "znhuiqhuai") {#sub {%1 utters the words, '%2' (extinction)}}

#if ("%2" = "zuguai") {#sub {%1 utters the words, '%2' (vision)}}

#if ("%2" = "zuharuhl") {#sub {%1 utters the words, '%2' (vitality)}}

#if ("%2" = "zuoaf") {#sub {%1 utters the words, '%2' (vigor)}}

#if ("%2" = "zwbarw") {#sub {%1 utters the words, '%2' (embalm)}}[/color:2crvzny6]

These are the spells I haven't added to the script yet:

Necro 16 - control undead

Necro 34 - pestilence

Druid 21 - canopied arbor

Druid 23 - elemental resistance

Druid 30 - twister

Druid 33 - willow wind

Avatar 1 - flesh golem

Avatar 7 - call followers

Avatar 7 - wellberry

Avatar 8 - demonic aura

Avatar 14 - word of torment

Avatar 22 - petrified armor

Avatar 24 - demonic strength

Avatar 25 - awaken the abyss

Avatar 28 - cleanse

Avatar 28 - natures restoral

Avatar 33 - annihilation

Avatar 38 - there and back again

</div>

<div class="post" data-post-id="2659" data-author="Zenkai" data-date="2004-11-07T17:23:53+00:00" data-subject="status bar">

Here is a color status bar when you 'look' at a mob or player.

Normal:

The demon has quite a few wounds.

Script Output:

The demon has quite a few wounds: [****---]

Triggers:

#TRIGGER {(*) is in excellent condition.} {#sub {%ansi(6)%1 is in %ansi(5)excellent condition%ansi(6): %ansi(7)%char(91)%ansi(4)*******%ansi(7)%char(93)}}

#TRIGGER {(*) has a few scratches.} {#sub {%ansi(6)%1 has a %ansi(5)few scratches%ansi(6): %ansi(7)%char(91)%ansi(4)******%ansi(7)-%char(93)}}

#TRIGGER {(*) has some small wounds and bruises.} {#sub {%ansi(6)%1 has some %ansi(5)small wounds and bruises%ansi(6): %ansi(7)%char(91)%ansi(4)*****%ansi(7)--%char(93)}}

#TRIGGER {(*) has quite a few wounds.} {#sub {%ansi(6)%1 has %ansi(5)quite a few wounds%ansi(6): %ansi(7)%char(91)%ansi(4)****%ansi(7)---%char(93)}}

#TRIGGER {(*) has some big nasty wounds and scratches.} {#sub {%ansi(6)%1 has some %ansi(5)big nasty wounds and scratches%ansi(6): %ansi(7)%char(91)%ansi(4)***%ansi(7)----%char(93)}}

#TRIGGER {(*) looks pretty hurt.} {#sub {%ansi(6)%1 looks %ansi(5)pretty hurt%ansi(6): %ansi(7)%char(91)%ansi(4)**%ansi(7)-----%char(93)}}

#TRIGGER {(*) is in awful condition.} {#sub {%ansi(6)%1 is in %ansi(5)awful condition%ansi(6): %ansi(7)%char(91)%ansi(4)*%ansi(7)------%char(93)}}

#TRIGGER {(*) is bleeding awfully from big wounds.} {#sub {%ansi(6)%1 is %ansi(5)bleeding awfully from big wounds%ansi(6): %ansi(7)%char(91)-------%char(93)}}[/color:3dkb0eim]

</div>

<div class="post" data-post-id="2661" data-author="Xandora" data-date="2004-11-07T18:26:51+00:00" data-subject="Mobreporter">

I thought about putting mine up here, but they can get annoying if people don't have on and off switches for them and some of the commands inside them, so I left it out on purpose ;)

</div>

<div class="post" data-post-id="2664" data-author="Zenkai" data-date="2004-11-07T20:08:24+00:00" data-subject="setting level gain variables">

That script is not a mob reporter, just a substitution :)

BTW-

Anyone have a script that would automatically set exp-needed-to-level variables (pri, sec, ter, qua, avatar) just by the 'score' command? It would be a cool script, but I'm to lazy to write it :P

</div>
