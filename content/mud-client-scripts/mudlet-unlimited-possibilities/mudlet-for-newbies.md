---
title: "Mudlet for newbies?"
topic_id: 4598
author: "Madigan"
date: 2016-02-26T22:03:32+00:00
last_activity: 2016-10-25T17:57:58+00:00
last_author: "Teron"
sticky: false
locked: false
post_count: 16
---

<div class="post" data-post-id="36648" data-author="Madigan" data-date="2016-02-26T22:03:32+00:00">

Posted this in the wrong forum but got quite a bit of response from people that seemed to be in the same boat as me as a zmud/cmud user for many years that wants desperately to try and migrate to mudlet, so reposting here in hopes to get some assistance.

---------------------------------------------------------

I know sochi, linx, and and several others (especially akayan) are guru's of the  mudlet client... I've been asking around for someone to share a basic mudlet config to no avail, but I wonder if we could convince them to maybe host a 30 minute -1 hour websession (i have hosting capabilities if needed) on Mudlet 101 with the following agenda:

1) basic client install including required addons (vysor, etc) - very little documentation online for this, but what does exist is out of date and does NOT work as documented.

2) brief overview of basic scripting for aliases/triggers etc. (i have looked at the online videos of this and have a very basic understanding of it) Would be nice to get some useful feedback using examples specific to sloth that we use daily.

3) configuration of core features/scripts (ie targeter, xp tracker, paths, chat captures to window, group necesities etc)

I would volunteer to document the discussion and post it to the forums for future reference.

I have played around with just getting the basic config up and running using some of the link breeze posted a while back but his versions are outdated and I'd prefer not to have a UI with a ton of unused background graphics, but more of core/basic functions like i noted in step 3 on the agenda.

Would anyone be willing to assist your other Slothers in joining the 21st century and getting on boards with mudlet?

Blix

</div>

<div class="post" data-post-id="36655" data-author="Madigan" data-date="2016-02-27T08:57:55+00:00">

[<LINK_TEXT text="http://www.aardwolf.com/wiki/index.php/ ... ardwolfGUI">http://www.aardwolf.com/wiki/index.php/Clients/MudletAardwolfGUI</LINK_TEXT>](http://www.aardwolf.com/wiki/index.php/Clients/MudletAardwolfGUI)

or something like that would be tits :) but it's wayyy overkill.

</div>

<div class="post" data-post-id="36656" data-author="*juggleblood*" data-date="2016-02-27T14:18:02+00:00">

I don't have enough confidence to post thorough tutorials, but for anyone who has seen it, please check out the directory of mudlet scripts for slothmud at [www.slothmud.org/mudlet](http://www.slothmud.org/mudlet).

</div>

<div class="post" data-post-id="36657" data-author="Madigan" data-date="2016-02-27T17:18:00+00:00">

seen it. there is an outdated vysor mpackager and 2 working ui's but the only really helpful thing there is a chat window capturer. pasting a full screen .jpg behind my mud window is of no use.

I can't get the mudlettxt layout to work, it looks like it might be the most helpful.

Come on folks, share your knowledge. Why spend all that time perfecting your scripts if you can't show it off by helping others ;)

</div>

<div class="post" data-post-id="36658" data-author="*Breeze*" data-date="2016-02-27T17:44:50+00:00">

was an experiment 

[http://www.slothmud.org/mudlet-tools/](http://www.slothmud.org/mudlet-tools/)

ymmv

</div>

<div class="post" data-post-id="36659" data-author="*juggleblood*" data-date="2016-02-28T00:16:22+00:00">

That is pretty slick.

</div>

<div class="post" data-post-id="36660" data-author="Madigan" data-date="2016-02-28T05:47:06+00:00">

THIS IS SLICK! Amazing work Breeze. VERY Thankful. This hits 75% of my needs. If it all worked.

I will update this post as I find issues or resolve them

Here are issues I have found:

1) Must use Mudlet 3 beta. I'm using delta release now. The 2.1 version I had did not have an MSDP enable feature in options.

</div>

<div class="post" data-post-id="36661" data-author="*Breeze*" data-date="2016-02-28T07:36:26+00:00">

yeah was made for delta. 

it's a template system. I can share details later if anyone wants to contribute or tweak the scripts. 

basically how I run my mortals with the exception of my aliases and triggers. 

somewhere I also have code to generate aliases easier. 

something like

#ac rr %1;recite recall %1

#ac rr;recite recall 

generates the aliases for rr $1 and rr and outputs to a file you load into mudlet.

</div>

<div class="post" data-post-id="36665" data-author="*juggleblood*" data-date="2016-02-28T20:04:48+00:00">

Wintin refugees rejoice!

</div>

<div class="post" data-post-id="36666" data-author="Teron" data-date="2016-02-29T07:04:09+00:00">

Oh, hey, Breeze, writing the aliases on the fly is what prevented me from switching anywhere.

Can you create a script, where you

- type in a name of an alias, say, ws

- press tab

- the script outputs the alias in the command prompt: wake;stand

- you can rewrite the alias on the fly?

If you do, I'll play around w/ switching to Mudlet, which is a very promising client.

Then again, there are triggers, which are a completely foreign beast to me on Mudlet.

Thanks.

</div>

<div class="post" data-post-id="36670" data-author="*juggleblood*" data-date="2016-02-29T15:20:53+00:00">

I wouldn't bother to switch unless you are committed to learning regex. 

The hack described above is pretty weak compared to taking full advantage of mudlet's features.

</div>

<div class="post" data-post-id="36675" data-author="Madigan" data-date="2016-02-29T22:44:58+00:00">

> **Teron wrote:**
> Oh, hey, Breeze, writing the aliases on the fly is what prevented me from switching anywhere.
> 
> 
> 
> Can you create a script, where you
> 
> - type in a name of an alias, say, ws
> 
> - press tab
> 
> - the script outputs the alias in the command prompt: wake;stand
> 
> - you can rewrite the alias on the fly?
> 
> 
> 
> If you do, I'll play around w/ switching to Mudlet, which is a very promising client.
> 
> 
> 
> Then again, there are triggers, which are a completely foreign beast to me on Mudlet.
> 
> 
> 
> Thanks.

After using Breeze's little jumpstart tool I spent 1 day with zmud up on one monitor and mudlet on the other and copy pasted all my others aliases and triggers and am very happy so far. This really helped me understand the difference in regex and cmud/zmud coding... there is basically an example of most of the things I needed to see and compare to make sense of it all.

The chat logging solution I found and adapted is SUPERB, I'll find a way to share it with this forum. Linx's affects window is SUPER. I'm needing to work ok a group status window and a window that shows current target and others MSDP settings like gleader, gtank etc just so it's visual at all times to me.

I ran a couple groups yesterday and I can tell it for me, its MUCH faster... like ALOT faster. So far I'm very happy.

</div>

<div class="post" data-post-id="36686" data-author="*Breeze*" data-date="2016-03-01T18:19:56+00:00">

that was its intended purpose :)

</div>

<div class="post" data-post-id="37017" data-author="Akaya" data-date="2016-07-01T07:08:52+00:00">

I'd be happy to post a Mudlet 101 video on my YouTube channel specifically for Slothers if there is still an interest.

Give me a day or two and I'll have it together.

</div>

<div class="post" data-post-id="37022" data-author="celerra7" data-date="2016-07-01T17:48:47+00:00">

Most definitely!

</div>

<div class="post" data-post-id="37451" data-author="Teron" data-date="2016-10-25T17:57:58+00:00">

Akaya, if you have time, could you translate these [ZMud/CMUD tank triggers](http://www.slothmud.org/forum/viewtopic.php?f=16&t=4684&p=37450#p37450) to Mudlet?

Thanks.

</div>
