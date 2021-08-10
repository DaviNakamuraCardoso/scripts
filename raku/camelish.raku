#! /usr/bin/rakudo

my $fd = open "words.txt", :r;
my $verbsfd = open "verbs.txt", :r; 

my @nouns = $fd.slurp.lines;
my @verbs = $verbsfd.slurp.lines;

grammar Camelish {

    # Tokens
    token adj { < red green > };
    token verb { :i@verbs["s" | "d" | "es" | "ed"]? };
    token noun { :i@nouns }; 
    token sep { ", " | " and " | " " }; 
    token art { :i"the" | :i"a" }; 

    # Rules 
    rule TOP { <subject> <verb> <object> }; 
    rule subject { <art>? <noun> }; 
    rule object { <art>? <comp> [<noun><sep>?]* }; 
    rule comp { [<adj> ]* }; 
}

say Camelish.parse: "Brian teaches AWK, C and Computer Science";



close $fd;
close $verbsfd;
