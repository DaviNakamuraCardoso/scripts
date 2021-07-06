#! /usr/bin/awk -f

BEGIN {
    population = 0
    city = "No city"
}


parseint($9) > population {
    population = parseint($9);
    city = $1;
}

function parseint(string)
{
    value = 0;
    factor = 1;
    split(string, arr, "");

    for (i = length(string)-1; i >= 0; i--)
    {
        value += (int(arr[i])) * factor;
        factor *= 10;
    }

    return value;
}


END {
    print city
}
