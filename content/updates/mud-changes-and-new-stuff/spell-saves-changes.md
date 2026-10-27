---
title: "Spell Saves changes"
topic_id: 3852
author: "*Splork*"
date: 2012-02-12T05:23:30+00:00
last_activity: 2012-02-12T05:23:30+00:00
last_author: "*Splork*"
sticky: false
locked: false
post_count: 1
---

<div class="post" data-post-id="33159" data-author="*Splork*" data-date="2012-02-12T05:23:30+00:00" data-subject="Spell Saves changes">

The current spell saves code was not working exactly as it was supposed to be but because of two separate bugs the overall effectiveness was pretty close to where it should of been anyways. There was a bug preventing saves eq from working and a secondary bug giving attunement way too much value. 

The current saves code has been fixed so that - saves eq works properly and attunement is valued properly as well.

A secondary saves code has been added and is a test config called test\_saves. Once toggled on, it gives better weight to a mobs level and also includes the mobs saves which are left out of the original equation in code one above. I will be testing this and seeing the results throughout the week and if we like them make the change to the new formula.

More detailed changes below:

SAVE CHANGES

Changed equation for player saves 

 \* added in additional importance to mob level

 \* added in mob saves ( was left out of original equation )

 \*\* now when a mob is damned, cursed, etc it helps player to get max damage

 \* Player saves now work completely. There was a small bug preventing it

 \* Fixed bug with attunement counting too much towards saves ( which evened out the above bug )

 \* Added in saves for Para

 \* added in attunement bonus ( same as channeling for saving\_spell ) for mental, when dealing with Para saves

Added in additional logging after every step of saves\_spell code

Added in severity logging after every step of saves\_spell code

Added new test config test\_saves so that we can do short tests of new equation

Enjoy,

Splork

</div>
