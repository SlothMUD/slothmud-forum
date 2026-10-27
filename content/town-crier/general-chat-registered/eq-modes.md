---
title: "EQ Modes"
topic_id: 2663
author: "jezer"
date: 2007-12-09T10:15:16+00:00
last_activity: 2007-12-14T02:22:36+00:00
last_author: "Weasel"
sticky: false
locked: false
post_count: 25
---

<div class="post" data-post-id="21584" data-author="jezer" data-date="2007-12-09T10:15:16+00:00" data-subject="EQ Modes">

I'm getting one of my chars to that stage where I am developing a regen EQ mode. Regen to me has previously just meant sleeping in your fighting EQ, but now that I play a "can't solo kobolds wthout mana" 4 x Caster, mana regen is essential.

So I get a bunch of robes and regen eq... and I sit down and try and make me a script to switch modes. It's not long till I am pulling my hair out about the best way to switch EQ Modes, hence I decided to ask for advice...

There are a bunch of problems...

1\) I want to keep my current inv for all modes. (Recalls, Potions, Moldies, Food, Drink Countainers etc)

2\) Everytime I use the ALL keyword, I always seem to accidentally put a robe in a robe in a robe or something stupid like that... or put inv in the wrong robe... apart from my drinking container which never seems to fit in any robe...? What is it with drinking containers? Why do they never seem to fit?!? and I spend the next 15mins putting everything back in it's right place.

3\) After setting up two modes... and then looking to make a 3rd mode for shapeshifting I realised that if I was in regen mode, I would have to go back to fight mode before I could do shapeshift mode!

So I am up against all these frustrating problems... and to compound the problem... if a eq slot doesn't have a piece of regen eq in it... why can't I keep my buff ac eq in that place... just incase I get attacked while sleeping in a regen mode!

Here is what I wanting to achieve...

1\) You can change from one mode to another, without returning to a primary mode first.

2\) The EQ change script works no matter what char I have logged on... yeah that's a biggie, I know. (But eq doesn't need to be named individually it can work!)

3\) Fighting Mode

4\) Shapeshift Mode

5\) Regen Mode

6\) Healo Mode

Here are my current scripts...

Fightmode

remove all;

put all.ring white-silk;

put all.ankh white-silk;

put all.bracelet white-silk;

put black-trimmed white-silk;

get all swirling-robes;

put white-silk mystical-cloak;

put swirling-robes mystical-cloak;

wear all;

Regenmode

remove all;

get swirling-robes cloak;

get white-silk cloak;

put all.ring swirling-robes;

put all.camail swirling-robes;

put all.wrist swirling-robes;

put ivory-scarab swirling-robes;

put white-sash swirling-robes;

put mystical-cloak swirling-robes;

put yawning-death swirling-robes;

put ivory-bracers swirling-robes;

put silver-gauntlets swirling-robes;

put mud-boots swirling-robes;

put silver-leg-plates swirling-robes;

put lesser-helm swirling-robes;

put mystic-plate-mail swirling-robes;

put ivory-torch swirling-robes;

get all white-silk;

wear all;

Please post and share your wintin scripts, and ideas that might help me...

\------------Note To Immortals-----------------

Can we not improve the flexibility of the remove, get and put commands?

I don't feel I am asking for anything unreasonable here, like more power and removing lags... I'm just asking for the flexibility I have in real life to change my clothes and put them in bags! <img src="/images/smilies/icon_e_biggrin.svg" alt=":D" title=":D" width="15" height="15" class="smiley nozoom">

How about "REMOVE ALL WORN PUT ROBE"? I mean it's simple enough to do this in real life... but in sloth... it all gets mixed up with my INV <img src="/images/smilies/icon_e_sad.svg" alt=":(" title=":(" width="15" height="15" class="smiley nozoom">

How about "GET RING RING BRACER LEGGINGS ROBE"? It's a bit better than GET ALL.RING ROBE and GET ALL.BRACER ROBE etc... I'm not asking to remove lag penalties or anything... add them all up and hit me at the end with them like they are at the moment... I'm just wanting a little bit more flexibility to change my eq with scripts.

</div>

<div class="post" data-post-id="21585" data-author="jezer" data-date="2007-12-09T10:30:36+00:00" data-subject="">

Ok... I'm just thinking a bit deeper about the issues at hand here...

If your like me, can't afford a vault... and you carry 100 items in your robe. I really hate it how some mob chills me and I loose strength... Somehow I can wear all my eq, but the moment I drop a piece, and pick it up I can't...??? I mean we talk about making the mud like real life... that's kind of weird. I can't lift something that I was already carrying...

I also don't understand if I wear a heavy robe I can pick stuff up... but if it's in INV I can't? That's weird too... nothing worse than being in my regen mode and I can't even create food and pick it up cause my fat robe is in INV.

Maybe the strength and inventory coding of sloth, has remained mostly unchanged since the original codebase... I mean it's foundational code that doesn't really need changing once it's in... but is it time for a planning phase and an upgrade?

</div>

<div class="post" data-post-id="21586" data-author="Tap" data-date="2007-12-09T12:05:29+00:00" data-subject="Cake walk if your&#x27;e a bag of flour">

Might take an extra sec or two but why not forget the get all/rem all method of re-organizing? Your Ac Robe should be just that... inside it is 2-3 seperate robes according to what mode you want to be in.. then you could....

rem ac.robe

l in ac.robe

robe (carried):

mana-robe

shift-robe

healo-robe

get mana-robe ac.robe

get item #1 mana-robe

etc

etc

then when done

put item #1 mana-robe

etc

etc

put mana-robe ac.robe

wear ac.robe

As far as your second query....also an easy solution

Don't get chilled

 <img src="/images/smilies/icon_cool.svg" alt="8)" title="8)" width="15" height="15" class="smiley nozoom">

</div>

<div class="post" data-post-id="21587" data-author="Roadrunr" data-date="2007-12-09T14:24:50+00:00" data-subject="">

getting each item individually from a robe is much much slower than get all the way you run into problems tends to be if youhave too much crap in inventory.

</div>

<div class="post" data-post-id="21588" data-author="Widow" data-date="2007-12-09T14:54:16+00:00" data-subject="">

Jezer,

I am almost to the point that you are with my eq, though I have additional Undead Control eq to deal with.

The simplest way to handle this for me is to script specific pieces to replace but store them all in a specific container, to eliminate confusion. I don't know of any way to make this work across characters as they have different equipment. I do think that zMud would offer you triggers to be able to do this if you script it correctly. I've had scripts that would recognize locations, but it still needs specific equipment to remove and replace.

Your best bet is to carry multiple robes/containers (I love the dirty lunch pail for UC gear) and script your wardrobe changes from there.

</div>

<div class="post" data-post-id="21589" data-author="Autolycos" data-date="2007-12-09T15:02:11+00:00" data-subject="Re: EQ Modes">

> <strong>jezer wrote:</strong>
> I'm not asking to remove lag penalties or anything... add them all up and hit me at the end with them like they are at the moment... I'm just wanting a little bit more flexibility to change my eq with scripts.

how about this?

SlothIII has been running for over 10+ years now and until now, I do not recall ever hearing anyone complain about eq-changes etc unless they were using telnet. I'd say that almost EVERY player has 3-4 changes of gear be it, AC, regen, raise, wtf ever. Yet they dont complain. 

Eq scripts are a neccesary evil that most only write once and lightly modify over the years. So stfu, suck it up and deal with it.

</div>

<div class="post" data-post-id="21590" data-author="Alberich" data-date="2007-12-09T15:26:10+00:00" data-subject="Re: EQ Modes">

> <strong>Autolycos wrote:</strong>
> Eq scripts are a neccesary evil that most only write once and lightly modify over the years. So stfu, suck it up and deal with it.

^^this

</div>

<div class="post" data-post-id="21591" data-author="brady" data-date="2007-12-09T15:39:21+00:00" data-subject="">

First off, Autolycos is an ornery prick.

Second, with the new eq changes, remove all/wear all might not be the best way to go if you are just developing your eq changes. I won't change mine cause I'm lazy but there is a new lag for those that remove all/wear all vs removing each item individually (I think it's dumb).

Keeping stuff in your inventory is not the best idea. I'm not Atwell or Ditheca but it makes a difference in what you can carry/change into. Get an inventory container.

For your change scripts, you have to be specific (ie. get all silk-robe). That should be obvious, really.

As for strength, most people will have one mode that offers more than the other. It can be frustrating but you should be able to change into the eq that lets you get what you need. Othwerwise, reroll.

As far as chill goes, dispel self and done.

Oh, and stop whining.

ps...my dirty lunch pail is small and full.

</div>

<div class="post" data-post-id="21593" data-author="jezer" data-date="2007-12-09T22:08:44+00:00" data-subject="">

Thanks Tap, I'll give that idea a shot later tonight and I'll post back what I came up with for critism... 

The ideas about avoiding the ALL tag and naming individual parts should cut down the bad ways I could make the script.

</div>

<div class="post" data-post-id="21595" data-author="Malison" data-date="2007-12-10T00:33:34+00:00" data-subject="">

You might try something like this:

Requirements:

\-all chars need the same names on storage containers.

\-an empty container in your inventory to go with your moldys, food, drinks, recalls, etc

Set an alias for removing and putting on each gear set

[getting out of ac]

\#alias fight-off

rem all;

get swirling-robes mystical-cloak;

put all swirling-robes;

get golden-sack swirling-robes;

get mystical-cloak swirling-robes;

put swirling-robes mystical-cloak

[getting into regen]

\#alias regen-on

get white-silk-robe mystical-cloak;

get all white-silk-robe;

put white-silk-robe mystical-cloak;

wear all;

\#var gear regen (\*this line stores what gear you're in so you can change out of it automatically)

...This wouldn't leave your AC piece on if you don't have a regen gear for that slot, but it works no matter what items you have for your gears as long as the storage containers are the same across your characters.

Then to switch gears, you only need one more alias for each gear to end up in:

\#alias shiftmode {put all golden-sack;$gear-off;shift-on;get all golden-sack}

Notice because you set your 'gear' variable when you put it on, you can use '$gear-off' and it'll pick the alias for what you're wearing.

This was designed keeping in mind you seem to use your mystical-cloak in multiple gears. If you ever use a mana regen robe, you'd need to store mystical-cloak in some container that's part of your regen gear, and to add a line to 'regen-off' about getting it back out.

</div>

<div class="post" data-post-id="21596" data-author="Yinao" data-date="2007-12-10T04:32:43+00:00" data-subject="">

.... AC, Max mana, mana regen, raise, heal, heal 2, shift, dam, and no complaints <img src="/images/smilies/icon_eek.svg" alt=":shock:" title=":shock:" width="15" height="15" class="smiley nozoom">

</div>

<div class="post" data-post-id="21597" data-author="Teron" data-date="2007-12-10T08:24:24+00:00" data-subject="">

Jezer, start small, write scripts yourself and eventually you'll come up with what suits you best.

Only this way you'll be able to create efficient scripts that you'll be able to edit blindfolded.

It requires play experience or at least some thinking at what scripting approach you should take, but it's worth it.

</div>

<div class="post" data-post-id="21600" data-author="Hotara" data-date="2007-12-10T11:51:40+00:00" data-subject="">

Shrugs, I gave up eq shifting years ago, and nowadays I 2.tank epic mobs with -2 ac, and sometimes live.

Chill!

Staying relevant, Whilst it seems interesting to be able to shift to multiple eq gear without returning to the default set, it's a helluva lot of work, especially if you want it to work for all your characters (which would be impossible, unless if you've got a weasel-ferret thing going on).

I think your \_default\_ gear should be regen; here's why:

Chances are, when you solo, you either do it with ac, or shift. So from regen, it covers both bases. Furthermore if you're healing, it's perfect, since most of us just use regen gear for healing (exclude the overenthusiastic clerics). Regen gear seems to be the best bet for default.

I do not see an instance where you would need to directly shift from ac -\> shift, naturally you would want to save as much mana as possible for sustaining your shift, so the regen -\> shift seems better, likewise for AC, as you mentioned you need mana to kill beyond kobolds.

But if you seem to need (really really need) to go from ac -\> regen -\> shift, instead of from ac -\> regen -\> ac -\> shift, just set some variables for your client to know what gear you're in, and assign values of what falls under the category of that variable. Then you're able to do so, and write a fail-safe trigger to ensure that you are in the proper gear. {You could get your client to parse all your eq to see if it's correct for the gear, tonnes of work again! Worst part, you'll have to edit it again when you gain better eq!}

It's pretty easy on Zmud, im not sure how it's done on wintin. Ask at the wintin forums if that's your client, they're a helpful lot.

My advice, fight it off with using a \_Default\_ gear, which would be able to change you to your other sets.

\-Hotara

</div>

<div class="post" data-post-id="21601" data-author="jezer" data-date="2007-12-10T12:40:30+00:00" data-subject="">

So I made a script which uses robes as modes... heavily based on the information provided by Malison.

\#defgroup {Mode}

\#alias {ac-off} {#var eqmode ac;#showme ---EQ CHANGE : AC Off---;putoff;} {G\|Mode} {T\|WT}

\#alias {ac-on} {#var eqmode ac;#showme ---EQ CHANGE : AC On---;puton;} {G\|Mode} {T\|WT}

\#alias {putoff} {#var changerobe $$eqmode$robe;put all $invrobe;remove all;get $changerobe $mainrobe;put all $changerobe;get $invrobe $changerobe;get $mainrobe $changerobe;put $changerobe $mainrobe;} {G\|Mode} {T\|WT}

\#alias {puton} {#var changerobe $$eqmode$robe;get $changerobe $mainrobe;get all $changerobe;put $changerobe $mainrobe;wear all;get all $invrobe;} {G\|Mode} {T\|WT}

\#alias {regen-off} {#var eqmode regen;#showme ---EQ CHANGE : Regen Off---;putoff;} {G\|Mode} {T\|WT}

\#alias {regen-on} {#var eqmode regen;#showme ---EQ CHANGE : Regen On---;puton;} {G\|Mode} {T\|WT}

\#variable {acrobe} {swirling-robes} {G\|Mode}

\#variable {changerobe} {eqmoderobe} {G\|Mode}

\#variable {eqmode} {regen} {G\|Mode}

\#variable {healrobe} {backpack-pack-leather} {G\|Mode}

\#variable {invrobe} {black-persecution} {G\|Mode}

\#variable {mainrobe} {mystical-cloak} {G\|Mode}

\#variable {regenrobe} {white-silk-robe} {G\|Mode}

\#variable {robe} {robe} {G\|Mode}

\#variable {shiftrobe} {robe-dark-mysteries} {G\|Mode}

\#defgroup {}

By being a bit fancy I can cut down the size of my script code by using variables as modes, and just calling "wear" and "unwear" commands with a mode parameter as it were.

I have two problems... that are REALLY annoying me...

1\) Wintin removes the double $ in my script when I save making it useless everytime I load it.

2\) It doesn't seem to save my variable straight away when I set it... here's the proof...

inv

You are carrying:

a mystical cloak (with a single-striped white sash (Private) attached to it)

a black robe of persecution..It emits a faint humming sound!

\<476hp 365ma 94mv 4.0ac +9al 15181953xp\>

<strong>\#var eqmode regen</strong>

<strong>\#Ok. {eqmode} now equals {regen}.</strong>

<strong>puton</strong>

<strong>You get swirling black and red robes from a mystical cloak.</strong>

\<472hp 364ma 94mv 4.0ac +9al 15181953xp\>

You get an ivory torch from swirling black and red robes.

You get a swirling red and blue ring from swirling black and red robes.

You get a swirling red and blue ring from swirling black and red robes.

You get steel camail from swirling black and red robes.

You get steel camail from swirling black and red robes.

You get a suit of mystic plate mail from swirling black and red robes.

You get a lesser helm from swirling black and red robes.

You get a pair of silver leg plates from swirling black and red robes.

You get a pair of mud encrusted boots from swirling black and red robes.

You get a pair of silver gauntlets from swirling black and red robes.

You get ivory bracers from swirling black and red robes.

You get a shield of yawning death from swirling black and red robes.

You get a soft white sash from swirling black and red robes.

You get a leather wrist guard from swirling black and red robes.

You get a leather wrist guard from swirling black and red robes.

You get an ivory scarab from swirling black and red robes.

\<472hp 364ma 94mv 4.0ac +9al 15181953xp\>

Ok.

\<472hp 364ma 94mv 4.0ac +9al 15181953xp\>

scarab ivory: You grab an ivory scarab.

guard wrist leather: You slide a leather wrist guard over your left wrist.

guard wrist leather: You slide a leather wrist guard over your right wrist.

sash white: You tighten a soft white sash about your waist.

shield skull great yawning death: You start using a shield of yawning death as a shield.

ivory bracers: You wear ivory bracers on your arms.

gauntlets silver: You wear a pair of silver gauntlets on your hands.

boots mud encrusted: You step into a pair of mud encrusted boots.

silver leg plates: You wear a pair of silver leg plates on your legs.

lesser helm: You wear a lesser helm on your head.

suit mystic plate mail: You crawl into a suit of mystic plate mail.

camail steel: You wear steel camail around your neck.

camail steel: You wear steel camail around your neck.

ring swirling red blue: You slide a swirling red and blue ring onto your left finger.

ring swirling red blue: You slide a swirling red and blue ring onto your right finger.

torch ivory light: You light an ivory torch and hold it.

cloak mystical robe: You wear a mystical cloak about your body.

You can't figure out how a black robe of persecution works.

A black robe of persecution is far above your experience in back alleys.

(You need to work on one of the above to use this item).

\<472hp 364ma 94mv -7.2ac +9al 15181953xp\>

You get a scroll of recall from a black robe of persecution.

You get a scroll of recall from a black robe of persecution.

You get a damp moldy scroll from a black robe of persecution.

You get a damp moldy scroll from a black robe of persecution.

You get a damp moldy scroll from a black robe of persecution.

You get a damp moldy scroll from a black robe of persecution.

You get a damp moldy scroll from a black robe of persecution.

You get a damp moldy scroll from a black robe of persecution.

You get a damp moldy scroll from a black robe of persecution.

You get a purple potion from a black robe of persecution.

You get a silver boat ticket from a black robe of persecution.

You get an ebony black amphora from a black robe of persecution.

\<472hp 364ma 94mv -7.2ac +9al 15181953xp\>

The day has begun.

\<476hp 364ma 94mv -7.2ac +9al 15181953xp\>

\#showme $regenrobe

white-silk-robe

\#showme $eqmode

regen

Notice how I set the #var eqmode to "regen" but when I run the "puton" command it uses the ac robe when the variable is set for the regen robe! It seems to be a wintin fault... ? Any ideas.

</div>

<div class="post" data-post-id="21603" data-author="Malison" data-date="2007-12-10T15:28:20+00:00" data-subject="">

> <strong>Quote:</strong>
> \#alias {puton} {#var changerobe $$eqmode$robe;get $changerobe $mainrobe;get all $changerobe;put $changerobe $mainrobe;wear all;get all $invrobe;} {G\|Mode} {T\|WT}

This is a Wintin thing...when you did 'puton' it sent all the commands to Sloth at the same time...meaning it called up the old $changerobe before having time to change it. If you set $changerobe at the same time as you set $eqmode that should be fixed.

Not sure how to fix the double $$ problem, being a Wintin95 user instead of .net

</div>

<div class="post" data-post-id="21605" data-author="Leaf" data-date="2007-12-10T16:39:06+00:00" data-subject="">

> <strong>brady wrote:</strong>
> First off, Autolycos is an ornery prick.
> 
> 
> 
> As far as chill goes, dispel self and done.
> 
> 
> 
> Oh, and stop whining.
> 
> 
> 
> ps...my dirty lunch pail is small and full.

From what I can recall, Chill Touch can not be dispeled. You have to wait

for it to go away, or pay a Mage on VK.

</div>

<div class="post" data-post-id="21607" data-author="brady" data-date="2007-12-10T17:00:22+00:00" data-subject="">

Ok.

You chill Brady.

You feel your life flowing away as Brady chills you.

sc

Brady \<\~PIRATE\~\> Vote! (level: 40)

Your levels: Ma: 40 Cl: 40 Wa: 40 Dr: 40 Av: 40 

You are 54 years old.

You are a citizen of Settlestone.

You are a devout worshipper of Akasha.

You are an example to us all.

You have visited most of this area.

You've seen 50.9% of the world.

You have (651/845+14) hit, (695/736+69) mana and (184/184+28) movement points.

Your armor class is 2.6.

You have +8 to hit and +9 on damage.

You have 1,428,458 gold coins.

You have seventy-four drachma.

You have 284,232,413 unused experience points.

You have been playing for 224 days and 20 hours.

You are a member of Pirates.

You are strongly attuned to the channelling stratum.

Str: 18 / 40, Int: 18, Wis: 18, Dex: 18, Con: 18

You are standing.

You are affected by the following spells:

 Chilled 

 Detect Evil 

 Detect Good 

 Detect Magic 

 Detect Invisible 

 Sense Life 

 Infravision 

 Resist Fire 

 Resist Webs 

 Stamina 

 Corona 

 Vigor 

 Vitality 

cast 'dispel mag' brady

Ok.

You feel a spell unravel! Success!

You feel dizzy for a moment...

You feel a spell unravel! Success!

You feel dizzy for a moment...

You feel a spell unravel! Success!

You feel dizzy for a moment...

You feel a spell unravel! Success!

You feel dizzy for a moment...

You feel a spell unravel! Success!

You feel dizzy for a moment...

You feel a spell unravel! Success!

You feel dizzy for a moment...

You feel a spell unravel! Success!

You feel dizzy for a moment...

You feel a spell unravel! Success!

You feel dizzy for a moment...

You feel a spell unravel! Success!

You feel dizzy for a moment...

You feel a spell unravel! Success!

You feel dizzy for a moment...

You feel a spell unravel! Success!

You feel dizzy for a moment...

You feel a spell unravel! Success!

You feel dizzy for a moment...

sc

Brady \<\~PIRATE\~\> Vote! (level: 40)

Your levels: Ma: 40 Cl: 40 Wa: 40 Dr: 40 Av: 40 

You are 54 years old.

You are a citizen of Settlestone.

You are a devout worshipper of Akasha.

You are an example to us all.

You have visited most of this area.

You've seen 50.9% of the world.

You have (653/762+14) hit, (698/686+69) mana and (184/184+28) movement points.

Your armor class is 2.6.

You have +8 to hit and +8 on damage.

You have 1,428,458 gold coins.

You have seventy-four drachma.

You have 284,232,413 unused experience points.

You have been playing for 224 days and 20 hours.

You are a member of Pirates.

You are strongly attuned to the channelling stratum.

Str: 18 / 0, Int: 18, Wis: 18, Dex: 18, Con: 17

You are standing.

You are affected by the following spells:

 Resist Fire

</div>

<div class="post" data-post-id="21608" data-author="mahkra" data-date="2007-12-10T17:10:45+00:00" data-subject="">

For what it is worth I made all my EQ slots variable so when I get a new piece of EQ I just change the variable, instead of fishing thru huge aliases. It took a while to setup but has saved me hours of screwing with it since itâ€™s rare I need to change a eq switch alias.

Var tankhead

Var solohead

etc

I have an alias for each direction of EQ change.

tank to regen

regen to tank

solo to regen

regen to solo

tank to solo

solo to tank

Since regen is the big issue for me I set a variable with which alias to call for regening and moving from regen to normal mode. I then have two commands to regen getup and crash. They each just call the appropriate variable.

For what ever reason if my eq ever gets messed up I can fix it by doing the triangle (usually because I lack space in inventory). Crash, getup, solototank, tanktosolo and everything gets put back into place. 

A different approach I suppose. Do with it what you will. 

I'm not a fan of the new changes but if I ever had the time I could make the changes faster with the change but then I belive my reseting trick will break as well and it sucks fishing thru 5 containers....

</div>

<div class="post" data-post-id="21609" data-author="Leaf" data-date="2007-12-10T17:31:20+00:00" data-subject="">

Interesting, thanks for testing it out Brady

</div>

<div class="post" data-post-id="21623" data-author="13" data-date="2007-12-11T14:18:21+00:00" data-subject="">

this is a good idea

my default eq is 'fighting' gear, from there i can do

\+handgear - into HD gear from dmg/spelldmg/ac

regon - switches into regen gear

from regon i can do 

memup - which mems

\+rent - rent gear

regoff - back to fighting gear

fighting gear is probably default for me because im not a caster prime

like hotbot

the only piece of eq that i var is drink container

i have one basic wintin file that i edit for each character when i start them

and then save and change the write alias.

thats the wintin experience for me.

</div>

<div class="post" data-post-id="21625" data-author="Autolycos" data-date="2007-12-11T18:03:41+00:00" data-subject="">

oddly enough mine is similar to that as well.

in ac or dam gear my regen/raise scripts are already programmed with every version of what i am wearing to save time. 

it also nulls the worry of what gear i'm in when i switch.

</div>

<div class="post" data-post-id="21644" data-author="Rodek" data-date="2007-12-12T20:45:56+00:00" data-subject="">

You can string removes or wears together now instead of using wear all, remove all, try something like this:

rem ring ring robe cloak bracelet-jade

all in one line like that.

As for me, I pick a main mode for each character that I pivot off of for most changes. For most of the chars it is actually the max mana mode, but I think using regen mode would make more sense if I were to redo it. Some of the stuff is in its own containers, but recently I have decided it is just as fast to pull evertying from a main robe. There is no lag on getting or putting items in or out of a container, just more scroll, and it is then easier to use the same items in multiple modes.

In other words, take everything off, put into main robe, pull new items by name, wear all.

</div>

<div class="post" data-post-id="21646" data-author="jezer" data-date="2007-12-12T22:44:17+00:00" data-subject="">

Thanks to Malison about wintin info. I put both vars together and it works sweet now. 

Truth is though, I'm starting to see things like Rodek... and last night after shocking because I was in regen mode... which put me back to 15 con... I think it's important to wear as much eq as possible, not just the few items you have for what ever mode. (Even if regen mode is near complete)

It's probably more work, but the item substitution out of one robe, probably will work the best. I tend to have problems with str in regen mode... as in I can't pickup food.

I have a question though... Rodek's idea says to put all in robe... which brings me back to Inventory...

I've seen people take a recall out of a robe and recite recall when they are about to die... is there any lag doing this? Should recalls always just go in inv? If you put all robe, don't you just end up with inv rubbish in your robe? Is it wise to run with a completely clean Inv?

Your thoughts...?

</div>

<div class="post" data-post-id="21660" data-author="strider" data-date="2007-12-13T15:43:22+00:00" data-subject="">

eq switches might be the only unique things we have left for everyone's characters. always fun to just play with them till ya get one you like. as for your inventory questions. large container, raft, recall, keychain, and drink container are about all i usually carry, (cept necro has his juju charm, and casters tend to carry the flux, and thief his pouch.) don't keep recall in inventory and then pull out to use, it'll get ya killed. go the other way around. alias that recalls you, then gets one out of container. only need to have one out and this way you always do, plus you'll notice when you run out. this won't help your str problems a whole lot, except that you can rem robe and put inventory container in it, wear robe, and you're strong again!! pick up all ya want, remove robe, get inv container out, and you've got all you wanted to carry on ya. 

peace out

</div>

<div class="post" data-post-id="21662" data-author="Weasel" data-date="2007-12-14T02:22:36+00:00" data-subject="">

> <strong>Rodek wrote:</strong>
> You can string removes or wears together now instead of using wear all, remove all, try something like this:
> 
> rem ring ring robe cloak bracelet-jade
> 
> all in one line like that.

Thanks, I wasn't aware of that. Amended all my eq change scripts accordingly last night, and now have less spam as well as being a few seconds faster overall than I had previously. Cheers.

</div>
