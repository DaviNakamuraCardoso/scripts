#! /usr/bin/perl

use v5.14;
use strict;

open(BIBLE, "<:utf8", "bible.txt");
binmode(STDOUT, 'utf:8');

my $counter = 0;
my $word = $ARGV[0];
my %appearences = ();


while (my $line = <BIBLE>)
{
    my @words = split(" ", $line);
    foreach (@words)
    {
        my $lower = lc($_);

        if (not $appearences{$lower})
        {
            $appearences{$lower} = 1;
        }
        else
        {
            $appearences{$lower}++;
        }
    }
}

say "The word $word appears $appearences{$word} times on the King James Version of the Bible";
