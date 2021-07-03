#! /usr/bin/awk -f

$2 > 10 { print "To much spent on " $1 " this month"}
