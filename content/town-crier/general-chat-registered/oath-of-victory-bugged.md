---
title: "Oath of Victory Bugged?"
topic_id: 4755
author: "Gorka"
date: 2017-04-15T14:15:49+00:00
last_activity: 2017-04-21T20:08:34+00:00
last_author: "Josiah"
sticky: false
locked: false
post_count: 7
---

<div class="post" data-post-id="38215" data-author="Gorka" data-date="2017-04-15T14:15:49+00:00" data-subject="Oath of Victory Bugged?">

> <strong>Quote:</strong>
> \<1387hp 283ma 288mv 128205717xp -8.0ac 97%\>
> 
> You swear a mighty oath of victory over a large troll prisoner!
> 
> 
> 
> \<1551hp 284ma 289mv 128205717xp -8.0ac 97%\>
> 
> A large troll prisoner misses you with his beat.
> 
> A large troll prisoner misses you with his hit.
> 
> A large troll prisoner misses you with his beat.
> 
> A large troll prisoner misses you with his hit.
> 
> You brutally massacre a large troll prisoner with your hit.
> 
> You brutally massacre a large troll prisoner with your hit.
> 
> You brutally massacre a large troll prisoner with your hit.
> 
> You brutally massacre a large troll prisoner with your hit.
> 
> You brutally massacre a large troll prisoner with your hit.
> 
> You land a powerful strike into a large troll prisoner's side.
> 
> 
> 
> \<1348hp 284ma 289mv 128225455xp -8.0ac 75%\>

Can someone explain...

1\) How I lost more than the extra hp from Oath of Victory without being hit?

2\) Why Oath of Victory only appears to last for 1 round?

3\) Why MSDP.HEALTH doesn't update with Oath of Victory?

4\) Why if I get paralysed, I fulfill my Oath of Victory?

5\) Why the mob only has to be incap to fulfill my Oath of Victory not dead?

</div>

<div class="post" data-post-id="38216" data-author="Josiah" data-date="2017-04-15T20:33:48+00:00" data-subject="Re: Oath of Victory Bugged?">

1\) You did get hit, but it took away from your warcry temporary hp instead of your actual hp. Since it did zero damage to you, it displays as a miss.

2\) Oath of victory lasts the entire combat, but the temporary hp can be lost pretty quick against a hard hitting mob.

3\) Your real hp never change, only the displayed hp in your prompt. The oath temporary hp are separate, so you can lose them when the fight ends. (No free healing!). This is the same mechanic for warcry hp by the way.

4\) Would you rather fail your oath every time you get hit by a bad proc?

5\) Knocking an opponent unconscious is obviously a victory. It isn't called oath of murder.

Edit: To be clear, I'm not arguing that there is no bug. I am explaining the game mechanics which are working as intended. The actual bug is that the mob's first few attacks <em>display</em> as 'misses' while they deplete your warcry and oath of victory temporary hp. It is purely a display issue. Your extra hp aren't timing out, they're being used up.

</div>

<div class="post" data-post-id="38217" data-author="Gorka" data-date="2017-04-15T21:32:38+00:00" data-subject="Re: Oath of Victory Bugged?">

After talking with Josiah a while, I went and killed an easier mob I knew would miss me in my ac equipment.

I swore victory and the hp bonus stayed with me.

Josiah thinks that in regards to the mob I posted about, I was actually being hit, but because it was only deducting from my temp hp's the hits are registered as misses. In effect there may not be a problem here <strong>but the messages are "misleading."</strong> I'll do some more investigation tomorrow.

</div>

<div class="post" data-post-id="38218" data-author="*teker*" data-date="2017-04-16T16:26:02+00:00" data-subject="Re: Oath of Victory Bugged?">

I can confirm what Josiah is saying. I had to work around that when tracking damage counters so that temp hps wouldn't throw off the numbers. The behavior could be corrected to show the correct message. I think it should also be corrected so that if damage is reduced to zero by spell or other ability, the attack should show a "tickle" message instead of a miss.

</div>

<div class="post" data-post-id="38219" data-author="Gorka" data-date="2017-04-16T19:59:06+00:00" data-subject="Re: Oath of Victory Bugged?">

Just an idea Teker... how about reporting the damage as it should... but showing the damage lines that used temp hp as a different colour?

I know in the coliseum when a mob procs and I didn't save red got used... and if I did save the light blue colour was used. Light blue (d09) could be used to signify the loss of "temp hp" whilst keeping the reporting "honest."

It was confusing to feel like the mob didn't hit me the first two rounds, but "never missed" after the second round. In my view, all reporting should be "honest." 

This system could be used for anything involving temp hp, such as warcry, oath and eudamon over heal.

</div>

<div class="post" data-post-id="38220" data-author="Teron" data-date="2017-04-17T05:32:34+00:00" data-subject="Re: Oath of Victory Bugged?">

I like the idea of using color, however, the last attack that eats through your temp hps doesn't consume all of them. Ie, an attack of 100 damage that hits your remaining 80 temp hps is currently displayed as a 20dam attack.

If you color it the same as the attack that was lost to the temp hps completely, then we'll lose the info on how much of damage went through with the last attack that hit the temp hps.

I have no solution to the problem other than showing damage numbers differently to the right of the message

The Tarrasque viciously massacres you with its hit (200)

The Tarrasque viciously massacres you with its hit (150) [50]

</div>

<div class="post" data-post-id="38228" data-author="Josiah" data-date="2017-04-21T20:08:34+00:00" data-subject="Re: Oath of Victory Bugged?">

Another solution is to not display anything fancy or colored. 

Just show that we got viciously massacred instead of pretending we were missed.

(First world warrior problems, its too hard to die!)

</div>
