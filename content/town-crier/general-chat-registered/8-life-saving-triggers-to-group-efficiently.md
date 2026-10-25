---
title: "8 life-saving triggers to group efficiently"
topic_id: 4642
author: "Teron"
date: 2016-06-10T13:46:36+00:00
last_activity: 2016-06-29T19:48:33+00:00
last_author: "Teron"
sticky: false
locked: false
post_count: 4
---

<div class="post" data-post-id="36956" data-author="Teron" data-date="2016-06-10T13:46:36+00:00">

While leading I repeatedly give out the same mundaine commands, so I thought you might wonna create triggers for them, so you could survive easier.

Legend:

@leader - the group leader variable

@char - your name variable, if you play many chars

%1 - any word or number that follows. You can use a more specific pattern recognition, such as (%w) in Zmud/Cmud, which only takes a single word into account

| - is a vertical pipe, shift \, which is used to clear the buffer of pre-typed commands. Basically, you stop doing whatever you were doing, except maybe one command that comes through.

The scripts are for Zmud/Cmud. If you want to port them to Wintin, replace @ with $ and consult the trigger/alias manual how to create them. Mudlet might require a completely different code.

0. If you don't man up to be the frontline, enable these two triggers:

Pattern: Your front line collapses!  Your group is thrown into chaos!

Command: |;man back

0.5

Pattern: You stumble as you try to move to the rear of the group.

Command: |;man back

Basically, it moves you out of the harm's way during the fight. It's the first trigger that you need. If there is one trigger to have, this is it.

1.

@leader -- 'all up'

Command: wake, stand, justup=1

Stop regenning, get up. Ready yourself to change.

Bonus:

@leader -- 'target *'

#IF {@justup=1} {eqs wear @mainmode;justup=0};

t=%1

On the first target from leader after regen, switch to your main mode. If you use a max mana mode (or your regen mode has more mana, than your main), you can benefit from some extra mana, if you change right before the mob. The caveat is that you need to be ready and pray the leader calls the target 2-3 seconds before the kill.

Also, you  capture the target (helpful for blind/weaken/damn and autoblast aliases).

2.

Pattern: @leader -- 'visage'

Command: cast 'undead visage'

Self-explanatory: you want to be visaged, when asked to. If you are the only person w/o visage, the mobs will pick you out first. Sometimes it hurts. Badly.

3.

@leader -- '@char gate %1'

E.g., Taron -- 'dr gate balthazar'

Command: cast 'gate' %1

If you only listen to the leader in this specific fashion, there's no room for mistakenly gating, when someone else says something, or when leader asks someone else.

You specifically gate the person/mob the leader asks you to.

4.

@leader -- 'wb up'

Command: cast 'water breath' @char

Put water breathing up, when required.

5.

@leader -- 'spectral'

Command: cast 'spectral shield' OR get abrasive @container, quaff abrasive OR get spectral-charm @container, use charm @char

Why? There are a few mobs with area spell damage or regen mobs and you may wonna have spectral shield up for them.

6.

For non-bards and non-healers:

@leader -- 'reign'

Command: |

The leader wants the mob to stop fighting the group and visa versa, so don't throw targeted spells at the mob. Healing tank is acceptable and probably encouraged, since the leader wants to walk away from the mob.

For bards:

Command: play 'reign of confusion'

Basically, you try to stop the fight from continuing. You can follow this up with play 'sacred reprieve', if the leader is not moving for some reason (e.g., is dead or ld and there's no staff).

Remember that you might have to keep casting this until the mob stops fighting (see below) or someone uses a red and white staff.

If you are a healer and are blasting, then you probably know to stop blasting/debuffing on reign.

7.

Pattern: steps back from the fight and

Command: | 

What it does:

- what you see is a fragment of a pattern, where a mob stops fighting, while under the influence of the 'reign of the confusion' bard song (see above)

- you stop executing any pre-typed commands, especially targeted damage spells/skills that affect the target. If you are a bard, you are stopping unnecessary reign of confusion (unless many mobs need to be stopped and only one did)

- you don't engage the mob by accident or on purpose, because the leader usually stops the fight on purpose (see above)

8.

Pattern: @tank yells '%1'$

Command: warcry %1

Wintin: warcry $1

The $ here marks the end of the line, so your %1 variable takes everything between the first and the last ', e.g.:

Tank yells 'WE'LL MAKE R'LYEH GREAT AGAIN!'

Taron yells 'LET'S ROCK!'

This trigger gives you 50-150 temporary hps, hitroll and damage, depending on tank's warcry points.

So, if you want to get more hps/hit/dam, create this trigger and join the warcry. This will also boost the tank's warcry points, which helps you, him and the entire groups he tanks for.

If you use more individual triggers that help you in groups, please share them.

</div>

<div class="post" data-post-id="36958" data-author="*juggleblood*" data-date="2016-06-13T22:06:18+00:00">

Good ones. 

I also like

Pattern: -- 'Is everybody here?'

Trigger: gt yup

</div>

<div class="post" data-post-id="36960" data-author="Teron" data-date="2016-06-14T07:09:03+00:00">

Well, the alternative is me not saying anything, just letting ppl get extra damage and learn. Do you think this is a better solution?

</div>

<div class="post" data-post-id="37005" data-author="Teron" data-date="2016-06-29T19:48:33+00:00">

Akaya has translated this script to Mudlet:

[<LINK_TEXT text="http://www.slothmud.org/forum/viewtopic ... 003#p37003">http://www.slothmud.org/forum/viewtopic.php?p=37003#p37003</LINK_TEXT>](http://www.slothmud.org/forum/viewtopic.php?p=37003#p37003)

Thanks, Akaya!

</div>
