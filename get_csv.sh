#!/bin/bash
echo "DOWNLOADING CSV"

if [ ! -d tmp ]; then
    mkdir tmp
fi

wget "https://docs.google.com/spreadsheets/d/1k0qCUQbKvipCa8dhFcFjccRAWVGSeYF_MJwcu1Fy5Ls/edit#gid=0" -O "tmp/eht.csv"
wget  "https://docs.google.com/spreadsheets/d/1k0qCUQbKvipCa8dhFcFjccRAWVGSeYF_MJwcu1Fy5Ls/export?format=csv&gid=431694755" -O "tmp/maud.csv"
wget  "https://docs.google.com/spreadsheets/d/1k0qCUQbKvipCa8dhFcFjccRAWVGSeYF_MJwcu1Fy5Ls/export?format=csv&gid=1501224853" -O "tmp/procivitas.csv"
wget  "https://docs.google.com/spreadsheets/d/1k0qCUQbKvipCa8dhFcFjccRAWVGSeYF_MJwcu1Fy5Ls/export?format=csv&gid=517548157" -O "tmp/important_events.csv"
wget  "https://docs.google.com/spreadsheets/d/1k0qCUQbKvipCa8dhFcFjccRAWVGSeYF_MJwcu1Fy5Ls/export?format=csv&gid=1645773200" -O "tmp/professions.csv"

# for file in tmp/*; do
#     if [ -s "$file" ]; then
#         mv "$file" site/_data/
#     fi
# done

# IS_SAME=1
# NOT_REFRESH=0

# EHT_HASH=$(cat `pwd`/site/_data/eht_hash.txt)
# MAUD_HASH=$(cat `pwd`/site/_data/maud_hash.txt)
# PROCIVITAS_HASH=$(cat `pwd`/site/_data/procivitas_hash.txt)

# NEW_EHT_HASH=$(md5sum `pwd`/site/_data/eht.csv | awk '{ print $1 }')
# NEW_MAUD_HASH=$(md5sum `pwd`/site/_data/maud.csv | awk '{ print $1 }')
# NEW_PROCIVITAS_HASH=$(md5sum `pwd`/site/_data/procivitas.csv | awk '{ print $1 }')

# for var in "$@"
# do
#     if [ "$var" = "--not-refresh" ]; then
#         NOT_REFRESH=1
#     fi
# done


# if [ "$NEW_EHT_HASH" = "$EHT_HASH" ]; then
#     echo "EHT Data is same"
# else
#     IS_SAME=0
#     echo "EHT Data is different"
#     echo "$NEW_EHT_HASH" > `pwd`/site/_data/eht_hash.txt
# fi

# if [ "$NEW_MAUD_HASH" = "$MAUD_HASH" ]; then
#     echo "MAUD Data is same"
# else
#     IS_SAME=0
#     echo "MAUD Data is different"
#     echo "$NEW_MAUD_HASH" > `pwd`/site/_data/maud_hash.txt
# fi

# if [ "$NEW_PROCIVITAS_HASH" = "$PROCIVITAS_HASH" ]; then
#     echo "Procivitas Data is same"
# else
#     IS_SAME=0
#     echo "Procivitas Data is different"
#     echo "$NEW_PROCIVITAS_HASH" > `pwd`/site/_data/procivitas_hash.txt
# fi

# if [ "$IS_SAME" -eq "0" ] && [ "$NOT_REFRESH" -eq "0" ]; then
#     sleep 2
#     echo "RELOADING SITE"
#     export DISPLAY=:0.0
#     xdotool key F5
# fi
