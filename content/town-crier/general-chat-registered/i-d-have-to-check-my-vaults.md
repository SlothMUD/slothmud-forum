---
title: "I'd have to check my vaults..."
topic_id: 4806
author: "Gorka"
date: 2017-12-04T16:30:07+00:00
last_activity: 2017-12-06T15:11:49+00:00
last_author: "*Breeze*"
sticky: false
locked: false
post_count: 5
---

<div class="post" data-post-id="38518" data-author="Gorka" data-date="2017-12-04T16:30:07+00:00">

We have all had it happen when trading with other players for gems and cps that we have had to check our vaults to find something. With the new vault code and vaults now storing 100 items, the management of vaults is becoming an issue. I have at least 500 vault slots, but I know other players have more. I also have vaults on every continent except island (for the moment) which means relo'ing around every continent to try and find something. I've tried to organize my crap into gem/personal/cp vaults but still having issues.

I wondered if a new command could be implemented to give us a reading of the contents of all our vaults... perhaps in a format, that's easily copied to excel for sorting. Currently the slot number being the first item on the current "list" command doesn't help when copying data to excel for sorting.

Suggested format would be something like this...

ITEM NAME, ITEM TYPE, VAULT SLOT, ROOM NUM, PERSONAL, TEMP

This command could literally save players hours of sorting out large lists of items and compiling lists of unfinished forges and trading lists. You could argue that this is not a very sloth command, to get knowledge of stuff in room that you are not presently in... well neither is the who list... Whats to say whenever I type list this grand list isn't updated by the character in our virtual world... surely this would be prudent?

Just an idea, but honestly it would save us hours sometimes... An it's really just a for loop and an echo from our player files to do it.

GIMME A G! if you're a player and feel this would help you a lot...

</div>

<div class="post" data-post-id="38519" data-author="*Splork*" data-date="2017-12-04T23:52:34+00:00">

I could of sworn we had added that information to the webpage login?

Vaults are SQL driven, it should be rather easy to add that information to a command in-game or here...

</div>

<div class="post" data-post-id="38520" data-author="Gorka" data-date="2017-12-05T12:08:59+00:00">

Yeah, there is a button for vaults on the website. I've tried to get that and the quest one working in the past to no avail. When I logged in it thought I was Zuzu, obviously I am so much better looking... but he is the player with the last name alphabetically so it had some sort of bug. In fact even the player stats was bugged for me. I'm not sure any of it will work with the website being only partially operational now... Hence the request for the in game feature.

</div>

<div class="post" data-post-id="38524" data-author="*Breeze*" data-date="2017-12-05T19:16:59+00:00">

> ***Splork* wrote:**
> I could of sworn we had added that information to the webpage login?
> 
> Vaults are SQL driven, it should be rather easy to add that information to a command in-game or here...

> **Gorka wrote:**
> Yeah, there is a button for vaults on the website. I've tried to get that and the quest one working in the past to no avail. When I logged in it thought I was Zuzu, obviously I am so much better looking... but he is the player with the last name alphabetically so it had some sort of bug. In fact even the player stats was bugged for me. I'm not sure any of it will work with the website being only partially operational now... Hence the request for the in game feature.

aforementioned zuzu/gorka website issues were caused by the "transparent" caching that bluehost used to do.

i didn't bother fixing the website login because of where the website is currently hosted.

vault link on website is/used to be a project i started where i had all the code done and tried to get the players to help design the output (i sent them a test db and the code that reads it etc..). a few people volunteered but no one ever got back to me.

not sure if its linked to the current live vaults but wouldn't be hard to check.

sample ::

```
array(80) {
  [0]=>
  array(5) {
    ["VnumRoom"]=>
    string(5) "76018"
    ["SortOrder"]=>
    string(2) "20"
    ["ItemVnum"]=>
    string(5) "37216"
    ["ItemShortDescription"]=>
    string(28) "the Shield of the Rainmaster"
    ["ItemName"]=>
    string(31) "shield rainmaster rain umbrella"
  }
  [1]=>
  array(5) {
    ["VnumRoom"]=>
    string(5) "76018"
    ["SortOrder"]=>
    string(2) "19"
    ["ItemVnum"]=>
    string(5) "84229"
    ["ItemShortDescription"]=>
    string(21) "a wand of quicksilver"
    ["ItemName"]=>
    string(29) "wand quick silver quicksilver"
  }
  [2]=>
  array(5) {
    ["VnumRoom"]=>
    string(5) "76018"
    ["SortOrder"]=>
    string(2) "17"
    ["ItemVnum"]=>
    string(5) "49281"
    ["ItemShortDescription"]=>
    string(25) "a purple minidemon brooch"
    ["ItemName"]=>
    string(29) "brooch purple minidemon demon"
  }

.. etc ..

Vault # 76018 
20) the Shield of the Rainmaster
19) a wand of quicksilver
17) a purple minidemon brooch
16) a strange story
13) a great shield of flame
12) a keg of Dragon's breath beer
11) a blue egg
10) a bottle of hatred
9) a prison guard helmet
8) a heavy greatshield
7) an electrum cuirass
6) an ivory scarab
5) a suit of glowing, diamond-encrusted platemail
4) a suit of glowing, diamond-encrusted platemail
3) a mithril pentagram
2) a pair of granite sleeves
1) shield of the black rose
```

</div>

<div class="post" data-post-id="38526" data-author="*Breeze*" data-date="2017-12-06T15:11:49+00:00">

just checked.  it is linked to new vaults.

```
Vault # 76018 
>snip<
21) An uninitialized Shimmering Crystal Token
```

</div>
