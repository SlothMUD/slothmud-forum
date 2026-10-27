---
title: "Re: order changes for shifted druids"
topic_id: 1577
author: "Deju"
date: 2005-11-28T18:19:54+00:00
last_activity: 2005-12-02T02:56:06+00:00
last_author: "dezakin"
sticky: false
locked: false
post_count: 42
---

<div class="post" data-post-id="9657" data-author="Deju" data-date="2005-11-28T18:19:54+00:00" data-subject="Re: order changes for shifted druids">

Hi -

I understand the change that keeps shifted players from ordering followers... i dont like it, but i understand it <img src="/images/smilies/icon_e_smile.svg" alt=":)" title=":)" width="15" height="15" class="smiley nozoom">

However, that said... I have a problem with the fact the the Juju almost ALWAYS disengages when a shifted player attacks a mob the Juju is already killing. So if i order the juju to kill sash, then shift and join in the killing, the juju stops fighting the sash. How am I to get the juju to engage again? In the middle of a fight, am i supposed to shift return, order the juju to fight, then shift back? To me, this seems a little silly.

Perhaps this is just a bug, I don't know. But if this is by design, it combined with the new order changes seem overly harsh.

Just curious if this was overlooked, or if its by design.

Thanks,

Deju/Scrugg

</div>

<div class="post" data-post-id="9658" data-author="12345" data-date="2005-11-28T18:31:42+00:00" data-subject="">

If I read the announcement correctly, it was changed so that you can't be shifted and use undead followers at the same time, so I think that's by design. However, I think that's why order lag and order failure rates and such were added as well, so having both in the game does seem rather harsh.

</div>

<div class="post" data-post-id="9659" data-author="kjartan" data-date="2005-11-28T18:55:26+00:00" data-subject="">

We took out most of the order lag when we made the change to disallow ordering of undead followers.

I don't know why the juju disengages; does he disengage if you don't attack the sash but just stand there, shifted or not? I wonder if somehow the code that was supposed to keep mobs from fighting each other is getting mistakenly applied to the juju.

By the way, we're working on fleshing out nature's familiar. It won't be as good as summon undead, but I am adding another half dozen or so mobs that are better than treants, some mobile, some rooted. We're also going to add the requirement that to cast it you must be somewhere with greenery, which means either one of the forest-type terrains or else at least have a 'brambles' or 'canopied arbor' effect. And we'll be changing the name of the spell, probably to 'awaken', but you won't need to relearn it.

Also, I noticed that the 'summon undead' mobs that require 2x40 or 3x40 for necros don't start counting forties with your necro class (like supplication) but count all your forties - I am going to change this, which I think is probably how it was originally intended, which means an avatar Necro-fourth won't have access to the top few summon undead mobs any longer, only necro primes will ever get the full list.

</div>

<div class="post" data-post-id="9660" data-author="Leaf" data-date="2005-11-28T19:07:45+00:00" data-subject="">

> <strong>\*kjartan\* wrote:</strong>
> By the way, we're working on fleshing out nature's familiar. It won't be as good as summon undead, but I am adding another half dozen or so mobs that are better than treants, some mobile, some rooted.

Suggestion ... Rock Golem to Iron Golem!!! DIABLO 2 LOD!!!

> <strong>\*kjartan\* wrote:</strong>
> Also, I noticed that the 'summon undead' mobs that require 2x40 or 3x40 for necros don't start counting forties with your necro class (like supplication) but count all your forties - I am going to change this, which I think is probably how it was originally intended, which means an avatar Necro-fourth won't have access to the top few summon undead mobs any longer, only necro primes will ever get the full list.

I can see alot of ppl with Necro in class order bitch about this one ...

Just like when Mages/Clerics had Summon undead taken away. They 

should have access to those mobs, cause of the lvl they have...

</div>

<div class="post" data-post-id="9661" data-author="Deju" data-date="2005-11-28T19:11:04+00:00" data-subject="">

ok, i did some further testing:

in all cases, i ordered juju to kill sash first.

not shifted, just stood there: juju fights

shifted, just stood there: juju fights

not shifted, jumped into fight: juju fights

shifted, jumped into fight: juju disengages

So it seems like only when a shifted player gets into the fight is when the juju disengages.

If there is anything i can do to help you diagnose it further, i'd be happy to help.

Thanks,

Deju/Scrugg

</div>

<div class="post" data-post-id="9662" data-author="Lis" data-date="2005-11-28T19:19:23+00:00" data-subject="">

> <strong>Leaf wrote:</strong>
> > <strong>\*kjartan\* wrote:</strong>
> > Also, I noticed that the 'summon undead' mobs that require 2x40 or 3x40 for necros don't start counting forties with your necro class (like supplication) but count all your forties - I am going to change this, which I think is probably how it was originally intended, which means an avatar Necro-fourth won't have access to the top few summon undead mobs any longer, only necro primes will ever get the full list.
> 
> 
> 
> 
> 
> I can see alot of ppl with Necro in class order bitch about this one ...
> 
> Just like when Mages/Clerics had Summon undead taken away. They 
> 
> should have access to those mobs, cause of the lvl they have...

Necro-not prime already have less Undead Control cap, so already weaker summons. 

Next thing will be not to allow Druid-noprimes to have all list of forms?

</div>

<div class="post" data-post-id="9663" data-author="Guinex" data-date="2005-11-28T19:32:51+00:00" data-subject="">

When I order my undead to attack, and i just stand there I allways get sucked in and one drops out, this goes for the same if I just use a juju.

</div>

<div class="post" data-post-id="9664" data-author="kjartan" data-date="2005-11-28T20:47:10+00:00" data-subject="">

Ok, I'll have to get back to you on the disengage thing.

On second thought, scratch that business about necro non-primes losing undeads. Here's what I want to change: I don't want a Necro 4th to get several undeads all at once when he hits 40. I'll look at ways of handling this that don't end up totally losing access to a bunch of undeads. In fact it's tempting to apply the same reasoning to supplication, I'm not all that enamored of prime-only stuff.

Maybe something along the lines of counting an extra "40" at av 10, 20, and 30 so even if you're necro 4th, at avatar 30 you get the 4x40 undead. That would mean necro 3rd and 4th still lost the one topmost undead (swordwraith maybe?), but otherwise everybody can eventually get everything.

</div>

<div class="post" data-post-id="9665" data-author="Rynquald" data-date="2005-11-28T20:52:29+00:00" data-subject="">

> <strong>Quote:</strong>
> Maybe something along the lines of counting an extra "40" at av 10, 20, and 30 so even if you're necro 4th, at avatar 30 you get the 4x40 undead. That would mean necro 3rd and 4th still lost the one topmost undead (swordwraith maybe?), but otherwise everybody can eventually get everything.

That would \*rock\* if you applied it to supp (i could even just about cope with shift being like that since i'm druid second <img src="/images/smilies/icon_e_smile.svg" alt=":)" title=":)" width="15" height="15" class="smiley nozoom"> )

EDIT: Thanks for considering adding to nature's familiar btw.

</div>

<div class="post" data-post-id="9666" data-author="blackmore" data-date="2005-11-28T20:56:05+00:00" data-subject="">

> <strong>\*kjartan\* wrote:</strong>
> Also, I noticed that the 'summon undead' mobs that require 2x40 or 3x40 for necros don't start counting forties with your necro class (like supplication) but count all your forties - I am going to change this, which I think is probably how it was originally intended, which means an avatar Necro-fourth won't have access to the top few summon undead mobs any longer, only necro primes will ever get the full list.

I have no clue why you'd think that it was "originally intended" that way. The concept of levels after the class with the spell was never raised until you created supplication, so as far as we know (we of course don't know private conversations), that concept was never conceived of until then. Every other spell before supplication with level requirements used total levels, including shapeshift. There have been many adjustments made to both spells that if they were originally meant to work differently than they do, it would have been noticed a long, long time ago.

</div>

<div class="post" data-post-id="9667" data-author="kjartan" data-date="2005-11-28T21:05:09+00:00" data-subject="">

My memory of the multi-40 mobs for summon undead is that they appeared after supplication and were intended to be along the same lines as supplication. The supplication setup works better in the sense that you get the mobs in a progression, not in-a-progression-or-all-at-once-depending-on-classo.

</div>

<div class="post" data-post-id="9668" data-author="blackmore" data-date="2005-11-28T21:07:53+00:00" data-subject="">

Since my last post is already outdated (sort of)...

> <strong>\*kjartan\* wrote:</strong>
> Here's what I want to change: I don't want a Necro 4th to get several undeads all at once when he hits 40.

Yeah, I can definitely respect that.

> <strong>\*kjartan\* wrote:</strong>
> Maybe something along the lines of counting an extra "40" at av 10, 20, and 30 so even if you're necro 4th, at avatar 30 you get the 4x40 undead. That would mean necro 3rd and 4th still lost the one topmost undead (swordwraith maybe?), but otherwise everybody can eventually get everything.

Without really knowing much about summons, it still seems like that would cause a huge reduction in the methods certain players are using to play their character, and it doesn't seem like that's healthy. I may be overstating the issue, though, since there's only 3 undeads 3x40 or higher.

</div>

<div class="post" data-post-id="9669" data-author="Medios" data-date="2005-11-28T22:27:10+00:00" data-subject="">

It seems to me that undead control eq takes care of the undeads. Removing followers is almost like saying that non mage primes cant use firestorm anymore. Supplicants dont have any sort of eq so its understandable about the placement of cleric in the class. 

Can druids order supplicants while shifted? I dont shift and havent gotten anyone to test it, but it seems to me this follower is from your god, why wouldnt it listen to you? 

Lets talk about overpower. I remember the days when we used to get 4 liches and really kill some big mobs. I tell u what, 4 liches will eat 2 swordwraiths for dinner. That was removed and only necros were allowed to summon/animate. Now players have found out how to kill the bigger mobs again using soul infusions/animates/mobs fighting each other. So were back to square one. It seems to me if you didnt want players soloing then you shouldnt have put any followers in at all, removed the liches and left it at that. Ill have to agree with the point shadis brings up time and again. Solo chars on sloth will be nerfed. It happened to thieves back in the day and its happening to druids/necros now. 

I tend to feel that you can take any classo out there, even the quad nc. Allow someone like rick, strider, annie, or anyone in my guild for that matter to play it and you will have an overpowered char. I dont remember a character that rick played that someone hasnt bitched about. Its not so much the class as the ability and the mud knowledge of the player. If this is a way to make everyone make new characters all the time just come out and say it.

Mike

PS I hate the push to make every char wear ac. In traditional d\&d it makes no sense at all. With the new druid/necro nerf do you think more ppl will be shifting, or remaking chars with bard or something to wear ac to order.

</div>

<div class="post" data-post-id="9686" data-author="dezakin" data-date="2005-11-30T08:43:49+00:00" data-subject="">

> <strong>Quote:</strong>
> Without really knowing much about summons, it still seems like that would cause a huge reduction in the methods certain players are using to play their character, and it doesn't seem like that's healthy. I may be overstating the issue, though, since there's only 3 undeads 3x40 or higher.

Not really understating it. the 4x25 forms are essentially useless. Demiliches have no ac and allways bind/damn even if bound/damned. Phantoms have less hp than banshees and their pseudo blind proc is a joke that is very probably nullified by fog anyways.

And with zukt I've been looking forward to swords because zukt has no cleric, and without cleric he cant stone/iron his pets the way everyone else with cleric/bard/mage can. Given all the red potions mysteriously disappeared from the game, this would be even more painful.

</div>

<div class="post" data-post-id="9687" data-author="kjartan" data-date="2005-11-30T18:42:37+00:00" data-subject="">

If the intermediate forms are actually useless for some reason, I'd like to fix that. (Note this applies to undeads, not to supps - I deliberately designed some of the supps to be pretty useless, and others aren't finished yet.) I'll have a look at the demilich proc for starters.

Right at the moment we are having some stability issues so I am not working on this stuff; I'll get back to it this weekend probably.

</div>

<div class="post" data-post-id="9688" data-author="12345" data-date="2005-11-30T20:19:56+00:00" data-subject="">

Out of curiousity, why were the red potions removed? It was only mildly annoying when I realized it since I already had a bunch of equipment to hand down to my Valker, but I've frequently suggested that newbies buy them to make their early levels less painful. Not that everyone in the mud isn't a cleric already... but this only seems to solidify that.

</div>

<div class="post" data-post-id="9689" data-author="Deju" data-date="2005-11-30T20:32:18+00:00" data-subject="">

> <strong>\*kjartan\* wrote:</strong>
> (Note this applies to undeads, not to supps - I deliberately designed some of the supps to be pretty useless, and others aren't finished yet.)

Maybe I am missing something here, but why would some supps be put ingame if they are useless?

</div>

<div class="post" data-post-id="9690" data-author="kjartan" data-date="2005-11-30T20:55:58+00:00" data-subject="">

I don't regret the Kachina.

</div>

<div class="post" data-post-id="9691" data-author="brand" data-date="2005-11-30T21:32:51+00:00" data-subject="">

> <strong>\*kjartan\* wrote:</strong>
> I don't regret the Kachina.

I also don't regret the Kachina.

post script: I do regret the Diva.

</div>

<div class="post" data-post-id="9692" data-author="*Splork*" data-date="2005-11-30T22:38:33+00:00" data-subject="red potions">

None of us removed red potions, if they are gone its a glitch somehow.

Where and what shops were they located at?

Splork

</div>

<div class="post" data-post-id="9693" data-author="12345" data-date="2005-11-30T22:44:49+00:00" data-subject="">

The Valk potion shop had them. 3n2en of recall.

The BH potion shop also had them. e3nw of recall.

Those are the only two I saw, I assumed the ones on AH and SS had followed suit. I don't recall if the dull gold potion was always sold on Valk, but I remember being kinda surprised to see it.

</div>

<div class="post" data-post-id="9695" data-author="deucer" data-date="2005-11-30T23:30:40+00:00" data-subject="">

I've been playing Sloth since this summer, created a necro prime character since that is what interests me from playing the original D\&D. During that brief time I've experienced at least two downgradings of the necro classo, as far as I can tell from the level of my pc, in the hp of the juju zombie. The last one was harsh, my juju dropped 15% in hp's, if you take into account i'm still playing a 1x40 pc. Far from motivating to continue playing the classo. In addition, the juju doesn't advance in hp to the same extent anymore after leveling. So I agree with Medios' post on several items he brings up. If solo characters are not allowed to cycle bigger mobs than those from classo's that are not intended for soloing, why create followers or have the class in the first place. If players adapt their strategies to be able to handle a biggie, don't change the rules. It's not that small group of necros that is going to imbalance the total game. It's simply called growth and experience. Now, instead of rewarding those solo players with normal level advancement, they get nerfed. An example ? I play at least 5 days a week, for 5 hours at least, more during weekends. Being a careful (or slow or bad) player i manage to scrape together 40M exp when I'm lucky, barely enough to reach lvl 33 secondary. Doesn't seem like overdoing it in necro powerplay. Using the finger command (thank you imms <img src="/images/smilies/icon_e_smile.svg" alt=":)" title=":)" width="15" height="15" class="smiley nozoom"> very informative ) I notice level 20 players to hoard 100-140 M exp a week and leveling like mad, by joining vast groups... I don't mind. Some of them will still need their hands held when reaching 3x40 <img src="/images/smilies/icon_razz.svg" alt=":P" title=":P" width="15" height="15" class="smiley nozoom"> and be asking for the run to the guild. Medios has a good point, stating that highly experienced players will probably make any classo look overpowered when they play it. Nerfing a solo classo has tougher consequences to the player than for the typcial non-solo ones.

I don't mind pthieves - I keep a clean inventory - but I do mind running uphill in the sand, trying to develop a character and seeing the rules changed to a clear disadvantage. 

Excuse me if it looks like venting an opinion, I feel strongly about my in silico character, even if it's one that plays with corpses and ghosts.

On the other side, Sloth is top, and it has a good team of dedicated, well-meaning imms. Only a pity we don't have a vote reminder. <img src="/images/smilies/icon_e_biggrin.svg" alt=":D" title=":D" width="15" height="15" class="smiley nozoom"> 

See you ingame.

Deucer aka Zuuul

</div>

<div class="post" data-post-id="9696" data-author="*Splork*" data-date="2005-12-01T00:53:57+00:00" data-subject="potion bug fixed on reboot">

Alright, I snooped a keeper mob and found out that kj is indead making smarter mobs, even the keepers were grabbing the potions and ready to use them at any moment.

I have made it so that shopkeepers will not attempt to hold and use potions...

About Necromancers and Druids...

Please express your opinions, just be aware that we are trying our best to balance the game and keep it fair for everyone. I have never minded hearing people dislike or not agree with changes we have made, but I do take things to heart when people think we are intentinally trying to piss people off or screw someone over Because we definately are not. Like I just said online, simply type NEWS and see the mass amount of time, effort, and changes we have made for SlothMUD recently. The vast majority are extremely well liked and I am very happy with our Immortal team atm.

On a side note, we do not plan on anymore nerfings of these two classes. For the most part, I believe we are about as well balanced as we can be...

However, I still feel they are extremely powerful when compared to other classes, but I am fine with that, I will always believe that some classes and classos are simply better than others-and it should be that way.

Thanks for handing in ideas btw, I have a list that will keep me busy for a few more days...

Enjoy,

Splork

</div>

<div class="post" data-post-id="9698" data-author="Mosaix" data-date="2005-12-01T02:05:56+00:00" data-subject="">

Would be overdue to see Cleric Primes get some help. Supplication is nice, but overall we are at the bottom of the barrel. For the amount of help we supply groups, and literally keeping the mud alive each day, its time to "thank" Cleric Primes for their work. While I cant speak for every cleric prime, I would personally appreciate the help. 

Some thoughts I had. 

Giving one drachma for every raise a Cleric Prime performs sucessfully. That can be countered by loosing a drachma for every one failed. Keeping the raise formula as it is now. 

Since quest groups most always reward the tanks and leaders, it would be a nice gesture to the clerics that often get the short hand of the quest eq. We keep them alive and end up with junk or nothing at all. The drachma would allow us to over time reach the desireable quest eq that we fail to get quest drachma for. Or even regular quest eq when it is handed out.

A spell that increases mana regen by +1 or higher.

A spell that works like spectral shield, even if its watered down id take it.

A spell that makes clerics completely invisible to all mobs, say a wizinvis type spell. Reason being to get us in and out of areas to save those who are toast and need raising.

A spell that can make a cleric invincible to offensive magic spells cast on them for 1 tick. Crunchy clerics might be able to take out some mobs then.

A spell that boosts the efficency of the healbonus for the caster.

Have more mobs, and/or convert more mobs to be injured and damaged by heals cast on them so we can use our strenghts as a weapon. Evil/Undead mobs for example could be hurt.

Most of all, id love it if Cleric Primes could cast a spell that could at least be done to evil/undead mobs, if not all mobs, set them on fire for 2 ticks.

Be a great group spell. 

I love the mud, its fun, you guys do a fantastic job. Ive been here since 1994 and plan on being here for a while longer.

Cleric Prime needs some help......hook us up.....please and thank you <img src="/images/smilies/icon_e_smile.svg" alt=":)" title=":)" width="15" height="15" class="smiley nozoom">

Mosaix

</div>

<div class="post" data-post-id="9700" data-author="Weasel" data-date="2005-12-01T02:41:46+00:00" data-subject="">

<img src="/images/smilies/icon_eek.svg" alt=":shock:" title=":shock:" width="15" height="15" class="smiley nozoom">

</div>

<div class="post" data-post-id="9701" data-author="Cami" data-date="2005-12-01T03:25:22+00:00" data-subject="">

Mosaix rocks!

I agree that Clerics could use some help, and I love those suggestions. I would be thrilled to see even 1 or 2 implemented. Every little bit helps. It's pretty tough for Cleric primes right now, without a lot of external reward. 

Thanks for the great ideas Mosaix, I hope they get a serious look.

</div>

<div class="post" data-post-id="9702" data-author="*Splork*" data-date="2005-12-01T03:53:53+00:00" data-subject="">

I hate to say it, but I really don't see us doing all too much more for clerics for quite some time. Kj is debating opening up more supplicants to cleric classes which are lower in the class order but besides that, its not really on the discussion board.

Our mud still revolves around the cleric class. Without it, you are simply going to struggle. 

Cleric class as a prime is not meant to be a soloer, if you can solo with them, great, but their purpose is to be a group character and help keep other people alive as well as raise them when they die. 

I have been debating amping servants hps and the proc rate on their prime spell weapon though...

Enjoy,

Splork

</div>

<div class="post" data-post-id="9703" data-author="Cami" data-date="2005-12-01T04:50:31+00:00" data-subject="">

Thanks for the reply and the honesty Splork. Sometimes it's nice just to know where things stand <img src="/images/smilies/icon_e_smile.svg" alt=":)" title=":)" width="15" height="15" class="smiley nozoom">

Clearly, cleric primes are not meant to be solo chars. But it's tough to be the cleric support when our mana doesn't stack up to other chars. Some of the suggestions by Mosaix address this, and almost all of his suggestions are group oriented, not helping the cleric solo.

I'm not sure why Mage/Cleric appears to get much more mana than Cleric/Mage, (and I'm not certain that's the case, just appears to be) when winds cost so much less than restores. When I'm in for heals, I'm tapped out fast, but when I'm blasting, I can much longer..so it would seem Clerics have the need of a way to boost mana/regen some how, to be better balanced.

A spell to boost mana regen, or a spectral shield type of spell for clerics, or even just cleric prime would help to balance that out.

These are just my thoughts, I feel like such a second class citizen at times. It's almost as though cleric primes really don't have many special skills to make them valuable. Mage/Clerics seem to raise as well as Cleric/Mage but they have the firepower boost, as well as more inherent mana. I'm not sure if the regen rates are higher.

I chose Cleric prime without knowing very much about this mud, and I've invested a lot of time in this char, but I would not recommend my classo now based on what I've seen and learned. That is why I think it needs a little something to balance it.

Cami

</div>

<div class="post" data-post-id="9704" data-author="Mosaix" data-date="2005-12-01T04:56:12+00:00" data-subject="">

Clerics do a lot of work for the benefit of the mud and other players. Thats fine its part of the reason why I picked the classo that i did.

Its time for the work and time spent to match up to some sort of fun/reward.

Thanks.

Mosaix

</div>

<div class="post" data-post-id="9705" data-author="Qa" data-date="2005-12-01T05:03:05+00:00" data-subject="Clerics">

> <strong>\*Splork\* wrote:</strong>
> I have been debating amping servants hps and the proc rate on their prime spell weapon though...

Cleric primes need something. Take a look at my death rate trying to pop myself Avatar Attack SBs. It's so brutal even Frost was surprised.

Please consider doing something. Either dial us up, or nerf everone else.

Qa

</div>

<div class="post" data-post-id="9706" data-author="Mosaix" data-date="2005-12-01T05:14:10+00:00" data-subject="">

Frankly this stuff is the main reason i didnt play from July to November of this year. Got tired of the same ol same ol. And additions or upgrades for the cleric primes are not going to effect hardly anyone anyway...... so......please take a long serious look at what can be done. 

Mosaix

</div>

<div class="post" data-post-id="9707" data-author="_edd_" data-date="2005-12-01T10:11:34+00:00" data-subject="">

Drachma raise idea isnâ€™t so bright because it will push people to abuse to buy some drachma stuff. I think it would be better to add more Cl Prime drachma eq to Weaverâ€™s shop and put more quests (regular or special) to allow people earn more drachma.

Regen spell, spectral shield or equal spell for clerics and other casters and spell to boost the efficiency of the healbonus are good ideas. Iâ€™d be glad to see immortals take it up.

Ma/Cl shouldnâ€™t get more mana/maregen then Cl/Ma except the case you have low Ins or Wis. As I know some tert and quad classes give you mana when you gain levels and other classes donâ€™t. So that should be a reason in different amount of mana. (In other words ma/cl/dr/ne will always has more mana then cl/ma/wa/th).

And about strong and weak classes: after all my whinings I still play ma/cl/wa/th though nowdays it isn't strong classo but I can say I enjoy my playtime a lot. Once I've won RPG (don't remember name of the game, it's one from wich Autolycos steals his picture) - so, i've won this game without any kill, it wasn't easy but it was FUN.

So don't calculate your slothlife, just pick up classo you wish to play and go ahead.

</div>

<div class="post" data-post-id="9708" data-author="*Splork*" data-date="2005-12-01T12:25:04+00:00" data-subject="">

A few observations;

"I'm not sure why Mage/Cleric appears to get much more mana than Cleric/Mage, (and I'm not certain that's the case, just appears to be) when winds cost so much less than restores"

Mage/cleric gets 1 more mana than a cleric/mage with same stats.

"A spell that works like spectral shield, even if its watered down id take it. "

 or

"A spell that can make a cleric invincible to offensive magic spells cast on them for 1 tick. Crunchy clerics might be able to take out some mobs then. "

Spellshield basically accomplishes this already. Ive yet to see a mob which can blast down a full spellshield in less than a tic....

"A spell that works like spectral shield, even if its watered down id take it. "

We try not to add similar spells or skills to classes anymore, so this is basically out of the question.

The drachma idea could never happen at sloth. Two friends would get together and abuse the hell out of this within an hour of me adding it ingame. One player would die-the other would raise, over and over, endless loop of drachma

However, I did give cleric primes quite a bonus on successful raises half year ago.

I will up the hps to aerial and increase the proc rate on mace tonight...

I also like the spell to increase mana regen a tad. But it would most likely be avatar spell so I dont see it affecting the majority of our playerbase...shrugs, maybe not...

Enjoy,

Splork

</div>

<div class="post" data-post-id="9709" data-author="Grue" data-date="2005-12-01T13:11:43+00:00" data-subject="">

I'd like to see an avatar version of the Dark Mace. We do it with lots of other prime skills/spells.

</div>

<div class="post" data-post-id="9710" data-author="Qa" data-date="2005-12-01T13:50:05+00:00" data-subject="">

> <strong>\*Splork\* wrote:</strong>
> I will up the hps to aerial and increase the proc rate on mace tonight...
> 
> 
> 
> Enjoy,
> 
> Splork

Thank you, I'll give it a try shortly. <img src="/images/smilies/icon_e_smile.svg" alt=":)" title=":)" width="15" height="15" class="smiley nozoom"> 

Qa

Edit: Err, thanks in advance. <img src="/images/smilies/icon_e_wink.svg" alt=":wink:" title=":wink:" width="15" height="15" class="smiley nozoom">

</div>

<div class="post" data-post-id="9711" data-author="Shazuko" data-date="2005-12-01T13:55:17+00:00" data-subject="">

I'd like to see clerics get their own strength spell, even if its just a +1 bonus; without mage the only alternative is a necro spell thats got a -con penalty. When you dont have mage ( or necro for that matter), you need orange potions well into your 40's even if you have a nat 18/8x(str eq tends to lower ac)....although adding a cl str spell would benefit anyone with cl in their classo, I happen to have a cl prime who can solo pretty well, but he has ma for str, he would be at a disadvantage to have to use potions, or lose a pt of con when soloing to get his str up...

> <strong>Quote:</strong>
> (don't remember name of the game, it's one from wich Autolycos steals his picture)

That is a picture of sir chadwick moore, esq. standing in front of vermillion train station, in the city of Tarant..the game is Arcanum, and its an excellent rpg...

Shazuko Roku Ryuu

\<\~Chaos\~\>

</div>

<div class="post" data-post-id="9712" data-author="dezakin" data-date="2005-12-01T14:12:50+00:00" data-subject="">

I think the answer to give clerics happy time is to just make the tard dark mace do an occasional proc that feeds you mana, rather than cooked up new spells. Maybe even make it more 'group friendly' by proccing more often in groups, bigger groups having jacked up happy mana rate. Maybe tie it to the number of people joining a warcry.

But so that it doesnt get into overpower right away maybe start with a real low proc rate and tweak up as seen fit rather than nerf down. Maybe the happy mana proc only hits undead/demons like the regular dark mace proc. Or maybe it only procs on mobs with the opposite allignment since cleric has the pay attention to morality thing goin on.

Or make darkmace 'base' weapons that affect how the dark mace procs. So you get some special weapon that is normally pretty lame, say 1d8 or something, and cast darkmace while wielding it and it turns into a darkmace, but different 'base' weapons have different procs. Have it work sort of similar to a bards instrument.

Or maybe everyone thinks its a goofy idea.

</div>

<div class="post" data-post-id="9714" data-author="Weasel" data-date="2005-12-01T19:49:54+00:00" data-subject="">

How about giving WA primes some additional natural AC since that and HP are supposed to be the WA prime's main features, yet most other classos can achieve the same AC and/or HP and maybe more.. 

translation: whine whine whine whine whine blah blah 

Ignore me, I'm just stirring. <img src="/images/smilies/icon_twisted.svg" alt=":twisted:" title=":twisted:" width="15" height="15" class="smiley nozoom">

</div>

<div class="post" data-post-id="9715" data-author="Mosaix" data-date="2005-12-01T22:30:23+00:00" data-subject="">

I tend to not look so far ahead sometimes, but yes people would abuse the drachma idea so that wouldnt work. I didnt think of it in that light. 

Perhaps there is a way to award at least one cleric prime type of eq during a quest so that it gets to the healo?

I really really appreciate the ups to aerial and dark mace. I really like dezakins idea of making a avatar type dark mace that sucks in mana. That would be extremely cool. If not/also maybe the weapon stays in place until you remove it. In other words it doesnt poof when the spell ends.

I can agree to understand the thoughts on some of the other spells. The comments were fair. But if I may ask again to please make it possible for cleric primes to set mobs on fire. Would make grouping even more fun <img src="/images/smilies/icon_e_smile.svg" alt=":)" title=":)" width="15" height="15" class="smiley nozoom"> The spell doesnt even have to do all that much damage. Call me a pyro, just sounds like a spell a cleric might be able to cast. Again if only on evil/undead mobs. Also the total invis would be helpfull for us to run and save the masses. The handfull of cleric primes that would benefit from that shouldnt offest the mud too much, and it would make us more valuable as players to the mud as a whole.

Thanks for listening, and I truly appreciate the efforts made towards cleric primes. 

Also Weasel makes an excellent point in his last post. Frankly monks make better tanks now than a warrior does. That seems goofey.

Mosaix

</div>

<div class="post" data-post-id="9716" data-author="kjartan" data-date="2005-12-01T22:32:34+00:00" data-subject="demilich procs">

Ok, I am looking at the demilich, and it was casting some blast-type spells and some curse-type spells more or less randomly. It casts damnation, weaken, word of pain, destruction, a custom blast spell, and demon bind.

As I left it this morning, it only uses the curse-type spells if the target is \> 1000 hp, and in that case it mostly casts the curses until they stick. Once the target is \< 1000 hp or it is weakened, damned, and bound, then it switches over to blasting.

Given that it is using basically that set of spells, how would you like it to work? Should it even bother with weaken? How should it decide when to use curse-type spells and when to blast?

</div>

<div class="post" data-post-id="9717" data-author="Aleksey" data-date="2005-12-02T00:30:39+00:00" data-subject="">

Kj, problem not in what it cast or repeating binding ,damning ,problem mostly stands that you reaching av25 and geting not battle but exotic undeads

 phantom - same as banshee(3x40 level undead) but 100-150 hp less , exect same number attacks , exect same damage and +hit ,ac itd,banshee in advance got +damage proc, phantom just useless 2hit reduction proc, usualy dies in first fue rounds due to luck of hp(nowdays we have not that ammount of undeads to afford kamikadze mob whose mission psudo blind mob and die fast)

Demilich nat ac so low that he dies 2s faster even than vilewight(3x40),if it tanking he averegly got chance for 1-2 disintegrates and dies

 In terms of survivance av25 combo around 2s weaker than 3x40 combo

 no need continue that thay do less damage cos thay dead and 3x40 combo continues fight.

 In terms of damage per round bonesnarl doing much more damage and nat protected much much better

 And most of all, need to do so many levels to get and see new undeads and at the end you getting complite dissapointment

 Not saying that not using tham at all , using mostly in specific areas where need bind mob(for demilich) 

 For phantom - using tham in corpse run whan geting tired from name banshee on my screen..

 5and half cents from me

</div>

<div class="post" data-post-id="9718" data-author="dezakin" data-date="2005-12-02T02:56:06+00:00" data-subject="">

I think phantom is worse than that, like -1 hitroll for me when I tried it.

What I'd really like are for demiliches to have higher base ac and cast petrified armor on themselves. (I cant iron or stone my pets) 

I tried using them but all of aleksey's points are true. They allways get killed too fast for it to be worthwhile to use em.

I'd like phantoms to at least be a little better than banshees in some respect, but theres nothing redeeming about them. Give them a little bit more hp than banshees and an armor spell and I'd use them.

</div>
