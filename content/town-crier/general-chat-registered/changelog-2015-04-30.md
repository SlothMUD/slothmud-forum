---
title: "Changelog 2015-04-30"
topic_id: 4479
author: "*teker*"
date: 2015-04-30T14:37:35+00:00
last_activity: 2015-05-30T15:58:36+00:00
last_author: "*teker*"
sticky: false
locked: false
post_count: 9
---

<div class="post" data-post-id="35873" data-author="*teker*" data-date="2015-04-30T14:37:35+00:00">

Prompts now support $f for fighting.  This will display the hit points of the mob you are fighting as a percentage 0-100.  It's currently coded to color the number opposite of normal player colors - that is green is good (mob < 20%) and red is bad (mob > 80%).  We've already had some discussion as to whether this is confusing or not.  Let us know how you feel.  I'm also curious if anyone plans on writing triggers for this - would it be better if we replaced the "0" while "not fighting" with a dash or something else.

The level command now displays a customized experience/gold table when used outside of guilds.  The table is color coded to show you which levels you currently have experience and/or gold for.  Again - green is good.  Yellow means you have the gold, but need to visit the bank.  Red means you've got work to do.  All prices include hometown discount.  We've already had a report that it's not showing anything for 8x40s - I'll take a look and get that fixed.

Previously unannounced but noticed by some - the query command now shows how many of each component you are carrying when you query about forges.  Same idea - green is good, yellow means you need to visit the bank or have the components stashed in a container somewhere.

We're continuing to do back-end work that isn't immediately visible.  There's a big effort to eliminate places in the code that could possibly buffer-overrun or corrupt memory and crash.  This is requiring thousands of changes throughout the code.  Please let us know if you see any garbage strings in your display and we'll try to track them down.  I think I've seen a couple reports in the last couple weeks - keep them coming in.

</div>

<div class="post" data-post-id="35874" data-author="Magi" data-date="2015-04-30T15:00:07+00:00">

Awesome additions!  Thanks teker.

And yeah, the opposite colors are going to be confusing, but i'll probably just swap them in my client.

</div>

<div class="post" data-post-id="35876" data-author="*juggleblood*" data-date="2015-04-30T15:04:48+00:00">

Really cool. What if it gave you current position (standing/sitting/resting/sleeping/fighting/reading/stunned/incap/morted) and then if you are fighting it also displays mob hit percentage? I was just thinking of what to display instead of 0 and it seemed like position might be nice.

Since you're tinkering with prompt, I'll mention that some druids might like to have room sector in prompt too.

</div>

<div class="post" data-post-id="35877" data-author="*teker*" data-date="2015-04-30T15:34:53+00:00">

If there's sufficient support for changing the colors or whatever else, we'll do it.  I'd like us to figure it out before too many people write custom triggers.

It looks like sector type is already available to all players as $S but it's documented as an immortal-only option.  If there's support to position of mob you re fighting, we can certainly do that, but I think it would be cleaner for scripting if it were a separate option.

I forgot to mention a couple other player reported bugs/ideas that should be fixed today - level 1 clan members can now use ktalk and level 10 players can now use the finger command.  Finger used to be level 11 but the error message said you needed to be 10.

</div>

<div class="post" data-post-id="35878" data-author="*Breeze*" data-date="2015-04-30T16:27:10+00:00">

I think not fighting should show a -  

After all, 0 != null

</div>

<div class="post" data-post-id="35879" data-author="*teker*" data-date="2015-04-30T16:29:25+00:00">

My bad on the $S option - looks like it is immortal only.  We'll talk about changing it.

</div>

<div class="post" data-post-id="35880" data-author="Yasik" data-date="2015-04-30T17:36:24+00:00">

I think "full mob -> green, dying mob -> red" is logical just as players HPs in the prompt, and we dont have to remember to flip to process the quickly incoming information correctly.

Dash instead of 0 seems better option than zero, because 0 hp is still not dead, we players die when reach -11hps; mobs are different, maybe, but still. If all is the same as in army, then less thinking, faster reactions - leads to better chances to stay alive.

</div>

<div class="post" data-post-id="35881" data-author="Unsub" data-date="2015-04-30T18:30:53+00:00">

Awesome stuff.  Thanks

</div>

<div class="post" data-post-id="35922" data-author="*teker*" data-date="2015-05-30T15:58:36+00:00">

The level command has been updated so that:

1) It doesn't interrupt studying/learning/teaching

2) You can't level gain while stunned or worse (presumably from fighting the guildmaster).

</div>
