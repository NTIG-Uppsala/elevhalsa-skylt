#!/bin/bash
echo "DOWNLOADING CSV"

if [ ! -d tmp ]; then
    mkdir tmp
fi

wget "https://docs.google.com/spreadsheets/d/1qY1KYAY-AjFh2DWsjiVwOVj2qqJ29kpSs_YaBHi-TEs/export?format=csv&gid=0" -O "tmp/eht.csv"

for file in tmp/*; do
    if [ -s "$file" ]; then
        mv "$file" site/_data/
    fi
done

IS_SAME=1
NOT_REFRESH=0

EHT_HASH=$(cat /home/pi/Git/elevhalsa-skylt/site/_data/eht_hash.txt)

NEW_EHT_HASH=$(md5sum /home/pi/Git/elevhalsa-skylt/site/_data/eht.csv | awk '{ print $1 }')

for var in "$@"
do
    if [ "$var" = "--not-refresh" ]; then
        NOT_REFRESH=1
    fi
done


if [ "$NEW_EHT_HASH" = "$EHT_HASH" ]; then
    echo "EHT Data is same"
else
    IS_SAME=0
    echo "EHT Data is different"
    echo "$NEW_EHT_HASH" > `pwd`/site/_data/eht_hash.txt
fi

if [ "$IS_SAME" -eq "0" ] && [ "$NOT_REFRESH" -eq "0" ]; then
    sleep 2
    echo "RELOADING SITE"
    export DISPLAY=:0.0
    xdotool key F5
fi
