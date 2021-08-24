#! /usr/bin/rakudo

sub MAIN returns Int {
    my Str $s = "Davi";
    say $s.^methods;
    say $s.split(" ");
    say $s.flip;

    return 0;
}
