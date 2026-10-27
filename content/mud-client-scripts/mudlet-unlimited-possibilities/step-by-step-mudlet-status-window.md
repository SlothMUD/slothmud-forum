---
title: "Step by Step Mudlet Status Window"
topic_id: 4232
author: "Thraxas"
date: 2014-04-21T23:00:41+00:00
last_activity: 2014-04-23T13:35:48+00:00
last_author: "Akaya"
sticky: false
locked: false
post_count: 2
---

<div class="post" data-post-id="35036" data-author="Thraxas" data-date="2014-04-21T23:00:41+00:00" data-subject="Step by Step Mudlet Status Window">

Fairly new to mudlet so still learning but thought that as I was asked in game it might be helpful to post my howto on creating a simple window showing various statuses (e.g. spells / toggles):

Step 1:

Set up a variable that can record the status of a variable in the case the variable will store the status of your sanctuary spell.

Go to Scripts

Add Item

```
Script name = Misc variables [i](or something similar)[/i]
Code (the big box at the bottom): mysanc=mysanc or ""
```

<em>(You can add definitions of additional variables into the same script each on a new line)</em>

Step 2 : 

Record the status of a spell in the variable.

Create 3 triggers for sanctuary up, sanctuary falling and sanctuary down.

Go to Triggers, Add Item:

Trigger 1 

```
Name: Sanc Up
keywords (exact match):
You start glowing.
Code: 
mysanc="S"
updatestatus()
```

Trigger 2

```
Name: Sanc Falling
keywords (exact match):
The 'sanctuary' spell on you is about to wear off.
Code:
mysanc="SF"
updatestatus()
```

Trigger 3

```
Name: Sanc Down
keywords (exact match):
The white aura around your body fades.
Code:
mysanc="N"
updatestatus()
```

Step 3:

Create a window to display the status of your sanctuary spell (and other spells in).

go to scripts

add item

script name: createstatus()

code (big box at the bottom):

```
function createstatus()
createMiniConsole("statuswindow",750,10,150,350)
updatestatus()
end
```

This code needs to be triggered when you log in so will also need a trigger:

go to triggers

add item

```
Name: Login 
keywords (exact match) (on 3 lines):
1) Enter the game.
Do you wish to force the connection closed (Y/N)
Password accepted. Press return to continue...
Code:
createstatus()
updatestatus()
```

<em>You will need to log back into the game for this to be created (or run the script from an alias)</em>

Step 4:

Now we need to create the updatestatus() script that will drop the sanctuary status into the status window

goto scripts

add item

Name: updatestatus()

code (big box at the bottom):

```
function updatestatus()

--Empty anything in the status window--
 clearUserWindow("statuswindow") 

--Add a Title to the top of the window--
	echo("statuswindow"," Status Window\n")
	cecho("statuswindow","--------------------------------------\n")

--Show Sanctuary Up in Green--
	if mysanc=="S" then
 cecho("statuswindow","<green> Sanctuary Falling\n")
	end
--Show Sanctuary Falling in Yellow--
	if mysanc=="SF" then
 cecho("statuswindow","<yellow> Sanctuary Falling\n")
	end
--Show Sanctuary Down in Red : make this a link to cast the sanctuary spell--
	if mysanc=="N" then
 fg("statuswindow","red")
 echoLink("statuswindow", " cast sanctuary \n", [[send("cast 'sanctuary'")]], "",true)
 resetFormat("statuswindow")
	end

end --function end--
```

Save all this, re-login then cast sanctuary. You should see a box appear top middle of the screen that shows you your sanctuary spell.

Hope that helps,

Thraxas

notes:

1\. The \\n in the echo text denotes a new line.

2\. in the createMiniConsole("statuswindow",750,10,150,350) the numbers here mean:

 750 and 10 position the console window across and down

 150 and 350 size the console window across and down

3\. console windows can be moved using e.g. moveWindow( "statuswindow", 750, 360 )

4\. console windows can be resized using e.g. resizeWindow( "statuswindow", 150, 600 )

5\. console windows can be hidden and displayed using hideWindow("statuswindow") and showWindow("statuswindow") <em>(I add these to buttons)</em>

6\. Its useful to give the mysanc variable a value when you login - nothing will be displayed until it has a value by casting sanc / sanc dropping or adding e.g. mysanc = "N" to login script

</div>

<div class="post" data-post-id="35073" data-author="Akaya" data-date="2014-04-23T13:35:48+00:00" data-subject="Re: Step by Step Mudlet Status Window">

Well done <img src="/images/smilies/icon_e_smile.svg" alt=":)" title=":)" width="15" height="15" class="smiley nozoom">

</div>
