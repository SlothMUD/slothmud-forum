---
title: "Mudlet 3.0.0-delta Mapper"
topic_id: 4732
author: "Gorka"
date: 2017-01-28T18:40:00+00:00
last_activity: 2017-02-13T21:05:43+00:00
last_author: "Gorka"
sticky: false
locked: false
post_count: 35
---

<div class="post" data-post-id="38000" data-author="Gorka" data-date="2017-01-28T18:40:00+00:00" data-subject="Mudlet 3.0.0-delta Mapper">

Yesterday I found the desire to start playing around with the Mudlet Mapper and after many, many hours of struggle I managed to get it functioning today... but not without problems that I thought I would share with you, as there is obviously a fair bit of interest in getting the mapper working for SlothMUD.

Problem 1: Akaya's original mapper. (It won't work)

Akaya who was instrumental in creating the buzz that brought MSDP to slothmud, originally wrote a Mapper for Slothmud. This mapper used the msdp COORDS variables that were later removed because they were thought to be lagging the mud. Furthermore, I got a sense his mapper was snippets of code, copy and pasted from other authors and slightly adapted. Because the variables he was using are no longer in Sloth I really had no choice but to write my own mapper completely from scratch using msdp.ROOM_EXITS.  

Problem 2: Room Collisions.

When I finally got my mapper to "map" a massive problem was exposed, which to some degree would probably make some area's not worth mapping... let me explain... the way I mapped things was using the x,y,z coordinate system in Mudlet. Lets assume that our first room is West Gate BH (0,0,0). We go 1 east (1,0,0). We go another east (2,0,0). We go one north (2,1,0) and we are in the Auction House. 

Ok, now try this out... Lets assume that our first room is West Gate BH (0,0,0). We go 1 east (1,0,0). We go 1 north (1,1,0). We go 1 east (2,1,0). Where are we? The auction house right? No! The Bal Harbor Animal Market. 

So straight away there is a problem... there are "collisions" with rooms... the coordinates for the Bal Harbor Animal Market are the same as the coordinates for the Auction House from West Gate... on the map this will place a room on top of another room. The reality is BH is a confused area with many collisions and essentially the map looks like crap. It would appear Akaya's original mapper didn't address this problem either.

So not to be beaten, I made a room collision detection system... when ever I added a new room to the map I checked to see if there was a double up, and if there was I placed that room with an angled line as to not place the rooms on top of each other. Perhaps I would even need to go further, and move all rooms that are on that axis over one, and re-index the rooms if I wanted to keep the lines straight. Area's like Kobolds mapped great as there are no collisions.

I think it would be fairly common to have coordinate collisions in a mud... and I wondered if anyone else has found a way to work around this, while trying to keep map lines straight? If so please share...

Problem 3: Detecting you have changed a room.

The other issue is each time you want to move a room, you want to add the new room and all it's links to the map... well as you may know, there is really no way to detect you have changed a room in Slothmud if you are solo. Capturing the msdp.ROOM_VNUM change event or msdp.ROOM_EXITS events are flawed because they fire multiple times and are subject to msdp update lag. If I walk fast then mapping some rooms will be missed out and my coordinates will be wrong. It appears the only way to map a room constantly once, would be to so in a group, as you could trigger the mapping on the following leader message. However as I was using msdp.ROOM_VNUM as the key for my rooms, and this variable is subject to lag... I wonder if that would even work. There doesn't seem to be a good way to do this but to add each room manually. Once again I wondered if anyone else has found a way to work around this?

I still have more work to do, to have colors for the terrain and run scripts that goto rooms etc... but I kind of feel without these other problems being resolved... whats the point... Does anyone have experience mapping muds and can tell me good ways to overcome these problems?

</div>

<div class="post" data-post-id="38001" data-author="*teker*" data-date="2017-01-28T21:31:25+00:00" data-subject="Re: Mudlet 3.0.0-delta Mapper">

I think there are 2 pieces to making this work better:

1) Have the game proactively send new room information each time you change rooms.  I'm not sure what you'd really need other than the Vnum.

2) The right solution for putting maps in the client is to throw away the idea of self discovery and include pre-built maps in a Sloth package for Mudlet.  We could built tools to take the existing areas from either file or database and convert them to XML files that Mudlet can read.  Someone would need to massage the X,Y coordinates to solve the collision problem but once the problem is solved, the entire community would benefit.

</div>

<div class="post" data-post-id="38003" data-author="Filk" data-date="2017-01-29T07:24:28+00:00" data-subject="Re: Mudlet 3.0.0-delta Mapper">

> **Quote:**
> 1) Have the game proactively send new room information each time you change rooms. I'm not sure what you'd really need other than the Vnum.

Great idea. And i even mailed you with such idea month ago. You didnt answer though, so not sure if mail was received or i used correct email :)

> **Quote:**
> 2.  pre-built maps

 

I also think thats only working idea for Sloth. Areas dont fit good into coordinates system, since we have alot of intersections, portals and other area entrances.

</div>

<div class="post" data-post-id="38004" data-author="Gorka" data-date="2017-01-29T07:46:02+00:00" data-subject="Re: Mudlet 3.0.0-delta Mapper">

I'm not sure it's practical to share the mudlet map data from client to client, although I haven't tried. I did open one of the map data files to see it was in a binary format. I also suspect it's format might change from version to version. However I do think the XML idea is better, as this information could be used to generate map data for any client. 

What I would need Teker is a test area export. Just a simple area for now to test the concept on... something like this...

AREA <NAME>, <ID>

ROOM <VNUM>, <NAME>, <TERRAIN>, <N>, <E>, <S>, <W>, <U>, <D>, <X>, <Y>, <Z>

The idea would be to open this XML area file, and change the X,Y,Z data manually. Then write a LUA script to import the XML and generate the mudlet map from that data. The lua script could become distributable with the area file XML so mudlet users could import and create maps for any areas they choose. At some point we could talk about handling the tricky stuff like, trig traps and doors etc. But best to keep it simple for now.

</div>

<div class="post" data-post-id="38006" data-author="*juggleblood*" data-date="2017-01-30T14:47:50+00:00" data-subject="Re: Mudlet 3.0.0-delta Mapper">

I don't believe it's possible to automatically generate these maps for export. 

The way you sposed to do it, is to build the map by exploring the area and then pulling and extending lines manually until it makes sense, then save it.  You'll never get around the issue that space is not equally represented per room. I don't even like calling these 'collisions', because in my mind they aren't any kind of problem, but just the normal dynamic. 

If you get the mapper working to the point that people can start making and sharing such maps, then your mission would be complete.  I think trying to design something that can automatically detect and adjust for the differences in scale would be incredibly hard, not to cast doubts on anyone's talents.

</div>

<div class="post" data-post-id="38007" data-author="Gorka" data-date="2017-01-30T16:29:12+00:00" data-subject="Re: Mudlet 3.0.0-delta Mapper">

> ***juggleblood* wrote:**
> If you get the mapper working to the point that people can start making and sharing such maps, then your mission would be complete.

As with my last post about the coliseum, I went at length to describe a coliseum system that was expandable, modular and maintainable. Likewise this time, in regards to mapping, we know that mudlet is subject to change (they just changed all the mapping stuff after version delta), we need a solution that is not just for the mudlet client, and we need a solution that can be shared. XML room data and manual coordinates solves that.

I know your not a programmer JB and that's fine, you've done remarkably well to master MUDL without that background, but some of us spend our professional lives fixing other people's bad ideas. It's not that there ideas were not solutions, it just that there ideas were poorly constructed and led to projects needing 3-4x as much maintenance time after they were implemented, than the time it took to write them in the first place. Knowing a programming languages syntax does not make people good programmers, just like being able to play an instrument means you make good music. 

The difference between what you are calling a solution, and the XML idea is that the XML idea proposed by Teker is a "programmers solution." It can work if mudlet changes, it can work if sloth changes. I don't believe releasing a working mudlet mapper is a good solution, and I believe all I will get is hours and hours of trying to help people use it afterwards if I did. If we did this right with a 3rd party exchange language such as XML we would have most bases covered for our future. The manual coordinates for rooms that get generated would need to be manually put into the XML files in the distribution. Any area added to sloth afterwards could have it's basic data extracted, and anyone using any client could build that into a usable map for whatever version of any program is the best at the time, with or without the people who originally created any part of the software. This is a true solution.

</div>

<div class="post" data-post-id="38008" data-author="*juggleblood*" data-date="2017-01-30T20:29:33+00:00" data-subject="Re: Mudlet 3.0.0-delta Mapper">

So you are telling me that this thing will be able to generate the maps based on the data alone, without human intervention?  How are you going to tell it what to do with different scales (what you call room collision) and how are you going to tell it to deal with areas like Hellwell and Spire, where you travel up and down on a slant. And then how is it going to cope with special exits? Currently there are a number of ways that a player can teleport, such as an old style trig trap, mob proc, obj proc, or room proc.

The way I see it, every map is going to require a human to help generate it, so why not get some basic tools out there?

</div>

<div class="post" data-post-id="38011" data-author="Gorka" data-date="2017-01-31T00:45:21+00:00" data-subject="Re: Mudlet 3.0.0-delta Mapper">

I think any decision a human can make in regards to mapping an area, a program could be programmed to make in the same way. But it would be difficult and probably not worth the effort... yes I think a few areas would be extremely difficult and not worth the time to try and program rules for, but I still think it's possible.

Regarding more "simple" collisions like I mentioned in an area like BH town, it would not be to hard to avoid collisions. Essentially N/S,W/E all act as an axis. It would be possible for a program to grab all the information and draw the rooms into lines that run on a single axis North/South and West/East, then combine these lines together. Where ever the opposite axis does not match - calculate the collision and extend the axis to compensate and add in the extra rooms. There is nearly always a way, if we can think it, we can do it... is it worth it, no it probably isn't. Hence as Teker said originally, the coordinates would need to be put in manually, although it could probably automate the most part of it first so there is less to fix up.

</div>

<div class="post" data-post-id="38012" data-author="*teker*" data-date="2017-01-31T15:05:18+00:00" data-subject="Re: Mudlet 3.0.0-delta Mapper">

I'll try to spend some time over the next two weeks on the following:

1) Getting a base Mudlet package together that includes non-UI elements: triggers, aliases, scripts, etc based on the replies to my previous Sloth Client thread.

2) Updating the MSDP room vnum more frequently.

3) Exporting BH in a format that can be loaded easily by Mudlet.

We'll see where we get from there.

</div>

<div class="post" data-post-id="38013" data-author="Filk" data-date="2017-01-31T17:07:54+00:00" data-subject="Re: Mudlet 3.0.0-delta Mapper">

While i dont have anything against more frequent vrum updates on msdp, it could be hard to do that probably, while keeping the same server running speed and eliminating wrong vrum chance.

So i still offer to think about vrum number in room description. Thats easy solution that dont break anything. Could be regulated by separate ingame setting, so only visible by ppl who want it.

I think exits line, room name line, or even another separate line after exits could do the same job as msdp. Without such troubles.

</div>

<div class="post" data-post-id="38014" data-author="*teker*" data-date="2017-01-31T19:27:29+00:00" data-subject="Re: Mudlet 3.0.0-delta Mapper">

Ok, I'll look at putting it after the description and making it toggle-able.

</div>

<div class="post" data-post-id="38015" data-author="*juggleblood*" data-date="2017-02-01T00:33:47+00:00" data-subject="Re: Mudlet 3.0.0-delta Mapper">

I'm really excited by this. That is great idea Fluffy about vnum. It will help a lot to have accurate vnum info.

Teker is there a central teleport function, which could trigger a msdp room vnum update? I know currently all the variables spit out on a timer, but how hard would it be to have it update when it changes, i.e. when player teleports (i.e. tranfers via any method)?

</div>

<div class="post" data-post-id="38016" data-author="Gorka" data-date="2017-02-01T09:28:49+00:00" data-subject="Re: Mudlet 3.0.0-delta Mapper">

I did think of Fluffy's idea as well... and It would work in most cases... however there are cases in slothmud with trig traps etc where you move a room and the room description is not shown... you have to "look" to get it. I guess this is why JB is asking about the central function for room changes, would there need to be a forced "look" in that function just to make the process smoother so that the VNUM can be extracted for sure in every room change?

For the client to pick it up could you make sure it's easily triggered and safely?.... something like [VNUM:xxx] Nothing else in slothmud should fire that trigger apart from what we need it too.

</div>

<div class="post" data-post-id="38017" data-author="Filk" data-date="2017-02-01T11:54:12+00:00" data-subject="Re: Mudlet 3.0.0-delta Mapper">

Personally for me, i think such silient teleport is a mistake. Each room changing should have same logic. So automatical looking after any silient teleport isnt that bad idea imo. Wonder if it could be done via mudl. 

Probably not so many of such places. They could be reported and eventually fixed, if fix is easy.

Anyway, while building the map, it could be a problem requiring manual map correction. 

But if moving on already created map, doent seem as big issue, since position will be fixed on next room description.

</div>

<div class="post" data-post-id="38018" data-author="*juggleblood*" data-date="2017-02-01T13:21:56+00:00" data-subject="Re: Mudlet 3.0.0-delta Mapper">

Yeah, it's easy enuff to make sure there are looks after special teleports. I was thinking that an invisible msdp room vnum is preferable to displaying it, if such is possible. If there is no central function tho, then displaying it is a great option.

</div>

<div class="post" data-post-id="38019" data-author="Gorka" data-date="2017-02-01T13:41:28+00:00" data-subject="Re: Mudlet 3.0.0-delta Mapper">

Off topic, but given splork's anxiety about displaying damage as part of the game, could they invisibly msdp it instead?  :twisted:

</div>

<div class="post" data-post-id="38020" data-author="*teker*" data-date="2017-02-01T16:24:13+00:00" data-subject="Re: Mudlet 3.0.0-delta Mapper">

I'm thinking that perhaps the room vnum should appear at the top of the "look" data in case clients want to capture more information.  Something like:

> **Quote:**
> Room Vnum: 8000
> 
> West Gate
> 
>    This is the west gate of the port city of Bal Harbor.  A wide dirt
> 
> roadway leads in between a pair of squarish-looking guard towers into the
> 
> city to the east, and to west disappears into a flat grassy plain.  Visible
> 
> to the far west is what appears to be a forest or jungle that rims the
> 
> entire western horizon.  To the east, the roadway can be seen to lead into
> 
> a distant town square.
> 
> Exits: East  West  Up

It seems like that would allow clients to grab the vnum and then the title, description, and exits if desired.  Does that work?  Does it really help you guys to have brackets and such around the values?

> **Quote:**
> Teker is there a central teleport function, which could trigger a msdp room vnum update? I know currently all the variables spit out on a timer, but how hard would it be to have it update when it changes, i.e. when player teleports (i.e. tranfers via any method)?

There is a function for adding a player/mobile to a room where it would make sense to refresh that information in MSDP.  I'm barely familiar with MSDP but I can look into it further to see if I could add something that doesn't break the clients.  I don't like the current structure of the MSDP data - I would prefer that we send down tables of data instead of lots of little pieces.  Instead of having ROOM_VNUM and ROOM_NAME, for example, we would have a single table called ROOM that would contain both values (and probably more).  Similar to how the GROUP table works now.

There will be a couple of text changes coming in the next reboot (not today's) to help in syncing the client.

1) After entering a correct password:

Old: Password accepted.  Press return to continue...

New: Welcome back [Character Name]!  Press return to continue...

2) After creating a new character:

Old: New character creation complete!

New: New character creation complete!  Welcome [Character_Name]!

These will allow us to get the character name ahead of time so that we can load character specific settings into the client.

3) When attempting to cast a spell that we don't know.

Old: Sorry, you can't do that.

New: Sorry, you don't know how to [cast|play|sing] '[spell/song name]'.

This will allow for the client to notify the group if the player can't cast 'visage' or other spells requested by the leader.

> **Quote:**
> Off topic, but given splork's anxiety about displaying damage as part of the game, could they invisibly msdp it instead?

We've discussed allowing players to see this data in some form but I don't think any progress has been made in that direction.  I'll see if I can remove an obstacle or two.

</div>

<div class="post" data-post-id="38021" data-author="Gorka" data-date="2017-02-01T17:10:50+00:00" data-subject="Re: Mudlet 3.0.0-delta Mapper">

> **Quote:**
> Room Vnum: 8000

That will work... as long as it is unique was all I was asking for, I doubt any room descriptions have "Room Vnum:" in them. Just check it's not the name of next new epic... VnumVnumkpa

</div>

<div class="post" data-post-id="38022" data-author="Filk" data-date="2017-02-01T17:45:38+00:00" data-subject="Re: Mudlet 3.0.0-delta Mapper">

I would prefer it within room name.

Like: 

West Gate [id:1234]

West Gate **1234

Just to avoid another line, since it adds little spam :)

But any variant works, since i could gag anything i dont want to see.

</div>

<div class="post" data-post-id="38023" data-author="*teker*" data-date="2017-02-01T22:45:56+00:00" data-subject="Re: Mudlet 3.0.0-delta Mapper">

> **Quote:**
> West Gate [id:1234]

I was thinking that long term it might be beneficial to do similar things with items - how would you match against this?  Originally I was thinking:

> **Quote:**
> Room Vnum: 8000: West Gate

since that would be searchable by Room Vnum at the start of the line.  Is that easy enough for all of you to parse?  In Mudlet as a Perl RegEx it'd be "^Room Vnum: (.*): (.*)$" to put the vnum in matches[2] and the room name in matches[3].

I did some playing around with MSDP and I have created a new variable (next reboot) called LOCATION that will send data in a structure that looks like this:

LOCATION

- CONTINENT

- - VNUM

- - NAME

- ZONE

- - VNUM

- - NAME

- ROOM

- - VNUM

- - NAME

It gets updated every time a player is placed into a room so I think it should be fairly accurate.

</div>

<div class="post" data-post-id="38024" data-author="Filk" data-date="2017-02-02T02:27:54+00:00" data-subject="Re: Mudlet 3.0.0-delta Mapper">

In terms of parsing, no big difference where specific text pattern will be placed, at start of the line or end. So putting it in end least eye breaking probably.

But well, if msdp value will be acurate enough, then maybe ingame displaying not necessary. Though trigger for detect room changing will be way easier with vnum on the screen. 

Not sure, why you want vnum displaying for items tbh. I dont see any real purpose in it. All things you want to do with items automaticaly, could be done with their names probably. At least i never met situation where i needed that value ingame.

</div>

<div class="post" data-post-id="38025" data-author="*juggleblood*" data-date="2017-02-02T13:01:15+00:00" data-subject="Re: Mudlet 3.0.0-delta Mapper">

This is just my 2 cents but I like:

Room 8000: West Gate

I don't see a need to put the word 'vnum' or a need for 2 colons. To me the word vnum is technical jargon and makes it even worse that we are displaying the room vnum. And I def agree with Filk that we don't want an extra line.

**And WOW, I can't believe you made that msdp room table that updates on room change already! You rock!

**

If you made that, do we even need an option to display room vnum?

</div>

<div class="post" data-post-id="38026" data-author="Gorka" data-date="2017-02-02T14:54:45+00:00" data-subject="Re: Mudlet 3.0.0-delta Mapper">

You could try using the MSDP table first. A single speedrun to another area echoing the room vnum and you will find out how functional using msdp will be. I doubt it will work, msdp just doesn't update fast enough. Having the number in the room description is "bomb proof." MSDP good for some things, not for others. It's a case of using the best tool for the right job.

</div>

<div class="post" data-post-id="38027" data-author="*teker*" data-date="2017-02-02T20:04:29+00:00" data-subject="Re: Mudlet 3.0.0-delta Mapper">

> **Quote:**
> Room 8000: West Gate

I like that also.

> **Quote:**
> I doubt it will work, msdp just doesn't update fast enough.

I'm optimistic that this new method will work better.  It's should be sending the MSDP info right after the room name/description show (or even if they don't show on teleport).  Since you can currently run 2 rooms between the MSDP updates (or more if falling), I can see how it would get out of sync.

> **Quote:**
> Not sure, why you want vnum displaying for items tbh.

At some point it'd be nice to be able to tell if there's a difference between a gray gemstone shard and another gray gemstone shard.  Or other items that can be forged/enchanted but don't change names.  And if we were to import the EQList into Mudlet (like I know some of you have) you would be able to pull correct stats on the items you're seeing.

</div>

<div class="post" data-post-id="38029" data-author="Filk" data-date="2017-02-04T14:28:11+00:00" data-subject="Re: Mudlet 3.0.0-delta Mapper">

Checked new location update. Its funny actually. Now its so fast, that its update even before you actually enter the room  :lol: 

Any pretyped moving do the same. Game counts you in some room along your pretyped moving, before sending you data about current room.

```
Rose Bush
Exits: East  South  West  * Rose Bush[89314]
<907hp 1101ma 351mv>
e
e

Magnolia
Exits: East  South  West * Lower Path[89310]

<907hp 1101ma 352mv>

Lower Path
Exits: North  West  * Lower Path[89310]
```

So it should be fixed to update self only after data about room entering was sent to player.

Or we will be reverted back to idea of direct ingame room displaying :)

Update1:

Often value of location is incorrect. Sending some golsland room, always the same one. Dont see logic when that happens yet.

CONTINENT: VNUM=0, NAME=Godsland

ZONE: VNUM=0, NAME=Godsland

ROOM: VNUM=2, NAME=Transmutation Storage Room

</div>

<div class="post" data-post-id="38030" data-author="*Breeze*" data-date="2017-02-04T21:46:35+00:00" data-subject="Re: Mudlet 3.0.0-delta Mapper">

those 2 rooms are the void and where your real body goes when you shapeshift.

</div>

<div class="post" data-post-id="38033" data-author="Filk" data-date="2017-02-05T04:30:37+00:00" data-subject="Re: Mudlet 3.0.0-delta Mapper">

Ok. Seems correct.

Transmutation Storage Room appears after i kill any mob while shifted. And last until i move out from the room. No matter what i do in the room after the kill - shift back, shift again, any other actions - transmutation room persists. 

After any movement location is correct again, even if i still shifted.

Not happens after each kill, but quite often and stable. Maybe 1/3-1/2 of kills or near so leads to that situation.

</div>

<div class="post" data-post-id="38034" data-author="*juggleblood*" data-date="2017-02-05T13:38:17+00:00" data-subject="Re: Mudlet 3.0.0-delta Mapper">

Maybe there could be a check on the msdp room update such that if the room vnum is one of those 2 rooms, do not update msdp.ROOM?

</div>

<div class="post" data-post-id="38043" data-author="*teker*" data-date="2017-02-06T23:55:16+00:00" data-subject="Re: Mudlet 3.0.0-delta Mapper">

I'll do some more testing and try to figure out how to get around these two issues.

I've attached 3 files in LUA format that contain info about the Sloth world.

- continents.txt is a list of the continents and their vnums

- 18-BalHarborTown.txt is a list of all the rooms and their exits in the zone

- 8-TheDraconisSewers.txt is a list of all the rooms and their exits in the zone

The data is stripped down (no room or exit descriptions, for example).  The rooms seem to have X,Y data in them already but I have no idea how good it is.  I've been loading the data into mudlet from the command line using the command "lua table.load("c:/temp/thenameofthefile.txt", nil)".  This creates a variable called World and put the data underneath it.  Right now it seems to delete the old data that's in there.

Let me know if you guys have any luck building maps from these and we can consider moving forward with more.

</div>

<div class="post" data-post-id="38046" data-author="Gorka" data-date="2017-02-07T12:15:06+00:00" data-subject="Re: Mudlet 3.0.0-delta Mapper">

Well done Teker! 

I've modified my mudlet mapper code to suck in Teker's data... I generated the rooms and exits... and I have this to show you guys...

Untitled.jpg

I am situated in BH Auction, look for the red line. I used the supplied X,Y coordinates to make this and they actually mostly work... mudlet mapper also requires a Z coordinate but I supplied that myself.

Hmm, where do we go from here Teker?

</div>

<div class="post" data-post-id="38047" data-author="Gorka" data-date="2017-02-07T13:02:20+00:00" data-subject="Re: Mudlet 3.0.0-delta Mapper">

Here are my thoughts...

Slothmud rooms should supply a correct X,Y,Z in the context of their area/zone. If they did, generating an area map from one of Teker's LUA dumps would be possible, and would not be mud client dependent as the maps would be built from data actually stored in sloths area files.

Currently the room data only has an X,Y... to be honest I feel it needs a Z as well. 

Some area files probably won't need changes... a lot of others will possibly need manual X,Y,Z coordinates supplied to fix the room and make the maps look right.

I'd be happy to go through areas one at a time and fix them, in my own time, but would need to be empowered to do so, and it would be good if some other people volunteered also. Perhaps a command could be made and assigned to certain players that would allow then to set X,Y,Z for a room, this would empower more people to do the job instead of a few immortals changing hundreds of area files.

Most of the "strangeness" of my generated map is directly due to the absence of the Z coordinate that would put those rooms and links on a different level in mudlet mapper, instead of over top.

</div>

<div class="post" data-post-id="38048" data-author="*teker*" data-date="2017-02-07T15:50:53+00:00" data-subject="Re: Mudlet 3.0.0-delta Mapper">

> **Quote:**
> Hmm, where do we go from here Teker?

In the short-term, I'm going to try to get the MSDP LOCATION fixed and get a base package for Mudlet posted on the web site.  I want to get something fairly simple out that we can test for new players.  My hope is that having a package with group related triggers will make it easier for groups to take on new players and make it more likely those new players will stick around.

Then I'll start looking at the mapper module.  Since there's no Z information in the files or database, I'll have to see how complicated that would be to create and maintain.  I can create a command to update the coordinate information once it's ready to store.  Then it's probably going to be a lot of manual work to go through and clean the data.

</div>

<div class="post" data-post-id="38049" data-author="Gorka" data-date="2017-02-07T16:26:19+00:00" data-subject="Re: Mudlet 3.0.0-delta Mapper">

Awesome!

Cleaning data... never a nice job, no one wants to do it, but once it's done... obstacle cleared, feature unlocked and it's all worth it. 

Good luck trying to get millennials to stick with sloth.

</div>

<div class="post" data-post-id="38060" data-author="*teker*" data-date="2017-02-13T18:37:18+00:00" data-subject="Re: Mudlet 3.0.0-delta Mapper">

Let me know if the MSDP changes are working better now.

</div>

<div class="post" data-post-id="38061" data-author="Gorka" data-date="2017-02-13T21:05:43+00:00" data-subject="Re: Mudlet 3.0.0-delta Mapper">

Almost perfect... I ran to castle echoing the msdp.LOCATION.ROOM.NAME, in a couple of cases the name of the room gets echoed before the room has changed.

An Old WallThe Wall

An Old Wall

   A castle's moat leaves only a narrow strip of dry land at the foot of 

the stronghold's outer wall.  The wall is made of grey stones which used to 

be polished.  Now the shiny surface is marred by many cracks and cuts, none 

of them deep enough to be used as a handhold.

Exits: East  West  

(Blue Aura) A squire travels the corridors, at ease for the first time in his young life.

<1220hp 552ma 316mv 29650213585xp -0.5ac -%>

The Wall

   The outer wall of a fortified castle and its moat leave only a narrow 

space between them.  That wall is at least thirty feet high, made of great 

blocks of grey stone.  The cracks between the stones are pencil-line thin, 

such a perfect fitting that it never required mortar.

Exits: East  West  

(Blue Aura) A squire travels the corridors, at ease for the first time in his young life.

</div>
