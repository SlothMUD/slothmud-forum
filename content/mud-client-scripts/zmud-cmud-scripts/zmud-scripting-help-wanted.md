---
title: "zmud scripting help wanted"
topic_id: 144
author: "Leizu"
date: 2004-06-02T16:55:31+00:00
last_activity: 2004-07-18T22:51:24+00:00
last_author: "fresh"
sticky: false
locked: false
post_count: 10
---

<div class="post" data-post-id="479" data-author="Leizu" data-date="2004-06-02T16:55:31+00:00" data-subject="zmud scripting help wanted">

I know the string, and need to "analyze" next one. Depends of what following string contains zmud should take different actions.

Let me explain in example:

Leizu is a druid prime. \<- this string comes from the mud and never changes. I need to check next, rigth after this one.

next string may contain 3 variants:

1\. druid \<- zmud should say cool

2\. mage \<- zmud should say comfort

3\. \<- (empty string) zmud should be silent

P.S. atm I use zMUD 4.62

</div>

<div class="post" data-post-id="485" data-author="Weasel" data-date="2004-06-02T19:16:55+00:00" data-subject="Re: zmud scripting help wanted">

I don't use zMUD, but probably works the same way as my client.. or can be adjusted accordingly.. trigger on

```
* is a * prime.
```

which sends %2 to the subroutine script (zMUD has scripting, right?) that says

```
sub Leizuscript (strTriggerName, trig_line, arrWildCards)

 dim class

 class = arrWildCards (1)

 if class = ("druid") then

 World.send "say cool"

 end if

 if class = ("mage") than

 World.send "say comfort"

 end if

end sub
```

or something like that anyway heh

</div>

<div class="post" data-post-id="488" data-author="Leizu" data-date="2004-06-02T20:55:17+00:00" data-subject="">

prolly I gave bad example. I'm not good in coding, so prolly missing something or understand in a wrong way.

those strings are not related anyhow except second goes right after first. hehe.

lets say first string is not 'Leizu is a druid prime', but 'asdfsdfsdfasdfsdfs'.

</div>

<div class="post" data-post-id="491" data-author="Zenkai" data-date="2004-06-02T23:43:24+00:00" data-subject="">

I'm using zMUd 5.55 here.

Lets say mud output is like so:

\<726hp 350ma 177mv\>

cast 'Aegis' Zenkai

You weave the threads of magic masterfully!

You are surrounded by a radiant light.

\<726hp 311ma 177mv\>

And you want to trigger a command if you cast a masterful aegis.

```
trigger:

^~<*hp*ma*mv~>

command:

#var magic 0

trigger:

^You weave the threads of magic masterfully!

command:

#var magic 1

trigger:

^You are surrounded by a radiant light.

command:

#if (@magic = 1) {say Alright! Masterful Aegis!}
```

Is that something like what you want to script?

</div>

<div class="post" data-post-id="499" data-author="Leizu" data-date="2004-06-03T08:11:33+00:00" data-subject="">

thanks Zenkai, I'll keep it in mind. this one might be useful.

btw zmud stores 3 last strings in variables what could be very useful for masterful cast detection. I tried to use it for this case, but empty string didnt let me make it done at first sight.

</div>

<div class="post" data-post-id="1105" data-author="Teron!" data-date="2004-07-17T11:43:15+00:00" data-subject="">

I use ZMud v4.62 too, and Ive solved such a problem this way:

there are two strings: string1 and string2

we need to do something on string2 if it follows string1

the triggers are like this

class: checkstring1

pattern: string1

\#T+ checkstring2;#t- checkstring1

class: checkstring2

pattern: %1

\#IF {%1=@variant1} {command1;#T- checkstring2;#T+ checkstring1};

\#IF {%1=@variant2} {command2;#T- checkstring2;#T+ checkstring1};

\#IF {%1\<\>''} {#T- checkstring2;#T+ checkstring1}

Can turn off the checkstring2 trigger on prompt,

like: Pattern: \<prompt\>, command: #T- checkstring2

I know it looks ugly, it smells bad, but its about to work..similiar code has worked for me..in the recasting spells trigger, I think.

Teron

P.S. ZMud v4.62 is way better than any other version of ZMud.

</div>

<div class="post" data-post-id="1117" data-author="fresh" data-date="2004-07-18T12:11:54+00:00" data-subject="">

Newbies!

There is oÂ­ne easy way to solve the problem, if there are not much variants of second string.

You can set up multiline triggers. It can be done this way:

1st trigger:

Trigger pattern: ^Leizu is a druid prime$^Leizu is a druid

Trigger text: #say cool

2nd trigger:

Trigger pattern: ^Leizu is a druid prime$^Leizu is a mage

Trigger text: #say crap

This is it. It should work oÂ­n zmud 4.62 as well.

</div>

<div class="post" data-post-id="1118" data-author="fresh" data-date="2004-07-18T12:20:55+00:00" data-subject="">

So, in addition to it, if you need to analyze the second string you will write a trigger like this:

^Leizu is a druid prime$^%1$

and you will have all the second string in your %1 variable

</div>

<div class="post" data-post-id="1119" data-author="Leizu" data-date="2004-07-18T14:04:02+00:00" data-subject="">

zmud 4.62 doesnt support multiline triggers, newbie :)

</div>

<div class="post" data-post-id="1123" data-author="fresh" data-date="2004-07-18T22:51:24+00:00" data-subject="">

Hehe, my fault, my memory is playing tricks with me, was using zmud 4.62 too long ago. Then i suppose Terons triggers should be working fine.

</div>
