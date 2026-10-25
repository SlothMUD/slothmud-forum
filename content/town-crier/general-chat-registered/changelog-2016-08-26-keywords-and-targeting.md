---
title: "Changelog 2016-08-26 - keywords and targeting"
topic_id: 4667
author: "*teker*"
date: 2016-08-26T14:57:15+00:00
last_activity: 2016-08-27T10:34:06+00:00
last_author: "Teron"
sticky: false
locked: false
post_count: 5
---

<div class="post" data-post-id="37282" data-author="*teker*" data-date="2016-08-26T14:57:15+00:00" data-subject="Changelog 2016-08-26 - keywords and targeting">

The old stuff:

Bash and kick shouldn't work against ether mobs with hammer wielded.  Only if misted.

I haven't seen any complaints regarding the new firestorm and chain lightning code so I'll start working on the rest of the area effect spells to move them over.  You probably won't see any real changes other than being able to cast them in rooms with ungrouped players.

The new stuff:

I have introduced four new reserved keywords.  The first three are "self", "leader", and "point".  You should be able to use these keywords in most commands to refer to yourself, the group leader, and the person on point.

Hopefully, the more exciting part is the fourth keyword "target" and the new commands that go with it.  The basic idea is that group leaders can target mobs and the entire group can use the word "target" in skills and spells to make sure they hit the right mobile.  When the mob dies, the target data is set to NULL so you don't accidentally hit something else.  I'm hoping this will remove the need for new players to write/copy scripts to participate fully in group combat.  Let me know how it works - there are probably some situations where it's not quite clean but I did test a number of situations including shifting.  Currently the new commands are in test most so if the game crashes, they will be disabled on reboot.  For some reason HELP TARGET shows the wrong page but you can type HELP TARGET COMMAND to see:

TARGET "TARGET COMMAND"

Usage:        TARGET [keywords]

See Also:     ASSIST TARGETASSIST SCORE

The TARGET command is used to specify target keywords for the mobile you want

to engage next in combat.  Once the player enters the room with a mobile that

matches the specified keywords, the player will lock onto that target.  Once

the target is locked onto, the "target" keyword can be used in most commands

to refer to that mobile.  Most aggressive and semi-aggressive skills and

spells will also default to the target if the player is not currently

fighting anyone.

This command is most useful in groups.  When the group leader uses the TARGET

command, all non-lurking players in the group will target the same keywords.

When the group leader locks onto a target, all non-lurking members of the

group will lock onto the same target.  This means that spellcasters in the

back line can cast spells like blind or curse using the keyword "target" (or

without specifying a target) and they will cast those spells at the targeted

mobile.  When the mobile dies, all target data is cleared and the spellcasters

won't accidentally hit another mobile in the room with the same keywords.

If the TARGET command is entered without any keywords, the player's current

target is cleared.  The only other times the target data is cleared is if the

mobile or player dies.  The current target can be seen in the output of the

SCORE command.

And HELP TASSIST to see:

TARGETASSIST TASSIST

Usage:        TARGETASSIST [player], TASSIST [player]

See Also:     ASSIST "TARGET COMMAND"

The TARGETASSIST command is used to set the current player's target to that

of the specified player.  If the specified player is currently fighting, the

current player's target is set to the mobile being fought.  If the specified

player is not currently fighting, the current player's target and target

keywords are set to the same as the specified player.

</div>

<div class="post" data-post-id="37283" data-author="Gorka" data-date="2016-08-26T15:47:10+00:00" data-subject="Re: Changelog 2016-08-26 - keywords and targeting">

On the subject of targets... spell targets... some default to targeting self with no argument, others don't. Would it be possible to make all spell targets either default to self, or if the spell is offensive use the target parameter?

</div>

<div class="post" data-post-id="37284" data-author="Teron" data-date="2016-08-26T16:08:02+00:00" data-subject="Re: Changelog 2016-08-26 - keywords and targeting">

In the same vein, what do heals in groups default to?

Do targets clear on following self b4 mob dies?

Thanks, Teker, very helpful.

</div>

<div class="post" data-post-id="37286" data-author="*teker*" data-date="2016-08-26T20:59:55+00:00" data-subject="Re: Changelog 2016-08-26 - keywords and targeting">

Well we've had our first crash so the commands have been disabled until I can look at the code and repro and fix on the test server.  The self, leader, and point arguments should still work.  To answer your questions:

> **Quote:**
> On the subject of targets... spell targets... some default to targeting self with no argument, others don't. Would it be possible to make all spell targets either default to self, or if the spell is offensive use the target parameter?

Most of the spells either defaulted to self or the mob that the player is fighting.  I added code so that if the spell is offensive or semi-offensive to have it default to target if the player isn't fighting anyone.  If there are particular spells that aren't doing this - let me know and I'll take a look.  One spell that I wasn't sure about is "dispel magic" - it defaults to self.

> **Quote:**
> In the same vein, what do heals in groups default to?
> 
> Do targets clear on following self b4 mob dies?

Heals remain unchanged - they default to self.  Targets do not clear on follow command - they only clear if the mob dies, the player corpses, or the player or leader manually clears it.

</div>

<div class="post" data-post-id="37288" data-author="Teron" data-date="2016-08-27T10:34:06+00:00" data-subject="Re: Changelog 2016-08-26 - keywords and targeting">

I've used target with my pets once, and they didn't attack it.

They might've been unable to see in the dark, though.

If you show me the test port, I'll test it myself.

</div>
