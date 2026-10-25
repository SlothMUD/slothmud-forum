---
title: "Gems/Runes auction house"
topic_id: 4628
author: "Yasik"
date: 2016-04-15T03:24:51+00:00
last_activity: 2016-04-19T21:08:47+00:00
last_author: "*teker*"
sticky: false
locked: false
post_count: 7
---

<div class="post" data-post-id="36839" data-author="Yasik" data-date="2016-04-15T03:24:51+00:00">

Since a big chunk of playerbase always looking to trade gems/runes, maybe its a good idea to provide ingame mechanics for that; BH Jeweller Shop can be a good place for this.

inv

You are carrying:

a Diamond

a Emerald

a Ruby

lots

______________________________________________

Lot #   |     Bidder     |      Wants      |       Offers        |

______________________________________________

    1     |    Splork      |   a Diamond   |       a Ruby       |

______________________________________________

    2    |    Teker       |   a Emerald    | a Rhodocrosite |

______________________________________________

    3    |     Breeze    |   a Jacinth     |     Pink Garnet  |

______________________________________________

bid 2

Jeweller the jeweller takes your a Emerald and hands over a Rhodocrosite to you in exchange.

Then after, Teker issues "check" and Jeweller give him what was exchanged.

inv

You are carrying:

a Diamond

a Rhodocrosite

a Ruby

(Emerald disappeared, Rhodo added instead)

lots

______________________________________________

Lot #   |     Trader     |      Wants      |       Offers        |

______________________________________________

    1     |    Splork      |   a Diamond   |       a Ruby       |

______________________________________________

    3    |     Breeze    |   a Jacinth     |     Pink Garnet  |

______________________________________________

(lot 2 disapperead since transaction was successful)

The exact command not nessesarily must be 'bid' but something else; trade (already used), exchange (already used), need to invite new one that is not in use.

Can extend to Offers two options that work "OR", so when player does "bid 2" they will need to add "op1" or "op2" keywords, like this:

_______________________________________________________________________

Lot #   |     Bidder     |      Wants      |       Offers option 1        |    Offers option 2  |

_______________________________________________________________________

    1     |    Splork      |   a Diamond   |              a Ruby              |      a Malachite     |

_______________________________________________________________________

    2    |    Teker       |   a Emerald    |        a Rhodocrosite        |          a Opal          |

_______________________________________________________________________

    3    |     Breeze    |   a Jacinth     |           Pink Garnet          |         a Zircon         |

_______________________________________________________________________

bid 2 op2

Jeweller the jeweller takes your a Emerald and hands over a Opal to you in exchange.

Can extend even further by adding "Wants" op1 / op2 AND at the same time "Offers" op1 / op2.

This way one player can exchange 2 gems he has to 2 gems he wants, in any combination. Maybe too complex.

As for actually consigning gems, dont have any ideas about how to enumerate gems/runes as we do with prices in coins...

</div>

<div class="post" data-post-id="36841" data-author="Josiah" data-date="2016-04-15T04:11:04+00:00">

You don't have to wait for this to be implemented in game.  Any decent web developer could build a website to facilitate gem trades.  I'd like to think our immorts have more exciting plans for their limited coding time.

If a lot of players use this feature in game, it'll get too long to read.  Next you'll be asking for custom queries and sorting options!

_______________________________________________________________________

Lot # | Bidder | Wants | Offers option 1

_______________________________________________________________________

1 | Josiah | a Star Ruby | a Aventurine

_______________________________________________________________________

2 | Josiah | a Star Ruby | a Black Onyx

_______________________________________________________________________

3 | Josiah | a Star Ruby | a Colorless Sapphire

_______________________________________________________________________

4 | Josiah | a Star Ruby | Emerald

_______________________________________________________________________

5 | Josiah | a Star Ruby | Gray White Diamond

_______________________________________________________________________

6 | Josiah | a Star Ruby | a Jacinth

_______________________________________________________________________

7 | Josiah | a Star Ruby | a Jasper

_______________________________________________________________________

8 | Josiah | a Star Ruby | a Jet

_______________________________________________________________________

9 | Josiah | a Star Ruby | a Light Blue Iolite

_______________________________________________________________________

10 | Josiah | a Star Ruby | a Malachite

_______________________________________________________________________

11 | Josiah | a Star Ruby | a Obsidian

_______________________________________________________________________

12 | Josiah | a Star Ruby | a Pink diamond

_______________________________________________________________________

13 | Josiah | a Star Ruby | a Rhodochrosite

_______________________________________________________________________

14 | Josiah | a Star Ruby | a Rose Quartz

_______________________________________________________________________

15 | Josiah | a Star Ruby | a Ruby

_______________________________________________________________________

16 | Josiah | a Star Ruby | a Sapphire

_______________________________________________________________________

17 | Josiah | a Star Ruby | a Smokey Quartz

_______________________________________________________________________

18 | Josiah | a Star Ruby | a Tiger Eye

_______________________________________________________________________

19 | Josiah | a Star Ruby | a Tomb Jade

_______________________________________________________________________

</div>

<div class="post" data-post-id="36842" data-author="Teron" data-date="2016-04-15T04:36:07+00:00">

I've been contemplating an idea for this trade website for a while, but so far I don't want it to be a separate website, so it has to be done by Breeze for this website, because it uses WordPress (and I prefer Drupal).

And yes, ingame will be too hard to use. Website offers much more and easier functionality to add, search and filter the gems. In fact, the website could mix and match the entire gem database, so more people would get what they want.

P.S. Josiah, no, that's not the way to do it.

Josiah

Needs:

A Star Ruby

Offers:

...

</div>

<div class="post" data-post-id="36843" data-author="Yasik" data-date="2016-04-15T04:58:55+00:00">

Possible solution can be limiting # of lots per player to 5, for example.

Let them to decide what is most important to trade faster, and what can be delayed.

</div>

<div class="post" data-post-id="36851" data-author="Teron" data-date="2016-04-15T06:33:18+00:00">

Yes, preference can be a factor in trading.

I don't see any need to set a limit. Players can store gems and only put gems they want on the market. The more gems there are on the market, the more likely there will be a trade.

Other things to consider:

- an option to sell/buy a gem

- an option to offer eq for trade

- a functionality to notify players, when a match is found

- If it's a circle (ie, the trade involves several people), suggest the time to trade ingame and share it in Google Calender via an export link

- obviously, need a field to specify, when the player is online or make the MUD analyze it and show a graph, like here:

![](http://i.imgur.com/WXTBTEf.png) - that's from theunderminejournal.com for WoW, powered by highcharts.com

What else do players need to trade effectively?

</div>

<div class="post" data-post-id="36857" data-author="*Breeze*" data-date="2016-04-18T03:13:28+00:00">

not completely on topic but...

1) the fact that auctioneer can even handle gems is a hack i added in.

(all gem's have the same vnum.. causes heck with the way the auctioneer was designed.. and i only added it because i had time and because i had changed the way that the buggers use to forge runes so i could reuse bits of that code)

2) i am not limiting # of slots per person (altho i had considered it earlier)

3) i am not removing the 1 minute limit in favor of one mass announcement later on of new items.  its just too much work that i dont have the time to do..

4) website .. see #3 .. my current project is listing vaults online.  i had asked for player help, and even gave the info needed to *someone* and still waiting on any sort of result.

5) re- bh jeweler / trade cmd, i kind of like it .  feel free to get teker to work on it if he has the time.

</div>

<div class="post" data-post-id="36862" data-author="*teker*" data-date="2016-04-19T21:08:47+00:00">

> **Quote:**
> feel free to get teker to work on it if he has the time.

Unfortunately my time is fairly scarce ATM.  I am trying to make progress on the quest work when I can, but it is moving slowly.

Thinking about the idea, there's probably 2 ways it could go:

1) Proc similar to auctioneer that handles everything (the in-game solution)

2) Web site set up to facilitate transfers of item(s) between players (the mostly out-of-game solution).  Players could put up an item for trade with a list of desired items in return and other players could make offers, etc.  Currently there is no way to add or remove in-game items via web so when an agreement is made it would be up to the two players to deliver the items to the "barter mob" in-game to facilitate the trade.  The potential downside here is that players could list items they don't have or back out by not delivering their items in a timely fashion.  If that were to happen the other player would have to cancel the deal (or wait for it to time out) and then go reclaim their items at the "barter mob".

</div>
