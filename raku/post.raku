grammar FurryDice {
    # Rules 
    rule TOP { <subject> <verb> <object> };
    rule subject { <art> <noun> };
    rule object { <art>? <comp> <noun> };  # Art is optional in this case
    rule comp { [<adj> ]* };  # Zero or more adjectives followed by spaces 
   
    # Tokens
    token verb { "bit" | "kicked" | "stroked" };
    token adj {  "two" | "furry" };
    token art { "the" | "a" }; 
    token noun { "dog" | "cat" | "dice" | "man" | "woman" | "robot" }; 
}

say FurryDice.parse("the robot stroked two furry dice");
