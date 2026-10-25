---
title: "Basic Health/Move/Mana and Opponent Health Bars"
topic_id: 4119
author: "Drule"
date: 2013-09-10T11:17:06+00:00
last_activity: 2013-09-12T07:36:36+00:00
last_author: "Akaya"
sticky: false
locked: false
post_count: 4
---

<div class="post" data-post-id="34418" data-author="Drule" data-date="2013-09-10T11:17:06+00:00">

Here are some very basic Hp/Mv/Ma bars and an opponent Hp bar for Mudlet. They are designed to show current/max and update whenever any of the 3 current values change. I'm focusing on very minimal code and my main goal is to understand this stuff as I create it. At any rate, I was glad to finally see some progress and would appreciate any suggestions. Big thanks to Akayan for the MSDP code and other pointers.

In order for this to work the MSDP variables must be turned on and I would highly recommend reading [Akayan's post](http://www.slothmud.org/forum/viewtopic.php?f=39&t=4002) about getting that setup

First, I went into settings and set top and bottom borders to 15 to allow room for my bars w/o overlapping my mud scroll.

Then I created a script (name is not important) to create the gauges that I used to display health/moves/mana and opponent health with the following code:

```
WindowWidth = 0;
WindowHeight = 0;
WindowWidth, WindowHeight = getMainWindowSize();

createGauge("HealthBar", WindowWidth/3, 15, 0, WindowHeight-15, nil, 200, 0, 0)
createGauge("MoveBar", WindowWidth/3, 15, WindowWidth/3, WindowHeight-15, nil, 0, 200, 0)
createGauge("ManaBar", WindowWidth/3, 15, WindowWidth/3*2, WindowHeight-15, nil, 0, 0, 200)

createGauge("OppHealthBar", WindowWidth, 15, 0, 0, nil, 200, 0, 0)
```

Next, I created a script to handle my bar updates, I called this "updatebars" and it was set to go off on the following User Defined Event Handlers:

```
MSDPHEALTH
MSDPMOVEMENT
MSDPMANA
MSDPOPPONENT_HEALTH
```

The code for this script is as follows (pay attention to the function being named the same as the script, again.. thanks to Akayan for explaining how this works):

```
function updatebars()
	setGauge("HealthBar",atcp.MSDPHEALTH,atcp.MSDPHEALTH_MAX)
	echo("HealthBar",[[<p style="font-size:14px"><center><b>]]..atcp.MSDPHEALTH..[[/]]..atcp.MSDPHEALTH_MAX..[[</b></center></p>]])
	setGauge("MoveBar",atcp.MSDPMOVEMENT,atcp.MSDPMOVEMENT_MAX)
	echo("MoveBar",[[<p style="font-size:14px"><center><b>]]..atcp.MSDPMOVEMENT..[[/]]..atcp.MSDPMOVEMENT_MAX..[[</b></center></p>]])
	setGauge("ManaBar",atcp.MSDPMANA,atcp.MSDPMANA_MAX)
	echo("ManaBar",[[<p style="font-size:14px"><center><b>]]..atcp.MSDPMANA..[[/]]..atcp.MSDPMANA_MAX..[[</b></center></p>]])
	setGauge("OppHealthBar",atcp.MSDPOPPONENT_HEALTH,atcp.MSDPOPPONENT_HEALTH_MAX)
	echo("OppHealthBar",[[<p style="font-size:14px"><center><b>]]..atcp.MSDPOPPONENT_HEALTH..[[/]]..atcp.MSDPOPPONENT_HEALTH_MAX..[[</b></center></p>]])
end
```

In hopes of not losing this post to a second Chrome crash I will post a screenshot in a reply. I hope this is helpful or at least interesting for someone

-Nate

</div>

<div class="post" data-post-id="34419" data-author="Drule" data-date="2013-09-10T11:35:57+00:00">

![](http://i44.tinypic.com/357ir8p.jpg)

I have since realized that OPPONENT_HEALTH seems to be percentage.. not sure why there is an OPPONENT_HEALTH_MAX then but w/e. If anyone knows how to make gauges fill the opposite way I would be interested in knowing your secret!

-Nate

</div>

<div class="post" data-post-id="34421" data-author="Drule" data-date="2013-09-10T12:02:01+00:00">

![](http://i42.tinypic.com/15i4uix.jpg)

Here's the updatebars script in case that was confusing

</div>

<div class="post" data-post-id="34425" data-author="Akaya" data-date="2013-09-12T07:36:36+00:00">

> **Drule wrote:**
> If anyone knows how to make gauges fill the opposite way I would be interested in knowing your secret!

This isn't possible using the createGauge() function.

Vyzor and Geyser both have this feature in their own versions of gauge creation: Vyzor.Gauge() and Geyser.Gauge:new()

If both frameworks don't appeal to you, you can try creating your own. A gauge is built from two labels, one atop the other. The bottom label stays a static size while the top label resizes based on whatever value it reflects. You can resize labels with resizeWindow() and move them with moveWindow(). To have your gauge move from right to left instead of left to right, you'd need to resize AND move the top label.

</div>
