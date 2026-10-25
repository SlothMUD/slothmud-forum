---
title: "AutoStab"
topic_id: 4170
author: "DarkArtist"
date: 2013-12-14T13:23:47+00:00
last_activity: 2013-12-14T20:31:33+00:00
last_author: "DarkArtist"
sticky: false
locked: false
post_count: 4
---

<div class="post" data-post-id="34631" data-author="DarkArtist" data-date="2013-12-14T13:23:47+00:00">

Hi Amoeba, I hope this helps.

Acquiring target from leader:

pattern: ^(\w+) -- 'target (.*)'$

script- check leader and store target  ***select perl-regex from the box**

if matches[2] == groupLeader then

local words = matches[3]:split(" ")

currentTarget = words[#words]

echo(" :::: Target is now: ".. currentTarget .. "\r\n")

end

then

pattern:^Exits$ 

script-check if my autostabbing is engaged and if so, stab target:

if autostab=true  then send("backstab "..currentTarget) end

and an alias for turning it on and off..

pattern:^autostab$

script:

autostab=autostab or false ---to define it, or put this in your definitions script

if autostab==false then autostab=true echo("stab on") else autostab=false echo("stab off") end

That's the brunt of it. I don't mind helping flushing it out either for example you could add:

...then if fighting==false then backstab(currentTarget) else send("grouptell 'cant stab, im fighting'") ...or wutever

I set up the fighting flag by setting up a script that sets the flag every time MSDPOPPONENT changes, if opponent=="" then fighting=false.  I like this setup because in a script I can set fighting=true and I wouldn't stab on multiple occurences of a pattern. For example if i trigger to stab kobold on kobold standing here and there's 10 kobolds in the room, it would only stab 1 because after the first one fighting=true. but after the fight fighting returns back to false when msdpopponent updates.

Addendum:

The above requires you have a couple group definitions set up. If you don't know what this means, go to scripts and create a new script and name it group definitions.

groupLeader=groupLeader or ""

currentTarget=currentTarget or ""

Now everytime mudlet starts, it will execute the above, which means, if this variable exists, keep it the same, otherwise create it and set it to "" 

So now make a new alias with the pattern ^leader (\w+)$ that executes: 

leader=matches[2] 

echo("leader="..matches[2])

</div>

<div class="post" data-post-id="34632" data-author="DarkArtist" data-date="2013-12-14T20:01:05+00:00">

something else you might find useful is to make a function in your scripts for fight() heal() armor() ..wutever

so create a new script and call it battle functions or something and put them all in one script, it'll all execute at start

here's an example

----Fight() = initiate combat if I'm not already fighting, set fighting to true, and do whatever spell / skill

----

function fight(mob)

if fighting==false and hitpoints>minHitpoints 

then fighting=true web(mob) strike(mob)

end end

function backstab(mob)

if fighting==false and hitpoints>minHitpoints and tankHealth>minTankHealth 

and leaderHealth>minLeaderHealth and currentWeapon=stabWeapon and imLit=true and tankLit=true

then send("backstab "..mob)

else send("|") send("grouptell I'm not in the mood to stab right now. Go ahead."

end end

ad infinitum...

</div>

<div class="post" data-post-id="34633" data-author="DarkArtist" data-date="2013-12-14T20:19:47+00:00">

Regarding the above example, if you want the fight flag to operate as such, then you need to follow Akaya's thread and insert the script for getmsdpvars and set it up to trigger on init event. Instructions in that thread. If you run into problems on login after adding that script, remove the two delayed carriage returns, the tempTimer([[...]]) functions. 

but then you also have to setup the update scripts for each msdpvar that you want to use. i suggest opponent as your first because fighting is a handy flag to use to make sure you dont send unwanted backstab commands.

here is my MSDPOPPONENT_NAME updater script:

script name: updateOpponent    *script name MUST match the fucntion name u define for it to work*

registered event handlers: MSDPOPPONENT_NAME *you have to type it in the box below and click +*

function updateOpponent()

opponent=atcp.MSDPOPPONENT_NAME

if opponent=="" then fighting=false else fighting=true end

end

Now this is not a perfect system, the opponent seems to clear immediately after the morted time expires which leaves a lag time between which the player can act. The solution is to add some redundancy to the system by adding additional triggers that flip the fighting flag on or off. Play with it to your liking, but for example you could actually flip fighting to true on R.I.P. and then turn it off on the sacrifice or on the next Exits: That way you aren't backqueing a backstab that'll execute in the next room or whatever. You can always assume that if opponent~="", i.e. there IS an opponent, then you are definitely fighting. When it's not, it gets fuzzier, you could be just wrapping up the fight and not ready to stab again yet.

</div>

<div class="post" data-post-id="34634" data-author="DarkArtist" data-date="2013-12-14T20:31:33+00:00">

btw is there a script with all the update functions for all the MSDPVARS already written by someone available? pls post link if u have one, or just post the whole thing here actually pretty pls.

</div>
