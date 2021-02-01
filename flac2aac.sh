for f in *.flac;
do
    ffmpeg -i "$f" -c:v copy -c:a libfdk_aac -vbr 3 "${f%.flac}".m4a
done
#rm *.flac
