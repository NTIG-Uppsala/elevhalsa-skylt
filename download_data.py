#!/usr/bin/python3
import time, subprocess

MINUTES_TO_WAIT = 10

while True:
    subprocess.call(["sh", "get_csv.sh"])
    subprocess.call(["python3", "get_images.py"])
    time.sleep(1000*60*MINUTES_TO_WAIT)
