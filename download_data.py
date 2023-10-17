import subprocess
import time
import pathlib

PATH = pathlib.Path(__file__).parent.absolute()

sheet_id = "1qY1KYAY-AjFh2DWsjiVwOVj2qqJ29kpSs_YaBHi-TEs"
data_path = "site/_data/stored_data.csv"
picture_path = "site/assets/img/Profile"

while True:
    subprocess.call(["python3", f"{PATH}/get_images.py", sheet_id, picture_path])
    subprocess.call(["python3", f"{PATH}/get_csv.py", sheet_id, data_path])
    time.sleep(5)
