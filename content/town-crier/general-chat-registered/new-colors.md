---
title: "new colors"
topic_id: 1976
author: "Weasel"
date: 2006-07-15T04:49:55+00:00
last_activity: 2006-08-12T03:27:14+00:00
last_author: "Weasel"
sticky: false
locked: false
post_count: 3
---

<div class="post" data-post-id="13478" data-author="Weasel" data-date="2006-07-15T04:49:55+00:00" data-subject="new colors">

Thought I'd write this up if anyone's wondering.. Splork recently added a few more color option for us to use in titles, grouptells, gname, whiner scripts etc, but it may have made existing ones change for you.

For the basic in-game settings, use help color:

Use 'color' on its own to turn color support on or off.

Use 'color show' to display your color settings.

Use 'color set' to modify your color settings

Use 'color reset' to reset them to default values.

Until this change, to make colors in grouptells, scripts etc bright or dull you needed to put a \\a02 (bright) or \\a01 (dull) in front of the color codes \\d01 \\d02 etc. Not any more. The bright and dull part is no longer required, which means we can put more in those titles etc when they're limited to 55 characters, and it makes 'coding' them a bit easier too. The new codes I have are:

standard or dull colors:

d01 - standard white

d02 - dark red

d03 - dark green

d04 - dark yellow, aka orange

d06 - dark pink, aka magenta

d07 - cyan, aka dark aqua

d08 - standard white

d12 - grey

d16 dark blue

bright colors:

d05 - medium blue

d09 - bright blue or aqua

d10 - bright yellow

d11 - bright white

d13 - bright green

d14 - bright red

d15 - bright pink

d17 and up seem to be standard white

and that's pretty much it afaik. For the commonly used colors, existing code can be changed as follows (old to new):

\\a02\\d04 = \\d10

\\a02\\d02 = \\d14

\\a02\\d03 = \\d13

\\a02\\d07 = \\d09

\\a02\\d08 = \\d11

PLEASE remember one thing when using color codes: when ending a line of color text, put a \\c02 at the end - this reverts all following text back to whatever the user's default color code is.. otherwise the color can overflow into the next line and mess up people's triggers if they are set to match colors, and generally it's just untidy coding and looks ugly. ..\\c02 works for me anyway.

cheers.

</div>

<div class="post" data-post-id="13479" data-author="Marchessa_red_witch" data-date="2006-07-15T17:31:02+00:00" data-subject="Very helpful">

Thank you.

</div>

<div class="post" data-post-id="13704" data-author="Weasel" data-date="2006-08-12T03:27:14+00:00" data-subject="">

bump

</div>
