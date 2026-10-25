---
title: "Changelog 2021-01-18"
topic_id: 5007
author: "*teker*"
date: 2021-01-18T19:18:13+00:00
last_activity: 2021-01-19T20:12:38+00:00
last_author: "cnl"
sticky: false
locked: false
post_count: 3
---

<div class="post" data-post-id="39673" data-author="*teker*" data-date="2021-01-18T19:18:13+00:00">

Fixed a crash in get if you mistyped the container name.  Not sure how we went on for so long with this in place, but it's fixed now.

Put in some overflow protection regarding number of eqsets.  It should now prevent you from creating new sets if you're going to overflow the buffer.  The max number of sets is related to the length of all the set names added together in a string.  If you make the names shorter, you can have more.  I'm guessing the limit is around 300 if all of the sets have 1-2 character names.

Maniac put in a fix for reading - we're hoping this solves the crash in there.  The command has been enabled again.

</div>

<div class="post" data-post-id="39674" data-author="Gorka" data-date="2021-01-19T13:55:32+00:00">

Thanks Teker and Maniac for the bug fixes.

Regarding the number of eqsets. I tend to back mine up, after accidentally overwriting things on a few occasions. Hence I have double what I use. I'm not sure if other people are doing the same, but given the ability to export the backup sets, we could then delete these duplicates. Reconstructing an eqset from a robe can take a good 15mins or more. The fact the clasps on the proc items (sleeves/gaunts/goblet) don't upgrade in the eqsets when the items level up, creates a situation where you have to resave your eqsets more than you would for regular eq. That's where I have come unstuck several times. 

Perhaps if eqset could be less concerned about missing items if that is a clasp and wasn't detachable in the first place?

</div>

<div class="post" data-post-id="39677" data-author="cnl" data-date="2021-01-19T20:12:38+00:00">

thanks for the update on fixes! also, really excited to have reading back

</div>
