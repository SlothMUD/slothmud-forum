---
title: "Exp/Gold Tables"
topic_id: 4672
author: "Firk"
date: 2016-09-16T07:59:14+00:00
last_activity: 2016-09-16T18:46:32+00:00
last_author: "Teron"
sticky: false
locked: false
post_count: 2
---

<div class="post" data-post-id="37353" data-author="Firk" data-date="2016-09-16T07:59:14+00:00">

I made some scripts for TamperMonkey on Chrome.

This one aligns the row number with the row data:

    jQuery( "table" ).eq(1).find("td:first").html(" ");

    jQuery( "table" ).eq(5).find("td:first").html(" ");

    jQuery( "table" ).eq(9).find("td:first").html(" ");

This one highlights a row when you mouse over:

            jQuery("table table").find("td:not(:first)").mouseenter( function(){

            var row=jQuery(this).parent("tr").index();

            var col=jQuery(this).parents("td").index();

            jQuery(this).parent().css("background", "#f3f3f3");

            jQuery(this).parents("table").parents("tr").children("td").eq((col+1)%4).find("tr").eq(row).css("background", "#f3f3f3")

            jQuery(this).parents("table").parents("tr").children("td").eq((col+2)%4).find("tr").eq(row).css("background", "#f3f3f3")

            jQuery(this).parents("table").parents("tr").children("td").eq((col+3)%4).find("tr").eq(row).css("background", "#f3f3f3")

        }).mouseleave( function(){

            var row=jQuery(this).parent("tr").index();

            var col=jQuery(this).parents("td").index();

            jQuery(this).parent().css("background", 'transparent');

            jQuery(this).parents("table").parents("tr").children("td").eq((col+1)%4).find("tr").eq(row).css("background", "transparent")

            jQuery(this).parents("table").parents("tr").children("td").eq((col+2)%4).find("tr").eq(row).css("background", "transparent")

            jQuery(this).parents("table").parents("tr").children("td").eq((col+3)%4).find("tr").eq(row).css("background", "transparent")

        });

</div>

<div class="post" data-post-id="37355" data-author="Teron" data-date="2016-09-16T18:46:32+00:00">

How best am I supposed to use it?

Also, I/you can check exp/gold ingame, as well as by using the "level" command.

</div>
