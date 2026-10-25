---
title: "Communcation filtering popups with colorized output"
topic_id: 2381
author: "Rosher"
date: 2007-03-06T07:19:04+00:00
last_activity: 2007-03-06T07:19:04+00:00
last_author: "Rosher"
sticky: false
locked: false
post_count: 1
---

<div class="post" data-post-id="17183" data-author="Rosher" data-date="2007-03-06T07:19:04+00:00" data-subject="Communcation filtering popups with colorized output">

I want to have all grouptells, gossips etc in separate windows. It is simple to implement, but the strings being filtered are stripped of ansi color codes - so it looks all grey and boring. Below is the script that filters communications to separate windows and saves ansi colors so they look there as they look in the main mud window

(P.S. Darn, i was gonna post screenshot, but sadly no hosting i have access to and I`m to lazy to find and deal with free one  :oops: )

[code:3f608fv0]

#defgroup {stringlog}

#alias  {assignrl} {#var recline %1} {G|stringlog} {T|WT}

#script  {persi} {using System;\r\nusing System.Windows.Forms;\r\nusing System.Text.RegularExpressions;\r\n\r\nusing ScriptEngine;\r\n//css_reference ScriptEngine.dll;\r\n\r\n/** CATEGORIES:\r\n *  ==========\r\n *    1. YouGrouptell\r\n *    2. Grouptells\r\n *    3. YouGossip\r\n *    4. Gossips\r\n *    5. YouNewbie\r\n *    6. Newbies\r\n *    7. YouSay\r\n *    8. Says\r\n *    9. YouShout\r\n *   10. Shouts\r\n *   11. CTalk\r\n *   12. KTalk\r\n *   13. YouAuction\r\n *   14. Auctions\r\n *   15. YouTell\r\n *   16. TellsYou\r\n */\r\n\r\npublic class Script : WintinScript\r\n{\r\n	protected class RxDesc\r\n	{\r\n		public RxDesc()\r\n		{\r\n			\r\n		}\r\n		public RxDesc(Regex aRx, string aSendTo)\r\n		{\r\n			rx = aRx;\r\n			sendTo = aSendTo;\r\n		}\r\n		public Regex rx;\r\n		public string sendTo;\r\n	};\r\n	private static string directMsgWnd = "direct";\r\n	private static string indirectMsgWnd = "indirect";\r\n	private static RxDesc rxYouGrouptell = new RxDesc(new Regex("^You grouptell: \\'.*\\'$", RegexOptions.Compiled), directMsgWnd);\r\n	private static RxDesc rxGrouptells   = new RxDesc(new Regex("^.* -- \\'.*\\'$", RegexOptions.Compiled), directMsgWnd);\r\n	private static RxDesc rxYouGossip    = new RxDesc(new Regex("^You gossip-- \\'.*\\'$", RegexOptions.Compiled), indirectMsgWnd);\r\n	private static RxDesc rxGossips      = new RxDesc(new Regex("^.* gossips-- \\'.*\\'$", RegexOptions.Compiled), indirectMsgWnd);\r\n	private static RxDesc rxYouNewbie    = new RxDesc(new Regex("^You newbie-- \\'.*\\'$", RegexOptions.Compiled), indirectMsgWnd);\r\n	private static RxDesc rxNewbies      = new RxDesc(new Regex("^.* newbies-- \\'.*\\'$", RegexOptions.Compiled), indirectMsgWnd);\r\n	private static RxDesc rxYouSay       = new RxDesc(new Regex("^You say \\'.*\\'$", RegexOptions.Compiled), directMsgWnd);\r\n	private static RxDesc rxSays         = new RxDesc(new Regex("^.* says \\'.*\\'$", RegexOptions.Compiled), directMsgWnd);\r\n	private static RxDesc rxYouShout     = new RxDesc(new Regex("^You shout \\'.*\\'$", RegexOptions.Compiled), directMsgWnd);\r\n	private static RxDesc rxShouts       = new RxDesc(new Regex("^.* shouts \\'.*\\'$", RegexOptions.Compiled), directMsgWnd);\r\n	private static RxDesc rxCTalkKTalk   = new RxDesc(new Regex("^.*> \\'.*\\'$", RegexOptions.Compiled), directMsgWnd);\r\n	private static RxDesc rxYouAuction   = new RxDesc(new Regex("^You auction-- \\'.*\\'$", RegexOptions.Compiled), directMsgWnd);\r\n	private static RxDesc rxAuctions     = new RxDesc(new Regex("^.* auctions-- \\'.*\\'$", RegexOptions.Compiled), directMsgWnd);\r\n	private static RxDesc rxYouTell      = new RxDesc(new Regex("^You tell .* \\'.*\\'$", RegexOptions.Compiled), directMsgWnd);\r\n	private static RxDesc rxTellsYou     = new RxDesc(new Regex("^.* tells you \\'.*\\'$", RegexOptions.Compiled), directMsgWnd);\r\n	\r\n	private void DoParseFilter(EncodedString et, RxDesc rxd)\r\n	{\r\n		if (rxd.rx.IsMatch(et.ClearText))\r\n		{\r\n			wintin.Interpret("#sendtowin {" + rxd.sendTo + "} {" + et.EncodedText.Trim() + "}\\n");\r\n		}\r\n	}\r\n	public override void Init()\r\n	{\r\n		wintin.ReceivedLine += new Wintin.ReceivedLineEventHandler(rle);\r\n	}\r\n\r\n	private void rle(Object sender, EncodedString et)\r\n	{\r\n		DoParseFilter(et, rxYouGrouptell);\r\n		DoParseFilter(et, rxGrouptells);\r\n		DoParseFilter(et, rxYouGossip);\r\n		DoParseFilter(et, rxGossips);\r\n		DoParseFilter(et, rxYouNewbie);\r\n		DoParseFilter(et, rxNewbies);\r\n		DoParseFilter(et, rxYouSay);\r\n		DoParseFilter(et, rxSays);\r\n		DoParseFilter(et, rxYouShout);\r\n		DoParseFilter(et, rxShouts);\r\n		DoParseFilter(et, rxCTalkKTalk);\r\n		DoParseFilter(et, rxYouAuction);\r\n		DoParseFilter(et, rxAuctions);\r\n		DoParseFilter(et, rxYouTell);\r\n		DoParseFilter(et, rxTellsYou);\r\n		\r\n	}\r\n}\r\n} {G|stringlog} {T|CS}

#variable  {recline} {[0;37mTataru[Clan:The Greedy Clan]> 'test'[1;32;40m} {G|stringlog}

#defgroup {}

[/code:3f608fv0]

Looks kinda twisted, but it does work  :P

</div>
