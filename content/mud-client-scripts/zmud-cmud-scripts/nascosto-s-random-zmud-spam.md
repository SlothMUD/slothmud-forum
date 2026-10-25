---
title: "Nascosto's random zmud spam"
topic_id: 1967
author: "Nascosto"
date: 2006-07-08T22:34:16+00:00
last_activity: 2006-07-10T02:33:03+00:00
last_author: "Nascosto"
sticky: false
locked: false
post_count: 2
---

<div class="post" data-post-id="13380" data-author="Nascosto" data-date="2006-07-08T22:34:16+00:00" data-subject="Nascosto&#x27;s random zmud spam">

It's useful to have color vars defined - makes it easier to use colors

[code:262lbwsa]#VAR c_red {\d02} {_nodef} "Color"

#VAR c_purple {\d06} {_nodef} "Color"

#VAR c_blue {\d05} {_nodef} "Color"

#VAR c_cyan {\d07} {_nodef} "Color"

#VAR c_green {\d03} {_nodef} "Color"

#VAR c_yellow {\d04} {_nodef} "Color"

#VAR c_white {\d08} {_nodef} "Color"

#VAR c_bold {\a02} {_nodef} "Color"

#VAR c_unbold {\a03} {_nodef} "Color"[/code:262lbwsa]

now something simple like this will work -

grouptell [@c_cyan] TEST [@c_white]

*"Allow [] for eval" has to be turned on under zmud preferences to allow this syntax to work

</div>

<div class="post" data-post-id="13404" data-author="Nascosto" data-date="2006-07-10T02:33:03+00:00" data-subject="">

This code is useful for formatting numbers. If you want to use it you'll have to save it to a text file and import text, else I think zmud will evalutate it at creation and make useless functions.

[code:3ib2gvem]#VAR numFormat {%if(%1<1000,%1,%if(%1<1000000,[@deciSHR([%1/100],K)],%if(%1<1000000000,[@deciSHR([%1/100000],M)],[@deciSHR([%1/100000000],B)])))} {_nodef} "Functions"

#VAR deciSHR {%concat( %left( %1, %len( %1)-1), ".", %right( %1, %len( %1)-1), %2)} {_nodef} "Functions"

[/code:3ib2gvem]

examples

[@numFormat(123)]

123

[@numFormat(12345)]

12.3K

[@numFormat(123456789)]

123.4M

[@numFormat(1234567890)]

1.2B

</div>
