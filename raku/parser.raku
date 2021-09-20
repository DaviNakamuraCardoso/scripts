

grammar Parser {
    rule TOP { <subject> <verb> <object> }
    token subject { "Larry" | "Dennis" | "Brian" | "David" | "Donald" }
    token verb { "created" | "hates" | "teaches" }
    token object { "Perl" | "C" | "AWK" | "Computer Science" | "C++" | "CS50" }
}


say Parser.parse: "Larry created Perl";
say Parser.parse: "Donald teaches Computer Science";
say Parser.parse: "Donald hates C++"; 
say Parser.parse: "Brian created AWK";
say Parser.parse: "Brian teaches C";
say Parser.parse: "Brian teaches CS50";
say Parser.parse: "David teaches CS50";




