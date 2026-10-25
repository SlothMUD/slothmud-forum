---
title: "tf logging"
topic_id: 3979
author: "raincrab"
date: 2012-12-11T23:53:23+00:00
last_activity: 2012-12-11T23:53:23+00:00
last_author: "raincrab"
sticky: false
locked: false
post_count: 1
---

<div class="post" data-post-id="33839" data-author="raincrab" data-date="2012-12-11T23:53:23+00:00">

autologging with log rotation with date in filename

```
/def logger = /log off %; \
	/log SlothMUD.$[ftime("%F")].log %; \
	/at 00:01 /logger

/hook CONNECT = /logger %; /set connected 1
/hook CONFAIL|ICONFAIL * = /log off %; /set connected 0
```

</div>
