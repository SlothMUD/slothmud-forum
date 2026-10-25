---
title: "MSDP error in large groups"
topic_id: 4533
author: "Dandelo"
date: 2015-11-01T02:57:25+00:00
last_activity: 2015-11-01T04:53:11+00:00
last_author: "Filk"
sticky: false
locked: false
post_count: 2
---

<div class="post" data-post-id="36131" data-author="Dandelo" data-date="2015-11-01T02:57:25+00:00" data-subject="MSDP error in large groups">

Not that it happens a lot, but it should be noted and maybe fixed. During the ridiculously large group this morning for the quest (thanks Idjit), I noticed that the GROUP variable in MSDP could only handle 27 or 28 members then it locked up and didn't update. I dropped link and reconnected to see if it was an error on my end, but the GROUP variable was empty. After the quest was over, the group shrunk down to 26 or 27 again and the GROUP variable starting updating again.

GROUP output after it stopped updating:

```
#show $MSDP_GROUP
{MEMBER100}{{CLASS}{Ma}{HITPOINTS}{925}{LEVELS}{6.24}{MANA}{646}{MAX_HITPOINTS}{925}{MAX_MANA}{719}{MAX_MOVES}{303}{MOVdai}{POSITION}{Back}{STATUS}{Standing}}{MEMBER101}{{CLASS}{Wa}{HITPOINTS}{1192}{LEVELS}{5.31}{MANA}{{1192}{MAX_MANA}{446}{MAX_MOVES}{326}{MOVES}{326}{NAME}{Jex}{POSITION}{Back}{STATUS}{Standing}}{MEMBHITPOINTS}{478}{LEVELS}{0.20}{MANA}{143}{MAX_HITPOINTS}{478}{MAX_MANA}{143}{MAX_MOVES}{184}{MOVES}{1{POSITION}{Back}{STATUS}{Standing}}{MEMBER103}{{CLASS}{Cl}{HITPOINTS}{818}{LEVELS}{5.33}{MANA}{775}{{MAX_MANA}{782}{MAX_MOVES}{348}{MOVES}{348}{NAME}{Crumbs}{POSITION}{Front}{STATUS}{Standing}}{MEMBERTPOINTS}{1388}{LEVELS}{9.40}{MANA}{477}{MAX_HITPOINTS}{1388}{MAX_MANA}{619}{MAX_MOVES}{467}{MOVES}{3OSITION}{Leader}{STATUS}{Standing}}{MEMBER79}{{CLASS}{Wa}{HITPOINTS}{1145}{LEVELS}{6.35}{MANA}{459}{}{MAX_MANA}{566}{MAX_MOVES}{378}{MOVES}{378}{NAME}{Taron}{POSITION}{Front}{STATUS}{Standing}}{MEMBERPOINTS}{1040}{LEVELS}{4.29}{MANA}{379}{MAX_HITPOINTS}{1040}{MAX_MANA}{396}{MAX_MOVES}{355}{MOVES}{35OSITION}{Back}{STATUS}{Standing}}{MEMBER81}{{CLASS}{Wa}{HITPOINTS}{1546}{LEVELS}{9.40}{MANA}{170}{MAMAX_MANA}{403}{MAX_MOVES}{422}{MOVES}{411}{NAME}{War}{POSITION}{Point}{STATUS}{Standing}}{MEMBER82}{TS}{907}{LEVELS}{9.40}{MANA}{840}{MAX_HITPOINTS}{907}{MAX_MANA}{1011}{MAX_MOVES}{354}{MOVES}{354}{NAN}{Back}{STATUS}{Standing}}{MEMBER83}{{CLASS}{Mo}{HITPOINTS}{1060}{LEVELS}{6.37}{MANA}{528}{MAX_HITPNA}{528}{MAX_MOVES}{387}{MOVES}{387}{NAME}{Ip}{POSITION}{Back}{STATUS}{Standing}}{MEMBER84}{{CLASS}{}{LEVELS}{6.30}{MANA}{391}{MAX_HITPOINTS}{1377}{MAX_MANA}{467}{MAX_MOVES}{420}{MOVES}{420}{NAME}{Stint}{STATUS}{Standing}}{MEMBER85}{{CLASS}{Ma}{HITPOINTS}{612}{LEVELS}{3.35}{MANA}{716}{MAX_HITPOINTS}}{MAX_MOVES}{253}{MOVES}{253}{NAME}{Tinx}{POSITION}{Back}{STATUS}{Standing}}{MEMBER86}{{CLASS}{Ma}{HELS}{9.40}{MANA}{917}{MAX_HITPOINTS}{1046}{MAX_MANA}{1088}{MAX_MOVES}{309}{MOVES}{309}{NAME}{SurfnazSTATUS}{Standing}}{MEMBER87}{{CLASS}{Dr}{HITPOINTS}{861}{LEVELS}{9.40}{MANA}{1222}{MAX_HITPOINTS}{96MAX_MOVES}{419}{MOVES}{419}{NAME}{Dr}{POSITION}{Front}{STATUS}{Standing}}{MEMBER88}{{CLASS}{Ma}{HITP{3.36}{MANA}{773}{MAX_HITPOINTS}{730}{MAX_MANA}{788}{MAX_MOVES}{274}{MOVES}{274}{NAME}{Aaz}{POSITIONnding}}{MEMBER89}{{CLASS}{Mo}{HITPOINTS}{941}{LEVELS}{4.31}{MANA}{557}{MAX_HITPOINTS}{941}{MAX_MANA}5}{MOVES}{365}{NAME}{Raphael}{POSITION}{Front}{STATUS}{Standing}}{MEMBER90}{{CLASS}{Th}{HITPOINTS}{1MANA}{458}{MAX_HITPOINTS}{1174}{MAX_MANA}{458}{MAX_MOVES}{487}{MOVES}{475}{NAME}{Reality}{POSITION}{ding}}{MEMBER91}{{CLASS}{Mo}{HITPOINTS}{911}{LEVELS}{4.28}{MANA}{504}{MAX_HITPOINTS}{911}{MAX_MANA}{}{MOVES}{346}{NAME}{Slovic}{POSITION}{Front}{STATUS}{Standing}}{MEMBER92}{{CLASS}{Wa}{HITPOINTS}{112NA}{519}{MAX_HITPOINTS}{1133}{MAX_MANA}{528}{MAX_MOVES}{337}{MOVES}{317}{NAME}{Ozzy}{POSITION}{Front}{MEMBER93}{{CLASS}{Wa}{HITPOINTS}{1581}{LEVELS}{9.40}{MANA}{548}{MAX_HITPOINTS}{1581}{MAX_MANA}{579OVES}{422}{NAME}{Stun}{POSITION}{Front}{STATUS}{Standing}}{MEMBER94}{{CLASS}{Ba}{HITPOINTS}{956}{LEV5}{MAX_HITPOINTS}{936}{MAX_MANA}{590}{MAX_MOVES}{312}{MOVES}{312}{NAME}{Singerzoh}{POSITION}{Back}{SEMBER95}{{CLASS}{Wa}{HITPOINTS}{1037}{LEVELS}{3.39}{MANA}{382}{MAX_HITPOINTS}{1037}{MAX_MANA}{498}{MS}{309}{NAME}{Zlodiak}{POSITION}{Front}{STATUS}{Standing}}{MEMBER96}{{CLASS}{Th}{HITPOINTS}{425}{LEV8}{MAX_HITPOINTS}{425}{MAX_MANA}{208}{MAX_MOVES}{234}{MOVES}{234}{NAME}{Risky}{POSITION}{Back}{STATUR97}{{CLASS}{Cl}{HITPOINTS}{1082}{LEVELS}{9.40}{MANA}{839}{MAX_HITPOINTS}{1082}{MAX_MANA}{1056}{MAX_323}{NAME}{Zuzu}{POSITION}{Front}{STATUS}{Standing}}{MEMBER98}{{CLASS}{Ba}{HITPOINTS}{969}{LEVELS}{4_HITPOINTS}{988}{MAX_MANA}{624}{MAX_MOVES}{350}{MOVES}{350}{NAME}{Sochi}{POSITION}{Front}{STATUS}{St{CLASS}{Dr}{HITPOINTS}{405}{LEVELS}{0.20}{MANA}{362}{MAX_HITPOINTS}{405}{MAX_MANA}{362}{MAX_MOVES}{1E}{Babo}{POSITION}{Back}{STATUS}{Standing}}
```

GROUP after I dropped link and reconnected:

```
#show $MSDP_GROUP
$MSDP_GROUP
```

Thanks,

Stilgar

</div>

<div class="post" data-post-id="36132" data-author="Filk" data-date="2015-11-01T04:53:11+00:00" data-subject="Re: MSDP error in large groups">

Noticed and bugged the same thing. Seems its not my client related only.

</div>
