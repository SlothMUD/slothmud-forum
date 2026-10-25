---
title: "Changelog 2018-02-12"
topic_id: 4832
author: "*teker*"
date: 2018-02-12T18:01:33+00:00
last_activity: 2018-02-15T23:03:30+00:00
last_author: "*teker*"
sticky: false
locked: false
post_count: 3
---

<div class="post" data-post-id="38666" data-author="*teker*" data-date="2018-02-12T18:01:33+00:00" data-subject="Changelog 2018-02-12">

Added EQSET SETINVENTORY and EQSET REMOVEINVENTORY to allow players to specify items that will always return to inventory when unequipped.  HELP EQSET has been updated.

I've been going through the bug list and working on fixing a bunch of the small nagging items:

583)  Sun Mar  6 09:47:09 2016  Dr  7012

    guards in poseidon temple that has cache become unpushable, without cache they are pushable

584)  Sun Mar  6 09:47:47 2016  Dr  7012

    echo message on the guards with cache shows that they improved on levels : You seem to annoy etc when trying to push high levels as per norm

This is by design to prevent players from cache access via push.

662)  Sun Mar 27 10:48:32 2016  Taron  38814

    dreamtalk prioritizes mobs if keyword matches a part of the player's name (surf)

1093)  Tue Feb 14 16:04:10 2017  Zuzu  8002

    dreamtalk will not accept an abbreviated name, yet.

1292)  Thu Jul 27 20:54:20 2017  Zuzu  76012

    dream talk will not take an abbreviated name for a target

1382)  Sun Oct 22 18:33:59 2017  Zuzu  10303

    you can abbreviate a player name for Tell but you cannot abbreviate a player name for Dream Talk, you are forced to fully spell it out, which is annoying

Spell rewritten - issue should be resolved.  Also prevented it from allowing a blank message to be sent.

798)  Fri Jul  8 11:21:26 2016  Taron  37281

    when I'm in a room with a peri, when I spy in a nearby room, it shows the same peri in that room

Fixed.

843)  Thu Aug 25 23:13:08 2016  Taron  48206

    there are way too many caches on solid rakashas in hellwell, compared to other areas, and it isn't that convenient or practical

Cache percentage (in general) was previously lowered.

665)  Mon Mar 28 01:40:41 2016  Taron  48131

    a kangaroo pouch is unapproved

776)  Wed Jun 22 11:21:11 2016  Sadnama  42283

    description of Papa Bear at Forest of Grimm reads   put your image here.

837)  Wed Aug 17 07:05:42 2016  Norks  30304

    potion of good intentions bugged. no change to alignment and gives Alchemical effect, NONE in score

845)  Sat Aug 27 07:58:58 2016  Vege  49059

    quaffed a goblet which didnt give any effect

All appear to have been previously fixed.

702)  Thu May 12 10:23:38 2016  Taron  70132

    please fix mantra of the ancient tribes (it says 3 shards isn't enough for a healing devak) or update the helpfile accordingly

1017)  Mon Dec 26 07:04:39 2016  Lerr  12034

    "The potential for plunder has reached an epiphany." is not explained under help extras

1050)  Thu Jan 12 15:45:11 2017  Felis  34250

    Cost for w

1051)  Thu Jan 12 15:45:43 2017  Felis  34250

    mana cost for Water Breathing skill is listed as "v" in the help file

Help files updated.

949)  Sun Nov 20 22:03:47 2016  Knubberub  37235

    blind needs a fail message. please, after 25 years

Done.

974)  Mon Dec  5 07:54:12 2016  Taron  58111

    I used hermetic resonance against firewind, I got 6 firewinds cast at me, and I resonanted 0 (zero). Increase successrate if no bugs present.

Previously updated some mobile procs to account for resonance.

1003)  Sat Dec 17 06:47:54 2016  Aowey  19026

    I am stuck with -4 HP but refuse to die. it's more than 5 minutes now... is that a bug or a feature? :) I was smashed to pieces by a tigress in heat, in

HINT now shown for newbies to let them know they can quit! out to die faster.

1028)  Sun Jan  1 21:05:13 2017  Zuzu  7012

    is there a compelling reason why menas would be relocatable and not delesor, seeing as delesor is the primary thalassas innkeep

1108)  Mon Feb 27 12:26:21 2017  Zuzu  7012

    reassess whether Delesor should be not gateable while other island innkeepers are?

1109)  Mon Feb 27 12:27:24 2017  Zuzu  7012

    disregard that. no one would walk overland to Thal if we did it.

1204)  Sat May 27 21:05:22 2017  Zuzu  31001

    gating thal-innkeeper succeeds yet gating Delesor always fails

Delesor is not the thal-innkeeper.  "The Receptionist" is the thal-innkeeper in the same room as Delesor and is gateable.

1140)  Sun Mar 26 12:21:58 2017  Taron  48175

    being silenced by a spell proc isn't shown in score affects2

1141)  Sun Mar 26 12:22:17 2017  Taron  48175

    being silenced isnt shown in score, too, actually

Updated score to show this.

1148)  Thu Apr  6 06:42:29 2017  Taron  72051

    lot's of "Ok." when eqs wear set

Pretty sure this no longer happens.

1182)  Thu Apr 27 10:05:53 2017  Taron  58045

    spells from potions, eg wraithform, are not saved through rent

Pretty sure they are saved through rent but not through corpsing.

1201)  Tue May 23 07:41:07 2017  Songster  98285

    the spirit watcher is broken. I was sitting at zeus, with a watcher, and watcher didnt warn me of repop. Only global extra on was fargate

Watcher zone reset check was previously rewritten - please file new bugs with examples if there are still issues.

1208)  Fri Jun  2 07:34:09 2017  Taron  58050

    rem ankh all.onyx flux doesn't work for "all.onyx"

Updated remove command to allow for this.

1304)  Sat Aug  5 16:57:43 2017  Zuzu  98263

    replay says it doesn't understand 'grouptell' in the context of replaying but it understands other channels

Previously "gtell" was the keyword.  Both "gtell" and "grouptell" work now.

1309)  Mon Aug  7 18:46:10 2017  Zuzu  10303

    when you water breath someone else, you don't really get a 'success' message saying "Kathrynn now feels new horizons..." no message at all

Added message.  Shows in mass water also.

1310)  Tue Aug  8 20:10:03 2017  Belrath  8180

    kangaroo pouch fail when quaffed straight from pouch: goodness, goblet, comradery

Previously fixed.

1334)  Wed Sep  6 12:44:04 2017  Slice  30431

    a potion of wispy prayers "Apply a bonus of 2 to the drinker's MAX_INT for 45 hours.", it does not, it increases INT by 2, but not above a chars MAX_INT.

I think this is confusion about what MAX_INT means.  MAX_INT should really be thought of as BONUS_INT where the natural cap is 18.  A player's maximum INT value is determined by class order and level.

1340)  Tue Sep 12 06:54:00 2017  Taron  10303

    crashbug: 1) make a familiar out of a simulacrum 2) reconnect from another pc 3) ... 4) crash!

1370)  Thu Oct  5 06:25:43 2017  Taron  10311

    1) use simulacrum as a familiar 2) lose link 3) log in twice 4) rent 5) crash

1371)  Sat Oct  7 09:02:30 2017  Taron  89378

    about the bug that crashed the game last time, I absent-mindedly rented in the same manner after crash, and it didn't crash.

Changes made a couple weeks ago - haven't seen this crash since.

1356)  Sun Sep 24 17:38:52 2017  Gu  6423

    there are times when a mob clambers back on its feet but it doesnt tell you it did

1357)  Sun Sep 24 17:50:00 2017  Gu  6415

    (reference to earlier) we know it's not telling us they clambered on their feet because theyre capable of being bashed again.

I made some changes to try to reduce/eliminate this.

1389)  Sat Oct 28 15:02:34 2017  Pit  4688

    the leaders autoloot should NOT be turned off at group formation. getting fkcing irritated of XXXXX saying "hey no ones looting" after i form up

Doesn't seem to happen to me when I am group leader.

1407)  Sat Nov 11 23:16:10 2017  Zuzu  39771

    that is REALLY annoying that you have to specify your name each time you Darkness self

Darkness now defaults to self.

1420)  Fri Nov 24 11:34:27 2017  Tau  48129

    If Dark Mace disintigrates while you are asleep, you don't see the message about it going away.

Previously fixed.

1432)  Sat Nov 25 22:15:31 2017  Zuzu  89312

    the play social said something about bard songs. rather than letting me play in the dirt with Mage

1433)  Sat Nov 25 22:16:54 2017  Zuzu  89312

    in other words instead of executing the play social play <PC name> says but you arent wielding an instrument

1434)  Sat Nov 25 22:17:31 2017  Zuzu  89312

    in consequence i can't play around in the dirt with Mage, which makes me Sad.

Fixed.  Except playing with another person involves leapfrog rather than playing in dirt.

1506)  Wed Dec 27 21:00:00 2017  Zuzu  8000

    at this time, it says i can read the wraithform book on janatra's list but clearly that's necro prime only

I believe this has been fixed.

1528)  Sun Jan  7 17:34:13 2018  Zuzu  13261

    and you cant bugs while you're paralyzed

Modified paralyze to allow some extra info-based commands.

1551)  Wed Jan 17 05:35:05 2018  Taron  58053

    close gate tries to close the gate guard first, the gate second

I have modified open/close/lock/unlock to ignore subdued creatures (I believe that's what the issue was here).  If it matches a subdued creature it will ignore that match and look for a door in the room instead.

1579)  Sun Jan 28 10:52:37 2018  Arya  99267

    warcry with no arguments is blocked from being used during a fight, but why, if it's only informational in that form?

Updated.

>> Player counters update when looting gold from player corpse.

This is fixed.  I also fixed SACRIFICE #.CORPSE to work.

>> Create food shows no message if the caster is invis but does not have detect invis up.

Fixed.

</div>

<div class="post" data-post-id="38667" data-author="*teker*" data-date="2018-02-14T17:05:21+00:00" data-subject="Re: Changelog 2018-02-12">

I wasn't expecting a reboot today but here's what made it in:

162)  Mon May  4 07:31:48 2015  Taron  89377

    make The Evening Star require a green ticket or change Seagull to require the golden one .)

Previously fixed.  Both boats from Lyme to the Island now require a green ticket.

191)  Sun May 10 13:02:07 2015  Taron  70240

    open hatch doesnt show anything, open trapdoor doesnt show anything in athenaeum

Fixed.  These are SILENT exits so only the player performing the action will see a message.

216)  Tue May 19 22:26:52 2015  Curate  47046

    the healbonus.. if any.. from my dark mace does not seem to show in score all2

Previously fixed.

251)  Thu Jun 18 22:13:15 2015  Zuzu  43044

    you cannot see follower rankings at Enea's tablet

252)  Thu Jun 18 22:13:27 2015  Zuzu  43044

    neither can you list to see what holy items to pray for at Enea's tablet

1046)  Mon Jan  9 14:59:11 2017  Knifey  10550

    This temple (Alana) seems to be the only one I've found so far that saying recall won't recall you at. Just a heads up.

I placed a tablet at Enea's altar with follower list.  Holy item list available via "list" or HELP HOLY.  SAY RECALL should work now at all temple altars.

282)  Fri Jul 24 22:56:03 2015  Orphe  30993

    dance with dead not in the spell list for bards

Shows up under SKILLS BARD.

319)  Wed Aug 26 09:29:58 2015  Fluffy  89312

    You feel burning poison in your blood, and suffer. - message not displaying while sleeping. Just lowering hps without reason

Previously fixed.

334)  Wed Sep 23 17:16:37 2015  Cyprimus  78038

    when i entred room, statue was already wounded... no apparent cause...

Likely a side-effect of fortune spell.  Previously fixed not to hurt mobs.

338)  Tue Sep 29 09:28:15 2015  Toxis  33408

    can't cast demonic aura on toxis, -10 align "too righteous"?

This message displayed when target was affected by bless.  Rewrote messages for spell conflicts on demonic and unholy aura.

377)  Tue Nov  3 09:06:49 2015  Taron  55307

    im fighting remoras and then this msg appears after banshees wail at them: the wailobj_ban object falls to the ground. I'll send log to splork+neptune

Fixed.  Hidden mudl objects no longer fall into rooms below.

384)  Fri Nov  6 10:52:25 2015  Kirei  34287

    when ask erdogan(valk quester) about something, he outputs his back messages twice

Previously fixed.

410)  Fri Dec  4 09:49:44 2015  Taron  98018

    a watcher doesnt detect morgana repop for some reason. when i walk in there, it can see her or me

Previously fixed.

424)  Sun Dec 13 08:25:05 2015  Songster  69982

    cant create a charm of cry of the avatars, says i dont know the spell

Can only create charms of spells, not songs.

468)  Mon Jan 11 12:22:07 2016  Taron  73520

    cant thwap in fight

Now allowed during combat.

477)  Fri Jan 15 14:01:45 2016  Taron  73296

    argosian quartermaster: Taron buries his claws deep within your chest freezing your soul!!

478)  Fri Jan 15 14:02:57 2016  Taron  73295

    argosian quartermaster: Taron buries his claws deep within your chest freezing your soul!! (sorry if double)

Fixed.

581)  Fri Mar  4 06:16:15 2016  Taron  71060

    can't summon or gate familiars

Fixed previously.

933)  Fri Nov 11 00:40:12 2016  Taron  89312

    when a mob has an eq worn and a cache, the watcher tells me about the cache, not that something is worn. I'd rather know of a pop, than a cache.

Fixed.  Will now notify about both.

1006)  Tue Dec 20 19:55:46 2016  Fluffy  89312

    i typing get food sack. and it trying to get that food from bag of persephone, despite the fact that bag dont have keyword sack

Fixed.  I rewrote the mudl proc from scratch - let me know if there are issues.

1189)  Tue May  2 11:56:59 2017  Zuzu  58058

    add keyword "fire" to blazing longsword of fire please so it doesnt conflict with blazing sword of maul titans (chopper)

Fixed.

1278)  Thu Jul 20 00:27:41 2017  Taron  19495

    cant deposit 2.girdle to vault

Fixed.

1594)  Thu Feb  1 22:24:43 2018  Arya  25525

    i can't bounce around while i am fighting. it makes me Sad.

Now allowed while resting or fighting.

1604)  Sun Feb  4 12:41:58 2018  Sochi  40103

    strikes should not be gagged by gag fight, they are special attacks, and we need to see them

Fixed.

</div>

<div class="post" data-post-id="38670" data-author="*teker*" data-date="2018-02-15T23:03:30+00:00" data-subject="Re: Changelog 2018-02-12">

I wasn't expecting a reboot today but you should notice a longer replay list and changes to reply/respond where they always send a tell back to the last person you heard from without specifying their name.  I'm going to fix the spirit watchers so that their tells show up in replay but there's a bug about auctioneers not showing up that I probably won't fix.  It seems to me that it'd totally overwrite the replay list every time someone buys or reclaims a bunch of tokens.

</div>
