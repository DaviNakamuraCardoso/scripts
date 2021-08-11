#! /usr/bin/rakudo

my $fd = open "words.txt", :r;
my $verbsfd = open "verbs.txt", :r; 
my $adjectivesio = open "adjectives.txt", :r;  

my @nouns = $fd.slurp.lines;
my @verbs = $verbsfd.slurp.lines;
my @adjectives = $adjectivesio.slurp.lines; 


grammar Camelish {

    # Tokens
    token adj { :i@adjectives };
    token verb { :i@verbs["s" | "d" | "es" | "ed"]? };
    token noun { :i@nouns }; 
    token sep { ", " | " and " | " " }; 
    token art { :i"the" | :i"a" }; 

    # Rules 
    rule TOP { [<phrase> ]+ }; 
    rule phrase { <subject> <verb> <object>"."}
    rule subject { <art>? [<noun> ]* <noun> }; 
    rule object { <art>? <comp>? [<noun><sep>?]* }; 
    rule comp { [<adj> ]+ }; 
}

say Camelish.parse: "Brian Davi likes C. "; 
#say Camelish.parse: "Brian likes C. Davi likes C. ";



close $fd;
close $verbsfd;
close $adjectivesio;
