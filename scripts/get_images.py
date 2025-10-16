import csv
import os
import shutil 
from openpyxl import load_workbook
import requests
from credentials import get_access_token
from openpyxl_image_loader import SheetImageLoader

def get_images(sheet_id, csv_data_path):
    SITE_PROFILEPICS = "./site/_profilepics"
    os.makedirs(SITE_PROFILEPICS, exist_ok=True)

    access_token = get_access_token()
    # MIME type from https://developers.google.com/drive/api/guides/ref-export-formats
    mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    url = f"https://www.googleapis.com/drive/v3/files/{sheet_id}/export?mimeType={mime_type}"
    response = requests.get(url, headers={"Authorization": "Bearer " + access_token})

    # This file is opened in binary write mode ("wb") because the response from Google API is in binary.
    # Read more about this at https://developers.google.com/drive/api/reference/rest/v3/files/export
    with open("info.xlsx", "wb") as file:
        file.write(response.content)

    with open("info.xlsx", "wb") as f:
        f.write(response.content)

    wb = load_workbook("info.xlsx")["NTI"]
    image_loader = SheetImageLoader(wb)

    stored_csv_data = list(csv.reader(open(csv_data_path, "r", encoding="utf-8")))
    image_filename_col = stored_csv_data[0].index("FILNAMN")
    image_col_number = [cell.value for cell in wb[1]].index("BILD") + 1

    for row in range(2, wb.max_row + 1):
        image_filename = stored_csv_data[row - 1][image_filename_col]
        # Create image cell name from column and row numbers
        image_cell_name = chr(ord("A") + image_col_number - 1) + str(row)
        image = image_loader.get(image_cell_name)
        image.save(os.path.join(SITE_PROFILEPICS, image_filename))

    os.remove("info.xlsx")

    DEST_PROFILEPICS = "./_site/_profilepics"
    os.makedirs(DEST_PROFILEPICS, exist_ok=True)

    for filename in os.listdir(SITE_PROFILEPICS):
        shutil.copy2(os.path.join(SITE_PROFILEPICS, filename), os.path.join(DEST_PROFILEPICS, filename))
