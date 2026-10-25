---
title: "processing MSDP spells in tintin++"
topic_id: 3986
author: "raincrab"
date: 2012-12-21T01:03:33+00:00
last_activity: 2012-12-21T01:03:33+00:00
last_author: "raincrab"
sticky: false
locked: false
post_count: 1
---

<div class="post" data-post-id="33856" data-author="raincrab" data-date="2012-12-21T01:03:33+00:00" data-subject="processing MSDP spells in tintin++">

here's an example to add a line to your status bar prompt thingie listing spells you're affected by and their duration.  (this would go somewhere in your msdp event handler)

```
	#format {aprompt} {};

	#foreach {$MSDP_AFFECTS[]} {affect} {
		#var key $affect;
		#var val $MSDP_AFFECTS[$affect];
		
		#if {$val > 0} {
			#format {aff} {<bbf>%s<g08>:<bbf>%s } {$affect} {$val};
			#format {aprompt} {$aprompt%s } {$aff};
		}
	};
	
	#line ignore #showme {$aprompt} {1};
```

</div>
