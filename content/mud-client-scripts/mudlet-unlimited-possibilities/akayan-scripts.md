---
title: "Akayan Scripts"
topic_id: 4002
author: "Akaya"
date: 2013-01-10T08:04:48+00:00
last_activity: 2016-06-30T17:03:39+00:00
last_author: "Akaya"
sticky: false
locked: false
post_count: 59
---

<div class="post" data-post-id="33908" data-author="Akaya" data-date="2013-01-10T08:04:48+00:00" data-subject="Akayan Scripts">

I'm very new to SlothMUD but not Mudlet. I'll do my best to post some useful scripts here. If you have any suggestions, or things you'd like to have, feel free to speak your voice.

The majority of scripts that create a user interface (UI) utilize the Vyzor Framework ( a mudlet script that makes creating a UI much easier ) so you'll want to grab a copy and install it which you can find [here](https://github.com/Oneymus/Vyzor). Download vyzor.mpackage from that link and install it using the Package Manager located on the Mudlet toolbar. Once you install, restart Mudlet for everything to take effect.

I'm happy to answer any questions you have and/or walk you through the installation process. Enjoy!

</div>

<div class="post" data-post-id="33909" data-author="Akaya" data-date="2013-01-10T08:13:39+00:00" data-subject="Re: Akayan Scripts">

This first script will activate the MSDP information exchange. This will give you loads of information sent by the game server for you to utilize in your scripts.

1\) Create a new script

2\) Copy and paste the following to the big white scripting box:

```
function getmsdpvars(event, args)
	for i = 1, 2 do tempTimer(i, [[send "\n"]]) end
 tempTimer(1, function () sendATCP("@REPORT", "SERVER_ID WORLD_TIME CHARACTER_NAME HEALTH HEALTH_MAX MANA MANA_MAX MOVEMENT MOVEMENT_MAX AREA_NAME ROOM_NAME ROOM_VNUM AC HONOR CONTINENT LEVEL CLASS DRACHMA ALIGNMENT EXPERIENCE MONEY STR CON DEX WIS INT STR_PERM CON_PERM DEX_PERM WIS_PERM WEAPON_DAM SPELL_BONUS_CAP HEAL_BONUS HEAL_BONUS_CAP CHARISMA CHARISMA_CAP FLAIL_DAM KICK_DAM HAND_DAM HAND_DAM_CAP DAM_RED DAM_RED_CAP SEX GROUP_LEADER TANK_HEALTH TANK_HEALTH_MAX TANK_LEVEL TANK_NAME LEVEL_SEC LEVEL_TER LEVEL_QUA LEVEL_QUI LEVEL_HEX LEVEL_SEP LEVEL_OCT LEVEL_AVA CITIZEN CLASS_SEC CLASS_TER CLASS_QUA CLASS_QUI CLASS_HEX CLASS_SEP CLASS_OCT CLASS_AVA STAB_DAM STAB_DAM_CAP UNDEAD_CONT UNDEAD_CONT_CAP SPELL_BONUS INT_PERM HITROLL DAMROLL OPPONENT_HEALTH OPPONENT_HEALTH_MAX OPPONENT_LEVEL OPPONENT_NAME TERRAIN") end)
--	tempTimer(2, function () cecho("<green><MSDP ACTIVATED><reset>") end)
end
```

3\) Click Save and be sure the script is enabled

You will now be able to request data from the server via the getmsdpvars() function!

Enjoy!

</div>

<div class="post" data-post-id="33910" data-author="Akaya" data-date="2013-01-10T09:11:58+00:00" data-subject="Fancy Gauges">

Need some fancy gauges for your UI?

![](http://oi45.tinypic.com/ehejcn.jpg)

Download Gauges.zip from here:

[https://sourceforge.net/projects/akayanui/files](https://sourceforge.net/projects/akayanui/files)

And install to your Mudlet profile using the Package Manager.

Then enter <strong>cg</strong> on your prompt line.

This script utilizes MSDP data and the Vyzor Framework.

Follow the instructions in the first two posts to get this working properly for you.

<strong>Keeps track of your health, mana, move, and mob health via colorful gauges. Also has a numerical display as the 'center piece'.</strong>

Enjoy!

</div>

<div class="post" data-post-id="33911" data-author="Akaya" data-date="2013-01-10T22:45:06+00:00" data-subject="Tabbed Chat Window">

This nifty script will redirect all your channels to a single window for you to sort through at your leisure.

![](http://i49.tinypic.com/122ygwk.png)

Download ChatWindow.zip from here:

http://sourceforge.net/projects/akayanui/files/

And install it on your Mudlet profile using the Package Manager

This script utilizes the Vyzor Framework so you'll want to follow the instructions on the very first post.

<strong>If you want to add/remove tabs, alter this line in the 'Create the UI' script included with the .xml file</strong>

![](http://i45.tinypic.com/34nfymt.png)

Enjoy!

</div>

<div class="post" data-post-id="33912" data-author="Akaya" data-date="2013-01-11T09:49:00+00:00" data-subject="Re: Akayan Scripts">

Here's a screencast of a UI in action.

Includes a chat window, gauges, a few clickable buttons, and the mudlet mapper widget (which I'm doing my best to set up for SlothMUD )

http://youtu.be/t2DjeKRhN74

</div>

<div class="post" data-post-id="33917" data-author="*Breeze*" data-date="2013-01-12T13:51:28+00:00" data-subject="Re: Akayan Scripts">

neat scripts <img src="/images/smilies/icon_e_smile.svg" alt=":)" title=":)" width="15" height="15" class="smiley nozoom">

thanks!

</div>

<div class="post" data-post-id="33918" data-author="Constin" data-date="2013-01-12T14:29:35+00:00" data-subject="Re: Akayan Scripts">

Does MSDP vars TANK\_HEALTH TANK\_HEALTH\_MAX TANK\_LEVEL TANK\_NAME exist? And how they used in game if yes?

</div>

<div class="post" data-post-id="33920" data-author="*Breeze*" data-date="2013-01-12T19:55:55+00:00" data-subject="Re: Akayan Scripts">

those are set if you are in a group and the tank uses the 'point' command.

</div>

<div class="post" data-post-id="33921" data-author="Akaya" data-date="2013-01-13T03:15:36+00:00" data-subject="Re: Akayan Scripts">

> <strong>Constin wrote:</strong>
> Does MSDP vars TANK\_HEALTH TANK\_HEALTH\_MAX TANK\_LEVEL TANK\_NAME exist?

<strong>YES!</strong>

> <strong>Constin wrote:</strong>
> And how they used in game if yes?

After following the instructions on post #2 of this topic, you'll have access to all MSDP information, including tank info.

MSDP is live. Meaning it updates automatically whenever the variables change.

To utilize this awesome feature, you'll want to create an [event handler](http://wiki.mudlet.org/w/Manual:Event_Engine).

When the MSDP information is sent to you, an event is raised that has the same name as the variable (In this case, MSDPTANK\_HEALTH, MSDPTANK\_HEALTH\_MAX, etc )

So you'll want to make a script that fires off of these variables. Here's an example:

![](http://oi49.tinypic.com/10eg41c.jpg)

When the MSDP variable, MSDPTANK\_HEALTH is updated, the function updateTank() is ran.

 <img src="/images/smilies/icon_exclaim.svg" alt=":!:" title=":!:" width="15" height="15" class="smiley nozoom"> Notice how the script name and function name match? This is very important!

The above script will display the following every time your tank's health changes:

<strong>TANK 75/100</strong>

Enjoy!

</div>

<div class="post" data-post-id="33922" data-author="Akaya" data-date="2013-01-13T07:22:25+00:00" data-subject="Re: Akayan Scripts">

Someone requested the following script, so here you are Someone.

This will remove all your EQ, place it in a defined container, pull another set of EQ from a defined container and wield/hold/wear the items.

The example contains <strong>two sets</strong> of default equipment which you can alter/add to. I included two example sets: AC and Stabbing

When you login, you'll want to let the system know which set you're currently wearing. Simply type: <strong>set eq \<set name\></strong>

You'll then want to set which container each EQ set belongs to. So type: <strong>set bag \<EQ set\> \<container\></strong>

To switch between equipment sets simply type: <strong>ex \<set name\></strong>

Due note that you'll need to set which EQ set your wearing and which containers they'll go into each time you re-open that profile in Mudlet.

 <img src="/images/smilies/icon_exclaim.svg" alt=":!:" title=":!:" width="15" height="15" class="smiley nozoom"> To add/alter equipment sets, create a new if statement, function and table in the format provided.

</div>

<div class="post" data-post-id="33923" data-author="*Breeze*" data-date="2013-01-13T09:05:53+00:00" data-subject="Re: Akayan Scripts">

tyvm. will try it

</div>

<div class="post" data-post-id="33924" data-author="Constin" data-date="2013-01-13T16:01:50+00:00" data-subject="Re: Akayan Scripts">

> <strong>Akaya wrote:</strong>
> To switch between equipment sets simply type: <strong>ex \<set name\></strong>
> 
> 
> 
> So to switch to the AC set you'd type: <strong>ex ac</strong>
> 
> 
> 
> To add/alter equipment sets, create a new if statement, function and table in the format provided. (If you need help in this area just ask. Should people like this script, I'll update it to have aliases for this)

You use bad algorithm. Ppl storing their eq in bags , or robes and using more then 2 mods. So u need:

 1\. rem all eq.

 2\. Then get EQ u need from container.

 3\. Wear Items u need.

 4\. put items from previos mode to containner. U cant put all items from inventory to container couse inventory may content some junk.

So. first of all u need to know previos mode , to know which items u need to put to container after exchange. Also u cant wear weapons and holding items. "wield dagger" "hold light" i mean u better test scripts before public it)

reliable way is to put all items from all modes exept mode u using to container in point 4. in this case u dont need to know previos mode.

\-------

Some good words about MSDP exchange script:

Thank you u all very match for this ability. Thank Splork and other coders for MSDP. Thank you Akaya for this script. Its greate abulity.

I can use this window and scripts w/o visior, am i right? Whoohoo!

</div>

<div class="post" data-post-id="33925" data-author="Akaya" data-date="2013-01-14T04:31:04+00:00" data-subject="Re: Akayan Scripts">

Updated the EQ Exchange script.

\- Fixed the problem with only being able to wear items and not wield or hold.

\- You can now set which containers you'd like to place your EQ in.

Remember that it still only includes two sets. If you want to have more, you'll need to wait for me to have the time or do it yourself. The script contains everything you need to add another set.

Enjoy!

</div>

<div class="post" data-post-id="33927" data-author="Akaya" data-date="2013-01-17T10:44:46+00:00" data-subject="Re: Akayan Scripts">

If you are using the latest version of Mudlet (2.1 is currently the latest) you will be able to run lua from the command prompt.

Simply type: 

<strong>lua \<whatever\></strong>

Whatever being the script you wish to run.

Enter this on the command prompt to display your profile's path on your computer:

<strong>lua cecho("\<yellow\>\\nProfile location: \<cyan\>"..getMudletHomeDir() )</strong>

If you receive msdp information (instructions on how to do this in post #2), you can enter this right from your prompt to display the msdp variable which holds your character's name (You can use this in an alias if you'd prefer to view it that way): 

<strong>lua display( atcp.MSDPCHARACTER\_NAME )</strong>

It's a very useful script that will save you hours of time in the long run.

Enjoy!

</div>

<div class="post" data-post-id="33932" data-author="Constin" data-date="2013-01-18T06:29:14+00:00" data-subject="Re: Akayan Scripts">

function getmsdpvars(event, args)

 for i = 1, 2 do tempTimer(i, [[send "\\n"]]) end

 tempTimer(1, function () sendATCP("@REPORT", "SERVER\_ID WORLD\_TIME CHARACTER\_NAME HEALTH HEALTH\_MAX MANA MANA\_MAX MOVEMENT MOVEMENT\_MAX AREA\_NAME ROOM\_NAME ROOM\_VNUM AC HONOR CONTINENT LEVEL CLASS DRACHMA ALIGNMENT EXPERIENCE MONEY STR CON DEX WIS INT STR\_PERM CON\_PERM DEX\_PERM WIS\_PERM WEAPON\_DAM SPELL\_BONUS\_CAP HEAL\_BONUS HEAL\_BONUS\_CAP CHARISMA CHARISMA\_CAP FLAIL\_DAM KICK\_DAM HAND\_DAM HAND\_DAM\_CAP DAM\_RED DAM\_RED\_CAP SEX GROUP\_LEADER TANK\_HEALTH TANK\_HEALTH\_MAX TANK\_LEVEL TANK\_NAME LEVEL\_SEC LEVEL\_TER LEVEL\_QUA LEVEL\_QUI LEVEL\_HEX LEVEL\_SEP LEVEL\_OCT LEVEL\_AVA CITIZEN CLASS\_SEC CLASS\_TER CLASS\_QUA CLASS\_QUI CLASS\_HEX CLASS\_SEP CLASS\_OCT CLASS\_AVA STAB\_DAM STAB\_DAM\_CAP UNDEAD\_CONT UNDEAD\_CONT\_CAP SPELL\_BONUS INT\_PERM HITROLL DAMROLL OPPONENT\_HEALTH OPPONENT\_HEALTH\_MAX OPPONENT\_LEVEL OPPONENT\_NAME TERRAIN") end)

\-- tempTimer(2, function () cecho("\<green\>\<MSDP ACTIVATED\>\<reset\>") end)

end

how to run this script at start? i need to start it manualy by using command getmsdpvars() every time im loging in

</div>

<div class="post" data-post-id="33933" data-author="Akaya" data-date="2013-01-18T21:07:07+00:00" data-subject="Re: Akayan Scripts">

MSDPSERVER\_ID is raised each time you log in. So you can create an event handler to run getmsdpvars() when you do. It would look like this:

![](http://oi49.tinypic.com/2i2371j.jpg)

Enjoy!

</div>

<div class="post" data-post-id="34053" data-author="Tuck" data-date="2013-02-19T23:13:30+00:00" data-subject="Re: Akayan Scripts">

Did you get TANK\_NAME, TANK\_HEALTH and other TANK related vars to work?

Thanks for your answer.

</div>

<div class="post" data-post-id="34118" data-author="Akaya" data-date="2013-03-03T19:00:30+00:00" data-subject="Re: Akayan Scripts">

> <strong>Tuck wrote:</strong>
> Did you get TANK\_NAME, TANK\_HEALTH and other TANK related vars to work?

Yes. Your tank's name, level, current and max health are all listed in your MSDP table.

MSDPTANK\_NAME

MSDPTANK\_LEVEL

MSDPTANK\_HEALTH

MSDPTANK\_HEALTH\_MAX

<strong>If a tank is not yet set, then the value will be nil.</strong>

Here are a few examples of what you can do with these values:

<em>This will simply display the value given in parenthesis</em>

```
display(atcp.MSDPTANK_NAME)
```

This will give it some color like so: Tank's HP: 1234/5000

```
cecho("\n<yellow>Tank's HP: <cyan>"..atcp.MSDPTANK_HEALTH.."<yellow>/"..atcp.MSDPTANK_HEALTH_MAX)
```

For Vyzor users, the following will send your tank information to a Frame.

<em>Tank\_Name(level): health/max</em>

```
Frame_Name:Echo(atcp.MSDPTANK_NAME.."("..atcp.MSDPTANK_LEVEL.."): "..atcp.MSDPTANK_HEALTH.."/"..atcp.MSDPTANK_HEALTH_MAX)
```

For Geyser users, the following will send your tank information to a label.

<em>Tank\_Name(level): health/max</em>

```
echo("label_name", atcp.MSDPTANK_NAME.."("..atcp.MSDPTANK_LEVEL.."): "..atcp.MSDPTANK_HEALTH.."/"..atcp.MSDPTANK_HEALTH_MAX)
```

Enjoy!

</div>

<div class="post" data-post-id="34197" data-author="Akaya" data-date="2013-03-28T03:53:21+00:00" data-subject="Akayan GUI Creator">

I'd like to invite the Sloth community to try out the new Akayan GUI Creator.

It's a script written with the Vyzor Framework on Mudlet. It allows you to create visually eye-popping GUIs with little to no coding involved. And it works with any MUD!

It's still in beta and many features are still being added but if you'd like to try it out or follow along, check out my YouTube channel: [http://www.youtube.com/channel/UC_ZY59zJZLHypwk8Vvib2Mw](http://www.youtube.com/channel/UC_ZY59zJZLHypwk8Vvib2Mw)

Here's a few videos from the channel so you can get an idea of what's in store:

[http://youtu.be/QLWJeuJuWeE](http://youtu.be/QLWJeuJuWeE)

[http://youtu.be/uAs2pIdOU4U](http://youtu.be/uAs2pIdOU4U)

The actual GUI Creator itself along with some other useful information can be found here: 

[http://forums.mudlet.org/viewtopic.php?f=6&t=3329#p16363](http://forums.mudlet.org/viewtopic.php?f=6&t=3329#p16363)

Enjoy!

</div>

<div class="post" data-post-id="34238" data-author="Jecka" data-date="2013-04-16T07:13:01+00:00" data-subject="Re: Akayan Scripts">

> <strong>Akaya wrote:</strong>
> I'm happy to answer any questions you have and/or walk you through the installation process. Enjoy!

Sorry Akaya <img src="/images/smilies/icon_e_smile.svg" alt=":)" title=":)" width="15" height="15" class="smiley nozoom"> 

I did my best at mudlet with your scripts for Slothmud but the only thing i got was 

"Vyzor: Loading modules..."

"Vyzor: Loading modules..."

and after i printed U

"Vyzor: Unloading modules..."

"Vyzor: Unloaded all modules."

any advice please <img src="/images/smilies/icon_e_smile.svg" alt=":)" title=":)" width="15" height="15" class="smiley nozoom">

</div>

<div class="post" data-post-id="34245" data-author="Akaya" data-date="2013-04-19T03:57:03+00:00" data-subject="Re: Akayan Scripts">

I'm guessing you installed vyzor.xml instead of vyzor.mpackage

Here's a video I made a little while back that shows you exactly how to install Vyzor properly. The last part of the video tells you to change a line in the code. DONT DO IT because the latest version of Vyzor does it for you.

[http://youtu.be/SAQ2SumHfRw](http://youtu.be/SAQ2SumHfRw)

If your problems persist, I'm more than willing to walk you through the process and make certain that your GUI is working as you'd expect.

</div>

<div class="post" data-post-id="34249" data-author="Jecka" data-date="2013-04-20T09:28:33+00:00" data-subject="Re: Akayan Scripts">

> <strong>Akaya wrote:</strong>
> I'm guessing you installed vyzor.xml instead of vyzor.mpackage

You were absolutely right.

But nevertheless after installing vyzor.mpackage I still can't figure out how you nice-looking scripts can be installed <img src="/images/smilies/icon_e_sad.svg" alt=":(" title=":(" width="15" height="15" class="smiley nozoom">

So please post some more additionel help <img src="/images/smilies/icon_e_smile.svg" alt=":)" title=":)" width="15" height="15" class="smiley nozoom">

</div>

<div class="post" data-post-id="34250" data-author="Akaya" data-date="2013-04-20T17:37:41+00:00" data-subject="Re: Akayan Scripts">

Each of my scripts come in a .zip file.

What you'll want to do is download this zip and DO NOT EXTRACT OR UNZIP.

Now install the .zip file on profile that has Vyzor and vuala! Your GUI should appear.

If you'd like, send me a PM on this forum and we'll set up a date/time where I can set it up for you.

</div>

<div class="post" data-post-id="34251" data-author="Jecka" data-date="2013-04-21T07:04:00+00:00" data-subject="Re: Akayan Scripts">

> <strong>Akaya wrote:</strong>
> Each of my scripts come in a .zip file.
> 
> 
> 
> What you'll want to do is download this zip and DO NOT EXTRACT OR UNZIP.
> 
> 
> 
> Now install the .zip file on profile that has Vyzor and vuala! Your GUI should appear.
> 
> 
> 
> If you'd like, send me a PM on this forum and we'll set up a date/time where I can set it up for you.

I got some improvements but still not all of them <img src="/images/smilies/icon_e_sad.svg" alt=":(" title=":(" width="15" height="15" class="smiley nozoom">

</div>

<div class="post" data-post-id="34287" data-author="Akaya" data-date="2013-05-10T19:29:30+00:00" data-subject="Mudlet Gameboys!">

For those that struggle to make the switch between Vyzor and Geyser, if you just want some great examples of how they differ from each other, or just need something to kill time while you wait/sleep in-game, I've created some Mudlet Gameboys for you to play with. Each comes with a default pong game.

The Geyser Gameboy is ready-to-play. Simply download, install and you're good to go.

The Vyzor Gameboy however will require the latest version of Vyzor. You can find a link to this in the first post of this topic.

You can pick up a copy of each Gameboy here:http://forums.mudlet.org/viewtopic.php?f=6&t=2984&start=20#p16781

Enjoy!

</div>

<div class="post" data-post-id="34298" data-author="Akaya" data-date="2013-05-17T18:42:35+00:00" data-subject="Re: Akayan Scripts">

Someone requested that I post a few screenshots of GUI work I've done in the past so I figured I'd share the link to my website. It's incomplete at the moment, but I plan on fleshing it out in the near future...

[http://guitararms420.wix.com/akayangui](http://guitararms420.wix.com/akayangui)

and my YouTube channel always has the latest projects I'm working on...

[http://www.youtube.com/user/rurik69](http://www.youtube.com/user/rurik69)

</div>

<div class="post" data-post-id="34441" data-author="Akaya" data-date="2013-09-17T02:50:50+00:00" data-subject="Re: Akayan Scripts">

Here's an example of how to make a visual cooldown timer. I didn't write this but someone in the Sloth community found it useful so I figured I'd repost it here.

First, download the following script:

[http://forums.mudlet.org/download/file.php?id=853](http://forums.mudlet.org/download/file.php?id=853)

Now you can enter the following from the command line to create a new cooldown timer:

lua demonnic.anitimer:new("Test1", {x=200, y=100, height = 30, width = 300, color="red"}, 5)

Usage:

demonnic.anitimer:new(name, constructor, time, container, showTime, css, cssback)

name: any name you wish to give the timer in string format

constructor: The same constructor you would pass to Geyser.Gauge:new(). This is where you specify your coordinates, height, width, etc.

time: How long in seconds you want the cooldown to run. Accepts decimal values

container: Optional argument. Give the timer a Geyser container to bind to. If you don't wish to bind to a container, but do wish to set up a stylesheet or turn off the display of the timeleft, then pass the empty string for this argument.

showTime: Optional argument, except if you want to pass further arguments. I may try to restructure this soon. This determines whether or not the time remaining is shown on the timer. Defaults to true if you

css: Optional argument. The stylesheet to apply to the front portion of the gauge.

cssback: Optional argument. The stylesheet to apply to the back portion of the gauge.

</div>

<div class="post" data-post-id="34648" data-author="Akaya" data-date="2013-12-17T18:12:24+00:00" data-subject="Exit Parser for Linux">

Here's a function I wrote with Ubuntu that will return a table of exits in your current room by parsing MSDPROOM\_EXITS. Not sure if this works with other operating systems because of the weird characters that separate the exit names, but if you're not on Linux, still give it a whirl, lemme know what happens:

```
function parseExits()
 exits = {}
 str = atcp.MSDPROOM_EXITS
 dirs = {"North","East","South","West","Up","Down"}
 for i=1,string.len(str) do
 if string.ends(str,"") or string.ends(str,"O") or string.ends(str,"") or string.ends(str,"") or string.ends(str,"") then
 str = string.cut(str,string.len(str)-1)
 else
 for k,v in pairs(dirs) do
 if string.ends(str,v) then
 str = string.cut(str,string.len(str)-string.len(v))
 table.insert(exits,v)
 end
 end
 end
 end
 return exits
end
```

To use this script, simply call parseExits() each time you enter a room or when MSDPROOM\_VNUM updates. Let's say I'm in a room with exits west, north and south. <strong>parseExits()</strong> would return:

```
{
 "West",
 "North",
 "South"
}
```

Let's say you want to move in the first direction parseExits gives you:

```
send(parseExits()[1])
```

That would move you west.

Enjoy!

</div>

<div class="post" data-post-id="34649" data-author="Akaya" data-date="2013-12-17T18:19:28+00:00" data-subject="Re: Akayan Scripts">

Unfortunately, the forum doesn't want to post the 'weird characters' which is the reason for the above script. So if you're still looking to parse the exits, you'll want to manually insert the 'weird characters' you see in MSDPROOM\_EXITS to <strong>string.ends(str,"weird\_character")</strong> of the above script.

</div>

<div class="post" data-post-id="34650" data-author="DarkArtist" data-date="2013-12-17T22:13:43+00:00" data-subject="Re: Akayan Scripts">

I admit to being a newb, but I couldn't understand what weird chars you meant at first cuz I couldn't even get MSDPROOM\_EXITS to give me anything, until I realized it was absent from getmsdpvars() that I got from you. So fyi other newbs, don't forget to add it to the list if its not there.

I found the character codes for those weird symbols under Terminal fonts, but how do I enter them into mudlet? When I paste them in from the character map they come out as foreign letters and upside down question mark.

I wrote down the character codes if I can do it that way somehow?

What I've got now for exits is a trigger off the pattern ^Exits:(\\s+)(.\*)(\\s)(\\s)(\\s)$

exitsString=matches[3]

exits={}

exits=exitsString:split(" ") -------(two spaces in the delimiter)

\--display(exits)

I'm guessing msdproom\_exits give you all the exits, whether u can see them or not? If so, I guess it'd be better to switch, but triggering off the exits output has the advantage that you can could capture the brackets and make a table of closed/open status for each valid exit. 

Thanks again for posting all this stuff. 

btw, it seems the board duplicates your post when u change title, i hope i responded correctly.

</div>

<div class="post" data-post-id="34651" data-author="Akaya" data-date="2013-12-18T07:12:41+00:00" data-subject="Re: Akayan Scripts">

The characters seem to vary depending on the OS. To use the characters in a script, you'll want to display MSDPROOM\_EXITS via Mudlet and copy/paste them into your Mudlet script. They will come out as 'forgein letters' but at least Mudlet keeps them consistent within itself.

As for capturing exits via triggers: That's always a viable option and I'm sure this is how many Slothers have been capturing exits regardless of their client. MSDP still offers exits though, and having a reliable way to parse the information, if one should choose to use it, should be there.

</div>

<div class="post" data-post-id="34652" data-author="*Breeze*" data-date="2013-12-18T07:27:27+00:00" data-subject="Re: Akayan Scripts">

could also ask the benevolent Splork to change the output to something nicer?

also, can mudlet parse JSON and put into a database that it can look up stuff from?

</div>

<div class="post" data-post-id="34653" data-author="Akaya" data-date="2013-12-18T17:00:53+00:00" data-subject="Re: Akayan Scripts">

> <strong>\*Breeze\* wrote:</strong>
> also, can mudlet parse JSON and put into a database that it can look up stuff from?

Yes! Just use yajl.to\_string and yajl.to\_value: [http://wiki.mudlet.org/w/Manual:Miscellaneous_Functions#yajl.to_string](http://wiki.mudlet.org/w/Manual:Miscellaneous_Functions#yajl.to_string)

</div>

<div class="post" data-post-id="34654" data-author="*Breeze*" data-date="2013-12-18T17:35:12+00:00" data-subject="Re: Akayan Scripts">

sweet. i let someone else who has time try to deal with it then, if they have the time/desire.

only thing i ask is if someone figures out how to use it with mudlet/wintin/whatever they share so others can use it.

this is not a permanent link. its only there for a few days. it has probably 99% of the eqlist, minus a few things like vault keys and anything with the keyword template in it, etc.

save as [eqlist.json](http://www.slothmud.org/eqlist.json)

</div>

<div class="post" data-post-id="34655" data-author="Akaya" data-date="2013-12-18T18:44:04+00:00" data-subject="Re: Akayan Scripts">

ooo. That's neat. It's a massive string though. I was able to take small sections of it and convert it to a lua table:

```
myData = [[{"Generated":"Wed, 18 Dec 2013 10:29:19 -0700","4":{"OBJECT_VNUM":"4","OBJECT_NAME":"hexagonal hex token","OBJECT_SHORT_DESCRIPTION":"a hexagonal shaped token","OBJECT_TYPE":"LIGHT","VALUE_COLOUR":"0","VALUE_LIGHT_TYPE":"0","VALUE_HOURS":"-1","OBJECT_WEAR":"TAKE HOLD","OBJECT_EXTRA_FLAGS":"MAGIC","OBJECT_WEIGHT":"1","OBJECT_VALUE":"100000","OBJECT_RENT":"5500"}}]]
myTable = yajl.to_value(myData)
display(myTable)
```

But only as much as Mudlet could handle as I'm in the scripting window. Here's the result for the first few lines using the above snippet:

```
{
 Generated = "Wed, 18 Dec 2013 10:29:19 -0700",
 ["4"] = {
 OBJECT_WEIGHT = "1",
 OBJECT_VNUM = "4",
 OBJECT_NAME = "hexagonal hex token",
 VALUE_LIGHT_TYPE = "0",
 OBJECT_VALUE = "100000",
 VALUE_HOURS = "-1",
 OBJECT_WEAR = "TAKE HOLD",
 OBJECT_EXTRA_FLAGS = "MAGIC",
 OBJECT_TYPE = "LIGHT",
 OBJECT_RENT = "5500",
 VALUE_COLOUR = "0",
 OBJECT_SHORT_DESCRIPTION = "a hexagonal shaped token"
 }
}
```

Meaning you can refer to this object's short description in a lua script with 

```
myTable["4"].OBJECT_SHORT_DESCRIPTION
```

If you manage to parse all that JSON data this would be a great scriptable database for eq!

This might be possible with [Mudlet's Database Functions](http://wiki.mudlet.org/w/Manual:Database_Functions#Database_Functions) but last I heard it was unfinished/buggy.

</div>

<div class="post" data-post-id="34656" data-author="*Breeze*" data-date="2013-12-18T19:10:08+00:00" data-subject="Re: Akayan Scripts">

yeah, it was meant to be used for that purpose exactly.

in php you can do

```
<?php

$eqArray = json_decode(file_get_contents('eqlist.json'),true);

echo '<pre>';print_r($eqArray);die('</pre>');

?>
```

or even build your own raw interface/search.

everything is cross referenced so its just a matter of searching / displaying it.

splitting that file into other stuff would be trivial, but i decided to just output the information and let others deal with it, since there is no way i can make everyone happy. it easier to just make \_me\_ happy.

you can do something like this to separate each item into its own line separated by \\n

```
<?php

 $eqArray = json_decode(file_get_contents('eqlist.json'),true);

 $eqBuffer = '';
 foreach ($eqArray as $eqK=>$eqV)
 {
 $eqBuffer .= json_encode($eqV)."\n";
 unset($eqArray[$eqK]);
 }

 die($eqBuffer);

?>
```

or a few other simple variations thereof to sort by OBJECT\_TYPE or anything else.

</div>

<div class="post" data-post-id="34670" data-author="Akaya" data-date="2013-12-21T15:45:49+00:00" data-subject="Re: Akayan Scripts">

Need to capture your group info to a miniConsole? Here's a nice start...
Group Capture.xml.xml
Just change myConsole to the name of your miniConsole.

</div>

<div class="post" data-post-id="34706" data-author="Akaya" data-date="2013-12-28T20:50:10+00:00" data-subject="Re: Akayan Scripts">

Here's a nice compass that will display not only room exits, but whether its an open/closed door or window:

[http://youtu.be/zq9Outs5QL4](http://youtu.be/zq9Outs5QL4)

![](http://i.imgur.com/cJpTFm9.png)
SlothCompass.xml
Enjoy!

</div>

<div class="post" data-post-id="34748" data-author="Akaya" data-date="2014-01-02T06:59:48+00:00" data-subject="Re: Akayan Scripts">

Here's a script that will automatically set your target to whatever the group leader calls (and only what the group leader calls). You can also manually set the target by typing <strong>t \<whatever\></strong>. If you want to use your target in a macro, you can do so: 

```
send("backstab "..target)
```

Group Target.xml.xml

Enjoy!

</div>

<div class="post" data-post-id="34767" data-author="Akaya" data-date="2014-01-07T19:20:18+00:00" data-subject="Scan">

This script captures all information via the SCAN command. It is placed in a lua table named Scan. The table is updated when you SCAN.

To attack your target if it is 'immediately to the north':

```
if Scan[target]["immediately to the north"] then
 send("north")
 send("backstab "..target)
end
```

Akayan Scanner.xml

Enjoy!

</div>

<div class="post" data-post-id="34792" data-author="Akaya" data-date="2014-01-14T22:26:25+00:00" data-subject="Re: Akayan Scripts">

Toyed around with Mudlet's new database functions and was able to parse the eqlist json file to produce this nice UI that displays my current eq:

![](http://i.imgur.com/6FFbG5T.png)

I'm still messing around with the parsing function though so I don't have a usable script atm. Just a snapshot. <img src="/images/smilies/icon_e_smile.svg" alt=":)" title=":)" width="15" height="15" class="smiley nozoom">

</div>

<div class="post" data-post-id="34793" data-author="*Splork*" data-date="2014-01-14T22:45:56+00:00" data-subject="Re: Akayan Scripts">

That is awesome!

</div>

<div class="post" data-post-id="34803" data-author="Akaya" data-date="2014-01-17T22:25:07+00:00" data-subject="Re: Akayan Scripts">

I present to you the eqlist database for Mudlet users!

![](http://i.imgur.com/rdb2nDQ.png)

Simply type <strong>lookup \<item\></strong> and it will update itself with all the info you'll find on the eqlist website.

It includes an eqlist.lua file with all the info from the eqlist database along with all the functions you need to query. So if you're up for scripting, it has everything you need.

You can type the following on the command line to display every piece of armor in the database:

```
getType("ARMOR")
```

This was a very daunting task to create. Lots of effort went into it. Thank you Splork and Breeze for all the help!

Enjoy!

The file is too big for this forum apparently so here's a direct download link via dropbox...

[https://dl-web.dropbox.com/get/Public/EQLIST_QUERY.zip?_subject_uid=154460497&w=AACYjTqOEq4HRqqea2H5OtwqHYCEWTnoIB0qjIx38qeu4w&dl=1](https://dl-web.dropbox.com/get/Public/EQLIST_QUERY.zip?_subject_uid=154460497&w=AACYjTqOEq4HRqqea2H5OtwqHYCEWTnoIB0qjIx38qeu4w&dl=1)

<em>Install Using the Package Manager!</em>

</div>

<div class="post" data-post-id="34804" data-author="Akaya" data-date="2014-01-18T00:34:13+00:00" data-subject="Re: Akayan Scripts">

made a small update to how the database was queried. Wasn't capturing all the info. Is now. Link updated in previous post.

</div>

<div class="post" data-post-id="34822" data-author="Akaya" data-date="2014-01-24T18:25:19+00:00" data-subject="Simple Gauges">

Here are some simple gauges to keep track of your health, mana, movement and mob health.

They sit at the bottom of your screen by default.

You can alter its size and position in Scripts\>Create the monster on lines 5,6 and 7

They use the Geyser framework. So just install using the package manager and you're all set!

Don't forget to make sure you're utilizing msdp variables! You can find how to do so here: [http://www.slothmud.org/forum/viewtopic.php?f=39&t=4002#p33909](http://www.slothmud.org/forum/viewtopic.php?f=39&t=4002#p33909)

Enjoy!

</div>

<div class="post" data-post-id="36230" data-author="Arus" data-date="2015-12-01T17:04:57+00:00" data-subject="Re: Akayan Scripts">

could you please re-upload your database scripts?

Here is my implementation of EQList searcher in mudlet: EQList.zip
It uses unmodified json file downloaded from website and saved in mudlet home directory.

There are two triggers to set links in equipment and merchant windows which you can click get query results in the same window. There is also alias "eq \<item\>" for same purpose. See example: EQList.png

</div>

<div class="post" data-post-id="36232" data-author="*Breeze*" data-date="2015-12-02T00:08:32+00:00" data-subject="Re: Akayan Scripts">

Db script?

</div>

<div class="post" data-post-id="36243" data-author="Arus" data-date="2015-12-04T04:54:47+00:00" data-subject="Re: Akayan Scripts">

Yes, Akaya's dropbox link went dead. Could you please repost?

I am thinking of writing a Mudlet mapper that uses all of the information available from COORD1-25 (exits, terrain, mobs, player characters). Eventually I want to track the movement of MOBs in the neighborhood and match them to POPPERS in EQList database. But in order to do that first I need AREA\_VNUM in REPORTED\_VARIABLES and MOB\_VNUM replacing MOB in COORD1-25. Thanks

What's the deal with ROOM\_RNUM being always lower than ROOM\_VNUM by 22856? As far as I understand, ROOM\_RNUM starts with AREA\_INFO like 113 "Newbatia"+44 "South Gate". But why do we need ROOM\_VNUM? Why do you have two room identifiers?

Akaya, where are you? Have you stopped developing for SlothMUD?

</div>

<div class="post" data-post-id="36246" data-author="*Breeze*" data-date="2015-12-04T05:16:30+00:00" data-subject="Re: Akayan Scripts">

[http://www.slothmud.org/mudlet/](http://www.slothmud.org/mudlet/)

</div>

<div class="post" data-post-id="36248" data-author="Arus" data-date="2015-12-04T09:31:57+00:00" data-subject="Re: Akayan Scripts">

why did all the COORDS become empty? <img src="/images/smilies/icon_rolleyes.svg" alt=":roll:" title=":roll:" width="15" height="15" class="smiley nozoom"> bug? was working fine 10 minutes ago.

</div>

<div class="post" data-post-id="36250" data-author="*Splork*" data-date="2015-12-04T16:37:52+00:00" data-subject="Re: Akayan Scripts">

I thought I disabled COORD1-25 a long time ago due to performance issues...

</div>

<div class="post" data-post-id="36251" data-author="Arus" data-date="2015-12-04T17:11:40+00:00" data-subject="Re: Akayan Scripts">

If you didn't notice, then there was no performance issue. I almost finished the code....

I was not going to report COORDS on every move but send them only in new rooms as discovery to build a map.

</div>

<div class="post" data-post-id="36971" data-author="Akaya" data-date="2016-06-23T05:46:05+00:00" data-subject="Re: Akayan Scripts">

Dropbox link for the eq db is alive now. I'll try to find a better way to keep it that way.

</div>

<div class="post" data-post-id="36972" data-author="Akaya" data-date="2016-06-23T06:04:39+00:00" data-subject="Re: Akayan Scripts">

> <strong>Arus wrote:</strong>
> If you didn't notice, then there was no performance issue. I almost finished the code....
> 
> I was not going to report COORDS on every move but send them only in new rooms as discovery to build a map.

This was one of the last projects I was working on, I believe... A 5x5 map that displayed everything from terrain to who was in which room. It did work (very beautifully) but the handshake was heavy.

I did, however, write a mapping script for use with Mudlet's native mapper. Hence the need for the VNUMS. It's tailored for use with SlothMud. I remember mapping many of the main areas with ease. I think I was able to do 20+ areas in a few hours. You can speedwalk to rooms by double clicking them, zoom in/out to view a single room or thousands, along with a plethora of other options. You can find the scrilpt on the Mudlet forum. The mapper is installed by default on every new Mudlet profile.

</div>

<div class="post" data-post-id="37003" data-author="Akaya" data-date="2016-06-29T18:01:08+00:00" data-subject="Group Triggers">

Probably the #1 request I receive is for group triggers. So here they are. Props to Taron for writing this post: [http://www.slothmud.org/forum/viewtopic.php?f=28&t=4642](http://www.slothmud.org/forum/viewtopic.php?f=28&t=4642) I've based this script off of his wisdom.

There is a script called 'config'. Change the values within to have this work for you. For example...

```
yourName = "Akaya"
leader = "Taron"
tank = "War"
```

This would set my name to Akaya so the triggers only work for me and my leader and tank to Taron and War so I only do what they tell me (no imposters!)

IF YOU DO NOT CHANGE THE VALUES IN THE CONFIG SCRIPT THIS WILL NOT WORK!

Group Triggers by Akaya.trigger.xml

</div>

<div class="post" data-post-id="37006" data-author="Teron" data-date="2016-06-29T19:59:37+00:00" data-subject="Re: Akayan Scripts">

So, if I were to create an alias to specify a tank or a leader, what would it look like?

Thanks.

</div>

<div class="post" data-post-id="37008" data-author="Akaya" data-date="2016-06-29T20:09:09+00:00" data-subject="Re: Akayan Scripts">

Pattern: ^leader (.\*)$

Script: leader = matches[2]

</div>

<div class="post" data-post-id="37009" data-author="*Splork*" data-date="2016-06-30T01:12:47+00:00" data-subject="Re: Akayan Scripts">

Missed you Akaya!

</div>

<div class="post" data-post-id="37015" data-author="Akaya" data-date="2016-06-30T17:03:39+00:00" data-subject="Re: Akayan Scripts">

> <strong>\*Splork\* wrote:</strong>
> Missed you Akaya!

I'll be around all summer. Hopefully longer. Sent you an email from my new address. Contact me that way. It goes straight to my phone.

</div>
