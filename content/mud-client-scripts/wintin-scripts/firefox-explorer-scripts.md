---
title: "Firefox/explorer scripts"
topic_id: 1812
author: "*Splork*"
date: 2006-03-30T01:59:56+00:00
last_activity: 2006-03-30T09:52:46+00:00
last_author: "Nightwolf"
sticky: false
locked: false
post_count: 2
---

<div class="post" data-post-id="11879" data-author="*Splork*" data-date="2006-03-30T01:59:56+00:00">

This will create a window that can bring up anything 

from inside your internet explorer, firefox,etc.

The small example below does the following:

1)creates a windowcalled web

2)creates an action called dynamic_map

   *This takes slothmuds dynamic map and sets it

 right inside wintin.net-inside the window titled web 

so that you can watch players move without opening 

your browser

3)creates an action called whatis. This brings up our eqlist 

right inside wintin.net in the window called web. You can 

search for equipment without opening up your broswer.

#htmlwindow {Web} {about:blank}

#defgroup {Maps}

#alias  {dynamic_map} {#htmlbrowse {Web} {http://www.slothmud.org/eqlist/dynmaps/map.html}} {G|Maps}

#alias  {web_clear} {#clearwin {Web}} {G|Maps}

#alias  {whatis} {#htmlbrowse {Web} {http://www.slothmud.org/eqlist/index.php?stage=3&alternateeqtype=All&orderby=Item+name&sortorder=asc&filterby=Any&filterstring=$0&continent=All&changemonth=01&changedate=01&changeyear=2000&viewflags=View+Only&actionmenu=maproom.php}} {G|Maps}

#defgroup {}

</div>

<div class="post" data-post-id="11886" data-author="Nightwolf" data-date="2006-03-30T09:52:46+00:00">

A question about the mechanics of the connection: Will the browser connect via its own settings (i.e. the proxy settings i put into firefox), or via the direct connection used by the client... (since my non-proxy-bandwith is restricted, I'd need to know that :/ )

Thanks, 

NW

</div>
