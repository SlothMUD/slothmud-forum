---
title: "Does resist disease even work?"
topic_id: 4794
author: "Gorka"
date: 2017-10-17T08:43:26+00:00
last_activity: 2017-10-21T03:58:02+00:00
last_author: "Teron"
sticky: false
locked: false
post_count: 8
---

<div class="post" data-post-id="38446" data-author="Gorka" data-date="2017-10-17T08:43:26+00:00" data-subject="Does resist disease even work?">

I wear the emerald serpent brooch proudly, but there isn't a single run of infirmary where I don't come away with hack... and if I kill the administrator I know I will get gold fever. 

I have long suspected that mob procs don't take into account your character resist disease property. Would an immortal be interested in checking on the usefulness of this clasp, otherwise I will sell it for the drachma.

</div>

<div class="post" data-post-id="38447" data-author="Driven" data-date="2017-10-17T15:55:29+00:00" data-subject="Re: Does resist disease even work?">

FWIW, I noticed the same thing. I wore my emerald brooch for a while and it didn't seem to help at all.

</div>

<div class="post" data-post-id="38448" data-author="*Breeze*" data-date="2017-10-17T21:43:29+00:00" data-subject="Re: Does resist disease even work?">

If a mob proc 100% diseases you, no amount of resist disease helps.. 

Unless its coded to take that into account..

however if someone else is diseased it will help you not get diseased

</div>

<div class="post" data-post-id="38449" data-author="Gorka" data-date="2017-10-18T08:52:01+00:00" data-subject="Re: Does resist disease even work?">

Say Ezekiel has the clap, erm, I mean hack... and he's spreading it around the group, how long is he contagious? Is my resist disease clasp constantly fighting it off, or does it only do the check at the point he becomes infectious?

Basically, if +50 resist disease is 50% save, but I'm constantly having to save every check... I am still going to eventually loose and get diseased anyway... so how often is this check performed to stop me getting diseased?

I'm just trying to work out if I should blow away this clasp, it's not sounding very useful.

</div>

<div class="post" data-post-id="38450" data-author="*teker*" data-date="2017-10-18T16:31:14+00:00" data-subject="Re: Does resist disease even work?">

I've made changes to the infector proc to take RESIST\_DISEASE into account. Should go live at the next reboot.

General details:

\+50 = 50% resistance. They stack but not by straight addition. +50 combined with +10 results in 55% resistance. There is a cap below 100%.

Player versus player:

The disease code is actually pretty complicated. Someone went to a lot of thought and detail on it. There are different methods of propagation depending on the disease. Hack is an airborne virus so if the infected player is coughing or sneezing there's a chance that the disease will spread when that happens. Some diseases also can propagate without showing symptoms. The intervals between propagation checks vary by disease and is somewhat random. For hack, it's probably around once per minute. Every time the disease attempts to propagate, your RESIST\_DISEASE comes into play.

</div>

<div class="post" data-post-id="38451" data-author="Gorka" data-date="2017-10-18T18:47:50+00:00" data-subject="Re: Does resist disease even work?">

Thanks, interesting info as well. Who would have thought that sloth's disease and drunk system would be some of it's most interesting code... Maybe we've been playing this game wrong... instead of gossiping... only 50 drachma till next item! we should be like, hey guys had donkeyitius last night... and all the players be like "gratz." That's some serious slothing right there... er, ok, maybe not.

</div>

<div class="post" data-post-id="38452" data-author="*Breeze*" data-date="2017-10-19T15:35:12+00:00" data-subject="Re: Does resist disease even work?">

iirc disease code was fine by Judge. And yes.. it is complex. The only code sloth has that is more complex is astrology/houses.. it actually simulates a solar system with sloth at the center. It's insane the math that went into it.

</div>

<div class="post" data-post-id="38453" data-author="Teron" data-date="2017-10-21T03:58:02+00:00" data-subject="Re: Does resist disease even work?">

How does the talking mobs code compare to this in compelxity?

</div>
