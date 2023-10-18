import sys
import os
import pathlib
from oauth2client.service_account import ServiceAccountCredentials
import openpyxl
from openpyxl_image_loader import SheetImageLoader
import requests

# cli arguments are used in the script to specify path and sheet id

SPREADSHEET_ID = sys.argv[1]
CREDENTIALS_JSON_FILE = "service_account_credentials.json"

# Get the image path from command-line arguments (sys.argv)
if len(sys.argv) < 3:
    print("Usage: python script.py <image_path>")
    sys.exit(1)
img_path = sys.argv[2]

# Check if the 'Profile' folder exists or create it
profile_folder_path = os.path.join(img_path, "Profile")
if not os.path.exists(profile_folder_path):
    os.makedirs(profile_folder_path)
    print(f"Folder '{profile_folder_path}' created.")
else:
    print(f"Folder '{profile_folder_path}' already exists.")

# Set the profile image path
profile_img_path = os.path.join(profile_folder_path, "{}.jpg")


scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_JSON_FILE, scope
)
# from https://stackoverflow.com/a/69776579
access_token = (
    credentials.create_delegated(credentials._service_account_email)
    .get_access_token()
    .access_token
)
# MIME type from https://developers.google.com/drive/api/guides/ref-export-formats
mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
url = f"https://www.googleapis.com/drive/v3/files/{SPREADSHEET_ID}/export?mimeType={mime_type}"
response = requests.get(url, headers={"Authorization": "Bearer " + access_token})

with open("info.xlsx", "wb") as file:
    file.write(response.content)

exel_spreadsheet = openpyxl.load_workbook("info.xlsx")["NTI"]
image_loader = SheetImageLoader(exel_spreadsheet)

for row in range(2, exel_spreadsheet.max_row + 1):
    image_filename = exel_spreadsheet["K" + str(row)].value
    image_path = profile_img_path.format(image_filename)
    image = image_loader.get("I" + str(row))
    image.save(image_path)

os.remove("info.xlsx")
