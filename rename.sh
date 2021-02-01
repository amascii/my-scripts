#!/bin/bash
input="index.txt"
while IFS= read -r line
do
#   
    #if [ -d "$line" ]; then
    #    echo "next is directory:"
    #fi
    base=$(basename "$line")
    dir=$(dirname "$line")
    base=${base// /_}

    mv "$line" "$dir/$base"


done < $input
