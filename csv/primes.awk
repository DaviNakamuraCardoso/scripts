#! /usr/bin/awk -f



BEGIN {
    size = 100;
    for (i = 0; i < size; i++)
    {
        rawbits[i] = 1;
    }

}

function reset()
{
    for (i = 0; i < size; i++)
    {
        rawbits[i] = 1;
    }
}

{ counts[$1] = $2; }

function validate_results()
{
    return counts[size] == count_primes();
}

function count_primes()
{
    counter = 0;
    for (i = 3; i < size; i++)
    {
        if (getbit(i) == 1) counter++;
    }

    return counter;
}

function clearbit(i)
{
    if (i % 2 == 0) print ";";
    rawbits[i] = 0;
    return;
}

function getbit(i)
{
    if ((i % 2) == 0) return 0;
    return rawbits[i];
}

function run_sieve()
{
    factor = 3;
    q = int(sqrt(size));

    while (factor < q)
    {
        for (i = factor; i < size; i+=2)
        {
            if (rawbits[i] == 1)
            {
                factor = num;
                break;
            }
        }

        for (i = factor*factor; i < size; i += factor*2)
        {
            rawbits[i] = 0;
        }

        factor = factor + 2;
    }

    reset();

    return;
}


END {
    start = systime();
    passes = 0;

    do {
        run_sieve();
        passes++;
        now = systime();
    } while ((now - start) < 5);

    print passes;
}
