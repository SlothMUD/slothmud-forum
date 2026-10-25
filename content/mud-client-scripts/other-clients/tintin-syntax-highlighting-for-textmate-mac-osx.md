---
title: "tintin++ syntax highlighting for textmate (mac osx)"
topic_id: 3985
author: "raincrab"
date: 2012-12-20T02:39:25+00:00
last_activity: 2012-12-20T02:39:25+00:00
last_author: "raincrab"
sticky: false
locked: false
post_count: 1
---

<div class="post" data-post-id="33855" data-author="raincrab" data-date="2012-12-20T02:39:25+00:00" data-subject="tintin++ syntax highlighting for textmate (mac osx)">

create a tintin bundle and add this grammar to it

```
{	patterns = (
		{	name = 'keyword.control';
			match = '#(if|case|continue|default|while|else|elseif|endif|break|for|foreach|forall|return)\b';
		},
		{	name = 'support.function';
			match = '#(action|alias|all|bell|buffer|chat|class|config|cr|cursor|debug|default|delay|echo|end|event|function|gag|greeting|grep|help|highlight|history|ignore|info|kill|line|list|log|loop|macro|map|math|message|parse|path|pathdir|prompt|read|regexp|replace|return|run|scan|script|send|session|showme|substitute|suspend|switch|system|tab|textin|ticker|variable|var|write|zap)\b';
		},
		{	name = 'comment.line';
			begin = '^#nop';
			end = '$';
		},
		{	name = 'variable.other';
			match = '\$(\w+)';
		},
		{	name = 'constant.other';
			match = '<...>';
		},
		{	name = 'constant.numeric';
			match = '\b(\d+)\b';
		},
		{	name = 'variable.parameter';
			match = '%([\-\+\w+|\.]+)';
		},
	);
}
```

</div>
