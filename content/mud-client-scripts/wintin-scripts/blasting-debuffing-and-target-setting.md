---
title: "Blasting/debuffing and target setting"
topic_id: 2382
author: "Rosher"
date: 2007-03-06T07:52:23+00:00
last_activity: 2007-03-10T20:18:27+00:00
last_author: "Avatar"
sticky: false
locked: false
post_count: 17
---

<div class="post" data-post-id="17184" data-author="Rosher" data-date="2007-03-06T07:52:23+00:00">

The main point of this script is to set target at the same as you cast sometihng on your victim. Of course if there is a target set by the leader you can use it as usual. Here is an example:

[code:2elv4zb8]

CASE 1:

gt target bird

***TARGET SET TO: bird

You grouptell: 'target bird'

<681hp 492ma 223mv>(+7){Aisholm Town}

fbt

Ok.

A small snow bird hates your guts!

Your frostbolt obliterates a small snow bird.

CASE 2:

fbt man

***TARGET SET TO: man

Ok.

A northern settler hates your guts!

Your frostbolt obliterates a northern settler.

[/code:2elv4zb8]

And the code with example aliases:

[code:2elv4zb8]

#defgroup {spells}

#alias  {basecast} {using System;\r\nusing System.Windows.Forms;\r\n\r\nusing ScriptEngine;\r\n\r\n//css_reference ScriptEngine.dll;\r\n// [0] - spell;\r\n// [1] - target;\r\n// [separator] - .;\r\npublic class Script : WintinScript\r\n{\r\n    public override void Init()\r\n    {\r\n        string line = wintin.Line.Trim();\r\n        string delim = ".";\r\n        char[] delimarr = delim.ToCharArray();\r\n        string[] pars = null;\r\n        pars = line.Split(delimarr, 2);\r\n        if (pars[1].Length == 0)\r\n        {\r\n            pars[1] = wintin.GetVariable("target");\r\n        }\r\n        else\r\n        {\r\n            wintin.Interpret("settar " + pars[1]);\r\n        }\r\n        wintin.SendToMud("cast '" + pars[0] + "' " + pars[1] + "\\r\\n");\r\n    }\r\n}\r\n} {G|spells} {T|CS}

#alias  {fb} {cast 'frostbolt'} {G|spells} {T|WT}

#alias  {fbt} {basecast frostbolt.%0} {G|spells} {T|WT}

#alias  {aab} {basecast arms of the abyss.%0} {G|spells} {T|WT}

#alias  {curse} {basecast curse.%0} {G|spells} {T|WT}

#alias  {acb} {cast 'acid blast'} {G|spells} {T|WT}

#alias  {acbt} {basecast acid blast.%0} {G|spells} {T|WT}

#alias  {settar} {#var {target} {%1};#showme ***TARGET SET TO: %1;} {G|spells} {T|WT}

#variable  {target} {off} {G|spells}

#defgroup {}

[/code:2elv4zb8]

So it is easy to extend this set with additional aliases... I tried to cover all usecases in the examples

</div>

<div class="post" data-post-id="17186" data-author="13" data-date="2007-03-06T12:55:48+00:00">

That's a lot of work for 

#al {fft}{cast 'frost' $target}

</div>

<div class="post" data-post-id="17187" data-author="Krok" data-date="2007-03-06T19:03:10+00:00">

I even enjoyed it when I had to add 'frt' to my client's profile :)

</div>

<div class="post" data-post-id="17188" data-author="Medios" data-date="2007-03-06T22:02:55+00:00">

When is someone going to write a script that does everything including respond to imms when they question whether im botting.  It would be alot easier if I didnt have to interact with sloth at all.  I mean really I could level to 5x40 and not know a single thing.  I could gate the inn from recall point.  Ask stupid questions like "where is the sun temple".  I could also let someone else pop all my spellbooks and teach them to me without even knowing im not there.  Someone needs to work on this.

Mike

</div>

<div class="post" data-post-id="17189" data-author="Autolycos" data-date="2007-03-06T22:11:32+00:00">

i thought aaron already did that?

</div>

<div class="post" data-post-id="17190" data-author="13" data-date="2007-03-06T22:15:44+00:00">

That was Sarge.  I'm the guy that kills people, remember?

</div>

<div class="post" data-post-id="17191" data-author="Autolycos" data-date="2007-03-07T00:19:30+00:00">

riiiiiight....

didnt sarge have his head replaced with a melon? :shock:

</div>

<div class="post" data-post-id="17195" data-author="13" data-date="2007-03-07T13:14:17+00:00">

[img:1mjnh3k1]http://www.ritasretros.com/folgers.jpg[/img:1mjnh3k1]

</div>

<div class="post" data-post-id="17216" data-author="Avatar" data-date="2007-03-08T06:27:30+00:00">

I think you guys are going a little overboard.  All he did was post an alias that sets your target variable when you blast a new mob.  That's most likely to be useful when soloing, not grouping.  My client is setup similarly, so I can use 'look target' later in the fight and the client remembers what the target was.

It's a good script, one command usable in different situations.

</div>

<div class="post" data-post-id="17230" data-author="*juggleblood*" data-date="2007-03-09T12:57:58+00:00">

When is someone going to write a script that does everything.........  It would be alot easier if I didnt have to interact with sloth at all..........level to 5x40 and not know a single thing...............Ask stupid questions like "where is the sun temple".....blah blah blah.....stupid noobs...blah blah blah....lazy botters...blah blah blah .....

Mike[/quote:3thyoy8u]

Mania/Bipolar Disorder: Bipolar disorder is marked by mood swings between periods of intense highs and lows. The bipolar patient may have elated moods and grandiosity (feelings of importance) alternating with periods of depression or chronic irritability. :twisted:

</div>

<div class="post" data-post-id="17231" data-author="*juggleblood*" data-date="2007-03-09T13:14:04+00:00">

[img:gqglqapd]http://www.geocities.com/saudixpat/Lithium.jpg[/img:gqglqapd]

</div>

<div class="post" data-post-id="17235" data-author="Medios" data-date="2007-03-09T22:06:42+00:00">

Feelings of importance:  This shit cracks me up.  I guess by this definition its safe to say that if you feel important your mentally unstable.  No wonder everyone is on pills.  "I feel good about myself Doc".  Here these pills will make that go away!  There is absolutely nothing wrong with self worth.

I will not take pills unless its for chronic back pain, and then I cant even move without something (this is only in the winter when my muscles get tight and I reinjure my back).  I self medicate for my anger management issues.  You talk about extreme highs and lows, hell I thought you knew me better than that.  You make it sound like im not this way all the time.  I was trying to be sarcastic about the welfare state of sloth.  As a leader its quite upsetting to have to deal with the same issues all the time.  I feel most of these problems arise from "scripts".

Lets pretend were fighting a mob that summons.  Leader targets mob, but then the mob summons a guard.  So I bolt the guard to kill him, then this script changes my target to guard, instead of the one the leader set.  Lets pretend your the stabber.  Leader walks out of the room after kill and your autotarget scripts stab some mob that the leader did not intend.  I have enough problems forgetting about mobs with similiar names to have followers changing targets randomly.  The same thing can be concluded with autoblasters.  If your not targetting what the leader says, then you can possibly blast something wrong.  If you guys want to write all these senseless scripts its your time not mine.  However if/when you start acting like a total n00b because you cant control your scripts, I will end up dealing with it.

I can cite too many times when "scripts" failed and caused a cf.

tar demo

ft

Mike

</div>

<div class="post" data-post-id="17236" data-author="Autolycos" data-date="2007-03-09T22:36:56+00:00">

You talk about extreme highs and lows, hell I thought you knew me better than that.  You make it sound like im not this way all the time.  I was trying to be sarcastic about the welfare state of sloth. [/quote:1p4s08bo]

snicker..

i've always felt you have maintained being a pain in the ass pretty consistantly!  :twisted: 

My autostabber was dangerous.. always stabbing random keywords... i'm just thankful that Nab & Blastem helped me set @tar clear on kill!!!

*leaving an Ettins group and going for food only to stab the shopkeeper is funny as hell... but gets old fast  :roll:

</div>

<div class="post" data-post-id="17237" data-author="Hades" data-date="2007-03-10T00:17:21+00:00">

a simple trigger to autoassist $tank and/or leader AFTER someone else has blinded it works out pretty good.... no mindless spam and you can sit back and surf the net while some dweeb (read: Medios) sits on his high horse and 

attempts to re-wriite the rules of MUDding. Zmud/Wintin are/were designed for this for a reason.

ps- I hate Auto

 :twisted:

</div>

<div class="post" data-post-id="17238" data-author="Autolycos" data-date="2007-03-10T00:38:56+00:00">

Zmud/Wintin are/were designed for this for a reason.

[/quote:hxtuzn91]

but not for sloth specifically...  there are many muds out there that encourage multiplaying and bot scripts..  of course then you could lead your own groups of +20 chars and get what ever you want.. 

muds that do that usually have near no actual playerbase..

i'm for one glad that sloth is strict..

ps.  kisses hades :x

</div>

<div class="post" data-post-id="17239" data-author="12345" data-date="2007-03-10T02:03:21+00:00">

There's nothing wrong with the script necessarily, in fact, its very nice for running solo.  The weakness of the script the same risk that anyone assumes when they don't use the target set by the leader.  Risky? Sure.  Unreasonable? Not if properly used.  Assuming they never use the re-targetting feature while grouped, its a non-issue.

That's a little idealist and unrealistic, but at least give folks a chance to prove they have an IQ over 5 first.

</div>

<div class="post" data-post-id="17240" data-author="Avatar" data-date="2007-03-10T20:18:27+00:00">

People who understand what the script does in the first place would have enough sense to use it correctly.

To reverse the argument, people who only target what the leader grouptells are never helping to blast the summoned guards.

I just hope that when I'm back to playing normally I remember how my client works and what mobs I should be blasting :)

</div>
