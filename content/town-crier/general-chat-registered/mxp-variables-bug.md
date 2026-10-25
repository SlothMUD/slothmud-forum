---
title: "mxp variables bug"
topic_id: 3048
author: "*Splork*"
date: 2009-02-21T14:13:54+00:00
last_activity: 2009-02-27T14:03:08+00:00
last_author: "*Splork*"
sticky: false
locked: false
post_count: 8
---

<div class="post" data-post-id="28242" data-author="*Splork*" data-date="2009-02-21T14:13:54+00:00">

I just received a comment that mxp variables are not updating as quickly or at all after a recent change to our prompt went live. Could someone please give me more information, I do know gold is not updating at all. Are there any others? Do you guys notice anything odd happening or variables getting set incorrectly?

Thanks

Splork

</div>

<div class="post" data-post-id="28248" data-author="Cizin" data-date="2009-02-21T20:08:01+00:00">

You have 1001444004 unused experience points.

Prompt:

-\1024hp 408ma 354mv/-\11444004xp-/

</div>

<div class="post" data-post-id="28254" data-author="*Splork*" data-date="2009-02-21T22:51:36+00:00">

This should of been fixed on today's crash, let us know please.

Splork

</div>

<div class="post" data-post-id="28255" data-author="jezer" data-date="2009-02-22T01:21:34+00:00">

Splork the mxpExits variable still seems to be blank/broken.

I tried to use it to make a psuedo automapper a couple of weeks back... which leads me to my next point... a mxp variable to say what was the last direction you travelled would be useful...

It could also be used to script a command to "backtrack" your steps... really useful when you invent stupid classos without cleric and mage, and you get stuck in the middle of no where with no recall and no word of recall. 

Of course that's never happened to me, because... because... erm...  :oops: 

Yeah, you can do it without an mxp variable, but involves making aliases for all the directions.... and trip traps you may enter to reverse properly.

</div>

<div class="post" data-post-id="28259" data-author="java" data-date="2009-02-22T13:45:53+00:00">

At least for me. Even more mxp varibles are INCORRECT since yesterday. 

Previously, only alignment,bank, and one more were not updating. One I've never seen before has suddenly started appearing.{City}, has been added to the bottom of listed mxp vars.

 It's always blank.

I just looked after exiting boat and most mxp varibles have NOT updated even after saving.

I'm using Wintin.net.ver 2.09

</div>

<div class="post" data-post-id="28260" data-author="*Splork*" data-date="2009-02-22T15:08:14+00:00">

I had to remove sector, area, and continent due to an unforeseen bug.

Everything else should be working properly after the next reboot.

I hope,

Splork

</div>

<div class="post" data-post-id="28261" data-author="firebrand" data-date="2009-02-22T18:08:53+00:00">

It could also be used to script a command to "backtrack" your steps... really useful when you invent stupid classos without cleric and mage, and you get stuck in the middle of no where with no recall and no word of recall. [/quote:2f0z78tp]

if you are on wintin, try using #path to see the steps you've taken (or attempted to make - it records wall bumps as a step/direction).  also use #mark to erase the #path history and start from point a - i.e. go to west gate, type #mark so that you have a fresh #path, then go about your merry way, when you get to a stopping point, type #path to see what directional commands you sent to the mud.  at this point, i am not sure how to make it not count wall bumps but i am sure with a little ingenuity someone will find a workaround.

"what do you mean the door's stuck? try jiggling the handle."  -chicha --> the emperor's new groove

</div>

<div class="post" data-post-id="28325" data-author="*Splork*" data-date="2009-02-27T14:03:08+00:00">

I think Ive fixed this for everyone, please let me know if not.

Splork

</div>
