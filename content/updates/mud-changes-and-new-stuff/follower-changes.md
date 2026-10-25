---
title: "Follower Changes"
topic_id: 3851
author: "*Splork*"
date: 2012-02-12T05:18:19+00:00
last_activity: 2012-02-12T05:18:19+00:00
last_author: "*Splork*"
sticky: false
locked: false
post_count: 1
---

<div class="post" data-post-id="33158" data-author="*Splork*" data-date="2012-02-12T05:18:19+00:00">

This change affects very few of you players but is yet another change which has been a long time coming. There are a couple of players which have been using hordes (6-9) of followers to run rampant through the mud. Obviously this is the last thing we want to see happening for a variety of reasons. Ive spoken to those involved and they are alright with the changes and understand fully why they needed to be done. They have also been very helpful in balancing this and other aspects of the game. 

Summary of the changes are this, Charms now count towards a player's total follower count and pts ( like necro undead ).  

Total number of charms allowed has been lowered from 4 to 3. 

Read the below for the actual code changes:

FOLLOWER CHANGES

Added a total_followers function. This checks for all followers, regardless of spell used to control the creature.

Added in control_undead and spell_person to total_servant_points function so that these followers get tallied into the total points a player has to control mobs.

Removed individual code in each necro follower spell to count control horde bonus and made get_total_control_horde_bonus. Replaced above code in several spells with the one function call. This way any changes defer to the one function rather than dozens of places inside 

our code.

Added checks to spell control_undead and spell charm_person for total_servant_points to control the proper amount of followers one player can have. Old checks for animate dead and summon undead work because the functions were changed, not spells.

Charms are worth 1 pt towards follower totals. Majority of pets are above 1 and increase upwards of 3. 

Total available charms have been lowered from 4 to 3 

Enjoy,

Splork

</div>
