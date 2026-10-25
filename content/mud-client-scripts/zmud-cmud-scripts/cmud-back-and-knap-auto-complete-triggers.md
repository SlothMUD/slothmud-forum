---
title: "CMUD: back and knap auto-complete triggers"
topic_id: 3422
author: "Gladavar"
date: 2010-05-12T09:20:19+00:00
last_activity: 2010-05-12T18:29:42+00:00
last_author: "Vixn"
sticky: false
locked: false
post_count: 2
---

<div class="post" data-post-id="31150" data-author="Gladavar" data-date="2010-05-12T09:20:19+00:00">

Copy the code below into a text editor and save as a .xml file  then use CMUD's import option in the package editor to import into your session package.

I am currently using 3.17 and have not tested on any previous versions but it should work fine.

```
<class name="containers" id="430">
  <trigger type="Command Input" priority="4310" id="431">
    <pattern>^(*) knap$</pattern>
    <value>%replace(%1~ knap,knap,knapsack)
</value>
  </trigger>
  <trigger type="Command Input" priority="4320" id="432">
    <pattern>^(*) back$</pattern>
    <value>%replace(%1~ back,back,backpack)</value>
  </trigger>
</class>
```

What's it do?  Anything you send to the mud that ends in the words back or knap will be auto-completed for you  saving those four extra keystrokes.

get barrel back = get barrel backpack

L in knap = L in knapsack

The pattern is anchored so if you don't want a line ending in back or knap to be completed simply end with a punctuation or space and it won't be.

I don't have anything but noob containers to use it with right now but you could easily add to the class to suit your needs.

</div>

<div class="post" data-post-id="31151" data-author="Vixn" data-date="2010-05-12T18:29:42+00:00">

Well done, Gladavar.

Now try this:

{I use a golden-sack from centaur merchant. It's a good & stylish container.}

#al getr {rem @robe;get @junk-sack @robe;get %1 @junk-sack;put @junk-sack @robe;wear @robe}

#al putr {rem  @robe;get @junk-sack @robe;put %1 @junk-sack;put @junk-sack @robe;wear @robe}

junk-sack=golden-sack (or whatever are you using)

I also improved this aliases to use it in different modes, i.e. for different robes in regen_mode, ac_mode etc. 

p.s. All credits go to Falca, the famous fief.

Have a good scripts!

Vixn.

</div>
