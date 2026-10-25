---
title: "zmud to tinyfugue speedwalk translator"
topic_id: 3968
author: "raincrab"
date: 2012-11-24T07:54:40+00:00
last_activity: 2012-12-15T11:56:34+00:00
last_author: "Tuck"
sticky: false
locked: false
post_count: 3
---

<div class="post" data-post-id="33803" data-author="raincrab" data-date="2012-11-24T07:54:40+00:00">

heres a perl script to translate zmud style speedwalks into tinyfugue commands

```
#!/usr/bin/env perl

#convert zmud speedwalks into tinyfugue commands

# usage: z2tf.pl '3nes2we;open door;'

use strict;
use warnings;

my $zwalk = shift;
my @chars = split //, $zwalk;
my $count = 1;
my $iscmd = 0;
my $cmd = '';

foreach my $char (@chars) {
	if ($char =~ /\;/) {
		if ($iscmd) {
			print $cmd;
			print '%;';
			$cmd = '';
			$iscmd = 0;
		} else {
			$iscmd = 1;
		}
	} elsif ($iscmd) {
		$cmd = "${cmd}${char}";
	} elsif ($char =~ /[nsewud]/) {
		while ($count > 0) {
			print $char;
			print '%;';
			$count--;
		}
		$count = 1;
	} elsif ($char =~ /\d+/) {
		$count = $char;
	}
}
```

you can just use the output in a macro definition for your speedwalk

</div>

<div class="post" data-post-id="33844" data-author="raincrab" data-date="2012-12-13T10:52:05+00:00">

this one fixes bugs where direction count > 10 and consecutive nondirectional commands

```
#!/usr/bin/env perl

# z2tf.pl
#convert zmud speedwalks into tinyfugue commands

# usage: z2tf.pl '3nes2we;open door;'

use strict;
use warnings;

my $zwalk = shift;
my @walks = split ';', $zwalk;
my $count;

foreach my $walk (@walks) {
	while ($walk ne '') {
		if ($walk =~ /^([0-9nsewud]+)$/) {
			if ($walk =~ s/^(\d+)//) {
				$count = $1;
			} else {
				$count = 1;
			}
			$walk =~ s/^(.)//;
			my $char = $1;
			while ($count > 0) {
				print "${char}%;";
				$count--;
			}
		} else {
			print "${walk}%;";
			$walk = '';
		}
	}
}
print "\n";
```

</div>

<div class="post" data-post-id="33846" data-author="Tuck" data-date="2012-12-15T11:56:34+00:00">

Good job!

</div>
