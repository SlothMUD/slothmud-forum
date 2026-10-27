---
title: "Searching Books at a Book Drop"
topic_id: 3709
author: "celerra7"
date: 2011-04-29T17:51:32+00:00
last_activity: 2011-04-29T17:51:32+00:00
last_author: "celerra7"
sticky: false
locked: false
post_count: 1
---

<div class="post" data-post-id="32573" data-author="celerra7" data-date="2011-04-29T17:51:32+00:00" data-subject="Searching Books at a Book Drop">

My crude attempt to search the books. Not necessarily clean, but it is effective:

```
<class name="Script - SearchBooks" id="532">
 <alias name="searchbooks" id="533">
 <value>;reset script variables
#FORALL @book_list {#VAR book_temp %pop(@book_list)}
#FORALL @book_found {#VAR book_temp %pop(@book_found)}
#VAR book_found_count 0
#VAR book_list_count 0
#VAR book_spell ""
#VAR book_temp ""
;turn of MXP Exit info so it is not added to the books to be examined
MXPEXITS off
#Wait 1000
;turn on the MXP book capture trigger
#T+ mxp_books
#Wait 500
;feed the MXP book capture trigger by sending a LOOK command to mud
Look
#Wait 2500
;turn MXP book capture trigger off
#T- mxp_books
#Wait 500
;turn the MXP Exit info back on
MXPEXITS on
#Wait 1000
;determine the count of books that need to be examined and announce it
#VAR book_list_count %numitems(@book_list)
;#SHOW @book_list
#SA
#SA Searching @book_list_count Books...
#SA
#SEND
#WAIT 1000
;turn on the Examine Book triggers to capture info on books needing read
#T+ Search_Books1
#T+ Search_Books2
#T+ Search_Books3
;start loop to examine all the books in the room 
#LOOP %numitems(@book_list) 
 {
;pull a book form the list to examine
 #VAR book_temp %pop(@book_list)
 Examine @book_temp
;wait for the MUD to return info on the book
 #WAITFOR {You see the words} 3500 {#WAIT 500} {#WAIT 1000}
 }
;turn the Examine Book triggers off
#T- Search_Books1
#T- Search_Books2
#T- Search_Books3
;retrieve a count of books to read and announce it
#VAR book_found_count %numitems(@book_found)
#SA
#SA Search complete. @book_list_count books processed, and @book_found_count found:
#SA
;display all books needed from the book_found list
#FORALL @book_found {#SA %pop(@book_found)}
#WAIT 1000
#SEND
;End of Script</value>
 </alias>
 <trigger name="mxp_books" type="MXP" priority="2520" enabled="false" id="534">
 <pattern><SEND href=</pattern>
 <value>$book_datapos = %match(%mxp,data=)
$book_temp1 = %left(%mxp,($book_datapos-3))
$book_hrefpos = %match($book_temp1,href=)
$book_temp2 = %right($book_temp1,($book_hrefpos+10))
$book_bar = %match($book_temp2,"|")
$book_temp3 = %left($book_temp2,($book_bar-1))
#IF ($book_temp3 != "") {#ADDITEM book_list $book_temp3}</value>
 <notes>Associated ONLY with Alias SEARCHBOOKS</notes>
 </trigger>
 <trigger name="Search_Books2" priority="5350" enabled="false" id="535">
 <pattern>You haven't learnt anything from this book.</pattern>
 <value>#ADDITEM book_found %concat(@book_temp," - '",@book_spell,"'")</value>
 </trigger>
 <trigger name="Search_Books3" priority="5350" enabled="false" id="536">
 <pattern>You can still learn more from this book.</pattern>
 <value>#ADDITEM book_found %concat(@book_temp," - '",@book_spell,"'")</value>
 </trigger>
 <var name="book_list_count" id="537">32</var>
 <var name="book_list" type="StringList" id="538">
 <json>[]</json>
 </var>
 <var name="book_found_count" id="539">0</var>
 <var name="book_found" type="StringList" id="540">
 <json>[]</json>
 </var>
 <var name="book_temp" id="541">spellbook-dissolved-aque-bragh</var>
 <trigger name="Search_Books1" priority="6650" enabled="false" id="665">
 <pattern>You see the words '%1' written on the cover.</pattern>
 <value>#VAR book_spell %1</value>
 </trigger>
 <var name="book_spell" id="666">acid blast</var>
</class>
```

Let me know what you think. <img src="/images/smilies/icon_e_smile.svg" alt=":)" title=":)" width="15" height="15" class="smiley nozoom">

</div>
