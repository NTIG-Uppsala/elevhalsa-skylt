import csv
import sys
import os
import pathlib
import openpyxl
from openpyxl_image_loader import SheetImageLoader
import requests
from credentials import get_access_token

# cli arguments are used in the script to specify path and sheet id

SPREADSHEET_ID = sys.argv[1]
CREDENTIALS_JSON_FILE = "service_account_credentials.json"

# Get the image path from command-line arguments (sys.argv)
if len(sys.argv) < 4:
    print("Usage: python get_images.py <spreadsheet_id> <img_path> <csv_data_path>")
    sys.exit(1)
img_path = sys.argv[2]
csv_data_path = sys.argv[3]

# Check if the 'Profile' folder exists or create it
profile_folder_path = os.path.join(img_path, "Profile")
if not os.path.exists(profile_folder_path):
    os.makedirs(profile_folder_path)
    print(f"Folder '{profile_folder_path}' created.")
else:
    print(f"Folder '{profile_folder_path}' already exists.")

# Set the profile image path
profile_img_path = os.path.join(profile_folder_path, "{}")

access_token = get_access_token()
# MIME type from https://developers.google.com/drive/api/guides/ref-export-formats
mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
url = f"https://www.googleapis.com/drive/v3/files/{SPREADSHEET_ID}/export?mimeType={mime_type}"
response = requests.get(url, headers={"Authorization": "Bearer " + access_token})

# This file is opened in binary write mode ("wb") because the response from Google API is in binary.
# Read more about this at https://developers.google.com/drive/api/reference/rest/v3/files/export
with open("info.xlsx", "wb") as file:
    file.write(response.content)

exel_spreadsheet = openpyxl.load_workbook("info.xlsx")["NTI"]
image_loader = SheetImageLoader(exel_spreadsheet)

# Find the columns of images and image filenames
first_row = exel_spreadsheet[1]
first_row_values = [cell.value for cell in first_row]
image_column_number = first_row_values.index("BILD") + 1

stored_csv_data = []
with open(csv_data_path, "r", encoding="utf-8") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        stored_csv_data.append(row)

image_filename_column_index = stored_csv_data[0].index("FILNAMN")

for row in range(2, exel_spreadsheet.max_row + 1):
    image_filename = stored_csv_data[row - 1][image_filename_column_index]
    # Create a full path to the image file by formatting the 'profile_img_path' with the image filename.
    image_path = profile_img_path.format(image_filename)
    # Create image cell name from column and row numbers
    image_cell_name = chr(ord("A") + image_column_number - 1) + str(row)
    image = image_loader.get(image_cell_name)
    image.save(image_path)

os.remove("info.xlsx")
