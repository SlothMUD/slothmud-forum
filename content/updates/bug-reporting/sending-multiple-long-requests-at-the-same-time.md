---
title: "Sending multiple long requests at the same time"
topic_id: 4546
author: "Dragoth"
date: 2015-11-28T11:44:59+00:00
last_activity: 2015-11-29T17:59:23+00:00
last_author: "*Splork*"
sticky: false
locked: false
post_count: 6
---

<div class="post" data-post-id="36212" data-author="Dragoth" data-date="2015-11-28T11:44:59+00:00">

Hey guys, I found an interesting issue you can test for yourself

==============================================================================================

If you are using Zmud or Cmud, type #loop 50 {say %i blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda}

==============================================================================================

If you are using Mudlet make an alias with any name and pattern blabla

in code window put:

for i=1,50 do

send ("say "..i.. " blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda")

end

and type blabla to activate it

==============================================================================================

This basically sends 50 lines of say command with a serial number and blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda after it. 

This line isn't long enough to be truncated by the mud, but because it gets spammed to the mud 50 times, the mud seemingly decides to do weird things with it, like reporting only the first few lines and then a few last ones, or it can report only the first one, or only the few last ones, or the commands won't go through at all and sometimes it will report absolutely fine.

This issue was already raised with an Immortal staff yesterday, but wasn't tested properly and resulted in dismissal. Since i was using Cmud and Immortal was using Wintin, it was suggested that it was Cmud issue, but it turns out that it's not.

==============================================================================================

Here are some logs if you don't want to test anything yourself, these are only one example out of many, as i said sometimes it reports fine, other times you get weird response like below, sometimes after the command is executed and your client sends the request, the mud just completely ignores your input.

CMUD:

#loop 50 {say %i blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda} 

<906hp 931ma 369mv>say 1 blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 2 blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 3 blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 4 blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 5 blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 6 blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 7 blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 8 blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 9 blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 10 blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 11 blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 12 blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 13 blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 14 blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 15 blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 16 blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 17 blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 18 blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 19 blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 20 blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 21 blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 22 blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 23 blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 24 blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 25 blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 26 blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 27 blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 28 blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 29 blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 30 blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 31 blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 32 blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 33 blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 34 blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 35 blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 36 blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 37 blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 38 blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 39 blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 40 blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 41 blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 42 blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 43 blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 44 blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 45 blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 46 blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 47 blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 48 blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 49 blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 50 blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

You say '1 blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda' 

Arglebargle, glop-glyf!?! 

You say '47 blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda' 

You say '48 blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda' 

You say '49 blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda' 

You say '50 blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda'

==============================================================================================

Here is Mudlet

blabla 

say 1 

blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 2 

blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 3 

blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 4 

blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 5 

blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 6 

blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 7 

blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 8 

blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 9 

blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 10 

blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 11 

blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 12 

blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 13 

blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 14 

blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 15 

blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 16 

blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 17 

blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 18 

blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 19 

blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 20 

blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 21 

blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 22 

blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 23 

blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 24 

blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 25 

blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 26 

blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 27 

blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 28 

blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 29 

blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 30 

blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 31 

blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 32 

blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 33 

blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 34 

blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 35 

blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 36 

blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 37 

blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 38 

blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 39 

blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 40 

blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 41 

blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 42 

blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 43 

blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 44 

blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 45 

blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 46 

blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 47 

blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 48 

blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 49 

blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

say 50 

blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslkjfdslfkjslsadasda 

Arglebargle, glop-glyf!?! 

<906hp 927ma 369mv> 

You say '36 

blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslk 

jfdslfkjslsadasda' 

<906hp 927ma 369mv> 

You say '37 

blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslk 

jfdslfkjslsadasda' 

<906hp 927ma 369mv>You say '38 

blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslk 

jfdslfkjslsadasda' 

<906hp 927ma 369mv> 

You say '39 

blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslk 

jfdslfkjslsadasda' 

<906hp 927ma 369mv> 

You say '40 

blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslk 

jfdslfkjslsadasda' 

<906hp 927ma 369mv>You say '41 

blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslk 

jfdslfkjslsadasda' 

<906hp 927ma 369mv> 

You say '42 

blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslk 

jfdslfkjslsadasda' 

<906hp 927ma 369mv> 

You say '43 

blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslk 

jfdslfkjslsadasda' 

<906hp 927ma 369mv>You say '44 

blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslk 

jfdslfkjslsadasda' 

<906hp 927ma 369mv> 

You say '45 

blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslk 

jfdslfkjslsadasda' 

<906hp 927ma 369mv> 

You say '46 

blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslk 

jfdslfkjslsadasda' 

<906hp 927ma 369mv>You say '47 

blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslk 

jfdslfkjslsadasda' 

<906hp 927ma 369mv> 

You say '48 

blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslk 

jfdslfkjslsadasda' 

<906hp 927ma 369mv> 

You say '49 

blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslk 

jfdslfkjslsadasda' 

<906hp 927ma 369mv>You say '50 

blablablalafljsdkfsdlkfjsdflkdsjflksjfslkfjsdlfjsdlfsjfdslkfjslfjsklfjsdlfjslfjsfklsjflsjfslkfjsdfslk 

jfdslfkjslsadasda' 

<906hp 927ma 369mv>

</div>

<div class="post" data-post-id="36213" data-author="Yasik" data-date="2015-11-28T11:52:42+00:00">

What is in-game situation that will require to say long string 50 times?

</div>

<div class="post" data-post-id="36214" data-author="Dragoth" data-date="2015-11-28T12:13:31+00:00">

Yasik, this post has nothing to do with you, it's not about you and judging from your post it's obviously not about anything that concerns you in any way, if this is the case, do you really have to forcefully insert your opinions that  have no importance and franky, no-one really cares about ?

Yes it's an obscure problem, but it affects some of us and some of us want to know why it's happening and whether its something that can be easily solved, or something that we have to live with and work around. And i am sure that any immortal with access to the code and an even a tiny bit of curiosity in them, will find it interesting enough to take a look at.

</div>

<div class="post" data-post-id="36219" data-author="Yasik" data-date="2015-11-29T10:25:47+00:00">

You can say that this post 'is not about you' to anyone who reads it. Why not send personal email instead of making it public?

</div>

<div class="post" data-post-id="36220" data-author="Dragoth" data-date="2015-11-29T11:47:39+00:00">

This is a bug and it's posted in the bugs section of the forum, what is the problem here exactly ?

Are you against people reporting bugs ?

</div>

<div class="post" data-post-id="36222" data-author="*Splork*" data-date="2015-11-29T17:59:23+00:00">

I'd like to know if this same bug is seen in other older MUDS such as Godwars, Realms of Despair, or another older popular DIKU.

I haven't even glanced at the code but my best guess is that this has something to do with MCCP or our input buffer. The majority of older muds all used the same MCCP snippet and then customized it for their own games which is why I ask the above question. 

This really isn't an issue because its easily bypassed by adding a tiny bit of lag between each communication which most likely wouldn't even be noticeable by either party. I'd rather see our coders spending their time on something important that affects the majority of our players, especially when this can be fixed quite easily by the player adding less than 10 characters of code  but I am sure one of us will look into it eventually!

@Yasik

He did speak with me personally about this both online and via forums!

</div>
