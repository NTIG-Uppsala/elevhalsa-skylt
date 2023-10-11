#!/usr/bin/python3
from oauth2client.service_account import ServiceAccountCredentials
import openpyxl, pathlib
from openpyxl_image_loader import SheetImageLoader
import requests

SPREADSHEET_ID = "1qY1KYAY-AjFh2DWsjiVwOVj2qqJ29kpSs_YaBHi-TEs"
CREDENTIALS_JSON_FILE = "client_login.json"

file_path = pathlib.Path(__file__).parent.absolute()
img_path = f"{file_path}/site/assets/img"
avatar_img_path = img_path + "/avatar.jpg"
profile_img_path = img_path + "/Profile/{}.jpg"


scope = ['https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_JSON_FILE, scope)
# from https://stackoverflow.com/a/69776579
access_token = credentials.create_delegated(credentials._service_account_email).get_access_token().access_token
url = "https://www.googleapis.com/drive/v3/files/" + spreadsheet_id + "/export?mimeType=application%2Fvnd.openxmlformats-officedocument.spreadsheetml.sheet"
res = requests.get(url, headers={"Authorization": "Bearer " + access_token})

with open("info.xlsx", 'wb') as f:
    f.write(res.content)

exel_document = openpyxl.load_workbook("info.xlsx")

def has_changed(sheet):
    image_loader = SheetImageLoader(sheet)

    for row in range(2, sheet.max_row + 1):
        image_filename = sheet["K" + str(row)].value
        image_path = profile_img_path.format(image_filename)
        image = image_loader.get("I" + str(row))
        image.save(image_path)

if __name__ == "__main__":
    has_changed(exel_document["NTI"])
