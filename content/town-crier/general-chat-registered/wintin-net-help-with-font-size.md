---
title: "Wintin.net  help with font size"
topic_id: 1953
author: "Turbo"
date: 2006-07-03T23:25:21+00:00
last_activity: 2006-07-14T00:42:40+00:00
last_author: "Turbo"
sticky: false
locked: false
post_count: 7
---

<div class="post" data-post-id="13256" data-author="Turbo" data-date="2006-07-03T23:25:21+00:00" data-subject="Wintin.net  help with font size">

Something happened to my wintin.net, suddenly the font size is huge, maybe it shows 10 words per screen and obviously I can't play like that. I can't seem to fix it either. Any advice? I uninstalled wintin.net and installed a new copy from the website but it seems to still have this cazy large font. 

I went to File- > Terminal Settings -> Window -> Appearance and it says 10 pt font so I don't know what's happening. If a config file had gone corrupt, then removing wintin.net would have taken care of that. Help pls ;-)  Thanks - AL, Turbo

</div>

<div class="post" data-post-id="13257" data-author="*Splork*" data-date="2006-07-03T23:41:49+00:00" data-subject="">

Try changing the font size to 6-8, click save or apply, exit wintin. Restart it and it should be fixed. I've noticed that any changes inside the terminal settings do not  take affect until the program is closed and reopened...

</div>

<div class="post" data-post-id="13258" data-author="Turbo" data-date="2006-07-04T00:16:16+00:00" data-subject="">

I did that but it didn't help. I am attaching a url to a screen shot of the problem in case someone has experienced it and recognizes the problem.

[http://www.users.cloud9.net/~al/wintin.JPG](http://www.users.cloud9.net/~al/wintin.JPG)

</div>

<div class="post" data-post-id="13261" data-author="Gimlet" data-date="2006-07-04T03:20:30+00:00" data-subject="">

happened to me once...

close your wintin, and check the font size/encoding in your internet explorer/any default browser u use, then run wintin again

</div>

<div class="post" data-post-id="13264" data-author="Turbo" data-date="2006-07-04T12:38:07+00:00" data-subject="">

How should I set the encoding? It's currently on Western (ISO). I have no idea what that means. I tried auto-select but that didn't make a difference.  BTW everything is fine with my internet browsing, it's just wintin that has this problem.

</div>

<div class="post" data-post-id="13266" data-author="Gimlet" data-date="2006-07-04T13:04:33+00:00" data-subject="">

can't remember how i did it...

alternatively u can try deleting the defaultwindow.wnd file, and let it recreate its settings

</div>

<div class="post" data-post-id="13473" data-author="Turbo" data-date="2006-07-14T00:42:40+00:00" data-subject="">

For all it's worth, I decided to try again, this time I deleted all files in

C:\Documents and Settings\....\Application Data\Wintin\*.*

Like magic, upon re-running Wintin, it returned to normal. Why didn't this work when I uninstalled Wintin.net, then searched for all instances of Wintin and deleted anything missed by the uninstall, I'll never know! But now it works!

</div>
