---
title: "lastLine, lineBefore, and duplicate line &quot;+&quot; echo"
topic_id: 4595
author: "*juggleblood*"
date: 2016-02-26T01:44:58+00:00
last_activity: 2016-02-27T03:01:52+00:00
last_author: "*juggleblood*"
sticky: false
locked: false
post_count: 3
---

<div class="post" data-post-id="36638" data-author="*juggleblood*" data-date="2016-02-26T01:44:58+00:00" data-subject="lastLine, lineBefore, and duplicate line &amp;quot;+&amp;quot; echo">

Here's a simple one that I like.

Define these vars in your definitions script:

lastLine=lastLine or ""

lineBefore=lineBefore or ""

Then make a new trigger and name it LAST LINE TRIGGER, or wutever

regex trigger:

(^[A-Z].\*)

block:

if matches[2]==lastLine then

selectCurrentLine()

deleteLine()

cecho("\<maroon\>+\<reset\>")

end

lineBefore=lastLine

lastLine=matches[2]

\------------

Now anytime you get a duplicate line from the mud, it will be deleted, and a maroon + will appear at the end of the preceeding line. Also now you can access the var lineBefore in your scripts which can be handy.

</div>

<div class="post" data-post-id="36640" data-author="Madigan" data-date="2016-02-26T06:06:24+00:00" data-subject="Re: lastLine, lineBefore, and duplicate line &amp;quot;+&amp;quot; echo">

what's an example of when this would be handy?

</div>

<div class="post" data-post-id="36653" data-author="*juggleblood*" data-date="2016-02-27T03:01:52+00:00" data-subject="Re: lastLine, lineBefore, and duplicate line &amp;quot;+&amp;quot; echo">

You could add a check to the xp updater for example to see what lastLine is and you could track averages on the xp that your strikes or blasts were doing.

</div>
