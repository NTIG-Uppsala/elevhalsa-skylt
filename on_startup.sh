#!/usr/bin/env bash
(
cd /home/pi/Git/elevhalsa-skylt/
python3 download_data.py &
chromium-browser --force-device-scale-factor=0.6 --start-fullscreen --kiosk http://127.0.0.1:4000/ --incognito
# Logs errors and output of all commands to /home/pi/elevhalsa-skylt-log.txt
) >> /home/pi/elevhalsa-skylt-log.txt 2>&1