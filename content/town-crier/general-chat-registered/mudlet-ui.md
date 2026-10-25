---
title: "Mudlet UI"
topic_id: 4136
author: "dimiric"
date: 2013-10-23T13:36:18+00:00
last_activity: 2013-10-25T15:33:10+00:00
last_author: "Tuck"
sticky: false
locked: false
post_count: 3
---

<div class="post" data-post-id="34506" data-author="dimiric" data-date="2013-10-23T13:36:18+00:00">

Hi everyone,

I'm just starting to play around with LUA so I began to work on creating my own UI.  I identified a few things that I want to try to do, but I am having all sorts of trouble figuring out a way to do them and would like some help.  It all started with the spell affects on a character.  I saw that although it doesn't appear officially in the "HELP MSDP" list, there is a variable being pushed to the clients called atcp.MSDPAFFECTS and it contains a mish-mash of active spell affects.

atcp.MSDPAFFECTS.png
Score says

You are affected by the following spells:

   Resist Electricity               

   Resist Acid                      

   Armor                            

   Bless

As you can see, it shows item-generated instead of Resist Electricity or Resist Acid.  Not to mention dupes for each of those, and also bless.  And even something for the class.  Not completely useful, but it does show the timer left on the affect too.  (And shouldn't it be "EFFECT"?)

So what I was thinking of doing was creating a timer that would send score to the mud, gag the response, but also collect it to a table or variable, and then parse it to find the item generated spells and put those in my UI as icons, similar to WoW and EQ once did when I played those years ago.  What are your thoughts?  Also, what regex code would be used to grab an entire line, not just a word?

</div>

<div class="post" data-post-id="34509" data-author="*Splork*" data-date="2013-10-24T12:26:28+00:00">

Mudlet 3.0 will have native MSDP support and will hopefully deal with parsing the tables and arrays correctly(ie affects and exits). 

Keep an eye out for their next release,

Splork

</div>

<div class="post" data-post-id="34513" data-author="Tuck" data-date="2013-10-25T15:33:10+00:00">

We mortals have discovered 2 un-official sloth msdp vars, like EXITS and AFFECTS.

They are using some strange layout and can't be parsed by client like other MSDP vars. 

In [that](http://www.slothmud.org/forum/viewtopic.php?f=28&t=4131) topic Splork said he will look into it.

</div>
