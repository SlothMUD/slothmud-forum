---
title: "GETMSDPVARS() ADVISORY"
topic_id: 4211
author: "DarkArtist"
date: 2014-03-18T19:32:26+00:00
last_activity: 2014-04-13T22:02:11+00:00
last_author: "DarkArtist"
sticky: false
locked: false
post_count: 4
---

<div class="post" data-post-id="34918" data-author="DarkArtist" data-date="2014-03-18T19:32:26+00:00" data-subject="GETMSDPVARS() ADVISORY">

Are you triggering your getmsdpvars() function on the event SERVER_ID? 

If you are, or if you are triggering your getmsdpvars cmd on any msdp update, then you are potentially lagging the whole mud slightly and if too many people do this then it could become more than slightly. This is because you are sending the request to the sloth server every second instead of every login.

If this is you, please correct it by triggering getmsdpvars() off of one of the login messages.

If you are confused about this, insert an echo command into your getmsdpvars() function. If you see the echo repeat over and over, then you're guilty and need to get right.

This has been a public service announcement.

</div>

<div class="post" data-post-id="34990" data-author="DarkArtist" data-date="2014-04-13T21:50:36+00:00" data-subject="Re: GETMSDPVARS() ADVISORY">

By the way if anyone wants it, here is my getmsdpvars function:

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

If any don't work properly, check the spacing. Notice the space before the second row of the list. I don't know why it should matter but it does.  I mention this because the above list is not complete as I don't use all of them and Splork asked us to only include the ones we intend to use. So if you add some to this list and they not working, try playing with the spacing.

</div>

<div class="post" data-post-id="34991" data-author="DarkArtist" data-date="2014-04-13T21:58:00+00:00" data-subject="Re: GETMSDPVARS() ADVISORY">

And after you set that up and trigger it something on startup you also need an update function for each var like so

Script Name updateMana 

function updateMana()

mana=atcp.MSDPMANA+0

end

Then you're going to type in an event handler that matches the name of the variable, in this case type in 

MSDPMANA and click the plus sign and you'll see it appear above.

And thats it. Remember that the script name matches the function name and dont forget to click the plus sign to add the event handler.

Oh, also don't forget that you need a script containing your variable definitions. In the above for example you need to define the variable named mana as such:

mana=mana or 0

for variables that are strings it would be

variable=variable or ""

fyi all msdp variables are strings, you have to convert them into integers when needed as in the above you see mana=atcp.MSDPMANA+0. In lua adding an integer to a string converts it to an integer if the the string is a numeral.

</div>

<div class="post" data-post-id="34992" data-author="DarkArtist" data-date="2014-04-13T22:02:11+00:00" data-subject="Re: GETMSDPVARS() ADVISORY">

While I'm at it, here is what I trigger my getmsdpvars off of:

1) Enter the game.

Do you wish to force the connection closed (Y/N)

Password accepted.  Press return to continue...

</div>
