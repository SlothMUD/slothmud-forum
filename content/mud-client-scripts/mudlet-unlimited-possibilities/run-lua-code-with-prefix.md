---
title: "Run Lua code with ! prefix"
topic_id: 4041
author: "Constin"
date: 2013-02-22T15:50:56+00:00
last_activity: 2013-03-03T07:17:52+00:00
last_author: "Akaya"
sticky: false
locked: false
post_count: 2
---

<div class="post" data-post-id="34070" data-author="Constin" data-date="2013-02-22T15:50:56+00:00">

Alias

Pattern:^!(.+)$

Code:

```
-- USAGE:  
--   !commnad
--
-- EXAMPLE:
--   !echo("Hello from Lua")

local f,e = loadstring("return "..matches[2])
if not f then 
	f,e = assert(loadstring(matches[2]))
end 

local r = f()
if r then display(r) end
```

</div>

<div class="post" data-post-id="34116" data-author="Akaya" data-date="2013-03-03T07:17:52+00:00">

This is now a default script that appears on every new profile. The only difference is that you use the alias **lua <whatever>** instead of **!**

</div>
