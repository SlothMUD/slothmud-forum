---
title: "string exts and string affects output"
topic_id: 4179
author: "DarkArtist"
date: 2013-12-28T15:49:23+00:00
last_activity: 2014-01-20T16:32:36+00:00
last_author: "Akaya"
sticky: false
locked: false
post_count: 10
---

<div class="post" data-post-id="34698" data-author="DarkArtist" data-date="2013-12-28T15:49:23+00:00">

EDITED OUT: 

DO NOT COPY SPECIAL CHARACTERS INTO YOUR SCRIPTS. THEY CAUSE SAVE/LOAD ISSUES.

</div>

<div class="post" data-post-id="34699" data-author="DarkArtist" data-date="2013-12-28T16:24:33+00:00">

EDITED OUT, DOESN'T WORK.

</div>

<div class="post" data-post-id="34700" data-author="DarkArtist" data-date="2013-12-28T16:41:03+00:00">

EDITED OUT, DOESN'T WORK

</div>

<div class="post" data-post-id="34702" data-author="Akaya" data-date="2013-12-28T18:56:58+00:00">

This won't work for everyone unfortunately. Because the 'special characters' aren't $ ] and [ on all operating systems.

Try this function out. It will work on ALL operating systems. It cuts the end off the string (the 'special character'), reverses the string and cuts off the end again (the other 'special character'). That cleans up the string to be parsed, and returns a table named MSDP. So you can refer to exits and their status' by checking MSDP.North or w/e:

```
function parseExits(event,msdp)
  MSDP = {}
  msdp = string.cut(msdp,msdp:len()-2)
  msdp = string.reverse(msdp)
  msdp = string.cut(msdp,msdp:len()-2)
  msdp = string.reverse(msdp)
  msdp = string.split(msdp,", ")
  for k,v in pairs(msdp) do
    msdp[k] = string.split(msdp[k],": ")
  end
  for k,v in pairs(msdp) do
    MSDP[v[1]] = v[2]
  end
  return MSDP
end
```

I'm using this for a nice looking compass I'll post later on by calling this function in an event handler.

</div>

<div class="post" data-post-id="34704" data-author="DarkArtist" data-date="2013-12-28T19:20:09+00:00">

EDITED OUT.

</div>

<div class="post" data-post-id="34705" data-author="Akaya" data-date="2013-12-28T20:36:18+00:00">

Altering a script in any way will always be less ideal than one that requires nothing at all.

</div>

<div class="post" data-post-id="34710" data-author="DarkArtist" data-date="2013-12-28T23:56:55+00:00">

EDITED OUT.

</div>

<div class="post" data-post-id="34722" data-author="Akaya" data-date="2013-12-29T04:59:45+00:00">

Nothing wrong with your script. In fact, you're doing a great job figuring things out! I only point out that there is a more optimal way of parsing the string that doesn't require a copy/paste.

</div>

<div class="post" data-post-id="34807" data-author="DarkArtist" data-date="2014-01-20T14:06:03+00:00">

It turns out there is a very important reason to do it your way...

If you use illegal characters in your scripts, they will cause your scripts to not save. Any scripts under the illegal characters will just vanish from existence. 

I just wanted to note that here in case anyone should try to copy and paste them from the msdp output and destroy their scripts.

</div>

<div class="post" data-post-id="34808" data-author="Akaya" data-date="2014-01-20T16:32:36+00:00">

Very good to know. Thank you!

</div>
