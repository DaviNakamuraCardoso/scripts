
grammar Dice {
    rule TOP { <subject> <verb> <object> }
    rule subject { <art> <noun> }
    rule object { <art>? <adj>? <noun> } 
    token adj { "two" | "furry" | "three" } 
    token verb { "bit" | "kicked" | "stroked" }
    token art { "the" | "a" }
    token noun { "dog" | "cat" | "dice" | "man" | "woman" | "robot" }

}

say Dice.parse: "the robot stroked the dice"; 
say Dice.parse: "a man kicked a woman"; 
say Dice.parse: "a dog bit a robot"; 
