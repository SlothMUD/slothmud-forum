---
title: "MSDP and Mushclient/Mudlet and few other clients"
topic_id: 3799
author: "*Splork*"
date: 2011-09-28T21:54:58+00:00
last_activity: 2012-08-12T02:26:14+00:00
last_author: "Tuck"
sticky: false
locked: false
post_count: 12
---

<div class="post" data-post-id="32940" data-author="*Splork*" data-date="2011-09-28T21:54:58+00:00">

I have been working on MSDP lately, it is a mud protocol which can be found at [http://tintin.sourceforge.net/msdp/](http://tintin.sourceforge.net/msdp/)

With the help of Kavir, from Godwars2( http://www.godwars2.org ), we have the protocol fully functioning and running on one of our test ports.  kavir has also created a few generic GUIs with both Mudlet and Mushclient to go with the protocol. I've tweaked the Mushclient one quite a bit and the results are as follows:

http://www.slothmud.org/images/splork/v2.5%20MC.PNG

The idea is that each player can create an atmosphere which they enjoy playing the game with. Some people like more of a graphical feel and may use this or the flash client we developed last year. Some people will stick with their regular clients with tons of windows and popups. To each his own but we will be supplying quite a bit more data to you guys, what you do with it is your choice.

I will keep everybody updated in regards to this project.

Splork

</div>

<div class="post" data-post-id="32947" data-author="Breezewood" data-date="2011-10-13T13:54:14+00:00">

Is this info now available in WinTin?

</div>

<div class="post" data-post-id="32949" data-author="*Splork*" data-date="2011-10-15T00:09:10+00:00">

WinTin, the windows versin of TinTin does use MSDP also, I believe.

Wintin.NET is hopefully going to be having the protocol added relatively soon.

Fmud, which is what our flash based client is based off of, has just released a new version which supports both MXP and MSDP. The information can be found at [http://bc-dev.net/2011/10/12/fmud-1-0-alpha-release/](http://bc-dev.net/2011/10/12/fmud-1-0-alpha-release/)

The majority of the information will also be available through MXP, but there is some information which can not be sent back and forth using the protocol. The clients which support only MXP will be in the same position as those players now who don't have access to MXP, regarding the extra information available for triggers, variables, etc.

Kavir ( as mentioned in the previous post ) has provided the MUD community with a protocols snippet. This snippet adds support for TTYPE, NAWS, MSDP, ATCP, MSSP, MSP and MXP, as well as UTF-8 (using CHARSET) and XTerm 256 colors.

<LINK_TEXT text="http://www.topmudsites.com/forums/mud-c ... ippet.html">http://www.topmudsites.com/forums/mud-coding/6418-gui-snippet.html</LINK_TEXT>

For the most part, SlothMUD has had most of this since Sept 25, 2005. 

<LINK_TEXT text="http://www.slothmud.org/forum/viewtopic ... 8824#p8824">http://www.slothmud.org/forum/viewtopic.php?f=26&t=1463&p=8824#p8824</LINK_TEXT>

We even have a command, thanks to Isabo, which shows us which players are using certain clients and what protocols these clients and players have access to. 

With the help of Kavir's snippet and kavir himself, we have meshed together our old protocols code and his snippet to add a few more options to our game.  Once added, we will support MSDP, ATCP, and UTF-8, to go along with the others which we already had. 

Splork

</div>

<div class="post" data-post-id="33344" data-author="*Splork*" data-date="2012-06-27T18:26:32+00:00">

This project was put on hold for quite some time due to work, life, children, yadda, yadda, but we are back on track.

I've extended the variables greatly, we are sending just about anything you can think of, at this time over 110 different variables will be automatically updated by your client, if it supports msdp.

We have been working on a script for CMUD, which might work for the newer versions of Zmud also.

Breeze has put together a sample script which looks like this, showing % hps for tank, opponent, etc etc.

[http://www.slothmud.org/images/splork/cmud_msdp_v1.PNG](http://www.slothmud.org/images/splork/cmud_msdp_v1.PNG)

Stun has been working on the test port also for Tintin users.

I already have a working mushclient plugin, thanks to kavir from Godwars2.

Mudlet can also be used with msdp to create a really nice graphical interface.

Hopefully, we can get this in-game in the next week or so.

I realize the majority of our players are wintin.net users and I am busy trying to get this taken care of. A couple of players are attempting to work with the wintin code currently, hopefully they will succeed. If not, we will figure something out, but rest assured, it will have msdp as well...

Enjoy,

Splork

</div>

<div class="post" data-post-id="33345" data-author="Stark" data-date="2012-06-27T19:42:06+00:00">

Woohoo!  Thanks, Splork!  I've been waiting on this as an excuse to wipe my scripts and start from scratch.  

A couple questions (because I'm excited and can't just wait and find out): When you say it will show % hp for opponent, is that the same data as the web client gets?  Will we also get raw hp numbers of opponent? (1348/2048 hp)  Are there any other pieces of new data that we'll be able to get via MSDP?

Now I just need to get myself a new laptop that works.

P.S.- It looks like you've got quite a load of drachma you're carrying around.  I'd be more than happy to lighten your load a bit.  :P  I'm also a bit sad we don't get a glimpse at the room description for Splork's Abode.

</div>

<div class="post" data-post-id="33346" data-author="*Splork*" data-date="2012-06-27T21:20:19+00:00">

Exact hit points of opponents will not be shown and those of you spoofing the flash client will not be able to once this protocol goes in-game. Hp % is just that, you will get a % that the mob, tank, etc is alive. If you see 77, it means he is 77% health, etc.

For more information on what variables will be set, please check help msdp in-game.

Splork

"MSDP" "MSDP PROTOCOL"

See Also: MXP MSP MSSP TELNET

MUD servers often want to send additional data to a MUD client that doesn't necessarily

need to be displayed, as well as needing a way to identify clients that support out-of-band data.

The MUD Server Data Protocol seeks to address these issues by providing a transparant and straight

forward out-of-band protocol for MUD servers to send variables and their values to MUD clients that

can be both generic, and specific for the MUD in question. Using generic variables will allow

generic client interface scripts that work on all MSDP MUDs.

The following clients support MSDP: tintin++, wintin++, mushclient, mudlet, fmud, decafmud, and cmud/zmud.

Soon there will be a forum on the website, including plugin support and instructions on how to setup

some of the above mentioned clients to work with MSDP. These can make for some pretty powerful graphically

oriented GUIs.

The following variables are currently set by Slothmud. If you wish additional variables, please

send request to splork@slothmud.org

          SERVERID

         WORLDTIME

         CHARACTERNAME

         LEVEL

         CLASS

         HEALTH

         HEALTHMAX

         MANA

         MANAMAX

         MOVEMENT

         MOVEMENTMAX

         AC

         HONOR

         DRACHMA

         ALIGNMENT

         EXPERIENCE

         MONEY

         STR

         CON

         DEX

         WIS

         INT

         STRPERM

         CONPERM

         DEXPERM

         WISPERM

         INTPERM

         HITROLL

         DAMROLL

         OPPONENTHEALTH

         OPPONENTHEALTHMAX

         OPPONENTLEVEL

         OPPONENTNAME

         AREANAME

         ROOMNAME

         ROOMVNUM

         TERRAIN

         CONTINENT

         WEAPONDAM,

         WEAPON_DAM,

         STAB_DAM,                               

         STAB_DAM_CAP,

         UNDEAD_CONT,

         UNDEAD_CONT_CAP,

         SPELL_BONUS,

        SPELL_BONUS_CAP,

        HEAL_BONUS,

        HEAL_BONUS_CAP,

        CHARISMA,

        CHARISMA_CAP,

        FLAILDAM,                         

        KICKDAM,

        HAND_DAM,

        HAND_DAM_CAP,

        DAM_RED,

        DAM_RED_CAP,

        SEX,

        GROUP_LEADER,

        TANK_HEALTH,

        TANK_HEALTH_MAX,

        TANK_LEVEL,

        TANK_NAME,

        LEVEL_SEC,

        LEVEL_TER,

        LEVEL_QUA,

        LEVEL_QUI,

        LEVEL_HEX,

        LEVEL_SEP,

        LEVEL_OCT,             

        LEVEL_AVA,

        CITIZEN,

        CLASS,

        CLASS_SEC,

        CLASS_TER,

        CLASS_QUA,

        CLASS_QUI,

        CLASS_HEX,

        CLASS_SEP,

        CLASS_OCT,              

        CLASS_AVA,

</div>

<div class="post" data-post-id="33347" data-author="Stark" data-date="2012-06-27T22:07:33+00:00">

Thanks for clarifying and for the list of variables.

Am I correct in thinking that we will be given the exact max hp number from the OPPONENTHEALTHMAX variable, and so we can figure the current hp of the mob down to 2 significant digits using the % from OPPONENTHEALTH?

Having the OPPONENTLEVEL and OPPONENTNAME are nice additions to have, and seem straight forward on how to use them.  

I assume TERRAIN will tell you whether you're underwater/flying/on the ground, etc?

And is ROOMVNUM a room's unique ID number or something like that?

Everything else seem to be standard values.

</div>

<div class="post" data-post-id="33354" data-author="Tuck" data-date="2012-06-30T20:11:34+00:00">

Confirmed to work with Cmud 3.34. 

Good job, Rickster.

</div>

<div class="post" data-post-id="33397" data-author="Magi" data-date="2012-07-26T14:03:38+00:00">

Anxiously awaiting news that MSDP is on the live server, and that it works in Wintin.Net :)

</div>

<div class="post" data-post-id="33401" data-author="*Splork*" data-date="2012-07-26T22:11:47+00:00">

The main coding port has been down for close to two weeks. Ive contacted Jake and once its brought back up I can commit and add MSDP.

MSDP is currently not working with wintin.net but a few different people are trying to add the feature. Hopefully it will get done... 

MSDP works with Mushclient, Mudlet, CMUD, Zmud, tintin, and one of our players has recently finished an update to TinyFugue which has this feature. He will be adding it relatively soon to the Mudbytes site.

</div>

<div class="post" data-post-id="33416" data-author="harik" data-date="2012-08-02T16:36:12+00:00">

> ***Splork* wrote:**
> MSDP works with Mushclient, Mudlet, CMUD, Zmud, tintin, and one of our players has recently finished an update to TinyFugue which has this feature. He will be adding it relatively soon to the Mudbytes site.

Actually I ended up putting the code on github since I do all my work in git anyway.   This should work for everybody except windows, and even then anyone who could build normal tinyfugye5 for windows should be able to build this.

[https://github.com/harikattar/tinyfugue5-msdp](https://github.com/harikattar/tinyfugue5-msdp)

Todo: testing on live server, documenting the /msdp command.

Hit me up in-game (harik/kirah) with any questions.  I also have a fairly large collection of useful scripts for sloth, including in-game item property tags.

</div>

<div class="post" data-post-id="33440" data-author="Tuck" data-date="2012-08-12T02:26:14+00:00">

*BUMP* for MSDP on LIVE server.

</div>
