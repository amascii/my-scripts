for i in *.AVI; do ffmpeg -i "$i" "${i%.*}.mp4"; done
