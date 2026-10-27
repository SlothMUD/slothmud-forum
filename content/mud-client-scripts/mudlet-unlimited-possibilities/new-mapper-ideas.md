---
title: "New mapper ideas"
topic_id: 4548
author: "Arus"
date: 2015-12-04T05:09:05+00:00
last_activity: 2015-12-08T07:25:20+00:00
last_author: "Arus"
sticky: false
locked: false
post_count: 6
---

<div class="post" data-post-id="36245" data-author="Arus" data-date="2015-12-04T05:09:05+00:00" data-subject="New mapper ideas">

I am thinking of writing a Mudlet mapper that uses all of the information available from COORD1-25 (exits, terrain, mobs, player characters). Eventually I want to track the movement of MOBs in the neighborhood and match them to POPPERS in EQList database. But in order to do that first I need AREA\_VNUM in REPORTED\_VARIABLES and MOB\_VNUM replacing MOB in COORD1-25. Thanks

What's the deal with ROOM\_RNUM being always lower than ROOM\_VNUM by 22856? As far as I understand, ROOM\_RNUM starts with AREA\_INFO like 113 "Newbatia"+44 "South Gate". But why do we need ROOM\_VNUM? Why do you have two room identifiers?

Akaya, where are you? Have you stopped developing for SlothMUD?

</div>

<div class="post" data-post-id="36249" data-author="*teker*" data-date="2015-12-04T15:51:52+00:00" data-subject="Re: New mapper ideas">

I can't speak as to the (MSDP?) variables you mentioned, but I can describe how RNUMs and VNUMs work in the game.

Builders are given a range of VNUMs for building their rooms/mobiles/objects. It's a unique value that never changes once it's assigned unless the room/mob/obj is deleted. The VNUMs are assigned in contiguous blocks for zones and usually gaps are left between zones for later additions.

The RNUM refers to where the room/mobile/object is stored in memory. It would be a waste of memory to allocate space for VNUMs that do not exist, so the game skips these. The RNUMs can and do change when new rooms/mobs/objs are added to the game because the RNUM lists are stored in VNUM order. So if I create a new room with VNUM 45000, the RNUM for all rooms with VNUM \> 45000 will increase by 1.

So you really want to save VNUMs on anything that persists long-term.

</div>

<div class="post" data-post-id="36252" data-author="Arus" data-date="2015-12-04T17:22:49+00:00" data-subject="Re: New mapper ideas">

Okay, but why did COORD1-25 report ROOM\_RNUM not ROOM\_VNUM? Bring them back please.

</div>

<div class="post" data-post-id="36259" data-author="Arus" data-date="2015-12-05T21:00:14+00:00" data-subject="Re: New mapper ideas">

Why does msdp.ROOM\_VNUM report two events during movement? <img src="/images/smilies/icon_eek.svg" alt=":shock:" title=":shock:" width="15" height="15" class="smiley nozoom"> 

First it reports RNUM and only then it reports correct VNUM.

If RNUMs are not permanent, then why does COORD1 report RNUM in Room? 

I could use ROOM\_EXITS for adjacent room VNUMs, but its being reported every second while standing to report STATUS... 

So I \*have\* to use COORD1 with its unreliable RNUMs. Please change COORD1 to report VNUMs instead. <img src="/images/smilies/icon_cry.svg" alt=":cry:" title=":cry:" width="15" height="15" class="smiley nozoom">

</div>

<div class="post" data-post-id="36263" data-author="*Splork*" data-date="2015-12-06T02:40:26+00:00" data-subject="Re: New mapper ideas">

> <strong>Quote:</strong>
> If RNUMs are not permanent, then why does COORD1 report RNUM in Room?

The original COORD code did use rnums because we used a previously coded function(Map command) for the map coordinates. This code was developed using Rnums because they were never intended to be reported and was done well before MSDP. Later on, I switched this to use vnums. It was during this time that we began experiencing issues with game performance and because this project was experimental, I removed it. At least I thought I had. Apparently, I had somehow left in the COORD Rnum code which you somehow found.

On reboot, the COORD code will use vnums, as it should.

> <strong>Quote:</strong>
> Why does msdp.ROOM\_VNUM report two events during movement? <img src="/images/smilies/icon_eek.svg" alt=":shock:" title=":shock:" width="15" height="15" class="smiley nozoom">

This is also resolved. MSDP is still reporting twice but you will probably not notice it because its just a backup.

Splork

</div>

<div class="post" data-post-id="36275" data-author="Arus" data-date="2015-12-08T07:25:20+00:00" data-subject="Re: New mapper ideas">

Could you please add AREA\_VNUM to COORD1-25 (just for the room not the exits)?

Thank you very much!

This will help tremendously <img src="/images/smilies/icon_mrgreen.svg" alt=":mrgreen:" title=":mrgreen:" width="15" height="15" class="smiley nozoom">

</div>
