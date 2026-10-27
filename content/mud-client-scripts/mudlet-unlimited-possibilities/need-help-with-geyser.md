---
title: "Need help with Geyser"
topic_id: 4006
author: "Constin"
date: 2013-01-17T14:32:50+00:00
last_activity: 2013-01-17T14:55:04+00:00
last_author: "Constin"
sticky: false
locked: false
post_count: 2
---

<div class="post" data-post-id="33929" data-author="Constin" data-date="2013-01-17T14:32:50+00:00" data-subject="Need help with Geyser">

I dont like Vyzor, couse it on betatest, it lag etc.

i like simple quick scripts. 

So this is my client now: [https://dl.dropbox.com/u/10038339/trash/mmmmm.png](https://dl.dropbox.com/u/10038339/trash/mmmmm.png)

The green window is for MSDP and local virables, but i cant understand , how to put it in this window.

Here script:

testlabel = Geyser.Label:new({

 name = "testlabel",

 x = -434, y = 0,

 width = 420, height = 240,

 fgColor = "black",

 color = "SeaGreen",

 message = [[..atcp.MSDPCHARACTER\_NAME..]]

})

Can smb help me? Akaya?

</div>

<div class="post" data-post-id="33930" data-author="Constin" data-date="2013-01-17T14:55:04+00:00" data-subject="Re: Need help with Geyser">

message = atcp.MSDPCHARACTER\_NAME 

works

</div>
