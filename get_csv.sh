echo "DOWNLOADING CSV"
wget --output-file="logs.csv" "https://docs.google.com/spreadsheets/d/1k0qCUQbKvipCa8dhFcFjccRAWVGSeYF_MJwcu1Fy5Ls/export?format=csv&gid=0" -O "site/_data/eht.csv"
wget --output-file="logs.csv" "https://docs.google.com/spreadsheets/d/1k0qCUQbKvipCa8dhFcFjccRAWVGSeYF_MJwcu1Fy5Ls/export?format=csv&gid=1501224853" -O "site/_data/procivitas.csv"

IS_SAME=1
EHT_HASH=$(cat "site/_data/eht_hash.txt")
PROCIVITAS_HASH=$(cat "site/_data/procivitas_hash.txt")

NEW_EHT_HASH=$(md5sum site/_data/eht.csv | awk '{ print $1 }')
NEW_PROCIVITAS_HASH=$(md5sum site/_data/procivitas.csv | awk '{ print $1 }')

if [ "$NEW_EHT_HASH" = "$EHT_HASH" ]; then
    echo "EHT Data is same"
else
    IS_SAME=0
    echo "EHT Data is different"
    echo "$NEW_EHT_HASH" > "site/_data/eht_hash.txt"
fi

if [ "$NEW_PROCIVITAS_HASH" = "$PROCIVITAS_HASH" ]; then
    echo "Procivitas Data is same"
else
    IS_SAME=0
    echo "Procivitas Data is different"
    echo "$NEW_PROCIVITAS_HASH" > site/_data/procivitas_hash.txt
fi

if [ "$IS_SAME" -eq "0" ]; then
    echo "RELOADING SITE"
    export DISPLAY=:0.0
    xdotool key F5
fi
