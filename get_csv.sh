# Get syv
echo "DOWNLOADING CSV"
wget --output-file="logs.csv" "https://docs.google.com/spreadsheets/d/1k0qCUQbKvipCa8dhFcFjccRAWVGSeYF_MJwcu1Fy5Ls/export?format=csv&gid=0" -O "site/_data/eht.csv"
