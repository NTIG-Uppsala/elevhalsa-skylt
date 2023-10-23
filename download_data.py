import subprocess
import time
import pathlib
import requests
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

PATH = pathlib.Path(__file__).parent.absolute()

sheet_id = "1qY1KYAY-AjFh2DWsjiVwOVj2qqJ29kpSs_YaBHi-TEs"
data_path = "site/_data/stored_data.csv"
picture_path = "site/assets/img"

scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    "service_account_credentials.json", scope
)
# from https://stackoverflow.com/a/69776579
access_token = (
    credentials.create_delegated(credentials._service_account_email)
    .get_access_token()
    .access_token
)
url = f"https://www.googleapis.com/drive/v3/files/1qY1KYAY-AjFh2DWsjiVwOVj2qqJ29kpSs_YaBHi-TEs"
parameters = {"supportsAllDrives": True, "fields": "modifiedTime"}
previous_modified_time = None

def get_modified_time():
    response = requests.get(url, 
                            headers={"Authorization": "Bearer " + access_token}, 
                            params=parameters)
    date_time_string = response.json()["modifiedTime"]
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
        subprocess.call(["python3", f"{PATH}/get_images.py", sheet_id, picture_path])
        subprocess.call(["python3", f"{PATH}/get_csv.py", sheet_id, data_path])
    else:
        print("Data is already updated")
        
    time.sleep(5)

