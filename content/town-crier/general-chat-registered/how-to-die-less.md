---
title: "How to die less..."
topic_id: 4946
author: "Gorka"
date: 2020-01-20T10:51:22+00:00
last_activity: 2020-01-20T10:51:22+00:00
last_author: "Gorka"
sticky: false
locked: false
post_count: 1
---

<div class="post" data-post-id="39357" data-author="Gorka" data-date="2020-01-20T10:51:22+00:00">

Generally solo deaths in sloth are stupid, the majority of which are caused by poor calculations, unexpected circumstances and the inability to react to them in time. (Unless you get "one shotted" in which case you are forgiven)

When a fight comes down to the wire, quite often the player is aware at least one round early that things are not going well... they have a couple of seconds to explore the alternatives... retreat, flee, recall or stand. (All of these options are quite prone to failure) After the player has made their decision, quite often a further thing can complicate the matter... like server lag, or another mob assisting or the fact you have already sent other commands to the mud which have not been squelched first.

It's not possible to plan for every circumstance and make the right decision quickly... however thankfully the rules that pertain to death in sloth are actually very simple... lack of hp. Now there are several ways to track this, either you can set a trigger to capture the hp in your command prompt, or read the msdp.HEALTH variable.

Now in my experience, knowing what to do in every circumstance that arises can be impossible, and no matter how much experience you have there can always be a circumstance you didn't expect. The important issue in this equation is the lack of time we have to respond. So here is my solution I personally have used for about 18 months now...

When your health reaches below a certain value  OR the amount of health you have lost, since the beginning of the fight till now, is more than the percentage the mob has lost, trigger this command to be sent to the mud...

|;stand;shapeshift tree (If you are a warrior send a second wind at the end as well)

In msdp it looks like this...

```
      if (100 - tonumber(msdp.OPPONENT_HEALTH) < (((starthp - tonumber(msdp.HEALTH)) / starthp) * 100)) and tonumber(msdp.HEALTH) <= 500 then
         conclusion = "LOSING!"
         echo("\nLOSING!")
         send("|;stand;shapeshift tree;@@")
      elseif tonumber(msdp.HEALTH) <= 500 then
         conclusion = "LOSING!"
         echo("\nLOSING!")
         send("|;stand;shapeshift tree;@@")
      else
         conclusion = "WINNING!"
      end
```

In 95% of cases this will automatically save your life, and give you the time to think about the best course of action. In perhaps 5% of cases maybe you are bashed and there isn't much you can do. But by doing this you don't have to worry about recalling and running back, or whether you can survive the next round, shape shifting tree will disengage the combat and give you as much time as you need to think about your next move whether that be recalling, or returning to human form and continuing to fight. If the shape shift command fails, the mud reports failure... and another command prompt is displayed which triggers the shape shift again so it's pretty fail safe.

The added advantage of disengaging the combat through tree is that in this matter, often the mobs will not attack immediately once the player returns to human form, giving you a chance to slip in a restore, or put back up a spell that had dropped.

Never initiate any combat with any mob, unless your spells are up, and your hp is full. The contemplation skill is your friend, make sure your hp is full before each and subsequent mob.

</div>
