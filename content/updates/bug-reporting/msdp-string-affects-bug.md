---
title: "MSDP.STRING_AFFECTS bug"
topic_id: 4729
author: "Tuck"
date: 2017-01-16T12:13:47+00:00
last_activity: 2017-01-16T14:15:59+00:00
last_author: "Tuck"
sticky: false
locked: false
post_count: 3
---

<div class="post" data-post-id="37966" data-author="Tuck" data-date="2017-01-16T12:13:47+00:00" data-subject="MSDP.STRING_AFFECTS bug">

** problem fixed **

Here is mudlet code to parse MSDPAFFECTS correctly:

Alias:

```
if not checkSpell("regeneration") then send("cast 'regen'") end
if not checkSpell("darksight") then send("darksi") end
if not checkSpell("stone skin") then send("cast 'stone skin'") end
if not checkSpell("infravision") then send("cast 'infravision'") end
if not checkSpell("mobility") then send("cast 'mobility'") end -- Mobility
if not checkSpell("detect magic") then send("cast 'detect m'") end
if not checkSpell("detect invisibility") then send("cast 'detect i'") end
```

Function:

```
function get_affects() 
	stringAffects=atcp.MSDPAFFECTS
	stringAffects=string.gsub(stringAffects,string.char(3)..string.char(1),"")
	stringAffects=string.gsub(stringAffects,string.char(1),",")
	stringAffects=string.gsub(stringAffects,string.char(2),": ")
	stringAffects=string.gsub(stringAffects,string.char(3)," ")
	stringAffects=string.gsub(stringAffects,string.char(4),"")
	affectsTable=stringAffects:split(",")
	affects={}
	for i,v in ipairs(affectsTable) do
		if not (v:split(": ")[2]=="-1") then
			affects[v:split(": ")[1]]=v:split(": ")[2]+0
		end
	end
end
function checkSpell(spell)	
	if table.contains(affects,spell) then 
		return true
	else
		return false
	end
end
```

</div>

<div class="post" data-post-id="37967" data-author="*juggleblood*" data-date="2017-01-16T13:55:07+00:00" data-subject="Re: MSDP.STRING_AFFECTS bug">

I told you string_affects is obsolete.  MSDPAFFECTS is the newer one.

</div>

<div class="post" data-post-id="37969" data-author="Tuck" data-date="2017-01-16T14:15:59+00:00" data-subject="Re: MSDP.STRING_AFFECTS bug">

yeah, it works

Thanks

</div>
