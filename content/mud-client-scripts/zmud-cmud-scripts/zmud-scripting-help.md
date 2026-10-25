---
title: "ZMud Scripting Help"
topic_id: 894
author: "Methyx"
date: 2005-02-28T07:35:37+00:00
last_activity: 2005-03-09T13:09:05+00:00
last_author: "Akasha2"
sticky: false
locked: false
post_count: 23
---

<div class="post" data-post-id="4659" data-author="Methyx" data-date="2005-02-28T07:35:37+00:00">

Hello All,

I have noticed that the use of scripts in a group setting (especially for tanks) is very helpful.  There are many scripts posted here that I'm sure many of our new players would like to try (me as well), but many of us are not  proficient enough in ZMud or coding to do this.

Could someone please post how to set up the scripts to use in ZMud?  The help file was pretty vague.  There was some mention in a previous post about a class folder (not sure what that is).   Are the scripts supposed to be set up as aliases, triggers, or what?

Thanks in advance for any help you can give :)

Humbly Seeking Enlightenment,

Methyx

Vagabond Monk

BTW....what happened to our pictured avatars??

</div>

<div class="post" data-post-id="4660" data-author="Methyx" data-date="2005-02-28T07:37:03+00:00">

Nevermind about the avatars...seems they've been fixed  :oops:

</div>

<div class="post" data-post-id="4661" data-author="guest" data-date="2005-02-28T08:50:32+00:00">

No clue about Zmud, but about avatar images ... we disabled them a few days for forum maintenance, and they are back.  So you are not seeing strange things.   :)

</div>

<div class="post" data-post-id="4662" data-author="Zam" data-date="2005-02-28T09:21:41+00:00">

No clue about Zmud [/quote:1wrx1ikz]

newbie!

</div>

<div class="post" data-post-id="4664" data-author="karl" data-date="2005-02-28T12:10:49+00:00">

Are you just looking for a tank reporter?  If so, what are you wanting it to report?

</div>

<div class="post" data-post-id="4681" data-author="Methyx" data-date="2005-03-01T08:07:36+00:00">

Basically, I just want some instruction on how to set up the scripts in ZMud.  Setting up a whiner that reports hit points and buff spell status was what I was hoping to start off with.  And hopefully, the instructions come in terms that the layman can understand.  :twisted: 

Splork put out some nice ideas/scripts in his post.  A few of those can be identified as simple, some not so simple, triggers.

Now Xandoras and the rest, these seem to be highly detailed blocks of code which require values for variables to be set up.  The mention of class folders for the different status whiners and mapping tools was mentioned, but I'm not sure what that means.

In utilizing a script, let's say it's a whiner, do I set up an alias/trigger to enable the script?  Is it set up as some part of my Sloth Zmud folder that automatically kicks in when I log in?  If I want to run multiple scripts (whiner, mapper, etc.), is there a collective folder set up for these, and if so, what and how??

</div>

<div class="post" data-post-id="4682" data-author="Akasha2" data-date="2005-03-01T08:51:41+00:00">

A class folder is basically a folder you create in your settings menu of zmud to store triggers/aliases/buttons/etc.  You use class folders to serperate and organize various settings, EG: you might create a folder called BASIC to hold things like triggers for #trigger {^You are hungry.} {get food bag;eat food} and other common instances, including thirst, recite recall, grouptell aliases, etc.

A trigger is something that *triggers* off a string sent from the mud.  Like:

You are hungry.  is sent from the mud telling you that you are hungry.  ZMud processes this string and checks your settings to see if there is a match, in which case might be the above, get food bag;eat food.  Then it does it for you.

An alias is something you configure in your settings to stand for something else, EG: you might setup a folder called COMBAT SPELLS, and inside it you might have #ALIAS fwind {cast 'firewind'}, so that typing fwind sends the cmd cast 'firewind' to the mud.

Variables are strings in which you assign items that might change throughout the course of their life.  EG: you might have an alias set up so that when you log on, Zmud captures the name of your character (for those who use the same batch of scripts for multiple characters).  You might do something like so:

Welcome to SlothMUD... blah blah...

you type: > charname Methyx

In your BASIC folder you have this alias or trigger to process it:

#TRIGGER {^charname %1} {#var charname %1}

This basically takes the %1 (which is a temp placeholder for variables until they are transfered to a string variable using the #var command) and processes it into a string variable for use elsewhere (in this case, charname, which will be refered to as @charname when used later).  Floating, temp variables include %1-%9 and * (that I use most often).  %1-%9 work for anything and * is simply a wildcard that is usually used to  account for junk.  EG: You are following someone in a group who uses:

Myleader -- '*** target blah'

To make a trigger from this using the above info:

first, you need to set up a trigger to recognize who your leader is, this can be done like the assignment of your charname above:

#TRIGGER {^leader %1} {#var leader %1}

so when you type leader Myleader, zmud processes @leader = Myleader.

Now, You can set up the target script:

let's say we create a class folder called TARGETTER, in it we put:

#TRIGGER {^@leader --'(*)target %1'} {#var target %1}

This sets your @target as %1, while the (*) is used to ignore the junk in front of target, and having preset your leader as @leader, the only person who can set this trigger is the person assigned as @leader by you, and not other members of your group who will surely mess with it if they find it to not be secure ;)  

As a note, the ^ at the beginning is what is called grounding your scripts.  This prevents your leader from doing:

gossip You are a target haha fool.

and thereby assigning your target as haha.  

Folders can be set as enabled when connecting or disabled using the properties setting of the class folder itself.  If you have something you do not wish to have on all the time, you set it as disabled and use #t-/+ to turn it on and off using aliases, or for advanced users, setting up buttons can do the same.

for instance, say you only wanted your targetter to operate while you were grouped.  You would set the folder properties as disabled, and in another folder that is enabled, you would put a simple script like:

#ALIAS groupon {#T+ TARGETTER;#show group targetting is on}

#ALIAS groupoff {#T- TARGETTER;#show group targetting is off}

#T+ enables folders, and #T- disables folders.  While #SHOW is used to show the exact text on your screen to you and no one else.  Therefore in the above example, you would see

group targetting is on(or off) on your screen, but no one else would be interupted by your spam.

So, in summary:

TRIGGERS _trigger_ off exact output from the mud, or input from your typing.  They then process the script they are to run, and produce the desired affect you have programmed.

ALIASES _trigger_ off of shortened commands to make your life easier, saving you hundreds of keystrokes an hour.

VARIABLES come in 2 types: floating temp variables like %1-%9 and (*), and string variables to which floating variables have been assigned for later use.

CLASS FOLDERS are simply a way to organize and control your scripts.  To control what is enabled and what is disabled, as to control what scripts are running and what are not.

I hope this clears some stuff up for you... it's about as basic as I can get.

But at least maybe this can help you ask more specific questions.

Akasha/Xandora

</div>

<div class="post" data-post-id="4683" data-author="Akasha2" data-date="2005-03-01T08:54:33+00:00">

> **Akasha wrote:**
> Myleader -- '*** target blah'
> 
> 
> 
> To make a trigger from this using the above info:
> 
> first, you need to set up a trigger to recognize who your leader is, this can be done like the assignment of your charname above:
> 
> #TRIGGER {^leader %1} {#var leader %1}
> 
> so when you type leader Myleader, zmud processes @leader = Myleader.

typoed :)

#TRIGGER {^leader %1} {#var leader %1}

should be

#TRIGGER {^@leader %1} {#var leader %1}

</div>

<div class="post" data-post-id="4684" data-author="Akasha2" data-date="2005-03-01T08:56:06+00:00">

bleah no its not.. im helluva tired, ignore these two posts and go to the 3rd one :) its right.

Aka/Xan

</div>

<div class="post" data-post-id="4687" data-author="karl" data-date="2005-03-01T11:45:49+00:00">

Awesome explaination Akasha/Xandora!!

</div>

<div class="post" data-post-id="4689" data-author="Methyx" data-date="2005-03-01T12:47:23+00:00">

That was a very detailed response and greatly appreciated.  Thank you very much  :D 

This should be my last question on the topic then, as you did ask for a more specific question. 

You posted what looked like a very good whiner.  What do I do in ZMud to implement the whiner after I have copied the code and it's ready to paste? :?: 

Still fumbling in the dark,

Methyx

Vagabond Monk

</div>

<div class="post" data-post-id="4696" data-author="Zenkai" data-date="2005-03-01T14:59:01+00:00">

Basic Whiner:

[code:1wwt823s]#class {Whiner_Script}

#var whiner {0} {0}

#var current_hp {0} {0}

#var maximum_hp {0} {0}

#var delta {0} {0}

#alias whineroff {#show Whiner: Off

#var whiner 0}

#alias whineron {#show Whiner: On

#var whiner 1}

#trigger {^You have %d~((%d)~) hit} {#var maximum_hp %1}

#trigger {^You have ~(%d~/(%d)~+%d~) hit} {#var maximum_hp %1}

#trigger {^~<(%n)hp} {

#if ((@whiner = 1) and (%1 < @current_hp)) {#math delta %1-@current_hp

#if (@delta < -5) {grouptell @delta Ouch! Hp: %1 / @maximum_hp}}

#if ((@whiner = 1) and (%1 > @current_hp)) {#math delta %1-@current_hp

#if (@delta > 15) {grouptell ~+@delta Ahhh! Hp: %1 / @maximum_hp}}

#var current_hp %1}

#class 0[/code:1wwt823s]

How do I install this script?

1. open notepad, cut and paste the above code and save as a text file

2. open zmud, select menu option "Settings" then "Import" then "Script (ASCII)"

3. open the import file that was saved with notepad

Now the script is installed, you can open the Settings Editor and see the class folder Whiner_Script.

PS-

You should use the special pattern matching symbols for trigger patterns, not the parameters %1 to %99. And only wrap () around the special pattern matching symbols if you wish to save the matched pattern in a parameter %1 through %99.

[code:1wwt823s]#TRIGGER {^@leader --'(*)target %1'} {#var target %1}[/code:1wwt823s]

The above code is just wrong, you are going to save the leader's grouptell prefix into the target variable, not the mob.

</div>

<div class="post" data-post-id="4698" data-author="Akasha2" data-date="2005-03-01T17:44:27+00:00">

heh, Zenkai, you and I disagree on so many zmud issues.  The spacing on the target code may be off ( it was 5:30am and I was extremely tired), but that is basically the same script ive used for targetting for years, and it has never given me any trouble. 

Besides Methyx wanted a simple, broken down version in understandable terms.  So that's what I gave him.  My exact target script is:

#TRIGGER {^@leader -- '(*)target %1'} {#var target %1;#if (@tank=@charname) {gt Target set to: \d02@target\c03}}

and it has never failed me ;)

</div>

<div class="post" data-post-id="4699" data-author="Akasha2" data-date="2005-03-01T18:04:35+00:00">

Whiner's are a dime a dozen.  The whiner I posted in another thread somewhere on here is very specific to the custom prompt that supports it.

It takes some getting used to, but you're free to use it:

#ALIAS newprompt {prompt ~<Time ~= $t | $w | $h/$Hhp $m/$Mma $v/$Vmv~>$n}

#ALIAS hpcolorchange {#if (@curhp>=@thirdhp) {#var hpcolor green} {hpcyan}}

#ALIAS hpcyan {#if (@curhp>=@halfhp) {#var hpcolor cyan} {hpyellow}}

#ALIAS hpyellow {#if (@curhp>=@criticalhp) {#var hpcolor yellow} {hpred}}

#ALIAS hpred {#if (@curhp<=@criticalhp) {#var hpcolor red}}

#ALIAS macolorchange {#if (@curma>=@thirdma) {#var macolor green} {macyan}}

#ALIAS macyan {#if (@curma>=@halfma) {#var macolor cyan} {mayellow}}

#ALIAS mayellow {#if (@curma>=@criticalma) {#var macolor yellow} {mared}}

#ALIAS mared {#if (@curma<=@criticalma) {#var macolor red}}

#ALIAS mvcolorchange {#if (@curmv>=@thirdmv) {#var mvcolor green} {mvcyan}}

#ALIAS mvcyan {#if (@curmv>=@halfmv) {#var mvcolor cyan} {mvyellow}}

#ALIAS mvyellow {#if (@curmv>=@criticalmv) {#var mvcolor yellow} {mvred}}

#ALIAS mvred {#if (@curmv<=@criticalmv) {#var mvcolor red}}

#ALIAS hitdown {

#if (@charname=@tank) {

grouptell "["\d02@curhp\c03"|"\d04@maxhp\c03"] "To Full:"<"\d02@needhp\c03"> "DAMG:"<"\d03@diffhp\c03">"

#SUB " "

#SHOW %ansi(white)"<"%ansi(@hpcolor)@curhp%ansi(white)"/"%ansi(green)@maxhp%ansi(white)"hp ~["%ansi(bold,red)@diffhp%ansi(white)"~] "%ansi(@macolor)@curma%ansi(white)"/"%ansi(green)@maxma%ansi(white)"ma "%ansi(@mvcolor)@curmv%ansi(white)"mv>"

} {

#SUB " "

#SHOW %ansi(white)"<"%ansi(@hpcolor)@curhp%ansi(white)"/"%ansi(green)@maxhp%ansi(white)"hp ~["%ansi(bold,red)@diffhp%ansi(white)"~] "%ansi(@macolor)@curma%ansi(white)"/"%ansi(green)@maxma%ansi(white)"ma "%ansi(@mvcolor)@curmv%ansi(white)"mv>"

}

}

#ALIAS hitup {

#if (@charname=@tank) {

grouptell "["\d02@curhp\c03"|"\d04@maxhp\c03"] "To Full:"<"\d02@needhp\c03"> "HEAL:"<+"\d04@diffhp\c03">"

#SUB " "

#SHOW %ansi(white)"<"%ansi(@hpcolor)@curhp%ansi(white)"/"%ansi(green)@maxhp%ansi(white)"hp ~["%ansi(bold,green)"+"@diffhp%ansi(white)"~] "%ansi(@macolor)@curma%ansi(white)"/"%ansi(green)@maxma%ansi(white)"ma "%ansi(@mvcolor)@curmv%ansi(white)"mv>"

} {

#SUB " "

#SHOW %ansi(white)"<"%ansi(@hpcolor)@curhp%ansi(white)"/"%ansi(green)@maxhp%ansi(white)"hp ~["%ansi(bold,green)"+"@diffhp%ansi(white)"~] "%ansi(@macolor)@curma%ansi(white)"/"%ansi(green)@maxma%ansi(white)"ma "%ansi(@mvcolor)@curmv%ansi(white)"mv>"

}

}

#ALIAS nochange {

#if (@diffhp<@hitdown) {

#SUB " "

#SHOW %ansi(white)"<"%ansi(@hpcolor)@curhp%ansi(white)"/"%ansi(green)@maxhp%ansi(white)"hp ~["%ansi(bold,red)@diffhp%ansi(white)"~] "%ansi(@macolor)@curma%ansi(white)"/"%ansi(green)@maxma%ansi(white)"ma "%ansi(@mvcolor)@curmv%ansi(white)"mv>"

} {

#SUB " "

#SHOW %ansi(white)"<"%ansi(@hpcolor)@curhp%ansi(white)"/"%ansi(green)@maxhp%ansi(white)"hp ~["%ansi(bold,green)"+"@diffhp%ansi(white)"~] "%ansi(@macolor)@curma%ansi(white)"/"%ansi(green)@maxma%ansi(white)"ma "%ansi(@mvcolor)@curmv%ansi(white)"mv>"

}

}

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

#math diffma (@curma-@lastma)

#math lastma @curma

#math needma %abs(@maxma-@curma)

#math mapercent ((@curma*100)/@maxma)

#math thirdmv @maxmv-(@maxmv/4)

#math halfmv @maxmv/2

#math criticalmv @maxmv/5

#math diffhp (@curhp-@lasthp)

#math needhp %abs(@maxhp-@curhp)

#math lasthp @curhp

#math hppercent ((@curhp*100)/@maxhp)

#var hitup {20}

#var hitdown {-1}

#math diffma %abs(@curma-@lastma)

#if (@timeofday > 12) {

#math standardtime @timeofday-12

#var ampm pm

#var timeofday @standardtime

} {#if (@timeofday = 0) {

#var timeofday 12

#var ampm am

} {#var ampm am}}

#if (@diffhp=0) {

hpcolorchange

macolorchange

mvcolorchange

nochange

} {

#if (@diffhp<>0) {

#if (@diffhp<@hitdown) {

hpcolorchange

macolorchange

mvcolorchange

hitdown

} {

#if (@diffhp>@hitup) {

hpcolorchange

macolorchange

mvcolorchange

hitup

} {

hpcolorchange

macolorchange

mvcolorchange

nochange

}

}

}

}

}

You can capture this the way Zenkai referred to, or you can just create a CLASS FOLDER called PROMPT-WHINER, set the folder to enabled, open the folder contents, and copy/paste this script into the folder.  Then save settings.  

If youll notice the first command in the script is #ALIAS newprompt.  Type this to change your current prompt to the prompt that this script triggers off of.  

All my scripts are posted at: 

[<LINK_TEXT text="http://ibite.fateback.com/Xandora/ZmudS ... cripts.htm">http://ibite.fateback.com/Xandora/ZmudScripts/ZmudScripts.htm</LINK_TEXT>](http://ibite.fateback.com/Xandora/ZmudScripts/ZmudScripts.htm)

The class folders are pretty self-explanitory, though the scripts might mind-boggle you.  But the instructions Zenkai gave for importing scripts will work for those that are posted, I believe.   But I'm pretty sure also that if not he'll post it ;)

*lick* Zenkai

Aka/Xan

</div>

<div class="post" data-post-id="4710" data-author="Zenkai" data-date="2005-03-02T01:14:44+00:00">

Sorry Akasha, I shouldn't have said your trigger was wrong :) but it may not work in the new zMUD version.

Here is a contrived example of a trigger that has different outputs for different zMUD versions.

#trigger {^(%w) tells you '%1'} {#echo Message = %1}

#echo Zugg tells you 'hello'

Output in zMUD 5.55:

Zugg tells you 'hello'

Message = hello

Output in zMUD 7.05:

Zugg tells you 'hello'

Message = Zugg

This is why I don't like using numbered parameters in trigger patterns because it is easy to write a version specific trigger.

You can still use %1..%99 in the pattern in the new version. They are converted to (*) by default. The main issue is that the %1..%99 need to be in numeric order.

If you used a trigger like so, it would work in both versions:

#trigger {^(%w) tells you '(*)'} {#echo Message = %2}

Happy Scripting :)

</div>

<div class="post" data-post-id="4711" data-author="Akasha2" data-date="2005-03-02T02:31:13+00:00">

actually i use version 7.05, and it doesnt require me to use %1-%99 in any particular order.  I can use (*), then %1, and it doesnt appear to make a difference, maybe 1 of my preference settings is different than yours or something.

*shrug*

</div>

<div class="post" data-post-id="4720" data-author="13" data-date="2005-03-02T16:33:57+00:00">

I really like them.

[http://www.journeys.com/images/products/1_16924_FS.jpg](http://www.journeys.com/images/products/1_16924_FS.jpg)

</div>

<div class="post" data-post-id="4721" data-author="Leaf" data-date="2005-03-02T16:50:16+00:00">

Why did u post that in this thrend?  It should have been in that Pic thrend, cause who cares  :P

</div>

<div class="post" data-post-id="4722" data-author="13" data-date="2005-03-02T17:20:30+00:00">

Hi, my name is Aaron Young and I am writing you this so that you

will tell me please what a "thrend" is.  You mentioned it twice already,

and I am quite curious sir!  

Eat a Bowl of Dicks,

Aaron

</div>

<div class="post" data-post-id="4730" data-author="Leaf" data-date="2005-03-02T19:09:45+00:00">

Eat a Bowl of Dicks,

Aaron[/quote:1cu1rka8]

Glad u got that out of ur closet. hehe

</div>

<div class="post" data-post-id="4740" data-author="Methyx" data-date="2005-03-03T11:11:50+00:00">

My thanks go to both Xandora and Zenkai.  I have a newbie monk meat shield who is making very good use of the help you provided  :D 

Ignorance begins when the quest for knowledge ends,

Methyx

Vagabond Monk

</div>

<div class="post" data-post-id="4910" data-author="Methyx" data-date="2005-03-09T12:39:29+00:00">

Hey Xandora,

Your script took my Zmud window to a split screen with communications on top and basic activity on the lower window.  Very nice touch, I don't miss communications due to battle spam :)  However, I accidentally closed out the top window, and I cannot for the life of me figure out how to get that window config back.  Can you help me restore the config?

Smooth seas do not a skillful sailor make, hence I seek the storm,

Methyx,

Vagabond Monk

</div>

<div class="post" data-post-id="4912" data-author="Akasha2" data-date="2005-03-09T13:09:05+00:00">

It should just pop back open when that particular communication comes through the scripts.  If that doesnt work, check your class folder where your #gag/#cap scripts are and unsure the script wasnt deleted accidently.  

Once you have your screen the way you want it once again, you can go into the Layout menu on the top of your zmud window and select Save Layout.  Just give your layout a name.  Next, click on Chars, highlight the selection which you choose to log onto sloth with, then click on Edit, select the Files tab.  In the info below you will see a space for Layout.  Here, just type the name of the layout you just saved.

EG: if you saved it as mylayout, then in the box provided you need to type mylayout.lay 

This should prevent the loss of your windows in the future.  This will force your zmud to automatically open with the split windows by default.

Aka/Xan

</div>
