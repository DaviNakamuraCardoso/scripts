#! /usr/bin/env bash

for i in values/*.csv; do 
    echo "In file $i";
    awk -f sums.awk -F ";" $i
done 
