if [ $# -ne 2 ]
then
    echo "./resfo [FOLDER] [HEIGHT]"
    exit
fi

FOLDER=$1
MAXVAL=$2

mkdir $FOLDER

TOTAL=$(ls *.JPG | wc -l)
COUNT=1
for i in *.JPG; do
    convert $i -resize ${MAXVAL}x$MAXVAL ${FOLDER}/$i
    echo "\r$COUNT/$TOTAL"
done

OG_SIZE=$(du -c *.JPG | grep total | sed "s/[^0-9]//g")
NEW_SIZE=$(du $FOLDER | sed "s/[^0-9]//g")

PERCENT=$(echo "result=${NEW_SIZE}/${OG_SIZE}*100; scale=2; result/1" | bc -l)
echo ${PERCENT}% the size
