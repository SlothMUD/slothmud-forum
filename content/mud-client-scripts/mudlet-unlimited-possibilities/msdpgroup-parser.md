---
title: "MSDPGROUP PARSER"
topic_id: 4584
author: "*juggleblood*"
date: 2016-01-25T20:00:50+00:00
last_activity: 2016-02-02T19:56:24+00:00
last_author: "*juggleblood*"
sticky: false
locked: false
post_count: 15
---

<div class="post" data-post-id="36546" data-author="*juggleblood*" data-date="2016-01-25T20:00:50+00:00" data-subject="MSDPGROUP PARSER">

Apparently mudlet 3.0 has some kind of native variable handler that sposed to let you easily parse msdpgroup.  But I'm using mudlet 2.1 cuz I'm stubborn and don't fully trust the new version ever since it destroyed so many of my scripts. So if you're not using 3.0 or can't figure out how to use the variables, here is how I parsed MSDP group into tables. 

The capital "O" which appears throughout is not actually an "O" it's the weird characters that you have to cut and paste, which by the way sometimes appear differently on your screen than when you cut and paste them into notepad.  The weird characters makes this a pain in the ass for people to adopt, so anyone who wants to clean this up and post something people can use, feel free.

When you are done, you will have separate tables for all the data, so to see sochi's mana for example you would use groupMana['Sochi'] or groupMaxMana['Sochi'], etc..

If you have a better way please post. Thanks.

function updateGroup()

groupString=atcp.MSDPGROUP

memberTable={}

groupTable={}

groupMana={}

groupHp={}

groupMaxMana={}

groupMaxHp={}

groupMove={}

groupMaxMove={}

groupPosition={}

groupStatus={}

groupClass={}

groupLevel={}

groupString=string.gsub(groupString,"OOM","OM")

groupString=string.gsub(groupString,"NAMEO","")

groupString=string.gsub(groupString,"HITPOINTSO","")

groupString=string.gsub(groupString,"MAX_HITPOINTSO","")

groupString=string.gsub(groupString,"MANAO","")

groupString=string.gsub(groupString,"MAX_MANAO","")

groupString=string.gsub(groupString,"MOVESO","")

groupString=string.gsub(groupString,"MAX_MOVESO","")

groupString=string.gsub(groupString,"POSITIONO","")

groupString=string.gsub(groupString,"STATUSO","")

groupString=string.gsub(groupString,"CLASSO","")

groupString=string.gsub(groupString,"LEVELSO","")

groupString=string.gsub(groupString,"MAX_","")

groupString=string.cut(groupString,groupString:len()-2)

groupString=string.reverse(groupString)

groupString=string.cut(groupString,groupString:len()-8)

groupString=string.reverse(groupString)

groupTable=groupString:split("MEMBER")

for i=1,#groupTable do

memberTable=groupTable:split("O")

--display(memberTable)  

end

groupTable={}

for i=1,#memberTable do

groupTable=memberTable[2]

groupHp[memberTable[2]]=0+memberTable[3]

groupMaxHp[memberTable[2]]=0+memberTable[4]

groupMana[memberTable[2]]=0+memberTable[5]

groupMaxMana[memberTable[2]]=0+memberTable[6]

groupMove[memberTable[2]]=0+memberTable[7]

groupMaxMove[memberTable[2]]=0+memberTable[8]

groupPosition[memberTable[2]]=memberTable[9]

groupStatus[memberTable[2]]=memberTable[10]

groupClass[memberTable[2]]=memberTable[11]

groupLevel[memberTable[2]]=0+memberTable[12]

end

end

</div>

<div class="post" data-post-id="36547" data-author="*juggleblood*" data-date="2016-01-26T16:39:49+00:00" data-subject="Re: MSDPGROUP PARSER">

Ok. That was stupid of me. Apparently cutting and pasting those special chars from the mud into your script xml file causes it to corrupt, something I knew, but forgot. I guess I have to breakdown and install 3.0 and figure out out to access the group msdp vars there. Any advice welcome.

</div>

<div class="post" data-post-id="36548" data-author="*Breeze*" data-date="2016-01-26T16:59:50+00:00" data-subject="Re: MSDPGROUP PARSER">

check your email

</div>

<div class="post" data-post-id="36549" data-author="*juggleblood*" data-date="2016-01-26T19:16:21+00:00" data-subject="Re: MSDPGROUP PARSER">

Ok, mudlet 3.0 has the same issue as 2.1 regarding special characters. The box symbol that is used in the msdpvars is an illegal character in xml. So what happens is you write a nice script that works in mudlet, but then when you close mudlet and reload from your xml file, everything in your scripts below the special character vanishes.

The workaround is to use string.cut to chop the special chars off the ends and then string.gsub with a wildcard character "." to sub out the special character for a comma.

Here is what I have that works without saving any illegal characters into your profile:

function updateGroup()

groupString=atcp.MSDPGROUP

memberTable={}

groupTable={}

groupMana={}

groupHp={}

groupMaxMana={}

groupMaxHp={}

groupMove={}

groupMaxMove={}

groupPosition={}

groupStatus={}

groupClass={}

groupLevel={}

groupString=string.gsub(groupString,"NAME.",",")

groupString=string.gsub(groupString,"HITPOINTS.",",")

groupString=string.gsub(groupString,"MAX_HITPOINTS.",",")

groupString=string.gsub(groupString,"MANA.",",")

groupString=string.gsub(groupString,"MAX_MANA.",",")

groupString=string.gsub(groupString,"MOVES.",",")

groupString=string.gsub(groupString,"MAX_MOVES.",",")

groupString=string.gsub(groupString,"POSITION.",",")

groupString=string.gsub(groupString,"STATUS.",",")

groupString=string.gsub(groupString,"CLASS.",",")

groupString=string.gsub(groupString,"LEVELS.",",")

groupString=string.gsub(groupString,"MAX_","")

groupString=string.cut(groupString,groupString:len()-2)

groupString=string.reverse(groupString)

groupString=string.cut(groupString,groupString:len()-8)

groupString=string.reverse(groupString)

groupTable=groupString:split("MEMBER")

for i=1,#groupTable do

memberTable=groupTable:split(",")

for j=1,#memberTable do

memberTable[j]=string.cut(memberTable[j],memberTable[j]:len()-1)

end

--display(memberTable) 

end

groupTable={}

for i=1,#memberTable do

groupTable=memberTable[2]

groupHp[memberTable[2]]=0+memberTable[3]

groupMaxHp[memberTable[2]]=0+memberTable[4]

groupMana[memberTable[2]]=0+memberTable[5]

groupMaxMana[memberTable[2]]=0+memberTable[6]

groupMove[memberTable[2]]=0+memberTable[7]

groupMaxMove[memberTable[2]]=0+memberTable[8]

groupPosition[memberTable[2]]=memberTable[9]

groupStatus[memberTable[2]]=memberTable[10]

groupClass[memberTable[2]]=memberTable[11]

groupLevel[memberTable[2]]=0+memberTable[12]

end

end

</div>

<div class="post" data-post-id="36551" data-author="*juggleblood*" data-date="2016-01-26T21:06:07+00:00" data-subject="Re: MSDPGROUP PARSER">

Ok, finally discovered the missing piece of the puzzle. Thanks Splork, Breeze, and Linx.

sendMSDP("REPORT", "GROUP")

will store the data as an msdp table and to access the data:

msdp.GROUP

msdp.GROUP.MEMBER0

msdp.GROUP.MEMBER0.MANA

etc..

</div>

<div class="post" data-post-id="36552" data-author="*juggleblood*" data-date="2016-01-26T22:35:56+00:00" data-subject="Re: MSDPGROUP PARSER">

I think I still might end up parsing atcp.GROUP myself because of the way msdp.GROUP table is set up:

msdp.GROUP={

MEMBER0={ MANA=1,

                    POSITION=....etc }

MEMBER1={ ... etc

}

Unless I'm missing something, this makes the data hard to access. Would it not be easier to work with if 

msdp.GROUP={

Sochi={ MANA=1,

               POSITION=... },

Crumbs={ ... }

}

Or can someone show me how to easily get from msdp.GROUP to a table called groupMana that contains names and mana, so that I can just use groupMana['Name'], etc...

One of the things giving me trouble with this btw is this: Why does "msdp.GROUP[1][1]" not work? With regular tables you can put the number of the value in brackets to identify it. I was going to use this to make a loop that sorts thru msdp.GROUP and puts the value in tables, but there must be some other kind of syntax for these kind of tables for some reason? lua msdp.GROUP[1] shows nothing, as well as lua msdp.GROUP[1][1]. I would thing that lua msdp.GROUP[1][1] should show me "MEMBER0", but it doesn't seem to work like a regular table.

It's not crucial, so don't spend time on it if you don't know. I've already gotten this far on parsing the atcp string, so I'll get it done one way or another.

</div>

<div class="post" data-post-id="36553" data-author="*juggleblood*" data-date="2016-01-26T23:01:05+00:00" data-subject="Re: MSDPGROUP PARSER">

Well it's a done deal. I'm just sticking with atcp vars until i understand msdp tables better. Everything is working now so no sense touching it again.

One thing I'm noticing tho is that msdp.GROUP.MEMBERX.POSITION options have some vagueness regarding the leader. Leader is either "leader" or "pleader" (point leader), but if leader is not point, then we dont know from msdp whether he/she is in the front or back row.

It's not a big deal, but since position is included, then for completeness i would think leader needs to be "pleader", "leaderf" (leader front row) or "leaderb" (leader back). This would be in case someone wants to manage the front / back row using msdp or if leader wants to track his/her own position via msdp.

</div>

<div class="post" data-post-id="36563" data-author="Dragoth" data-date="2016-01-31T18:40:43+00:00" data-subject="Re: MSDPGROUP PARSER">

This is unrelated, but is there a way to only receive the requested msdpvar once ?

From what I understand, when we use sendmsdp REPORT, we actually ask the server to start sending us reports on value change in that particular msdpvar and in huge groups coupled with loads of active affects this just loads up the subchannel and you get lagged, i would really love to only receive each msdpvar as I request it, not when the server notices a change in it.

What went on:

[![](http://s30.postimg.org/uedrqjrj1/blabla.jpg)](http://postimg.org/image/uedrqjrj1/)

What was going on behind the scenes:

[![](http://s11.postimg.org/fv0c9z5xb/msdpspam.jpg)](http://postimg.org/image/fv0c9z5xb/)

</div>

<div class="post" data-post-id="36564" data-author="*Splork*" data-date="2016-01-31T23:22:45+00:00" data-subject="Re: MSDPGROUP PARSER">

@Dragoth

Sorry but we won't be altering the MSDP code in this manner. 

If a person's group gets so big that it causes them a bit of lag, they will need to remove that variable from their report list or deal with it!

It might be possible to create other group variables and cut down on the amount of information we are sending, that would probably help...

</div>

<div class="post" data-post-id="36565" data-author="Dragoth" data-date="2016-02-01T08:19:34+00:00" data-subject="Re: MSDPGROUP PARSER">

I'm not really asking for anything to be altered, but Is it not possible to create an additional subchannel command, say REQUEST in addition to REPORT, where it does the function of reporting requested msdpvars only once ?

</div>

<div class="post" data-post-id="36566" data-author="*Splork*" data-date="2016-02-01T12:39:12+00:00" data-subject="Re: MSDPGROUP PARSER">

I am sure its possible but its not something we will be doing. 

According to the MSDP Spec which can be found at http://tintin.sourceforge.net/msdp/

REPORT

"The REPORT command can be used by either side, but should typically be used by the client. After the client has received a list of reportable variables, or already knows which variables are supported, it can request the server to start reporting those variables. **When receiving a REPORT request the server should send the requested variables to the client, and re-send each individual variable whenever it changes. **Instead of sending MSDP_VAR "REPORT" MSDP_VAL "HEALTH" MSDP_VAR "REPORT" MSDP_VAL "HEALTH_MAX" it is allowed to string values together for command-like variables, in this case: MSDP_VAR "REPORT" MSDP_VAL "HEALTH" MSDP_VAL "HEALTH_MAX".

Maybe we can figure out a better option when we have tons of data tied to the same variable...

</div>

<div class="post" data-post-id="36567" data-author="Dragoth" data-date="2016-02-01T14:21:52+00:00" data-subject="Re: MSDPGROUP PARSER">

Thanks for the link Splork, this is very in-depth and it solved my issue.

Turns out the command is already built-in, instead of REPORT client should use SEND and the server will send the requested msdpvars only once.

No more subchannel overload for me!

</div>

<div class="post" data-post-id="36568" data-author="Dragoth" data-date="2016-02-01T15:03:21+00:00" data-subject="Re: MSDPGROUP PARSER">

Btw since MSDP varlist is incomplete in helpfiles, here is the full list I was able to retrieve from the server

CHARACTER_NAME

SERVER_ID

SERVER_TIME

SNIPPET_VERSION

WHO_LIST

AFFECTS

STRING_AFFECTS

STRING_PERM_AFFECTS

SPELLS

ALIGNMENT

EXPERIENCE

EXPERIENCE_MAX

EXPERIENCE_TNL

HEALTH

HEALTH_MAX

HEALTH_REGEN

LEVEL

LEVEL_SEC

LEVEL_TER

LEVEL_QUA

LEVEL_QUI

LEVEL_HEX

LEVEL_SEP

LEVEL_OCT

LEVEL_AVA

CITIZEN

CLASS

CLASS_SEC

CLASS_TER

CLASS_QUA

CLASS_QUI

CLASS_HEX

CLASS_SEP

CLASS_OCT

CLASS_AVA

MANA

MANA_MAX

MANA_REGEN

BANK

PRACTICE

MONEY

HONOR

DRACHMA

MOVEMENT

MOVEMENT_MAX

MOVEMENT_REGEN

HITROLL

DAMROLL

AC

STR

INT

WIS

DEX

CON

STR_PERM

INT_PERM

WIS_PERM

DEX_PERM

CON_PERM

OPPONENT_HEALTH

OPPONENT_HEALTH_MAX

OPPONENT_LEVEL

OPPONENT_NAME

TANK_HEALTH

TANK_HEALTH_MAX

TANK_LEVEL

TANK_NAME

AREA_NAME

ROOM_EXITS

STRING_ROOM_EXITS

ROOM_NAME

ROOM_VNUM

ROOM_RNUM

TERRAIN

CONTINENT

WORLD_TIME

CLIENT_ID

CLIENT_VERSION

PLUGIN_ID

ANSI_COLORS

XTERM_256_COLORS

UTF_8

SOUND

MXP

WEAPON_DAM

WEAPON_DAM_CAP

STAB_DAM

STAB_DAM_CAP

UNDEAD_CONT

UNDEAD_CONT_CAP

SPELL_BONUS

SPELL_BONUS_CAP

HEAL_BONUS

HEAL_BONUS_CAP

CHARISMA

CHARISMA_CAP

FLAILDAM

KICKDAM

HAND_DAM

HAND_DAM_CAP

DAM_RED

DAM_RED_CAP

SEX

HUNGER

THIRST

WORSHIPS

POSITION

GROUP_LEADER

COORD1

COORD2

COORD3

COORD4

COORD5

COORD6

COORD7

COORD8

COORD9

COORD10

COORD11

COORD12

COORD13

COORD14

COORD15

COORD16

COORD17

COORD18

COORD19

COORD20

COORD21

COORD22

COORD23

COORD24

COORD25

ROOM_NORTH

ROOM_EAST

ROOM_SOUTH

ROOM_WEST

ROOM_UP

MSDP_ROOM_DOWN

WEAR_LIGHT

WEAR_FINGER_R

WEAR_FINGER_L

WEAR_NECK_1

WEAR_NECK_2

WEAR_BODY

WEAR_HEAD

WEAR_LEGS

WEAR_FEET

WEAR_HANDS

WEAR_ARMS

WEAR_SHIELD

WEAR_ABOUT

WEAR_WAIST

WEAR_WRIST_R

WEAR_WRIST_L

WEAR_WIELD

WEAR_HOLD

WEAR_TWO_HANDED

WEAR_LOADED

WEAR_INSTRUMENT

WEAR_EMBLEM

GROUP

</div>

<div class="post" data-post-id="36569" data-author="*Splork*" data-date="2016-02-01T15:29:33+00:00" data-subject="Re: MSDPGROUP PARSER">

Great find(Forgot about SEND) and nice list!

We have updated the helpfile. Please remember -> do NOT request variables you are not using!!!

</div>

<div class="post" data-post-id="36572" data-author="*juggleblood*" data-date="2016-02-02T19:56:24+00:00" data-subject="Re: MSDPGROUP PARSER">

Very cool. Thanks for both the list and the tip.

</div>
