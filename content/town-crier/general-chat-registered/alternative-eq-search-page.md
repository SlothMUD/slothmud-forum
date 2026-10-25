---
title: "Alternative eq search page"
topic_id: 4483
author: "Filk"
date: 2015-05-19T07:48:19+00:00
last_activity: 2015-11-21T07:32:56+00:00
last_author: "Ertai"
sticky: false
locked: false
post_count: 19
---

<div class="post" data-post-id="35904" data-author="Filk" data-date="2015-05-19T07:48:19+00:00" data-subject="Alternative eq search page">

I was working for some time on eq search page. More convenient for me, then default eq page on site.

And while i still have a lot of things to do with that script, it already can be used by other people.

So i uploaded it on server. Feel free to use.

[http://slothmudeq.tk/](http://slothmudeq.tk/)

ps: I attached free domain to it for a while, could take some time to update all dns servers. 

Also, A-record like eq.slothmud.org to its ip address might be usefull, if you have interest in that.

</div>

<div class="post" data-post-id="35905" data-author="*Breeze*" data-date="2015-05-20T07:37:32+00:00" data-subject="Re: Alternative eq search page">

Not bad.

I have said time and again if someone thinks they can do better than me to code it and I will host it.

A few people said they could and no one followed through.

</div>

<div class="post" data-post-id="35906" data-author="Filk" data-date="2015-05-21T10:30:57+00:00" data-subject="Re: Alternative eq search page">

Uploaded fresh version.

- Filtering without refreshing of the page

- Search by mob name or area name

- Some minor interface tweaks.

Breeze, is it posible to export forge page data as json file?

</div>

<div class="post" data-post-id="35907" data-author="*Breeze*" data-date="2015-05-21T11:27:44+00:00" data-subject="Re: Alternative eq search page">

its already dumped to json just noone has access to it except me.

the data is probably useless to you though its all done with vnums of objs and mobs.

i dont think i put the mob vnums in the dl eqlist not that i remembereither way.

</div>

<div class="post" data-post-id="35908" data-author="Filk" data-date="2015-05-21T14:10:33+00:00" data-subject="Re: Alternative eq search page">

I have vnums of all objects, mobs and areas.

So some basic array with links will be enough for me. Like  {item_vnum, forger_vnum, cps {cps_vnums}}. You can include forge name or forger name also, but that will be just for more unserstandble file. Though maybe forger_name will be good idea anyway, in case if that mob dont pops anything, so its name not at eq list.

Also would be nice, if eq dump and that forge dump will be accessed by some permanent link. Current eq dump link changes by some unknow rule, so tricky to add autoimport at cron. 

Might be good to have constant links with first elements as date of file change.

</div>

<div class="post" data-post-id="35909" data-author="*Breeze*" data-date="2015-05-21T16:20:46+00:00" data-subject="Re: Alternative eq search page">

i will see if i can remember where the file is

not going to code extra for it though. at least not anytime soon. still setting up my new pc.

</div>

<div class="post" data-post-id="35910" data-author="*Breeze*" data-date="2015-05-21T22:50:50+00:00" data-subject="Re: Alternative eq search page">

here is what the data looks like

{"FORGE_VNUM":"99246","FORGER_VNUM":"99239","FORGE_TYPE":"Trade","FORGE_EXPLOSION_CHANCE":"3","FORGE_COST":"2000000","COMPONENT_VNUM":["99218","99219","99220","99221","

99222","99224","99225","99226","99227","99228"],"COMPONENT_QUANTITIES":["1","1","1","1","1","1","1","1","1","1"]}

{"FORGE_VNUM":"99244","FORGER_VNUM":"99223","FORGE_TYPE":"Trade","FORGE_COST":"6000000","COMPONENT_VNUM":["99245","99246","99247","99248"],"COMPONENT_QUANTITIES":["1","

1","1","1"]}

problem 

 a) there are/may be undiscovered forges (which i am not going to manually remove)

 b) you wont be able to cross reference forger_vnum

 c) the file is out of date since the exporter code for it is broken and not fixable for the time being.

only real solution is for me to combine the forge and eqlist.json file

</div>

<div class="post" data-post-id="35911" data-author="Filk" data-date="2015-05-22T06:21:02+00:00" data-subject="Re: Alternative eq search page">

Well. Current format seems almost good enough. Single addition of forger_name will make it better. With forger_area_vnum - perfect :)

Actually forger name is almost enough. But it can work even with just vnum. At least i will have exact list of mob vnums that i will need to name in db :)

About undiscovered forges. If item is hidden - its absent in eq list. So vnum gives nothing about actual forge.

Though it gives a hint, that forge exists and where is start point to search.

From my point, thats even good for the game, if that info is available. Like new quest list gave some starting info about quests.

I dont see anything good in forges that noone knows about. And if area isnt new, chance to such forge beeing discovered isnt really high.

Imho ofc.

If you will be able to fix script that generate that file, that would be great. No ideas why its broken and how long it will take to fix it.

But guess that will be faster then writing some new export system from the scratch.

If not, i can work with thing you have now. At least something. And we dont have lots of new forges added on constant basis. So maybe isnt that big lack there.

</div>

<div class="post" data-post-id="35912" data-author="*Breeze*" data-date="2015-05-22T09:53:40+00:00" data-subject="Re: Alternative eq search page">

Exporter works on coders port but not game port. It crashes the game port. .

</div>

<div class="post" data-post-id="35913" data-author="*Breeze*" data-date="2015-05-25T08:48:51+00:00" data-subject="Re: Alternative eq search page">

Email me filk.

</div>

<div class="post" data-post-id="35914" data-author="Yasik" data-date="2015-05-26T09:04:29+00:00" data-subject="Re: Alternative eq search page">

Limited practical use.

Example 1: I want to search "shield" AND "forged". How? Same as www version, scroll through list, watch with eyes or Ctrl+F.

Example 2: I want to search "armor" AND "waist". How?

Example 3: I want to sort by AC. You got the idea.

I dont want to be rude, but it seems you exersising at coding only for the sake of it, without a goal. Just take a deep breath and look at your results. Would you use it yourself?

Blackmore's was the best, too bad its gone :(

</div>

<div class="post" data-post-id="35916" data-author="*Breeze*" data-date="2015-05-26T13:47:27+00:00" data-subject="Re: Alternative eq search page">

re:

 1) he doesnt have access to forge data yet

 2 & 3 ) i assume its still a work in progress.

</div>

<div class="post" data-post-id="35917" data-author="Filk" data-date="2015-05-26T14:23:04+00:00" data-subject="Re: Alternative eq search page">

> **Yasik wrote:**
> Limited practical use.
> 
> Example 1: I want to search "shield" AND "forged". How? Same as www version, scroll through list, watch with eyes or Ctrl+F.

As breeze said, no forge data for use yet. WIll add it, if i will get the data.

> **Yasik wrote:**
> Example 2: I want to search "armor" AND "waist". How?

I didnt add filters for exact slots yet, just in my to do list.

> **Yasik wrote:**
> Example 3: I want to sort by AC. You got the idea.

List after any filtering sorted by ac within each slot group. Not sure if filter by armor have any uses with that conception. But not any problems to add it, if someone think it will be usefull.

At mainpage list sorted by the date i add item to my db, to easy check, what is new. But actually it was only one data update since that time, so only several top items are new.

> **Yasik wrote:**
> I dont want to be rude, but it seems you exersising at coding only for the sake of it, without a goal. Just take a deep breath and look at your results. Would you use it yourself?
> 
> Blackmore's was the best, too bad its gone :(

I have exact goals, and i made this page to use for myself. In the way i want to use eq filtering page. 

Just shared with ppl, if anybody else want to use it too. If you dont like that realization - dont use. If you have some good offers - share :)

Current stage is just point where i think it can be already used by other ppl, but it isnt finish point.

I have big list of things i want to add. And dont mind to add other good ideas as well.

No ideas what Bm did, never even heard. But whatever. More not less :)

</div>

<div class="post" data-post-id="35918" data-author="*Breeze*" data-date="2015-05-26T14:41:06+00:00" data-subject="Re: Alternative eq search page">

just emailed fluffy/filk.  here is the parts of the email that pertain to this conversation.

the rest is me apologizing to him for being a bit of a jerk when it wasn't him i was mad at.

i will consider the a-record. at a minimum i can add it to the menu's.

```
added forge data download to the eqlist. same place as weekly dump.
if/when the command to export the missing forges gets fixed, it will update.
for now, its a static file.

also added mob names/vnums in the same place.
this file updates as areas are added to the mud

the only file missing is the one with area vnums and area names but that has some stuff that 
needs to be edited out so i have to fix that before i can send you that.

continents file is useless to export as it never changes. here is the contents.

{"CONTINENT_VNUM":"0","CONTINENT_NAME":"Godsland"}
{"CONTINENT_VNUM":"1","CONTINENT_NAME":"Thordfalan"}
{"CONTINENT_VNUM":"2","CONTINENT_NAME":"Thule"}
{"CONTINENT_VNUM":"3","CONTINENT_NAME":"The Island"}
{"CONTINENT_VNUM":"4","CONTINENT_NAME":"Niebelung"}
{"CONTINENT_VNUM":"5","CONTINENT_NAME":"Lyme"}
{"CONTINENT_VNUM":"6","CONTINENT_NAME":"The Clipper"}
{"CONTINENT_VNUM":"7","CONTINENT_NAME":"Valkyre"}

anything on godsland needs to stay in godsland and not on the eqlist.

as of this point, the eqlist is completely opened up and everyone has the same data i do
with the exception of area lifespans and unpopped/unidentified items (not many of those left anyways)
```

</div>

<div class="post" data-post-id="35920" data-author="Yasik" data-date="2015-05-27T08:36:10+00:00" data-subject="Re: Alternative eq search page">

Well, it would be really cool if you guys finish what you say is in your to-do list and what I mentioned.

</div>

<div class="post" data-post-id="35921" data-author="Marvel" data-date="2015-05-27T13:14:41+00:00" data-subject="Re: Alternative eq search page">

This is an awesome some start, Filk!

One thing that should be on to do list is some ac is + not -, like red clown shoes is +2.0.

As for Blackmore eqlist, what Yasik forgets is it was completely manual database with php to query and sort, and links to area and forge instructions. I saved static version of this in ABC order without ability to query or view forge list.

[http://nicklong.net/sloth/sloth3_eq.htm](http://nicklong.net/sloth/sloth3_eq.htm)

Go to [http://nicklong.net/sloth/](http://nicklong.net/sloth/) for other archived stuff. I haven't had time lately to do anything in game or out of game. Summer is busy for me.

One thing I did do once was use table headers and simple JavaScript to be able to sort on columns. It is simple and JavaScript sucks, but you might find it useful for some application. This is what I used:

[http://www.kryogenix.org/code/browser/sorttable/](http://www.kryogenix.org/code/browser/sorttable/)

</div>

<div class="post" data-post-id="35932" data-author="Filk" data-date="2015-06-03T14:00:36+00:00" data-subject="Re: Alternative eq search page">

Uploaded some updates on the eq page.

- Forges now displays all cps, forger and forge price.

- All items that are cps for something shows in what forge they are needed for.

- Forge check in a filters

Also found that eq dump file has some missing items, so you can see things like 1 x [12345] in cps list for forges.

That means that item was missing in eq dump, but i have its id from forge dump. That issue require some fixes to the eq dump file.

</div>

<div class="post" data-post-id="36192" data-author="Filk" data-date="2015-11-19T07:10:22+00:00" data-subject="Re: Alternative eq search page">

Some new updates.

- Added filters by eq slots and few other item types

- When you filter by clasps or runes, all items now displayed in exact eq slot, that clasp or rune can be attached. If item attaches to several eq slots, it displays in each.

</div>

<div class="post" data-post-id="36199" data-author="Ertai" data-date="2015-11-21T07:32:56+00:00" data-subject="Re: Alternative eq search page">

Just wanted to say 'thanks'.

Fluffy, just several days ago found your eq list, it's great! Easy to use, very logical. Thank you.

</div>
