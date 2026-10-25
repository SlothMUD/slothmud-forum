---
title: "VK Autoquest bug"
topic_id: 3950
author: "raincrab"
date: 2012-10-27T10:07:58+00:00
last_activity: 2012-10-27T10:07:58+00:00
last_author: "raincrab"
sticky: false
locked: false
post_count: 1
---

<div class="post" data-post-id="33684" data-author="raincrab" data-date="2012-10-27T10:07:58+00:00" data-subject="VK Autoquest bug">

I showed this to juggleblood a week ago or so, he said it was setup right, but probably a bug in the code.  I poked around a bit more with it, came up with this cyclical conversation:

```
> ask azra about quests

You ask Azra, the cartographer about 'quests'.
Azra, the cartographer tells you 'I need some help completing my map collection...'
Azra, the cartographer tells you 'Since you mention it,'
Azra, the cartographer tells you 'there is one more thing you could help me with!'
Azra, the cartographer tells you 'I offer the quest 'map_of_burbalangs' for 25000 gold pieces.'
You ask Azra, the cartographer about 'quests'.

> ask azra about map_of_burbalangs

You ask Azra, the cartographer about 'map_of_burbalangs'.
Azra, the cartographer tells you 'I don't have a map of the newly'
Azra, the cartographer tells you 'discovered area of catwalks that hangs below Newbatia...'
Azra, the cartographer tells you 'if you would fully explore that area and then come back to'
Azra, the cartographer tells you 'tell me about it, I would be most grateful!  I'm only a poor'
Azra, the cartographer tells you 'mapmaker, but I could pay you 500 gold, and I'm sure the'
Azra, the cartographer tells you 'experience would benefit an adventurer such as yourself!'

> undertake map_of_burbalangs

Azra, the cartographer tells you 'Sadly, you aren't eligible for this quest because you must 
    first complete 'map_of_mines''

> undertake map_of_mines

Azra, the cartographer tells you 'Sadly, you aren't eligible for this quest because you must 
    first complete 'map_collection''

> undertake map_collection

Azra, the cartographer tells you 'You don't need to sign up, just do it!'

> ask azra about map_collection

You ask Azra, the cartographer about 'map_collection'.
Azra, the cartographer tells you 'I don't have a map of the newly'
Azra, the cartographer tells you 'discovered area of catwalks that hangs below Newbatia...'
Azra, the cartographer tells you 'if you would fully explore that area and then come back to'
Azra, the cartographer tells you 'tell me about it, I would be most grateful!  I'm only a poor'
Azra, the cartographer tells you 'mapmaker, but I could pay you 500 gold, and I'm sure the'
Azra, the cartographer tells you 'experience would benefit an adventurer such as yourself!'
```

Back to where we started.

</div>
