# Resize JPGs to arg size and save in ./new/

if [$# != 1]
then
    echo "wrong"
fi
mkdir new
for i in *.JPG; do
     convert $i -resize ${1}x new/$i
done
