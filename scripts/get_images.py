import csv
import os
import openpyxl
import requests
from credentials import get_access_token
from openpyxl_image_loader import SheetImageLoader

def get_images(sheet_id, csv_data_path):
    IMAGES_FOLDER_PATH = "./site/profilepics" 

    access_token = get_access_token()
    # MIME type from https://developers.google.com/drive/api/guides/ref-export-formats
    mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    url = f"https://www.googleapis.com/drive/v3/files/{sheet_id}/export?mimeType={mime_type}"

    if not os.path.exists(IMAGES_FOLDER_PATH):
        os.makedirs(IMAGES_FOLDER_PATH)

    response = requests.get(url, headers={"Authorization": "Bearer " + access_token})

    # This file is opened in binary write mode ("wb") because the response from Google API is in binary.
    # Read more about this at https://developers.google.com/drive/api/reference/rest/v3/files/export
    with open("info.xlsx", "wb") as file:
        file.write(response.content)

    excel_spreadsheet = openpyxl.load_workbook("info.xlsx")["NTI"]
    image_loader = SheetImageLoader(excel_spreadsheet)

    # Find the columns of images and image filenames
    first_row = excel_spreadsheet[1]
    first_row_values = [cell.value for cell in first_row]
    image_column_number = first_row_values.index("BILD") + 1

    stored_csv_data = []
    with open(csv_data_path, "r", encoding="utf-8") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            stored_csv_data.append(row)

    image_filename_column_index = stored_csv_data[0].index("FILNAMN")

    for row in range(2, excel_spreadsheet.max_row + 1):
        image_filename = stored_csv_data[row - 1][image_filename_column_index]
        image_path = os.path.join(IMAGES_FOLDER_PATH, image_filename)
        # Create image cell name from column and row numbers
        image_cell_name = chr(ord("A") + image_column_number - 1) + str(row)
        image = image_loader.get(image_cell_name)
        image.save(image_path)

    os.remove("info.xlsx")
