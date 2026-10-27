---
title: "Dynamic World Map"
topic_id: 2227
author: "Fenyang"
date: 2006-12-21T18:30:40+00:00
last_activity: 2006-12-21T18:30:40+00:00
last_author: "Fenyang"
sticky: false
locked: false
post_count: 1
---

<div class="post" data-post-id="15707" data-author="Fenyang" data-date="2006-12-21T18:30:40+00:00" data-subject="Dynamic World Map">

Here is a global where alias using the 'Dynamic World Map' on the website-

```
#alias worldmap {

#script {strHTML = ~"~"}

#script {Sub GetWorldMap:Set objHTTP = CreateObject~(~"MSXML2.ServerXMLHTTP~"):objHTTP.Open ~"GET~", ~"http:~/~/www.slothmud.org/eqlist/dynmaps/mapserver.html~", ~"FALSE~":objHTTP.Send:strHTML = objHTTP.ResponseText:Set objHTTP = Nothing:End Sub}

#script {Sub FormatWorldMap:intX = instr~(strHTML, ~"~<div area~"):intY = instr~(strHTML, ~"~</body~>~"):intZ = intY - intX:strHTML = mid~(strHTML, intX, intZ~):strHTML = Replace~(strHTML, ~" area=~" & chr~(34~), ~"~>~" & chr~(10~) & ~"%ansi(6)~"):strHTML = Replace~(strHTML, chr~(34~) & ~" icon=~", ~":~<~"):Set objRegExp = New Regexp:objRegExp.Global = True:objRegExp.Pattern = ~"~<(.|n)+?>~":strHTML = objRegExp.Replace~(strHTML, ~"~"):objRegExp.Pattern = ~"\n(\n|$)~":strHTML = objRegExp.Replace~(strHTML, ~"~"):objRegExp.Pattern = ~":\n~":strHTML = objRegExp.Replace~(strHTML, ~":%ansi(7) ~"):Set objRegExp = Nothing:End Sub}

#mss {GetWorldMap}

#mss {FormatWorldMap}

#if (%1 = %null) {#show %mss(strHTML)} {#show %replace(%mss(strHTML),%proper(%1),%ansi(3)%proper(%1)%ansi(7))}}
```

Tis useful to help find dead players... or check if a zone if being cycled.

The script uses vbscript, so you need to check 'allow vbscript' under preferences for it to run.

commands-

worldmap

worldmap \<keyword to color\>

example-

Pathways of Thordfalan: Valanthe

Bal Harbor Town: Taji

Bal Harbor Town: Lob

Bal Harbor Town: Ramoth

Bal Harbor Town: Brand

Bal Harbor Town: Thumper

Duergar Caverns: Marge

Duergar Caverns: Bit

Valkyre Guilds: Faleral

Here is the basic vbscript for other clients that use the language-

```
strHTML = ""

Sub GetWorldMap

 Set objHTTP = CreateObject("MSXML2.ServerXMLHTTP")

 objHTTP.Open "GET", "http://www.slothmud.org/eqlist/dynmaps/mapserver.html", "FALSE"

 objHTTP.Send:strHTML = objHTTP.ResponseText

 Set objHTTP = Nothing

End Sub

Sub FormatWorldMap

 intX = instr(strHTML, "<div area")

 intY = instr(strHTML, "</body>")

 intZ = intY - intX

 strHTML = mid(strHTML, intX, intZ)

 strHTML = Replace(strHTML, " area=" & chr(34), ">" & chr(10))

 strHTML = Replace(strHTML, chr(34) & " icon=", ":<")

 Set objRegExp = New Regexp

 objRegExp.Global = True

 objRegExp.Pattern = "<(.|n)+?>"

 strHTML = objRegExp.Replace(strHTML, "")

 objRegExp.Pattern = "\n(\n|$)"

 strHTML = objRegExp.Replace(strHTML, "")

 objRegExp.Pattern = ":\n"

 strHTML = objRegExp.Replace(strHTML, ": ")

 Set objRegExp = Nothing

End Sub

GetWorldMap

FormatWorldMap

WScript.Echo strHTML
```

</div>
