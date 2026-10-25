---
title: "Auto bash kick broadside and frenzy"
topic_id: 1686
author: "*juggleblood*"
date: 2006-01-27T11:27:21+00:00
last_activity: 2006-01-27T11:27:21+00:00
last_author: "*juggleblood*"
sticky: false
locked: false
post_count: 1
---

<div class="post" data-post-id="10356" data-author="*juggleblood*" data-date="2006-01-27T11:27:21+00:00">

#defgroup {warrior skills}

#alias  {bashoff} {#disable autobash;#showme Bash disabled} {G|warrior skills}

#alias  {bashon} {#enable autobash;#showme Bash enabled} {G|warrior skills}

#alias  {bs} {broadside} {G|warrior skills}

#alias  {bsoff} {#disable autobroadside} {G|warrior skills}

#alias  {bson} {#enable autobroadside} {G|warrior skills}

#alias  {bst} {broadside $target} {G|warrior skills}

#alias  {flall} {flail all} {G|warrior skills}

#alias  {fr} {frenzy} {G|warrior skills}

#alias  {frenzyoff} {#showme Frenzy Off;#alias targ {#var target %0;#showme Target Set To: $0}} {G|warrior skills}

#alias  {frenzyon} {#showme Frenzy On;#alias targ {#ac {hates your guts} {frenzy} {O};#var target %0;#showme Target Set To: $0}} {G|warrior skills}

#alias  {kickoff} {#disable autokick;#showme Autokick Disabled} {G|warrior skills}

#alias  {kickon} {#enable autokick; #showme AutoKick Enabled} {G|warrior skills}

#defgroup {autobash}

#action  {^You attempt to bash} {bash;#showme Bashing} {G|autobash}

#action  {^You charge and bash} {bash;#showme Bashing} {G|autobash}

#defgroup {autobroadside}

#action  {^You use the flat of} {#showme Broadsiding;broadside} {G|autobroadside}

#action  {^Your weapon completely misses} {#showme Broadsiding; broadside} {G|autobroadside}

#defgroup {autokick}

#action  {^You miss your kick} {kick;#showme (Kicking)} {G|autokick}

#action  {^Your beautiful full} {kick;#showme (Kicking)} {G|autokick}

#action  {^Your boots} {kick; #showme (Kicking)} {G|autokick}

#action  {^Your kick} {kick;#showme (Kicking)} {G|autokick}

To use auto frenzy u have to target the mob before u engage it. For groups this means that your leader target action should trigger the alias 'targ %0' rather than setting the target directly thru #var.

Cheers

</div>
