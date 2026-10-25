---
title: "Changing Weapons"
topic_id: 4895
author: "Gorka"
date: 2019-03-06T13:34:54+00:00
last_activity: 2020-01-22T08:47:55+00:00
last_author: "Gorka"
sticky: false
locked: false
post_count: 10
---

<div class="post" data-post-id="39123" data-author="Gorka" data-date="2019-03-06T13:34:54+00:00" data-subject="Changing Weapons">

There is a game issue I'd like to discuss surrounding switching weapons, because as a stabber, gripper, warrior and user of proc weapons - things are complicated these days with the increased arsenal of options. Recently for example in MNM I stab and switch to a chopper to take advantage of a possible excruciating blow/chop combo. There isn't really a combination I don't use at some point as a tank...

Generally weapon switching has three important events...

1) Opening Weapon

2) After Opening Weapon

3) Change of Weapon On Mob Death

Eqmodes don't handle the issue correctly, (I think?) because depending on the mob I may stab, slash, grip, chop or strike the mob while not changing any worn eq, especially if I am tanking in AC.

These 3 events are not all able to be captured correctly using scripting which creates issues. For example, continuing to fight a second mob after the first dies triggers often unwanted weapon switches or a splork triggers a weapon swap when none is needed. MSDP can tell you what weapon you wear, but after a mob dies your status does not remain "FIGHTING" when continuing to fight a second mob so you can't mute a weapon change.

Weapon swaps factor on the mob, your eq mode or your desired opener. Coding the possibilities can lead to coding outcomes for 50+ possibilities. The inability to capture game data to precisely interpret the events correctly, and with rescues often requiring squelching changes makes this in my opinion one of the more difficult scripting issues.

I wonder how other players do it. But I'd be very interested to hear from Teker. I wonder if there could be a possibility of creating a eqset for weapons based around the 3 events... we could setup a profile where we set our opener weapon, our continuing weapon and a switch on death weapon if there is no second opponent. The idea being the switching would be done by the game automatically without the need to try and decipher the results of inconclusive game text.

But also if implementing this idea interfered with rebirth shop, whatever is happening with that... I'd much prefer rebrith shop of course!

</div>

<div class="post" data-post-id="39127" data-author="*teker*" data-date="2019-03-11T19:32:31+00:00" data-subject="Re: Changing Weapons">

Rather than have the game do things automatically, I would prefer to create a new MSDP variable that would give you a list of mobs (and/or players) in the room with information currently available to you via a LOOK or other command.  So you could tell who is fighting whom, etc.  Then you can choose what to do about it on the client side.

</div>

<div class="post" data-post-id="39128" data-author="Gorka" data-date="2019-03-11T22:44:57+00:00" data-subject="Re: Changing Weapons">

Perhaps if you made msdp.OPPONENT... msdp.OPPONENTS it might solve the multi-mob issue. If the OPPONENTS array has multiple mobs in it after a death I won't re-equip my stabber and continue slashing... however I know whats going to happen... I will kill the last mob and the array won't update quick enough... and I will keep wielding an incorrect weapon... Msdp isn't useful in every case because it's slightly delayed. For instance try build a healbot using msdp... terrible idea. Try echoing your status on mob death and you will find sometimes it still says you are FIGHTING and other times STANDING.

Splorks I usually solve by checking my equipped weapon on the "Total Exp" trigger. If it's my sword I requip my stabber ready for the next mob. 

It's messy and I have to handle things in non centralised ways. Not sure how you can solve all the issues that I raised with Msdp. It's only good for some things, mud text is quicker for others. OPPONENT already doesn't update to catch a splork nor will it be quick enough to register a dead mob on the total xp line. Perhaps I could stop using the total xp line and catch the msdp.opponent change event instead, I just suspect it won't work very well.

</div>

<div class="post" data-post-id="39129" data-author="*teker*" data-date="2019-03-11T23:16:11+00:00" data-subject="Re: Changing Weapons">

Modern game architecture runs on a slight delay so that the client and server are both running independent simulations of the same events.  You can script easier on that type of architecture because the client knows the future for a small period of time.

If I were to build the list as you suggest, I could include a field to identify which opponent you are currently fighting.  At mob death, you could remove that element from the list (if it still exists due to msdp lag) and look at whether your list is empty.  Not perfect, but would get you closer.

</div>

<div class="post" data-post-id="39130" data-author="Gorka" data-date="2019-03-12T01:55:35+00:00" data-subject="Re: Changing Weapons">

That's possibly a good idea... I could manually remove the opponent I am fighting from the opponents array. However it's not fool proof, there are potential problems to do with the timing of when the msdp OPPONENTS updates and other mobs of the same name in the existing room. I can see a scenario where the msdp updates in a timely fashion, and my manual update, removes incorrectly the second mob of the same name. 

In any case Teker, I still think even if it didn't solve the multi-fighting weapon switching issue... the OPPONENTS array could prove useful in other situations... Tossing summons for instance... prioritising enemies... engaging mobs which are closest to death... lots of very interesting possibilities to geek out on.

</div>

<div class="post" data-post-id="39142" data-author="Roga" data-date="2019-03-26T02:54:14+00:00" data-subject="Re: Changing Weapons">

I mostly do this manually with an automated assist.  In Mudlet I use the following to capture my current wielded weapon in VAR.wielded (Item 16 appears to stay constant for me as wielded):

Scripts -> Name ->  Char_Eq

Add user Event Handler -> msdp.CHARACTER_EQUIPMENT

```
function Char_Eq()
  local eq16 = msdp.CHARACTER_EQUIPMENT['16']
  if eq16['ITEM'] ~= nil then
    VAR.wielded = eq16['ITEM']['KEYWORDS']
  else
    VAR.wielded = ''
  end
end
```

You can then make aliases like...

Alias -> swap_weapon

Pattern -> ^swap$

```
local prevwield = VAR.wielded
send('rem ' .. prevwield)
if string.match(prevwield, 'bolt') then
  send('wield valor')
else
  send('wield bolt')
end
```

Which will swap between valor and bolt.  Or any such combination.  Doesn't solve the 50 different combinations or address issue #3.

The main reason I wanted to comment is that I very much like teker's idea about an msdp variable that would list mobs attacking players (available via LOOK) but for an entirely different reason.  This would have the potential to improve rescue scripts.  As some group member engagement events are not reported this might solve that.

Roga

</div>

<div class="post" data-post-id="39143" data-author="Gorka" data-date="2019-03-26T06:11:54+00:00" data-subject="Re: Changing Weapons">

I also use msdp to get my wielded item in the eqset from position 16, but the core of the issue is not that I don't know what I am wielding, but what I am fighting and at what stage - and if the best weapon is equipped for that.

I'd stop short of supporting an MSDP variable that has all the mobs in the room in it... but instead support an MSDP variable that at least had all of my opponents in it. I think all the mobs in the room, goes a little bit too far... takes a little bit of the reactionary element from the game and assists roboting (not that anything can stop that really). It seems logical that if I am fighting something - I know it is there. If it is there, and I am not fighting it, then that's really another story... that would expose, hidden, invis and hunting mobs potentially. That surprise arguably adds to the game.

Regarding rescue's there are ways to capture everything as far as I know... even silent disengages... that doesn't mean a player like Ezekiel in his best pjyamas won't go splat in a single round though... Good rescue scripts are really what separates the top tanks from each other at the highest level (where essentially we all have the same stats and eqsets, and we are much the same). The following script nearly captures everything that's not a proc special.

(.*) massacres (.*) with  - (Mudlet regex)

```
if tanking == 1 then
   for key,value in pairs(msdp.GROUP) do
      if msdp.GROUP[key]["NAME"] == matches[3] then
         send("|;rescue "..matches[3]..";@@")
      end
   end
end
```

</div>

<div class="post" data-post-id="39144" data-author="Roga" data-date="2019-03-26T10:49:54+00:00" data-subject="Re: Changing Weapons">

Thanks Gorka.  Sometimes I get too focused on a particular solution.  Adding your method should capture the majority of those situations that I was missing.

Roga

</div>

<div class="post" data-post-id="39292" data-author="Gorka" data-date="2019-08-14T07:42:53+00:00" data-subject="Re: Changing Weapons">

Is the changing of the msdp.OPPONENTS variable to include an array of all opponents that are currently fighting you rather than just the engaged one, still something we can do?

Today for instance, I nearly died when 3 maug fighters engaged me a few seconds after each other. It's very difficult to figure out which maug fighter of the 3 was the closest to death so I could engage and kill it when there are 3 mobs with the same name attacking you, and only a few seconds to react. When you retreat and come back into the room, you won't be necessarily engaged with the one closest to death, but you will be fighting all 3. I understand this is not a new problem and it has always been this way... however with msdp there was an attempt to give this information to the player... my argument is, it hasn't gone far enough to be useful.

</div>

<div class="post" data-post-id="39358" data-author="Gorka" data-date="2020-01-22T08:47:55+00:00" data-subject="Re: Changing Weapons">

Last night I changed my weapon switching mechanics again in my sloth scripts. As I have lamented in the past, being 100% sure of what weapon you are wielding at any one point is not a straight forward exercise for a tank. Msdp updates too slow, if you splork something, often you will equip your sword after the splork when you want to keep your backstab weapon for the next mob. Squelching means you can loose track of what you were wielding if you try and track weapon movements in aliases... and there are far to many triggers to capture all the wearing and unwearing of your weapons and eqsets to not end up with a tangled mess. Add to this the different scenario's such as tanking, chopping, or letting another person stab... it's a very difficult thing to track your weapon for tanks.

What I did in the end was basically duplicated all my eqsets but wearing the backstab weapon instead. When I use my backstab alias... I "eqset switch" into the same mode I am wearing, but the backstab version just before I stab. I know this doesn't sound perfect to switch weapons right before you backstab, ideally you would equip your backstab weapon after the last mob dies. Unfortunately in practice that doesn't work so well, as in a place like EU you will frequently get aggroed while wearing a backstab weapon, and pierces are extremely weak and some mobs will bash, leaving you fighting a mob that can kill you with a backstab weapon for several rounds. Yes... In my opinion, it's better to be aggroed wearing the correct weapon, than miss a stab while trying to change.

Using a feature of mudlet, I discovered that my old way of switching weapons using remove weapon / wear weapon was actually taking about a total time of .75 seconds because of the two command lags. Each command you send to the mud has a lag of about .25 of a second, along with the wear equpiment lag. However when I use eqset switch, it only has a total lag of 0.25 to change your weapon (It only has eq lag, not command lag). In a place like EU, that extra .5 seconds changing weapons makes a MASSIVE difference because I am landing stabs quicker now before I get aggroed, using the new method. 

Also a frequent problem using the old method was that after splorking a mob, my msdp based scripts would switch out my backstab weapon for a sword, which meant the next mob I went to stab I would be wearing my sword - which the mud would respond to, which I would then unequip my sword and wear my backstab weapon... by this point a full second has past and the mob has aggroed me. With this new method using eqset to switch into the backstab version of the eqset before stab, it only has the 0.25 wear lag and it's 100% perfect... and if I do get aggroed before making the stab the correct weapon is already equipped.

Unfortunately eqset does not allow you to change weapons while fighting... so I can't use the same method to switch to my sword after backstab, I have to remove the backstab weapon, wear the sword at a cost of a 0.75 seconds which often means I fight the first round still wearing my backstab weapon. This might seem like such a small thing... but when you add up 200 mobs an hour, costing you .5 seconds extra each mob, and then getting aggroed before making the stab... it makes a significant difference.

In my opinion the wear and remove command in sloth shouldn't have "command lag" only "change eq lag." Also I think eqsets should be able to be changed while fighting in the cases where only the weapons are changing... and the game already allows you to change weapons while fighting but eqset does not. So basically eqset and remove / wear work quite differently and have different command lags. Ideally they should work the same, either eqset should at least switch weapons on a change, or the command lag in the wear and remove commands should only be the changing eq lag not the combination of the command and eq wear lags.

</div>
