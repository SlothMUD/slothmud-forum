---
title: "targetting for Mushclient"
topic_id: 1374
author: "seshi"
date: 2005-07-24T12:24:22+00:00
last_activity: 2005-07-24T12:24:22+00:00
last_author: "seshi"
sticky: false
locked: false
post_count: 1
---

<div class="post" data-post-id="7976" data-author="seshi" data-date="2005-07-24T12:24:22+00:00">

Targeting for Mushclient

I have found the mushclient help to be very comprehensive but not always easy to follow. I have written what I hope is an easy to follow guide for implementing targeting and some other triggers and aliases useful for grouping. Please let me know if you find this useful and if there is anything I can add or make clearer. A big thank you to my friends who patiently helped me test this out and who offered suggestions.

Targetting

The aim is to have an alias that changes automatically when the leader changes the target. 

make 2 variables:

name : leader

contents: leave blank

name : target

contents: leave blank

Make 2 triggers

Trigger: @leader * 'target *'

Send: %2

Send to: Variable

At bottom of screen enter target in box Variable

Trigger:You now follow *.

Send: %1

Send to: Variable 

At bottom of screen enter leader in box Variable

for both triggers: 

Tick enabled, ignore case and expand variables in menu on left-hand side.

Aliases

make an alias, for example:

Alias: as

Send: assist @leader

Send To:World

or 

Alias: cu

Send: cast 'curse' @target

Send To: World

Ensure that in the left-hand side menu Enabled and expand Variables are ticked

Ok Now when you follow a new leader any aliases with @leader are automatically updated with leaders name and any aliases with @target will automatically target the mob    announced by the leader (and only the leader)

Other suggestions to make grouping easier

Make a trigger to respond to leaders order 'all up'

Trigger: @leader -- 'all up'

Send: Wake

          Stand

Make a variable 'tank' for bigger groups when leader and tank are different and set up an alias to change the variable when leader announces who is the tank. Being a cleric I have also made aliases (and macros) to heal leader and tank.

Hope this is helpful 

Salan

</div>
