---
title: "MSDP additons"
topic_id: 4173
author: "Akaya"
date: 2013-12-19T23:50:13+00:00
last_activity: 2014-06-15T16:35:12+00:00
last_author: "Tuck"
sticky: false
locked: false
post_count: 19
---

<div class="post" data-post-id="34659" data-author="Akaya" data-date="2013-12-19T23:50:13+00:00">

I keep coming across ideas for MSDP variables. Figured I'd start a topic to keep them organized...

1. Hunger and thirst level

</div>

<div class="post" data-post-id="34660" data-author="DarkArtist" data-date="2013-12-20T14:04:14+00:00">

2. Character Position

3. Spell Affects

</div>

<div class="post" data-post-id="34661" data-author="*Splork*" data-date="2013-12-20T14:49:04+00:00">

Spell Affects and exits are already in-game but again, they are listed with the odd characters. I still can't figure out why it works for mushclient but not mudlet. I will update the helpfile today with the missing variables which are already reported.

They said this issue will be addressed with mudlet 3.0 but I do not believe thats anywhere in sight. I know that Akaya, for windows, used gsub() for the unknown characters and replaced it with a comma in one of his scripts but I don't have a copy of that one.

We might have to look at sending each affect separably maybe.

</div>

<div class="post" data-post-id="34662" data-author="DarkArtist" data-date="2013-12-20T18:53:01+00:00">

Separate would be a ton of new vars. I will just take the string and do a pattern match and send the matches to a new table, rather than sub out the weird chars. It should be pretty straightforward.

So thanks for putting those in, that's pretty awesome. I'll post the pattern match script when I get it worked out. I didn't get around to trying Akaya's after he told me how to input the characters, so I don't know if that works or not. He said something about linux or Ubuntu being different? I'm not even sure what that means with regard to mudlet. I need to muscle thru it anyway as a learning exercise. 

It would be pretty cool too btw if msdpexits added a prefix or suffix that indicates door status.  Since we have to pattern match anyway, it wouldn't make it any harder.

Here is how I currently parse the room exits that I pull from regular output, to take out the brackets. It's a crude first step to parsing them for door status as well.

exits=exits or {}

parsedExits=parsedExits or {}

exitString=exitString or ""

function parseExits()

parsedExits={}

for k,v in pairs(exits) do  --print(k,v) --for testing

if string.findPattern(v, "North") then

table.insert(parsedExits, "North") 

elseif string.findPattern(v, "South") then

table.insert(parsedExits, "South") 

elseif string.findPattern(v, "East") then

table.insert(parsedExits, "East") 

elseif string.findPattern(v, "West") then

table.insert(parsedExits, "West") 

elseif string.findPattern(v, "Up") then

table.insert(parsedExits, "Up") 

elseif string.findPattern(v, "Down") then

table.insert(parsedExits, "Down")  end end

Then to test an exit against the parsed table:

function validExit(dir)

parseExits()

if table.contains(parsedExits,dir) then

return(true)

else return(false) end end

Here's my exits trigger in case someone needs it too

^Exits:(\s+)(.*)(\s\s\s)$

exitString=matches[3]

exits=exitString:split("  ")    ---TWO SPACES

--display(exits)...for testing

parseExits()

selectCurrentLine()

deleteLine()  --I don't care to see the exits.

This should work for the msdp output too. Haven't done it yet tho. I'm working on parsing door status (open/closed) brackets to make a key val pair of valid exits / status. This stuff probably exits in the mapper scripts somewhere, but it's too obtuse for my limited skills as of yet. The advantage of the above scripts is that a newb like me can understand whats going on.

edit: maybe instead of a prefix or suffix for door status, just have the output in pairs? i.e. North closed South open East locked.  Just a thought.

</div>

<div class="post" data-post-id="34663" data-author="*Splork*" data-date="2013-12-20T20:17:53+00:00">

> **DarkArtist wrote:**
> It would be pretty cool too btw if msdpexits added a prefix or suffix that indicates door status. Since we have to pattern match anyway, it wouldn't make it any harder.

I probably should document some of these variables better. The room_exits table includes W for Window, C for Closed exit ( door ), and O for an Open door. So if you call MSDP Room_EXits and see North O South C it means there is a north exit which is clear or open and a south exit with a door which is closed. I can extend this once we figure out what is going on with the parsing.

I got extremely frustrated before with the odd characters from the msdpTable stuff ( exits and affects ) that I created the following msdp variables were added long ago but never mentioned ( they are in-game, just need to call for them ):

Room_Up

Room_Down

Room_East

Room_West

Room_South

Room_North

These variables will either read the direction or none, meaning there is no exit to that direction. I am not sure how useful these are but they will read clearly and not need any pattern matching:)

Also, I started a larger project with Akaya which never got finished but the basic idea was to output msdp variables to create a 5x5 grid which displayed in this order:

RoomVnum, possible rooms in each direction, pcs and mobs in each of those rooms. 

This code may or may not be in-game currently but to try to  mess around with this code, you need to ask for the following variables:

 COORD1,

   COORD2,

   COORD3,

   COORD4,

   COORD5,

   COORD6,

   COORD7,

   COORD8,

   COORD9,

   COORD10,

   COORD11,

   COORD12,

   COORD13,

   COORD14,

   COORD15,

   COORD16,

   COORD17,

   COORD18,

   COORD19,

   COORD20,

   COORD21,

   COORD22,

   COORD23,

   COORD24,

   COORD25,

 

If this is not working please let me know and I can look into it.

Splork

</div>

<div class="post" data-post-id="34664" data-author="*Splork*" data-date="2013-12-20T20:40:15+00:00">

I figured the issue out with the above mentioned variables:

Here is the output for splork, only tested coord1-3 and the room_Dir variables, its leaving out the odd characters seperating everything. I will have to tinker with this some more. Atm, the variables are not Room_East but MSDP_ROOM_EAST:) I removed the msdp part on next reboot.

  

MSDPGROUP_LEADER = "Splork",

  MSDPMSDP_COORD2 = "12199619560199721192050000",

  MSDPMSDP_ROOM_WEST = "West",

  MSDPMSDP_COORD3 = "13196101962000002",

  MSDPAFFECTS = "bought-1bought-1bought-1bought-1bought-1bought-1bought-1class-1",

  MSDPMSDP_ROOM_EAST = "East",

  MSDPMSDP_ROOM_DOWN = "None",

  MSDPMSDP_ROOM_SOUTH = "South",

  MSDPMSDP_ROOM_NORTH = "North",

  MSDPMSDP_COORD1 = "22199719962044199820162051000",

  MSDPROOM_EXITS = "NorthOEastOSouthOWestOUpO",

</div>

<div class="post" data-post-id="34665" data-author="DarkArtist" data-date="2013-12-20T23:06:30+00:00">

So the new format for MSDPROOM_EXITS goes in on reboot too? You have it printed there as output but I still get the old format ingame.

I wrote a parser for the new format, using only the functions that I know, so yeah it's probably needlessly complex, but then needlessly complex is my forte.

I think the above should give a key val pair of Dir / Status. Am I on the right track here?:

exits=exits or {}

----parse mspdroom_exits into a list of elements

function getExits()

dirMatch={"NorthO","SouthO","EastO","WestO","UpO","DownO","NorthC","SouthC","EastC","WestC","UpC","DownC"}

--exitString=atcp.MSDPROOM_EXITS 

exitString={"NorthOSouthCWestO"} --testing

rawExits={}

exits={}

for i,v in ipairs(dirMatch) do

if string.findPattern(exitString,v) then

table.insert(rawExits, v)

end end

---now parse it into a new key val table of Dir/Status

for k,v in pairs(rawExits) do

if k=="NorthO" then 

table.insert(exits,"North")

exits["North"]="O" 

elseif k=="SouthO" then

table.insert(exits,"South")

exits["South"]="O" 

elseif k=="EastO" then

table.insert(exits,"East")

exits["East"]="O" 

elseif k=="WestO" then

table.insert(exits,"West")

exits["West"]="O" 

elseif k=="UpO" then

table.insert(exits,"Up")

exits["Up"]="O" 

elseif k=="DownO" then

table.insert(exits,"Down")

exits["Down"]="O" 

elseif k=="NorthC" then

table.insert(exits,"North")

exits["North"]="C" 

elseif k=="SouthC" then

table.insert(exits,"South")

exits["South"]="C" 

elseif k=="EastC" then

table.insert(exits,"East")

exits["East"]="C" 

elseif k=="WestC" then

table.insert(exits,"West")

exits["West"]="C" 

elseif k=="UpC" then

table.insert(exits,"Up")

exits["Up"]="C" 

elseif k=="DownC" then

table.insert(exits,"Down")

exits["Down"]="C" 

end end 

display(exits)

end

</div>

<div class="post" data-post-id="34666" data-author="*Splork*" data-date="2013-12-21T01:30:37+00:00">

My post was missing the odd characters, they wouldn't paste for some reason. Room_exits and affects output has not changed and the current in-game outputs are the same. Sorry for the confusion.

I am going to spend tonight and try to figure out a better output, it wont meet the msdp specification but who really cares. Ill call it something like mudlet_room_exits and mudlet_affects.

Ill post any updates as they come.

</div>

<div class="post" data-post-id="34667" data-author="Dragoth" data-date="2013-12-21T08:36:58+00:00">

Any chance to add aerial servant %hp to MSDP

</div>

<div class="post" data-post-id="34673" data-author="Akaya" data-date="2013-12-21T16:35:14+00:00">

DarkArtist had a good idea....

Here's a parser for MSDPROOM_EXITS that will work regardless of the OS.

It simply checks MSDPROOM_EXITS against a table of possible directions and returns a key-value table of room exits AND door status.

```
function parseExits()
  local exits = {}
  local str = atcp.MSDPROOM_EXITS
  local dirs = {"North","South","East","West","Up","Down"}
  for k,v in pairs(dirs) do
    if string.findPattern(str, v) then
      local len = string.cut(string.reverse(string.cut(atcp.MSDPROOM_EXITS, string.find(str,v) + string.len(v) + 1)), 1)
      exits[v] = len
    end
  end
  return exits
end
```

Sample Usage:

```
-- use this function to run away to the direction specified returned and open the door (if there is one):
function runAway(dir)
  if parseExits()[dir] == "O" then
    send(dir)
  end
end
```

</div>

<div class="post" data-post-id="34674" data-author="DarkArtist" data-date="2013-12-21T17:44:26+00:00">

Thanks for that, if you come up with an elegant way to assign door status values to the elements of the exits table, pls post it too. I'm not doing too bad for two weeks of studying, but the simple solution isn't clear to me on that one yet.

</div>

<div class="post" data-post-id="34677" data-author="Akaya" data-date="2013-12-21T22:43:58+00:00">

Update the parseExits() function. It now returns a key-value table of each exit and it's door status. Comes out looking like this when you run it:

```
{
  West = "O",
  South = "C",
  East = "O",
  North = "W"
}
```

Since the door status is 2 characters after every exit, I was able to cut the string to length, reverse it, then cut it again to 1 character (the door status) and assign it as the value to it's exit.

Best part: All the 'weird characters' are avoided.

</div>

<div class="post" data-post-id="34679" data-author="*Splork*" data-date="2013-12-23T20:13:42+00:00">

Please check the following format for MSDPJSON_AFFECTS AND MSDPJSON_ROOM_EXITS and see if this will be easier to parse.  I do realize this is not JSON format but its close which is why its named that. The odd characters are pushed outside the brackets and only show at the front and back of the entire line. Is this good or any ideas how to make it easier for you guys?

NewMSDPFormat.PNG

</div>

<div class="post" data-post-id="34680" data-author="Akaya" data-date="2013-12-23T20:43:19+00:00">

Since we're trying to parse a single string here, I think it might be best to place a delimiter between each value rather than encasing it in brackets or quotes. So rather than having the string represent JSON, have it as the most simplified string possible with only the necessary info. Something like this would be ideal:

"bless: 1110, stone skin: 1030, shield of faith: 24"

Because we are dividing the string up and not converting it, having a simple delimiter at the end of every section make it much more simplistic.

I know the weird characters at the beginning and end are unavoidable but they can be parsed out fairly easy if its just the two of 'em.

</div>

<div class="post" data-post-id="34681" data-author="*Splork*" data-date="2013-12-23T23:14:24+00:00">

Variable Names :STRING_AFFECTS and STRING_PERM_AFFECTS -> Affect name followed by affect modifier
string_affects.PNG

Variable Name: STRING_EXITS -> exit direction followed by open, closed, window, etc.
string_exits.PNG

I can't seem to figure out why certain affects duplicate. Very odd and I will keep looking into it.

How does this format look? Suggestions?

Splork

</div>

<div class="post" data-post-id="34682" data-author="Akaya" data-date="2013-12-24T04:38:55+00:00">

this is beautiful. Im on my phone right now but ill write a parser for this in the morning. Thanks Splork!

</div>

<div class="post" data-post-id="34743" data-author="DarkArtist" data-date="2013-12-30T17:42:41+00:00">

Spell affects output looks good since it can be parsed with the same algorithm as string_exits.

Since you've got string exits in, maybe ROOM_EAST, ..WEST, etc could be repurposed to return the room sector, exit flags, and room flags for the attached room? Sector would be good for knowing if you're about to walk off a cliff or underwater. Some handy room flags would be Dark and Indoors, I wouldn't expect any that couldn't be reasonably determined from an adjacent room, e.g. NoFlee. Some handy exit flags would be NoMount, Locked,  NoMob. They could just be a colon separated list without categories that could be split into a simple table. Wouldn't need to specify if it was the sector or room flag or exit flag. Just test ROOM_X for MidAir or wutever and you'd be good to go. It seems this would be pretty handy for automated mapping features, once more people get into that.

Not a priority, just a thought.

</div>

<div class="post" data-post-id="34824" data-author="Akaya" data-date="2014-01-24T20:10:40+00:00">

Here's a parser for the new MSDPWEAR_<slot> additions.

```
function parseEQ(event,msdp)
  local EQ = {}
  msdp = string.split(msdp,",")
  for k,v in pairs(msdp) do
    msdp[k] = string.split(msdp[k],":")
  end
  for k,v in pairs(msdp) do
    EQ[v[1]] = v[2]
  end
  return EQ
end
```

It returns a lua table with the relevent info from the eq slot requested

```
--Example Usage (sent by an event)
display(parseEQ("MSDPWEAR_HEAD","VNUM:3002,DESC:a lesser helm,AC-apply:-1.0,"))
```

</div>

<div class="post" data-post-id="35343" data-author="Tuck" data-date="2014-06-15T16:35:12+00:00">

Continued here: [http://www.slothmud.org/forum/viewtopic.php?f=30&t=4371](http://www.slothmud.org/forum/viewtopic.php?f=30&t=4371)

</div>
