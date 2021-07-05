#! /usr/bin/awk -f

distance($3, $4) < 1 { print $2 }

function distance(x, y) {
    xo = int(ARGV[2])
    yo = int(ARGV[3])
    dx = (x-xo) * (x-xo)
    dy = (y-yo) * (y-yo)

    return int(sqrt(dx+dy))
}
