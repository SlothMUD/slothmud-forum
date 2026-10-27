---
title: "Debugging Help Thread"
topic_id: 4415
author: "abraxsis"
date: 2014-12-01T04:29:05+00:00
last_activity: 2014-12-06T16:34:11+00:00
last_author: "*Breeze*"
sticky: false
locked: false
post_count: 7
---

<div class="post" data-post-id="35531" data-author="abraxsis" data-date="2014-12-01T04:29:05+00:00" data-subject="Debugging Help Thread">

I'm starting this thread for people like me who need help with triggers and scripts for mudlet.

</div>

<div class="post" data-post-id="35532" data-author="abraxsis" data-date="2014-12-01T04:52:04+00:00" data-subject="Re: Debugging Help Thread">

Ok, I'm trying to set up a trigger named Ticket to set my destination when I buy a boat ticket. Eventually I will have an entry for all the boat trips, but this is what I have so far:

trigger statement - 

```
^You now have a (.*) boat ticket.$ 
```

(pearl regex)

this is the script i have when the trigger fires

```
------- bh ah -------
if matches [2] == "blue"
	then shipto = "bhah"
	end
end
------- bh ss --------
if matches[2] == "silver"
	then shipto = "bhss"
	end 
end
-------- ss ah -------
if matches[2] == "black"
	then shipto = "ssah"
	end
end
```

I'm getting the following error: Trying to activate trigger <em>Ticket</em> failed, reason: Lua syntax error:[string "function Trigger17(}..."\]:11: "expected near 'end'.

Any ideas/suggestions?

</div>

<div class="post" data-post-id="35535" data-author="*Breeze*" data-date="2014-12-01T07:22:25+00:00" data-subject="Re: Debugging Help Thread">

Without looking at my stuff on the laptop since it's not here atm, try removing the second end

If x == "y" then

 z = "blah"

end

</div>

<div class="post" data-post-id="35536" data-author="abraxsis" data-date="2014-12-01T07:30:51+00:00" data-subject="Re: Debugging Help Thread">

Thanks, that got it. Looked back at the trigger I got the idea from and realized it had a second if-then nested inside the first, hence the need for 2 end statements. It just didn't click when I was first setting this up.

</div>

<div class="post" data-post-id="35537" data-author="*Breeze*" data-date="2014-12-01T07:38:45+00:00" data-subject="Re: Debugging Help Thread">

No problem

</div>

<div class="post" data-post-id="35545" data-author="*juggleblood*" data-date="2014-12-06T16:29:18+00:00" data-subject="Re: Debugging Help Thread">

You may want to get in the habit of using elseif instead of having multiple ends. For example:

if matches[2]=="x" then x()

elseif matches[2]=="y" then y()

elseif matches[2]=="z" then z()

end

It's just a lil cleaner. 

One other thing to note is that the . in your regex pattern means any single character. It's not of consequence in this example, just pointing it out to you for your info. If you want to indicate an actual period, use /.

</div>

<div class="post" data-post-id="35547" data-author="*Breeze*" data-date="2014-12-06T16:34:11+00:00" data-subject="Re: Debugging Help Thread">

Thought it was \\. not /.

</div>
