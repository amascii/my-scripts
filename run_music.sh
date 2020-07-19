# Change FLACs to ogg using ffmpeg, saves result in ./result/

mkdir result
for i in *.flac; do
	ffmpeg -i "$i" "result/${i/.flac/.ogg}"
done
echo "done"
