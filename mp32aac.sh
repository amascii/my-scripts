dir="."
if [ $# -eq 1 ]; then
    dir="$1"
fi

for file in "$dir"/*.mp3
do
    echo "converting $file"
    ffmpeg -loglevel warning -i "$file" -c:a libfdk_aac -vbr 4 "${file%.mp3}".m4a
done


#read -p "Remove flacs? (y/n) " -n 1 -r
#echo    # (optional) move to a new line
#if [[ $REPLY =~ ^[Yy]$ ]]
#then
#    # do dangerous stuff
#    rm "$dir"/*.flac
#fi
