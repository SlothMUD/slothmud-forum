---
title: "Wintin.net Fail to load"
topic_id: 2805
author: "nomic"
date: 2008-04-30T04:15:10+00:00
last_activity: 2008-04-30T05:11:03+00:00
last_author: "nomic"
sticky: false
locked: false
post_count: 3
---

<div class="post" data-post-id="24108" data-author="nomic" data-date="2008-04-30T04:15:10+00:00" data-subject="Wintin.net Fail to load">

Greetings Guys, 

Can I seek some expert advice as to why my wintin.net failed to load up? This is despite me uninstalling and reinstalling/repair. The following box still turn up.

Could not load XML:

The root element is missing.

Kindly help pls. 

Thanks

Nomic

</div>

<div class="post" data-post-id="24112" data-author="jezer" data-date="2008-04-30T04:39:24+00:00" data-subject="">

Wintin uses XML to store the settings from memory. If you reinstall wintin and it's not fixed, then the bug/corruption that causes the crash is in something that has been left behind... like a setting file. Look for files with an XML extenstion.

These setting files that need to be hunted down normally reside in your...

\*C:\\Documents and Settings\\\<username\>\\Local Settings\\Application Data\\Wintin.Net folder

OR

\*C:\\Program Files\\Wintin.Net

If depends if your using Windows XP, where you installed wintin and a bunch of other factors. Without getting technical, I think your best bet is too install wintin.net to a different place and point the setting paths to a different place as well. Then copy your scripts across to the new place. (Totally Fresh Copy)

If you really want to fix your current copy, then send me a pm, and we can arrange for you to send me your setting files and I can fix them up and email them back.

</div>

<div class="post" data-post-id="24114" data-author="nomic" data-date="2008-04-30T05:11:03+00:00" data-subject="">

U R the SAVIOUR! 

Many thanks...i just went to the folder that houses my scripts and deleted all XML files. From tehre...Wintin.net worked!

Just had to redirect the window default and scripts. 

Many thanks again Jezer.

Cheers

Nomic

</div>
