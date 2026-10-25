---
title: "Changelog 2016-02-23"
topic_id: 4594
author: "*teker*"
date: 2016-02-23T15:29:03+00:00
last_activity: 2016-02-23T16:37:08+00:00
last_author: "*teker*"
sticky: false
locked: false
post_count: 2
---

<div class="post" data-post-id="36629" data-author="*teker*" data-date="2016-02-23T15:29:03+00:00">

I rewrote quite a bit of the code involved in casting spells/singing songs so that our builders can create better triggers off of casting/singing.  Hopefully not much is noticeable, but if there are problems casting particular spells, please let me know.  One positive change I made is that bards shouldn't stop singing/playing until the command has been successfully parsed so that cast 'something-I-mispelled' shouldn't stop singing/playing the current song.

I also went through and added keywords to items based on bugs/typos that had been filed.  I don't have the list on me but I got a few of them done.

</div>

<div class="post" data-post-id="36630" data-author="*teker*" data-date="2016-02-23T16:37:08+00:00">

A couple things noticed already:

Keyless entry for the new vaults has actually been broken for a couple days but I just saw it this morning and couldn't get the fix in before the reboot.  It works from outside to inside but not inside out. 

The list of memorized spells may have bad data in it.  If you mem clear or keep memorizing additional spells it should clear itself up.

</div>
