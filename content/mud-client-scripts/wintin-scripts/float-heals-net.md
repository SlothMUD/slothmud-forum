---
title: "Float Heals -NET"
topic_id: 1770
author: "*juggleblood*"
date: 2006-03-11T08:35:44+00:00
last_activity: 2006-03-13T12:13:27+00:00
last_author: "12345"
sticky: false
locked: false
post_count: 15
---

<div class="post" data-post-id="11157" data-author="*juggleblood*" data-date="2006-03-11T08:35:44+00:00">

Automatically heal the tank in group when they drop below set hps.

#def group {tankfloat}

#al tank {#var tank $0;#showme {Tank is now $tank}}

#al myheal {#var myheal $0;#showme {My preferred heal is set to'$myheal'.}}

#al floatset {#var floatset $0;#showme {I will now heal $tank when they drop below $floatset hp.}}

#al checktank {#if {$tankhp<$floatset}{#showme -*Floating*-;healtank} 

#al healtank {|;cast '$myheal' $tank}

#al tankfloat {#showme {I am floating $tank when they drop below $floatset hps.;#showme {Commands are: Tank, Floatset. To disable, type 'floatset 0'.}}

#ac {^$tank %0[%1/%2]} {#var tankhp $1;checktank}

You could extend this for healo by doing something like this:

#al healin {#2 grouptell I'M IN FOR HEALS;floatset 550}

#al healout {#2 grouptell I'M OUT... NEXT HEALER!;floatset 0}

</div>

<div class="post" data-post-id="11158" data-author="Gnu" data-date="2006-03-11T12:57:52+00:00">

Thank you very much! But I have a question. Is it possible to some more changes to extend "this" for the entire life in sloth? 

You know, I play Sloth just to test scripts, so I need some help with excluding such terms as "listening a group leader", "paying attention" etc...

</div>

<div class="post" data-post-id="11159" data-author="Vixn" data-date="2006-03-11T13:48:12+00:00">

Cleric Bots are illegal if you are away from keyboard. You will be 

considered a robot even if your actions are not benefiting yourself.[/quote:1e02rtrc]

Be careful if u gonna use this script. Don't use it when you are a.f.k.

Also, read again what bard said.

</div>

<div class="post" data-post-id="11160" data-author="Krok" data-date="2006-03-11T18:30:53+00:00">

As a leader and a cleric, I will ungroup the ppl who use auto-healing scripts, cause it only shows their newbieness and lack of attention. Your fingers and your reaction should be quick, only this way you'll be a good healo. And imagine you are asked to heal two people at one time, this way the scripts will fuck it up.

</div>

<div class="post" data-post-id="11163" data-author="*juggleblood*" data-date="2006-03-12T14:39:57+00:00">

My char Rub (Wa/Ma/Cl) is rarely if ever in the healo. I just have this script to toss the tank an emergency heal if the healers are slacking or lose concentration. I seriously doubt Krok would ungroup me for healing the tank when they drop below 150hp. 

That said...make sure to mind your mother Krok.  Don't be a bot healer, wash behind your ears, and don't go out in public without clean underwear on.

</div>

<div class="post" data-post-id="11164" data-author="*juggleblood*" data-date="2006-03-12T14:57:03+00:00">

Thank you very much! But I have a question. Is it possible to some more changes to extend "this" for the entire life in sloth? 

You know, I play Sloth just to test scripts, so I need some help with excluding such terms as "listening a group leader", "paying attention" etc...[/quote:1xfeog9u]

I know I'm not a smart man, but I thinks yous is tryin to be sarcastik. I just like usin these here scripts cuz of what I read on yalls home page. You know, where it says:

The name "Sloth" was chosen to embody the original philosophy of the mud, which was to make everybody's lives as easy as possible. This convenience is embodied in commands such as "hunt" and "scan", as well as a multiclass system that allows each player to eventually access a great deal of the available class abilities.[/quote:1xfeog9u]

I just figgured, well garsh, this client thing makes everything even slothier. I can tell my guy what I want him to do and he just, you know, does it. Now I just need to learn how to use that mxp stuff so I can use the mouse more to free up my beer hand.

</div>

<div class="post" data-post-id="11165" data-author="Weasel" data-date="2006-03-12T16:27:04+00:00">

LOL kicking someone out of group for healing.. nice. That'll learn 'em.

</div>

<div class="post" data-post-id="11166" data-author="Krok" data-date="2006-03-12T17:53:48+00:00">

You guys suck :))

</div>

<div class="post" data-post-id="11167" data-author="Weasel" data-date="2006-03-12T18:01:23+00:00">

hehe  :twisted:

</div>

<div class="post" data-post-id="11171" data-author="Rynquald" data-date="2006-03-12T21:02:47+00:00">

Auto floating only becomes a problem imho when there's enough people using them at once that the tank gets 4 restores as soon as they drop below 500 hp, or they're set to fire at 400 from max or so and overheal if the current healer's restores are 250+, even with a single floater.

</div>

<div class="post" data-post-id="11181" data-author="Gnu" data-date="2006-03-12T23:19:35+00:00">

Auto floating only becomes a problem imho when there's enough people using them at once that the tank gets 4 restores as soon as they drop below 500 hp, or they're set to fire at 400 from max or so and overheal if the current healer's restores are 250+, even with a single floater.[/quote:1sff7h38]

Auto-anything becomes a problem when ppl botting. In some cases it is very important to switch from healing to blasting fast, but that becomes almost impossible, since scripts rule the game.

That's why I do not set a regular heal-order in my groups, and like to add orders like "everyone go w"  after 'all up' :P

</div>

<div class="post" data-post-id="11184" data-author="jezer" data-date="2006-03-12T23:42:17+00:00">

I think Autolycos is rubbing off too much on Krok!  :evil:

</div>

<div class="post" data-post-id="11188" data-author="Rynquald" data-date="2006-03-13T06:25:24+00:00">

[quote:1gq52mas]Auto-anything becomes a problem when ppl botting. In some cases it is very important to switch from healing to blasting fast, but that becomes almost impossible, since scripts rule the game.[/quote:1gq52mas]

Definitly....I was refering to using such a script without being afk. And if you write a script with the potential to lag that you can't disable very quickly you may as well be a bot weather you're afk or not  :twisted:

</div>

<div class="post" data-post-id="11189" data-author="Vixn" data-date="2006-03-13T07:19:57+00:00">

[quote:34ksmdew]Definitly....I was refering to using such a script without being afk. And if you write a script with the potential to lag that you can't disable very quickly you may as well be a bot weather you're afk or not  :twisted:[/quote:34ksmdew][/quote:34ksmdew]

Agree, usually I am not absent but sleeping right on a keyboard. So the best script for me is something that will beep when someone tell/whisper/grouptell 'Edd?' :P

And another bright idea is to make triggers for entering archways or climb staircase right after tank. This allow group move together and Krok won't know you are boting since she put you in healo :P

</div>

<div class="post" data-post-id="11199" data-author="12345" data-date="2006-03-13T12:13:27+00:00">

Maybe I'm just lucky, but most the folks I group with are very reliable and good in a pinch.  As an example, I got unlucky with a repop in cano the other day.  I died almost instantly.  There's nothing quite like the feeling of being locked in with a really angry mob when the group is bound, you're dead and holding the only key.  I was pleasantly surprised when we all ended up at the west gate and I was the only one dead.

In the largish groups I've been leading, the botters are remarkably obvious about botting. Most folks laugh at my little trigger that pesters them to put their AC and max mana in their gjob.  But it's amazing how many people follow up, and then go completely silent almost immediately.  I'll usually pester them for a short while and then give them a quick trip to recall.

Scipts themselves aren't much of a problem.  Many times I write them just to keep up with the leader because Mike's groups move VERY fast and Krok's aren't much slower.  The majority of the folks I have trouble with lately are playing from sidekicks and have almost no ability to respond to any kind of abnormal situation.

</div>
