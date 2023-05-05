for i in {001..200}
do
    echo "stamping $i"
    ./cpdf -stamp-on "outputs/"$i"_stamp.pdf" $1 -o "outputs/"$i"_ready.pdf"
done
