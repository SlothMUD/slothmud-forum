---
title: "Add Fastrun to the MUD to kill mobs faster"
topic_id: 4571
author: "Teron"
date: 2016-01-05T10:15:21+00:00
last_activity: 2016-01-16T18:33:31+00:00
last_author: "Teron"
sticky: false
locked: false
post_count: 26
---

<div class="post" data-post-id="36407" data-author="Teron" data-date="2016-01-05T10:15:21+00:00" data-subject="Add Fastrun to the MUD to kill mobs faster">

Greetings.

Crumbs made a nice exp-tracking script and it became completely obvious to me that exp per mob/area is diminished, if it takes a while to walk between mobs. In fact, it's so obvious I mentioned runs in [a post about making better areas](http://www.slothmud.org/forum/viewtopic.php?t=4472&p=35807#p35807) before Crumbs even showed me the results of the script:

> **Quote:**
> So, as you can see, I like areas that have:
> 
> - ...
> 
> - short runs between mobs
> 
> - safe runs between mobs

Fastruns will allow you to increase engagement and retention at all levels.

1. Increase new player retention by increasing engagement and progress

So while thinking about what would keep new players on the mud, I thought that perhaps adding speedruns to newbie areas would be helpful to increase engagement, progress and enjoyment, as well as adding some comfort level to playing the mud. This completely eliminates the need to think that there might be a website or a map shop to get directions from, then the need to follow those directions manually, etc. For newbies, it'll make exceptional difference.

fastrun blaster

You start running to the Blaster's Temple:

The Intersection of Main and Fargo Streets

Main Street

The Intersection of Main and Granite Streets

Main Street

Main Street

Main and Fathnir Street

North Gate of Newbatia

The North Road of Newbatia

The North Road of Newbatia

The North Road of Newbatia

Edge of an Enchanted Forest

Exits: North  East  

A mystical bugbear wanders about the sacred land.

A mystical bugbear wanders about the sacred land.

A mystical bugbear wanders about the sacred land.

<373hp 173ma 137mv> 

Since it's easier to keep a new player, than an old player, making an improvement at lower levels should make a more noticeable effect, which you can measure.

2. Make running easier for all players to slightly increase exp and retention

An added bonus to adding fastruns is increased conveniency and enjoyment of old players, who can run easier, get more exp and stay more engaged/satisified by the MUD, which goes well with this goal and improvement:

[http://www.slothmud.org/forum/viewtopic.php?f=26&t=3822](http://www.slothmud.org/forum/viewtopic.php?f=26&t=3822)

3. Keep the dangereous runs

I have to mention that I understand why some runs have to be long and dangerous (DWeb, Moors, Dmount, Volcano), but for grouping, [long and breakable running in Moria](http://www.slothmud.org/forum/viewtopic.php?t=4472&p=35807#p35807) kills area exp. You can keep the mob aggro, while on the run, but just make running faster - potentially, with unlocking doors, if the key is in the inv/keychain.

I talked to Crumbs and he said he had already suggested the idea of fastruns to be unlocked by the level.

I also suggest measuring before and after the change on how it affects the gameplay:

- measure mobdeath per area per week

- measure number of visits to an area per week

- measure visited rooms per area per week.

- mobs killed per player per day/week

Thanks.

</div>

<div class="post" data-post-id="36408" data-author="Filk" data-date="2016-01-05T11:17:06+00:00" data-subject="Re: Add Fastrun to the MUD to kill mobs faster">

How that differs from your own personal run alias in your client, which you could make with all doors, flees, shifting ferrets etc? I see only skipping description part in your message. But they dont make runs any noticeble slower. as i see on my own speedwalk sets.

</div>

<div class="post" data-post-id="36409" data-author="Teron" data-date="2016-01-05T14:43:21+00:00" data-subject="Re: Add Fastrun to the MUD to kill mobs faster">

1. Newbies don't:

- find the mapmaker quickly enough unless there's an obvious autoquest (there isn't). There might be a newbie guide in the inv, but I'm not sure how often it's used.

- go to the map section and find the dirs

- know they can run faster with flee.

And if they do all the above (about 5-15% by my estimate), they'll need to spend the time to do it, which they'd rather spend on exploring the mud and getting the first exp to level.

As for experienced players, I agree that the effect will be minimal, if any. At least I'll be able to ask ppl to reliably run to Fiends, DWeb or Dragonmountain.

2. There is a room movement lag. If you go to an underwater area, you'll notice that you move slightly slower.

You already know that you move, when fleeing, faster, than you walk. I propose making fastruns move faster, than the normal walk, to speed up the runs as well.

P.S. I'm now considering adding speed-running aliases in addition to group-friendly ones. Fastrun would remove the requirement of personal aliases, though I wonder if you could take a group w/ you on a fastrun alias. Will have to think about it, if there's any movement in the fastrun direction.

</div>

<div class="post" data-post-id="36410" data-author="*Splork*" data-date="2016-01-05T15:14:15+00:00" data-subject="Re: Add Fastrun to the MUD to kill mobs faster">

Its not a terrible idea just one which I don't think would as much an effect as you think it will. 

We would never add something which took away the danger of runs to and through aggressive areas though...

</div>

<div class="post" data-post-id="36411" data-author="Teron" data-date="2016-01-05T16:13:59+00:00" data-subject="Re: Add Fastrun to the MUD to kill mobs faster">

I agree that aggro needs to stay. Who doesn't want to be ripped apart by a beholder in a nocast room.

If we agree that the idea of fastruns is valid, then we can try to find a solution to keep aggro:

- don't do anything that'll remove mob reach to the running mortals

- if that doesn't work, increase mob reaction speed to running  mortals proportionally to the speed difference

- if anything, make it harder to get long and dangerous runs: an autoquest or a complete area exploration, for example.

I'm sure you or Teker can offer a way to keep aggro w/o unnecessarily complicating things here.

As for impact on newbies, I agree that it is no magic pill. I still think that a bigger help would be a newbatia college w/ educational quests and an area with lots of mobs.

</div>

<div class="post" data-post-id="36412" data-author="cyprimus" data-date="2016-01-05T22:28:48+00:00" data-subject="Re: Add Fastrun to the MUD to kill mobs faster">

maybe just add a run command.

you run you do not see roomname, description or content..and don't update prompt etc.. till run is over.

also cannot run while hiding sneaking et.c..

</div>

<div class="post" data-post-id="36413" data-author="*teker*" data-date="2016-01-06T03:50:25+00:00" data-subject="Re: Add Fastrun to the MUD to kill mobs faster">

So is this a feature to run to the entrance of a zone?  Or would it be used to run around inside zones also to get to the next mob?  How would I get a list of potential destinations?

Can you run to shops or other important locations?  "Run bank" or "Run docks" or "Run recall" or "Run vault"?

Currently players can execute a command every 250ms but mob aggro only gets checked every 10 seconds.  Would the run execute that fast?

Do players run through underwater areas without water breath?  If not, are they told before they start running or do they run up to the water's edge and then stop?

Are there other terrain types or exit/door types that prevent running?

Can you run in the dark?

Can players stop running midway through?

Is there an extra bonus hit chance and/or damage if mob aggro takes place while running?

Do players consume movement points faster when running?  This is a huge problem for new characters - especially casters.  It's easy to run out of moves on VK as is.

</div>

<div class="post" data-post-id="36414" data-author="Filk" data-date="2016-01-06T08:42:44+00:00" data-subject="Re: Add Fastrun to the MUD to kill mobs faster">

I guess you dont expect answers on these questions, but just displayng that such addition is quite complicated for the output  :lol: 

Though i could add several more questions and problems to that list, but dont doubt that was just quick review of the idea, so no point in that :)

</div>

<div class="post" data-post-id="36415" data-author="Teron" data-date="2016-01-06T10:22:03+00:00" data-subject="Re: Add Fastrun to the MUD to kill mobs faster">

Fluffy, these questions are good product questions that needs answers. So ask more questions, so we have a deeper understanding of the mechanics, so that we have a more useful feature that imms can develop faster.

> **Quote:**
> - So is this a feature to run to the entrance of a zone? Or would it be used to run around inside zones also to get to the next mob? How would I get a list of potential destinations?

The run starts from the continent recall, unless you can make it start anywhere on the continent, provided the rooms are connected (an added value).

Yes, to the entrance.

2nd iteration is for players to mark a spot/room that needs to run to.

For example:

Bottom of the Stairs

run mark

Run dweb runs to the entrance

Run dweb spot runs to my spot.

I specifically don't mention it to be a gatable spot, because some areas are nogate, e.g. CF. 

Some areas need waiting to get there, such as UD2 and Infernites, so I'm not holding my breath on the runs taking me longer, then the rooms I need to wait in. Though, if you do find such a challenge interesting, that'd be very useful.

If there are any technical limits on the amount of spots players can store, limit those spots or add quests to get them. Then again, quests may be not a scalable option, if there are lots of areas that need a restriction.

> **Quote:**
> - Can you run to shops or other important locations? "Run bank" or "Run docks" or "Run recall" or "Run vault"?

Yes, while in town.

Also, run alchemist/potion also works.

Afaik there's only one vault per person per continent, so yes, it runs to the vault and unlocks and locks the door afterwards, as long as the key is in the inv. If the trigtrap is purchased, it uses the trigtrap.

> **Quote:**
> - Currently players can execute a command every 250ms but mob aggro only gets checked every 10 seconds. Would the run execute that fast?

Maybe it's my perception, but I do get caught often, if I don't make precautions. Is it really 10 seconds, not 1-2 seconds?

Yes, the whole idea is to make the run be fast, maybe 50ms per room. Aardmud run command moves at about 3 rooms per 250ms. 100ms per room might be acceptable.

Can you make aggro mobs fast-to-attack running ppl, so the aggro rate is the same, compared to walking ppl? Any ideas about this?

> **Quote:**
> - Do players run through underwater areas without water breath? If not, are they told before they start running or do they run up to the water's edge and then stop?

Players are subjected to the same restrictions they have, when not running.

So yes, they can move, while choking, as they can now.

Thus, players run where the command takes them. If they forgot wb and decided to run to poseidon's realm, their fault.

If they need fly somewhere and decide to run, their fault.

> **Quote:**
> - Are there other terrain types or exit/door types that prevent running?

Same as with regular running: magic warded doors and locked doors the player doesnt have keys to.

> **Quote:**
> - Can you run in the dark?

Yes

> **Quote:**
> - Can players stop running midway through?

Yes, if you are fast enough to press |. There may be a specific command, if need be, since pipe only clears player sent command.

> **Quote:**
> - Is there an extra bonus hit chance and/or damage if mob aggro takes place while running?

No, unless the mob is wielding a spear or a sword :) 

> **Quote:**
> - Do players consume movement points faster when running? This is a huge problem for new characters - especially casters. It's easy to run out of moves on VK as is.

No, the mvs are consumed as usual.

Tl;dr: Still need ideas on how to save mob aggro from a technical side. Since I haven't seen the code nor know C, I have no idea.

</div>

<div class="post" data-post-id="36416" data-author="cyprimus" data-date="2016-01-06T11:05:48+00:00" data-subject="Re: Add Fastrun to the MUD to kill mobs faster">

I have also seen bypassing it with portals to area entrances in town... and teleports... but they ignore the intervening areas.. and usually take you to the last safe room on the way... ie-not past aggro mobs.

maybe a forge like the invitations etc..  but requires you to have completely explored area, and have track and shadowwalk?  maybe area keys too.. maybe even require convo.. and use mana to work on group?

5 am.. lots of idea.. wonder how stupid they will be after i sleep..p

</div>

<div class="post" data-post-id="36417" data-author="Teron" data-date="2016-01-06T12:08:09+00:00" data-subject="Re: Add Fastrun to the MUD to kill mobs faster">

Portals from forges or autoquests can be a good idea, as well. Unfortunately, it doesn't help newbies a lot, because it is invisible to them, unless they get a portal in the inv or from newbie college.

</div>

<div class="post" data-post-id="36419" data-author="Dragoth" data-date="2016-01-06T15:28:50+00:00" data-subject="Re: Add Fastrun to the MUD to kill mobs faster">

Before wasting coder's resources to add or fix stuff shouldn't we first figure out the issue that we are trying to address ?

You say that fastruns would be nice to have to increase exp rate, but is this a priority for anyone ? There are much easier ways for immortals to increase our exp rate and doing it through fastruns is quite dubious at best.

More convenience ? Again, is this a problem for anyone that needs fixing ? I think that this goes against some of our MUDs core principles, where good exp rate areas are nearly always hard to access and make you feel badass simply for being able to reach them. I could probably understand a forge/portal type of thing like they have in aard, where you get ease of access to an area as a reward for doing a quest/forge, we already have this for some areas and making it for every area has to be properly weighted, but I personally think that overall, this whole ease of access to areas for experienced players is a non-issue, we all have clients that have fast-runs and aliases already. 

It's true that I have suggested idea of fastruns to Splork before, but my main reason was newbie-oriented, as I felt newbies could use pointers about what areas to hit and how to get there without spending hours searching the website to figure out what they can kill and how to get there. I constantly heard newbies asking on gossip about what they can kill and I thought that some pre-programmed area level-list and fastruns could make life a bit easier for them and keep them interested a bit longer, although thinking about it now, it's coming to me that convolution and harshness play an important part in sloth, so making newbies search and research and die while simply trying to get to an area is an initiation of some sort and making them learn this principle early on isn't such a bad idea. Yes we lose players, but it kind of also weeds out the lazy ones early on and the ones that stay are the ones that can take all the pain and hardships that they will have to go through during their time here.

Either way I think I have to agree with Splork, this function isn't going to have that much effect and it probably doesn't warrant all the time that'll have to be spent to implement it properly.

</div>

<div class="post" data-post-id="36420" data-author="*Splork*" data-date="2016-01-06T17:02:04+00:00" data-subject="Re: Add Fastrun to the MUD to kill mobs faster">

I am still having a difficult time understanding how exactly this would help real newbies to Sloth. I have used fastwalk/run on some other muds and found that its not really as useful as a newbie as I thought it would be. A player needs to know different aspects of the game before it actually becomes useful such as names of areas you want to explore, names of mobs you want to visit, etc.  I can't count how many times on other games I have speedwalked to an area, died, and not had a clue how to get my equipment back.

    I see the feature as having little to no effect for the rest of the playerbase. These players all already have nearly every area aliased or more importantly, they know the runs to speedwalk them. They also have the benefit of skills/features which partially does what Tarons "2nd Phase" would do which is find a particular room and run to it (lloyds, greater lloyds, clan recalls, etc, which is why we wouldn't add something like that... we have enough).

Call me old school, I believe a player should learn an area. Why would a player be able to speedwalk/run to an area they have never visited before?  :mrgreen:

For the record, I am not for or against this type of feature. I am against anything which removes any danger from running to areas or the game in general.

</div>

<div class="post" data-post-id="36421" data-author="*teker*" data-date="2016-01-06T17:05:46+00:00" data-subject="Re: Add Fastrun to the MUD to kill mobs faster">

I'm going to go ahead and continue posing questions about this particular feature request to see how it hashes out.  I think the question of where resources should be spent would probably be better in another thread where we look at a variety of ideas from a higher/less detailed level.

> **Teron wrote:**
> The run starts from the continent recall, unless you can make it start anywhere on the continent, provided the rooms are connected (an added value).

Yes, the run could start anywhere without much effort.  It would use the existing hunt/track code to find the route which can start anywhere.

> **Quote:**
> Yes, to the entrance.
> 
> 2nd iteration is for players to mark a spot/room that needs to run to.

I think these could be done as a single item where "waypoints" are saved to the database as either "global" or "personal".  I would probably use the same "run <waypoint>" command and allow players to override the global waypoint by specifying one with the same name. 

> **Quote:**
> Some areas need waiting to get there, such as UD2 and Infernites, so I'm not holding my breath on the runs taking me longer, then the rooms I need to wait in. Though, if you do find such a challenge interesting, that'd be very useful.

Not sure what this means as I'm not familiar with these areas.  If you mean waiting, like for a boat or event to happen, then no, it's probably not something I would look to automate.  Best path would be to have a waypoint at the wait spot (system or personal depending on where it is) and then have a second one you could run to after the event.

> **Quote:**
> If there are any technical limits on the amount of spots players can store, limit those spots or add quests to get them. Then again, quests may be not a scalable option, if there are lots of areas that need a restriction.

I imagine we'd come up with some sort of limitation to prevent players from putting them everywhere.  Actual datasize of a waypoint would be something like of 9 bytes + 1 byte per character in the name.

> **Quote:**
> Maybe it's my perception, but I do get caught often, if I don't make precautions. Is it really 10 seconds, not 1-2 seconds?

It should be 10 seconds.  Not all the mobs are processed at once so if you're in a room with multiple mobs their 10 second check happens at different times to make the game run smoother.

> **Quote:**
> Yes, the whole idea is to make the run be fast, maybe 50ms per room. Aardmud run command moves at about 3 rooms per 250ms. 100ms per room might be acceptable.

We could probably do this.  Easiest first pass would be to do it in bursts (2-3 rooms every 250ms) but it may be possible to make it more even.

> **Quote:**
> Can you make aggro mobs fast-to-attack running ppl, so the aggro rate is the same, compared to walking ppl? Any ideas about this?

We can run a check when the player enters the room to see if they're running and give the mobs some sort of chance to jump early.

> **Quote:**
> Thus, players run where the command takes them. If they forgot wb and decided to run to poseidon's realm, their fault.

Not very newbie friendly.

</div>

<div class="post" data-post-id="36424" data-author="*Breeze*" data-date="2016-01-06T20:02:21+00:00" data-subject="Re: Add Fastrun to the MUD to kill mobs faster">

#

We can run a check when the player enters the room to see if they're running and give the mobs some sort of chance to jump early.

#

would go well with the idea I had to add in dodge/agility stats.

</div>

<div class="post" data-post-id="36431" data-author="Teron" data-date="2016-01-07T11:24:12+00:00" data-subject="Re: Add Fastrun to the MUD to kill mobs faster">

**Splork**/**Crumbs**, in short, fastruns means that:

- newbies need to learn areas to go and dirs to get there

- newbies run to areas faster and easier

- start killing faster and progress faster, engaging better with the MUD.

(I agree that the exp side won't be that noticeable, it's more convenience, than exp.)

So it seems that we do need a good help on newbie areas and possibly more signs in newbatia to exp areas for real newbies to actually need fastruns.

For example:

help newbie should include a mention of a new command, areas, or help areas

help areas - a list of areas by difficulty/player level, probably with dirs

help areaname (help daar): a description of an area, suggested levels, directions

In this context, fastrun would be most useful, because newbies would have smth to pick from.

As for other muds, yes, there's a system that helps newbies choose mobs: it tracks mobs killed by level and lets players search/refine mob list by level/align. Here, it'll work for newbies, but will be mostly useless for mobs for 2x40+ and above.

As for fastrun itself, here's the summary:

- help areas give dirs to newbies

- newbies run to areas faster and easier

- start killing faster and progress faster, engaging better with the MUD

Essentially, the newbie college helps newbies to go from "What do I do here?" to "What else can I kill to gain levels?"

The help system above will get them from "what do I need to kill?" to "how do I get there?"

Fastrun is a smooth transition from "how do I get there?" to "start killing".

I guess, admittedly, college and help areas would be more useful, but I didn't say I had a plan - I sent it to JB earlier, anyway. I simply had a random idea that someone already had and I wanted to suggest it before I've forgotten about it.

**Splork**, 

If we want to make things easier for newbies to start, they can fastrun to newbie areas w/o visiting them earlier.

If we agree that players need to visit an area before being able to fastrun, enable it for 100% exploration of an area, as long as there are no unconnected rooms. (Though Undead City comes to mind, where there's a quest area. That might even limit the fastrun users further.)

In my groups, people don't run to areas far area for me. Maybe with fastruns they'd do it. Also, fastrun spot is helpful in this regard, as it allows to run to an area after you logged in and you haven't set a beacon. I still think it'd add something unique to this mud. If fastrun spot is a powerful feature, it can be limited with an autoquest+100% exploration or limited in number of spots per character (3-5).

As for comparing fastrunning with aliases, let me remind you that fastrunning is supposed to be several times faster, than running. Speed running is so important to me that I am/was going to create additional, personal, faster-moving aliases, than I'd use for a group. So fastrun would still improve the game even for those, who use aliases.

As you can see above, one of my arguments is to keep the aggro element, as I agree it's useful. Which is why I asked for ways to solve this and Teker confirms it's possible to keep the chance to get aggroed similar/the same as compared to walking.

I have no idea how much effort/time this feature needs and how it compares to other features in this regard. Maybe we need to estimate possibly retention % from this feature and divide it by hrs spent on the feature and compare the number to other features.

I estimate that:

- a newbie college with proper signs should increase conversion by 30%

- help areas with dirs will increase conversion by 5-10%

- fastrun should increase retention at lower levels by 3-5%.

How much time this will take is on Teker, but I guess a newbie college needs weeks of work - no idea how much hours that is.

Also, another way to know what to do, besides estimating conversions, is to actually ask mudders what they look for in MUDs and ask them to grade their needs on importance. This can be done on the forums, but I think we need a more scalable approach: a link to a G.Docs form that we can ask feedback on numerous MUD forums.

</div>

<div class="post" data-post-id="36433" data-author="Teron" data-date="2016-01-07T13:13:21+00:00" data-subject="Re: Add Fastrun to the MUD to kill mobs faster">

Teker,

> **Quote:**
> I think these could be done as a single item where "waypoints" are saved to the database as either "global" or "personal". I would probably use the same "run <waypoint>" command and allow players to override the global waypoint by specifying one with the same name.

That'll work, I guess, though what if a player has a spot in an area and still wants to run to its entrance? 

Re: waiting in areas. Yes, waiting means coming to a room and waiting for an event to happen, e.g. moving down through a waterfall in UD2 or waiting for you to be devoured by the flame in Midgaard.

> **Quote:**
> I imagine we'd come up with some sort of limitation to prevent players from putting them everywhere. Actual datasize of a waypoint would be something like of 9 bytes + 1 byte per character in the name.

So there's no actual technical limit. Nice :-)

> **Quote:**
> **We can run a check when the player enters the room to see if they're running and give the mobs some sort of chance to jump early.**

Nice, so we can keep the aggro mobs aggro, so Splork, just as I, should be content with this.

> **Quote:**
> Thus, players run where the command takes them. If they forgot wb and decided to run to poseidon's realm, their fault.
> 
> 
> 
> Not very newbie friendly

Well, my idea was only to speed up the runs.

If we want to make them safe, then you definitely don't want to move past rooms that require flying and you don't have it.

As for waterbreath, I don't see great immediate danger.

You can run through an area underwater w/o waterbreathing. You will be losing hps, but you'll make it. As for Poseidon's specifically, there are a few air rooms (Hermind, Mind) that players can stop by and recast. Or shift to frog and reshift/wb selves. 

As far as I remember, there aren't newbie areas that require waterbreath before entering them. Valk Waterfall doesn't need wb early on and you need wb in Kuo-Toans/Sahaguins right after the entrance. Lycanthropia has a waterbreath area at least 5 rooms after the entrance.

Same for flying: you don't enter Clouds w/o flying, that is all.

So I'd suggest to stopping before rooms that require a person to fly or have a boat (and stopping the run there) and not doing anything about waterbreath, since newbies run to areas that don't need waterbreath and you only need wb either in high level areas or after entering the areas (Tower temple) - ie, if you run to a spot. But if you run to a spot that you set, you ought to know better, imho.

</div>

<div class="post" data-post-id="36435" data-author="*Splork*" data-date="2016-01-07T16:26:16+00:00" data-subject="Re: Add Fastrun to the MUD to kill mobs faster">

I believe that players should have exploration to 100% before they would ever be able to use a feature like this. This belief directly counters your initial ideas regarding the feature because you stated it would make it easier for real newbies to find areas to play in. I've already countered this thought process in my last post because these types of players simply do not possess the knowledge to use the feature. Although, this isn't much different from features like advice and others which newbies just don't know about...

        Why is it a good idea, new player or old, to allow players to automatically run to areas they have no previous  knowledge of or the danger that possibly exists there?  This would be a recipe for disaster. On that thought process:

> **Quote:**
> o I'd suggest to stopping before rooms that require a person to fly or have a boat (and stopping the run there) and not doing anything about waterbreath, since newbies run to areas that don't need waterbreath and you only need wb either in high level areas or after entering the areas (Tower temple) - ie, if you run to a spot. But if you run to a spot that you set, you ought to know better, imho.

Why should we be coding skills which protects the players using them? Should we go back to shadowwalk and make sure it cant go into water without waterbreathing? Should we add checks to backstab and make sure you can actually kill the mob before you stab it? Where does this thought process begin and end?

> **Quote:**
> As for comparing fastrunning with aliases, let me remind you that fastrunning is supposed to be several times faster, than running. Speed running is so important to me that I am/was going to create additional, personal, faster-moving aliases, than I'd use for a group. So fastrun would still improve the game even for those, who use aliases.

I am a bit baffled that you are acting like it takes a minute to run anywhere on this game. My best guess is that the average aliased run takes less than 10-15 seconds real time. To me, saving time really isn't an argument here because you are really saving about 5-10 seconds at best, and that would be if we cut runs in half with this feature.  It would have a huge impact on those players who don't know areas and runs but do we really want that?

> **Quote:**
> In my groups, people don't run to areas far area for me. Maybe with fastruns they'd do it. Also, fastrun spot is helpful in this regard, as it allows to run to an area after you logged in and you haven't set a beacon. I still think it'd add something unique to this mud. If fastrun spot is a powerful feature, it can be limited with an autoquest+100% exploration or limited in number of spots per character (3-5).

This is most likely because they are either lazy, don't know the areas, are afraid to die, or don't have the runs aliased. Why should we make it easier for these players? They aren not LEARNING anything by typing fastrun demonweb. They learn by actually running to the areas by themselves, or with guidance from other players, using the website maps to help them, etc.  One of the biggest complaints I hear about players is that lowbies are brought up with a silver spoon in their mouth and don't even know the most common area runs. Is this going to help with this issue or make it even worse?

> **Quote:**
> As you can see above, one of my arguments is to keep the aggro element, as I agree it's useful. Which is why I asked for ways to solve this and Teker confirms it's possible to keep the chance to get aggroed similar/the same as compared to walking.

We all already knew this, its how we do it thats vital. Does anyone really want us adjusting the aggressive timers on all in-game mobs just to add this feature? I'm not sure how many of you remember the uproar when we changed aggressive timer to be random, per mob, every 10 seconds and not ALL mobs being aggressive every 10 seconds ( when we could time runs through aggressive areas without ever being hit ) Do we simply trigger a new set of aggressive protocols for mobs marked as running? Do we address the issue another way entirely...

I actually like the idea of the skill ( for the most part ). I don't like the "2nd iteration" idea of it. It impedes on existing skills/features. It would have to be severely limited before we considered it and some suggestions have already been made regarding this.

This also has a huge effect on corpse retrievals and death in general. Plenty of times people die and people can't get to them because nobody knows the run well enough. Well hell, just type fastrun demonweb and save the person. Without proper implementation, a skill like this removes a ton of danger and excitement from the game... and I don't like that.

</div>

<div class="post" data-post-id="36439" data-author="Teron" data-date="2016-01-08T16:04:17+00:00" data-subject="Re: Add Fastrun to the MUD to kill mobs faster">

> ***Splork* wrote:**
> I believe that players should have exploration to 100% before they would ever be able to use a feature like this. This belief directly counters your initial ideas regarding the feature because you stated it would make it easier for real newbies to find areas to play in. I've already countered this thought process in my last post because these types of players simply do not possess the knowledge to use the feature. Although, this isn't much different from features like advice and others which newbies just don't know about...

**Splork**, as I said, there needs to be an adequate amount of signs and help to guide newbies to the areas, which they can run to.

Also, to make fastruns available to newbies and not available to others we can:

- allow fastruns w/o exploration on Valk

- allow fastruns w/o exploration to 1-20lev areas on other continents (penguin tower, asylum, kobolds, jungle, quicklings, lycanthropia, sewers, kings bazaar, AH beach, gremlyns, etc)

- allow free fastruns to our most used temples: Nia, Splork, Ming, Alana, Enea

- require complete exploration for fastruns to other areas

- require exploration and a completion of an autoquest for a runto spot

> **Splork wrote:**
> Why is it a good idea, new player or old, to allow players to automatically run to areas they have no previous  knowledge of or the danger that possibly exists there?  This would be a recipe for disaster. On that thought process:
> 
> 
> 
> Why should we be coding skills which protects the players using them? Should we go back to shadowwalk and make sure it cant go into water without waterbreathing? Should we add checks to backstab and make sure you can actually kill the mob before you stab it? Where does this thought process begin and end?

I don't understand. Do you want to keep the danger of running to areas or not?

I think I've written enough that it should be obvious my intention was to keep the danger level *the same* as it is now, when you walk. Given your previous posts, I'm assuming you want to keep the danger, which is what Teker can do. Running to a dangerous area is as dangerous to walking to a dangerous area.

Now, as long as the danger level of running is the same, I don't see a problem here. And I am not starting the process of making it safe, Teker made a comment in this regard. If the majority opinion - yours and mine and maybe others - in this case is for danger, not against it, then we don't stop ppl b4 chasms and waterbreath areas. Or you can apply this to players of 20 prime and under. 

Also, if a player decides to go to an area, he can walk there or run there. Changing the means of transportation (a walk, a run, or a horse or even a unicorn) doesn't make an area any more or less dangerous.

> **Quote:**
> I am a bit baffled that you are acting like it takes a minute to run anywhere on this game. My best guess is that the average aliased run takes less than 10-15 seconds real time. To me, saving time really isn't an argument here because you are really saving about 5-10 seconds at best, and that would be if we cut runs in half with this feature.

I've just measured a run to the Jungle of Sess'Inek. It took 27 seconds. A run to the Moors - a newbie area - is longer. A run to the Tower of Gr'vald is even longer. If it gets cut to 10 seconds, I'll be glad.

A run to On the Webbed Spiral Stair is 22 seconds with both runs, to the entrance and internally, stacked.

Yes, cutting the time from 20+ seconds to 8 seconds would be noticeable and useful for me. As I said, I am intending to add a whole bunch of aliases just to speed up my runs. For others, it should be a similar convenience, but I'm not sure they notice or argue about it now, but it'll be interesting to see their reaction afterwards.

To see why I want speed, find a website that takes 20 seconds to load. Then make it load in 8 seconds. Then in 1 second. Which one do you want to use and which one you'll abandon before reading?

> **Quote:**
> It would have a huge impact on those players who don't know areas and runs but do we really want that?

This is related to the newbiness of ppl. If they know runs, they can kill more mobs and actually get moving.

Yes, that's precisely the point: to get ppl to the mobs instead of them walking like turtles to an area.

If we limit free fastruns to newbies, then it'll help only them, for the most part.

If you want the player to walk the run and, though, to be honest, it's a sort of an accomplishment to make an alias that takes you to On the Webbed Spiral Stairs w/o a bump in a wall, then earning a fastrun spot could require getting to the spot from recall in the minimal time, say, to be in top 50% of runners to the area:

- say, 20 ppl take a quest to get a spot for the area

- 20 ppl run to the area for speed

- 5 ppl make it under 25 seconds, 5 ppl make it in 25-30 seconds, 5 in 30-40, 5 in 40

- top 10 fastest ppl get the runto spot.

This way, we:

- ensure players get the spot only if they know the run

- add another mini-competition to the game

- limit the amount of spots used at any time.

However, if this tidbit does go in, there has to be a larger limit on total spots to run to. Also, given that this competition does require coding, it should be simpler to just limit the amount of spots. That being said, we can set a limit first, and add quests in iteration #3.

> **Quote:**
> This is most likely because they are either lazy, don't know the areas, are afraid to die, or don't have the runs aliased. Why should we make it easier for these players? They aren not LEARNING anything by typing fastrun demonweb. They learn by actually running to the areas by themselves, or with guidance from other players, using the website maps to help them, etc.  One of the biggest complaints I hear about players is that lowbies are brought up with a silver spoon in their mouth and don't even know the most common area runs. Is this going to help with this issue or make it even worse?

If people get used to fastruns and require exploration after valk to get to their areas, they'll be more likely to explore those areas. If we require running to an area under average time, then they'll need to learn the runs and make fast aliases.

If we limit fastruns to 100% exploration to non-newbie areas, in the worst case scenario, this won't change a thing in terms of ppl learning runs: most ppl won't do it and will continue to be w/o aliases or runs. However, if ppl do decide to use fastruns, we'll get ppl to explore the areas completely - this should be a win and an imm's book, imho.

I don't see a problem here other than boosting exploration %.

> **Quote:**
> We all already knew this, its how we do it thats vital. Does anyone really want us adjusting the aggressive timers on all in-game mobs just to add this feature? I'm not sure how many of you remember the uproar when we changed aggressive timer to be random, per mob, every 10 seconds and not ALL mobs being aggressive every 10 seconds ( when we could time runs through aggressive areas without ever being hit ) Do we simply trigger a new set of aggressive protocols for mobs marked as running? Do we address the issue another way entirely...

This is a technical question to Teker, though I believe he had already written that this change can apply *only to those running*. If the change makes fastrunning more dangerous, than walking, then we'll either take it or argue about it and arrive at a solution that works. However I am led to believe the danger level should remain the same.

> **Quote:**
> I actually like the idea of the skill ( for the most part ). I don't like the "2nd iteration" idea of it. It impedes on existing skills/features. It would have to be severely limited before we considered it and some suggestions have already been made regarding this.

I agree that the fastrun spot idea can be discussed and a limit put on it. Atm, there are several ways to do it:

- require 100% exploration, same as for the fastrun

- require an autoquest to complete

- limit total amount per player

- allow only the 50% faster runners to the area get the spot

- give top 3 players by monthly leadership 3 extra fastrun spots (or the inverse of their place: 1st place gets 5, 2nd gets 4, 3d gets 3, 4th gets 2, 5th gets 1)

- give every top leader by exp in the level bracket an extra fastrun spot for a month

> **Quote:**
> This also has a huge effect on corpse retrievals and death in general. Plenty of times people die and people can't get to them because nobody knows the run well enough. Well hell, just type fastrun demonweb and save the person. Without proper implementation, a skill like this removes a ton of danger and excitement from the game... and I don't like that.

If a person died in an area outside the entrance room, fastrunning demonweb won't help: you have to find the room you are running to. Also, even if you die on the fastrun in DWeb, someone will have to use a run alias to save you, because stopping fastrun, if it is there, will be unreliably imprecise.

Also, even if you can use a fastrun to save a person outside Valk, you had explored the area already. 

As for danger:

- we keep the danger level the same while running

- fastruns are available only to those with 100% exploration for an area

- fastruns for CRs only speed up the run by 3-10 seconds, because the person w/ the fastrun already has 100% exploration of an area

- fastrun doesn't run to the mob that killed or looted someone, you have to do it yourself.

Even if you do believe that fastrunning will somehow help CRs, getting back EQ easier is what would make the MUD more playable, in the same vein, but not scale, as adding bonus exp for 40's. In this regard, fastruns won't help, because they don't take the runner to the mob. They will help, because they will make ppl explore the areas, if they do this at all.

</div>

<div class="post" data-post-id="36441" data-author="*Splork*" data-date="2016-01-08T19:08:34+00:00" data-subject="Re: Add Fastrun to the MUD to kill mobs faster">

You are reading but not understanding what I am saying, which is fine. 

I've stated my thoughts and concerns and there is a ton of good conversation being bantered about.

Good stuff...

Enjoy,

</div>

<div class="post" data-post-id="36444" data-author="Teron" data-date="2016-01-09T08:28:18+00:00" data-subject="Re: Add Fastrun to the MUD to kill mobs faster">

Splork, I see that you want more active exploration and travelling, than fast running. I like the idea, too, but in my mind, slow random walking is what can drive the newbies in despair, if they don't find what to kill. Questions  "What do I kill after college" or "what do I kill on bh for xp?" are asked too often to be ignored, as well, meaning that this exploration *does not work*. No one visits the old library any more. Or knows about it.

Also, don't existing runs, printed on the maps and on the website, hurt natural exploration from the South Gate?

Does it mean that my suggestions of a more informative help system of what and where to kill will hurt this, too?

Once you create an area run alias from a map, you are no longer an explorer, you aren't reading the room descs or even room names, you simply want to get from A to B. Fastrunning will only speed this up.

Still, I'd prefer you clarify your point of view, because clearly I am not getting something.

</div>

<div class="post" data-post-id="36446" data-author="*Breeze*" data-date="2016-01-09T14:33:11+00:00" data-subject="Re: Add Fastrun to the MUD to kill mobs faster">

more informative help files per area would be a useful/awesome thing that would help people decide what to kill after newbie school and even help older players remember areas they haven't run in awhile..  players can write them and submit to us and we can add them in.

we could even display a message after they leave newbie school that points to the new help files as an index and they can read on from there.

</div>

<div class="post" data-post-id="36467" data-author="*Breeze*" data-date="2016-01-15T20:06:23+00:00" data-subject="Re: Add Fastrun to the MUD to kill mobs faster">

no takers?

</div>

<div class="post" data-post-id="36477" data-author="Teron" data-date="2016-01-16T13:25:43+00:00" data-subject="Re: Add Fastrun to the MUD to kill mobs faster">

I am going to do it, just not sure when. Guess I need to plan better.

</div>

<div class="post" data-post-id="36479" data-author="*Splork*" data-date="2016-01-16T15:01:31+00:00" data-subject="Re: Add Fastrun to the MUD to kill mobs faster">

We've spoke about doing a system very similar to what Taron has suggested many times, it really comes down to the vast amount of work it actually takes.

Ultimately, something which gave specific information about every area would be ideal such as:

Area Name:  Name of area

Run: run from recall point

Levels: Levels the area is ideal for ( we know this isn't perfect )

Difficulty: easy, hard, extremely hard, high avatar

Type: solo/small group/large group/ etc

Aggressive: etc etc

You get my point. From there we would have cmds where players would pull up all the areas which have the different requirements they are looking for, and on and on...

Its definitely something which we could add to over time but I honestly don't see something like this ever being completely finished:)

</div>

<div class="post" data-post-id="36487" data-author="Teron" data-date="2016-01-16T18:33:31+00:00" data-subject="Re: Add Fastrun to the MUD to kill mobs faster">

Since the amount of areas is limited, the helpfiles can be written - all it takes is dedication, planning and perseverence.

It just takes lots of time, just as with creating lots of different mobs - as you've told me recently.

</div>
