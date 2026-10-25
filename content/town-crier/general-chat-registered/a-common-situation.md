---
title: "A common situation >:("
topic_id: 1286
author: "Yasik"
date: 2005-06-22T14:54:54+00:00
last_activity: 2005-06-22T18:24:34+00:00
last_author: "Avatar"
sticky: false
locked: false
post_count: 10
---

<div class="post" data-post-id="7465" data-author="Yasik" data-date="2005-06-22T14:54:54+00:00">

[img:1v25kkii]http://yasik.mci.kiev.ua/Frenzy_fail_3times_2.jpg[/img:1v25kkii]

And this happens very often. Men, i tell you there is something wrong with this skills in the code, i swear.  :evil:

Also put there Berserk and Counter attack.

</div>

<div class="post" data-post-id="7468" data-author="kjartan" data-date="2005-06-22T15:22:16+00:00">

I just double-checked the code, there is nothing wrong.

A triple failure should be about a 1 in 200 or 1 in 300 occurrence, so yes you will see it occasionally.

</div>

<div class="post" data-post-id="7472" data-author="Yasik" data-date="2005-06-22T15:41:29+00:00">

Well, my player's experience tell me that x3 fail happens 1 from 50 times, x2 fail happens 1 from 20 times, and x1 fail happens 1 from 2..4 times, approximately.

It should not be this way and this isnt a 'feature'.

Maybe the code is correct, but so much fails is unnatural.

</div>

<div class="post" data-post-id="7473" data-author="Alberich" data-date="2005-06-22T15:52:54+00:00">

sounds like you just have bad luck :)  I cannot remember frenzy (or berserk for that matter) failing 3x in a row ever.. even 2x is pretty rare for me.  

Now, apply poison, on the other hand.... :P

</div>

<div class="post" data-post-id="7474" data-author="13" data-date="2005-06-22T16:02:16+00:00">

or flurry...

</div>

<div class="post" data-post-id="7475" data-author="12345" data-date="2005-06-22T16:11:39+00:00">

Honestly, it almost always comes back to random number generation, whether it's lost conc, failed skills, or rerolling.  Some may be interested that there's a lot of Diku derivatives that use their own random number generators... For instance, this is taken from a Mythran codebase, but I believe Furey was a Merc coder.  Either way, it's Furey's code:

[code:2aivgsk2]/*

 * I've gotten too many bad reports on OS-supplied random number generators.

 * This is the Mitchell-Moore algorithm from Knuth Volume II.

 * Best to leave the constants alone unless you've read Knuth.

 * -- Furey

 */

static	int	rgiState[2+55];

void init_mm( )

{

    int *piState;

    int  iState;

    piState	= &rgiState[2];

    piState[-2]	= 55 - 55;

    piState[-1]	= 55 - 24;

    piState[0]	= ( (int) current_time ) & ( ( 1 << 30 ) - 1 );

    piState[1]	= 1;

    for ( iState = 2; iState < 55; iState++ )

    {

	piState[iState] = ( piState[iState-1] + piState[iState-2] )

			& ( ( 1 << 30 ) - 1 );

    }

    return;

}

int number_mm( void )

{

    int *piState;

    int  iState1;

    int  iState2;

    int  iRand;

    piState		= &rgiState[2];

    iState1	 	= piState[-2];

    iState2	 	= piState[-1];

    iRand	 	= ( piState[iState1] + piState[iState2] )

			& ( ( 1 << 30 ) - 1 );

    piState[iState1]	= iRand;

    if ( ++iState1 == 55 )

	iState1 = 0;

    if ( ++iState2 == 55 )

	iState2 = 0;

    piState[-2]		= iState1;

    piState[-1]		= iState2;

    return iRand >> 6;

}

/*

 * Roll some dice.

 */

int dice( int number, int size )

{

    int idice;

    int sum;

    switch ( size )

    {

    case 0: return 0;

    case 1: return number;

    }

    for ( idice = 0, sum = 0; idice < number; idice++ )

	sum += number_range( 1, size );

    return sum;

}

/*

 * Generate a random number.

 */

int number_range( int from, int to )

{

    int power;

    int number;

    if ( ( to = to - from + 1 ) <= 1 )

	return from;

    for ( power = 2; power < to; power <<= 1 )

	;

    while ( ( number = number_mm( ) & ( power - 1 ) ) >= to )

	;

    return from + number;

}

/*

 * Generate a percentile roll.

 */

int number_percent( void )

{

    int percent;

    while ( ( percent = number_mm( ) & ( 128-1 ) ) > 99 )

	;

    return 1 + percent;

}[/code:2aivgsk2]

</div>

<div class="post" data-post-id="7476" data-author="kjartan" data-date="2005-06-22T16:14:24+00:00">

Our random number generator is fine.  I tested it, really, it's fine.  (And even if it wasn't fine, it's very unlikely that the failure mode would be visible in these skill checks as "a number from 1 to 100 comes out above 85 too often").

What it comes down to is the nature of human perception of rare events.  You remember the times something unusal happens more strongly than you remember the times everything worked out as expected, so it seems like the unusual events happen more often than they actually do.

</div>

<div class="post" data-post-id="7477" data-author="firebrand" data-date="2005-06-22T17:01:37+00:00">

grumble then why is the failed skill check and lost concs on spells so bloody HIGH?  and why does it seem that the concentration skill for avs does not reduce the lost concs like it is supposed to?  why do we avs still have approx same number of lost concs with the skill learned as compared to before we learned/read the skill?  one would think that with something learned at 85%, failed skill check should occur approx on avg 15% of the time and with spell learned at 95%, there should be an approx lost conc of only 5% or more, but some days it seems like the actual failed skill/lost conc is actually closer to 20% on skills and spells

</div>

<div class="post" data-post-id="7479" data-author="12345" data-date="2005-06-22T18:20:28+00:00">

Skill checks _may_ have other things going on with them that contribute to failure.  Easiest example I can think of is kick.  If you're facing a mob with an AC of 10, you get your full 85% to land a kick.  The better armored the mob, the harder it gets until you have 75% against an AC of -10. (These numbers are from Diku gamma, Sloth may be different.)

Anyway, the point is that skills may have other factors that can contribute to success or failure.  Looking at gamma, spells look to be a straight 95%, but again... we're not playing gamma.

*shrug*

</div>

<div class="post" data-post-id="7480" data-author="Avatar" data-date="2005-06-22T18:24:34+00:00">

You're reinforcing the argument that people notice failures more often than they notice successes.

Firebrand:

[quote:mqxbqzoj]but some days it seems like the actual failed skill/lost conc is actually closer to 20% on skills and spells[/quote:mqxbqzoj]

The last time I remember anyone posting actual numbers from spellcasting they ran right at 95%.

</div>
