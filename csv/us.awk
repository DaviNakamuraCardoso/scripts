#! /usr/bin/awk -f

{
    sum += $9;
}


END {
    print sum; 
}
