---
title: ".: Website Changes :."
topic_id: 3221
author: "*Breeze*"
date: 2009-08-08T01:20:55+00:00
last_activity: 2011-12-12T17:43:07+00:00
last_author: "*Breeze*"
sticky: false
locked: false
post_count: 15
---

<div class="post" data-post-id="29787" data-author="*Breeze*" data-date="2009-08-08T01:20:55+00:00" data-subject=".: Website Changes :.">

The Dynamic World Map has been skinned to match the rest of the website.

The EQ List and Maproom are in the process of being redone also. (read as, if you see something weird in the maproom its probably because I am working on it.

</div>

<div class="post" data-post-id="29788" data-author="Rigwarl" data-date="2009-08-08T03:47:14+00:00" data-subject="">

I am glad they are being updated, however i have a small request.

Previously, the gwhere trigger for zmud would show a players location perfectly, however now it seems to show

The Mines of Moria" continent=": Wimpy

What happened :)

-Rig

</div>

<div class="post" data-post-id="29789" data-author="*Breeze*" data-date="2009-08-08T09:41:37+00:00" data-subject="">

I am glad they are being updated, however i have a small request.

Previously, the gwhere trigger for zmud would show a players location perfectly, however now it seems to show

The Mines of Moria" continent=": Wimpy

What happened :)

-Rig[/quote:1khyiq7f]

thats part of a feature being added.  i disabled it for now til the feature is done.

link me to the gwhere script and will see if it can be updated (otherwise i search for it later)

</div>

<div class="post" data-post-id="29790" data-author="Rigwarl" data-date="2009-08-08T12:44:43+00:00" data-subject="">

Here's the code I'm using

[code:1tlu260s]#script {strHTML = ~"~"}

#script {Sub GetWorldMap:Set objHTTP = CreateObject~(~"MSXML2.ServerXMLHTTP~"):objHTTP.Open ~"GET~", ~"http:~/~/www.slothmud.org/eqlist/dynmaps/mapserver.html~", ~"FALSE~":objHTTP.Send:strHTML = objHTTP.ResponseText:Set objHTTP = Nothing:End Sub}

#script {Sub FormatWorldMap:intX = instr~(strHTML, ~"~<div area~"):intY = instr~(strHTML, ~"~</body~>~"):intZ = intY - intX:strHTML = mid~(strHTML, intX, intZ~):strHTML = Replace~(strHTML, ~" area=~" & chr~(34~), ~"~>~" & chr~(10~) & ~"%ansi( green)~"):strHTML = Replace~(strHTML, chr~(34~) & ~" icon=~", ~":~<~"):Set objRegExp = New Regexp:objRegExp.Global = True:objRegExp.Pattern = ~"~<(.|n)+?>~":strHTML = objRegExp.Replace~(strHTML, ~"~"):objRegExp.Pattern = ~"\n(\n|$)~":strHTML = objRegExp.Replace~(strHTML, ~"~"):objRegExp.Pattern = ~":\n~":strHTML = objRegExp.Replace~(strHTML, ~":%ansi( yellow) ~"):Set objRegExp = Nothing:End Sub}

#mss {GetWorldMap}

#mss {FormatWorldMap}

#show {%ansi( red)Global Where}

#if (%1 = %null) {#show %mss( strHTML)} {#show %replace( %mss( strHTML), %proper( %1), %ansi( red)%proper( %1)%ansi( red))}[/code:1tlu260s]

</div>

<div class="post" data-post-id="29791" data-author="Jag" data-date="2009-08-08T18:25:24+00:00" data-subject="">

Very Cool.  I use the website a lot and appreciate your working on it.

</div>

<div class="post" data-post-id="29793" data-author="*Breeze*" data-date="2009-08-10T00:08:09+00:00" data-subject="">

Very Cool.  I use the website a lot and appreciate your working on it.[/quote:2es0nntg]

Not a problem :) I enjoy it.

 - Fixed a bug where clan names / titles with certain characters in them were not showing up on the "Who's Online" section of the website.

 - Various Cartography section changes.  *too many to list*

</div>

<div class="post" data-post-id="29794" data-author="Rigwarl" data-date="2009-08-11T18:45:12+00:00" data-subject="">

It's been mislabeled for a while but the cartography section incorrectly shows 2 maps.

Mercurial woods map [AH] leads to a map of Murkwood [SS] and vice versa.

-Rig

</div>

<div class="post" data-post-id="29797" data-author="*Breeze*" data-date="2009-08-12T20:34:25+00:00" data-subject="">

It's been mislabeled for a while but the cartography section incorrectly shows 2 maps.

Mercurial woods map [AH] leads to a map of Murkwood [SS] and vice versa.

-Rig[/quote:if7ilkdr]

Fixed! thanks :)

</div>

<div class="post" data-post-id="29837" data-author="*Breeze*" data-date="2009-08-16T11:51:24+00:00" data-subject="">

Modified :)

[code:1fj6727u]

#script {strHTML = ~"~"}

#script {Sub GetWorldMap:Set objHTTP = CreateObject~(~"MSXML2.ServerXMLHTTP~"):objHTTP.Open ~"GET~", ~"http:~/~/www.slothmud.org/support/mapserver.php~", ~"FALSE~":objHTTP.Send:strHTML = objHTTP.ResponseText:Set objHTTP = Nothing:End Sub}

#script {Sub FormatWorldMap:intX = instr~(strHTML, ~"~<div area~"):intY = instr~(strHTML, ~"~</body~>~"):intZ = intY - intX:strHTML = mid~(strHTML, intX, intZ~):strHTML = Replace~(strHTML, ~" area=~" & chr~(34~), ~"~>~" & chr~(10~) & ~"%ansi( 6)~"):strHTML = Replace~(strHTML, chr~(34~) & ~" icon=~", ~":~<~"):strHTML = Replace~(strHTML, chr~(34~) & ~" continent=~" & chr~(34~), ~" on ~"):Set objRegExp = New Regexp:objRegExp.Global = True:objRegExp.Pattern = ~"~<(.|n)+?>~":strHTML = objRegExp.Replace~(strHTML, ~"~"):objRegExp.Pattern = ~"\n(\n|$)~":strHTML = objRegExp.Replace~(strHTML, ~"~"):objRegExp.Pattern = ~":\n~":strHTML = objRegExp.Replace~(strHTML, ~":%ansi( 7) ~"):Set objRegExp = Nothing:End Sub}

#mss {GetWorldMap}

#mss {FormatWorldMap}

#if (%1 = %null) {#show %mss( strHTML)} {#show %replace( %mss( strHTML), %proper( %1), %ansi( 3)%proper( %1)%ansi( 7))}

[/code:1fj6727u]

</div>

<div class="post" data-post-id="31591" data-author="*Breeze*" data-date="2010-08-25T13:21:04+00:00" data-subject="Re: .: Website Changes :.">

This is old-ish, but I don't think I posted it anywhere..

On the menu, if you choose

   Configure Site >> Store Menu State

it will cause the menu to remember which items you had open and reopen them for you after you click them.

(it wont collapse all nodes on page-load)

   Configure Site >> Forget Menu State

turns this feature off.

</div>

<div class="post" data-post-id="31946" data-author="*Breeze*" data-date="2010-10-30T13:04:33+00:00" data-subject=".: Website Changes :.">

upgraded forum. let me know if you see any odd behaviour

</div>

<div class="post" data-post-id="32983" data-author="*Breeze*" data-date="2011-11-15T20:38:00+00:00" data-subject="Re: .: Website Changes :.">

New link on left side menu: WebCVS

http://www.slothmud.org/index.php?module=WebCVS

this is updated weekly, each Sunday and shows the CVS logs from the previous

week.

</div>

<div class="post" data-post-id="33086" data-author="*Breeze*" data-date="2011-12-12T14:50:08+00:00" data-subject="New Mount &#x27;An Mystica Map">

New map submitted by Alris

<LINK_TEXT text="http://www.slothmud.org/wiki/maproom/Ly ... tica_b.jpg">http://www.slothmud.org/wiki/maproom/Ly_Mount_%27An_Mystica_b.jpg</LINK_TEXT>

</div>

<div class="post" data-post-id="33087" data-author="Slowdraw" data-date="2011-12-12T16:08:28+00:00" data-subject="Re: .: Website Changes :.">

Hmm. This seems like as suitable places as any, so I guess I'll post it here. I found a couple of nonfunctional website links. The big one is that the MUSHclient plugin on the menu tree doesn't find the file and redirects to the site map. The other one is on the site map. Both the eqlist link in the equipment information section and the find book or manual link in the class abilities section try to link to [http://www.slothmud.org/www.slothmud.org/eqlist/](http://www.slothmud.org/www.slothmud.org/eqlist/) instead of [http://www.slothmud.org/index.php?module=EQList](http://www.slothmud.org/index.php?module=EQList) and end up redirecting back to the site map.

</div>

<div class="post" data-post-id="33089" data-author="*Breeze*" data-date="2011-12-12T17:43:07+00:00" data-subject="Re: .: Website Changes :.">

> **Slowdraw wrote:**
> Hmm. This seems like as suitable places as any, so I guess I'll post it here. I found a couple of nonfunctional website links. The big one is that the MUSHclient plugin on the menu tree doesn't find the file and redirects to the site map. The other one is on the site map. Both the eqlist link in the equipment information section and the find book or manual link in the class abilities section try to link to [http://www.slothmud.org/www.slothmud.org/eqlist/](http://www.slothmud.org/www.slothmud.org/eqlist/) instead of [http://www.slothmud.org/index.php?module=EQList](http://www.slothmud.org/index.php?module=EQList) and end up redirecting back to the site map.

+ Removed MUSHClient plugin link (until splork finishes/reuploads)

+ Redirected eqlist links to [http://www.slothmud.org/eqlist](http://www.slothmud.org/eqlist) on sitemap

Thanks for reporting

</div>
