---
title: "AFFECTS"
topic_id: 4501
author: "Linx"
date: 2015-07-15T16:21:24+00:00
last_activity: 2016-03-03T11:21:26+00:00
last_author: "Madigan"
sticky: false
locked: false
post_count: 16
---

<div class="post" data-post-id="35992" data-author="Linx" data-date="2015-07-15T16:21:24+00:00">

Thought I'd share a bit of code I use to display all the Prots currently up and their timers

from the MSDP var AFFECTS in a miniConsole window

Firstly you need the "AFFECTS" var in your msdp initialise code

```
sendMSDP("REPORT","AFFECTS")
```

This brings in all the currently active Prots in a Lua table "AFFECTS"

Test that it is working by casting several Prots and typing;

lua msdp.AFFECTS

in the command line. You should get something similar to below

{

  rejuvenation = "401",

  darksight = "6706",

  grace = "384",

  ["detect invisibility"] = "21649",

  aegis = "2177",

  class = "-1",

  ["dark cloak"] = "2177",

  ["item-generated"] = "-1"

}

You see two odd ones "item-generated" and "class", we will filter them out later.

Prots with white spaces or multi-words are encapsulated in [" "]

Next, create a miniConsole to display all the Prots in (adjust x,y as needed so it sits where you want it)

```
createMiniConsole("test",900,0,420,200)
setMiniConsoleFontSize("test", 9)
setBackgroundColor("test",20,0,0,255)
```

Here the miniConsole is called "test"

Next, create a new script, call it UpdateSStats

Add a Event Handler msdp.AFFECTS 

(type msdp.AFFECTS in "Add User Defined Defined Event Handler:" and click the +)

and add the code as below

```
function UpdateSStats()
clearWindow("test")
for k,v in pairs(msdp.AFFECTS) do 
	if (k ~= "item-generated") then
		if k ~= "class" then
				echo("test",string.format("%-20s",string.upper(k))..string.format("%5s",os.date("*t",v).min..":"..os.date("%S",v)).."\n")
		end
	end
end
end
```

The miniConsole should look like the code window below and constantly update. 

As a Prot falls it is removed from the table and doesn't display.

```
DARKSIGHT            24:16
GREATER FLUIDITY     11:59
DETECT INVISIBILITY  33:19
DARK CLOAK            8:47
AEGIS                 8:47
GRACE                22:08
PETRIFIED ARMOR      28:44
IMPROVED HASTE        6:41
```

Any issues let me know or ask in-game

Linx

</div>

<div class="post" data-post-id="35993" data-author="*Breeze*" data-date="2015-07-16T03:31:11+00:00">

thanks for sharing Linx.

tested it out and it works well.

here is your script in a package importable into mudlet with the package manager and added it to my mudlet-tools script generator. (made a slight change) 

//Breeze

</div>

<div class="post" data-post-id="35995" data-author="Unsub" data-date="2015-07-16T15:21:31+00:00">

Awesome stuff for the programmer/players.  At some point, I hope someone will do some stuff for non-programmers (me) and other newbies.  After playing a while, I understand that an enhanced interface is not necessary for me to play and have fun. I do enjoy my sloth.

But, for those of us playing with less info and tools it can be kind of a bummer to think we might be playing with one hand tied behind our backs.

An example would be code to allow a non-programmer to use group targeting.

You might say this has been provided, but the bits posted always assumes that the user has set variables for leaders and such installed in a way to take advantage of the snippets provided.  And that the user has the knowledge and skills to adapt the snippet to their client.

Anyway, very cool stuff, good of you to share it.

</div>

<div class="post" data-post-id="35996" data-author="*Breeze*" data-date="2015-07-16T15:59:23+00:00">

> **Unsub wrote:**
> Awesome stuff for the programmer/players.  At some point, I hope someone will do some stuff for non-programmers (me) and other newbies.  After playing a while, I understand that an enhanced interface is not necessary for me to play and have fun. I do enjoy my sloth.
> 
> 
> 
> But, for those of us playing with less info and tools it can be kind of a bummer to think we might be playing with one hand tied behind our backs.
> 
> 
> 
> An example would be code to allow a non-programmer to use group targeting.
> 
> 
> 
> You might say this has been provided, but the bits posted always assumes that the user has set variables for leaders and such installed in a way to take advantage of the snippets provided.  And that the user has the knowledge and skills to adapt the snippet to their client.
> 
> 
> 
> Anyway, very cool stuff, good of you to share it.

Already working on that. Check you pm.

</div>

<div class="post" data-post-id="35997" data-author="Unsub" data-date="2015-07-17T13:38:24+00:00">

Thanks Breeze for helping me with Mudlet.  Much appreciated!

</div>

<div class="post" data-post-id="36689" data-author="Madigan" data-date="2016-03-02T20:21:25+00:00">

So I stole some of the code from an old mudlet "status window" snippet but I can't seem to get it to work.

I would like to use the same miniconsole that I'm using to show affects to shows the following as well.

```
echo("<green>-----------------------------------\n")
cecho("<green> Continent :<white> "..atcp.MSDPCONTINENT.."\n")
cecho("<green> Char      :<white> "..atcp.MSDPCHARACTER_NAME.."\n")
cecho("<green> EXP       :<white> "..atcp.MSDPEXPERIENCE.."\n")
cecho("<green> Coins     :<white> "..atcp.MSDPMONEY.."\n")
cecho("<green> AC        :<white> "..atcp.MSDPAC.."\n")
cecho("<green> HIT/DAM   :<white> +"..atcp.MSDPHITROLL.."/+"..atcp.MSDPDAMROLL.."\n")
cecho("<green> Group \n")
cecho("<green> Leader    :<white> "..atcp.MSDPGROUP_LEADER.."\n")
cecho("<green> Tank      :<white> "..atcp.MSDPTANK_NAME.."\n")
cecho("<green> Target HP :<white> "..atcp.MSDPOPPONENT_HEALTH.."/"..atcp.MSDPOPPONENT_HEALTH_MAX.."\n")
cecho("<green> Target    :<white> "..target.."\n")
```

Any suggestions on how to get the above data into A miniconsole also?

</div>

<div class="post" data-post-id="36694" data-author="*Breeze*" data-date="2016-03-03T07:41:12+00:00">

you have to use msdp not atcp. 

search my script for msdp. 

you also have to tell echo/cecho which window to target. 

	[Utility] Affects Window

- Affects Window (mostly) by Linx 

  by Linx

does this already 

also 

lua msdp 

will show what the mud is sending. will share part of my mortal script in a few days if you can't figure it out

</div>

<div class="post" data-post-id="36695" data-author="Madigan" data-date="2016-03-03T07:53:57+00:00">

> ***Breeze* wrote:**
> you have to use msdp not atcp.

 

I should have clarified - i knew that, i just wanted to see those specific MSDP Attributes.

> ***Breeze* wrote:**
> search my script for msdp. 
> 
> you also have to tell echo/cecho which window to target.

 

I haven't see a script of yours doing this and I was ab le to get the mdsp attributes to echo, but exactly as you said... it was spamming it to my main window - not linx's affect's window like I was attempting.

> ***Breeze* wrote:**
> [Utility] Affects Window
> 
> - Affects Window (mostly) by Linx 
> 
>   by Linx
> 
> does this already

 

Hrmm, no it only shows Affects, and i can't seem to get it to show any other msdp attribs. IF I had one example I could figure out the rest.

> ***Breeze* wrote:**
> also 
> 
> lua msdp 
> 
> will show what the mud is sending. will share part of my mortal script in a few days if you can't figure it out

This is awesome... hes I think everything I need is being sent  already ( I was able to uncomment the attributes I needed from Linx's onConnect script to get msdp.

Blix

</div>

<div class="post" data-post-id="36696" data-author="*Breeze*" data-date="2016-03-03T08:03:25+00:00">

onConnect is mine. 

I adapted Linx script to work with my code. and did some other changes which no one will notice. 

echo("AffectsWindow",  "Foo:Bar") ;

</div>

<div class="post" data-post-id="36698" data-author="Madigan" data-date="2016-03-03T08:35:52+00:00">

> ***Breeze* wrote:**
> Screenshot.. not really as blurry as it looks but I edited it in cell phone. 
> 
> 
> 
> [https://imageshack.com/i/pmcg2qgwp](https://imageshack.com/i/pmcg2qgwp)
> 
> 
> 
> I prefer simple interface

Yes, BOOM... Exactly THIS is what I was trying to build. I have a tabbed chat window I adapted from mudlet forums on the bottom now.

</div>

<div class="post" data-post-id="36699" data-author="*Breeze*" data-date="2016-03-03T08:37:33+00:00">

you should be able  to finish it now. :)

</div>

<div class="post" data-post-id="36700" data-author="Madigan" data-date="2016-03-03T09:13:19+00:00">

> ***Breeze* wrote:**
> you should be able  to finish it now. :)

I must have missed something.

```
function UpdateSStats()
	clearWindow("AffectsWindow")
   echo("AffectsWindow","\nStatus\n--------\n")
   echo("AffectsWindow"," Group Leader: "..msdp.GROUP_LEADER.."\n")
--   echo("AffectsWindow"," XP: "..msdp.MSDPEXPERIENCE.."\n")
--   echo("AffectsWindow"," XP: "..msdp.MSDPMONEY.."\n")
--   echo("AffectsWindow"," AC: "..msdp.MSDPAC.."\n")
   echo("AffectsWindow","\nAffects\n--------\n")
	for k,v in pairs(msdp.AFFECTS) do 
   	if (k ~= "item-generated") then
      	if k ~= "class" then
   	
echo("AffectsWindow",string.format("%-20s",string.upper(k))..string.format("%5s",os.date("*t",v).min..":"..os.date("%S",v)).."\n")
     	end
  		end
	end
end
```

Got one line to show up in the window, but more than one msdp var causes the whole box to clear, so I commented them out. Maybe I was supposed to gather something from what you shared in that pic aside jealousy , lol.. but its not helping me with the code. 

PS - if all affects drop - the msdp vars drop too...

</div>

<div class="post" data-post-id="36701" data-author="*Breeze*" data-date="2016-03-03T09:25:36+00:00">

missing the ; at the end of the commands

</div>

<div class="post" data-post-id="36702" data-author="*Breeze*" data-date="2016-03-03T09:27:24+00:00">

also iirc you need to use msdp["xxxx"]  INSTEAD  of msdp. xxxx

</div>

<div class="post" data-post-id="36703" data-author="Madigan" data-date="2016-03-03T10:16:26+00:00">

> ***Breeze* wrote:**
> also iirc you need to use msdp["xxxx"]  INSTEAD  of msdp. xxxx

as far as I can tell it works the same for both syntax's.

</div>

<div class="post" data-post-id="36704" data-author="Madigan" data-date="2016-03-03T11:21:26+00:00">

Here is my completed script as an update to both Linx's and Breeze's work. Please feel free to use freely.

```
function UpdateSStats()
	clearWindow("AffectsWindow")
     cecho("AffectsWindow","\n<yellow>Status\n<green>--------\n");
     cecho("AffectsWindow","<green>\nTarget\:<white> "..target.."<green>  HP:<white> "..msdp["OPPONENT_HEALTH"].."\n");
     cecho("AffectsWindow","<green>--------------------------------------------\n");
     cecho("AffectsWindow","<green>Continent:<white> "..msdp["CONTINENT"].."<green>  Area:<white> "..msdp["AREA_NAME"].."\n");
     cecho("AffectsWindow","<green>--------------------------------------------\n");
     cecho("AffectsWindow","<green>Group Leader:<white> "..msdp["GROUP_LEADER"].."<green>  Tank:<white> "..msdp["TANK_NAME"].."\n");
     cecho("AffectsWindow","<green>Align:<white> "..msdp["ALIGNMENT"].."\n");
     cecho("AffectsWindow","<green>XP:<white> "..msdp["EXPERIENCE"].."<green>   $$:<white> "..msdp["MONEY"].."\n");
     cecho("AffectsWindow","<green>HIT/DAM:<white> +"..msdp["HITROLL"].."/+"..msdp["DAMROLL"].."<green>   AC:<white> "..msdp["AC"].."\n");
     cecho("AffectsWindow","<green>[Weap Dam]:<white> "..msdp["WEAPON_DAM"].."<green> [Stab Dam]:<white> "..msdp["STAB_DAM"].."<green> [Spell Bonus]:<white> "..msdp["SPELL_BONUS"].."\n");
     cecho("AffectsWindow","\n<yellow>Affects\n<green>--------\n")
 	for k,v in pairs(msdp.AFFECTS) do 
    	if (k ~= "item-generated") then
       	if k ~= "class" then
   	
echo("AffectsWindow",string.format("%-20s",string.upper(k))..string.format("%5s",os.date("*t",v).min..":"..os.date("%S",v)).."\n")
      	end
  		end
	end
end
```

If you already had Linx's affects script :

1) just paste the above code over his scripts/slothMUD/utility/UpsateSStats script.

2) add the following changes to the [onConnect] initAffectsWindow  trigger also:

```
createMiniConsole("AffectsWindow",900,0,600,510)
setMiniConsoleFontSize("AffectsWindow", 10)
setBackgroundColor("AffectsWindow",0,0,0,255)
```

right click the image link below and choose to open in a new window.

![](https://www.dropbox.com/s/2r7u0y2to45c9w0/Updated-Affects-Status-WIndow.jpg?dl=0)

<LINK_TEXT text="https://www.dropbox.com/s/2r7u0y2to45c9 ... w.jpg?dl=0">https://www.dropbox.com/s/2r7u0y2to45c9w0/Updated-Affects-Status-WIndow.jpg?dl=0</LINK_TEXT>

</div>
