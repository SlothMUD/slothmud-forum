---
title: "tinyfugue syntax highlighting for textmate (mac osx)"
topic_id: 3983
author: "raincrab"
date: 2012-12-19T22:55:28+00:00
last_activity: 2012-12-19T22:55:28+00:00
last_author: "raincrab"
sticky: false
locked: false
post_count: 1
---

<div class="post" data-post-id="33853" data-author="raincrab" data-date="2012-12-19T22:55:28+00:00" data-subject="tinyfugue syntax highlighting for textmate (mac osx)">

create a new bundle in tm, add this to it

```
{	patterns = (
		{	name = 'keyword.control.untitled';
			match = '\/(if|endif|else|elseif|for|while)\b';
		},
		{	name = 'entity.name.function';
			match = '\/(addworld|at|bamf|beep|bind|break|cat|changes|connect|dc|def|dokey|echo|edit|escape|eval|not|exit|export|expr|features|fg|finger|for|gag|getfile|grab|help|hilite|histsize|hook|if|input|kill|lcd|let|limit|list|listsockets|liststreams|listvar|listworlds|load|localecho|log|more|nohilite|partial|paste|ps|purge|purgeworld|putfile|quit|quote|recall|recordline|repeat|replace|restrict|return|runtime|save|saveworld|send|set|setenv|sh|shift|sub|substitute|suspend|telnet|test|tick|time|toggle|tr|trig|trigger|unbind|undef|undefn|undeft|unhook|unset|untrig|unworld|version|watchtdog|watchname|while|world)\b';
		},
		{	name = 'comment';
			match = '^;.+';
		},
		{	name = 'constant.numeric';
			match = '\b([0-9]+)\b';
		},
		{	name = 'invalid';
			match = '\b([\t ]+)$';
		},
		{	name = 'constant.language';
			match = '\b(yes|no)\b';
		},
		{	name = 'support.type';
			match = '\-(\w+)\b';
		},
		{	name = 'support.variable';
			match = '(%?\{(\S+)\}|%(\w+))';
		},
		{	name = 'string.regexp';
			begin = '"';
			end = '"';
			patterns = (
				{	name = 'constant.character.escape.untitled';
					match = '\\.';
				},
			);
		},
	);
}
```

edit: replaced xml with textmate grammar

</div>
