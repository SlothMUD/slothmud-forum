---
title: "tf afk script"
topic_id: 3978
author: "raincrab"
date: 2012-12-11T23:51:20+00:00
last_activity: 2012-12-12T23:47:14+00:00
last_author: "jezer"
sticky: false
locked: false
post_count: 2
---

<div class="post" data-post-id="33838" data-author="raincrab" data-date="2012-12-11T23:51:20+00:00">

defines a /afk macro that toggles afk, updates title, and auto lurks.

```
/set title %s
/set isafk 0

/def afk = \
	/if ({isafk} == 0) \
		/set isafk 1 %; \
		lurk on %; \
		title %title \\d10<<\\d09A.F.K\\d10>> %; \
	/elseif ({isafk} == 1) \
		/set isafk 0 %; \
		lurk off %; \
		title %title %; \
	/endif

/def doafk = \
	/if ({connected} == 1) \
		/if ({isafk} == 1) \
			yawn %; \
		/endif %; \
	/endif

/repeat -60 i /doafk
```

</div>

<div class="post" data-post-id="33841" data-author="jezer" data-date="2012-12-12T23:47:14+00:00">

Can you post your Ruby dropping script?  :P  :shock:  :twisted:

</div>
