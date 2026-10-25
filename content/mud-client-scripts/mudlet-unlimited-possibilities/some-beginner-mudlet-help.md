---
title: "Some beginner mudlet help."
topic_id: 4195
author: "DarkArtist"
date: 2014-02-14T00:59:36+00:00
last_activity: 2014-12-27T04:30:16+00:00
last_author: "*juggleblood*"
sticky: false
locked: false
post_count: 17
---

<div class="post" data-post-id="34863" data-author="DarkArtist" data-date="2014-02-14T00:59:36+00:00">

Please post any newbie mudlet questions you have here. This is in response to a request for help ingame.

The first question was: How to set up simple targeting.

First define your global target variable. Outside of functions, all of your variables are global vars and have to be defined in a script. In this case make a script and name it Main Definitions or something like that.

Inside that script you can define as many variables as you want.

target=target or ""

leader=leader or ""

tank=tank or ""

Here is the trigger pattern for matching the leader's called target:

^(\w+) -- 'target (.*)'$  (perl regex)

and the script:

if matches[2] == groupLeader then

local words = matches[3]:split(" ")

target = words[#words]

echo(" :::: Target is now: ".. target .. "\r\n")

end

some explanation:

\w+ means one or more consecutive letters (a word)

.* means zero or more of any kind of character (anything)

matches[2] is the first set of parenthesis because matches[1] is reserved for the entire triggering line.

local words =  means set a local variable thats only used within this script

I won't get into explaining the splitting as it could probably be done better now that I look at it, but this works.

</div>

<div class="post" data-post-id="34866" data-author="DarkArtist" data-date="2014-02-15T13:43:09+00:00">

Another one by request. For tracking:

Pattern:

^Tracks to (.+) lead (\w+)ward?\.$

Script:

tracking=true

send(matches[3])

tempTimer(1,[[send("track "..target)]])

selectCurrentLine()

fg("turquoise")

Tracking flag is nonessential of course but can be useful depending on what you're doing. The time delay makes it run smoother.

</div>

<div class="post" data-post-id="34868" data-author="DarkArtist" data-date="2014-02-15T15:02:04+00:00">

Here is some help getting getmsdpvars setup correctly. There are some issues with the other thread that discusses it.

Here is my getmsdpvars function script:

function getmsdpvars(event, args)

   tempTimer(1, 

function () sendATCP("@REPORT", 

[[HEALTH HEALTH_MAX SERVER_ID STRING_AFFECTS HUNGER THIRST 

 MANA MANA_MAX HITROLL DAMROLL ALIGNMENT EXPERIENCE MONEY TERRAIN

 OPPONENT_HEALTH 	OPPONENT OPPONENT_NAME OPPONENT_HEALTH_MAX OPPONENT_LEVEL

 POSITION MOVEMENT MOVEMENT_MAX AREA_NAME ROOM_NAME ROOM_VNUM AC

 TANK_NAME GROUP_LEADER TANK_HEALTH TANK_HEALTH_MAX STRING_ROOM_EXITS]]

) end)

end

*I've got this set up with no event. Just what you see above. These are the only vars i'm using currently, if you add to this list WATCH YOUR SPACING. If you foul up the spacing, some variables won't load.

Then I set up a separate script that runs getmsdpvars at startup called init_msdp:

function init_msdp()

	getmsdpvars()

end

Set a trigger on any of the mud startup messages that executes getmsdpvars(). Remember that there are different messages for reconnect than connect, so make sure you've got both covered.

Previously I advised tacking this on the event msdpserver_id. This was a bad mistake. You don't want to send this command to the mud every second or you'll lag yourself and possibly everyone else. I wasn't aware at the time that server_id was getting resent every second.

</div>

<div class="post" data-post-id="34869" data-author="DarkArtist" data-date="2014-02-15T15:08:52+00:00">

Script name: updateOppHealth()

function updateOppHealth()

oppHealth=atcp.MSDPOPPONENT_HEALTH

end

Timer: OppHealth 5 seconds

if position=="Fighting" then

cecho("<tomato>"..oppHealth.."<reset>")

end

which assumes...

Script name: updatePosition()

function updatePosition()

position=atcp.MSDPPOSITION

end

You could also stick a flag in updatePosition if position="Fighting" then fighting=true else fighting=false. 

Also don't forget to define any variables  you use in your main definitions, for example:

oppHealth=oppHealth or 0

position=position or ""

fighting=fighting or false

</div>

<div class="post" data-post-id="34902" data-author="Maarg" data-date="2014-03-11T09:04:58+00:00">

I've got an error when trying your track addon:

Lua error:[string "send("track "..target)"]:1: attempt to concatenate global 

'target' (a nil value)

</div>

<div class="post" data-post-id="34903" data-author="DarkArtist" data-date="2014-03-11T12:40:43+00:00">

Usually that means you didn't define the variable. 

I keep all my variable definitions in a single script called Definitions and I do them all like this:

target=target or ""

foodCount=foodCount or 0

This way if the variable is already defined then it's value does not change should you reinitialize the definitions script. i.e. set the value of target to target, unless target is nil, in which case target="" .

</div>

<div class="post" data-post-id="34904" data-author="DarkArtist" data-date="2014-03-11T12:44:25+00:00">

Another by request:

AutoSkill/Spell Toggles

autoKick=autoKick or true

alias:

^autokick$

if autoKick~=true then

autoKick=true

cecho("enabled")

else autoKick=false

cecho("disabled")

end

trigger:

Your boots need polishing again - blood all over. (exact)

^Your kick hits (.*) in the solar plexus.$ (regex)

Your beautiful full-circle-kick misses (begin substring)

You miss your kick at (begin substring)

script:

if autoKick==true then send("kick") end

</div>

<div class="post" data-post-id="34908" data-author="DarkArtist" data-date="2014-03-13T11:58:56+00:00">

Someone asked about autohealing the tank. There's 3 ways one could go about it: a timer that checks tank health every x seconds, a check in updateTankHealth, or a trigger off the tanks reporter.

I don't have a cleric, but I'm thinking the best answer might be the simple trigger off the tank reporter. It's a toss up between that and a timer. 

The disadvantage of using the updated msdp variable as an event is that it's constantly sending the updated value, so you have to do some tricky stuff to avoid sending extra heals. It can be done of course, but it's much more advanced.

I give the trigger a slight advantage over the timer because you can count on the reporter to fire once per round, whereas with the timer you have to play with it to get it just where u want it and also the time a combat round takes varies with lag. Also using the reporter gives the tank some control over the healing. And finally, the reporter trigger is the easiest to set up and requires no msdp.

Feel free to disagree. Can post the setup of any of these 3 methods on request. Hope that helps.

</div>

<div class="post" data-post-id="35456" data-author="Unsub" data-date="2014-10-17T20:18:39+00:00">

>> First define your global target variable. Outside of functions, all of your variables are global vars and **have to be defined in a script**. In this case make a script and name it Main Definitions or something like that.

Inside that script you can define as many variables as you want. <<

From these directions, I think I use the script button, not triggers or aliases to open a window to put in my variable definitions.   I'm not sure how to enter the variables.  There are boxes for registered event handlers, user defined event handlers, and the big box that says lua functions go here.  

What goes in the boxes if anything?  

Alias's seem to call code from input, triggers call code from mud input, what does a script do?

</div>

<div class="post" data-post-id="35457" data-author="DarkArtist" data-date="2014-10-18T08:09:13+00:00">

scripts all load up at start and remain there. They define variables and functions.

So I could make a function in a script like recall() or reciteMoldy() or a variable or a table definition. Then I can refer back to that function, variable, or table in other places like aliases, triggers, or timers. 

One tip about making a script that might not be intuitive is you click activate twice and then save item before you see the green tick appear indicating that it's been applied.

User defined events are something different. Leave it blank. I don't use them personally.

</div>

<div class="post" data-post-id="35583" data-author="Tsuman" data-date="2014-12-27T00:20:58+00:00">

Alright, trying to make triggers for the coliseum. my problem is, as a noncaster monk, ether mobs. specifically "A giant ethereal ant". My current script is this:

^(.*) is waiting for you on the other side.$    pearl regex <--Trigger line

if matches[2] == "A giant ethereal ant" then

send("wraithtouch "..matches[3])

else

send("deathgrip "..matches[3])

send("release")

end

However, with this setup, things like "A giant ethereal ant" and "An undead octopus" get the response

"Deathgrip who?"  I assume this is because when "deathgrip an undead octopus" is sent, the game only reads "deathgrip an" and doesn't know who to hit. Any advice??

</div>

<div class="post" data-post-id="35585" data-author="*juggleblood*" data-date="2014-12-27T00:35:46+00:00">

one simple way to adjust it would be:

(\w+) is waiting for you on the other side\.$

Now this just means match the first whole word before the 'is'. So if example you had:

A giant ethereal ant is waiting for you on the other side.

matches[2]=ant

</div>

<div class="post" data-post-id="35586" data-author="parsec" data-date="2014-12-27T01:10:20+00:00">

Tsuman, here's how I'm testing the regex.

Juggleblood says to use:

(\w+)\ stands before you.$

..so to test, I use:

(\w+)\ stands before you.\'$

..and I tell it to do this:

echo(matches[2].."\n")

..and then I type:

say A large boar stands before you.

Like this:

<420hp 217ma 155mv>

say A large boar stands before you.

You say 'A large boar stands before you.'boar

<420hp 217ma 155mv>

Now that I know my trigger works, I change it back to this:

(\w+)\ stands before you.$

(exactly what Juggleblood wrote)

</div>

<div class="post" data-post-id="35587" data-author="Tsuman" data-date="2014-12-27T01:16:39+00:00">

I appreciate the help from everyone, and I'm sorry if i'm just retarded and that's why it's not working lol here's what I have...

(\w+) is waiting for you on the other side\.$ <-- what Juggleblood wrote.

if matches[2] == "ant" then

send("wraithtouch "..matches[3])

else                                                           

send("deathgrip "..matches[3])

send("release")

end

I tested it by going into the coliseum. push button, I get this...

A rusty iron wall in the center of the arena slowly lowers into the floor.

A sludge monster is waiting for you on the other side.

And the trigger doesn't fire. It does literally nothing. I did this with 8 different enemies. Nothing happened... what am I doing wrong?

</div>

<div class="post" data-post-id="35588" data-author="parsec" data-date="2014-12-27T01:25:24+00:00">

Change your stuff to this:

if matches[2] == "ant" then

send("wraithtouch "..matches[2])

else 

send("deathgrip "..matches[2])

send("release")

end

(all matches[2])

</div>

<div class="post" data-post-id="35589" data-author="abraxsis" data-date="2014-12-27T01:27:54+00:00">

> **Tsuman wrote:**
> if matches[2] == "ant" then
> 
> send("wraithtouch "..matches[3])
> 
> else                                                           
> 
> send("deathgrip "..matches[3])
> 
> send("release")
> 
> end

what about 

if matches[2] == "ant" then

send ("wraithtouch ant")

else send ("deathgrip"..matches[2])

end

I noticed you have matches [2] at the beginning and matches [3] later on, if im thinking right they should be matches [2]

---- sorry, looks like parsec beat me to the punch -----

</div>

<div class="post" data-post-id="35591" data-author="*juggleblood*" data-date="2014-12-27T04:30:16+00:00">

> **Tsuman wrote:**
> if matches[2] == "ant" then
> 
> send("wraithtouch "..matches[3])
> 
> else                                                           
> 
> send("deathgrip "..matches[3])
> 
> send("release")
> 
> end

typo...You changed matches[2]  to matches[3]

</div>
