---
title: "Con +Mob Health"
topic_id: 818
author: "Terin"
date: 2005-02-08T19:04:26+00:00
last_activity: 2005-02-09T12:38:16+00:00
last_author: "Calim"
sticky: false
locked: false
post_count: 6
---

<div class="post" data-post-id="4224" data-author="Terin" data-date="2005-02-08T19:04:26+00:00">

So im fighting something and wanna quickly check the health of the mob.  To my understanding the only way to do this is by Looking at them.  Of course when you do this its kind of hard to see the mobs health with all the battle text going on, and on my client at least the text color blends in.

My suggestion is to also add health to the Consider command.  This would make it a appear as follows:

con servant

You would need some luck!

A servant of Blaster is in excellent condition.

Hope you guys like the idea, and I'll look forward to reading the replies.  ^_^

</div>

<div class="post" data-post-id="4225" data-author="Leaf" data-date="2005-02-09T00:01:06+00:00">

Alot of ppl's clients use scripts to read their "health" and then report a %.

Here is what I use:

/alias {woundtellon} {woundtellon1;woundtellon2;woundtellon3;woundtellon4;woundtellon5;woundtellon6}

/alias {woundtellon1} {/action {^%0 has a few scratches.} {gt $0:SCRATCHES--->1%-10% RIP}}

/alias {woundtellon2} {/action {^%0 has some small wounds and bruises.} {gt $0:SMALL WOUNDS AND BRUISES--->11%-25% RIP}}

/alias {woundtellon3} {/action {^%0 has quite a few wounds.} {gt $0:QUITE A FEW WOUNDS--->26%-50% RIP}}

/alias {woundtellon4} {/action {^%0 has some big nasty wounds and scratches.} {gt $0:BIG NASTY--->51%-70% RIP}}

/alias {woundtellon5} {/action {^%0 looks pretty hurt.} {gt $0:PRETTY HURT--->71%-85% RIP}}

/alias {woundtellon6} {/action {^%0 is in an awful condition.} {gt $0:AWFUL--->86%-99% RIP}}

/alias {woundtelloff} 

I know this is a crappy script, and prob a better one out there.  But this 

was created about 8yrs ago, and I never changed it.  If it an't broke, why

fix it?!

</div>

<div class="post" data-post-id="4226" data-author="Terin" data-date="2005-02-09T01:28:52+00:00">

Could you tell me how to set up this script?

</div>

<div class="post" data-post-id="4234" data-author="Calim" data-date="2005-02-09T12:29:21+00:00">

A different idea, add a new command, 'Assess' that just returns the last line of the look regarding the mobs condition.

besides, then we can all type a-s-s 'mobname' :)

</div>

<div class="post" data-post-id="4235" data-author="12345" data-date="2005-02-09T12:32:37+00:00">

I'll laugh my ass off when everyone starts assisting mobs.  :lol:

</div>

<div class="post" data-post-id="4237" data-author="Calim" data-date="2005-02-09T12:38:16+00:00">

shh, that was the point... :)

</div>
