---
title: "Some advice about small groups needed"
topic_id: 3582
author: "jess"
date: 2010-11-19T13:05:12+00:00
last_activity: 2010-11-20T06:40:20+00:00
last_author: "jezer"
sticky: false
locked: false
post_count: 9
---

<div class="post" data-post-id="32080" data-author="jess" data-date="2010-11-19T13:05:12+00:00">

When in a small group (2,3 man) should everyone use man back triggers?

I was point in a 2 man group with the other member in the back line. I often get the message 'Your front line collapses!  Your group is thrown into chaos!' usually followed by 'You can't fall back, you're being attacked!' so I stay on point. However sometimes the front line collapses completely and I lose point, end up in the back line with the other member in the front line being attacked.

Is there anything I can do to stop this and stay on point? Would it be better not to use man back triggers at all in small groups? If so what size group should they be used for? Should all members of a small group turn them off or only the one on point?

</div>

<div class="post" data-post-id="32081" data-author="blackmore" data-date="2010-11-19T14:09:08+00:00">

A first suggestion would be that you should never use a man back trigger if you're point.  Ever.

Otherwise, make it easy enough to turn off and on that you can make your own decision based on the group you're in.  A trigger does nothing but performs a function for you so you don't have to do it yourself.  If it's doing something you wouldn't want to be doing manually, then shut it off.

</div>

<div class="post" data-post-id="32082" data-author="Thraxas" data-date="2010-11-19T16:32:16+00:00">

You're on point and man back? why? 

Not sure if I'm missing something but are you manning back and sloth somehow allowing you to do so, or is sloth putting you in the back row automatically somehow? I didnt think either of these could happen especially the 2nd.

Surely everyone has a toggle on their man back scripts depending on whether they want to be in the front row or back?

T

</div>

<div class="post" data-post-id="32083" data-author="jess" data-date="2010-11-19T16:53:59+00:00">

I didn't think it would let me man back when I was on point as for a long time I always got the message 'You can't fall back, you're being attacked!'. So I left the man back triggers active. 

I can turn them off when I'm on point in future easily enough.

</div>

<div class="post" data-post-id="32084" data-author="jess" data-date="2010-11-19T16:57:18+00:00">

> **Quote:**
> Surely everyone has a toggle on their man back scripts depending on whether they want to be in the front row or back?

Hmm - no I don't! Not sure how to do this. Do you mean to have it automatically do man up after a man back if you want to be in the front row?

</div>

<div class="post" data-post-id="32085" data-author="element" data-date="2010-11-19T17:57:10+00:00">

if you wanna stay on front row, just don't man back at all?

</div>

<div class="post" data-post-id="32086" data-author="Teron" data-date="2010-11-19T21:15:29+00:00">

The following works for ZMud, but should work for Wintin or other graphical MUD clients.

Instead of "man back" in your command for your man back trigger, enter this:

```
#IF {@tank<>@char} {man back}
```

You'd have to set the char and tank variables (case-sensitive, most likely) to the current point, though, to keep this working right (that's how I do it, since I use the tank variable with pets).

This alias works a treat:

```
#al tank #var tank %1
```

E.g.: tank Katie would set Katie as the tank.

(a cooler variant would be to grab the name of the (Point), but I set this variable manually ;) )

Another way to do it is this:

Man back trigger command:

```
#IF {@mback=1} {man back}
```

Toggle alias:

```
#al mback '#IF {@mback=1} {#var mback 0} {#var mback 1}'
```

```
#al tank '#var tank %1;mback=0', if you use the latter variant for some weird reason.
```

</div>

<div class="post" data-post-id="32087" data-author="jess" data-date="2010-11-19T22:26:59+00:00">

Thanks Teron that's very useful useful information.

</div>

<div class="post" data-post-id="32092" data-author="jezer" data-date="2010-11-20T06:40:20+00:00">

I tried reading this post but lost concentration so I decided to read another post but stumbled. A lump of coal appeared in my hands, which really did hurt... but now I'm lying here still cause I'm dead... so I actually read the post. I really liked the ending - so I decided to rent and the innkeeper smiled and took all my gold... oh well. See ya on the flip side.

</div>
