---
title: "EQList"
topic_id: 4180
author: "*Breeze*"
date: 2013-12-28T21:35:47+00:00
last_activity: 2014-01-08T04:02:52+00:00
last_author: "*Breeze*"
sticky: false
locked: false
post_count: 25
---

<div class="post" data-post-id="34707" data-author="*Breeze*" data-date="2013-12-28T21:35:47+00:00" data-subject="EQList">

I received a few messages from people saying that a few others don't like the eqlist.

My reply is simple.

The new interface should make it easier to find things.

The filters are searchacle (top box on top)

And you can even use partial keywords to search.

As I get time I plan on adding more filters as per a few suggestions I received.

If you still don't like it, download the full eqlist file.

It has everything in there and it gets updated weekly. Everything is fully cross referenced and you can do whatever you like with it.

I can't make everyone happy and I refuse to try.

Maps are on the wiki as before

Live info is there as before

Its not really that different.

</div>

<div class="post" data-post-id="34708" data-author="*Splork*" data-date="2013-12-28T21:46:55+00:00" data-subject="Re: EQList">

I haven't received one complaint via email or tell in-game so I am rather clueless in regards to how the players feel. There were many compliments on gossip and I do know people are trying to get used to the new Eqlist.

If people have suggestions and/or complaints they need to express them via bugs, emails, tells, or nicely on the forum:)

With anything new, there will be changes and adaptations which make the site better for everyone involved. Overall, not a whole lot besides appearance has changed. Navigation is almost identical. Most of the content is identical. Forums are unchanged.

If anyone has ideas for additions or changes, please let us know. If you email one of us, please include the other via cc.

Splork

</div>

<div class="post" data-post-id="34711" data-author="Maarg" data-date="2013-12-29T00:02:33+00:00" data-subject="Re: EQList">

It has been a refreshing change from the old EQ List. Just needs a tad of fine tuning.

</div>

<div class="post" data-post-id="34712" data-author="DarkArtist" data-date="2013-12-29T00:28:37+00:00" data-subject="Re: EQList">

It's trivial, but if you ever got around to it, I liked the feature of looking up the eq for a particular zone. I don't see that option on the new page. It's not a priority tho.

Maybe some of the people with feedback on the format could be more specific about what they'd like to see. Personally, I'd kinda like the entries to be shorter vertically so more fit on the page, but it might be nitpicky of me to say so.

</div>

<div class="post" data-post-id="34713" data-author="*Splork*" data-date="2013-12-29T00:45:19+00:00" data-subject="Re: EQList">

Breeze actually added Area as one of the possible selections to search from on the EqList before he went to bed. 

Here is the current sample, its not flushed out yet and he plans on prettying it up soon:

http://www.slothmud.org/wp/welcome-to-slothmud/equipment/eqlist?area=18

You can find this option on the right hand side of the eqlist. If chosen, it overrides any other option which you selected.

I already suggested a possible Brief option for the listed results which might just show item short description and affects so that many items would be displayed without needing to scroll down. This sounds exactly like you are suggesting also. I like the addition of a Brief option because personally, I do like the longer format also and would hate to see him just junk it for a shorter version.

Splork

</div>

<div class="post" data-post-id="34715" data-author="Nyctivoe" data-date="2013-12-29T01:12:41+00:00" data-subject="Re: EQList">

Now that I've gotten my slow mind around the website changes, I like the new EQList. Thanks to those who did the work.

</div>

<div class="post" data-post-id="34716" data-author="Shyla" data-date="2013-12-29T03:15:19+00:00" data-subject="Re: EQList">

any chance if we put in a mob we can see what all it pops like typing in baoht and come up with all that is listed for him..?? also I was trying to find windrun book and windrun came up with nothing as did manual of wind I had to put in manual of THE wind before anything at all would show up ..anychance we can put in spell name and have mobs come up and not just the complete book name

Shyla

</div>

<div class="post" data-post-id="34719" data-author="*Splork*" data-date="2013-12-29T03:42:25+00:00" data-subject="Re: EQList">

I am not sure about the requests themselves, that is Breeze's expertise. However, I believe you must be doing something wrong in terms of your search because I type in manual of wind and the first result is clearly the A Manual of the Wind.

ManualWind.PNG

There were two other results below that one: 

a manual of wind blown footprints

manual of vigorous exercise

The searches use partial matching so it should work extremely well. I can't really understand why your results are not the same?

Splork

</div>

<div class="post" data-post-id="34721" data-author="blackmore" data-date="2013-12-29T04:56:42+00:00" data-subject="Re: EQList">

Some issues I see with the new eqlist...

Bard stats for instruments aren't displayed.

?x40 restricts aren't displayed.

There's a huge amount of whitespace. It seems like there would be something that could be done to fit more on the screen.

Overall, it's definitely a good step, and I'm going to have to experiment with the json file. You pretty much have to write a parser to be able to read it, and I'm not quite that far yet.

</div>

<div class="post" data-post-id="34724" data-author="Agni" data-date="2013-12-29T06:25:14+00:00" data-subject="Re: EQList">

also weapon dice and potions affects are not displayed

</div>

<div class="post" data-post-id="34725" data-author="*Breeze*" data-date="2013-12-29T07:44:41+00:00" data-subject="Re: EQList">

> <strong>Agni wrote:</strong>
> also weapon dice and potions affects are not displayed

was my fault. fixed

removed pretty mode. too many different variables to keep track of and 

in general a pain for me to try and interpret data for you.

added brief mode. does nothing as of yet.

changed normal mode. it shows everything now. not even minimal prettying up.

with the exception of forge components for an item.

changed shown poppers to first 9999. 

there is no more hidden data other than has been identified/popped or not.

if it doesnt show up in normal mode, the eqlist doesnt know it.

</div>

<div class="post" data-post-id="34726" data-author="*Breeze*" data-date="2013-12-29T07:46:28+00:00" data-subject="Re: EQList">

> <strong>blackmore wrote:</strong>
> Overall, it's definitely a good step, and I'm going to have to experiment with the json file. You pretty much have to write a parser to be able to read it, and I'm not quite that far yet.

there is no need to write own parser for json.

i posted a php example on a diff thread, and

[http://json.org/](http://json.org/)

has parsers for just about every language.

</div>

<div class="post" data-post-id="34727" data-author="*Breeze*" data-date="2013-12-29T09:33:52+00:00" data-subject="Re: EQList">

linked in eq by area. click the area name on a regular search or use the \*AREA\* filter to pull up a list of areas then

click from there.

there is no pretty and no csv mode. 

just a straight dump of the data.

</div>

<div class="post" data-post-id="34729" data-author="Marvel" data-date="2013-12-29T15:23:39+00:00" data-subject="Re: EQList">

Is there a way to see eq that can shapeshift?

Also - any way to display that an item is a CP for a forge? You can find cps for forges if you know the forge, look up forge,then look up cp. But not other way around. Example - search "father" and "globe". Father for the forge, Globe for the cp.

</div>

<div class="post" data-post-id="34742" data-author="Yasik" data-date="2013-12-30T14:43:55+00:00" data-subject="Re: EQList">

What about sorting? Can we sort ascending/descending by AC, for example?

</div>

<div class="post" data-post-id="34751" data-author="*Breeze*" data-date="2014-01-02T23:21:10+00:00" data-subject="Re: EQList">

what you are both asking for is basically more filters.

the main responses i got to the eqlist are: <em>it sucks</em> and <em>its too hard to use</em>.

adding more filters wont make that any easier to use, and tbh i have other things to do.

today i sorted the eq poppers. they are sorted/grouped by continent/area/mob. 

if i get time in the future, i will see about adding in more filters, but that is not my priority at the moment.

as for forge cps, all forge data is listed here on one page.

[http://www.slothmud.org/wp/equipment/forges-trades-enchantments-and-brews](http://www.slothmud.org/wp/equipment/forges-trades-enchantments-and-brews)

i am not about to do a bunch more queries to the database to see if each and every item is a forge component, sorry.

</div>

<div class="post" data-post-id="34752" data-author="Marvel" data-date="2014-01-03T23:53:53+00:00" data-subject="Re: EQList">

Thanks for all the hard work, Breeze!

Forge page (separate from EQ list, searchable) functions fine as the cp item now. Much thanks!

Shapeshift is found in extra flags, but it's viewable now due to your additions.

</div>

<div class="post" data-post-id="34756" data-author="*Breeze*" data-date="2014-01-04T07:46:06+00:00" data-subject="Re: EQList">

I could link that forge page to the eq list to filter if the item found is part of a forge but it wouldn't be automatic.

Not sure.

Will think about it.

</div>

<div class="post" data-post-id="34762" data-author="*Breeze*" data-date="2014-01-06T20:04:49+00:00" data-subject="Re: EQList">

splork added code to export the eq sets (eg all leather sets)

i added in code to display said sets.

i am also considering adding in

IS\_XXXX filters for

IS\_SHAPESHIFT

IS\_FORGE

IS\_SET

am i missing anything?

if someone wants to write up a blurb that i can put on the eqlist page (when you first go and havent searched)

that says how to use eqlist i will add it in. no pictures tho. if we want picture page then it has to be a separate page that we can link to, any takers?

</div>

<div class="post" data-post-id="34763" data-author="Marvel" data-date="2014-01-06T21:38:20+00:00" data-subject="Re: EQList">

Thanks Splork and Breeze.

I'll see what I can do about the separate page. But I just got a Win 8 machine (and it's the only machine I have). May take me a while to do a new page (on how to use eqlist).

</div>

<div class="post" data-post-id="34764" data-author="*Breeze*" data-date="2014-01-06T21:41:05+00:00" data-subject="Re: EQList">

come up with the text / pics / layout and i will 

make it a page on the main site.

</div>

<div class="post" data-post-id="34768" data-author="blackmore" data-date="2014-01-08T01:40:08+00:00" data-subject="Re: EQList">

I have a question about the json.

It seems like the list of objects should have a common property name. In the download file, the property name is the vnum. Shouldn't there be a property name instead of the vnum?

</div>

<div class="post" data-post-id="34769" data-author="*Breeze*" data-date="2014-01-08T02:29:36+00:00" data-subject="Re: EQList">

the layout was designed to not be able to overwrite other items in php.

easiest way was with vnums

hence the 

```
$myEQArray = json_decode(file_get_contents('filename.json'),true);
echo '<html><body><pre>';print_r($myEQArray);die('</pre></body></html>');
```

if you have a better way i am willing to listen but not promising i will change anything

</div>

<div class="post" data-post-id="34770" data-author="blackmore" data-date="2014-01-08T03:59:44+00:00" data-subject="Re: EQList">

I don't know if I have a better idea of not, I'm just asking. I've never consumed json I haven't written before, it just looked different.

</div>

<div class="post" data-post-id="34771" data-author="*Breeze*" data-date="2014-01-08T04:02:52+00:00" data-subject="Re: EQList">

nod. 99% of everything i do, i export with php parseable json. <img src="/images/smilies/icon_e_smile.svg" alt=":)" title=":)" width="15" height="15" class="smiley nozoom">

</div>
