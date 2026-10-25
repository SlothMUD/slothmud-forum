---
title: "Neat Triggers for 12 Occasions for an Awesome Tank"
topic_id: 4684
author: "Teron"
date: 2016-10-25T17:52:25+00:00
last_activity: 2016-10-25T17:52:25+00:00
last_author: "Teron"
sticky: false
locked: false
post_count: 1
---

<div class="post" data-post-id="37450" data-author="Teron" data-date="2016-10-25T17:52:25+00:00">

These days, simple rescue triggers don't do the job well, you need to combat the new mechanics that immort added to baffle tanks and when players get in trouble on their own.

Legend:

@t = target

@s = stabber

@g = gripper

(%w) = the last word before the next part of the pattern

sw = the second wind alias

halp = #alias halp '|;|;sta;sta;sw;#2 rescue %1'

Rescues are single for patterns that occur a lot, and double for rare patterns, because rescues fail.

The simplest triggers

Rescue on stab:

You warily lead the way ahead -> rescue @s

@s place%1in the back of*resulting in some strange -> rescue @s

@s tried to backstab *, but nearly cut*own finger. - > rescue @s

Rescue on circle:

@s slowly circles around to -> rescue @s

@s tried to sneak to the side of -> rescue @s

Rescue on grip:

@g circles around -> #2 rescue @g

@g reaches out with * spiritual hands, gripping -> #2 rescue @g

smartly steps out of -> #2 rescue @g

@g expertly touches -> #2 rescue g

Rescue on sing

SEEK SHELTER AT ONCE! %1 has begun to sing. -> #2 rescue %1

Rescue on aggro:

sees (%w), and attack -> #2 rescue %1

growls at (%w) and attacks -> #IF {%1<>you} {#2 rescue %1}

leaps out of the shadows and attacks %1! -> #2 rescue %1

engages (%w)! -> #2 rescue %1

Dispel

isn't taking any more: * attacks %1! -> #2 rescue %1

Situational rescues:

The soul drinker forms jaws of smoke that latch onto (%w)l! -> #2 rescue %1

Complex triggers

Some mobs bash, then engage someone else right away:

disengages %1, and attacks %2! -> halp %2 (halp is an alias for |;|;sta;sta;sw;rescue %1;rescue %1)

switches targets and powerfully engages (%w)! -> halp %1

ideally, you need to remember these mobs and use entrench anyway.

Silent disengage:

(%w) *@t*hard. -> rescue %1 (this will also rescue An, The, etc, since I don't use a group member list - a chance for improvement here)

(%w) massacres *@t* to small fragments with -> rescue %1

Rescue mages, when you become disengaged from the mob on Uhhhl, Klklklpa and the like or when they "blast guard", when there were two in the room and you've just killed 1.guard:

(%w) gestures dramatically, and *@t* is roasted in a burning wind. -> #2 rescue %1

*@t* screams in pain as (%w)'s frostbolt freezes -> #2 rescue %1

Target problem is a leader's issue, though, don't yell at mages unless they blast wrong targets on their own.

When someone engages the target (or the target hits someone):

*@t*massacres (%w) with -> rescue %1

*@t*misses (%w) with -> rescue %1

When you are confused, who's fighting whom, type look, and see:

*@t* is here, fighting %1 -> rescue %1

Some advice

As you noticed, there aren't many triggers, where you send a | to clear your command queue, because you do that in the middle of the round. And most of the patterns either happen before the fight, or when you are disengaged, or after the mob's attacks, such as the silent engage.

I don't recommend doing using flail on mobs that bash, engage a lot or hit very hard. You want to be able to rescue anyone before the next round starts, unless you add |;sw to most of your rescue triggers. But even then, there's a risk that you've already used second wind that round. Also, use entrench and grease self.

For example, on Klklklpa if the tank is blasting with second wind, the next target of Klklklpa is likely to eat a round, unless you are quick to save him/her.

If anything, use the "halp" alias I outlined above to get back on track to save someone.

But most of all, pay attention to what's going on, pipe and rescue people. Triggers can't save from every situations, but if you use all of the above, they will from most, because the above triggers work, when the target engages someone else.

If your group member is hit by something other than the target, you need to rescue manually. This also happens, when the leader targets a word that's not in the short name of the mob (e.g., god in Olympus or burly/male in ogres).

Alternatively, you can remove the target requirement in the patterns and introduce a group member list, so if anything fights anyone from the list, you rescue them. Otherwise, if you rescue anyone who's fighting anyone, it's going to be messy, because mobs have single-word names, too.

The usual disclaimer is that the code is in Zmud script, you'll have to translate it to your client if it's not Zmud/Cmud.

</div>
