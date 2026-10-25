---
title: "A few WinTin Tips for Total Beginners"
topic_id: 1747
author: "*juggleblood*"
date: 2006-02-22T09:29:30+00:00
last_activity: 2008-10-16T11:33:26+00:00
last_author: "Archive_M"
sticky: false
locked: false
post_count: 5
---

<div class="post" data-post-id="10834" data-author="*juggleblood*" data-date="2006-02-22T09:29:30+00:00">

[u:3rl2gnkd]ClearQueue Command in Aliases[/u:3rl2gnkd]

The command '|' in Sloth clears your command queue. This command can save your life.

For example:

You are fighting a kobold.

   You enter the 'kick' command several times.

   The kobold is about to kill you. You want to flee.

   You type 'flee'.

   Instead of fleeing, you kick the kobold and it kills you.

But, had you typed '|' and then 'flee'

   The mud would have known that you wanted to forget all about the 

   kick that you entered. And you would have fled.

Here are some simple aliases using the '|' command.

  #alias {fl} {|;flee}

  #alias {cureme} {|;cast 'cure light' myname}

  #alias {rr} {|;recite recall}

[u:3rl2gnkd]Anchoring Your Triggers[/u:3rl2gnkd]

You should anchor your triggers (actions) as much as possible. 

 For example:

       Someone gossips 'You are hungry'

       Your trigger goes off and you try to eat.

       This means your trigger was not anchored.

Putting the symbol '^' in front of the trigger part of the action will anchor it.

    

Like this:

   #action {^You are hungry.}{get food pack;eat food;burp}

Now the action will only occur, if the words "You are hungry" appear at the very beginning the of the line. In other words, the trigger will not go off by accident.

[u:3rl2gnkd]Single Action Triggers[/u:3rl2gnkd]

Sometimes you only want a trigger to go off once.

The way to do this is put {O} (capital letter o, not zero) at the end of the action.

like this: #action {^You are hungry}{eat food}{O}

Usually with single trigger Actions you will want to make an alias that sets the trigger anytime you want.

For example, you want to sit your character at Sork to wait for the Crimson Dragon. But you want to take a toilet break while your waiting on it. You can set a single action trigger that will make you get on the dragon, and then get off when it arrives. The trigger will then turn itself off, so that you don't get on the dragon by mistake the next time you are in the room.

Try this:

#alias {trigcrimson}{#action {^A Crimson Dragon}{enter crimson;rest}{O}}

Now, if you want to go to the toilet while waiting for the Crimson Dragon, you just buy a ticket, go to the departure spot, and type trigcrimson.

You can make a permanent action that makes you stand and exit upon arrival, since you will almost never want to stay on.

Cheers

</div>

<div class="post" data-post-id="10871" data-author="Malrin" data-date="2006-02-23T22:59:55+00:00">

Thanks for the information.

It's the first thing i read that actualy helps me understand a little how Wintin scripting might work.

I know a little basic, a little assembly, a little Turbo Pascal, a little Dbase, a little about .bat files, a little VBA, a little C++ and a little of some other forms of programming. I got that from here and there, in school, in help files, from asking people, but i haven't fully mastered any of those.

I'd like to know if anyone has a link that could get me the information i need to start learning enough to be able to write my own scripts for Wintin and to understand the scripts that i come across.

BTW, not new to computers, internet and chatting, but i'm new to Mudding.

</div>

<div class="post" data-post-id="10873" data-author="Avatar" data-date="2006-02-23T23:59:42+00:00">

Well, if you understand some basics (if...then statements, loops, setting variables, etc) those are good building blocks.  There are endless web pages describing scripting and beginner programming tips, but it sounds like you have a good general grasp of those.  The important thing then seems to be 2 parts:

A)  find a reference that shows how to apply those basic commands using the client you intend to use

B)  understand how your client interacts with the mud ... for example how does it capture and compare incoming text, how do you send commands back to the mud (from a script)

Maybe I'll take an opportunity to mention two other points, not scripting specific but etiquette in general.  One important client command to learn is how do you send informative messages to yourself without necessarily grouptelling them to everyone in the group.  That's a key because a lot of new users will code informative messages about every little trigger they turn on and off.  Really, the rest of the group maybe doesn't need to see the results of your "automatic eat food" action, and too many of those messages can annoy people pretty quickly.

A second key point is related, but it is good to add methods to toggle triggers on and off.  Many clients have groups that you can use to enable/disable sets of triggers at once.  Again, I'll give an example, it's a common script to grouptell status messages certain actions or spells.  When a mob is blinded, your char might grouptell "look at that, the target can't see!" or when your sanc falls, your character might grouptell "Uh oh!  My glow has bit the dust!!"  Well, these messages can be quite useful.  The problem is that in a group of 12 people there may be 8 that can report on each of these little status messages.  That could mean that every time a mob is blinded there are 8 grouptells about it being blinded, and when a run ends there may be 8 people grouptelling about their lights falling.  That's a lot of spam and again can annoy people pretty quickly.  Rather than that, you could add a toggle to your actions so you can turn them on and off at your whim.

It's been a while since I did anything in Wintin specifically, but you could set a variable, for example called "output" and use that variable in your informative messages.  Wintin might be something like this:

bad version:

#action {^The white aura around your body fades.} {grouptell Argh! Lite fell!!}

better version:

#action {^The white aura around your body fades.} {$$output Argh! Lite fell!!}

#alias {onsancmsg} {#var {report} {grouptell}}

#alias {offsancmsg} {#var {report} {#showme}}

Now you could toggle that automatic grouptell either on or off depending on your needs.  As a next step, you might consider turning it on and off along with your reporter.  Most tanks have a reporter that they can turn on to grouptell their current hps each time they get hit.  The tanks are really the only member of the group that needs to be sending grouptells about the status of their sanc spell, so turning it on when the reporter is enabled and off when the reporter is disabled seems like a natural fit.

I hope that code would work like expected, again it's been awhile!  I realize this isn't specifically what you asked for, but hopefully it's useful strategy as you start to customize your client.

charles

</div>

<div class="post" data-post-id="10875" data-author="Avatar" data-date="2006-02-24T00:12:43+00:00">

I should read these again before pressing submit.  The improved code should look more like:

better version: 

#action {^The white aura around your body fades.} {$$output Argh! Lite fell!!} 

#alias {onsancmsg} {#var {output} {grouptell}} 

#alias {offsancmsg} {#var {output} {#showme}} 

I mistyped the variable name as "report" because it's one I actually use.  :)  Another tip is to try to pick a standard style for your variables and command names.  In my own example, that "onsancmsg" is maybe understandable as an example but it would be annoying as an actual command alias because it's rather long.  I made that mistake, not this exactly but similar.  Then, because the alias was a bad choice I actually had an easier time remember the variable "report" and I'd set it manually during playtime.  This is nice in some ways, because you could do interesting things on the fly.  If you got silenced and understood how your tank reporter works, you could quickly type:

#var report emote

Then your report messages are sent to the mud using emote, which other people in the room could see even if you were silenced (which disables grouptell, say, etc).

charles

PS.  This may all be too complex.  I guess someone should work on a more basic level introduction...

</div>

<div class="post" data-post-id="26727" data-author="Archive_M" data-date="2008-10-16T11:33:26+00:00">

Excellent information! Now I don't have to die every time I run out of HP and have to ditch the fireballs.

</div>
