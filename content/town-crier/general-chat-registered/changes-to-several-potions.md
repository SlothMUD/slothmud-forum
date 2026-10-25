---
title: "Changes to several potions"
topic_id: 5008
author: "Driven"
date: 2021-01-25T00:07:39+00:00
last_activity: 2021-01-29T02:23:47+00:00
last_author: "Nyx"
sticky: false
locked: false
post_count: 5
---

<div class="post" data-post-id="39679" data-author="Driven" data-date="2021-01-25T00:07:39+00:00" data-subject="Changes to several potions">

FYI, we (read: the highly talented Teker) has tracked down the bug behind the recent crashes around the reading command and found that we were overrunning buffers in the rent code.  Based on the contents of the memory dumps, my strong suspicion is that the culprit was kangaroo pouches containing extremely high numbers of zero-weight potions.  Teker has rewritten the rent code to prevent the overruns, but for general stability reasons, we have changed wispy, good-intention, and mindflayer potions to weight 1.  For those of you with a huge stash of these potions in your kangaroo pouch, don't be surprised if you find your pouches to be tremendously heavy.  If you guys know of any more objects of weight zero that can be put in containers that do not count towards laden/rent counts, please let us know so that we can fix them.  The containers in question would be things like the kangaroo pouch, dice bag, flux of dreams, white silken bag, etc.

</div>

<div class="post" data-post-id="39680" data-author="Gorka" data-date="2021-01-25T13:58:56+00:00" data-subject="Re: Changes to several potions">

I often rent with 100 shards in my white-silken-bag. I'm not one of the potion hoarders. I junk almost everything I pop these days, or use potions immediately or very quickly after. 

I don't think changing the weight of shards is a good solution. The reason I don't use shards much and they tend to overflow, is because it takes Tonedeaf something like 45 seconds to create a single restoration charm, and when the charm is used it doesn't take into account heal bonuses. The shards can't be vaulted... and it's possible to regen an equivalent benefit in hp, and mana just by contemplation for the same amount of time making shards takes. They are really impractical.

I'd suggest 4 changes...

1) Make charms vaultable.

2) Include bonuses when they are used.

3) Do something about the 45 second sidhe animation to make 1 shard - because you tend to make them in batches. 

4) Someone make a charm bag? Was this something Mirage was going to do? Either the White silk bag needs an update or a charm bag should be added to shops.

If these changes were made, I'd do something about using them more often.

</div>

<div class="post" data-post-id="39681" data-author="Gorka" data-date="2021-01-25T14:12:10+00:00" data-subject="Re: Changes to several potions">

The other thing I could do is vault my hundred shards and junk all new ones, if it makes a difference to the mud.

Furthermore, on the subject of vaults... Are we going to hit similar size limits?... I have 1000 spaces set aside just for tokens... never mind my other crap.

</div>

<div class="post" data-post-id="39682" data-author="*teker*" data-date="2021-01-26T15:26:34+00:00" data-subject="Re: Changes to several potions">

- The "offer" limitation was really a limit in how the list was buffered and sent back to the player.  It wasn't a problem in the rent file.  I don't see future problems with potions or shards or gems in dice bags because the new buffer will grow if needed.

- It was my intention to keep the output identical - I saw your email that the list is no longer sorted.  I'll try to track that down in the next week and get it fixed.

- The vault code uses a different mechanism for displaying its contents that shouldn't be affected by this.

</div>

<div class="post" data-post-id="39683" data-author="Nyx" data-date="2021-01-29T02:23:47+00:00" data-subject="Re: Changes to several potions">

Found 3 to fix. Thanks.

Object 'potion periwinkle', Item type: POTION

Item is: NOBITS

Weight: 0, Value: 0gold, Worn in: TAKE 

Apply a bonus of 3 to the drinker's MAX_CON for 15 hours.

Object 'potion mauve', Item type: POTION

Item is: NOBITS

Weight: 0, Value: 0gold, Worn in: TAKE 

Apply a bonus of 2 to the drinker's MAX_DEX for 9 hours.

Object 'potion burgundy', Item type: POTION

Item is: NOBITS

Weight: 0, Value: 0gold, Worn in: TAKE 

Apply a bonus of 3 to the drinker's MAX_INT for 15 hours.

</div>
