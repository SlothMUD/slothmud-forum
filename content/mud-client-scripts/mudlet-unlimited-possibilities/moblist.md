---
title: "Moblist"
topic_id: 4647
author: "Akaya"
date: 2016-07-01T07:22:59+00:00
last_activity: 2016-07-14T05:32:13+00:00
last_author: "*Breeze*"
sticky: false
locked: false
post_count: 11
---

<div class="post" data-post-id="37018" data-author="Akaya" data-date="2016-07-01T07:22:59+00:00" data-subject="Moblist">

I noticed there was a JSON file for mobs on the webpage. Though I can't seem to parse it with Mudlet like I can with the eqlist. I recieve a malformed JSON error. I'm familiar with JSON. But not enough so to detect an error it seems. Could anyone lend a hand? Maybe I'm doing something wrong.

The mob JSON file can be found here: http://www.slothmud.org/wp/equipment/eqlist?dl=07&dlk=9cb66283451c196d54bc117e2c1b369c&lua=0&mobs=1

Here's the error I recieve:

```
 Lua syntax error:InvalidJSONInput: parse error: trailing garbage
 ":"Weylyn","AREA_VNUM":"76"} {"MOB_VNUM":"130146","MOB_NAME"
 (right here) ------^
```

</div>

<div class="post" data-post-id="37019" data-author="Akaya" data-date="2016-07-01T07:33:46+00:00" data-subject="Re: Moblist">

Did a bit of research and it seems that each line is valid JSON, but it needs to be placed into an array. So to turn it into a proper array you'd separate each object with a "," and wrapping that up in an array with "[]"'s ?

Does this sound familiar Breeze? I know you helped me sort out eqlist. Did you have to do this with that one too?

It's 12,000+ lines of code so manually doing this is daunting.

</div>

<div class="post" data-post-id="37024" data-author="*Breeze*" data-date="2016-07-02T21:24:00+00:00" data-subject="Re: Moblist">

Let me get back to you on that. That file was there for an alt eq list and me meant to be parsed with php. Will add a Lua switch like I did for the eqlist.

</div>

<div class="post" data-post-id="37037" data-author="*Breeze*" data-date="2016-07-09T22:33:53+00:00" data-subject="Re: Moblist">

try that... new entry "LUA MOBS" same place as the rest.

i think i got it right.

make sure i didnt break eqlist export in lua too, if you can please.

</div>

<div class="post" data-post-id="37052" data-author="Akaya" data-date="2016-07-14T02:04:31+00:00" data-subject="Re: Moblist">

The Lua file for eqlist still works as expected. But the LUA MOBS file is still returning the same error mentioned above.

Here's a snippet of what I use to parse the LUA MOBS file within Mudlet if it helps with debugging...

```
function initMoblist()
 dofile(getMudletHomeDir().."/moblist.lua")
 moblist = yajl.to_value(MOBS)
end

initMoblist()
```

I do the same with eqlist which seems to work fine...

```
function initEqlist()
 dofile(getMudletHomeDir().."/eqlist.lua")
 eqlist = yajl.to_value(EQLIST)
end

initEqlist()
```

</div>

<div class="post" data-post-id="37053" data-author="*Breeze*" data-date="2016-07-14T03:14:20+00:00" data-subject="Re: Moblist">

try again...

made a small change.

[http://json.parser.online.fr/](http://json.parser.online.fr/) and json decode in php both handle the \_huge\_ string properly.

</div>

<div class="post" data-post-id="37054" data-author="Akaya" data-date="2016-07-14T05:04:12+00:00" data-subject="Re: Moblist">

Works! Awesome. Thank you! I can do some cool stuff with this now...

</div>

<div class="post" data-post-id="37055" data-author="*Breeze*" data-date="2016-07-14T05:10:29+00:00" data-subject="Re: Moblist">

viel Spass damit

</div>

<div class="post" data-post-id="37056" data-author="Akaya" data-date="2016-07-14T05:13:29+00:00" data-subject="Re: Moblist">

Ich werde. Vielen Dank.

</div>

<div class="post" data-post-id="37057" data-author="Akaya" data-date="2016-07-14T05:18:34+00:00" data-subject="Re: Moblist">

Now if we could just get the AREA\_VNUM added to the MSDP, I can tie this in with a map <img src="/images/smilies/icon_e_smile.svg" alt=":)" title=":)" width="15" height="15" class="smiley nozoom">

</div>

<div class="post" data-post-id="37058" data-author="*Breeze*" data-date="2016-07-14T05:32:13+00:00" data-subject="Re: Moblist">

Email me

</div>
