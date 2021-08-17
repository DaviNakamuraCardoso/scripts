#! /usr/bin/rakudo

sub MAIN returns Int {
    for 1..1000 -> $i {
        printf("%i\n", $i);
    }
    return 0; 
}
