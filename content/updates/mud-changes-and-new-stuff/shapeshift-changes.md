---
title: "Shapeshift changes"
topic_id: 3555
author: "*Splork*"
date: 2010-10-23T17:48:02+00:00
last_activity: 2011-01-03T07:28:08+00:00
last_author: "*Chobbs*"
sticky: false
locked: false
post_count: 7
---

<div class="post" data-post-id="31922" data-author="*Splork*" data-date="2010-10-23T17:48:02+00:00" data-subject="Shapeshift changes">

Over the course of the last month, our Immortal team has worked on restructuring shapeshifting and hopefully solving some of the issues regarding the ability. Many of the complaints concerning this skill have been addressed and we hope the new changes only strengthen shapeshifting in general.

Shapeshifting is now structured similar to supplicants and necromancer pets. What this means is, the higher up in your classo that a player has chosen druid, the access to more unique forms this player will have. 

Mana costs across the board, both upkeep and initial shift costs, have been greatly reduced. The major complaint regarding shapeshifting centered around the mana costs and the inability to stay in form for any length of time. We are hoping this addresses this complaint. It should also enable players to do more damage in form, as many of the abilities rely on mana to perform and the player should have much more due to the lower costs.

Lag has been decreased for most of the forms.

An additional twenty + forms have been created( thanks Chobbs!!!) and spread out throughout the life of a characterâ€™s levels. New creatures will be available at levels 40+25 and 40+32, as well as more Avatar forms. We are hoping the additional forms helps ease the pain of those of you who are losing the ability to shift into certain creatures by the scaling change. The newly created forms have some very interesting abilities, such as intercontinental travel and chopping on Lyme. 

Overall, Id like to thank everyone who helped with the project but mostly Chobbs who led the charge. This was a total team effort. 

Please remember there will be many adjustments and bug fixes pertaining to the new changes and forms, as they have not been thoroughly tested yet. Please report any bugs, abuses to one of us. This was a major project with Isabo and myself adjusting much of the shapeshift code, so there will be issues to fix. As well, with Chobbs creation of 20+ new forms, there is bound to be an exploit or two and bug or five that will need to be touched. Please don't be afraid to suggest changes in abilities or stats or simply share a new idea.

The new helpfile is shapeshift creatures. We will be adding much more shapeshift eq and other fun things such as abilities which will be unlocked if a certain item is being worn in form.

Enjoy,

Splork

</div>

<div class="post" data-post-id="31927" data-author="*Chobbs*" data-date="2010-10-24T07:01:39+00:00" data-subject="Re: Shapeshift changes">

Majorish changes:

\- Skills such as crit hit, frenzy, and bloodrage changing after shifting to various forms should be fixed now; those affected, let me know

\- Several forms had their hp inflated too highly due to being saved during futility. Among those are felid, ether worm and raptor; hp readjusted

The rest:

\- Ether worm and manticore stats changed

\- Boar charged fixed, guess who forgot to set a base damage value

\- Sparrows can peck now! 

\- Anoint fixed so that it actually works now! I had forgotten to set a cost!

\- Cobra can shed skin properly now. Seems turning the proc on helps

\- Felid pounce should hit better now. Need to stalk/be unseen prior to combat

\- Felid pounce damage increased a bit; will never be nearly as strong as a stab of a comparable level

\- Numerous message fixes

\- Raptor shriek no longer hits self. Several other area skills might suffer from this too; let me know 

\- Kartazonon stats messed up, thanks Madeline for mentioning this

\- cloak of thorns carrying capacity doubled to 300, since Roku asked so nicely

\- Albatross mana upkeep should be lowered significantly; no more running out of mana mid flight! Hopefully!

To do, probably:

\- Readjust some of the old forms to match new position in forms list

\- A lot of movement values are probably messed up/way too low.

\- Might need to find a way to restrict terrain on forms. Having a shark swim about on land seems... odd

\- Finish forage and feed ability for multiple forms

Keep reporting those bugs!

Chobbs

</div>

<div class="post" data-post-id="31944" data-author="*Splork*" data-date="2010-10-28T18:15:07+00:00" data-subject="Re: Shapeshift changes">

We forgot to mention two more druid enhancements:

1\) The dropping of relatively simple spells, such as detect invisible or darksight, will no longer occur while in form. This should partially correct the complaint regarding having to shapeshift return, cast simple spells, and go back to form. We have not included the more powerful spells such as Sanctuary, Wraithform, etc, as we still expect a strong sense of danger when playing and timing these spells correctly is a large part of this.

2\) Shiftable eq with spell damage and heal bonus eq may now work in form, depending how the form has been coded. Please stay tuned for more information regarding this subject.

Splork

Changes in on reboot

</div>

<div class="post" data-post-id="31966" data-author="*Chobbs*" data-date="2010-11-04T23:44:41+00:00" data-subject="Re: Shapeshift changes">

Mornin' folks,

Most of the old shapeshift forms have been adjusted to closer fit their new positions. 

Honorable mentions/a few changes I remember:

\- Naga damage/hp highly irregular, brought in line with neighboring forms.

Hp lowered, ac increased

\- Owlbear damage/hp highly irregular, brought in line with neighboring forms. Maxmoves abnormally low, doubled them. Hp lowered, ac increased

\- Dragon damage/hp slightly irregular, brought in line with neighboring forms.

Hp lowered, ac increased

\- Elephant ac increased

\- Crocodile ac increased, hp lowered slightly

\- Bat strengthened slightly

\- Wolf, Roc, Griffon greatly enhanced to reflect new positions

\- Mild damage reduction and natural resists added to a few forms here and there

\- Probably a few other minor tweaks here and there. These are probably the big ones.

Haven't had time to add/readjust skills to the older forms yet, will do so at some point in the future.

Chobbs

</div>

<div class="post" data-post-id="32004" data-author="*Chobbs*" data-date="2010-11-12T08:32:07+00:00" data-subject="Re: Shapeshift changes">

Random changes done earlier, reposted here for posterity:

\- Griffons can dive now

\- ALL equus forms can charge now (previously only unicorn couldn't charge)

\- fixed a fairly hilarious bug with charge, both in target acquisition and damage output

Other changes:

\- Elephants can bash/stomp now, probably need to wait for a reboot/crash/the apocalypse

\- Cephalopods can use ink now! Guess who forgot to turn that proc on.

\- Added a smidge of lag to some of the skills; it was never intended for folks to use essentially costless skills three times in a combat round. My mistake and I apologize. Lag should be similar to the normal free actions such as kick or bash now, i.e. one per round/often two, with stronger skills firing once per round. Let me know if any of the skills have too much lag now.

Thanks for the continued bug reports,

Chobbs

</div>

<div class="post" data-post-id="32102" data-author="*Chobbs*" data-date="2010-11-29T00:58:43+00:00" data-subject="Re: Shapeshift changes">

Random changes:

\- Griffon/Raptors should acquire targets and lag pcs properly now, thanks magi for reporting

\- Ether worms should work properly now (well, probably a few weeks ago, but I just remembered to mention it now. Thanks splork for fixing this)

\- Forms should critical hit properly now (old fix from a few weeks ago, just remembered to mention it now. Thank splork again!)

\- Albatross mana consumption lowered again, added messages when taking off/landing, changed other messages (forgot to change them from my rather sarcastic debug messages)

\- Might have fixed a soar bug that caused you to soar indefinitely

Some elucidation:

\- Soar:

Only works if the skies are clear/cloudy (i.e. you can't soar if it's raining/storming or if indoors), so control weather kinda has a function now! (shock!) If the weather changes mid-flight, there is a chance of a slight delay in transit time. Flight time based on continent proximity (e.g. Island/BH takes an average of 3 minutes while AH/Lyme takes a minimum of 4:30 mins). It should not exceed 6:30 minutes in absolute worse case scenario. Still has a high mana cost. 

\- Pounce:

Only works if stalking prior to pouncing, or if the mob cannot see you (i.e. blind or dark room). Fails if the mob has perception or sense-life. And some other minor checks here and there. Follows similar usage rules as backstab/deathgrip/charge.

\- Ether worms:

Permanent wraithform, can hit ethereal mobs. However, cannot hit non-ethereal mobs. Might think of giving them some form of a blast for them at some point.

\- Heightened Smell/Sight:

Uses the commands sniff/farlook respectively, see the corresponding help files for more info.

To do:

\- Still need to rework a few old forms here and there. Eventually.

Thanks for the bug reports. Keep them coming. Back to afk!

Chobbs

</div>

<div class="post" data-post-id="32256" data-author="*Chobbs*" data-date="2011-01-03T07:28:08+00:00" data-subject="Re: Shapeshift changes">

Mornin' folks,

Minor changes:

\- Fixed constrict on cephalopod form (thanks Roku for reporting). Hopefully.

\- A few more message fixes/additions here and there

\- Wolf form can bite properly now (thanks Mercy for reporting)

Chobbs

</div>
