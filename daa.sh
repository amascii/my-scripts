#!/bin/bash
shopt -s nullglob

dir="."
if [ $# -eq 1 ]; then
    dir=$1
fi

for file in "$dir"/*.{mp3,m4a}
do
    #echo "$file"
    name="${file%%.*}"
    ext="${file##*.}"
    echo $name
    ffmpeg -loglevel warning -i "$file" -vn -c:a copy "${name}tmp.${ext}"
    mv "${name}tmp.${ext}" "$file"
done
