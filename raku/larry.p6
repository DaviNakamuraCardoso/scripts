grammar Lang {
    rule TOP { <uop>? <statement> [<bop> <uop>?<statement>]* }
    token uop { "not" }
    token bop { "or" | "and" }
    rule statement { self } 
}

say Lang.parse: "self";
say Lang.parse: "self or self";

