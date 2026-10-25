---
title: "Equipment sets"
topic_id: 4590
author: "*teker*"
date: 2016-02-15T16:04:43+00:00
last_activity: 2016-02-21T01:06:49+00:00
last_author: "Teron"
sticky: false
locked: false
post_count: 20
---

<div class="post" data-post-id="36596" data-author="*teker*" data-date="2016-02-15T16:04:43+00:00" data-subject="Equipment sets">

So we've been running a few days without any problems in the equipment set code, so I figured I'd announce it to the general public.  The basic idea is that each player can design custom sets of equipment and then change between them in an easy fashion.  HELP EQSET has all the information regarding the new command and how it works.  I do have some debugging in there to try to catch the hang we were seeing so if you see some weird output as a result of the command, please let me know.

</div>

<div class="post" data-post-id="36599" data-author="Dragoth" data-date="2016-02-16T08:35:40+00:00" data-subject="Re: Equipment sets">

Looks very good!

But PLEASE cut the lagg in half !

</div>

<div class="post" data-post-id="36600" data-author="Dragoth" data-date="2016-02-16T11:57:31+00:00" data-subject="Re: Equipment sets">

I changed my mind, this is not just very good, this is INSANELY good!

This script:

#SW (@mode=Regen AND @heal=off AND @charisma=off) {rem all;#if (@darkmace>0) {wie dark-mace};#if (@gaunts=mana) {detach lord tendon;attach lord banded};detach righteous lotus-blossom;detach righteous 2.lotus-blossom;detach iolite ars;detach golden-charm 1.green-claw;detach golden-charm 2.green-claw;detach emerald ring-radiance;detach emerald 2.ring-radiance;get wereraven robe-healer;get all.ring-spider wereraven;get adamantium-sceptre wereraven;get strip-bloody wereraven;get guards wereraven;attach golden-charm darksteel-guards;attach iolite adamantium;attach righteous-cause strip-bloody;attach righteous-cause bracer-order;attach emerald-insight spider-ring;attach lord banded-sleeves;attach emerald-insight 2.spider-ring;wear strip-bloody adamantium-sceptre darksteel-guards banded thunder gown bracer-order spider-ring spider-ring;put all robe-healer;get sack robe-healer;get wereraven robe-healer;detach brooch robe-healer;attach brooch wereraven;get @water robe-healer;get all wereraven;put robe-healer wereraven;put vest wereraven;wear all;#if (@darkmace>0) {rem dark-mace};#var mode Armor} (@mode=Armor AND @charisma=off) {rem all;detach iolite adamantium-sceptre;detach righteous strip-bloody;detach righteous bracer-order;detach golden-charm darksteel-guards;#if (@darkmace>0) {wie dark-mace};detach emerald-insight 1.spider-ring;detach emerald-insight 2.spider-ring;put all wereraven-cloak;get iolite wereraven-cloak;get all.emerald-insight wereraven-cloak;get golden-charm wereraven;get all.righteous-cause wereraven;get banded-sleeves wereraven-cloak;detach lord banded-sleeves;get bracer-order wereraven-cloak;get gown wereraven-cloak;get thunder-gauntlets wereraven-cloak;get robe-healer wereraven-cloak;detach brooch wereraven;attach brooch robe-healer;get @water wereraven-cloak;get sack wereraven-cloak;get all robe-healer;attach righteous-cause blossom;attach righteous-cause 2.blossom;attach iolite ars;attach golden-charm green-claw;put wereraven-cloak robe-healer;attach lord tendon;attach emerald-insight ring-radiance;attach emerald-insight 2.ring-radiance;wear all;#var mode Regen}

just became this : 

#SW (@mode=Regen AND @heal=off AND @charisma=off) {eqset switch armor;#var mode Armor} (@mode=Armor AND @charisma=off) {eqset switch regen;#var mode Regen}

And it's only 1 example of many eq changers i had, and it takes 1 seconds to switch..

*Bow* Teker

</div>

<div class="post" data-post-id="36601" data-author="*teker*" data-date="2016-02-16T15:15:41+00:00" data-subject="Re: Equipment sets">

You may not have been able to tell before, but there's always been a small amount of lag when wearing and removing items.  The eqset command just adds them up - there's no extra lag involved.

I received a couple tells while I was AFK about some issues people were having - please post them here.  I recall seeing the following in my buffer:

1) Something regarding switches with rose oil not working.  Probably something related to it being non-removable.  If someone can show me what's going on during a "switch" or "wear" with the "debug" flag set I can take a look at it.

2) Someone had their containers reset at rent.  One thing to keep in mind is that the container is set to a particular instance of an item - not the type.  This means that if you designate "a golden sack" as your default container, it saves the hidden id associated with that sack.  If you pop another one, it will have a different id and the code will not confuse the two.  It also means that if you lose your original sack (or deposit in vault, or sell, etc) the code will decide that the container is missing and will leave items in inventory.

</div>

<div class="post" data-post-id="36602" data-author="Ker" data-date="2016-02-16T17:59:28+00:00" data-subject="Re: Equipment sets">

Good day,

Great addition, really nice.

Currently it works nicely - but I get this message trying to sort shifted in form.

"Mobiles don't need equipment sets!"

Are we able to sort accordingly already shifted(ac/regen/spellsave for example) or still need change to human to do it?

Kind regards,

Dr

</div>

<div class="post" data-post-id="36603" data-author="*teker*" data-date="2016-02-16T18:47:41+00:00" data-subject="Re: Equipment sets">

Ok, I've reproduced the "rose oil" issue which is really an issue for any clasp that has a maximum number that can be worn at one time.  Affects runes also.  You've been experiencing this if you've seen something like:

<A rune or clasp> is preventing you from using the item...

You can't wear <something>.

Most people are seeing this when attempting to switch between 2 items that have the same clasp/rune that is limited by a maximum number.  I have a fix for this but it will require another build/reboot.

There's another bug which is displaying an "ERROR!" message which I think I have tracked down, but will require another build/reboot to verify.

I will check into whether or not it's safe to perform eqset actions while shifted.

</div>

<div class="post" data-post-id="36604" data-author="*teker*" data-date="2016-02-16T23:51:21+00:00" data-subject="Re: Equipment sets">

I've uploaded a guide to the wiki.  It includes some scenarios that I think people will find useful.  If there are other "frequently asked questions" please let me know.

[http://www.slothmud.org/wiki/Guide:Eqset](http://www.slothmud.org/wiki/Guide:Eqset)

</div>

<div class="post" data-post-id="36605" data-author="Dragoth" data-date="2016-02-17T08:49:21+00:00" data-subject="Re: Equipment sets">

Ok, I think i did everything as explained by the wiki:

1) Save my regen set as eqset preset 1

2) While wearing my regen set, assign all my regen items to use radiant-robe as container (eqset setcontainer raven-robe all)

3) Save my solo set as eqset preset 2

4) While wearing my solo set, assign all solo items to use wereraven-cloak as container

5) So that my wereraven cloak is not stored in inventory when I switch to regen set, I assign radiant-robe as default container for wereraven-cloak (while wearing weraraven-cloak, eqset setcontainer radiant-robe wereraven-cloak)

Now when I switch from solo to regen, all my solo items are put into wereraven cloak and wereraven cloak is put into radiant-robe

6) While in regen mode I now assign radiant-robe to use wereraven-cloak as it's container (eqset setcontainer wereraven-cloak radiant-robe)

Now when i switch from regen to solo, all my regen items are put into radiant-robe and my radiant-robe is put into wereraven-cloak

Now this works fine! But as soon as I rent and come back, all my container links are gone.

Here is an example with Anrok, added a divider "-" before container, so it's easier on the eye 

Equipment Set 'armor':

Position        Item                            -Container

Light           a tiger eye stone               - an elven cloak of agility

   Clasp        a flawed glowing gem            - an elven cloak of agility

Left Finger     an enchanted band of hematite   - an elven cloak of agility

   Clasp        an emerald of insight           - Shroud of the Undead Spiritcharmer

Right Finger    a heavy iron ring               - an elven cloak of agility

   Clasp        an emerald of insight           - Shroud of the Undead Spiritcharmer

Shoulders       darksteel shoulder guards       - an elven cloak of agility

   Clasp        a purple minidemon brooch       - an elven cloak of agility

Neck 2          a thief's shadow bending half-  - an elven cloak of agility

   Clasp        a red minidemon brooch          - an elven cloak of agility

Body            Adamantine Cuirass of the Anci  - an elven cloak of agility

Head            a crimson tri-cornered hat      - an elven cloak of agility

   Clasp        the crest of the crimson bucca  - an elven cloak of agility

Legs            chiseled granite greaves        - an elven cloak of agility

   Clasp        a polished spectrolite charm    - an elven cloak of agility

Feet            black orcskin boots             - an elven cloak of agility

Hands           Talons of the Dragon Lords      - an elven cloak of agility

Arms            amethyst-inlaid mithril bracer  - an elven cloak of agility

Shield          a crystal greatshield           - an elven cloak of agility

About           - an elven cloak of agility       - Shroud of the Undead Spiritcharmer

   Clasp        a golden, four-pointed star (M  - Shroud of the Undead Spiritcharmer

Waist           a feathered cincture            - an elven cloak of agility

Left Wrist      the Bracelet of the High Orc    - an elven cloak of agility

Right Wrist     the Bracelet of the High Orc    - an elven cloak of agility

Wielded         a jeweled saber                 - an elven cloak of agility

Held            an obsidian pearl               - an elven cloak of agility

Equipment Set 'undead':

Position        Item                            -Container

Light           eye of the undead               - Shroud of the Undead Spiritcharmer

Left Finger     a ring of imminent death        - Shroud of the Undead Spiritcharmer

   Clasp        an emerald of insight           - Shroud of the Undead Spiritcharmer

Right Finger    a ring of imminent death        - Shroud of the Undead Spiritcharmer

   Clasp        an emerald of insight           - Shroud of the Undead Spiritcharmer

Shoulders       woven shoulder guards of flesh  - Shroud of the Undead Spiritcharmer

   Clasp        a clasp of life and death       - Shroud of the Undead Spiritcharmer

Neck 2          an ugly decaying ankh           - Shroud of the Undead Spiritcharmer

Body            a blackened, corrupted rose     - Shroud of the Undead Spiritcharmer

Head            a ruby-inlaid crown             - Shroud of the Undead Spiritcharmer

Legs            a set of polished bone legging  - Shroud of the Undead Spiritcharmer

Feet            boots of radiance               - Shroud of the Undead Spiritcharmer

Hands           arcane gauntlets of the moon    - Shroud of the Undead Spiritcharmer

Arms            a set of ruby studded vambrace  - Shroud of the Undead Spiritcharmer

Shield          a shield of stolen souls        - Shroud of the Undead Spiritcharmer

About           Shroud of the Undead Spiritcha  - an elven cloak of agility

   Clasp        a golden, four-pointed star (M  - Shroud of the Undead Spiritcharmer

Waist           a golden-feathered girth        - Shroud of the Undead Spiritcharmer

Left Wrist      a strand of opalescent silk     - Shroud of the Undead Spiritcharmer

Right Wrist     a strand of opalescent silk     - Shroud of the Undead Spiritcharmer

Wielded         a staff of entwined serpents    - Shroud of the Undead Spiritcharmer

Held            Grey Tome with Silver Runes     - Shroud of the Undead Spiritcharmer

And now as soon as i rent and come back this happens:

Equipment Set 'armor':

Position        Item                            Container

Light           a tiger eye stone               an elven cloak of agility

   Clasp        a flawed glowing gem            [ Default ]

Left Finger     an enchanted band of hematite   [ Default ]

   Clasp        an emerald of insight           [ Default ]

Right Finger    a heavy iron ring               [ Default ]

   Clasp        an emerald of insight           [ Default ]

Shoulders       darksteel shoulder guards       [ Default ]

   Clasp        a purple minidemon brooch       [ Default ]

Neck 2          a thief's shadow bending half-  [ Default ]

   Clasp        a red minidemon brooch          [ Default ]

Body            Adamantine Cuirass of the Anci  [ Default ]

Head            a crimson tri-cornered hat      [ Default ]

   Clasp        the crest of the crimson bucca  [ Default ]

Legs            chiseled granite greaves        [ Default ]

   Clasp        a polished spectrolite charm    [ Default ]

Feet            black orcskin boots             [ Default ]

Hands           Talons of the Dragon Lords      [ Default ]

Arms            amethyst-inlaid mithril bracer  [ Default ]

Shield          a crystal greatshield           [ Default ]

About           an elven cloak of agility       [ Default ]

   Clasp        a golden, four-pointed star (M  [ Default ]

Waist           a feathered cincture            [ Default ]

Left Wrist      the Bracelet of the High Orc    [ Default ]

Right Wrist     the Bracelet of the High Orc    [ Default ]

Wielded         a jeweled saber                 [ Default ]

Held            an obsidian pearl               [ Default ]

Equipment Set 'undead':

Position        Item                            Container

Light           eye of the undead               Shroud of the Undead Spiritcharmer

Left Finger     a ring of imminent death        Shroud of the Undead Spiritcharmer

   Clasp        an emerald of insight           [ Default ]

Right Finger    a ring of imminent death        Shroud of the Undead Spiritcharmer

   Clasp        an emerald of insight           [ Default ]

Shoulders       woven shoulder guards of flesh  [ Default ]

   Clasp        a clasp of life and death       [ Default ]

Neck 2          an ugly decaying ankh           [ Default ]

Body            a blackened, corrupted rose     [ Default ]

Head            a ruby-inlaid crown             [ Default ]

Legs            a set of polished bone legging  [ Default ]

Feet            boots of radiance               [ Default ]

Hands           arcane gauntlets of the moon    [ Default ]

Arms            a set of ruby studded vambrace  [ Default ]

Shield          a shield of stolen souls        [ Default ]

About           Shroud of the Undead Spiritcha  [ Default ]

   Clasp        a golden, four-pointed star (M  [ Default ]

Waist           a golden-feathered girth        [ Default ]

Left Wrist      a strand of opalescent silk     [ Default ]

Right Wrist     a strand of opalescent silk     [ Default ]

Wielded         a staff of entwined serpents    [ Default ]

Held            Grey Tome with Silver Runes     [ Default ]

</div>

<div class="post" data-post-id="36606" data-author="Dragoth" data-date="2016-02-17T09:20:30+00:00" data-subject="Re: Equipment sets">

Ok, after testing this some more, I think i found that it's the clasps that are causing the setcontainer resets.

Any item that has clasp attached, even if it's only used in 1 set, will reset the setcontainer parameter for all items that go after this clasp in eqset.

I have removed all clasps except 1 for testing purposes and only used 1 set

Here is a set before rent:

Equipment Set 'regen':

Position        Item                            Container

Light           a philosopher's stone          - a robe of raven's feathers

Left Finger     a basalt ring                  - a robe of raven's feathers

Right Finger    a basalt ring                  - a robe of raven's feathers

Neck 1          an onyx necklace of demons     - a robe of raven's feathers

Neck 2          an onyx necklace of demons     - a robe of raven's feathers

Body            an octiron cuirass             - a robe of raven's feathers

Head            a wolf head hat                - a robe of raven's feathers

Legs            a pair of pitch black greaves  - a robe of raven's feathers

Feet            a pair of dolphin skin boots   - a robe of raven's feathers

Hands           a set of emerald gauntlets     - a robe of raven's feathers

Arms            flowing sleeves of the wind    - a robe of raven's feathers

Waist           Sash of Swirling Colors        - a robe of raven's feathers

Left Wrist      a band of ether                - a robe of raven's feathers

Right Wrist     ribbons of the vernal equinox  - a robe of raven's feathers

Wielded         hidden mace of the underworld  - a robe of raven's feathers

   Clasp        a repulsive yellow eye         - a robe of raven's feathers

Held            a moss-covered pebble          - a robe of raven's feathers

Here is what happens after rent:

Equipment Set 'regen':

Position        Item                            Container

Light           a philosopher's stone          - a robe of raven's feathers

Left Finger     a basalt ring                  - a robe of raven's feathers

Right Finger    a basalt ring                  - a robe of raven's feathers

Neck 1          an onyx necklace of demons     - a robe of raven's feathers

Neck 2          an onyx necklace of demons     - a robe of raven's feathers

Body            an octiron cuirass             - a robe of raven's feathers

Head            a wolf head hat                - a robe of raven's feathers

Legs            a pair of pitch black greaves  - a robe of raven's feathers

Feet            a pair of dolphin skin boots   - a robe of raven's feathers

Hands           a set of emerald gauntlets     - a robe of raven's feathers

Arms            flowing sleeves of the wind    - a robe of raven's feathers

Waist           Sash of Swirling Colors        - a robe of raven's feathers

Left Wrist      a band of ether                - a robe of raven's feathers

Right Wrist     ribbons of the vernal equinox  - a robe of raven's feathers

Wielded         hidden mace of the underworld  - a robe of raven's feathers

   Clasp        a repulsive yellow eye          [ Inventory ]

Held            a moss-covered pebble           [ Inventory ]

</div>

<div class="post" data-post-id="36607" data-author="*teker*" data-date="2016-02-17T15:39:32+00:00" data-subject="Re: Equipment sets">

Ok, I've figured out the container issue and committed a fix.  I'm hoping we'll reboot tomorrow to get all these fixes in place.

</div>

<div class="post" data-post-id="36610" data-author="Teron" data-date="2016-02-18T04:18:33+00:00" data-subject="Re: Equipment sets">

May I suggest Teker to internally use the wear a b c and rem a b c command, so that we don't rem/wear individual items, but first rem items in 1-2 sweeps, put them away, then wear other items in 1-2 uses of the wear command, rather than 18.

This will reduce the lag for those, who don't have second wind.

Of course, an alternate solution is to remove the lag from using these commands altogether, but I have no idea how it works, so.

</div>

<div class="post" data-post-id="36612" data-author="Ker" data-date="2016-02-18T15:33:09+00:00" data-subject="Re: Equipment sets">

Good day,

Err where did Splork's post go? :-)

We had an issue with choppers being transferred around in robes without assigned value.

Not sure if intended or not but putting it here.

Regards,

Dr

</div>

<div class="post" data-post-id="36615" data-author="*Splork*" data-date="2016-02-18T18:18:29+00:00" data-subject="Re: Equipment sets">

I deleted my post and sent an email instead 8) 

However, eqset should have the same amount of lag as a player using their client to switch all of their eq!

</div>

<div class="post" data-post-id="36616" data-author="Ker" data-date="2016-02-18T20:30:17+00:00" data-subject="Re: Equipment sets">

Good day,

So it seems! For a second I thought warriors would face the axe - S

Choppers moving around in containers from switching seemed long lost since the reboot -

And best news, EQset seems to be working again!

Yay,

Dr

</div>

<div class="post" data-post-id="36617" data-author="Teron" data-date="2016-02-18T23:56:32+00:00" data-subject="Re: Equipment sets">

Splork, that's the point: to have the same lag as with a regular switching alias.

When I change my eq, I use only 4 commands to change eq itself, here's an example:

rem wind-symbol hat devilskin cloak guards greaves

rem cross cross cuirass walls dark-bracer loop relic

get pail sack

get ring-ap sack

get ring-ap sack

get skulls sack

get all pail

wear eye-undead thorns amber ankh ankh skulls

wear ring-ap ring-ap shawl demise opalescent opalescent pail

The lag from these rem/wear commands is pretty small, compared to 36 similar commands, 9 times more the usual.

Even when I use wear all in another alias, it doesn't give me a 4 second lag, a 500ms lag at best.

Thanks.

</div>

<div class="post" data-post-id="36619" data-author="Josiah" data-date="2016-02-19T14:56:54+00:00" data-subject="Re: Equipment sets">

Taron (and others) use a clever workaround to game the system and change eq faster than intended.  He wants the lag from eqset to be based on the optimal equipment change method rather than the obvious one.

Cutting out the word 'all' and using two remove and wear commands shaves off about 5 seconds of lag.

</div>

<div class="post" data-post-id="36620" data-author="*teker*" data-date="2016-02-19T16:45:10+00:00" data-subject="Re: Equipment sets">

I will run some tests to compare the lag.

I've added documentation for EQSET DEPOSIT and EQSET WITHDRAW which work with the new vaults.  I need to work on WITHDRAW a little - the items are coming out correct but they're being left in inventory rather than placed into their proper containers.

I'm also starting to test the code on shapeshifted characters.

</div>

<div class="post" data-post-id="36621" data-author="*Splork*" data-date="2016-02-19T17:31:21+00:00" data-subject="Re: Equipment sets">

I am not so sure I would call it a work around because it was added intentionally on November of 2007.

Here is the write-up regarding the changes:

**Added wait state  to remove all/wear all dependent on what you wear and remove (some will hate this!)

Severly lowered the wait state on wear/remove single items (some will love this!)

Basically this is much fairer**

We will let Teker decide what to do :mrgreen: but its definitely a Slothy feature, as JB likes to say!

</div>

<div class="post" data-post-id="36622" data-author="*teker*" data-date="2016-02-19T18:05:40+00:00" data-subject="Re: Equipment sets">

I'll make the lag more consistent with "wear many" + "remove many".  I'm not seeing any issues with shifted players using eqset so I will enable that also.  These both require a new build so you'll see the changes then.

</div>

<div class="post" data-post-id="36624" data-author="Teron" data-date="2016-02-21T01:06:49+00:00" data-subject="Re: Equipment sets">

Well, it's certainly faster to use wear/rem commands, if I only need to remove 10 items, not 18.

So you are using that

wear ring ring cloak guards

will now lag 4 times as much?

And that the 4-5 second lag on eqs switch of a complete set is normal? I did use the "wear all" command in my regen alias and it never lagged as much, maybe gave me a regular round-long lag (about 1-1.5 seconds).

</div>
