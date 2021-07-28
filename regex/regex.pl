#! /usr/bin/perl 


use v5.14;

my $os = "Ubuntu 20.4";


if (/Windows 7/)
{
    print "Time to upgrade?\n";
}

my ($good, $bad, $ugly) = split(/,/, "vi,emacs,teco");


say $good; say $bad; say $ugly;


