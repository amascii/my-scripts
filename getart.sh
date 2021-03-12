
shopt -s nullglob

dir="."
if [ $# -eq 1 ]; then
    dir=$1
fi

for file in "$dir"/*.{mp3,m4a}
do
    ffmpeg -i "$file" "${dir}/cover.jpg"
    break
done
