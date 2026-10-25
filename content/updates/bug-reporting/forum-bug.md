---
title: "Forum Bug"
topic_id: 1921
author: "killme"
date: 2006-06-09T04:24:10+00:00
last_activity: 2006-06-10T00:50:26+00:00
last_author: "Clink"
sticky: false
locked: false
post_count: 2
---

<div class="post" data-post-id="12930" data-author="killme" data-date="2006-06-09T04:24:10+00:00" data-subject="Forum Bug">

I cannot login with my usual login.. I can login to the site, but if I go to the forums I get the following php errors in both IE and FireFox (more details following pasted errors):

 [code:3ixek1f6]

Warning: setup_style(./modules/PNphpBB2/templates/wowHorde/wowHorde.cfg): failed to open stream: No such file or directory in /home/slothmud/public_html/modules/PNphpBB2/includes/functions.php on line 734

Warning: setup_style(./modules/PNphpBB2/templates/wowHorde/wowHorde.cfg): failed to open stream: No such file or directory in /home/slothmud/public_html/modules/PNphpBB2/includes/functions.php on line 734

Warning: setup_style(): Failed opening './modules/PNphpBB2/templates/wowHorde/wowHorde.cfg' for inclusion (include_path='.:/usr/lib/php:/usr/local/lib/php') in /home/slothmud/public_html/modules/PNphpBB2/includes/functions.php on line 734

PNphpBB : Critical Error

Could not open wowHorde template config file

[/code:3ixek1f6]

The error is presumably because that wowHorde template no longer exists, but to change my preferences to use a different template, I have to log in to the forum first, which I cant because of that error, which means I cannot ever login to the forum with my existing username.. 

I'm sure there will be many others becoming apparent in the near future effected by this. If you don't believe me, go to the forum, click profile at the top of the page, and change your preferences to use that wowHorde template and save. Good luck, you wont be using that username again unless you quickly backup and select subblack (which appears to be the new default).

This is Weasel btw.

The only fix I can figure is to put back the wowHorde template at least temporarily so we can login and change to subblack as our preferred template, or somehow change everyone to subblack.

</div>

<div class="post" data-post-id="12946" data-author="Clink" data-date="2006-06-10T00:50:26+00:00" data-subject="">

The override is back in place now, but will be periodically turned on and off as we do some development.  I'll see about setting your profiles back to the default (subBlack) one time if I can figure it out, but after that you are on your own.  In the mean time, anyone who had issues, please follow the directions that were posted but actually change it to subBlack instead of away from it.

Regards,

Clink

</div>
