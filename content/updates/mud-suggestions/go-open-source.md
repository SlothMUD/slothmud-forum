---
title: "Go Open-Source?"
topic_id: 4475
author: "Hung"
date: 2015-04-17T00:02:33+00:00
last_activity: 2015-05-01T19:07:30+00:00
last_author: "Yasik"
sticky: false
locked: false
post_count: 30
---

<div class="post" data-post-id="35821" data-author="Hung" data-date="2015-04-17T00:02:33+00:00" data-subject="Go Open-Source?">

First of all, I clearly understand that everything proposed is simply never going to happen. Therefore I propose it not in hope of being done, but to discuss it. I am going to publish my thoughts in two major parts: in first I am going to defend the idea of going open-source, in second - propose a development methodology which doesnt require a code contributor to be trusted in order to accept contributions from him.

Part I. Why Open-Source?

MUDs very rarely have its source code released. In my opinion, it's some archaic tradition going from 90x not having anything reasonable. But that is the way it is. The situation is different in the domain of roguelike games(which is close to MUDs by its spirit). Nethack, Angband, Dungeon Crawl, etc have its source code released.

Someone would object, that releasing source code would result in appearance 10 SlothMUD clones which will distribute the player base among them.

First of all, I dont ask to release content(areas, etc), maybe just a 3-4 areas to make the whole thing deployable and runnable on local environment(in the Part II I'll state reasons).

Also, as far as I remember in the beginning of 2000 some banned imm in rage released the SlothMUD source. How many clones did appear?

Finally, our players in most play for decades, know each other, etc. They are used to the game and the community and it's quite unlikely they'll run to the clone at first possible chance.

Releasing the SlothMUD source code would be great help in learning the game mechanics. For me most the mysterious and interesting part is how is final damage calculated. It has to go through sanc, fluditity, greater fluidity, sanctity, damage reduction, etc. And my interest isnt just idle curiosity, but it'll result on where I'd place monk in my future chars' class order.

Secondly Open-Source SlothMUD will make possible competely different methodology that will allow anyone to make the code contributions. I'll describe that methology(it is safe and isn't require for the contributor to be trusted) in the next post.

</div>

<div class="post" data-post-id="35822" data-author="Hung" data-date="2015-04-17T01:29:21+00:00" data-subject="Re: Go Open-Source?">

Part II: Code Contribution Methodology

<strong>Prerequisites</strong>

- The SlothMUD source code with some content(3-4 areas) released on the corresponding platform such as github
- Coding Conventions Guide(describes how the new code should be written)
- Deployment Guide (describes how the SlothMUD should be deployed on the local environment)

<strong>Step I: Application</strong>

A developer contacts an admin with the application to fix a bug or implement some feature. It could be either his own idea or something already registered in the bug-tracker. The admin gives the green light and provides access to the repository.

<strong>Step II: Development</strong>

The developer fetches the latest source and deploys the game on the local environment. The he creates new working branch where he implements the proposed changes.

<strong>Step III: Review</strong>

The developer joins his changes in the one commit and merges it in the main branch. The admin asks one of the staff coders to review the changes. The staff coder check whether the changes correspond to the coding conventions, is the code clean, understandable, etc. He may reject changes. Then the commit gets reverted and the developer returns to the Step II.

If the staff coder accepts changes then we go to the Step IV.

<strong>Step IV: Testing</strong>

Changes are deployed on the test shard. Where they are throughfully tested. Btw, testers could be simple players and their work could be rewarded with drachma/gems. If testing fails, then the commit reverted and the developer returns to the Step II.

If testing succeeds then the binaries from the test shards are copied to production. The developer is rewarded with drachma/gems. And the process finishes succesfully.

</div>

<div class="post" data-post-id="35823" data-author="Teron" data-date="2015-04-17T07:56:37+00:00" data-subject="Re: Go Open-Source?">

1\. I believe the reason why imms keep everything a secret is that they want us to learn things on our own. At least that's what I heard way before the code was shared by Tower.

However, not everyone has the patience to test everything.

Given that all the research players do they keep to themselves or don't publicly document it, the research is essentially wasted other than in the head of players or is just shared via grouptells, when the topic is brought up.

Since players do leave and take the knowledge with them, this doesnt benefit other players.

So, it does make the MUD look like a poorly documented project and I applaud the efforts to make the help files up-to-date.

I'd too prefer the background mechanics to be known for me to make educated decisions. Sure, I can test stab/grip on the arena, but do imms honestly expect every player, who needs an answer, to test everything on the arena? I personally don't expect that from the new comers and yet they do need information on how to make the most important decision: picking their classo.

Wiki is supposed to help here, of course, but I think the open-source code and the wiki can work togethether: not everyone is a developer and not everyone wants to write lots of articles for the wiki. Each to his own.

2\. As anyone running any project knows, to take it off the ground requirse immense time and effort resources, as well as perseverence. I hardly doubt anyone is able to pull off starting another MUD on their own. So I wouldn't put this as the #1 reason for not making the code open-source.

Besides, there are hundreds MUDs out there. Another new, which is a copy, wouldn't make it any different. If they don't like Sloth, players wouldn't go there and I'd stay away from it, because it'd mean the new MUD is even more buggy and less maintained, than the current one, due to lack of developers.

Also, each MUD is unique and that's what makes it worthwhile. If imms are confident they provide value, they have nothing to be afraid of by sharing the code.

If anything, the code can be distributed through any type of the Creative Commons license that requires attribution and/or limits the changes that can be done without permission.

3\. I do believe that making the code open source will open the code for peer review, which will:

\- allow player developers help with fixing bugs

\- let player developers help with minor things and learn the code, so they can help with larger things.

I think the latter is what the MUD could really use to get more hands, given the lack of developers - that's how big projects get some of their inhouse developers, too. People start small and then develop great stuff. But they do need to start with something.

Honestly, if we are comparing the idea that players should test stuff themselves and the faster developing MUD, I'd pick the faster developing mud that crashes less.

</div>

<div class="post" data-post-id="35825" data-author="*juggleblood*" data-date="2015-04-17T10:45:50+00:00" data-subject="Re: Go Open-Source?">

If there are any talented coders who want to join the development team they are free to do so. They have to show some commitment to the game, vision, and the ability to carry out the intended reforms. This is the way things get done. 

Even though you are talking in an abstract, third person sense. I read this more as your personal desire for more serious involvement with the game. I suggest you think about it and contact Splork about how you might participate. 

I think going open code would be like running a restaurant where the patrons have free access to the kitchen and can stand over the cook's shoulder criticizing them and fighting amongst one another. It seems like a non-starter to me.

</div>

<div class="post" data-post-id="35826" data-author="*Splork*" data-date="2015-04-17T12:07:07+00:00" data-subject="Re: Go Open-Source?">

This was actually discussed a bit the other day, right after he corpsed and got looted and I expressed my views then but will share them again.

There are plenty of avenues to take to contribute to the game such as area building, wiki articles, writing MUDL code for better quests and game content, running quests, coding for the website or the game itself, and on and on.

For some of these, players don't ever have to become an Immortal. However, if one wants to become an Immortal, the process is easier than ever. Play the game, come up with an idea, and we normally give you an Immortal. Simple as that( unless you are a problem player ). There is no long wait. Players no longer have to achieve certain levels or play time. Of course we want you to know the game. A level 10 newbie with 2 days playing experience will not be allowed to become an Immortal.

Ten or Fifteen years ago if an Immortal wanted to code they were forced to build an area. I changed that when I brought in Isabo and Breeze. Both started out helping with the website and moved on to our code. Teker, our newest programmer, helped out with the wiki and coding( we gave him access to only the MUDL files ) additional MUDL procs on the builder's port. Within a couple of months, he was given an account on our coding port and away he went. Honestly, it only takes someone to show a bit of dedication and desire and it should be quite obvious we will create room for that person. On that point, we just brought back Toxis again! Enough said.

We will not be going open source any time soon. We may eventually, who knows. Claiming that because we are closed source stunts development or labels us "archaic" is simply ignorant. Our methods have changed as the times have and we will continue to do so. We have opened up plenty of avenues to allow players to contribute and to be quite honest, for the most part, they have chosen not to. Its good enough for me that the players are playing and I applaud those who step up and help...

In terms of our stability or lack there of, we experienced a two month blip of being unstable due to upgrading our server ( we had to, all linux environments had a major security flaw ). We fought through that, fixed the issues, and came out on the other side. For years before that, and up until yesterday, we have been extremely stable. In the past 1 1/2 months we fixed over 1300 compiler warnings, fixed quite a few memory leaks, redid a great deal of the backbone regarding our game procs/engine and yesterday's reboot prompted two crashes which were both fixed within hours. Honestly, for making the mass amount of changes we did, that is pretty incredible.

One of the comments is that open source brings a more stable environment and in some rare cases this may be true, in a case like ours, that would not be remotely close to the truth. We have hundreds of thousands of lines of code and probably close to the same amount in in-game procs. Take for example the changes Teker just made in regards to giving us the ability to add room procs and the ability to use MUDL in rooms: no amount of testing with our code and 3-4 areas worth of objects and mobs would of prevented the crash from yesterday. Matter of fact, quite possible that even with a full world of mobiles and objects that all testing would of been fine. We have thousands of events triggering every few seconds, its impossible to test for everything, even for those of us who know our code inside and out.

Anyone who thinks that allowing dozens of untrained programmers access to make changes is helping stability really needs to step back and rethink the situation. Arguing that more testing would be done and people walking each other's code would prevent that simply has not been in this type of environment. When I first began coding, all of my code was walked and tested by Frobisher ( wintin developer ) and we still had crashes and bugs. While comments like that read great in text its simply not the reality.

Either way, feel free to contact any of us if you have a desire to contribute. As mentioned, there are plenty of ways to help out.

</div>

<div class="post" data-post-id="35827" data-author="Hung" data-date="2015-04-17T15:30:19+00:00" data-subject="Re: Go Open-Source?">

I apologize for the word 'archaic'. I agree that things are changing constantly(i.e. requirements to immortality). However the base principes stay unchanged. It came from tradition that is quite same for MUDs.

And there is another tradition. I'll cite Nethack as example again. It's creators see nothing wrong in allowing customers into kitchen. I am not saying Nethack is better game than Sloth(those games are too different to even compare). I am saying, there are different traditions. And my sympathies are on open-sourced one.

As for immorting. I feel it's quite wrong to immort mainly to find out how final damage is calculated.

</div>

<div class="post" data-post-id="35832" data-author="*teker*" data-date="2015-04-17T22:36:45+00:00" data-subject="Re: Go Open-Source?">

I can't figure out if the motivation is:

1\) I want to know how all the numbers are crunched so I want to see the source

Which could be remedied by printing out all the formulas next to the answer. Personally I'm against this kind of number crunching and think that it's more fun to just play the game. I would like some additional documentation to know if a fireball does more damage than a flamestrike - but I prefer language that gives me some kind of x is slightly/double/way more powerful than y. We've talked about putting together a wiki article for class order that gives some details but no specific numbers.

2\) I want to learn game development

Diku/Sloth is not really a good example of modern-day game development. Moving that direction is something I'm fond of thinking about, but you'd have to go with a custom protocol and either build a custom client or build a protocol stack for one of the existing clients. Client-server applications have changed quite a bit in the last 20 years (along with most people's processor speeds, bandwidth, etc).

3\) Changes/updates are too slow and/or unstable - need more people

In my short experience "working" here, I can tell you that there's been no shortage of ideas that people have for moving forward with new features. Some of them aren't too hard to implement. But they often lack specific details on how the game would be affected, balance issues, etc. You can't code something without the details and you really shouldn't code something until the idea is hashed out and everyone is confident that it won't mess up the game. 

4\) Something else

??.

</div>

<div class="post" data-post-id="35838" data-author="Teron" data-date="2015-04-20T11:09:27+00:00" data-subject="Re: Go Open-Source?">

1\. Splork, I believe you should be familiar with how Git works. Programmers don't contribute the code directly to the live server, they show it to you and you make the decision, whether to merge it with the live server or not.

2\. I don't think there will be many onlookers from behind your shoulders. As long as the feedback is structured, it shouldn't be a problem - more ideas is always better.

Then again, I can't tell you how to feel regarding your development. If open-source doesn't cut it, alright, but that's the now old trend in web development that makes projects better.

3\. As for an easy way for developers to join you, I am talking about an easy way to start with small things. There should be an open invitation to developers to join the coding team and a list of things to fix, which they can see before getting an immort.

4\. Teker, on a number of my suggestions Juggleblood told me that anything that isn't coding can be changed quickly. Anything that's related to coding is a no go, because the developers are busy.

Is this not true now?

I can take a reason that there are other priorities or that my suggestion needs to be improved to become a real development task. I can work on that.

</div>

<div class="post" data-post-id="35840" data-author="*Splork*" data-date="2015-04-20T13:28:33+00:00" data-subject="Re: Go Open-Source?">

I am quite familiar with how GIT and other repositories work. 

I am not sure why JB would say anything code related is a no-go because that hasn't been the case that I am aware of. We do work on our own projects but whenever something someone else needs is requested, we sure try to get it as quickly as possible. We do have what we feel is a priority list and we also banter the ideas around before they are actually coded. For the past year, we have been working extremely hard on stuff which players don't really see much of. Its all back-end related but eventually we hope it leads to some great stuff. I've personally been spending probably 30-40 hours a week for the last 5-6 months working on this project. 

I use the idea command several times a day and add the ones I/we like. 

Teker is starting out fixing some things and working on an easier way for our Immortals to add dynamic content to our game. Not everyone can write MUDL or be expected to. Having a third programmer should definitely increase our output though. However, it does not mean that every idea submitted will be coded. The ones we like and find interesting we will discuss, as we always do, and possibly start work on soon after.

Thanks!

</div>

<div class="post" data-post-id="35841" data-author="Teron" data-date="2015-04-21T07:22:45+00:00" data-subject="Re: Go Open-Source?">

Teker, just to give you real, current examples:

1\. One thief and I are not sure, whether buying the max dex drachma item is worth it for a thief right now, or we should rather save for nekodes/crystal sleeves.

We were told by two different people that max dex matters and doesn't matter, even if it says so in the files.

Even if it does, does it lead to more damage, compared to standard damage?

As you can see, the items in question cost lots of drachma, so it's a decision one makes once in a life of a character and yet, there's no definitive answer and it probably can not be found in the help files, even if they were updated to the limit.

2\. Should one buy +dam or +5stab dam for a thief? EQlist suggests they are equally weighted, but are they equal in final damage? Drachma costs suggest otherwise, as well as arena testing. But testing was done by one person, should every thief test it before arriving at his own conclusions?

3\. Weapon dam for charge: does it help? It should, but I was told it doesn't.

So I do agree that there should be answers. They can be written in a normal language, not formulas. But like I said, previously, imms were reluctant to give out any information regarding inner game mechanics, insisting on tests. Has this changed? Do you only need writing hands to update the help files?

Thanks.

</div>

<div class="post" data-post-id="35843" data-author="*teker*" data-date="2015-04-21T14:50:46+00:00" data-subject="Re: Go Open-Source?">

> <strong>Quote:</strong>
> 4\. Teker, on a number of my suggestions Juggleblood told me that anything that isn't coding can be changed quickly. Anything that's related to coding is a no go, because the developers are busy.
> 
> 
> 
> Is this not true now?

I'm not going to say that we're not busy - but I don't think that coding suggestions are no-gos. Since I'm new, I'm not going to work on things that change gameplay or balance without hearing from the others whether it should be done or not. But I'm open to working on new features or fixing old things that don't work right.

> <strong>Quote:</strong>
> Teker, just to give you real, current examples

Yes, I think there should be some documentation to aid you in your questions. I'm happy to look at the code to see if things matter - but I have to run it by the others before I can reveal it to you. So are your questions equivalent to:

1\. Does max-dex matter or is it just dex that matters with regard to damage?

2\. What's better +1dam or +5stab-damage for a thief?

3\. Does weapon damage affect the charge skill in any way?

</div>

<div class="post" data-post-id="35845" data-author="Filk" data-date="2015-04-21T17:46:26+00:00" data-subject="Re: Go Open-Source?">

> <strong>\*teker\* wrote:</strong>
> But I'm open to working on new features or fixing old things that don't work right.

Could you be so kind and put up a discussion about max stats not working while shifted <img src="/images/smilies/icon_cool.svg" alt="8)" title="8)" width="15" height="15" class="smiley nozoom"> 

To at least be decided, will it ever be implemented or not. So i could stop to ask about that. <img src="/images/smilies/icon_lol.svg" alt=":lol:" title=":lol:" width="15" height="15" class="smiley nozoom"> 

Also, would be lovely to see all forms damage rolls somewhere. Since now its unbalanced at higher levels and probably should be changed in some ways. Revealing damage rolls could help alot to make some offers to balance forms.

</div>

<div class="post" data-post-id="35846" data-author="Dragoth" data-date="2015-04-21T19:42:54+00:00" data-subject="Re: Go Open-Source?">

Could you also please take away the code that adds a timer on aerial servant recast for clerics after a deathgrip, Splork approves! Thanks!

</div>

<div class="post" data-post-id="35848" data-author="*teker*" data-date="2015-04-22T13:59:26+00:00" data-subject="Re: Go Open-Source?">

> <strong>Quote:</strong>
> 1\. Does max-dex matter or is it just dex that matters with regard to damage?

Max-Dex does not appear to do anything other than let you get a higher Dex. I did notice that items marked AFF\_MAX\_DEX add to MAX\_DEX and DEX.

> <strong>Quote:</strong>
> 2\. What's better +1dam or +5stab-damage for a thief?

From the looks of things, +dam is better. Stab-damage only applies when using the backstab skill. Damage applies to each physical attack each round. Unless the mob dies in less than 5 hits, damage will be better.

That being said, I know there are damage caps and if you've hit yours, +stab-damage might be a bonus on top of that - not really sure.

> <strong>Quote:</strong>
> 3\. Does weapon damage affect the charge skill in any way?

No.

</div>

<div class="post" data-post-id="35850" data-author="Teron" data-date="2015-04-24T09:42:18+00:00" data-subject="Re: Go Open-Source?">

Teker, thanks for replying.

1\. "Help dex" says max dex helps with attack skills:

"The reaction bonus helps with things such as palming, squirm, stalk, deathgrip, wraithtouch, flurry, dodge, focus, presage, prediction, evade capture, and deathtouch."

It also shows max dex of 25 adds 6 reaction bonus. Is it there or it's just in the help files?

2\. Weapon damage is added to the total damage of charge - I've tested this in the arena. I think there should be a multiplier for weapon damage for an opening attack and I've ideased it.

Interestingly, standard damage (+1 damroll) does \*not\* affect the charge damage in any way.

As you can see, even with your input there's contradiction between what you know and what's in the help files, so there should be clearer information, either in a form of correct help files or open source code for those willing to know. Though I agree that opening the code just to learn the mechanics isn't really helpful to most players.

What might work is opening the code for (individual?) players, who wish to research and contribute to the wiki/help files.

</div>

<div class="post" data-post-id="35851" data-author="*Splork*" data-date="2015-04-24T10:58:02+00:00" data-subject="Re: Go Open-Source?">

Taron, 

You are asking somebody who is new to our code, has spent less than 2 weeks inside of it,and hasn't even broken its surface.

He has not really had a chance to even get his feet wet and you expect the poor guy's answers to be remotely correct. Honesty, you get what you asked for, accuracy in a situation like this wasn't going to be the case. He was most likely looking at what affects MAX\_DEX has and there are none. However, there is a dex structure ( there is this for all stats )which gives bonuses based on what your current stats are. He most likely didn't notice this, After all, our code is hundreds of thousands of lines and you have to know where to look. I've been inside our code for nearly 17-18 years and I still can't find quick and accurate answers to some questions.

Technically speaking, he is correct though. Max\_Stat items simply increases that statistic...

Max dex does exactly what is says in the helpfile, as does all the max stats and their helpfiles, which I spent hours on creating and back tracing through the code.

I am going to say this one last time, there isn't a snow balls chance in hell we are releasing our code and going open source. We will not be releasing our code to anyone other than our programmers and Immortals. If there are helpfiles which players want, please feel free to ask. If there are helpfiles players want us to be a bit more specific, please feel free to ask...

Our game is extremely well documented and we spent a great deal of time recently making it possible to edit and add helpfiles with a click of a button. If we feel a player's request warrants an addition to our documentation, we have no issues doing so.

</div>

<div class="post" data-post-id="35852" data-author="Hung" data-date="2015-04-24T11:09:07+00:00" data-subject="Re: Go Open-Source?">

Also I would like the administration to review idea of rewarding with drachma/gems code and documentation contributors.

One of the reasons I am not certain about immorting is that I'm not getting anything for my potential work. Of course, you may consider me selfish bastard(and you prob be right). And I know that paying imms drachma/gems for their work contradicts the whole SlothMUD ideology, where you suppose to work for free.

But when that ideology was formed there were no drachma, no gems and even no complex forges. One could easily(comparing with the today) get all items he wanted. So the payment wasnt required at all.

Now times are different. I.e. I have two chars and both need a rhodo rune. And I doubt I'll ever get what I want unless there'll be a miracle.

Also map contributors get payment for their work. Why code/documentation contributors are deprived from that?

</div>

<div class="post" data-post-id="35853" data-author="Marvel" data-date="2015-04-24T11:23:34+00:00" data-subject="Re: Go Open-Source?">

Work as an imm doesn't reward your mortals.

Work as a mortal (eg: mapping, help files, wiki stuff) rewards your mortals. You don't need to be an imm to do any of these things. Splork has repeatedly rewarded people for submitting needed help files such as coliseum, juju for necros, and the like.

Immortal work is done because that person loves the game and wants to create things. I did a lot of mortal work before immorting and since then, I've still done both variations of work. If imms got rewarded for their work, Splork and Breeze's mortals would be able to buy every single drachma item that exists.

</div>

<div class="post" data-post-id="35854" data-author="Hung" data-date="2015-04-24T11:41:07+00:00" data-subject="Re: Go Open-Source?">

If you want documentation to have acceptable quality, you have to be an imm and have access to the source code.

I.e. damage reduction help:

> <strong>Quote:</strong>
> Damage reduction is an innate ability the monk class has to absorb damage
> 
> from monsters they are fighting. With each point of damage reduction 
> 
> achieved, the monk will absorb more damage than previously till they have
> 
> reached the maximum amount allowed. The amount of damage absorbed depends
> 
> on the difficulty and how hard the monster a player is fighting.

is not informative at all.

Another example: [http://www.slothmud.org/wiki/Monk](http://www.slothmud.org/wiki/Monk)

It states that prime monk gains additional deathgrip modifier, which is simply wrong.

Of course, you may object that I should report documentation bugs. But the problem is one can't figure out there's a bug without access to the source code. 

But, ok, source code isnt going to be released.

I think, area building shouldn't be rewarded, because it is now optional and fun for area builders. But what about coding? Especially coding things that arent fun, but required to be done.

And I dont mind at all if Splork and Breeze buy all drachma items for their mortals.

</div>

<div class="post" data-post-id="35855" data-author="*Splork*" data-date="2015-04-24T11:46:43+00:00" data-subject="Re: Go Open-Source?">

We used to have a "Stars" program for our Immortals and we have debated adding that back in. The basic idea is that different contributions were rewarded different amounts of 'stars'. These stars were normally used for restring tokens, if I remember right.

Here is the actual helpfile:

> <strong>Quote:</strong>
> Stars are awarded for immortal contributions to the game. They can be
> 
> exchanged for certain items that can be handed to mortals.
> 
> 
> 
> Please think about using these items in mini quests or in other ways to
> 
> enhance the game - they are not intended just to be rewards for your
> 
> mortal characters, though you can use them that way if you wish.
> 
> 
> 
> stars list tells you how many stars a player has been awarded.
> 
> 
> 
> stars wrap tells you the history of star awards and redemptions.
> 
> 
> 
> stars bid allows you to bid for a certain number of stars that you feel
> 
> you have earnt. A mail is circulated to the admin weekly, and your request
> 
> will be included. Please specify the reason that you feel you have earnt
> 
> the stars.
> 
> 
> 
> stars give allows you to give a reward to a mortal player. The mortal must
> 
> go to the buxcom wench in the Mermaid's Song and type 'receive' in order
> 
> to receive the reward. Type 'stars list' on its own to see the rewards
> 
> available.
> 
> 
> 
> stars add and stars use are admin commands that will increase and reduce
> 
> an immort's available stars. Use 'stars use' if you give a reward to an
> 
> immort yourself as opposed to their using the wench.

We reward players all the time for different contributions. This can range from helping out a newbie to submitting an extremely bad bug. Those who submit maps or helpfiles are always given drachma. We will never reward in-game items such as gems, sorry.

</div>

<div class="post" data-post-id="35856" data-author="*Splork*" data-date="2015-04-24T11:57:43+00:00" data-subject="Re: Go Open-Source?">

As for the damage reduction helpfile, it gave exactly the amount of information we wanted to at the time. I redid quite a few helpfiles the other night such as weapon damage, spell bonus, etc, and was about to do damage reduction but decided against it because there is a great possibility we are going to take another look at that affect. It needs to be better than it currently is but its going to take a discussion between Immortals to get it right. When we have an agreement and its coded, I will post a more thorough helpfile. That does not mean it will give exact numbers, it may or may not.

As for the issue regarding the Monk discrepancy on the Wiki, I will take a look today or tomorrow and if its incorrect, we will fix it.

I feel the majority of our documentation more than meets the requirements to be labeled 'acceptable quality' when considering the fact this is a hobby, its free, nobody gets paid or makes money. In fact, many of us have contributed to the nearly $20,000 it has taken to keep this game afloat. 

As you said, you won't help unless you are rewarded. Well, we aren't rewarded and we will help when we have time and we will help in whatever manner we choose to help. At least we are helping...

</div>

<div class="post" data-post-id="35857" data-author="Hung" data-date="2015-04-24T13:02:45+00:00" data-subject="Re: Go Open-Source?">

Btw, how many innate damage reduction one is getting depending on monk's position in classo? I've never found answer on this one also.

"Acceptable level of documentation" means it actually answers on questions. Unfortunately as we see in this topic and in many others the documentation doesnt do it. Therefore, no, it's quality is not acceptable. I apologize again, if it hurts someone.

Believe or not, but I am quite thankful for everything you do. And I highly respect unselfish commitment for everyone's fun. Unfortunately I don't do such things. But I look at things in the terms of efficiency. A commitment can be done for free or for something. But is there any difference from the perspective of consumers of that commitment? No.

I.e. let's imagine SlothMUD went open-source(I know that is not going to happen, but we discuss it in theory). The code is on github. All tickets are open and looking for someone to fix it.

First commiter is unselfish. He got a lot of fun playing the game and decided to pay back. So he chooses a ticket and fixes it. Everyone benefits.

Second commiter is like me. He collects drachma for an item. He chooses a ticket, agrees to fix it for, say, 30 dr. Does the job. Everyone benefits.

Third commiter is deadly tired from annoying issue that spoils his run. So he finds corresponding ticket(or creates new one conforming with the admin). Fixes it. Everyone benefits.

Motivations are different but result is same. Everyone benefits.

</div>

<div class="post" data-post-id="35858" data-author="*Splork*" data-date="2015-04-24T13:33:05+00:00" data-subject="Re: Go Open-Source?">

I will agree with you, we do not meet your criteria in terms of acceptable documentation and neither does any other game of our kind that I am aware of. Actually, most games would not. 

Your not offending or hurting anyone with your opinion. Just as I should not be offending anyone when I say that we will run this game however we choose to and see fit.

You can either play and live with what you see as our faults or you can go find a game which is open sourced and has documentation to your liking. 

Either way, the game will carry on with those whom want to play and those whom want to contribute.

</div>

<div class="post" data-post-id="35860" data-author="Hung" data-date="2015-04-24T14:17:07+00:00" data-subject="Re: Go Open-Source?">

I dont think that is fault of the administration. It's rather fault of the system contributions are made. And the admin isn't the one who developed it.

With that system, taking into account the estimated project size, it is simply not possible to keep the documentation at the acceptable level and fix all the small issues(ones that trouble only 1-2 players).

Therefore I propose the systematic solution.

And, yes, the situation is quite common in the world of MUDs. But it doesnt mean the system is right.

</div>

<div class="post" data-post-id="35869" data-author="*Splork*" data-date="2015-04-29T01:52:07+00:00" data-subject="Re: Go Open-Source?">

Feel free to enjoy Hung's thread on TMC...

http://www.mudconnect.com/SMF/index.php?topic=79291.0

Splork

</div>

<div class="post" data-post-id="35870" data-author="Hung" data-date="2015-04-29T07:29:31+00:00" data-subject="Re: Go Open-Source?">

Yes, that topic is quite interesting for me. Therefore I've decided to discuss it with MUD owners to find out their reasons.

Meanwhile, I've found several commercial(!) MMORPGS that have their engines open-sourced:

[http://ryzom.com/](http://ryzom.com/)

[http://www.mystonline.com/en/](http://www.mystonline.com/en/)

</div>

<div class="post" data-post-id="35871" data-author="*Splork*" data-date="2015-04-29T11:10:57+00:00" data-subject="Re: Go Open-Source?">

I am sure there are examples of open-sourced projects for most all types of games available today. 

I find the discussion rather predictable <img src="/images/smilies/icon_lol.svg" alt=":lol:" title=":lol:" width="15" height="15" class="smiley nozoom"> There are plenty more threads on TMC/Mudbytes regarding open-sourced vs closed, which follow a similar path to the one you started. People are basically simply regurgitating what they have already discussed before.

The reasons given to remain closed-source on TMC are extremely accurate in today's MUD world. 

Sorry,

Splork

</div>

<div class="post" data-post-id="35872" data-author="*Breeze*" data-date="2015-04-30T07:07:54+00:00" data-subject="Re: Go Open-Source?">

We can't go open source.... Then the players would see the comment in the code that shows command lag was 'borrowed' from my mud before I was an immortal here. I don't need the players to hate me more than they already do!

</div>

<div class="post" data-post-id="35875" data-author="Magi" data-date="2015-04-30T15:01:39+00:00" data-subject="Re: Go Open-Source?">

So... much... hate...!

Wait, I'm a warrior, nevermind.

</div>

<div class="post" data-post-id="35884" data-author="Yasik" data-date="2015-05-01T19:07:30+00:00" data-subject="Re: Go Open-Source?">

Did not read the whole post, just subject. My opinion: NO!

You want open source - go get CircleMUD sources and mess as much as you want, as I did in my early days.

Then buy hosting, and let your work go live, and see how many players will stay at least few hours.

</div>
