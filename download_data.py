#!/usr/bin/python3
import subprocess, time
import pathlib

PATH = pathlib.Path(__file__).parent.absolute()



while True:
    subprocess.call(["sh", f"{PATH}/get_csv.sh"])
    subprocess.call(["python3", f"{PATH}/get_images.py"])
    time.sleep(5)
