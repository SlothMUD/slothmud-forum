---
title: "Rhodo Rune Eqset Issue"
topic_id: 4913
author: "Gorka"
date: 2019-06-01T13:10:32+00:00
last_activity: 2019-06-07T06:36:52+00:00
last_author: "Gorka"
sticky: false
locked: false
post_count: 5
---

<div class="post" data-post-id="39207" data-author="Gorka" data-date="2019-06-01T13:10:32+00:00" data-subject="Rhodo Rune Eqset Issue">

I finally got around to putting a Rhodo rune on eq for my blasting eq modes. However I quickly ran into a problem... I decided to put the Rhodo held low, when in all my other eq modes it's on my light. When switching from a blasting eq mode... it first attempts to wear my bauble... but at that moment my broom has not yet been unequipped held low and the double rhodo blocking code jumps into action.

Ideally the double rhodo blocking code shouldn't jump into action until all items are worn at the end. Maniac helped me out and I switched the Rhodo to my light as a bypass for now.

</div>

<div class="post" data-post-id="39209" data-author="Josiah" data-date="2019-06-03T02:18:30+00:00" data-subject="Re: Rhodo Rune Eqset Issue">

First world problem... "I haz too much Rhodo!"

In all seriousness though, I also ran into this problem.

</div>

<div class="post" data-post-id="39210" data-author="*Breeze*" data-date="2019-06-05T16:22:22+00:00" data-subject="Re: Rhodo Rune Eqset Issue">

not sure how to fix this.

i would guess change order that the eq is put on/off i guess. would need to look into teker code.

you could probably alias around it by removing those 2 items first

</div>

<div class="post" data-post-id="39211" data-author="Josiah" data-date="2019-06-07T06:22:20+00:00" data-subject="Re: Rhodo Rune Eqset Issue">

The best way I found was an eqset with a single piece of eq in it.  With minimal lag, you can quickly equip a light or held low with no rune.

Example:

eqset wear fakelight;eqset wear regen

</div>

<div class="post" data-post-id="39212" data-author="Gorka" data-date="2019-06-07T06:36:52+00:00" data-subject="Re: Rhodo Rune Eqset Issue">

Teker reckons he's fixed it in next reboot anyway.

</div>
