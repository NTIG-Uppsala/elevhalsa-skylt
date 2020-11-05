#!/usr/bin/python3
import subprocess

subprocess.call(["sh", "get_csv.sh"])
subprocess.call(["python3", "get_images.py"])
