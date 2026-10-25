---
title: "autoruns/paths"
topic_id: 4601
author: "Madigan"
date: 2016-03-01T00:01:51+00:00
last_activity: 2016-03-01T15:08:38+00:00
last_author: "*juggleblood*"
sticky: false
locked: false
post_count: 4
---

<div class="post" data-post-id="36677" data-author="Madigan" data-date="2016-03-01T00:01:51+00:00" data-subject="autoruns/paths">

Does anyone have a solution for storing and easliy accessing autoruns/paths w/o memorizing a bunch of aliases? Zmud had a nice pop-out window that would store them all... possibly a db function within mudlet to do this.

ideas?

</div>

<div class="post" data-post-id="36679" data-author="*juggleblood*" data-date="2016-03-01T00:55:05+00:00" data-subject="Re: autoruns/paths">

By db function do you mean tables / libraries?

You could make a library of them. Make a new folder under scripts, name it Libraries or something, then make a new script in that folder and name it RUN ALIAS LIBRARY or wutever.

Then in the block:

SSrunAliases={

["dweb"]="Demon Web",

["theris"]="Theris",

["skeep"]="Shadow Keep" }

You've now created a key, value pair table. You could make an alias to display it, i.e. display(SSrunAliases), or you could get fancy and loop thru it and display it in color:

for k,v in pairs(SSrunAliases) do

cecho("<green>"..k.."="..v.."<reset>")

end

Another tip, I like to add checks to some runs too btw for fly or wtb, such as

if affects["FLY"]==nil then cecho("You better fly first!")

else expandAlias("nnneeessswww") end

</div>

<div class="post" data-post-id="36682" data-author="Madigan" data-date="2016-03-01T08:59:42+00:00" data-subject="Re: autoruns/paths">

> ***juggleblood* wrote:**
> By db function do you mean tables / libraries?
> 
> 
> 
> You could make a library of them. Make a new folder under scripts, name it Libraries or something, then make a new script in that folder and name it RUN ALIAS LIBRARY or wutever.
> 
> 
> 
> Then in the block:
> 
> SSrunAliases={
> 
> ["dweb"]="Demon Web",
> 
> ["theris"]="Theris",
> 
> ["skeep"]="Shadow Keep" }
> 
> 
> 
> You've now created a key, value pair table. You could make an alias to display it, i.e. display(SSrunAliases), or you could get fancy and loop thru it and display it in color:
> 
> for k,v in pairs(SSrunAliases) do
> 
> cecho("<green>"..k.."="..v.."<reset>")
> 
> end
> 
> 
> 
> Another tip, I like to add checks to some runs too btw for fly or wtb, such as
> 
> if affects["FLY"]==nil then cecho("You better fly first!")
> 
> else expandAlias("nnneeessswww") end

I love this idea - i need breeze or someone to dumb it down a bit - lost me at the alias setup.

</div>

<div class="post" data-post-id="36685" data-author="*juggleblood*" data-date="2016-03-01T15:08:38+00:00" data-subject="Re: autoruns/paths">

Hrm... Let's make a simple run alias to see where u getting stuck.

Alias menu is second icon down on left, select it. 

Click add group. Select that new alias folder. Put alias name RUN ALIASES. Click save object.

Click add item. Select that new alias. Name it DEMONWEB RUN ALIAS. It helps to have a good naming convention so u can easily do searches. That's why I name things like HUNGER TRIGGER or DEATHGRIP ALIAS. So that if I do a search i wont get confused with DEATHGRIP TRIGGER or DEATHGRIP FUNCTION.

In the pattern box, put: ^dweb$      You'll notice that regex is already selected here, its the only option. What regex means is an expression matching grammar. If you had ^d(emon)?web$ instead of ^dweb$ then either dweb or demonweb would work because the question mark says that text is optional.

In the text block put:

expandAlias("8w")

send("climb up")

expandAlias("6wn3w4s")

send("pray lolth")

send("shapeshift bat")

send("shapeshift bat")

send("pray lolth")

expandAlias("d")

send("open stone")

expandAlias("e2s2de2dsded4e")

send("flee down")

expandAlias("se2d6en3esese2nes3e2s2eneu2es")

send("unlock gate")

send("open gate")

expandAlias("sus")

Now save object and save profile, make sure it's activated, i.e. the green tick left of the alias name. 

So if someone had a lot of these runs to share, they could keep a folder tree RUN ALIASES, containing folders SS RUN ALIASES, BH RUN ALIASES, etc.. and export the main folder as a module that anyone can import, like Breezes.

Helpful?

</div>
