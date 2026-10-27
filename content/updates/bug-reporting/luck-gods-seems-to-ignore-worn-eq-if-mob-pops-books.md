---
title: "luck gods seems to ignore worn eq, if mob pops books"
topic_id: 4786
author: "Teron"
date: 2017-08-23T07:27:42+00:00
last_activity: 2017-08-26T08:56:36+00:00
last_author: "*Breeze*"
sticky: false
locked: false
post_count: 6
---

<div class="post" data-post-id="38414" data-author="Teron" data-date="2017-08-23T07:27:42+00:00" data-subject="luck gods seems to ignore worn eq, if mob pops books">

Hi.

I've been cycling the War Avatar for greaves, and tried singing to him with my bard.

3-4 on separate times it said that "luck gods smile at you, but the avatar only loaded the berserk manual, no greaves.

I suspect that the code prioritizes song affect and loads the book, rather than helping loading the greaves, because I've killed him about 10-15 times on BH days, half of repops were with the bard singing luck gods at 27 charisma.

There might be other mobs with a similar situation.

Could anyone check this please? Thanks

</div>

<div class="post" data-post-id="38415" data-author="*Breeze*" data-date="2017-08-24T18:59:32+00:00" data-subject="Re: luck gods seems to ignore worn eq, if mob pops books">

its not even that complicated..

if (try1 == fail)

{

 try\_again()

}

oversimplifed but thats how it works.

basically the same as the original gempop special before i changed it due to nagging.

</div>

<div class="post" data-post-id="38416" data-author="Teron" data-date="2017-08-25T08:32:03+00:00" data-subject="Re: luck gods seems to ignore worn eq, if mob pops books">

So I assume the song works on all items that the mob pops.

Thanks.

</div>

<div class="post" data-post-id="38417" data-author="*Breeze*" data-date="2017-08-25T18:43:13+00:00" data-subject="Re: luck gods seems to ignore worn eq, if mob pops books">

anything zoned. if something is loaded via mudl (not much is) then it uses it.

</div>

<div class="post" data-post-id="38418" data-author="Teron" data-date="2017-08-26T07:30:21+00:00" data-subject="Re: luck gods seems to ignore worn eq, if mob pops books">

How was the gempop special changed?

Thanks

</div>

<div class="post" data-post-id="38419" data-author="*Breeze*" data-date="2017-08-26T08:56:36+00:00" data-subject="Re: luck gods seems to ignore worn eq, if mob pops books">

Adjusted rate to be a little higher and added the code to upgrade gem to next tier (the alternate message when a gem loads)

</div>
