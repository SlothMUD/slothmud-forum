---
title: "ship autoexit"
topic_id: 4004
author: "Constin"
date: 2013-01-11T19:03:23+00:00
last_activity: 2013-01-11T21:56:52+00:00
last_author: "Constin"
sticky: false
locked: false
post_count: 2
---

<div class="post" data-post-id="33914" data-author="Constin" data-date="2013-01-11T19:03:23+00:00" data-subject="ship autoexit">

perl regex: ^A (.\*) gracefully lands and folds its wings at (.\*)\\.$

prel regex: ^The ship has arrived at (.\*)\\!$

command:

send("wake")

send("sta")

send("exit")

</div>

<div class="post" data-post-id="33915" data-author="Constin" data-date="2013-01-11T21:56:52+00:00" data-subject="Re: ship autoexit">

some lame extra update for autoenter VK ships to selected destinations

Trigger1:

regexp: ^A (.\*) gracefully lands and folds its wings.$

command:

if shipto == "bh" then send("enter dragon") end

if shipto == "ah" then send("enter blue") end

if shipto == "ss" then send("enter white") end

shipto = "null"

Trigger2:

perl regex: ^A (.\*) gracefully lands and folds its wings at (.\*)\\.$

prel regex: ^The ship has arrived at (.\*)\\!$

command:

send("wake")

send("sta")

send("exit")

shipto = "null"

Alias:

pattern: ^shipto (.+)$

command:

shipto = matches[2]

cecho("\<light\_slate\_blue\>SHIPPING TO: \<red\>"..shipto.."\\n")

\----------------

so now all u need is come to dock type: shipto bh( or ah, or ss) and wait for ship w/o looking at screen.

</div>
