---
title: "MSDP.MobAffects"
topic_id: 4828
author: "Gorka"
date: 2018-01-30T18:32:02+00:00
last_activity: 2018-02-03T21:15:27+00:00
last_author: "*teker*"
sticky: false
locked: false
post_count: 10
---

<div class="post" data-post-id="38650" data-author="Gorka" data-date="2018-01-30T18:32:02+00:00" data-subject="MSDP.MobAffects">

After loosing at least 1b xp today, trying to load Ryzen... I wondered if the imms might consider an MSDP variable that will list the affects players have casted onto the engaged mob. I tried setting timers and making warnings, but tracking the blind dropping on Ryzen turned out to be a major issue. It appears that one tick acid blind had some sort of variability to it that wasn't exact. It was impossible for me to tell if it was up or down... well, when it was down... I was dead... but you get what I mean. It would not only be useful for blind, but any spell a player puts on a mob.

I would protest the death proc that happens even when not engaged as well, if I thought someone might actually see it for how stupid it is. It's just dumb. The game is supposed to be challenging... a struggle... but when you walk into a room and instantly die, there is no struggle, it's just what it is... dumb.

warcry LEEEEEROOOY JEEEENKINS!!!

s sneak;backstab ryzen

You yell 'LEEEEEROOOY JEEEENKINS!!!'

<1334hp 762ma 407mv 1182776640xp -11.9ac -%>

Guarding the Portcullis

   Below narrow arrow-loops in the south wall, six defenders clutch stout 

bows in lifeless hands.  Identical ear-to-ear slits viciously expose their 

soft arterial membranes.  On the west wall are bloodied, unmanned hand 

crossbows staggered at different heights to defend the entrance point of 

the keep.  From the central ladder, a seventh elf, the left side of his 

head missing, dangles upside down from a wedged ankle.  An archway leads 

north onto the main thoroughfare.

Exits: North  Up  

A very small crystal flask containing a cerise liquid sits here.

You sense a hidden life form in the room.

You sneak through the shadows.

<1334hp 762ma 406mv 1182776640xp -11.9ac -%>

Ryzen whispers in your ear, 'I'll see you on the other side.'

You have been killed!!

You have been KILLED!! 

Lie still; you are DEAD!!! :-(

</div>

<div class="post" data-post-id="38651" data-author="*teker*" data-date="2018-01-30T20:01:32+00:00" data-subject="Re: MSDP.MobAffects">

OPPONENT.STATUS has this.  It is a comma separated list of debuffs and other items.  If there are none, the value is "Ok".  I have non-perfected code in mudlet that looks at changes to this value and prints out things like "Mob no longer blind".  But you have to be fighting the mob - you can't just walk into rooms and get the values on the mobs there.

The following values may be present:

Blind,Bound,Cursed,Deaf,Drowning,Grappled,Paralyzed,Petrified,Silenced,Webbed

</div>

<div class="post" data-post-id="38652" data-author="Gorka" data-date="2018-01-31T06:48:59+00:00" data-subject="Re: MSDP.MobAffects">

Well that's a good start isn't it. Wasn't aware of that variable. I've added it to my scripts, thanks. Having the timers would be premium in the future, but I understand...

I wondered what the effect of "disintegrate" was on a mob, is it possible to tell from a mob affect that double disints are currently active?

</div>

<div class="post" data-post-id="38653" data-author="Ker" data-date="2018-01-31T08:11:33+00:00" data-subject="Re: MSDP.MobAffects">

G'day,

Shadow pauldrons, a highly desired shoulder piece for the damage dealers that is barely equivalent, in fact better, to a shattered bone shoulder guards (high_quest item) was introduced along with the area Mercurial Woods. Likewise continued the policy of it's predecessor, with certain modifications suggested by the change of circumstances, is what brought it to exist. To reflect on it's power and value, severe circumstances were made present and yes that includes death - even on entry.

Now at the time Mercurial Woods was introduced; we had 2 massive groups, led by me and Josiah separately on its opening debut. Back in the day, there lived a high % of mages which contributed heavily in dropping Ryzen within 4 rounds. Times have changed. Given how the value of a shadow pauldrons has since improved drastically (high_quest shattered bone shoulder guards had a -wisdom penalty, thief_prime restrictions removed from the AQ upgrade, improved stats with stab_dam, potential conversion of drachma), one would think Ryzen needs a major overhaul. Fortunately, that is not the case.

Ryzen was never meant to be solo material. I am not saying it isn't solo, it can be done. However your risking and substantial power which led you to overcome this thought and the final outcome of it has resulted to some very undeserving remarks. There are many ways to deal with your "so many problems" - MSDP and this attitude does not factor in a slight bit. Dr on wintin95 with 0 MSDP, >100 Actions kills Ryzen easily. Did it ever occur to you that your approach is "dumb" instead of flaming the game?

But hey, you got a reply from Teker at least in regards to a problem. Perhaps that was the intention. 

It truly sickens me to read such things. Meh.

M

</div>

<div class="post" data-post-id="38654" data-author="Gorka" data-date="2018-01-31T11:19:23+00:00" data-subject="Re: MSDP.MobAffects">

I'm tired of your increasingly public demonisation of me Mage. You've miss represented my comments in a way unintended, then sort to label me in line with your misrepresentation and complain about my attitude. Even now when I seek to put the record straight, I fear the only thing you will see is another opportunity to further demonize me from these comments. Why are you being like this? What have I done to you? I'm sorry.

The name of the thread is MSDP.MobAffects, it's not change Ryzen. I did not expect Ryzen would be changed, Ryzen was a justification for a "suggestion" about mob effects. I don't think death procs on unengaged mobs better the game, that's my personal opinion, but I'm living with it. I'm aware the mob is not meant to be soloed but despite my "so many problems" I've managed 26 kills. I have followed up with a question about double disints.

You're just totally out of line, and I don't understand your bias to demonize me in a lot of situations lately. I feel I am being publicly misrepresented. You are out of line.

</div>

<div class="post" data-post-id="38655" data-author="Ker" data-date="2018-01-31T12:59:22+00:00" data-subject="Re: MSDP.MobAffects">

Kindly enlighten me.

1) Which part of your attempt in killing this said mob, whatever the outcome may be, justifies a label to the game as being 'stupid' and 'dumb' on the public forums? 

2) The conversation and challenges faced in the undertaking of said mob, which you deemed 'impossible' is vague. Simply put - there is no feedback from the mud to client if any mob is not engaged, specifically MSDP.MobAffects speaking and especially something that is on a timer. If I had some sort of counter which does that whenever I walk into a room, I'll hook you up personally ;) Hence, your follow up comments based on this 'impossible' is unwarranted.

Acid blinds got reduced sometime ago iirc ~40 seconds to 60 seconds. As of late, data shows a full 60. Not entirely sure if its a random % for it to range min/max.

To further clarify - should they remove the shadow pauldrons, (now this is 'out of line') go back to old school methods, force one to die 20+ times to attain a high_quest item which only gets produced once a year(if lucky) make it any better and having said that be the reverse along the lines of 'smart'? Death proc or not, one will certainly die plentiful on the basis of a high_quest item leading to a ton of exp loss etc - does that make it stupid and dumb? Ryzen in particular has been that way since it's inception, there were no changes as you adequately put. To me, this is brilliant since the item itself grew immensely in value.

3) This is no public demonisation. It is feedback - ideally feedback's are neutral. You took it public, I attend to it public. Whichever way you want to react to it is the conversation you are having. Personally though, I have chosen to ignore most of what happens on the forums in this nature. But really, I care for you and anybody in this manner.  You are a good friend and a long time Sloth patron dear Apprentice. Had it been just MSDP.Mobaffects like the title actually says without the label, the entirety of this page would have been very different. 

 I sincerely hope you get my point, or we can talk personally in game for that matter.

M

</div>

<div class="post" data-post-id="38656" data-author="*teker*" data-date="2018-01-31T16:54:54+00:00" data-subject="Re: MSDP.MobAffects">

Disintegrate affects constitution - what should I call that?  Chill touch affects strength which I can call "weakened".

I should have also mentioned that the structure within GROUP2 contains a STATUS field for each member that shows similar values.  It also includes values for "Dead", "Mortally wounded", "Incapacitated", "Stunned", "Sleeping", "Resting", "Sitting" so that group leaders can see if the group is ready to move.

</div>

<div class="post" data-post-id="38657" data-author="Gorka" data-date="2018-01-31T17:54:11+00:00" data-subject="Re: MSDP.MobAffects">

How about ailing... or these other ideas...

lacking physical strength, especially as a result of age or illness.

"by now, he was too feeble to leave his room"

synonyms:	weak, weakly, weakened, puny, wasted, frail, infirm, delicate, sickly, ailing, unwell, poorly, failing, helpless, powerless, impotent, enfeebled, enervated, debilitated, incapacitated, effete

If it's minus Con, how about constipated...  :shock:  :twisted:

</div>

<div class="post" data-post-id="38659" data-author="Gorka" data-date="2018-02-01T07:11:10+00:00" data-subject="Re: MSDP.MobAffects">

Hey Teker, just realised Faerie Fire is missing and might be useful to add if it's easy.

</div>

<div class="post" data-post-id="38663" data-author="*teker*" data-date="2018-02-03T21:15:27+00:00" data-subject="Re: MSDP.MobAffects">

Ok, I've added some and changed others to match the spell name:

    "Arms of the Abyss",

    "Blind",

    "Chill Touch",

    "Curse",

    "Deafness",

    "Demon Bind",

    "Disintegrate",

    "Drowning",

    "Deathgrip",

    "Faerie Fire",

    "Paralyze",

    "Petrify",

    "Silence",

    "Web"

Should be in next reboot.

</div>
