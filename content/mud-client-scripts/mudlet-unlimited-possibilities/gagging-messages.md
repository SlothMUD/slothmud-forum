---
title: "Gagging messages"
topic_id: 4001
author: "dracmas"
date: 2013-01-09T02:32:14+00:00
last_activity: 2013-01-09T22:58:12+00:00
last_author: "dracmas"
sticky: false
locked: false
post_count: 2
---

<div class="post" data-post-id="33902" data-author="dracmas" data-date="2013-01-09T02:32:14+00:00" data-subject="Gagging messages">

Text on the screen you don't want to see? Gag it!

Use triggers to locate what you don't want to see and get rid of it.

For example: 

A large sign with info for newbies has been placed here.

would trigger off of that sentence in mud. Then to gag:

deleteLine()

That's it! You'll never have to see that sentence again as long as the trigger is activated. Someone annoying you in chat? Use a trigger! 

Soandso tells you (change the option to beginning of line substring)

deleteLine()

You can echo to let yourself know if you want to.

echo("Annoying player sent you a message")

You can even replace the text if you want to get more fancy.

Trigger : A large sign with info for newbies has been placed here.

Code:

selectString( "A large sign with info for newbies has been placed here.", 1 )

replace( "The only thing left of this defaced sign is a spray painted smiley face." )

Check the manual for different ways to trigger text:

[http://wiki.mudlet.org/w/Manual:Trigger_Engine](http://wiki.mudlet.org/w/Manual:Trigger_Engine)

</div>

<div class="post" data-post-id="33903" data-author="dracmas" data-date="2013-01-09T22:58:12+00:00" data-subject="Re: Gagging messages">

image: [http://i.troll.ws/a72cbb46.png](http://i.troll.ws/a72cbb46.png)

Here's an example of how you can change text around in the mud to work for you client side.

Note: MSDP has to be running for this to work.

After installed go to the South Gate of Newbatia. See anything different?

First code is called cardboard and second one just in case is for msdp. Select the text for both in notepad/editor saving them as cardboard.xml and msdp.xml Then you can load them into Mudlet with the Package Manager.

cardboard.xml

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE MudletPackage>
<MudletPackage version="1.0">
 <AliasPackage>
 <Alias isActive="yes" isFolder="no">
 <name>cardboard from taking</name>
 <script>if atcp.MSDPROOM_VNUM == "34200" then
echo("\nThis piece of cardboard is too heavy to pick up.")
end -- if</script>
 <command></command>
 <packageName></packageName>
 <regex>^(get|take) cardboard$</regex>
 </Alias>
<Alias isActive="yes" isFolder="no">
 <name>read-cardboard</name>
 <script>if atcp.MSDPROOM_VNUM == "34200" then
cecho("\n<grey>Cardboard with directions written upon it.\nNote: All runs are from Newbatia's South gate.")
cecho("\n<grey>1. Blaster's temple\nRun: 9n Overall Difficulty: Level 10+, 2-3 man group.")
cecho("\n<grey>2. Carnival\nRun: 10nenw6n Overall Difficulty: Newbie.")
cecho("\n<grey>3. Chessboard\nRun: 10nenen Overall difficulty: Level 1 Solo to Level 20 Group.")
cecho("\n<grey>4. Circus\nRun: s3w2n2w3n Overall Difficulty: Mid newbie and up.")
cecho("\n<grey>5. Daar\nRun: 3nu Overall Difficulty: Low level newbies.")
cecho("\n<grey>6. Fens\nRun: s2w2n3w Overall Difficulty: Mid newbie to high newbie.")
cecho("\n<grey>7. Newbatia\nRun: You're here! Overall Difficulty: 1+.")
cecho("\n<grey>8. Newbatis Adventurer's School\nRun: 1u; enter portal Overall Difficulty: Level 1 and up.")
cecho("\n<grey>9. Shadow Playground\nRun: n2es; open shadow; d Overall Difficulty: Level 15-20 Newbie, Mage Oriented.")
cecho("\n<grey>10.Star City\nRun: Be Flying sws2ue;open vines;6e;worship orion;n Overall Difficulty: low level.")
cecho("\n<grey>11.Tiger Glen\nRun: 10nenw5nw Overall Difficulty: Newbie.")
cecho("\n<grey>12.Waterfall\nRun: s3w2n3w3nw4ne2un2un Overall Difficulty: ?")
end -- if</script>
 <command></command>
 <packageName></packageName>
 <regex>^(look|read) cardboard$</regex>
 </Alias>
 </AliasPackage>
 <TriggerPackage>
 <Trigger isActive="yes" isFolder="no" isTempTrigger="no" isMultiline="no" isPerlSlashGOption="no" isColorizerTrigger="no" isFilterTrigger="no" isSoundTrigger="no" isColorTrigger="no" isColorTriggerFg="no" isColorTriggerBg="no">
 <name>tablet-trigger</name>
 <script>selectString( "A large sign with info for newbies has been placed here.", 1 )
deleteLine()
cecho( "<green>\nA large sign with info for newbies has been placed here.\nA piece of cardboard leans against the southern wall." )

</script>
 <triggerType>0</triggerType>
 <conditonLineDelta>0</conditonLineDelta>
 <mStayOpen>0</mStayOpen>
 <mCommand></mCommand>
 <packageName></packageName>
 <mFgColor>#ff0000</mFgColor>
 <mBgColor>#ffff00</mBgColor>
 <mSoundFile></mSoundFile>
 <colorTriggerFgColor>#000000</colorTriggerFgColor>
 <colorTriggerBgColor>#000000</colorTriggerBgColor>
 <regexCodeList>
 <string>A large sign with info for newbies has been placed here.</string>
 </regexCodeList>
 <regexCodePropertyList>
 <integer>0</integer>
 </regexCodePropertyList>
 </Trigger>
 </TriggerPackage>
</MudletPackage>
```

msdp.xml

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE MudletPackage>
<MudletPackage version="1.0">
 <ScriptPackage>
 <ScriptGroup isActive="yes" isFolder="yes">
 <name>thesloth_layout</name>
 <packageName>testing</packageName>
 <script></script>
 <eventHandlerList/>
 <Script isActive="yes" isFolder="no">
 <name>SERVER_ID</name>
 <packageName></packageName>
 <script>function SERVER_ID(event, args)
	initialise_msdp()
end -- SERVER_ID
</script>
 <eventHandlerList>
 <string>MSDPSERVER_ID</string>
 </eventHandlerList>
 </Script>
 <Script isActive="yes" isFolder="no">
 <name>initialise_msdp</name>
 <packageName></packageName>
 <script> function initialise_msdp()
 -- Set the PLUGIN_ID so the mud knows which version you're using.
 sendATCP("@PLUGIN_ID", "GW2_Mudlet_Plugin_(version_1.0)")
 -- Tell the mud which MSDP variables to report.
 sendATCP("@REPORT", "WORLD_TIME CHARACTER_NAME HEALTH HEALTH_MAX MANA MANA_MAX MOVEMENT MOVEMENT_MAX AREA_NAME ROOM_NAME ROOM_VNUM AC HONOR CONTINENT LEVEL CLASS DRACHMA ALIGNMENT EXPERIENCE MONEY STR CON DEX WIS INT STR_PERM CON_PERM DEX_PERM WIS_PERM WEAPON_DAM SPELL_BONUS_CAP HEAL_BONUS HEAL_BONUS_CAP CHARISMA CHARISMA_CAP FLAIL_DAM KICK_DAM HAND_DAM HAND_DAM_CAP DAM_RED DAM_RED_CAP SEX GROUP_LEADER TANK_HEALTH TANK_HEALTH_MAX TANK_LEVEL TANK_NAME LEVEL_SEC LEVEL_TER LEVEL_QUA LEVEL_QUI LEVEL_HEX LEVEL_SEP LEVEL_OCT LEVEL_AVA CITIZEN CLASS_SEC CLASS_TER CLASS_QUA CLASS_QUI CLASS_HEX CLASS_SEP CLASS_OCT CLASS_AVA STAB_DAM STAB_DAM_CAP UNDEAD_CONT UNDEAD_CONT_CAP SPELL_BONUS INT_PERM HITROLL DAMROLL OPPONENT_HEALTH OPPONENT_HEALTH_MAX OPPONENT_LEVEL OPPONENT_NAME TERRAIN AFFECTS ROOM_EXITS")
 end -- initialise_msdp
</script>
 <eventHandlerList/>
 </Script>
 </ScriptGroup>
 </ScriptPackage>
</MudletPackage>
```

</div>
