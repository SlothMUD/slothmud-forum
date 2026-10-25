---
title: "Bug with silence"
topic_id: 1640
author: "grantis"
date: 2006-01-09T20:04:28+00:00
last_activity: 2006-08-08T14:05:36+00:00
last_author: "brand"
sticky: false
locked: false
post_count: 42
---

<div class="post" data-post-id="10033" data-author="grantis" data-date="2006-01-09T20:04:28+00:00">

cast 'silence' older

Ok.

A gang leader's mouth clams shut![/color:3g2jxeuf]

<209hp 128ma 109mv>

cast 'fireball' older

Ok.

A gang leader hates your guts!

You throw a fireball at a gang leader and have the satisfaction of seeing him en

veloped in flames.

<210hp 115ma 109mv>

order followers assist grantis

You massacre a gang leader to small fragments with your slash.

A gang leader crushes you extremely hard.

A gang leader misses you with his pound.

You massacre a gang leader to small fragments with your slash.

A gang leader misses a kick at your groin, you breathe lighter now.

<192hp 115ma 109mv>

Mayor Virdo tells a manes that it is the nicest person he has ever met.

A manes misses a gang leader with its claw.

<192hp 115ma 109mv>

A soiled janitor leaves east.

<192hp 116ma 109mv>

You massacre a gang leader to small fragments with your slash.

A manes claws a gang leader hard.

A manes misses a gang leader with its claw.

A gang leader crushes you very hard.

A gang leader massacres a manes to small fragments with his pound.

You massacre a gang leader to small fragments with your slash.

A gang leader makes a nice ballet step which plants a foot a mile above your hea

d.

<178hp 116ma 109mv>

cast 'fireball'

You massacre a gang leader to small fragments with your slash.

A manes claws a gang leader hard.

A manes misses a gang leader with its claw.

A gang leader misses you with his crush.

A gang leader misses a manes with his pound.

You massacre a gang leader to small fragments with your slash.

A gang leader misses a kick at your groin, you breathe lighter now.

A gang leader yells 'Thugs, to me, I am in need of aid.[/color:3g2jxeuf]

<179hp 117ma 109mv>

Ok.

You throw a fireball at a gang leader and have the satisfaction of seeing him en

veloped in flames.

Damn cheating gang leaders

</div>

<div class="post" data-post-id="10046" data-author="Vixn" data-date="2006-01-10T08:16:47+00:00">

Seems he uses mysterious technique based on deaf-and-dumb language and pantomime.

</div>

<div class="post" data-post-id="10047" data-author="Krok" data-date="2006-01-10T10:24:59+00:00">

Oh, he borrowed my mystical ki powers!

</div>

<div class="post" data-post-id="10061" data-author="Yasik" data-date="2006-01-10T17:42:25+00:00">

His yelling is a proc message. Silence is useless.

</div>

<div class="post" data-post-id="10064" data-author="kjartan" data-date="2006-01-10T18:05:50+00:00">

But really... slience [i:x8i5u4m4]ought[/i:x8i5u4m4] to work.  Maybe I'll have a look at that tonight too.

</div>

<div class="post" data-post-id="10065" data-author="12345" data-date="2006-01-10T18:38:19+00:00">

*blink*  Oh yeah... realism.

While you're at it...  there's a couple procs that still allow mobs to cast through silence, though it's been fixed in many areas.

Is there supposed to be a way to stop mobs from phasing? Because webs, arms of the abyss and the rest just don't seem to work.

I'm sure I'll think of something else... I kinda like having this realism thing on my side for once. :)

</div>

<div class="post" data-post-id="10066" data-author="kjartan" data-date="2006-01-10T19:11:39+00:00">

I think many, but probably not all, of the phase checks are level based.  That is, a level 41 or 42 mob can phase right through your pathetic level 40 bind.  I'd have to double check that, though - it could just be random.

I think you can't phase through force fields.

</div>

<div class="post" data-post-id="10067" data-author="12345" data-date="2006-01-10T19:35:56+00:00">

Hmm.. I used a bad word.  I was referring to the proc that allows mobs to 'fly away' in battle.  In sakura, there's a mob under the water that uses it to hide underwater and come back and attack, in Aaost, there's a bird that flies away then returns and attacks.  In ET there's a gargoyle that does basically the same thing.  You can still web or use arms to reduce their hitroll, but they'll fly and swim away with no really problem at all.

Just seems odd that if I'm holding them with arms that they'd be able to move out of my reach... same with webs.

I call it phasing, but it's not a 'phase door' type effect, it's some mob_proc.

</div>

<div class="post" data-post-id="10070" data-author="12345" data-date="2006-01-10T20:37:12+00:00">

In Kj speak: kvp_hide(), possibly kvp_hostage() as well.

</div>

<div class="post" data-post-id="10071" data-author="Clink" data-date="2006-01-10T20:59:46+00:00">

... You can still web or use arms to reduce their hitroll, but they'll fly and swim away with no really problem at all.

Just seems odd that if I'm holding them with arms that they'd be able to move out of my reach... same with webs.

I call it phasing, but it's not a 'phase door' type effect, it's some mob_proc.[/quote:2wl76pj1]

It probably makes sense for them to resist webs and be too nimble for the arms to grab hold.  Maybe I can convince one of the coders to look at that.

 :D

</div>

<div class="post" data-post-id="10072" data-author="12345" data-date="2006-01-10T21:12:01+00:00">

Cool, while you're at it, you can adjust it so they're not close enough to hit me with their weapons too.

</div>

<div class="post" data-post-id="10073" data-author="kjartan" data-date="2006-01-11T04:29:30+00:00">

Ok, the thug leader is silencable as of next crash or reboot.  If there are other specific mobs that are violating reasonable silence behavior, tell me the specific mob on here and I'll probably try to fix it.

</div>

<div class="post" data-post-id="10075" data-author="grantis" data-date="2006-01-11T11:33:54+00:00">

Many thanks, much appreciated

</div>

<div class="post" data-post-id="10078" data-author="heaven" data-date="2006-01-11T14:26:56+00:00">

what about those mobs that are not silenced despite masterful casting? Would these be solved? It makes no sense that masterful casting = useless action.

</div>

<div class="post" data-post-id="10085" data-author="kjartan" data-date="2006-01-11T18:11:44+00:00">

It depends on the mob.  If you see a mob that is acting like it's not silenced even though you successfully cast a silence spell on it, post it here and I'll perhaps fix it.  I have to fix them, or at least some of them, on a case-by-case basis and I don't want to search the entire zillion mobs so I'll just fix them as they're problems.

I don't know what masterful silence does; I'll check and if it doesn't do anything, I'll make it so that you never get a masterful casting of silence.

</div>

<div class="post" data-post-id="10284" data-author="deucer" data-date="2006-01-22T11:23:17+00:00">

I cast a successful silence spell on librarian at Cholemry school. This mob was still able to "silence" one of my followers, and myself. For example:

Ok.

The golem librarian's mouth clams shut!

<576hp 149ma 178mv>

A wraith claws the golem librarian very hard.

A wraith rakes the golem librarian extremely hard.

A wraith claws the golem librarian extremely hard.

A wraith massacres the golem librarian to small fragments with its claw.

A wraith rakes the golem librarian extremely hard.

A wraith claws the golem librarian extremely hard.

A wraith claws the golem librarian extremely hard.

A wraith rakes the golem librarian extremely hard.

A wraith claws the golem librarian extremely hard.

The golem librarian massacres a wraith to small fragments with her hit.

The golem librarian hits a wraith extremely hard.

The golem librarian massacres a wraith to small fragments with her hit.

A Ju-Ju Zombie massacres the golem librarian to small fragments with its hit.

A Ju-Ju Zombie misses the golem librarian with its hit.

A Ju-Ju Zombie misses the golem librarian with its hit.

The golem librarian frowns at the noise you're making.

A wraith`s mouth suddenly seals shut as the golem librarian scolds it.[/color:22f5jfa6]

A Ju-Ju Zombie utters the words, 'oculowai buie'

The golem librarian is suddenly entwined with an ethereal darkness!

<577hp 152ma 178mv>

It even sends tells:

The golem librarian tells you `SHHHH!` and waggles her finger at you.[/color:22f5jfa6]

 :? This could be one of the beasties you might want to take a look at ?

great move to new server btw, thanks imms! Sloth rocks !

Deucer - Zuuul ingame

</div>

<div class="post" data-post-id="10287" data-author="kjartan" data-date="2006-01-22T16:04:33+00:00">

Ok, should be fixed next crash or reboot.

</div>

<div class="post" data-post-id="10300" data-author="Mustang" data-date="2006-01-23T17:14:00+00:00">

now would it be possible/appropriate to stop blinded mobs from healing themselves?  since we can't heal/restore self while blinded, it would be weird that mobs can.

</div>

<div class="post" data-post-id="10330" data-author="Mike" data-date="2006-01-25T10:37:27+00:00">

Seems to me that crystal golem in water plane buged. 

<867hp 244ma 158mv -9>

Rynquald utters the words, 'gurunsoqz' (silence)

A crystal golem's mouth clams shut![/color:3mwdbjbg]

<868hp 244ma 158mv -9>

Pendalf utters the words, 'candusghafahuai' (restoration)

The cleansing fires of healing fill your body!

<1037hp 245ma 158mv -9>

You skillfully parry the attack of a crystal golem.

You are brutally massacred by a crystal golem's pound.

A crystal golem misses you with its crush.

A crystal golem misses you with its crush.

You are brutally massacred by a crystal golem's crush.

You massacre a crystal golem to small fragments with your pierce.

You massacre a crystal golem to small fragments with your pierce.

A crystal golem utters the words, 'yafqz yuzre' (force field)[/color:3mwdbjbg]

Edd utters the words, 'yfaghbarh' (frostbolt)

Hope it is not a big deal to fix this mob. Thanks imms!

</div>

<div class="post" data-post-id="10489" data-author="deucer" data-date="2006-01-31T21:06:42+00:00">

white-robed sorcerer at Zodiac castle :

A white-robed sorcerer's mouth clams shut![/color:2vs94sfs]

<631hp 241ma 178mv>

web sorc

Tourney 2006 info posted on the crier

Ok.

A white-robed sorcerer is enmeshed in thick webs!

<631hp 228ma 178mv>

A wraith claws a white-robed sorcerer extremely hard.

A wraith misses a white-robed sorcerer with its rake.

A wraith misses a white-robed sorcerer with its claw.

A wraith claws a white-robed sorcerer extremely hard.

A wraith misses a white-robed sorcerer with its rake.

A wraith claws a white-robed sorcerer extremely hard.

A wraith claws a white-robed sorcerer extremely hard.

A wraith rakes a white-robed sorcerer extremely hard.

A wraith claws a white-robed sorcerer extremely hard.

A Ju-Ju Zombie massacres a white-robed sorcerer to small fragments with its hit.

A Ju-Ju Zombie massacres a white-robed sorcerer to small fragments with its hit.

A Ju-Ju Zombie hits a white-robed sorcerer extremely hard.

A white-robed sorcerer misses you with his pound.

A white-robed sorcerer misses you with his pound.

A white-robed sorcerer misses a wraith with his pound.

You are brutally massacred by a white-robed sorcerer's pound.

A white-robed sorcerer hates your guts!

You slash a white-robed sorcerer very hard.

You slash a white-robed sorcerer hard.

A Ju-Ju Zombie utters the words, 'abrawg ay hpz ablgg'

A white-robed sorcerer utters the words, 'pzar'[/color:2vs94sfs]

A white-robed sorcerer heals himself.

 :shock:

</div>

<div class="post" data-post-id="10495" data-author="*Splork*" data-date="2006-02-01T00:40:49+00:00">

These two should be fixed after next reboot....

Enjoy,

Splork

</div>

<div class="post" data-post-id="10596" data-author="Dedsune" data-date="2006-02-06T22:59:40+00:00">

<567hp 190ma 180mv>[-7.1:+13:+71:+17]:542504156xp>

Elusive utters the words, 'gurunsoqz'

The Queen of Storms's mouth clams shut!

<570hp 191ma 182mv>[-7.1:+13:+71:+17]:542504156xp>

Drum utters the words, 'gurunsoqz'

<570hp 191ma 182mv>[-7.1:+13:+71:+17]:542504156xp>

circl

You circle around to the Queen of Storms's side and place the cinquedeas between two of her ribs.

<571hp 191ma 177mv>[-7.1:+13:+71:+17]:542505476xp>

You pierce the Queen of Storms extremely hard.

The Queen of Storms misses you with her hit.

The Queen of Storms massacres you to small fragments with her hit.

You massacre the Queen of Storms to small fragments with your pierce.

You pierce the Queen of Storms extremely hard.

[b:2jkbz24f]The Queen of Storms utters the words, 'diesilla barh'[/color:2jkbz24f][/b:2jkbz24f]

YOU'RE HIT. A lightning bolt from the Queen of Storms has reached its goal.

<528hp 191ma 177mv>[-7.1:+13:+47:+17]:542506752xp>

Drum utters the words, 'gurunsoqz'

</div>

<div class="post" data-post-id="10597" data-author="*Splork*" data-date="2006-02-07T01:00:04+00:00">

Fixed...

Enjoy,

Splork

</div>

<div class="post" data-post-id="11168" data-author="Vixn" data-date="2006-03-12T19:01:21+00:00">

<656hp 143ma 216mv -11.0ac -9al>

look life-force

The life force teacher is a very religious woman, as evidenced by the many 

conflicting religious symbols on her robes, necklace, amulets, charms and 

bracelets. Apparently she's one of those people who are capable of 

believing three impossible and contradictory things before breakfast each 

day. A book she carries in her left hand bears the unlikely title, 'The 

Floobdinachery of Pelshanai.' 

The life force instructor is in excellent condition: [*******]

You attempt to peek at the inventory:

You can't see anything.

<655hp 144ma 216mv -11.0ac -9al>

cast 'silence' instructor

Ok.

The life force instructor's mouth clams shut![/color:1chvipky]

<649hp 136ma 216mv -11.0ac -9al>

cast 'silence' instructor

cast 'acid blast' life-force

Ok.

Nothing seems to happen.

The life force instructor growls at you and attacks!

The life force instructor hates your guts!

The life force instructor hates you and attack!

The life force instructor misses you with her hit.

<649hp 123ma 216mv -11.0ac -9al>

You pierce the life force instructor extremely hard.

The life force instructor misses you with her hit.

The life force instructor misses you with her hit.

You pierce the life force instructor extremely hard.

You pierce the life force instructor very hard.

The life force instructor utters the words, 'carpe vital'[/color:1chvipky]

<648hp 125ma 216mv -11.0ac -9al>

Ok.

You watch in grim satisfaction as your acid blast burns the life force instructor horribly.

<648hp 108ma 216mv -11.0ac -9al>

cast 'acid blast'

cast 'frostbolt' life-force

The 'aegis' spell on you is about to wear off.

Ok.

Your acid horribly burns the life force instructor's flesh, causing it to fall to the ground.

<647hp 93ma 216mv -11.0ac -9al>

cast 'frostbolt' life-force

You pierce the life force instructor extremely hard.

The life force instructor misses you with her hit.

The life force instructor misses you with her hit.

You pierce the life force instructor extremely hard.

The life force instructor utters the words, 'carpe vital'[/color:1chvipky]

<647hp 93ma 216mv -11.0ac -9al>

cast 'frostbolt' life-force

Ok.

You form a cone of frost in your hand and launch it at the life force instructor.

<646hp 70ma 216mv -11.0ac -9al>

look life-force

You massacre the life force instructor to small fragments with your pierce.

A pair of ceramic eyes misses you with their hit.

The life force instructor hits you.

The life force instructor misses you with her hit.

You deal a critical blow to one of the life force instructor's vital organs.

You massacre the life force instructor to small fragments with your pierce.

You deal a critical blow to one of the life force instructor's vital organs.

You massacre the life force instructor to small fragments with your pierce.

Someone glows softly as they stare at you.

Someone utters the words, 'carpe vital'[/color:1chvipky]

thanks in advance.

</div>

<div class="post" data-post-id="11179" data-author="kjartan" data-date="2006-03-12T22:43:21+00:00">

Fixed.

</div>

<div class="post" data-post-id="12395" data-author="deucer" data-date="2006-04-29T15:39:13+00:00">

KJ fixed this some time ago. Looks like librarian in Cholemry forgot lesson  to keep it shut. :P :

sil libr

Ok.

The golem librarian's mouth clams shut![/color:136uqa1k]

<662hp 169ma 176mv>

A wraith claws the golem librarian extremely hard.

A wraith rakes the golem librarian extremely hard.

A wraith claws the golem librarian extremely hard.

A wraith claws the golem librarian extremely hard.

A wraith rakes the golem librarian extremely hard.

A wraith misses the golem librarian with its claw.

A Ju-Ju Zombie massacres the golem librarian to small fragments with its hit.

A Ju-Ju Zombie massacres the golem librarian to small fragments with its hit.

A Ju-Ju Zombie hits the golem librarian extremely hard.

The golem librarian hits a wraith extremely hard.

The golem librarian hits a wraith extremely hard.

The golem librarian misses a wraith with her hit.

A Ju-Ju Zombie utters the words, 'oculowai buie'

The golem librarian is suddenly entwined with an ethereal darkness!

A wraith`s mouth suddenly seals shut as the golem librarian scolds it.[/color:136uqa1k]

and two rounds later:

The golem librarian's blow passes right through you with no effect!

The golem librarian misses you with her hit.

The golem librarian massacres a wraith to small fragments with her hit.

The golem librarian hates your guts!

You slash the golem librarian very hard.

You miss the golem librarian with your slash.

A Ju-Ju Zombie utters the words, 'xafe ay saui'

The golem librarian stumbles as a Ju-Ju Zombie's power word subdues her.

The golem librarian tells you `SHHHH!` and waggles her finger at you.[/color:136uqa1k]

Just to let you know :D

Zuuul

</div>

<div class="post" data-post-id="12396" data-author="Leaf" data-date="2006-04-29T16:00:02+00:00">

I think those are procs.

</div>

<div class="post" data-post-id="12397" data-author="13" data-date="2006-04-30T12:23:29+00:00">

Will, stfu.

</div>

<div class="post" data-post-id="12398" data-author="Leaf" data-date="2006-04-30T22:45:41+00:00">

No can Do AA, ur silence spell didn't work on me. Bitch!!!

</div>

<div class="post" data-post-id="12414" data-author="Assirian" data-date="2006-05-04T07:55:33+00:00">

I don't know what masterful silence does; I'll check and if it doesn't do anything, I'll make it so that you never get a masterful casting of silence.[/quote:3sthikcp]

Is it possible to check miss Lebowski in cholomery too?

Miss Lebowski utters the words, 'uizuguburuhl'

<736hp 354ma 189mv>

cast 'silence' miss

You weave the threads of magic masterfully!

Miss Lebowski's mouth clams shut!

<736hp 340ma 189mv>

fle

Third Floor Hallway

Exits: North  East  West  

You flee head over heels.

PANIC! You couldn't escape!

<736hp 342ma 187mv>

n

Secret Stash

Exits: South  

A steaming pile of intestines lie puddled on the floor here.

*Miss Lebowski begs you to free her from slavery.

Miss Lebowski glows with a bright light!

<736hp 343ma 186mv>

Miss Lebowski utters the words, 'uizuguburuhl'

<736hp 344ma 187mv>

You feel less protected.

cast 'stone skin' Assirian

<736hp 345ma 188mv>

Ok.

You feel your skin become much, much stronger.

<736hp 330ma 188mv>

cast 'sanc' Assirian

Ok.

You start glowing.

<736hp 258ma 189mv>

Miss Lebowski utters the words, 'uizuguburuhl'

</div>

<div class="post" data-post-id="12415" data-author="Assirian" data-date="2006-05-04T07:56:36+00:00">

sorry, the post was doubled by mystake

</div>

<div class="post" data-post-id="12569" data-author="Mog" data-date="2006-05-16T10:53:55+00:00">

More mobs that cast through Silence.

A black-robed firenewt war wizard stands here.

cast 'silence' wizard

cast 'silence' wizard

538hp 179ma 143mv -8.4ac -1

Ok.

A firenewt war wizard's mouth clams shut![/color:3a39vv71]

538hp 164ma 143mv -8.4ac -1

A firenewt war wizard claws you hard.

532hp 165ma 144mv -8.4ac -1

Impossible! You can't concentrate enough!

532hp 165ma 144mv -8.4ac -1

A firenewt war wizard hates your guts!

You slash a firenewt war wizard extremely hard.

A firenewt war wizard claws you hard.

A firenewt war wizard claws you hard.

A firenewt war wizard bites you very hard.

You massacre a firenewt war wizard to small fragments with your slash.

You slash a firenewt war wizard extremely hard.

A firenewt war wizard utters the words 'ya azik xarfzx'.[/color:3a39vv71]

A hellish swarm of flaming meteors flies from a firenewt war wizard's hand!

You resist a bit of the damage...

You are enveloped in flames from a fireball sent by a firenewt war wizard - OUCH.

480hp 166ma 144mv -8.4ac -1

You massacre a firenewt war wizard to small fragments with your slash.

A firenewt war wizard claws you hard.

A firenewt war wizard bites you very hard.

You massacre a firenewt war wizard to small fragments with your slash.

You massacre a firenewt war wizard to small fragments with your slash.

A firenewt war wizard utters the words 'ya azik xarfzx'.

A hellish swarm of flaming meteors flies from a firenewt war wizard's hand!

You resist a bit of the damage...

You are enveloped in flames from a fireball sent by a firenewt war wizard - OUCH.

431hp 167ma 144mv -8.4ac -1

Tested most of the caster mobs in Firenewts, all cast through silence.  Thanks in advance.

</div>

<div class="post" data-post-id="12570" data-author="Mog" data-date="2006-05-16T10:55:46+00:00">

More mobs that cast through Silence.

A black-robed firenewt war wizard stands here.

cast 'silence' wizard

cast 'silence' wizard

538hp 179ma 143mv -8.4ac -1

Ok.

A firenewt war wizard's mouth clams shut![/color:38w138sn]

538hp 164ma 143mv -8.4ac -1

A firenewt war wizard claws you hard.

532hp 165ma 144mv -8.4ac -1

Impossible! You can't concentrate enough!

532hp 165ma 144mv -8.4ac -1

A firenewt war wizard hates your guts!

You slash a firenewt war wizard extremely hard.

A firenewt war wizard claws you hard.

A firenewt war wizard claws you hard.

A firenewt war wizard bites you very hard.

You massacre a firenewt war wizard to small fragments with your slash.

You slash a firenewt war wizard extremely hard.

A firenewt war wizard utters the words 'ya azik xarfzx'.[/color:38w138sn]

A hellish swarm of flaming meteors flies from a firenewt war wizard's hand!

You resist a bit of the damage...

You are enveloped in flames from a fireball sent by a firenewt war wizard - OUCH.

480hp 166ma 144mv -8.4ac -1

You massacre a firenewt war wizard to small fragments with your slash.

A firenewt war wizard claws you hard.

A firenewt war wizard bites you very hard.

You massacre a firenewt war wizard to small fragments with your slash.

You massacre a firenewt war wizard to small fragments with your slash.

A firenewt war wizard utters the words 'ya azik xarfzx'.

A hellish swarm of flaming meteors flies from a firenewt war wizard's hand!

You resist a bit of the damage...

You are enveloped in flames from a fireball sent by a firenewt war wizard - OUCH.

431hp 167ma 144mv -8.4ac -1

Tested most of the caster mobs in Firenewts, all cast through silence.  Thanks in advance.

</div>

<div class="post" data-post-id="12610" data-author="kjartan" data-date="2006-05-20T15:49:47+00:00">

Firenewt: fixed, in next crash or reboot

Mme. Lebowski: fixed, in next crash or reboot (I also tweaked her casting to be a bit smarter)

</div>

<div class="post" data-post-id="12879" data-author="Avatar" data-date="2006-06-04T03:04:28+00:00">

It's not really concerning Silence, but this could be fixed too:

Ygol the Arch-Lich utters the words, 'heal'

Ygol the Arch-Lich heals himself.

Ygol the Arch-Lich has been banished to the astral plane!

Everything Ygol the Arch-Lich was carrying suddenly drops to the ground.

Regards,

Charles

</div>

<div class="post" data-post-id="12880" data-author="12345" data-date="2006-06-04T04:18:02+00:00">

It's not really concerning Silence, but this could be fixed too:

Ygol the Arch-Lich utters the words, 'heal'

Ygol the Arch-Lich heals himself.

Ygol the Arch-Lich has been banished to the astral plane!

Everything Ygol the Arch-Lich was carrying suddenly drops to the ground.

Regards,

Charles[/quote:1kuzfju1]

I kinda liked that proc :)

</div>

<div class="post" data-post-id="13254" data-author="Weasel" data-date="2006-07-03T17:48:23+00:00">

another one that doesn't know when to stfu..

Firenewt Dwelling Chamber

   This large black marble chamber is comfortably furnished.  Red velvet 

and black wooden furniture sits in stately fashion near some large book- 

cases also made of a painted black wood.  A large bed, almost as an after- 

thought, sits against the western wall.  

Exits: South  

A black-robed firenewt war wizard stands here.

cast 'silence' wizard

Ok.

A firenewt war wizard's mouth clams shut!

cast 'frostbolt'

Ok.

A firenewt war wizard hates your guts!

You form a cone of frost in your hand and launch it at a firenewt war wizard.

You skillfully parry the attack of a firenewt war wizard.

A firenewt war wizard claws you hard.

A firenewt war wizard bites you very hard.

You massacre a firenewt war wizard to small fragments with your pierce.

You massacre a firenewt war wizard to small fragments with your pierce.

You deal a massive blow to one of a firenewt war wizard's vital organs.

You viciously massacre a firenewt war wizard with your pierce.

A firenewt war wizard utters the words 'fzimmo bofnil'.

There is a puff of smoke, and a firenewt sergeant appears![/color:q4dv6c3g]

:)

</div>

<div class="post" data-post-id="13255" data-author="kjartan" data-date="2006-07-03T18:09:07+00:00">

Fixed, incor.  I also fixed the bully clouds' 'skitzle' spell while I was in there.

</div>

<div class="post" data-post-id="13686" data-author="madmax" data-date="2006-08-07T03:11:13+00:00">

<334hp 273ma 102mv>

You weave the threads of magic masterfully!

A maimed elf's mouth clams shut!

(Cut spam)

<334hp 264ma 102mv>

Your weapon blasts a maimed elf with a cone of frost!

You rake a maimed elf hard.

Si pierces a maimed elf extremely hard.

Tallac hits a maimed elf hard.

Krystal pierces a maimed elf.

A maimed elf pounds Tallac hard.

Si pierces a maimed elf extremely hard.

Tallac tickles a maimed elf with his hit.

The maimed elf says `I will remember you, Tallac. We, elves, live long and remember well...`

The maimed elf produces a small vial of colored liquid.

He smashes it with his mace, and is gone in a puff of blue smoke!

Not that he couldnt use the vial without saying anything.  Also, he smashes it with his mace (that he dosent have.)

Madmax

</div>

<div class="post" data-post-id="13687" data-author="Nascosto" data-date="2006-08-07T05:06:35+00:00">

yes yes. this should be:

The maimed elf gives you the finger!!!

The maimed elf produces a small vial of colored liquid.

He smashes it with his mace, and is gone in a puff of blue smoke!

</div>

<div class="post" data-post-id="13689" data-author="kjartan" data-date="2006-08-08T01:11:46+00:00">

Fixed, although not exactly as Nascosto suggested.  And he DOES have a mace, read his description.

</div>

<div class="post" data-post-id="13690" data-author="brand" data-date="2006-08-08T14:05:36+00:00">

...

</div>
