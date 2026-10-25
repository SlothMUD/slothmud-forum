---
title: "Changelog 2016-01-25 (vault news)"
topic_id: 4583
author: "*teker*"
date: 2016-01-25T16:53:43+00:00
last_activity: 2016-02-02T00:02:26+00:00
last_author: "*Breeze*"
sticky: false
locked: false
post_count: 10
---

<div class="post" data-post-id="36542" data-author="*teker*" data-date="2016-01-25T16:53:43+00:00">

First the smaller stuff:

The equipment set code has been disabled until I can figure out the loop we're seeing.  Should only affect the few testers that knew of the command and were using it.

Items with clasps and/or runes are no longer being "grouped" in inventory lists.

The crash this weekend may be fixed - it appears to be in the monk proc and it looks like the mob died from attempting to strike or stun it's opponent.  I'm guessing someone had a spell up to cause damage back at the monk.

Sleeping players should see group leader changes.

So the new vault code is in.  I've found some minor formatting issues and a bug in my migration process but the bulk of the code seems good.  I haven't had time to update the in-game help files but I did write a wiki guide at [http://www.slothmud.org/wiki/Guide:Housing](http://www.slothmud.org/wiki/Guide:Housing) .  It details the process for building your first room and purchasing enhancements and upgrades to the vault.  It also has directions to the new zones that have been created on AH and IS for housing (thanks Neptune!).  The old zone on AH was full and there never was an official zone on IS so we've created new ones near the recall spots.

The new houses allow you to:

- Purchase additional vault slots, regen bonuses, and upgrade bonuses automatically

- Purchase and connect additional rooms in a single command

- Deposit items with clasps, runes, and/or contents

- Deposit and withdraw items using keyword, all.keyword or all

- Customize teleportation messages in and out of the vault

- Once equipment sets are fixed, you'll be able to deposit or withdraw an entire set in one command

- If I can get help with the web site, you'll be able to view vault items there

All new houses will be constructed with the new code.  I can (and would like to) migrate existing houses to the new code.  I'll try to get on and spend some time doing this for people this week.  But it requires that the player who originally bought the vault is logged in and that the vault is empty.  Once I get the migration bug fixed, other imms will be able to do this as well.

</div>

<div class="post" data-post-id="36543" data-author="cyprimus" data-date="2016-01-25T17:15:48+00:00">

Do we convert one vault at a time?  I have too many to possibly carry all of the content..even for just one continent at a time..

</div>

<div class="post" data-post-id="36544" data-author="*teker*" data-date="2016-01-25T17:22:17+00:00">

I upgrade one room at a time so we can withdraw, upgrade, deposit, repeat.

</div>

<div class="post" data-post-id="36545" data-author="cyprimus" data-date="2016-01-25T17:24:52+00:00">

Great! 

Thanks!

</div>

<div class="post" data-post-id="36550" data-author="cyprimus" data-date="2016-01-26T19:58:35+00:00">

Oh, other question... on eq sets... will they carryover between alts?  Will we need to create alt trees? or just set up eq for each alt separately?

</div>

<div class="post" data-post-id="36554" data-author="*teker*" data-date="2016-01-26T23:42:49+00:00">

Equipment sets are unique per character.  There is no facility to share them between characters.

I should be in tomorrow to start on vault upgrades.  I've noticed something that I want to change regarding keyless entry so I'd like to wait on those rooms until the next build.  But if people have back rooms or vaults without keyless we can start with those.

</div>

<div class="post" data-post-id="36555" data-author="Yasik" data-date="2016-01-27T09:58:05+00:00">

> ***teker* wrote:**
> I've noticed something that I want to change regarding keyless entry...

Will there be reimbursements? We pay 1 million coins per key.

</div>

<div class="post" data-post-id="36558" data-author="*teker*" data-date="2016-01-27T15:47:02+00:00">

I'm not giving out coins during the upgrades, if that's what you're asking.  If a vault already has say recall or keyless entry enabled, I'll make sure the features are enabled after the upgrade without any extra charges.  Keys are still useful for vaults with keyless entry - they're the only free way to let others in the vault.

</div>

<div class="post" data-post-id="36570" data-author="*teker*" data-date="2016-02-01T20:59:50+00:00">

The new customizable vault messages went in this morning so you can modify the strings when teleporting in and out of the vault using keyless entry and/or say recall.  You can see the options on the wiki or by typing HOUSE LIST <recall|keyless>.  It should go without saying (but I'm saying it anyway) that messages displayed in common areas (outside the vault) should be tasteful and in a similar theme to the game.  

I think the upgrades have gone fairly smoothly so far - I'm finding a few minor things during the process but once the process is done everything with the vault seems to be working 100%.

I've received feedback from one clan regarding clan vaults requesting that:

- Clan officers be the only ones allowed to buy keys

- Any clan member can add themselves to the keyless entry permit list

Any other clan leaders want to speak up on this topic?

</div>

<div class="post" data-post-id="36571" data-author="*Breeze*" data-date="2016-02-02T00:02:26+00:00">

"officially" there is no such thing as clan vaults.

we just treat them as clan vaults.

if you want to go through the effort to add clan specific code, we can talk about it 

but there is no such thing as clan vaults.  we just made vaults with 1 char in charge;;; and a few of the keyless stuff i added clan checks, but officially there is no such thing as clan vaults.

come up with a plan for clan specific stuff and we discuss it.

// B

</div>
