#!/usr/bin/python3
import subprocess, time
import pathlib

PATH = pathlib.Path(__file__).parent.absolute()

subprocess.call(["sh", f"{PATH}/get_csv.sh"])
subprocess.call(["python3", f"{PATH}/get_images.py"])
subprocess.call(["python3", f"{PATH}/parse_salary.py"])

while True:
    time.sleep(60*5)
    subprocess.call(["sh", f"{PATH}/get_csv.sh", "--not-refresh"])
    subprocess.call(["python3", f"{PATH}/parse_salary.py"])
