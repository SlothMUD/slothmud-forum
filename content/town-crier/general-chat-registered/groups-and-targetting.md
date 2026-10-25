---
title: "groups and targetting"
topic_id: 1284
author: "seshi"
date: 2005-06-22T10:43:56+00:00
last_activity: 2005-07-24T12:32:08+00:00
last_author: "seshi"
sticky: false
locked: false
post_count: 20
---

<div class="post" data-post-id="7442" data-author="seshi" data-date="2005-06-22T10:43:56+00:00">

Being new to grouping I've been searching the forum and came across this:

quote "Everyone worth their salt has some kind of targetting script for use in groups" ([<LINK_TEXT text="http://slothmud.org/index.php?name=PNph ... opic&t=825">http://slothmud.org/index.php?name=PNphpBB2&file=viewtopic&t=825</LINK_TEXT>](http://slothmud.org/index.php?name=PNphpBB2&file=viewtopic&t=825))

Correct me if I'm wrong but I assume a targetting script sets up a trigger to attack the mob the leader or tank is attacking.

2 points

1. At the moment I am assigning a macro to assist leader/tank as soon as the mob is engaged. Assuming I'm paying attention this works Ok at the moment. is this going to be good enough for higher level play or do I really need to get a targetting script?

2. If I do does anyone have  a mush client script that I could use without extensive alterations?

I'm sure I'm not the only one who doesn't want to (or hasn't got the time) to write/alter scripts. I'm getting on fairly well with mushclient and the built in aliases/triggers/macros etc but I really don't want to have to learn detailed script writing to be able to have fun mudding. 

Any help would be appreciated

Salan

</div>

<div class="post" data-post-id="7443" data-author="Akasha2" data-date="2005-06-22T10:57:00+00:00">

In larger groups a targetter is very helpful so that the leader can just grouptell target XXX and your client assigns XXX to a variable @target.  This way when the leader asks you to blind, curse, web, etc, you can alias your spells to work on the target automatically: EG:

This is zmud btw, i dont know mush:

#alias bt {cast 'blind' @target}

#alias lt {look @target}

If you're paying attention and don't mind typing a lot, I suppose you could do it manually.  However, when you get larger and go to more obscure places on the mud, you start seeing strange names like Neeblryxxz, which is a pain to type everytime you want to look at it or target it for a spell. 

Your assist macro is fine, and everyone should make one :P  Advanced triggers like this just make it easier and more fun to group, with less aggrivation.

Akasha

</div>

<div class="post" data-post-id="7444" data-author="12345" data-date="2005-06-22T11:13:18+00:00">

A targetting script works one of two ways.  You can either set the target manually, or you accept the target the leader sets.  Emphasis on leader.

follow firebrand

You follow Firebrand.

leader -> Firebrand

Firebrand -- '*tigress* target sash'

target -> sash

It's a simple trigger in wintin:

#var {leader}{null}

#action {^You follow %1.}{#var leader $1;#showme {leader -> $1}}

#var {target}{null}

#action {^$leader -- '%1target %2'}{#var target $2;#showme {target -> $2}}

#action {^$leader -- '%1Target %2'}{#var target $2;#showme {target -> $2}}

Setting up a personal trigger is pretty much the same:

#alias {tar}{#var target $1;#showme {target -> $1}}

After that, it's simple to keep your eye on the ball.

#alias {blt}{cast 'blindness' $target}

Assuming your leader is announcing targets, you're always targeting what they are.  Doesn't solve the problem of mobs wandering in and out, so it's still best to use assist and untargetted attacks in battle, but it keeps everyone on the same page.

Having an autotargeter can be very useful in fast moving groups because the leader will often announce the next target while still in battle... or even shift targets.

Happy hunting.

</div>

<div class="post" data-post-id="7445" data-author="seshi" data-date="2005-06-22T11:34:28+00:00">

Thanks for the detailed help. I'll be trying this out. 

Will post my experience using this with mushclient for the other users out there.

Salan

</div>

<div class="post" data-post-id="7449" data-author="firebrand" data-date="2005-06-22T12:50:44+00:00">

on a side note, if a leader is leading an area like ettins (on ss) where all mobs can be targetted as target:ettin, there are mobs that can sometimes wander in that have same target name.  it is wiser (where possible) to assist $tank instead of attack $target

</div>

<div class="post" data-post-id="7450" data-author="Leaf" data-date="2005-06-22T12:59:21+00:00">

Yes also, if you in Firebrand's group.  Make sure u cast "moon".  She likes

that better then aegis :)

</div>

<div class="post" data-post-id="7452" data-author="firebrand" data-date="2005-06-22T13:07:00+00:00">

will, i am gonna kick your ever-lying ass dude :)  while that may be funny to you and the rest of us vets up here, but for a true newb who follows me and casts that spell based on this post is just gonna get him growled at by me.  everyone that groups with me knows i *normally* do not like moon aura for reasons of my own.  that is not fair to those newbs, will

</div>

<div class="post" data-post-id="7453" data-author="12345" data-date="2005-06-22T13:13:52+00:00">

I'm curious which newbie (besides Impz) has moon.

</div>

<div class="post" data-post-id="7454" data-author="firebrand" data-date="2005-06-22T13:34:08+00:00">

yeah yeah yeah - i forget that moon is an av spell, but still the point remains the same: IGNORE LEAF.

</div>

<div class="post" data-post-id="7455" data-author="Vixn" data-date="2005-06-22T13:43:12+00:00">

and targeter of 12345 is good, but won't work with such leader as **tigress**  err.... reb i mean :)

:roll:

</div>

<div class="post" data-post-id="7456" data-author="Leaf" data-date="2005-06-22T13:45:35+00:00">

Hehehe :) I have my fun times :)

Also if your a newbie with "Feast".  Make a auto-script to cast it every time

it falls.  That way we can all get that nice +1hit *cough*

MUAHAHAHAHAHAHAHA!!!

Love yea Reb *wink*

</div>

<div class="post" data-post-id="7457" data-author="Leaf" data-date="2005-06-22T13:46:55+00:00">

Hehehe :) I have my fun times :)

Also if your a newbie with "Feast".  Make a auto-script to cast it every time

it falls.  That way we can all get that nice +1hit *cough*

MUAHAHAHAHAHAHAHA!!!

Love yea Reb *wink*

</div>

<div class="post" data-post-id="7461" data-author="Zalasta" data-date="2005-06-22T14:00:28+00:00">

[quote:vmtwwqu3]However, when you get larger and go to more obscure places on the mud, you start seeing strange names like Neeblryxxz, which is a pain to type everytime you want to look at it or target it for a spell.[/quote:vmtwwqu3]

Gee, I wonder who's fault it is that we see 'strange names like Neeblryxxz'...

</div>

<div class="post" data-post-id="7471" data-author="guest" data-date="2005-06-22T15:40:42+00:00">

It's obviously pzyruxal fault ...

</div>

<div class="post" data-post-id="7481" data-author="madmax" data-date="2005-06-22T18:59:35+00:00">

and targeter of 12345 is good, but won't work with such leader as **tigress**  err.... reb i mean :)

:roll:[/quote:vxu2pt8s]

#var {target}{null} 

#action {^$leader -- '%1target %2'}{#var target $2;#showme {target -> $2}} 

#action {^$leader -- '%1Target %2'}{#var target $2;#showme {target -> $2}} 

[/quote:vxu2pt8s]

Sure it does, the '%1 will pick up anything infront of the "target" and ignore it.

The word immediately after target is used as the variable.

Firebrand -- '**tigress** target Vixn'

or

^$leader --'%1target Vixn'

$leader = {Firebrand}

%1 = {**tigress** }

%2 = {Vixn}

</div>

<div class="post" data-post-id="7496" data-author="firebrand" data-date="2005-06-23T15:02:15+00:00">

all my sigs are *tigress* - note the single stars

</div>

<div class="post" data-post-id="7497" data-author="Leaf" data-date="2005-06-23T15:35:01+00:00">

Eh, close enough I say

</div>

<div class="post" data-post-id="7532" data-author="firebrand" data-date="2005-06-24T11:45:17+00:00">

it makes a diff to those who are wanting exact string, darlin.  some ppl just copy/paste the string and then trigger on that instead of using variables.

</div>

<div class="post" data-post-id="7541" data-author="Avatar" data-date="2005-06-24T12:51:06+00:00">

They can copy / paste the code, which works not only with one leader's tag but also with any tags that people use.

Charles

</div>

<div class="post" data-post-id="7977" data-author="seshi" data-date="2005-07-24T12:32:08+00:00">

I've been working on targetting for Mushclient and have posted a help guide in the Mud Client Scripts - Other Clients forum

[<LINK_TEXT text="http://www.slothmud.org/index.php?name= ... pic&t=1374">http://www.slothmud.org/index.php?name=PNphpBB2&file=viewtopic&t=1374</LINK_TEXT>](http://www.slothmud.org/index.php?name=PNphpBB2&file=viewtopic&t=1374)

Hope this is helpful to other Mushclient users out there.

Salan

</div>
