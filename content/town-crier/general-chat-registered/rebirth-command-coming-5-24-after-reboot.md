---
title: "Rebirth command coming 5/24 after reboot"
topic_id: 4852
author: "*teker*"
date: 2018-05-23T18:18:12+00:00
last_activity: 2018-06-04T20:33:56+00:00
last_author: "*Breeze*"
sticky: false
locked: false
post_count: 18
---

<div class="post" data-post-id="38805" data-author="*teker*" data-date="2018-05-23T18:18:12+00:00" data-subject="Rebirth command coming 5/24 after reboot">

The prime goal here being to automate the rebirth process that Breeze is currently performing manually. The command is REBIRTH 1/0 or REBIRTH 1/1/0. The instructions I've been given to code (and have completed) are as follows:

Players have 2 options:

\- Option 1: Rebirth to level 1/0 - primary class is level 1 and the rest are 0 and can be reordered. This option involves a reset of stats to 13 and you'll be rerolled per a new character at levels 8/1.

\- Option 2: Rebirth to level 1/1/0 - primary and secondary classes are level 1 and the rest are 0 and can be reordered. No change in stats and no free rerolls at level 8/1

Both options include:

\- Experience reset to 1.

\- Drachma reset to 0. \*\*\* UPDATED 5/24 \*\*\*

\- Zone visitation info cleared.

\- Quest completion cleared except for enlisting in the army and moon temple.

\- Remmort flag/bonuses enabled.

\- Avatar shop bonuses kept - but only 1/2 effective until regaining 9x40. Max stats purchased at the avatar shop will remain. \*\* UPDATED 5/24 \*\*\*

\- Rank/honor remains unchanged.

Questions?

</div>

<div class="post" data-post-id="38809" data-author="cyprimus" data-date="2018-05-23T22:35:02+00:00" data-subject="Re: Rebirth command coming 5/24 after reboot">

Can we repeat the process indefinately?

</div>

<div class="post" data-post-id="38811" data-author="Filk" data-date="2018-05-24T02:30:11+00:00" data-subject="Re: Rebirth command coming 5/24 after reboot">

> <strong>Quote:</strong>
> Drachma remains unchanged.

Thats correct? In Breeze version(which in the help file), drachma was reduced to 0 as well.

And there are nothing about max stats. They were staying. Acording to helpfile and other players.

</div>

<div class="post" data-post-id="38812" data-author="cyprimus" data-date="2018-05-24T02:36:25+00:00" data-subject="Re: Rebirth command coming 5/24 after reboot">

not true fluffy. 

Stats were reset if you changed classo. regardless of having 19's in all etc..

Drac was reset to 0. and you could rerun the continents quests.. from the town questmasters.. and a few others.

</div>

<div class="post" data-post-id="38814" data-author="Filk" data-date="2018-05-24T02:43:43+00:00" data-subject="Re: Rebirth command coming 5/24 after reboot">

> <strong>cyprimus wrote:</strong>
> not true fluffy. 
> 
> Stats were reset if you changed classo. regardless of having 19's in all etc..

I meant only 1/1/0 variant. Gorka said he got his max dex at 3x40, when his classo allowed that max stat. I assume he got his 19 str at level 40 also.

</div>

<div class="post" data-post-id="38818" data-author="Teron" data-date="2018-05-24T11:51:08+00:00" data-subject="Re: Rebirth command coming 5/24 after reboot">

About stats for 1/0:

[http://www.slothmud.org/forum//viewtopic.php?t=4850#p38795](http://www.slothmud.org/forum//viewtopic.php?t=4850#p38795)

> <strong>Breeze wrote:</strong>
> i would be willing to change the bought stats to match a classo though.
> 
> 
> 
> that is if you have bought str / dex and your new classo uses int/str i would change 
> 
> bought str to int and bought dex to str

</div>

<div class="post" data-post-id="38819" data-author="*teker*" data-date="2018-05-24T13:00:07+00:00" data-subject="Re: Rebirth command coming 5/24 after reboot">

I currently have the function set to block multiple rebirthing. We should probably discuss bonuses for multiple rebirths before making it possible.

Max stat purchase is tracked on the player and does persist through rebirth. I thought that it wouldn't go live until 9x40 but maybe it doesn't get halved like the other stats. I don't think stat purchase up to 18 is saved anywhere so I believe going to lose those purchases.

</div>

<div class="post" data-post-id="38820" data-author="*teker*" data-date="2018-05-24T14:06:09+00:00" data-subject="Re: Rebirth command coming 5/24 after reboot">

I've updated a couple items on the original post. Namely:

\- Max stat purchases to take effect at level 1. That means if you purchased MAX\_STR and get reset to 13s, your strength will be a natural 14. If you reroll, you get your new strength roll +1. Except that normal max stat rules apply, you can't be a level 1 with 19 strength.

\- Drachma now reset to 0 to make it consistent with the help file and previous manual rebirths. Your quest history is mostly wiped so you'll be able to redo nearly ever quest in the game to earn it back.

</div>

<div class="post" data-post-id="38823" data-author="Gorka" data-date="2018-05-24T14:12:28+00:00" data-subject="Re: Rebirth command coming 5/24 after reboot">

The MAX\_STATS on Gorka remained on my msdp.CHARACTER\_AFFECTS through rebirth. I saw them listed in there from the first day... however the stats did not become "active" until my class order allowed. So in Gorka's case wa mo, my purchased MAX\_DEX kicked in when I became 3x40. There is also something up with the ARMOR stat, that seems to have persisted from the start of rebirth as well, well the other stats were halved. (as I expected)

Now this is just my opinion... and yes, it's completely self serving... But enabling all the stats in full from the start probably doesn't make much difference... I levelled so fast, and I had so much power in the form of elite eq available to me, that +2 dam and +2 hit and +3 handdam and +12spellbonus probably doesn't mean much. You get to wear so much of your elite eq so quickly, I really don't think halving them matters that much to be honest.

</div>

<div class="post" data-post-id="38825" data-author="*teker*" data-date="2018-05-24T15:25:40+00:00" data-subject="Re: Rebirth command coming 5/24 after reboot">

Some issues so far:

\- It's not setting up remort correctly so the xp bonus isn't being applied. Should have a fix in for next reboot.

\- You can't use the HOUSE command to buy extras on vaults until level 8. So you might want to store your high level gear before you rebirth. We are forcing a "remove all" as part of the rebirth process so you do end up with a lot of gear in inventory. I have a fix for the house command at next reboot as well.

</div>

<div class="post" data-post-id="38827" data-author="*teker*" data-date="2018-05-24T17:34:12+00:00" data-subject="Re: Rebirth command coming 5/24 after reboot">

Norks is reporting that avatar shop sanctuary, resist cold, and resist fire don't work after rebirth. I imagine this is probably consistent across all rebirthers.

</div>

<div class="post" data-post-id="38833" data-author="Filk" data-date="2018-05-31T02:07:41+00:00" data-subject="Re: Rebirth command coming 5/24 after reboot">

I just realised other rebirthers can use their avatar lights, while i cant. Guess thats related to the thing Teker gave me to manualy fix double exp, but maybe its something else.

</div>

<div class="post" data-post-id="38835" data-author="*Breeze*" data-date="2018-05-31T09:40:58+00:00" data-subject="Re: Rebirth command coming 5/24 after reboot">

its because they are personal items so i removed the 

avatar restriction when i remembered to.

there is also a way to recycle your avatar light so you can rebuild it.

\*edit\* - Fixed

</div>

<div class="post" data-post-id="38836" data-author="*teker*" data-date="2018-05-31T14:16:56+00:00" data-subject="Re: Rebirth command coming 5/24 after reboot">

I just fixed Paka's also. Let us know if there are others. It looks like the code has been fixed for new avatar lights.

</div>

<div class="post" data-post-id="38837" data-author="*Breeze*" data-date="2018-05-31T18:47:14+00:00" data-subject="Re: Rebirth command coming 5/24 after reboot">

> <strong>\*teker\* wrote:</strong>
> I just fixed Paka's also. Let us know if there are others. It looks like the code has been fixed for new avatar lights.

yep. did that when josiah rebirthed <img src="/images/smilies/icon_e_smile.svg" alt=":)" title=":)" width="15" height="15" class="smiley nozoom">

</div>

<div class="post" data-post-id="38850" data-author="*teker*" data-date="2018-06-04T15:01:32+00:00" data-subject="Re: Rebirth command coming 5/24 after reboot">

Today's reboot was for bug fixes and most of those were rebirth related. You should be able to store 3x40 equipment in the new vaults now, for instance. It seems like most of the rebirths are at 3x40 or beyond so it may be the next batch that actually sees the changes.

</div>

<div class="post" data-post-id="38851" data-author="norks" data-date="2018-06-04T15:37:21+00:00" data-subject="Re: Rebirth command coming 5/24 after reboot">

Great thanks.

Can you fix rank gain too please? At the moment it's not possible to gain rank in moon temple if one isn't at least a level 1 avatar. Asking around this seems to be a bug rather than a feature.

Thanks,

Norks

</div>

<div class="post" data-post-id="38854" data-author="*Breeze*" data-date="2018-06-04T20:33:56+00:00" data-subject="Re: Rebirth command coming 5/24 after reboot">

pretty sure i said in group last night that i need someone there 

who is bugged, so i can see what the bug is so i can look at it.

</div>
