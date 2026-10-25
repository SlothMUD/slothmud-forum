---
title: "Changelog 2016-02-12"
topic_id: 4588
author: "*teker*"
date: 2016-02-12T15:46:09+00:00
last_activity: 2016-02-12T20:21:03+00:00
last_author: "*Splork*"
sticky: false
locked: false
post_count: 4
---

<div class="post" data-post-id="36586" data-author="*teker*" data-date="2016-02-12T15:46:09+00:00" data-subject="Changelog 2016-02-12">

Went through a number of bugs:

226) Wed May 27 01:10:27 2015  Primal  27514

    keyless entry does not work if your shapeshifted.

Another reason to request an upgrade to the new vaults.  Shapeshifted players can use keyless access in the new code.

498) Sat Jan 23 10:21:27 2016  Songster  8001

    using the quest channel breaks reading the book, though using the gossip doe

Fixed.  Also fixed for the settings command.

515) Tue Feb  2 03:33:20 2016  Taron  30304

    can't mem demon bind, a mage 34 spell

Demon bind is level 20 cleric/necromancer so it's not eligible for memorization via mage ioun stones.

Lots of bugs regarding mounts:

327) Fri Sep 11 23:24:11 2015  Zuzu  8026

    it's actually fairly hard to cause your mount to get webbed without you fighting it, but if you do manage it, the horse can move despite being webbed

329) Sat Sep 12 01:10:44 2015  Mose  34231

    I bought a horse & it was covered in sticky webs ... it still moved normally, but reported 'sticky webs' every time it moved

345) Fri Oct  9 13:13:41 2015  Songster  1988

    i died on a mount, going s from tomb it said You can't go in there while on a mount!

364) Tue Oct 27 17:47:04 2015  Qaz  8000

    if you die while mounted, you will stay mounted even if your horse is not with you at tomb.

406) Thu Dec  3 02:28:23 2015  Taron  33203

    when you are mounted and recall someone, you are dismounted

407) Thu Dec  3 03:19:01 2015  Taron  69257

    get webbed, dismount, squirm, rid of webs. Horse is seen as webbed. mount, can move, horse is shown as webbed.

522) Sun Feb  7 06:56:48 2016  Ozzy  4233

    'is_mounted' flag does not clear when I beacon return - trying to mount again after beacon return says I already riding something, and mount goes not wit

These should all be fixed.  Mounted players now need to break webs to dismount.  Mounts need to break the webs to move.  Let me know if there are other places where mounts are not behaving as expected.

The eqset code is back in but needs to be toggled on by a god.  There's more bug checking in the code but I haven't been able to reproduce the bug that is/was hanging the game.

</div>

<div class="post" data-post-id="36587" data-author="*teker*" data-date="2016-02-12T15:53:11+00:00" data-subject="Re: Changelog 2016-02-12">

Also - there's a large number of bugs that have been filed about problems with the web site.  Is anyone still having issues logging in?

</div>

<div class="post" data-post-id="36588" data-author="*Breeze*" data-date="2016-02-12T19:35:30+00:00" data-subject="Re: Changelog 2016-02-12">

I seem to remember fixing that.

</div>

<div class="post" data-post-id="36589" data-author="*Splork*" data-date="2016-02-12T20:21:03+00:00" data-subject="Re: Changelog 2016-02-12">

That was fixed on 2/2/16. There were two separate issues and both were addressed.

Once a player logs in and sets their password, they need to log out and back in. Once that happens it takes a bit more time before the website gets that information.

I believe we tested with several players that week, so we should be good to go. If there are still problems, please post here or shoot us an email...

</div>
