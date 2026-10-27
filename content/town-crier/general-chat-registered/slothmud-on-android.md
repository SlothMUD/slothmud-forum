---
title: "Slothmud on Android"
topic_id: 4873
author: "Driven"
date: 2018-09-11T17:34:49+00:00
last_activity: 2019-05-22T01:19:22+00:00
last_author: "Driven"
sticky: false
locked: false
post_count: 2
---

<div class="post" data-post-id="38973" data-author="Driven" data-date="2018-09-11T17:34:49+00:00" data-subject="Slothmud on Android">

As most of you know I mud most of the time from my phone, so I have spent a fair amount of time figuring out the best way to do exactly that. I used Blowtorch for a long time, but this got quickly replaced by tintin++ once Termux supported the tintin++ package. Here are the basic steps you'll need to get up-and-running with tintin++ on your phone:

1\) Install Termux from Google Play store to emulate a Linux terminal on your phone

 [https://play.google.com/store/apps/details?id=com.termux](https://play.google.com/store/apps/details?id=com.termux)

2\) Launch Termux and enter the following commands

 2a) apt update // generates the list of updates available for Termux

 2b) apt upgrade // updates Termux with the list of updates from the last command

 2c) apt install tintin++ // installs tintin++

3\) Enable data sharing for Termux in the Android settings by toggling Settings\>Apps\>Termux\>Permissions\>Storage to "On"

4\) Go back into Termux app and execute 

 termux-setup-storage // This create the storage directory in your $HOME that gives you a directory structure for your Android internal storage.

5\) Create a simlink for your tintin++ script file in $HOME that points to the internal storage for the Termux app within Android. This links together an easily-accessible script file within Termux and the real location of the file within Android's internal storage that you can edit directly or copy to easily. I manage my tintin++ script file within Ubuntu on my laptop and then copy that same file over to my phone's internal storage in Android/data/com.termux/files/.

 ln -s storage/shared/Android/data/com.termux/files/slothmud.tt .

6\) Create a simlink for your tintin++ log file in $HOME that also points to the internal storage for the Termux app within Android.

 ln -s storage/shared/Android/data/com.termux/files/slothmudLog.html .

7\) On your computer, create your slothmud.tt script file with your editor of choice. Here is a simple one to get you started:

\#SESSION {slothmud} {slothmud.org} {6101}

\#SPLIT {0} {1}

\#CONFIG {LOG} {HTML}

\#LOG {OVERWRITE} {slothmudLog.html}

\####################### VARIABLES #####################################################

\#VAR leader v\_null

\#VAR tank v\_null

\#VAR target v\_null

\#VAR myName \<insertYourCharNameHere\>

\####################### ACTIONS #####################################################

\#ACTION {^You are hungry.} {get food persephone; eat food}

\#ACTION {^You are thirsty.} {#2 drink decanter}

\#ACTION {^$$leader -- 'target %1'} {#var target %1}

\#ACTION {^$$tank yells '%1'} {warcry %1}

\#ACTION {^{.\*} briefly reveals a red aura!} {assist $tank}

\#ACTION {^{.\*} as red tendrils of mist infuse {.\*} body.} {assist $tank}

\####################### ALIASES #####################################################

\#ALIAS {cb} {sing 'echo'; cast 'cure blind' $myName}

\#ALIAS {goargo} {.3esesesenen7es3e2n2enwd}

\#ALIAS {goath} {.3enenene2nw2nw}

\# Speedrun alias

\#ALIAS {^.%0} { #PARSE {%0} {char} {

 \#if {"$char" \>= "0" \&\& "$char" \<= "9"} {#VAR cnt $cnt$char};

 \#elseif {"$cnt" == ""} {$char};

 \#else {#LOOP $cnt 1 cnt {$char}; #var cnt {}}}}

8.) Connect your phone to your laptop with (most likely) a microUSB-to-USB cable that was provided with your phone (most chargers use this cable nowadays). When your phone asks you whether you want to Allow access to your data, select "Allow".

9\) Your phone should now be mounted on your computer, so use your file explorer (WindowsButton-E, for example) and copy your slothmud.tt over to your phone at Android/data/com.termux/files/

10\) Before launching tintin++ for the first time within Termux, I highly recommend you upgrade your phone's keyboard to one that has access to the arrow keys and the tab character. I use Hacker's Keyboard:

 [https://play.google.com/store/apps/details?id=org.pocketworkstation.pckeyboard](https://play.google.com/store/apps/details?id=org.pocketworkstation.pckeyboard)

 10a) After installing Hacker's keyboard, set it as your default keyboard Settings\>General management\>Language and input\>Default keyboard\>Hacker's Keyboard

 10b) Configure Hacker's Keyboard by going into an App that uses the keyboard (which will now use Hacker's Keyboard), and hit the Settings wheel on the keyboard itself. I use the following settings:

 Keyboard height, portrait -\> 40%

 Keyboard mode, portrait -\> 5-row compact layout (US QWERTY only)

11\) Finally, go back into Termux and execute

 tt++ slothmud.tt

12\) You're off and running now. The one flaw that I can see with Termux is the scroll-back feature, and if anyone can figure it out, please let me know. It will scroll back, but whenever the mud outputs text, the screen jumps back down. My solution to this, albeit not a great solution, is to view the slothmudLog.html file in an HTML viewer app in Android. I am using Local HTML Viewer and am moderately happy with it, but I really wish Termux could just freeze scrolling on TTY output.

 [https://play.google.com/store/apps/details?id=com.marcoscg.localhtmlviewer](https://play.google.com/store/apps/details?id=com.marcoscg.localhtmlviewer)

 12a) From above, you'll see that I created a slothmudLog.html simlink to your Android internal storage, so Local HTML Viewer can simply open the file under Android/data/com.termux/files/slothmudLog.html.

</div>

<div class="post" data-post-id="39200" data-author="Driven" data-date="2019-05-22T01:19:22+00:00" data-subject="Re: Slothmud on Android">

After playing in Termux for a year+, I finally figured out that the PageUp keys on the Function menu of Hackers Keyboard enables you to scroll back without being interrupted by MUD output. Oh, happy day!

</div>
