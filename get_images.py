#!/usr/bin/python3
from oauth2client.service_account import ServiceAccountCredentials
import openpyxl
from openpyxl_image_loader import SheetImageLoader
import pathlib
import requests

SPREADSHEET_ID = "1qY1KYAY-AjFh2DWsjiVwOVj2qqJ29kpSs_YaBHi-TEs"
CREDENTIALS_JSON_FILE = "client_login.json"

file_path = pathlib.Path(__file__).parent.absolute()
img_path = f"{file_path}/site/assets/img"
profile_img_path = img_path + "/Profile/{}.jpg"

scope = ['https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_JSON_FILE, scope)
# from https://stackoverflow.com/a/69776579
access_token = credentials.create_delegated(credentials._service_account_email).get_access_token().access_token
# MIME type from https://developers.google.com/drive/api/guides/ref-export-formats
mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
url = f"https://www.googleapis.com/drive/v3/files/{SPREADSHEET_ID}/export?mimeType={mime_type}"
res = requests.get(url, headers={"Authorization": "Bearer " + access_token})

with open("info.xlsx", 'wb') as file:
    file.write(res.content)

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
