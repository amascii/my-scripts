# Replace space in a file name with underscores
for i in *" "*; do
	newname=$(echo $i | tr " " "_")
	mv "$i" $newname
done
