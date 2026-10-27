---
title: "Find string in buffer"
topic_id: 4042
author: "Constin"
date: 2013-02-22T15:55:41+00:00
last_activity: 2013-02-22T15:55:41+00:00
last_author: "Constin"
sticky: false
locked: false
post_count: 1
---

<div class="post" data-post-id="34071" data-author="Constin" data-date="2013-02-22T15:55:41+00:00" data-subject="Find string in buffer">

alias

Pattern: ^bfind((\\[(\\d+)\\])?) (.\*)$

Code:

```
-- usage:
-- bfind rat
-- bfind[2] rat
-- bdind ^lua
-- bfind[10] quest

-- config
local bfindMark = "bfind" -- should be same as alias
local hist = 7500
local minL = 0

-- getting lines
if getLineCount() > hist then
	minL = getLineCount() - hist
end
local data = getLines(minL, getLineCount())

-- prepare for search
local pattern = string.genNocasePattern(matches[5])
local delta = nil
if matches[4] then 
	delta = tonumber(matches[4])
end

-- looking for pattern in history
for i,line in ipairs(data) do
	local match = string.findPattern(line, pattern)
	if match then
 if not string.starts(line, bfindMark) then
 local hline = string.gsub(line, pattern, "<purple>" .. match .. "<lime_green>")	
 -- printing lines before match
 if delta then
 for ii=delta,1,-1 do 
 if (i-ii) >= 1 then
 cecho(string.format("<black>%s <dark_green>%4d: <lime_green>%s\n", bfindMark, (i-ii), data[i-ii]))
 end
 end
 end
 -- printing match line
 cecho(string.format("<black>%s <medium_sea_green>%4d: <lime_green>%s\n", bfindMark, i, hline))
 -- printing lines after match
 if delta then
 for ii=1,delta do 
 if (i+ii) <= hist then
 cecho(string.format("<black>%s <dark_green>%4d: <lime_green>%s\n", bfindMark, (i+ii), data[i+ii]))
 end
 end
 -- printing separator
 cecho(string.format("<black>%s<dark_slate_grey>-----\n", bfindMark))
 end
 end
	end
end

-- reseting color and adding final blank line
resetFormat()
echo("\n")
```

</div>
