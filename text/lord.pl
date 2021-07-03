#! /usr/bin/perl

use v5.14;
use strict;

open(BIBLE, "<:utf8", "bible.txt");
binmode(STDOUT, 'utf:8');

my $counter = 0;
my $word = $ARGV[0];

while (my $line = <BIBLE>)
{
    my @words = split(" ", $line);
    foreach (@words) {
        if (lc($_) eq lc($word)) {
            $counter++;
        }
    }
}

say "The word $word appears $counter times on the King James Version of the Bible";
