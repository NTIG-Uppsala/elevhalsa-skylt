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
    "https://www.googleapis.com/auth/drive.metadata.readonly",
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
Parameters = {"supportsAllDrives": True, "fields": "modifiedTime"}
response = requests.get(url, headers={"Authorization": "Bearer " + access_token}, params=Parameters)
dateTimeString = response.json()["modifiedTime"]
datetime = datetime.fromisoformat(dateTimeString.replace("Z", ""))

while True:
    subprocess.call(["python3", f"{PATH}/get_images.py", sheet_id, picture_path])
    subprocess.call(["python3", f"{PATH}/get_csv.py", sheet_id, data_path])
    time.sleep(5)

