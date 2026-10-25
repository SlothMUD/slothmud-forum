---
title: "zmud mxp run scripts"
topic_id: 3514
author: "Thraxas"
date: 2010-09-09T09:50:29+00:00
last_activity: 2010-09-09T09:50:29+00:00
last_author: "Thraxas"
sticky: false
locked: false
post_count: 1
---

<div class="post" data-post-id="31743" data-author="Thraxas" data-date="2010-09-09T09:50:29+00:00" data-subject="zmud mxp run scripts">

I've been having a play with putting mxp links into my own zmud scripts to contol some of my functionality, one that I think may be of interest is to control runs, but it could be adapted to any group of aliases:

A cut down version of the code is as follows:

#MXP AH <send "w;s;e;e|w;w;s;s;s;e;e;n|n;e;e;e;e;e;s;open gate;s;w;s|ahvault" "inn|moran|bank|vault">Run Menu</send>

This send a line to the main mud window as follows:

AH Run Menu

Run Menu is a link

If you left click the link the following commands are sent to the mud w;s;e;e ... i.e. the first run listed, the run from recall to the inn.

If however you right click the link you see a context sensitive menu

inn

moran

bank

vault

you can click any of these options and the appropriate commands are sent to the mud to make the run, 3 of these are explictit runs defined in the above code the 4th ahvault is my pre-existing alias containing the run to my AH vault, both work.

I obviously alias the above #mxp command and then I run all such commands capturing to a links window on startup so they sit there ready to be used.

This is helpful to me to save me needing to remember all the aliases I have for runs to all areas, but could equally well be used to choose which spell to cast, or equipment set to change to etc.

Hope this ios of interest or help,

Thraxas

</div>
