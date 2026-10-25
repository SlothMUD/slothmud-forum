---
title: "Prompt"
topic_id: 3454
author: "Kelven"
date: 2010-06-24T12:24:05+00:00
last_activity: 2010-06-25T08:43:25+00:00
last_author: "Thraxas"
sticky: false
locked: false
post_count: 2
---

<div class="post" data-post-id="31328" data-author="Kelven" data-date="2010-06-24T12:24:05+00:00" data-subject="Prompt">

I have two questions concerning prompts. Firstly...

Is there a way to add color to your prompt? I've read 'help prompt' and 'help color', unfortunately the codes in 'help color' don't work in prompts.

I pretty much want to change the default prompt from: <$hhp $mma $vmv>

to something along the lines of:

<$h/$Hhp $m/$Mma $v/$Vmv>

And secondly...

Is it possible to add another prompt function that will display my current target's condition? (ie: what you see when you "look" at it while fighting so you have a general idea of what it's hps are, "Dying", "Bleeding" "Perfect Condition" etc...)

</div>

<div class="post" data-post-id="31329" data-author="Thraxas" data-date="2010-06-25T08:43:25+00:00" data-subject="Re: Prompt">

> **Kelven wrote:**
> I have two questions concerning prompts. Firstly...
> 
> 
> 
> Is there a way to add color to your prompt? I've read 'help prompt' and 'help color', unfortunately the codes in 'help color' don't work in prompts.
> 
> 
> 
> I pretty much want to change the default prompt from: <$hhp $mma $vmv>
> 
> 
> 
> to something along the lines of:
> 
> 
> 
> <$h/$Hhp $m/$Mma $v/$Vmv>

Yes it is possible but I can only do with a client.

Using zmud if your prompt is like:

<174hp 76ma 229mv>

then tiggering

^<%1hp %2ma %3mv>$

to

#GAG

#SAY {%ansi( 7)MYPROMPT:%ansi( 6)%1hp %ansi( 5)%2ma %ansi( 4)%3mv}

works well where the 7 6 5 and 4 are the colour definitions, this also opens up the possibility to code the colors with conditional logic

e.g.

#GAG

#if {%1 >100} {#VA hpcolor 6} {#VA hpcolor 7}

#SAY {%ansi( 7)MYPROMPT:%ansi( @hpcolor)%1hp %ansi( 5)%2ma %ansi( 4)%3mv}

I would however advise against this as it seems an unneccessary overhead to your processing (GAG isnt efficient in zmud) and could impact client performance particularly in fast spamming group situations.

As an alternative you might want to consider picking up mxpvariables (in zmud %mud.currentmana etc.) and putting into a status window or status bar so they update automatically on prompt and putting ansi code against this, this is far more efficient as the main problem with the above approach is the frequent use of the GAG.

*As an aside this use of status windows can be extended further to include all spell statuses (spell up/down spell time up / expected life etc.) this if done right can augment the sc(ore) command nicely, I also use to show current tank condition in groups ... I gag all autoreporting by the group tank and use to update a single line in the status window this reduces group spam a lot.*

I can help with wintin or similar translations if needed

> **Kelven wrote:**
> And secondly...
> 
> 
> 
> Is it possible to add another prompt function that will display my current target's condition? (ie: what you see when you "look" at it while fighting so you have a general idea of what it's hps are, "Dying", "Bleeding" "Perfect Condition" etc...)

This would remove the need to look mob to see condition i.e. deskilling the game something I wouldnt necessarily agree with, and would include complications such as what do you do if you're engaged against 5 mobs simultaneously which gets reported and what does it show if you're not engaged against a mob.

Thraxas

</div>
