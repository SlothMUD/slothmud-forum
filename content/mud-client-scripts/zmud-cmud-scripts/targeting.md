---
title: "Targeting"
topic_id: 2991
author: "Ordin"
date: 2008-12-16T18:28:25+00:00
last_activity: 2008-12-16T21:00:37+00:00
last_author: "firebrand"
sticky: false
locked: false
post_count: 4
---

<div class="post" data-post-id="27477" data-author="Ordin" data-date="2008-12-16T18:28:25+00:00" data-subject="Targeting">

i dont know if this will help anyone this you can type ttt and name like

(ttt ferret) and it will target ferret then you make another alias like for what what you gonna do and point it at the target so then all you got to do is like type missile instead of the cast 'magic missile' ferret you just type missile after typing ttt ferret

\#ALIAS ttt {tt %1;targ = %1;#say target is set to: %1}

\#ALIAS missile {cast 'magic missile' %1 @targ}

if anyone wants to explain this better go ahead

</div>

<div class="post" data-post-id="27478" data-author="Ordin" data-date="2008-12-16T18:29:26+00:00" data-subject="">

also i fogot this will work for any ability

</div>

<div class="post" data-post-id="27480" data-author="firebrand" data-date="2008-12-16T20:56:49+00:00" data-subject="">

\#alias mm {cast 'magic missile'}

\#alias targ {#var $targ %0; groupt target is %0}

\#alias mmt {mm $targ}

"don't shoot, don't shoot! he's cool. he made a deal with dr. doom, same as you." - l.j. --\> resident evil: apocalypse

</div>

<div class="post" data-post-id="27481" data-author="firebrand" data-date="2008-12-16T21:00:37+00:00" data-subject="">

> <strong>firebrand wrote:</strong>
> \#alias mm {cast 'magic missile'}
> 
> \#alias targ {#var $targ %0; groupt target is %0}
> 
> \#alias mmt {mm $targ}

whoops. was supposed to be: 

\#alias targ {#var target $0; groupt target $0}

</div>
