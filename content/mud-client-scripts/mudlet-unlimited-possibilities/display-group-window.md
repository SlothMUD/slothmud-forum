---
title: "Display Group Window"
topic_id: 5011
author: "cnl"
date: 2021-02-16T07:39:34+00:00
last_activity: 2021-02-16T07:39:34+00:00
last_author: "cnl"
sticky: false
locked: false
post_count: 1
---

<div class="post" data-post-id="39686" data-author="cnl" data-date="2021-02-16T07:39:34+00:00" data-subject="Display Group Window">

Here's an example package of how to display GROUP using MSDP variables.

![](https://raw.githubusercontent.com/wiki/CodeAndLoathing/mudlet-slothmud/images/win_group.png)

[Click here to see the screenshot by itself.](https://raw.githubusercontent.com/wiki/CodeAndLoathing/mudlet-slothmud/images/win_group.png)

Description

Displays current msdp GROUP information in an adjustable container (window).

Container can be dragged, resized, minimized/restored, closed and re-opened and position will persist through Mudlet restarts.

From the Mudlet console you can run the following commands:

If you closed the window and want it to come back

```
lua win_group:show()
```

If you locked the container and want to be able to move/drag/resize it again

```
lua win_group:unlockContainer()
```

If you want to lock the container in place so you don't accidentally move/drag/resize.

```
lua win_group:lockContainer()
```

See for more info on adjustable containers:

 [https://wiki.mudlet.org/w/manual:geyser#Adjustable.Container](https://wiki.mudlet.org/w/manual:geyser#Adjustable.Container)

 [https://www.mudlet.org/geyser/files/geyser/AdjustableContainer.html](https://www.mudlet.org/geyser/files/geyser/AdjustableContainer.html)

Installation

 Download [win\_group.zip](https://github.com/CodeAndLoathing/mudlet-slothmud/releases/latest/download/win_group.zip) from [releases/latest](https://github.com/CodeAndLoathing/mudlet-slothmud/releases/latest)

 Extract win\_group.xml from zip.

 Use Mudlet package manager to install or uninstall the xml file.

 It can be installed as either a package or a module.

</div>
