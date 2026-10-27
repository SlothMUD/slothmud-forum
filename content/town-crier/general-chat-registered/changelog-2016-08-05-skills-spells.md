---
title: "Changelog 2016-08-05 - skills / spells"
topic_id: 4663
author: "*teker*"
date: 2016-08-05T14:29:34+00:00
last_activity: 2016-08-09T03:07:20+00:00
last_author: "cyprimus"
sticky: false
locked: false
post_count: 22
---

<div class="post" data-post-id="37171" data-author="*teker*" data-date="2016-08-05T14:29:34+00:00" data-subject="Changelog 2016-08-05 - skills / spells">

I've added some logging so we can track how much damage everyone is doing with their skills. It'll help me to see what kind of damage the skills do to make tweaking easier. The following changes have been implemented:

Firestorm:

You shouldn't be able to use this spell to pkill anymore. I've completely rewritten the area-affect spell damage code so that you can still cast the spell if ungrouped players are in the room and it will start fights with the mobs but skip the players.

Chain lightning:

I moved this spell over to the new code also figuring that more people can test it than firestorm. Previously this spell would not cast if ungrouped players were in the room - now it just skips them. Once the new code has been thoroughly tested, I'll move all the area affect damage spells over to it.

Cry of the Avatar:

Flames at Midnight:

These songs should use the saves color now when appropriate.

Broadside:

Damage increases slowly with warrior and avatar levels. Weapon damage bonus counts now. Ether mobs can be hit if mist is up. Spiritual hammer doesn't work as it's not the right type of weapon for broadside. Max weight of target increases at warrior 40 and every 40 thereafter.

Flail:

I haven't changed the damage until I can see the log results. It looked like flail wasn't working to start fights when ungrouped players were in the room so I fixed that. You should also be able to hit ether mobs with hammer/mace or when mist is up.

</div>

<div class="post" data-post-id="37172" data-author="Teron" data-date="2016-08-05T14:44:45+00:00" data-subject="Re: Changelog 2016-08-05 - skills / spells">

Thanks. Testing atm.

What about riposte with the hammer or when mist is up?

</div>

<div class="post" data-post-id="37173" data-author="*teker*" data-date="2016-08-05T15:17:00+00:00" data-subject="Re: Changelog 2016-08-05 - skills / spells">

Looks to me like riposte works with mist up. Hammer isn't the right weapon type.

</div>

<div class="post" data-post-id="37174" data-author="Gorka" data-date="2016-08-05T16:03:16+00:00" data-subject="Re: Changelog 2016-08-05 - skills / spells">

Thanks Teker, you're awesome!

I logged in to check the changes, but could not notice anything. The sad reality is I am now almost 5x40 - and not throughout lack of trying - but I have still been unable to secure even a single weapon dam item or rune even though my cap is now at 20.

I have 3/5 of one weapon dam rune.

100 drachma from my first weapon dam item.

An item or two from a weapon dam forge.

But currently I have been unable to even get one single point before nearly 5x40.

Hopefully before I reach 9x40 I will get my first piece of weapon damage. I'll enjoy 20 hand dam, an extra attack and strike till then.

</div>

<div class="post" data-post-id="37175" data-author="*teker*" data-date="2016-08-05T16:37:35+00:00" data-subject="Re: Changelog 2016-08-05 - skills / spells">

The early results show Gorka is getting about a 30% increase in damage. Some of the higher level warriors are seeing double to triple their original damage.

</div>

<div class="post" data-post-id="37176" data-author="Teron" data-date="2016-08-05T16:51:55+00:00" data-subject="Re: Changelog 2016-08-05 - skills / spells">

My initial results tell me that my broadside damage went up from 40-80 to consistent 60-80.

For me, broadside does about 1.3-1.5 of attack damage.

Or is my delta-exp counter totally off the mark, and I'm actually dealing 200 damage with broadside?

Because for me, broadside does 1-2%, whereas 4 attacks deal 5-6% mobhp damage, so broadside isn't doing any damage worth talking about.

What conditions should be met, so I can deal the triple of my old damage?

Thanks.

</div>

<div class="post" data-post-id="37177" data-author="Gorka" data-date="2016-08-05T17:22:42+00:00" data-subject="Re: Changelog 2016-08-05 - skills / spells">

30%!!! <img src="/images/smilies/icon_eek.svg" alt=":shock:" title=":shock:" width="15" height="15" class="smiley nozoom"> <img src="/images/smilies/icon_cool.svg" alt="8)" title="8)" width="15" height="15" class="smiley nozoom"> 

It's difficult to tell there was an increase, as the game damage is not transparent. I used to 3-4%, and now I still 3-4%... Maybe I 4% more, I didn't notice?

Does regular dam count in the same way weapon dam counts for broadside? It's far easier to get damage items currently then weapon dam items, would like to think it's counting the same way?

</div>

<div class="post" data-post-id="37180" data-author="cyprimus" data-date="2016-08-06T04:39:32+00:00" data-subject="Re: Changelog 2016-08-05 - skills / spells">

wow, i got a stun from broadsiding. Nice.

no idea how common they are. Or how common falling over is now.

Good improvement.

</div>

<div class="post" data-post-id="37181" data-author="Gorka" data-date="2016-08-06T05:23:00+00:00" data-subject="Re: Changelog 2016-08-05 - skills / spells">

Falling over is still flipping annoying... I've taken it out of my coliseum scripts again, it's still more a nuisance than a help at the moment.

</div>

<div class="post" data-post-id="37182" data-author="Filk" data-date="2016-08-06T05:36:00+00:00" data-subject="Re: Changelog 2016-08-05 - skills / spells">

Maybe its time to move away from hidden damage numbers and show real numbers after each damage done? <img src="/images/smilies/icon_rolleyes.svg" alt=":roll:" title=":roll:" width="15" height="15" class="smiley nozoom"> 

So people will be able to write their own damage meters and everyone will be happy to see their actual output. Especially in groups. C'mon is 2016 year. Every mmo game do it already!

</div>

<div class="post" data-post-id="37184" data-author="*teker*" data-date="2016-08-06T21:24:41+00:00" data-subject="Re: Changelog 2016-08-05 - skills / spells">

> <strong>Teron wrote:</strong>
> My initial results tell me that my broadside damage went up from 40-80 to consistent 60-80.
> 
> For me, broadside does about 1.3-1.5 of attack damage.

My logs show lower damage than what you're seeing so I suspect either your counter is off or there's additional damage being added somewhere in the code that I haven't found yet. It's pretty hard to read. My logs show that the base damage for you has about doubled.

> <strong>Quote:</strong>
> Because for me, broadside does 1-2%, whereas 4 attacks deal 5-6% mobhp damage, so broadside isn't doing any damage worth talking about.

What are you doing between rounds if not broadsiding? Just curious. Your numbers would be 17-20 rounds with nothing between rounds or 13-17 rounds with broadside. That seems like something that would be beneficial.

> <strong>Quote:</strong>
> What conditions should be met, so I can deal the triple of my old damage?

Ask Stun. He's doing the best damage according to my logs.

</div>

<div class="post" data-post-id="37185" data-author="*juggleblood*" data-date="2016-08-06T23:24:07+00:00" data-subject="Re: Changelog 2016-08-05 - skills / spells">

> <strong>Filk wrote:</strong>
> Maybe its time to move away from hidden damage numbers and show real numbers after each damage done? <img src="/images/smilies/icon_rolleyes.svg" alt=":roll:" title=":roll:" width="15" height="15" class="smiley nozoom"> 
> 
> So people will be able to write their own damage meters and everyone will be happy to see their actual output. Especially in groups. C'mon is 2016 year. Every mmo game do it already!

Yes this please. I mean common, we've moved soooo far from Jake's original position that game mechanics should be hidden from the players, and damage done is THE most essential bit of information that players want. Ok, I hit the mob, but how effective was it, i.e. how much damage was done.

From what I understand we intentionally obscure this information so that the players don't nitpick and complain the admin to death. But does it really stop anyone from over-analysing and posting stuff to the forums? I think it does not. This is a hack and slash mud. I attack the mob and hurt it and I just want to know how many frigging hit points I took off the thing, so I can decide my most effective strategies going forward. For 2 decades we've been intentionally obscuring this bit of data, and I think it's been a mistake the whole time. 

That being said, I understand this isn't a democracy and other admin have a right to their opinions, but for the record, I've stated mine.

Sorry, I forgot to start by mentioning how much I appreciate the changes mentioned at the start of this thread!

</div>

<div class="post" data-post-id="37186" data-author="*Idjit*" data-date="2016-08-07T03:25:46+00:00" data-subject="Re: Changelog 2016-08-05 - skills / spells">

In that vein, are we actually happy that melee "work exp" is currently randomized relative to the damage we do?

Slightly different subject (requiring a slightly different fix) but I thought I'd mention it here.

Maybe we should roll this back.

\--Idj

</div>

<div class="post" data-post-id="37187" data-author="*Breeze*" data-date="2016-08-07T04:32:22+00:00" data-subject="Re: Changelog 2016-08-05 - skills / spells">

> <strong>\*juggleblood\* wrote:</strong>
> > <strong>Filk wrote:</strong>
> > Maybe its time to move away from hidden damage numbers and show real numbers after each damage done? <img src="/images/smilies/icon_rolleyes.svg" alt=":roll:" title=":roll:" width="15" height="15" class="smiley nozoom"> 
> > 
> > So people will be able to write their own damage meters and everyone will be happy to see their actual output. Especially in groups. C'mon is 2016 year. Every mmo game do it already!
> 
> 
> 
> Yes this please. I mean common, we've moved soooo far from Jake's original position that game mechanics should be hidden from the players, and damage done is THE most essential bit of information that players want. Ok, I hit the mob, but how effective was it, i.e. how much damage was done.
> 
> 
> 
> From what I understand we intentionally obscure this information so that the players don't nitpick and complain the admin to death. But does it really stop anyone from over-analysing and posting stuff to the forums? I think it does not. This is a hack and slash mud. I attack the mob and hurt it and I just want to know how many frigging hit points I took off the thing, so I can decide my most effective strategies going forward. For 2 decades we've been intentionally obscuring this bit of data, and I think it's been a mistake the whole time. 
> 
> 
> 
> That being said, I understand this isn't a democracy and other admin have a right to their opinions, but for the record, I've stated mine.
> 
> 
> 
> Sorry, I forgot to start by mentioning how much I appreciate the changes mentioned at the start of this thread!

I actually would not be against this except for the fact that I would get people asking me details on it. 

there are a million and one things that can affect how much damage you do. I don't feel the need to clarify then on a per fight basis. having said that, I wouldn't be against a toggle that says if you turn this on \* or if you don't turn it on \*, dont ask the admins why you do X damage.base damage can easily be calculated. any bonus damage, not. 

after my vacation I may do a test run of something like that actually. just depends on how I feel and how much bs I have to deal with afterwards.

</div>

<div class="post" data-post-id="37188" data-author="Ker" data-date="2016-08-07T06:48:37+00:00" data-subject="Re: Changelog 2016-08-05 - skills / spells">

Guten Tag Breeze!

Wir hoffen dass Sie bei guter Gesundheit sind!

To address your concern - I firmly believe that the players of Sloth are at the minimum in this regard. Minus a few handful.

Since Telegram took part, we have been a voice of unity and strength. What's changed? Majority are slowly understanding the dire need of a subtle approach. I will personally see to it a mighty druid slap to anyone who harasses you with a million questions without even asking what you ate earlier!

Have fun and don't trip on your vacation!

Prost,

Dr

</div>

<div class="post" data-post-id="37189" data-author="Teron" data-date="2016-08-07T10:47:00+00:00" data-subject="Re: Changelog 2016-08-05 - skills / spells">

Teker, I'm getting my numbers from the randomized exp counter, from some hours of experience - but, unfortunately, no statistics. Overall, however, say, about 10-20-30 hits, do give a fairly objective, if blurred, picture of damage.

I believe you that my base damage has doubled, but I barely noticed it. I know Stun does great damage, but 95% of our warriors are not Stun or Cyprimus, so let's work with the base damage, and how we can scale it up to 9x40. You can look at 3-5x40 warriors, if you want to see, how broadside damage compares to other skills.

As a tank, it means I don't want to use broadside to do miniscule damage, because it lags, or to stun mobs, because there's a chance it'll put me on my back, unable to rescue or heal self.

As an assisting warrior or in solo, I can wind or flail. With capped flail, flail does more damage. The only drawback is, when you land the flail after the mob dies.

I haven't tested the knock-back level yet, but for damage, this skill is fairly useless.

Could you describe us, where in the damage skill list you (or you and imms) want to place broadside and flail, so you'd set our expectations right?

You probably should take scale damage with weapon damage more, if you want to

\- limit tank damage

\- make it useful for assisting warriors, who wear weapon damage eq.

Perhaps, it's the 4x40 warrior, who should be doing 60-80 damage with a broadside in ac, not a 8x40 warrior in a +12 weapon damage set.

Also, I support the public damage display for skills. It adds satisfaction in seeing the damage numbers you've worked so hard to produce. So far, only healers see the exact numbers of their heals - and it has yielded no wild pestering, to my knowledge.

</div>

<div class="post" data-post-id="37196" data-author="Gorka" data-date="2016-08-07T20:02:14+00:00" data-subject="Re: Changelog 2016-08-05 - skills / spells">

Kiss Juggleblood.

Highfive Taron.

Pat Teker.

Lick Zuzu.

Worship Breeze.

Taunt Sam.

Lay off teker guys! It's not his fault that our lack of weapon dam eq still renders broadside pretty undesirable for us mid-bie warriors. 

But a few pointsTeker... don't compare other warriors to Stun. Stun is an immortal warrior among the players, and I'd also suggest that he probably got his weapon dam runes before changes to gem pop rates. They say behind every good man is a... woman, er druid, and his partnership with a certain very smart druid goes a long way to making Stun even greater. For some of us, these things are impossible to obtain. Also Teker - you mention double damage... double what? My broadside formally did the same damage as a kick, but failed more. Double isn't very impressive when you double not much at all. I understand at the moment you can't really say it did 40 damage and now it does 80 damage, because "secret squirrel" still dark cloaks the mud but yeah...

That's me for this round.

</div>

<div class="post" data-post-id="37199" data-author="Teron" data-date="2016-08-08T06:14:06+00:00" data-subject="Re: Changelog 2016-08-05 - skills / spells">

> <strong>Gorka wrote:</strong>
> Lay off teker guys! It's not his fault that our lack of weapon dam eq still renders broadside pretty undesirable for us mid-bie warriors.

I don't think Teker or anyone said he'd add more ingame and drachma weapon damage eq, so we analyze what we see and provide the feedback that's required to make things better. We are attacking the issue, not Teker, so I think that is within the lines of constructive criticism. So don't swing your axe at us prematurely, Gorka.

Also, you or I don't know where imms want the new broadside/flail to stand in terms of damage, or how it scales with weapon damage.

And so far broadside is still lacking. Teker said there'd be a few tweaks, I hope it'll get better.

</div>

<div class="post" data-post-id="37201" data-author="Gorka" data-date="2016-08-08T09:26:04+00:00" data-subject="Re: Changelog 2016-08-05 - skills / spells">

I think weapon damage eq is the cause of the problem though. That is the domain of the builders who add eq, not the coder's like Teker as I understand it.

What ever gets done, it's going to get considerably better for Stun than for us... simply because weapon damage is currently part of the broadside formula. I don't see how it's possible to win in this situation without fixing the linear progression of warrior weapon dam eq over levels. It will either suck for us, or overpower Stun... (Not saying it's effect on Stun is overpowering either, just that it's better in comparison)

There are only two solutions as I see it, you would have to make the progression of the skill non linear, or make it ignore weapon dam altogether. I think making the progression of the skill non linear, ie, the progression of the skill increase faster for low levels, isn't a good solution, as at some point weapon damage eq will be added to the game... at that point it will become over powered for the newbies. I call these types of things "bandaid solutions" because they don't address deep issues.

So to summarise... weapon dam eq is weird, how can you "win" when using weapon damage as a formula in broadside and still keep everyone happy? I don't think it's possible without creating a problem that bites at another point later. The only reason I defended Teker on that particular point, is because as a programmer myself I see he is between a rock and hard place, trying to use weapon dam in a formula, that's just not linear or even for all players. It would be easier to avoid using weapon damage in the formula all together, or lessen any multiplication it might do, simply due to the fact the variable is essentially flawed and causing inbalances.

</div>

<div class="post" data-post-id="37202" data-author="Teron" data-date="2016-08-08T10:24:33+00:00" data-subject="Re: Changelog 2016-08-05 - skills / spells">

Though Teker should know better, here's what I'd do:

\- make broadside do ok damage with mostly regular/dice damage with linear bonuses from 40s (that's how it is, I imagine?)

\- introduce weapon dam eq

\- update broadside to favor weapon damage.

Then again, if flail is supposed to be main damage dealing skill, then the last point should apply to flail also/instead.

</div>

<div class="post" data-post-id="37208" data-author="*teker*" data-date="2016-08-08T21:31:53+00:00" data-subject="Re: Changelog 2016-08-05 - skills / spells">

> <strong>Teron wrote:</strong>
> As a tank, it means I don't want to use broadside to do miniscule damage, because it lags, or to stun mobs, because there's a chance it'll put me on my back, unable to rescue or heal self.
> 
> 
> 
> As an assisting warrior or in solo, I can wind or flail. With capped flail, flail does more damage. The only drawback is, when you land the flail after the mob dies.
> 
> 
> 
> Could you describe us, where in the damage skill list you (or you and imms) want to place broadside and flail, so you'd set our expectations right?

We haven't really discussed it on an imm level other than that I was going to try some changes and see what happens. I don't like "useless" skills. It seems like bodyslam would also fall into that category. I think a single target skill like broadside should do more than an area affect skill like flail. I would like to see additional weapon skills that can be used with other weapon types so that players could enable those skills if they choose a different weapon. We have that somewhat in that only certain weapons can broadside or riposte but I'd like to see alternatives that can be used with other weapons. Additional bare hand skills could be added as well to give monks more variety.

</div>

<div class="post" data-post-id="37209" data-author="cyprimus" data-date="2016-08-09T03:07:20+00:00" data-subject="Re: Changelog 2016-08-05 - skills / spells">

Well. My two cents, i feel monks have good variety... its just others got the same.. ieeveryone eventually will have grip/strike etc.. 

Would encourage my monk more to do something along the lines of like thieves... reduced cost on touch and or grip..

and or reduced hit penalty.. touch misses a lot..

Again, would suggest just extending the barehanded bonus' to addetional 40's after 40 monk, especially for primes.

Also, altering where/when damage reduction is applied, in terms of before/same/after lite fluidity etc..... but thats something major.. and, not knowing the numbers, i cannot say what would be reasonable.

Bodyslam is fairly useless.. maybe make it more like a flying kick, that can be done in a fight... risk falling to knock your opponent down and do extra damage.. maybe use some moves in the process.

Could also see adding stances--ie-defensive stance gives bonus to ac, pen to attacks.. etc..... but seen them unbalance more muds than i wanna count..

Anyways, thanks for your work!

</div>
