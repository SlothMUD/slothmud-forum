---
title: "VOTE SLOTH Helper Script"
topic_id: 5000
author: "cnl"
date: 2020-12-30T19:56:27+00:00
last_activity: 2020-12-30T19:56:27+00:00
last_author: "cnl"
sticky: false
locked: false
post_count: 1
---

<div class="post" data-post-id="39652" data-author="cnl" data-date="2020-12-30T19:56:27+00:00" data-subject="VOTE SLOTH Helper Script">

Displays a large clickable banner on login or reconnect reminding you to vote for SlothMUD if it has been more than 12 hours since you last clicked the banner.

Clicking should launch a seperate browser window making it easy to vote quickly without the hassle of trying to remember when you last voted.

If installed as a module (instead of a package) on multiple profiles it will track a single last voted time across all of them.

Currently this package only has an entry for TMS since it looks like TMC has been defunct for a year with no sign of being fixed.

![](https://github.com/CodeAndLoathing/mudlet-slothmud/wiki/images/vote.png)

**Installation**

    1. Download [vote.zip](https://github.com/CodeAndLoathing/mudlet-slothmud/releases/latest/download/vote.zip) from releases/latest

    2. Extract vote.xml from zip.

    3. Use Mudlet package manager to install or uninstall the xml file.

    4. It can be installed as either a package or a module.

    If you play multiple game characters each in their own profile it is recommended to install it as a module for each of those characters profiles instead of a package.

    The difference is that packages (and the last voted data) are specific to a profile and modules can remember a single last voted time across multiple profiles.

    To install as a module put the XML in a folder outside your profiles - you could create a new folder called modules for example, and then use the package manager dropdown to launch module manager and install from that location. You will want to do this from each of your active profiles.

see also <LINK_TEXT text="https://github.com/CodeAndLoathing/mudl ... /wiki/vote">https://github.com/CodeAndLoathing/mudlet-slothmud/wiki/vote</LINK_TEXT>

</div>
