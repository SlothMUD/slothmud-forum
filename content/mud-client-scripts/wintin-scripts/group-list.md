---
title: "Group list"
topic_id: 663
author: "12345"
date: 2004-12-06T18:04:19+00:00
last_activity: 2004-12-07T13:42:43+00:00
last_author: "12345"
sticky: false
locked: false
post_count: 4
---

<div class="post" data-post-id="3216" data-author="12345" data-date="2004-12-06T18:04:19+00:00" data-subject="Group list">

This might already be out there somewhere, but I'll ask because I would find it very useful.

Does anyone have a client script that will output the group listing to a separate window?  I hate trying to read the list in large groups before it gets spammed away, especially if I'm trying to protect over someone (or more than one) who died, someone enters the group, leaves the group (Absent), etc.

If this doesn't exist, what are some other ways folks are dealing with this?  Any help is appreciated.  Thanks.

</div>

<div class="post" data-post-id="3217" data-author="Calim" data-date="2004-12-06T21:58:26+00:00" data-subject="">

Wintin.net has a nice #popup feature that you can apply filters to.   The filter I have used is '[Lvl:|consists of:'  The '[Lvl:' part is for each group member, and the 'consists of:' is for the name of the group and is a useful separator.  I'm not sure if that still works, been awhile since I used it in a group.

</div>

<div class="post" data-post-id="3218" data-author="Annie" data-date="2004-12-06T22:40:55+00:00" data-subject="">

Wintin 95

#openwin {5} {group}

#highlight {65} {Group '%0' consists of:}

#highlight {65} {%0 [Lvl:%1}

Change 5 to the number you want ... if you change it to say 7, should be 7 in first line and 67 in the other 2.

Annie

</div>

<div class="post" data-post-id="3226" data-author="12345" data-date="2004-12-07T13:42:43+00:00" data-subject="">

Thanks much. Should help me avoid a cf or two.  :D

</div>
