---
title: "color group listings"
topic_id: 3418
author: "Samel"
date: 2010-05-08T14:41:39+00:00
last_activity: 2010-05-10T23:55:41+00:00
last_author: "Gladavar"
sticky: false
locked: false
post_count: 7
---

<div class="post" data-post-id="31119" data-author="Samel" data-date="2010-05-08T14:41:39+00:00" data-subject="color group listings">

If the group listing had colors similar to the prompt denoting health, percent of mana, etc. it would save a lot of 'what's your max mana' type questions.

As an example:

 (Leader)[/color:uxos37yl]             Zuzu [Cl:5.30  792[/color:uxos37yl]hp 349[/color:uxos37yl]ma 30[/color:uxos37yl]mv] ---

</div>

<div class="post" data-post-id="31120" data-author="jezer" data-date="2010-05-09T09:43:19+00:00" data-subject="">

Good idea. Doubt it would be hard to implement. Isabo has done a few group command changes like this lately... I nominate Isabo.  :)

</div>

<div class="post" data-post-id="31124" data-author="Gladavar" data-date="2010-05-10T23:15:07+00:00" data-subject="">

This would be a cool feature to have implemented.  But until someone gets a chance to/decides to work on it, it shouldn't be terribly difficult to do client side for most of the clients out there today.

</div>

<div class="post" data-post-id="31127" data-author="jezer" data-date="2010-05-10T23:18:58+00:00" data-subject="">

This would be a cool feature to have implemented.  But until someone gets a chance to/decides to work on it, it shouldn't be terribly difficult to do client side for most of the clients out there today.[/quote:3ivg2595]

How would you know the other players max mana?

</div>

<div class="post" data-post-id="31132" data-author="Gladavar" data-date="2010-05-10T23:29:51+00:00" data-subject="">

I haven't seen many players report and my memory is a bit fuzzy right now, but the few i recall doesn't it show the max as well as the current stats when they do?  A trigger to pick that up and you would have the values.  

I think i actually had a report of someone in my scrollback before the mud went down but closed my client before thinking to check the actual output.

</div>

<div class="post" data-post-id="31133" data-author="Gladavar" data-date="2010-05-10T23:35:28+00:00" data-subject="">

just did a quick read of a few posts and it doesn't look like report shows the mana.  but you could have a system where when you group with people on a regular basis they could fire an alias real quick to report max hp ma and mv when joining a group. Then pull all the values from the output of that alias just as easily.

</div>

<div class="post" data-post-id="31136" data-author="Gladavar" data-date="2010-05-10T23:55:41+00:00" data-subject="">

Mud's back up and i just did a little test.  Got someone to report and when you use the actual report command the current and max hp, ma, and mv are all shown, so you wouldn't need any special alias.  just a trigger to read the max values from the actual report not autoreport and there are your values.  From there it's just a matter of making things all shinny to suit your taste clientside.

</div>
