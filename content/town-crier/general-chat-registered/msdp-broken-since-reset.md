---
title: "MSDP Broken Since Reset?"
topic_id: 5033
author: "Gorka"
date: 2021-09-06T19:14:50+00:00
last_activity: 2021-10-10T23:18:41+00:00
last_author: "cnl"
sticky: false
locked: false
post_count: 7
---

<div class="post" data-post-id="39812" data-author="Gorka" data-date="2021-09-06T19:14:50+00:00" data-subject="MSDP Broken Since Reset?">

```
Welcome back Gorka!  Press return to continue...

Reconnecting.

<1883hp 852ma 655mv -15.0ac Settlestone 51807024724xp -%>

^[F210][^oINFO^[F210]]^n MXP version 1.0 detected and enabled.
```

None of my MSDP is working since reset.

</div>

<div class="post" data-post-id="39813" data-author="Gorka" data-date="2021-09-06T20:25:12+00:00" data-subject="Re: MSDP Broken Since Reset?">

Turns out a setup trigger wasn't firing due to the Arglebargle, glop-glyf!?!

I fixed the trigger and everything now works... however I think the issue on login should be fixed also.

</div>

<div class="post" data-post-id="39814" data-author="cnl" data-date="2021-09-07T00:31:31+00:00" data-subject="Re: MSDP Broken Since Reset?">

I have mxp disabled in mudlet settings because it's buggy 

Options > Preferences > Special Options > Force MXP Negotiations Off

I turn on MSDP on the following 2 triggers since doing so makes the MXP message not show up.

```
Welcome to the land of SlothMUD. May your visit here be... Interesting.
Reconnecting.
```

However, I agree something has changed with MXP on this latest reboot - even with it off I get the following message on **channel who**

```
Here are the currently open channels.
Locked?  #Users  Name
------------------------------------
     No       5  	<SEND "channel join slackers|channel who slackers" hint="Join slackers|Show members of slackers?">slackers	</SEND>
```

which looks like MXP plaintext mixed in for some reason even though I have it turned off, plus the weird login stuff you're seeing.

</div>

<div class="post" data-post-id="39815" data-author="*teker*" data-date="2021-09-08T19:47:28+00:00" data-subject="Re: MSDP Broken Since Reset?">

I believe this will be fixed at next reboot.  I was working on cleaning up some of the comm code (to try to figure out some of the MXP issues) and I think it accidentally got put into production.

</div>

<div class="post" data-post-id="39837" data-author="cnl" data-date="2021-10-10T06:16:34+00:00" data-subject="Re: MSDP Broken Since Reset?">

is there something that has broken msdp for SAVING_SPELL in CHARACTER_AFFECTS for "item-generated'

I'm seeing entries for things like HEAL_BONUS but not for SAVING_SPELL. 

eg

  ["0"] = {

    DURATION = "-1",

    LEVEL = "45",

    MODIFY = "HEAL_BONUS",

    PERMANENT = "1",

    POINTS = "10",

    SOURCE = "item-generated"

  },

I rely on this ("item-generated" SAVING_SPELL) quite heavily.

EDIT: Did confirm with 2 9x40s that it's not showing properly for them anymore either.

</div>

<div class="post" data-post-id="39838" data-author="Insomnia" data-date="2021-10-10T19:32:43+00:00" data-subject="Re: MSDP Broken Since Reset?">

Umm, how did you rely on a non-existent thing? Are you sure you're looking into the right place?

It never was on msdp.CHARACTER_AFFECTS with "item-generated". I think it appears there only in special cases with these sources (according to my logs): "fortune", "bless", "word of pain", "fare thee well" and "warcry".

I only use msdp.CHARACTER_STATISTICS.SAVING_THROWS.SPELL.MODIFIER – what's your use case?

</div>

<div class="post" data-post-id="39839" data-author="cnl" data-date="2021-10-10T23:18:41+00:00" data-subject="Re: MSDP Broken Since Reset?">

hmmm.. I think you're right. what the heck is my script doing.

it's definitely not working but maybe that has to do with reborn weirdness or eq not equipping that i expect to be equipped.

I have a set of functions that's going into a loop and I'm not sure why. One of its logic gate functions is 

```
function u.sumAffect(modify)
  local sum = {
    spell = 0,
    class = 0,
    item  = 0,
  }

  for k,v in pairs(msdp.CHARACTER_AFFECTS) do
    if v.MODIFY == modify then
      local key
      
      if v.SOURCE == "item-generated" then
        key = "item"
      elseif v.SOURCE == "class" then
        key = "class"
      else
        key = "spell"
      end
      
      sum[key] = sum[key] + tonumber(v.POINTS)
    end  
  end
  return sum
end

function u.sumAffectSavingSpell()
  return u.sumAffect("SAVING_SPELL")
end
```

and my initial read was perhaps that this adding up to the wrong value was the cause of it looping but looking through my logs I'm kind of thinking you're right and msdp.CHARACTER_AFFECTS never included item-generated SAVING_SPELL

EDIT: OK, this was totally my fault. The values aren't what are expected because I can't wear all items in the eqsets. Sorry :(

</div>
