---
title: "ATCP Questions"
topic_id: 3996
author: "dracmas"
date: 2013-01-04T10:03:48+00:00
last_activity: 2013-01-08T04:57:02+00:00
last_author: "dracmas"
sticky: false
locked: false
post_count: 10
---

<div class="post" data-post-id="33887" data-author="dracmas" data-date="2013-01-04T10:03:48+00:00">

I've fleshed out the plugin Im making for Mudlet and I'm almost certain that atcp is being sent to the client AFTER the prompt is sent. If this is the case, data is always going to be trailing behind. health/mana/moves will be off during fights as well as in movement. While traveling around it will show you the previous room you were in while moving on to the next.

The MSDP variables for enemy name/health aren't showing up maybe not updating. Doesn't show when I do a report in Mudlet for them (all declared for msdp mind you). msdp FLAIL_DAM / msdp KICK_DAM didnt show up when I tried them out either. 

Also, if you have any ideas I could add to this plugin I'd be happy to look into it. So far it looks like this.

[![](http://i.troll.ws/1876f5e2.png)](http://i.troll.ws/1876f5e2.png)

</div>

<div class="post" data-post-id="33888" data-author="*Breeze*" data-date="2013-01-04T11:10:18+00:00">

pretty plugin

as for your questions ::

mob health/name arent sent at the moment. splork is working on them.

current status is sent actually rather often.

mxp is sent with the prompt/once every 4 seconds or so.

iirc msdp is sent every second.  

rick should be back in awhile and he can probably give you a better answer.

--Breeze

</div>

<div class="post" data-post-id="33889" data-author="dracmas" data-date="2013-01-04T12:09:15+00:00">

At least from what I've gathered, I can't update the msdp without a triggered event.

The prompt being the only thing that updates fast enough to keep up with all the current data that is what I  trigger for to update msdp. I'd be greatful to know if there was an easier way.  So thats how I came to the conclusion thinking that atcp was being sent after the strings for the prompt.  Otherwise Im not quite sure what to trigger off of to keep everything current.

Yeah, definitely took awhile to get the gui to look like that. Was bugging Vadi and others for help but I dont think they minded since I was trying my best to figure it all out. I'll be  combining these later in into tabbed windows when I learn more, but this is all Ive got for now. Project  goals from here are to consolidate the labels into a tabbed box, figure out the mapper, MSP for areas,fix a chat box into the layout, and   a gui system with health bars that appear when you're fighting and disappear out of your way once the battle is over. Then  somewhere in there figure out a good skin.

I'll post version two tonight. so  you all can play with it.

</div>

<div class="post" data-post-id="33890" data-author="*Breeze*" data-date="2013-01-04T13:17:19+00:00">

you cant trigger off of prompt. you have to trigger off of something else

or a loop of some sort that runs every 2 seconds or so.

</div>

<div class="post" data-post-id="33891" data-author="dracmas" data-date="2013-01-04T14:24:06+00:00">

I asked for help fixing it. Im just not sure how to call for it.

In the meantime, Here's the script if you want to see it.

</div>

<div class="post" data-post-id="33892" data-author="*Breeze*" data-date="2013-01-04T16:14:33+00:00">

how do you use it?

i load it, reconnect and it still looks the same, except i see your msdp enabled message

</div>

<div class="post" data-post-id="33893" data-author="dracmas" data-date="2013-01-05T01:27:40+00:00">

Ripped out the prompt, updating to work off of events instead of prompt/timers. Now it's just WHEN to call for MSDP. Mine has no specifications yet, so It asks for it right when you try to log in. Then after you're in the game it keeps requesting, so I need to have a conditional statement to stop requesting variables as well.

[http://www.mudbytes.net/topic-4105-63887#p63887](http://www.mudbytes.net/topic-4105-63887#p63887)

</div>

<div class="post" data-post-id="33894" data-author="dracmas" data-date="2013-01-05T06:03:29+00:00">

I'd be ripping out my hair if I had any. 

The handler for MSDPSERVER_ID isn't triggering

any scripts. Its triggering nothing at all. Really not 

sure where to go from here. I know this can be done from within

the scripting, so I really don't want to have to add a trigger if I don't have

to to get t the ball rolling.

</div>

<div class="post" data-post-id="33895" data-author="dracmas" data-date="2013-01-06T00:13:43+00:00">

A few fixes to the gui plugin. 

*Pointed labels to their correct container.

*Spelling error.

*wasn't seeing scrollbar for main window. fixed.

*triggered off of MSDP now instead of prompt.

*ripped out my MSDP echo prompt. Not necessary.

</div>

<div class="post" data-post-id="33900" data-author="dracmas" data-date="2013-01-08T04:57:02+00:00">

My last post on this. I complained about no comments in someone elses script when I didn't say anything within my own. I've started working on more graphical guis but didn't feel like this was complete until I commented on what I've done so you can see what's happening.

Server_ID and initialise_msdp I can't say much about, because all it does is tell the mud to report to you which msdp variables you want sent to you're client. Then it's up to you as to how to display it. Note that the variables in initialise_msdp aren't the complete set of variables this mud has, so add the new ones as you need them the same way the rest are written. 

> **Quote:**
> I know this is a bad way to do a layout. You should REALLY not update a whole gui every time an event is triggered. More advanced I would assign functions
> 
> to various sections to update variables without redoing everything, but this is a learning environment and everyone has to start everywhere. I've commened everything below. I may not know exactly what Im doing half the time, or might comment wrong. Lemme know if this is the case. But! At least you will see what's going through my head while doing this.
> 
> 
> 
> -- where I start my layout. It gets called everytime the MSDP variables change. If you were to see the Handler Variables from the gui editor you would see all the MSDP variables tacked on to this script. What I could do better is to add more functions to change how variables are updated to the layout, put handler MSDP just for those functions, and stop redrawing the layout every time something happens.
> 
> 
> 
> function layout()
> 
> 
> 
> -- Setting my boarders for the left side of the main window.
> 
> setBorderLeft(210)
> 
> 
> 
> -- this is where I name the containers of the screen where I will put labels with my info. The labels are the boxes you see with the stats in it. The container once again is the location of the screen where the labels will be placed. I then named one of the container as left_container so I can call it specifically when adding labels to place content on the screen. The variables are location of x/y positioning of where the container starts at, the width of how wide I want my container to be, and I made the Hight 100% so it covers the whole hight area of the left side where I specified how wide it would be.
> 
> 
> 
> left_container = Geyser.Container:new({
> 
>   name = "left_container",    -- give it a unique name here
> 
>   x=0, y=0,                   -- have it start at the top-left corner of mudlet
> 
>   width = 200, height="100%", -- with a width of 200, and a height of the full screen, hence 100%
> 
> })
> 
> 
> 
> setBorderRight(210)
> 
> right_container = Geyser.Container:new({
> 
>   name = "right_container",    -- give it a unique name here
> 
>   x=0, y=0,                   -- have it start at the top-left corner of mudlet
> 
>   width = 200, height="100%", -- with a width of 200, and a height of the full screen, hence 100%
> 
> })
> 
> 
> 
> setBorderTop(100)
> 
> top_container = Geyser.Container:new({
> 
>   name = "top_container",    -- give it a unique name here
> 
>   x=0, y=0,                   -- have it start at the top-left corner of mudlet
> 
>   width ="100%", height= 100, -- with a width of 200, and a height of the full screen, hence 100%
> 
> })
> 
> 
> 
> setBorderBottom(100)
> 
> bottom_container = Geyser.Container:new({
> 
>   name = "bottom_container",    -- give it a unique name here
> 
>   x=0, y=0,                   -- have it start at the top-left corner of mudlet
> 
>   width = "100%", height= 100, -- with a width of 200, and a height of the full screen, hence 100%
> 
> })
> 
> 
> 
> -- Here I made a new label for the boarder for sloth. You can see it references top_container as the area it's to be placed within. width/height end up showing the percentage of how much I'm filling the container, instead of the whole screen, since top_container is the parent area of where the label is placed. X/y is placement from within the container area. Values can place this outside of the container, but It can be helpful for other reasons, such as moving a whole container somewhere else on the screen. The stylesheet gives me the fancy oval like boarders/width/font ect. It makes it look better overall. The same can be said with the other labels. Not hard to do once you get it down. It just takes some playing with to get the values right for positioning and how you want the look and feel to be.
> 
> 
> 
> Top_Border = Geyser.Label:new({
> 
>   name = "Top_Border",
> 
>   x = "15%", y = "0%",
> 
>   width = "70%", height = "95%",
> 
>   message = [[<center><font size=40>SLOTHMUD - A RETURN TO ITS ORIGINS</font></center>]]
> 
> }, top_container)
> 
> Top_Border:setStyleSheet([[
> 
>   background-color: black;
> 
>   border-width: 2px;
> 
>   border-style: solid;
> 
>   border-color: grey;
> 
>   border-radius: 10px;
> 
>   font: bold "Monospace";
> 
>   font-size: 14px;
> 
> ]])
> 
> 
> 
> Locations = Geyser.Label:new({
> 
>   name = "Locations",
> 
>   x = "0%", y = "0%",
> 
>   width = "100%", height = "25%"
> 
> }, left_container)
> 
> Locations:setStyleSheet([[
> 
>   background-color: black;
> 
>   border-width: 2px;
> 
>   border-style: solid;
> 
>   border-color: grey;
> 
>   border-radius: 10px;
> 
>   font: bold "Monospace";
> 
>   font-size: 1px;
> 
> 
> 
> ]])
> 
> 
> 
> -- MSDP values, unless stored by lua again as something user defined will always be "atcp.MSDP(somevariablehere)" Partly because we are using atcp to fetch our MSDP variables. Below I'm just using echo to directly display our information to the labels. This one is sending echo text to the Locations label we made earlier on. <br> will return you to the next line, while <hr> makes the devider line between each stat I had displayed. Play with it a bit and you'll know just how to change it to suit your own needs. You can go to the statistics button in the area to see every msdp value I have getting reported for this plugin, as well as the values. Debug can also be benefitial to see where scripts are firing, and areas where you think they are, yet nothing is actually happening.
> 
> 
> 
> Locations:echo("LOCATION INFORMATION:<br><hr><br>Continent:"..atcp.MSDPCONTINENT.."<hr>Area: "..atcp.MSDPAREA_NAME.."<hr>Room: "..atcp.MSDPROOM_NAME.."<hr>Exits: "..atcp.MSDPROOM_EXITS.."<hr>Terrain: "..atcp.MSDPTERRAIN.."<hr>Room ID: "..atcp.MSDPROOM_VNUM)
> 
> 
> 
> Grouping = Geyser.Label:new({
> 
>   name = "Grouping",
> 
>   x = "0%", y = "25%",
> 
>   width = "100%", height = "35%" 
> 
> }, left_container)
> 
> Grouping:setStyleSheet([[
> 
>   background-color: black;
> 
>   border-width: 2px;
> 
>   border-style: solid;
> 
>   border-color: grey;
> 
>   border-radius: 10px;
> 
>   font: bold "Monospace";
> 
>   font-size: 4px;
> 
> 
> 
> ]])
> 
> Grouping:echo("GROUP FIGHTING:<br><hr><br>Group Leader: "..atcp.MSDPGROUP_LEADER.."<hr>Tank Name: "..atcp.MSDPTANK_NAME.."<hr>Tank Health: "..atcp.MSDPTANK_HEALTH.."/"..atcp.MSDPTANK_HEALTH_MAX.."<hr>Tank Level: "..atcp.MSDPTANK_LEVEL.."<hr><br>Enemy: "..atcp.MSDPOPPONENT_NAME.."<hr>Level: "..atcp.MSDPOPPONENT_LEVEL.."<hr>Health: "..atcp.MSDPOPPONENT_HEALTH.."/"..atcp.MSDPOPPONENT_HEALTH_MAX)
> 
> --echo("Grouping", "[[<p style="font-family: monospace; font-size:small;">]][[GROUP FIGHTING: <br>==============<br>Group Leader: ]]..atcp.MSDPGROUP_LEADER..[[<br>Tank Name: ]]..atcp.MSDPTANK_NAME..[[<br>Tank Health: ]]..atcp.MSDPTANK_HEALTH..[[/]]..atcp.MSDPTANK_HEALTH_MAX..[[<br>Tank Level: ]]..atcp.MSDPTANK_LEVEL..[[<br><br>Enemy: ]]..atcp.MSDPOPPONENT_NAME..[[<br>Level: ]]..atcp.MSDPOPPONENT_LEVEL..[[<br>Health: ]]..atcp.MSDPOPPONENT_HEALTH..[[/]]..atcp.MSDPOPPONENT_HEALTH_MAX[[</p>]])
> 
> 
> 
> Statistics = Geyser.Label:new({
> 
>   name = "Statistics",
> 
>   x = "580%", y = "0%",
> 
>   width = "100%", height = "100%"
> 
> }, right_container)
> 
> Statistics:setStyleSheet([[
> 
>   background-color: black;
> 
>   border-width: 2px;
> 
>   border-style: solid;
> 
>   border-color: grey;
> 
>   border-radius: 10px;
> 
>   font: bold "Monospace";
> 
>   font-size: 6px;
> 
> ]])
> 
> Statistics:echo("STATS INFORMATION:<hr>Name: "..atcp.MSDPCHARACTER_NAME.."<br>Citizen of "..atcp.MSDPCITIZEN.."<br> Your alignment is: "..atcp.MSDPALIGNMENT.."<br>Sex: "..atcp.MSDPSEX.."<hr>Money: "..atcp.MSDPMONEY.."<br>Drachma: "..atcp.MSDPDRACHMA.."<hr>Levels:<br>"..atcp.MSDPCLASS.." "..atcp.MSDPLEVEL.." "..atcp.MSDPCLASS_SEC.." "..atcp.MSDPLEVEL_SEC.." "..atcp.MSDPCLASS_TER.." "..atcp.MSDPLEVEL_TER.." "..atcp.MSDPCLASS_QUA.." "..atcp.MSDPLEVEL_QUA.."<br>"..atcp.MSDPCLASS_QUI.." "..atcp.MSDPLEVEL_QUI.." "..atcp.MSDPCLASS_HEX.." "..atcp.MSDPLEVEL_HEX.." "..atcp.MSDPCLASS_SEP.." "..atcp.MSDPLEVEL_SEP.." "..atcp.MSDPCLASS_OCT.." "..atcp.MSDPLEVEL_OCT.."<br>Avatar: "..atcp.MSDPCLASS_AVA.." "..atcp.MSDPLEVEL_AVA.."<hr> Experience: "..atcp.MSDPEXPERIENCE.."<hr>Health: "..atcp.MSDPHEALTH.." / "..atcp.MSDPHEALTH_MAX.."<hr> Mana: "..atcp.MSDPMANA.." / "..atcp.MSDPMANA_MAX.."<hr> Moves: "..atcp.MSDPMOVEMENT.." / "..atcp.MSDPMOVEMENT_MAX.."<hr> AC: "..atcp.MSDPAC.."<hr> HONOR: "..atcp.MSDPHONOR.."<hr> STR:"..atcp.MSDPSTR.."/"..atcp.MSDPSTR_PERM.." CON:"..atcp.MSDPCON.."/"..atcp.MSDPCON_PERM.."<br> DEX:"..atcp.MSDPDEX.."/"..atcp.MSDPDEX_PERM.." WIS:"..atcp.MSDPWIS.."/"..atcp.MSDPWIS_PERM.."<br>INT:"..atcp.MSDPINT.."/"..atcp.MSDPINT_PERM.." CHAR:"..atcp.MSDPCHARISMA.."/"..atcp.MSDPCHARISMA_CAP.."<hr>Spells and Damage:<br>Weapon Damage: "..atcp.MSDPWEAPON_DAM.."<br>Stab Damage: "..atcp.MSDPSTAB_DAM.."/"..atcp.MSDPSTAB_DAM_CAP.."<br>Hand Damage: "..atcp.MSDPHAND_DAM.."/"..atcp.MSDPHAND_DAM_CAP.."<br> Undead Cont: "..atcp.MSDPUNDEAD_CONT.."/"..atcp.MSDPUNDEAD_CONT_CAP.."<br>Spell Bonus: "..atcp.MSDPSPELL_BONUS.."/"..atcp.MSDPSPELL_BONUS_CAP.."<br>Heal Bonus: "..atcp.MSDPHEAL_BONUS.."/"..atcp.MSDPHEAL_BONUS_CAP.."<hr>Hitroll: "..atcp.MSDPHITROLL.."<hr>Damroll: "..atcp.MSDPDAMROLL.."<hr>Damage Red: "..atcp.MSDPDAM_RED.."/"..atcp.MSDPDAM_RED_CAP)
> 
> 
> 
> 
> 
> end
> 
> 
> 
> 
> 
> -- Thanks. I didn't write the same thing for every line on here, but I think you get the general picture of what I did on here. Note that this isn't even scratching the surface of what mudlet can do. I'm just a newbie doing what I like to do best, playing with code, seeing how things work, and happy when something does work right, no matter how easy it may seem for others lol. Hope this can help anyone.
> 
> 
> 
> One tip when scripting, when you don't know if something is working right or not, is to place echo("test1") ... within various places in your script if you are unsure if things are being called. Echo variables to make sure they are being called or updated echo(somevariablehere)  or like I've done sometimes echo("This is where I started such and such") or echo("This variable just got stored with the value"..somevaluename)
> 
> 
> 
> Good luck!

</div>
