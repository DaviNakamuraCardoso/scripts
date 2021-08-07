

my $fd = open "words.txt", :r;
$fd.WHAT;
my $contents = $fd.slurp.lines;
say $contents; 

grammar Dice {

    # Tokens
    token adj { < two furry little green red > };
    token verb { "bit" | "kicked" | "stroked" };
    token art { :i"the" | :i"a" };

    # Rules 
    rule comp { [<adj> ]* }; 
    rule subject { <art> <noun> }; rule object { <art>? <comp> <noun> }; rule TOP { <subject> <verb> <object> }; 
    rule noun { $contents }; 
}

say Dice.parse: "The robot stroked two red furry little little green dice"; 
say Dice.parse: "a man kicked the little dog"; 
say Dice.parse: "I like Raku"; 


