import subprocess
import time
import pathlib

PATH = pathlib.Path(__file__).parent.absolute()

while True:
    subprocess.call(["python3", f"{PATH}/get_images.py"])
    subprocess.call(["python3", f"{PATH}/get_csv.py"])
    time.sleep(5)
