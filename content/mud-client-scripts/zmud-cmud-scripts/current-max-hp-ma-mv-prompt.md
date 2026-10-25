---
title: "Current / Max HP MA MV Prompt"
topic_id: 669
author: "Strago"
date: 2004-12-09T00:16:01+00:00
last_activity: 2004-12-09T00:16:01+00:00
last_author: "Strago"
sticky: false
locked: false
post_count: 1
---

<div class="post" data-post-id="3242" data-author="Strago" data-date="2004-12-09T00:16:01+00:00" data-subject="Current / Max HP MA MV Prompt">

Thanks go out to Nascosto for giving me the basic script, I just added the color.

This script will give you a prompt in the format

<20[/color:3ul6lou1]/100[/color:3ul6lou1]hp 50[/color:3ul6lou1]/100[/color:3ul6lou1]ma 80[/color:3ul6lou1]/80[/color:3ul6lou1]mv>

I found it very useful.

[code:3ul6lou1]

-- Trigger 1

Pattern: <&%d{hp}hp &%d{ma}ma &%d{mv}mv>

Value:

@dhp = 4

#if (@hp > @maxhp*25/100) {@dhp = 6}

#if (@hp > @maxhp*90/100) {@dhp = 2}

@dma = 4

#if (@ma > @maxma*25/100) {@dma = 6}

#if (@ma > @maxma*90/100) {@dma = 2}

@dmv = 4

#if (@mv > @maxmv*25/100) {@dmv = 6}

#if (@mv > @maxmv*90/100) {@dmv = 2}

#sub {%ansi(7)<%ansi(@dhp)[@hp]%ansi(7)/%ansi(@dhp)[@maxhp]%ansi(7)hp %ansi(@dma)[@ma]%ansi(7)/%ansi(@dma)[@maxma]%ansi(7)ma %ansi(@dmv)[@mv]%ansi(7)/%ansi(@dmv)[@maxmv]%ansi(7)mv>}

--Trigger 2

Pattern: ^You have %d~(&%d{maxhp}~) hit, %d~(&%d{maxma}~) mana and %d~(&%d{maxmv}~) movement points.

Value: Leave Blank[/code:3ul6lou1]

With these triggers everytime you check your score the max values get updated. The values for color changing is:

Less than 25% is Red

Less than 90% is Olive

Greater than 90% is Green

Good luck with the script.

</div>
