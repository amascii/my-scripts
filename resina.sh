# Rename and resize .jpg/.JPGs

if [ $# != 1 ]
then
	echo "./resina [folder]"
else
	path=$1
	name=$(basename $path)
	dir="${name}2"
	cp -r $path $dir
	jhead -n%Y%m%d-%H%M%S-$name $dir/*.jpg
	jhead -n%Y%m%d-%H%M%S-$name $dir/*.JPG
	for i in $dir/*.jpg; do
		convert $i -resize 1200x $dir/$(basename $i)
	done
fi
