---
title: "DarkArts"
topic_id: 4171
author: "DarkArtist"
date: 2013-12-15T17:23:26+00:00
last_activity: 2013-12-28T19:09:30+00:00
last_author: "DarkArtist"
sticky: false
locked: false
post_count: 11
---

<div class="post" data-post-id="34635" data-author="DarkArtist" data-date="2013-12-15T17:23:26+00:00" data-subject="DarkArts">

I deleted my post about food pickup (multiline trigger example), and just made this post as a catchall sandbox for mudlet banter.

I've worked out some protocols for automated route finding and I've found it's kind of a fun hobby to print out slothmaps and see how much of the map you can route in as few statements as possible.

For example if you wanted to explore every room in Ice City minus the ups on a circular route the algorithm would be a timer (seconds, timername)

if roomNumber=startRoomNumber then heading="North" 

if canRight() Right() else if canForward() Forward() else if canLeft() Left() else if canBack Back() else disableTimer("Ice City") end

That's it. The thing would wander around thru every room one by one forever and never get lost. Then you can put in your various triggers for exceptions to the rule.  You trace out the route with your finger and find where the pattern breaks down or falls into a circular loop. Then you add a trigger to say:

if roomNumber==8000 and heading="West" then E(). For example this would keep you from heading west from bal harbor west gate. Room numbers are available from MSDPROOM_NUMBER.

The fun part I think would be sharing the algorithms themselves, like saying hey I figured out how to patrol the entirety of the demonweb in a hundred words or less..etc.."

Let me know if you're interested in creating / sharing zone algorithms. Pls don't ask for my definitions/functions for the above related material. I figure if you want to use it, u should have to want to know how it works.  Lets do this thing. It's fun!

</div>

<div class="post" data-post-id="34642" data-author="DarkArtist" data-date="2013-12-16T19:58:15+00:00" data-subject="Re: DarkArts">

Ok, got sounds set up on mudlet and it rocks.

Imagine if everyone downloaded the same sound files and setup triggers so they could send sounds in groups.

i.e. you ctalk something like ctalk sound:fail.wav and anyone with the package setup up would hear the wav file with that name (if they have it). You would join the sounds channel if you wanted to receive sounds, so others in the group wouldn't get spammed with grouptells. If you didn't have that sound in your library you just wouldn't hear anything, and you could gag out the actual messages, so you only receive the sound, no spam msg.

Infinite fun possibilities and it's super simple, you just put your sounds in a folder and playSoundFile([[folder\soundname.wav]]). 

Check out the waves at http://www.villagegeek.com/html/wavfiles1.htm for an idea of how awesome this feature could be.

</div>

<div class="post" data-post-id="34644" data-author="DarkArtist" data-date="2013-12-16T23:10:25+00:00" data-subject="Re: DarkArts">

If you don't have enough reasons to get aboard the mudlet train, color functionality is awesome! Have complete control over the color of anything and everything ingame by using the ingame color set feature +mudlet's color trigger functionality. Want room descrips to be DarkOliveGreen? Just set them to white and then trigger white to select the line and set foreground to green.

selectCurrentLine()

fg("DarkOliveGreen")

Too easy.  Or if you're like me and you just dont care to ever see the room description, do a deleteLine() or replace it with a carriage return.  Likewise you could gag out emotes, says, objects or wutever for reducing spam in group play. 

set the color trigger to whatever color you're going to use for that gag and then make an alias to turn it on and off like: 

^gagMost$

gagMost=gagMost or false

if gagMost~=true then gagMost=true else gagMost=false 

And voila, you can peacefully group without seeing room  descrips or people's annoying emotes or talking with mobs or junk on the ground etc.. Way too easy.

</div>

<div class="post" data-post-id="34646" data-author="DarkArtist" data-date="2013-12-17T16:39:33+00:00" data-subject="Re: DarkArts">

**Using multi-line filter triggers Instead of using enableTrigger disableTrigger** :!: 

Let's say you want to put all hedge clippings from your inventory in a bag.

trigger: a few clippings from a hedge --beginning of substring match

or u could do...^a few clippings from a hedge(\s?)(\[?)(\d?)(\d?)(\]?)$ --regex

script: send("put clippings bag")

But now when you look in a container and it contains hedge clippings the trigger will fire.

So we need to tell it to only trigger if the item follows the line "You are carrying:"

One way to do this is to disableTrigger("trigger group name") on "carried:" (means it's a container) and set a tempTimer(2, [[enableTrigger("trigger group name")]] ). Then the trigger for the put should be disabled for two seconds while you receive the container contents.

**However**, it's buggy as hell. The triggers will get stuck in the off position. 

This is pointed out in the mudlet manual:

..trigger chains are a means to automatically enable/disable trigger groups without the hassle of enabling and disabling trigger groups manually. This has 2 important advantages: Chains are faster than conventional solutions and chains reduce the complexity of your scripts and greatly reduce the usual system bugs that inevitably go along with *enable/disable trigger xy function calls as itâ€™s very difficult and** error prone*** to enable and disable your triggers correctly in large complex trigger systems. This is one of the most powerful features in Mudlet and should be used whenever possible.

So to accomplish the same thing with a filter chain:

In some folder (maybe "inventory") make a subfolder "carrying in inventory" now you make the trigger on the folder item itself (not a new item).

trigger: You are carrying (begin of line substring)

script: none

set fire length (the pink box in upper right) to 20 or 30 or so (the number of lines to check for matches following the trigger line)

Now make a new item (not folder) under that subgroup "carrying in inventory" and make a trigger "clippings"

trigger:a few clippings from a hedge (begin of line substring or make it into a regex pattern)

script:send("put clippings bag")

Done. Now only clippings that are in your inventory will trigger a match, not in containers, without the bugs associated with enabling and disabling trigger groups.

You can further chain trigger groups as well. Instead of making the trigger for clippings, you could add another subgroup to further test the trigger. 

For example you could make a trigger than only fires if the item is in your inventory and then only fires if it contains the word dust  and then only fires if it contains the words emerald or diamond and then  places the dust in brewNameBag or whatever. This filter chain would consist of 3 nested trigger groups.

Of course with the large amount of items you'll be handling it would make more sense to make databases and use them within the triggers so that if the item is in inventory and element of wantedCps database, check to see which brew it goes to and put it in the appropriate container. Likewise you can create databases this way to track your inventory, container contents, etc...

But I haven't gotten that far yet. By the way, DONT USE THE MUDLET MANUAL DATABASE EXAMPLES UNTIL YOU INSTALL THE FIX POSTED TO THE MUDLET FORUM BY VASU. IT DOESN'T WORK WITHOUT IT :!:

</div>

<div class="post" data-post-id="34647" data-author="DarkArtist" data-date="2013-12-17T17:50:04+00:00" data-subject="Re: DarkArts">

following that train of thought, here is how to fix database functions in mudlet:

"To fix it, create a new script - before your database-using ones - and put the content of this 

https://raw.github.com/vadi2/mudlet-lua ... lua/DB.lua into it. Restart Mudlet or use resetProfile(), and all examples will work." -Vasu

</div>

<div class="post" data-post-id="34668" data-author="DarkArtist" data-date="2013-12-21T14:43:06+00:00" data-subject="Re: DarkArts">

Can anyone tell me the regex pattern that would mean zero or more additional whole words...i.e. zero or more of (\w+\s)? 

so for instance in:

a blue car

an ugly blue car

a very ugly blue car

matches[2] would be:

"a blue "

"an ugly blue "

"a very ugly blue "

Please and thanks!

</div>

<div class="post" data-post-id="34671" data-author="Akaya" data-date="2013-12-21T16:13:40+00:00" data-subject="Re: DarkArts">

```
(.*?)car$
```

The ? is what you're looking for. It caputres 0 or 1 times. So in our case, if no adjective is given with the car, the pattern will still match.

</div>

<div class="post" data-post-id="34672" data-author="DarkArtist" data-date="2013-12-21T16:33:20+00:00" data-subject="Re: DarkArts">

no because that would match any character.

I want one or more whole words only, i.e beginning with a whitespace or at the begging of the line and ending at the end of the line, without special characters.

I think this would be described as ^(\w+)(\s(\w+)+) but this isn't supported in lua. 

I think the answer has something to do with \b but I haven't gotten it right yet.

</div>

<div class="post" data-post-id="34675" data-author="Akaya" data-date="2013-12-21T17:46:18+00:00" data-subject="Re: DarkArts">

Here's a reference: [http://www.autohotkey.com/docs/misc/RegEx-QuickRef.htm](http://www.autohotkey.com/docs/misc/RegEx-QuickRef.htm)

</div>

<div class="post" data-post-id="34676" data-author="DarkArtist" data-date="2013-12-21T18:10:21+00:00" data-subject="Re: DarkArts">

nice one.

I got it pretty much, just for up to 3 key words:

^a jar of (\w+)\s*(\w*)\s*(\w*)$

so that it would match a jar of oil, a jar of roiling fluid, or a jar of pickled mountain oysters in your inventory and give you the matches.

</div>

<div class="post" data-post-id="34703" data-author="DarkArtist" data-date="2013-12-28T19:09:30+00:00" data-subject="Re: DarkArts">

Here's a handy one for chasing down fleeing mobs.

There's 3 cases for flee. So you make 3 different multi-line triggers.

A. The mob flees and you don't see which direction, just a blank line.

Trigger 0:^.+ panics, and attempts to flee\.$ (regex)

Trigger 1:1 (line spacer)

Trigger 2:return not line:find("leaves") (lua function)

line delta:1

script:

pipe()   --a useful function to define, send("|",false); cecho("<red>|||<reset>")

send("scan")

send("sneak")

B. The mob flees and leaves "direction".

Trigger 0:^.+ panics, and attempts to flee\.$ (regex)

Trigger 1:^.+ leaves (\w+)\.$ (regex)

Trigger 2:return not line:find("arrives") (lua function)

line delta:2

script:

pipe()  

send("sneak")

send(multimatches[2][3])

send("cast 'web' "..target)

C. The mob flees and re-enters the room from the same direction.

Trigger 0:^.+ panics, and attempts to flee\.$ (regex)

Trigger 1:^.+ leaves (\w+)\.$ (regex)

Trigger 2:^.+ arrives from the (\w+)\.$ (regex)

line delta:2

script:

pipe()  

send("cast 'web' "..target)

**this one would be better with checks to make sure its the right mob and direction.

You can also set this up to work without having targeted the mob first by using a pattern which gives you the last word of the short descrip, but the last word of the short isn't always a keyword, the pattern would be:

^((.*)\b(\w+)) panics, and attempts to flee. And the last word of the short here is multimatches[1][4], assuming its the first listed trigger. If you use the feature a lot, you could always make a mob dictionary of short/key name values and send("cast 'web' "..keyName[matches[2]]). I set up a trash dictionary like this that cleans my inventory.

----credit to Mork on the mudlet forum for helping me set this up.

</div>
