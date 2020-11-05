#!/usr/bin/python3
import subprocess
import pathlib

PATH = pathlib.Path(__file__).parent.absolute()

subprocess.call(["sh", f"{PATH}get_csv.sh", "--no-refresh"])
subprocess.call(["python3", f"{PATH}get_images.py"])
