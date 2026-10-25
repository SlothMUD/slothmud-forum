---
title: "HOWTO: Assist Tank in all Circumstances"
topic_id: 4815
author: "Gorka"
date: 2017-12-29T07:24:54+00:00
last_activity: 2018-01-02T21:22:58+00:00
last_author: "Gorka"
sticky: false
locked: false
post_count: 2
---

<div class="post" data-post-id="38570" data-author="Gorka" data-date="2017-12-29T07:24:54+00:00">

For new players, setting up triggers to assist the tank in a fight can be a daunting process. However there is a way you can assist the tank in all circumstances, without trapping specific events. This can be done by using the msdp.GROUP variable.

Inside this variable contains information on all the members in your group, their position and status. We can set an event handler on this variable to run a function every time the contents of this variable changes. This can be done in mudlet by creating a new script and entering "msdp.GROUP" under Add User Defined Event Handler box and pressing the + button to add it to the list of "Registered Event Handlers."

Once that has been setup, you can now program your function to run every time this variable changes... What this function does, is finds the person in the group who is the tank... if that person is not you, it checks that persons status to see if they are fighting. If that condition is true, and your status is not fighting, then it will assist the tank.

```
function AssistTank()
   if msdp.TANK_NAME ~= msdp.CHARACTER_NAME then
      for key,value in pairs(msdp.GROUP) do
         if msdp.GROUP[key]["NAME"] == msdp.TANK_NAME then
            if msdp.GROUP[key]["STATUS"] == "Fighting" and msdp.POSITION ~= "Fighting" then
               send("assist "..msdp.TANK_NAME)
            end
         end
      end
   end
end
```

This function is basic, and there are many ways to improve it... for example, you could add a check to see if you are "Absent" from the group, so you don't try and assist when you are absent, or you could provide a set variable to define who the tank is, so all the members of the group are not looped each time the variable changes to increase efficiency. Furthermore instead of assisting, you could call a further function which completes some functions on the fight initiation such as web, damn, blind etc. Or you could continue being a tosser and do nothing... in which case enjoy the xp at continent recall at least in my groups.

</div>

<div class="post" data-post-id="38582" data-author="Gorka" data-date="2018-01-02T21:22:58+00:00">

I promised Breeze I would update my script a bit more... (Note: Name Change - but no consequence)

New Version:

-- Script won't assist if you are absent

-- Script prepares leader/tank/me variables for further use

-- Script creates a group report, saves it to a string variable (groupreport) this could be outputted to a window

-- Script could man you back if your position is set to "Front" just uncomment the lines

-- Created condition to warn you if the tank is fighting and you are not with the group

```
function ProcessGroup()
   local tank, leader, me
   groupreport = ""

   --Determine who is what in the group
   for key,value in pairs(msdp.GROUP) do
      if msdp.GROUP[key]["NAME"] == msdp.TANK_NAME then
         tank = key
      end
      if msdp.GROUP[key]["NAME"] == msdp.CHARACTER_NAME then
         me = key
      end
      if msdp.GROUP[key]["POSITION"] == "Pleader" then
         leader = key
      end
      if msdp.POSITION == "Fighting" then
         if msdp.GROUP[key]["STATUS"] == "Standing" then
            groupreport = groupreport.."\n"..msdp.GROUP[key]["NAME"].." is not fighting."   
         end
      end
      if tonumber(msdp.GROUP[key]["HITPOINTS"]) <= -10 then
         groupreport = groupreport.."\n"..msdp.GROUP[key]["NAME"].." is Dead."  
      end
      if tonumber(msdp.GROUP[key]["HITPOINTS"]) >= -9 and tonumber(msdp.GROUP[key]["HITPOINTS"]) <= 0 then
         groupreport = groupreport.."\n"..msdp.GROUP[key]["NAME"].." is Incap."  
      end
      if tonumber(msdp.GROUP[key]["HITPOINTS"]) > 0 and tonumber(msdp.GROUP[key]["HITPOINTS"]) <= 100 then
         groupreport = groupreport.."\n"..msdp.GROUP[key]["NAME"].." is Dying."  
      end
      if msdp.GROUP[key]["STATUS"] == "Absent" then
         groupreport = groupreport.."\n"..msdp.GROUP[key]["NAME"].." is Absent."  
      end
   end

   --Assist the tank, if I am with group and he is fighting
   if msdp.TANK_NAME ~= msdp.CHARACTER_NAME then
      if msdp.GROUP[tank]["STATUS"] == "Fighting" and msdp.POSITION ~= "Fighting" and msdp.GROUP[me]["STATUS"] ~= "Absent" then
         --echo("THE TANK IS FIGHTING, I WILL ASSIST THEM!")
         send("assist "..msdp.TANK_NAME)
      elseif msdp.GROUP[tank]["STATUS"] == "Fighting" and msdp.GROUP[me]["STATUS"] == "Absent" then
         --echo("THE TANK IS FIGHTING, I AM ABSENT!")
      end
   end

   --Man back if I am in the front row
   --if msdp.GROUP[me]["POSITION"] == "Front" then
   --   send("man back")
   --end
end
```

</div>
