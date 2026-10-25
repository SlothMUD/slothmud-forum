---
title: "Website bug found"
topic_id: 1616
author: "resouh"
date: 2005-12-25T01:54:28+00:00
last_activity: 2005-12-25T01:54:28+00:00
last_author: "resouh"
sticky: false
locked: false
post_count: 1
---

<div class="post" data-post-id="9920" data-author="resouh" data-date="2005-12-25T01:54:28+00:00" data-subject="Website bug found">

Clicked on the crier for info on Christmas Quest, read the info, then clicked on the "more on quests" link to the right, and got the following errors:

Warning: open_basedir restriction in effect. File is in wrong directory in /home/httpd/vhosts/slothmud.org/httpdocs/includes/search/dq_helpdesk.php on line 30

Warning: Failed opening 'modules//pnlang/eng/dq_helpdesk.php' for inclusion (include_path='.:/usr/share/pear') in /home/httpd/vhosts/slothmud.org/httpdocs/includes/search/dq_helpdesk.php on line 30

Fatal error: Call to a member function on a non-object in /home/httpd/vhosts/slothmud.org/httpdocs/includes/search/dq_helpdesk.php on line 114

Resouh:)

</div>
