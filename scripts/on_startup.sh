#!/usr/bin/env bash

# This is placed outside of the parentheses because otherwise it modifies the log and writes to the log at the same time.
LOG_PATH="~/elevhalsa-skylt-log.txt"
TEMP_LOG_PATH="${LOG_PATH}.tmp"
# Only keep the last 10000 lines of the log file
tail -n 10000 $LOG_PATH > $TEMP_LOG_PATH
mv -f $TEMP_LOG_PATH $LOG_PATH
(
cd ~/Git/elevhalsa-skylt/
source ./.venv/bin/activate
python3 scripts/main.py
deactivate
chromium-browser --force-device-scale-factor=0.8 --start-fullscreen --kiosk http://127.0.0.1:4000/ --incognito
# Logs errors and output of all commands to the log file
# The purpose of this file is to log errors so the source of an error can be located if something goes wrong.
) >> $LOG_PATH 2>&1