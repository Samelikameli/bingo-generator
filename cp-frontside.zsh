for i in {001..200}
do
    (( TARGET=$i*2-1 ))
    PADDED=${(l:3::0:)TARGET}
    echo $PADDED
    cp "outputs/"$i"_ready.pdf" "merging/"$PADDED".pdf"
done
