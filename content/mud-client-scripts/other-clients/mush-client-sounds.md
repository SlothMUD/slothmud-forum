---
title: "MUSH Client Sounds"
topic_id: 4093
author: "Yasik"
date: 2013-06-02T16:25:48+00:00
last_activity: 2013-06-02T16:25:48+00:00
last_author: "Yasik"
sticky: false
locked: false
post_count: 1
---

<div class="post" data-post-id="34312" data-author="Yasik" data-date="2013-06-02T16:25:48+00:00" data-subject="MUSH Client Sounds">

Hi guys!

I have decided to contribute to this thread as well, so here are my MUSH Client triggers that make you unable to sleep during chop or to warn you when admin talks to you to see if you're botting or not (hi Tuk!).

1\.

```
^(.+) is unable to respond right now\.$
```

Checkboxes: Enable, Keep Evaluating, Regular Expression; Send To: World; Everything else - empty.

Sound: Blood Raven taunt from Diablo 2: [https://dl.dropboxusercontent.com/u/72105811/Blood_Raven_Taunt_2.wav](https://dl.dropboxusercontent.com/u/72105811/Blood_Raven_Taunt_2.wav)

2\. 

```
^(.+) tells you \'(.+)\'(.*)$
```

Checkboxes - same as previous.

Sound: Battlecruiser from StarCraft: [https://dl.dropboxusercontent.com/u/72105811/Starcraft_Battlecruiser_Receiving_Transmission.wav](https://dl.dropboxusercontent.com/u/72105811/Starcraft_Battlecruiser_Receiving_Transmission.wav)

3\.

```
^The \'(aegis|sanctuary|wall of flesh)\' spell on you is about to wear off\.$
```

Checkboxes - same as in first one.

Sound: Bloodlust from Warcraft 2: [https://dl.dropboxusercontent.com/u/72105811/Warcraft_2_Bloodlust.wav](https://dl.dropboxusercontent.com/u/72105811/Warcraft_2_Bloodlust.wav)

4\.

```
^(.+) is unable to respond right now\.$
```

Checkboxes: same + Repeat on same line; Send To: Script; Send: "ActivateClient;".

Not making any sound, but if you browse pron in another window - it will bring MUSH Client in front of you so you can see who's died leaving the channel. Smart!

Enjoy. (c)

</div>
