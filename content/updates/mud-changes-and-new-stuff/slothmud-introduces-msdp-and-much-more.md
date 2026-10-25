---
title: "SlothMUD introduces MSDP and much more"
topic_id: 3992
author: "*Splork*"
date: 2013-01-01T23:12:20+00:00
last_activity: 2013-01-01T23:12:20+00:00
last_author: "*Splork*"
sticky: false
locked: false
post_count: 1
---

<div class="post" data-post-id="33883" data-author="*Splork*" data-date="2013-01-01T23:12:20+00:00" data-subject="SlothMUD introduces MSDP and much more">

This project started around September of 2011 and I can finally say that it is nearing the  end.  For the most part, our old protocol code has been ripped out and replaced by Kavirâ€™s protocol code, which can be found at [http://www.mudbytes.net/file-2811](http://www.mudbytes.net/file-2811) .  Because our MUD has been ahead of the curve in regards to most protocols, removing our old code and replacing it with something entirely different has been extremely difficult and time consuming.  

     Some of the new features available are:

 MSDP & ATCP support:  These are out-of-band protocols and allow us to invisibly send variables and their values to clients. Please see help MSDP and help ATCP for more information regarding what variables we use.  This gives our players an easy way to update their variables, stats, icons, energy bars without having to trigger off in-game data such as prompts, room entries, or score.  It also allows those with clients such as Mushclient or Mudlet to build incredible GUI interfaces.  Please check out Mud Client section under our website navigation for information regarding this topic. 

Clients which currently support MSDP are:

Tintin and Wintin++,  Mudlet,  Mushclient,  Cmud/Zmud, FMud, DecafMud, and TinyFugue( which was coded by our very own Harik and available on our website). There are plenty of starter scripts available for most of these clients on their home pages. ( Detailed instructions for Mushclient and TinyFugue can be found under Mud Clients on our home page )

I have also added ATCP and MSDP to settings command.

Ability to use extended colours: I will post regarding this ability in the near future...

Unicode support: Allows us to embed Unicode characters within regular ASCII strings. This might be nice for future in-game maps.

Sound Support: Provides an extremely simple mechanism for sending sounds via MSDP or ATCP.  This is something we worked on long ago but never finished. We will need to compile a sound pack and go from there.

</div>
