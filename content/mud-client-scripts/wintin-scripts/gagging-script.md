---
title: "Gagging Script"
topic_id: 2665
author: "Reece"
date: 2007-12-11T06:01:33+00:00
last_activity: 2007-12-13T02:31:25+00:00
last_author: "Reece"
sticky: false
locked: false
post_count: 3
---

<div class="post" data-post-id="21619" data-author="Reece" data-date="2007-12-11T06:01:33+00:00" data-subject="Gagging Script">

For all the people I know who've always wanted to Gag people. (especially me hehe) Here ya go.

\#defgroup Brogag

\#alias {brogagon} #ac {^Bro tells you '%1'} {G\|Brogag}

\#action {Bro tells you '%1'} {#enable Brogag}

\#gag {Bro -- '%1'} {G\|Brogag}

\#gag {Bro tells you '%1'} {G\|Brogag}

\#gag {Bro says '%1'} {G\|Brogag}

\#gag {Bro gossips-- '%1'} {G\|Brogag}

\#gag {Bro auctions-- '%1'} {G\|Brogag}

\#gag {Bro newbies-- '%1'} {G\|Brogag}

\#gag {Bro[\~dragonsworn\~]\> '%1'} {G\|Brogag}

\#gag {Bro quests-- '%1'} {G\|Brogag}

\#gag {Bro whispers to you, '%1'} {G\|Brogag}

\#gag {Bro yells '%1'} {G\|Brogag}

\#gag {Bro shouts '%1'} {G\|Brogag}

\#gag {Bro giggles.} {G\|Brogag}

\#gag {Bro smiles.} {G\|Brogag}

\#gag {Bro slaps you.} {G\|Brogag}

You can replace Bro with $charname to gag anyone you choose. Hope ya have fun, Enjoy <img src="/images/smilies/icon_e_smile.svg" alt=":)" title=":)" width="15" height="15" class="smiley nozoom">

</div>

<div class="post" data-post-id="21624" data-author="Blastem" data-date="2007-12-11T15:28:07+00:00" data-subject="">

Should really anchor those actions with a ^.

\#action {^Bro tells you '%1'} {#enable Brogag} 

Just a word to the wise anchoring any of your actions/triggers that can be will save a ton of troubleshooting later.

</div>

<div class="post" data-post-id="21654" data-author="Reece" data-date="2007-12-13T02:31:25+00:00" data-subject="">

aight sweet thanks for the tip <img src="/images/smilies/icon_e_smile.svg" alt=":)" title=":)" width="15" height="15" class="smiley nozoom">

</div>
