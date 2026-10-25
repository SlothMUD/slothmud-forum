---
title: "Changelog 2017-12-02 - Post office changes"
topic_id: 4810
author: "*teker*"
date: 2017-12-12T00:10:45+00:00
last_activity: 2017-12-14T21:34:32+00:00
last_author: "*teker*"
sticky: false
locked: false
post_count: 2
---

<div class="post" data-post-id="38531" data-author="*teker*" data-date="2017-12-12T00:10:45+00:00">

First I want to remind everyone that the post office has issues with the Jan 1 rollover so everyone should be checking and receiving their packages before Jan 1.

The following items will go in with the next reboot:

I have rewritten the post office storage to put new packages into the database.  This will fix the Jan 1 problem moving forward.  Items with clasps and/or runes now cost more to ship.

Letters should remain intact if rented.

A natural extension of the post office was to add the ability to send coins to offline players.  This will now work at the bank.  Recipients will receive the transfer once they log back into the game.

I found an uninitialized variable in "pick" if your bard and thief levels are the same.  Fixed.

I found an uninitialized variable in "knight's blessing" that could add bizarre hidden effects to players.  Fixed.

I had done some earlier work in MSDP CHARACTER_AFFECTS that would show "cool down" numbers for aerial servant, mirror image, and endure/defy pain - but realized it was only working for cleric prime.  Fixed.

Added similar "cool down" info for these spells/skills to "score affects2".

I also rewrote the "cool down" counter for aerial servant and mirror image as it was tick based rather than time based.  Endure/defy was already time based.

</div>

<div class="post" data-post-id="38540" data-author="*teker*" data-date="2017-12-14T21:34:32+00:00">

I've received a couple bugs regarding restrung items not showing up correctly - I'm working on it and should have a fix in a few days.  People will most likely notice this with gems.

</div>
