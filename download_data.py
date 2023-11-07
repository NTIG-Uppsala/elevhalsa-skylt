import subprocess
import time
import pathlib
import requests
from datetime import datetime
from credentials import get_access_token
from dotenv import load_dotenv
import os
load_dotenv()

PATH = pathlib.Path(__file__).parent.absolute()

data_path = "site/_data/stored_data.csv"
picture_path = "site/assets/img"

access_token = get_access_token()
url = f"https://www.googleapis.com/drive/v3/files/1qY1KYAY-AjFh2DWsjiVwOVj2qqJ29kpSs_YaBHi-TEs"
# supportsAllDrives is needed because the google sheet is stored in a shared google drive folder
parameters = {"supportsAllDrives": True, "fields": "modifiedTime"}
previous_modified_time = None

def get_modified_time():
    response = requests.get(url, 
                            headers={"Authorization": "Bearer " + access_token}, 
                            params=parameters)
    date_time_string = response.json()["modifiedTime"]
    # Removes the Z to maintain compatibility with older python verisons than 3.11
    # The Z comes from that the datetime string is written in ISO 8601, which contains a Z at the end
    return datetime.fromisoformat(date_time_string.replace("Z", ""))

def data_has_changed():
    global previous_modified_time
    modified_time = get_modified_time()
    data_has_changed = (modified_time != previous_modified_time)
    previous_modified_time = modified_time
    return data_has_changed

while True:
    if data_has_changed():
        print("Updating data")
        subprocess.call(["python3", f"{PATH}/get_csv.py", os.getenv("sheet_id"), data_path])
        subprocess.call(["python3", f"{PATH}/get_images.py", os.getenv("sheet_id"), picture_path, data_path])
        try:
            subprocess.run(["xdotool", "key", "F5"])
        except:
            print("Error: Ignore this error if you are not in Raspberry pi")
    else:
        print("Data is already updated")
        
    time.sleep(30)

