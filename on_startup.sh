#!/usr/bin/env bash
(
tail -n 10000 /home/pi/elevhalsa-skylt-log.txt > /home/pi/elevhalsa-skylt-log.txt.tmp
mv -f /home/pi/elevhalsa-skylt-log.txt.tmp /home/pi/elevhalsa-skylt-log.txt.log

cd /home/pi/Git/elevhalsa-skylt/
# Run in background because download_data.py is continuous
python3 download_data.py &
chromium-browser --force-device-scale-factor=0.8 --start-fullscreen --kiosk http://127.0.0.1:4000/ --incognito
# Logs errors and output of all commands to /home/pi/elevhalsa-skylt-log.txt
# The purpose of this file is to log errors so the source of an error can be located if something goes wrong.
) >> /home/pi/elevhalsa-skylt-log.txt 2>&1