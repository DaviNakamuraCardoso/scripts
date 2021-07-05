#! /usr/bin/perl

use v5.14;
use strict;

open(BIBLE, "<:utf8", "bible.txt");
binmode(STDOUT, 'utf:8');

my $counter = 0;
my $search = $ARGV[0];
my %appearences = ();


while (my $line = <BIBLE>)
{
    my @words = split(" ", $line);
    foreach my $word (@words)
    {
        my $lower = lc($word);

        unless ($appearences{$lower})
        {
            $appearences{$lower} = 0;
        }

        $appearences{$lower}++;
    }
}

say "The word $search appears $appearences{lc($search)} times on the King James Version of the Bible";
