---
title: "Talking Mobs!"
topic_id: 3371
author: "*Splork*"
date: 2010-02-03T03:28:05+00:00
last_activity: 2010-02-08T04:10:27+00:00
last_author: "*Splork*"
sticky: false
locked: false
post_count: 5
---

<div class="post" data-post-id="30809" data-author="*Splork*" data-date="2010-02-03T03:28:05+00:00" data-subject="Talking Mobs!">

We are extremely excited to officially announce phase one of our talking mob code. This code will make mobs respond to players using say, tell, and ask to make statements and questions in plain English.    It works like this:

   1. A player says something aloud in presence of a mob

 usually in the form of a greeting, such as "Hi <mobname>" or "Hey <mobname"

   2. The mob decides if it's being addressed

   3. If yes, the mob translates what the player says to one of a long list of possible things a player might say, like "how are you?" or "where is <person>?".  

4. Custom code generates the best response .  Each question has many logical responses, such as "East", "Never heard of him" or "That's you." 

5. Grammar generator creates a unique phrasing, so the mob might actually say "I think he lives to the east of here." or "I heard he was off to the east." It's quite possible to ask the very same question ten times in a row and get ten different answers.

We have put in some careful checking so that the mob can decide whether you are talking to it or to someone else, so it shouldn't butt into conversations between players.  

     The greatest aspect of this code is that the majority of the information that can be garnered from talking to mobs can be directly used inside of SlothMUD. Currently, new players to our game will get the most out of this feature but we are busy adding  information that our veteran players will be able to use as well. We believe a few shining examples of the usefulness of this can be found in everyday questions that our players hear on gossip, such as â€œwhere can I get some water?â€, or â€œcan I get some food around here?â€ These questions can now be asked to creatures throughout the game and they will helpfully point the way, sometimes even giving you exact directions to the very location you need to travel!

     This feature has been tied to our history database which tracks every mob and playerâ€™s movement throughout the game so questions such as â€œHave you seen Splork?â€ could possibly generate responses such as â€œHe left a few minutes ago.â€  Or â€œHe was just here a second ago.â€  

This project has been in the works for nearly four years, with the initial emails regarding the topic originating on May 9th, 2006. Kjartan spearheaded the idea behind and developed the engine for which it runs on.  The project consists of two separate but equally important parts: the code and the grammar files the code calls upon. This project involved a great deal of Immortal involvement but most notably besides Kjartan were Clink and  Juggleblood on grammar,  and Splork and  Isabo with the code.  

     We have thoroughly tested this feature and it has been on the live machine for nearly three months now, though not widely announced. However, with any project of this magnitude, we do realize there will be some kinks to iron out. Please add any bugs that you may find to the bugs list and we will address them as quickly as possible.  Hopefully, you will find this feature as interesting as we do.

Enjoy,

Splork

</div>

<div class="post" data-post-id="30811" data-author="Tuck" data-date="2010-02-03T11:00:52+00:00" data-subject="">

You tell Elena, Keeper of the Gardens 'who is toxis?'

Elena, Keeper of the Gardens says 'Its an Immortal.'

lol

</div>

<div class="post" data-post-id="30816" data-author="Vixn" data-date="2010-02-04T18:43:04+00:00" data-subject="">

You gave them the ability to speak,

They vote for Toxis being an immortal!!

P.S. Do you think they could pass Turing test?

</div>

<div class="post" data-post-id="30820" data-author="Clink" data-date="2010-02-05T03:30:31+00:00" data-subject="">

Pretty sure I wouldn't pass a Turing test.

</div>

<div class="post" data-post-id="30869" data-author="*Splork*" data-date="2010-02-08T04:10:27+00:00" data-subject="">

Fixed a couple smaller bugs regarding this topic.

On a side note, this code allows our mobs to answer probably upwards of 1000+ sloth related questions.

For instance, the question "where is" can be used to find a player, creature, room name, guilds, etc. 

Anyways, hope you guys are enjoying it and pushing it on the newbies.

Splork

</div>
