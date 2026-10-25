---
title: "Example on Formatting numbers"
topic_id: 5038
author: "cnl"
date: 2021-11-04T06:33:42+00:00
last_activity: 2021-11-04T06:33:42+00:00
last_author: "cnl"
sticky: false
locked: false
post_count: 1
---

<div class="post" data-post-id="39861" data-author="cnl" data-date="2021-11-04T06:33:42+00:00">

Some folks were saying that they had a hard time reading numbers in sloth sometimes.

I find it handy to format them into shorter form and color coding them makes it much more useful.

https://postimg.cc/6yVdV46W

Here's a function i use to format numbers for cecho 

```
u = u or {}
function u.formatNumColor(n)
  if n >= 10^10 then
    return string.format("<dark_violet>%.0f<purple>B<reset>", n / 10^9)
  elseif n >= 10^9 then
    return string.format("<dark_violet>%.1f<purple>B<reset>", n / 10^9)
  elseif n >= 10^7 then
    return string.format("<steel_blue>%.0f<deep_sky_blue>M<reset>", n / 10^6)
  elseif n >= 10^6 then
      return string.format("<steel_blue>%.1f<deep_sky_blue>M<reset>", n / 10^6)
  elseif n >= 10^4 then
      return string.format("<forest_green>%.0f<lime_green>K<reset>", n / 10^3) 
  elseif n >= 10^3 then
      return string.format("<forest_green>%.1f<lime_green>K<reset>", n / 10^3)
  elseif n >= 10^2 then
      return string.format("<ansi_yellow>%.0f<reset>", n) 
  else 
      return string.format("<ansi_yellow>%.1f<reset>", n)
  end      
end
```

Here's how I would use the function in the image example from above using perl regex triggers

https://postimg.cc/Xpr8wYGX

</div>
