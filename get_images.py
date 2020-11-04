#!/usr/bin/python3
import wget, os, openpyxl
from openpyxl_image_loader import SheetImageLoader

def save_images(sheet):
    image_loader = SheetImageLoader(sheet)
    print("Sheet maxrow" + str(sheet.max_row))
    for col in range(2, sheet.max_row):
        if(sheet["A" + str(col)].value != None):
            image = image_loader.get("I" + str(col))
            image_filename = sheet['B' + str(col)].value
            image.save(f"site/assets/img/Profile/{image_filename}.png")

print("DOWNLOADING EXCEL FILE")
url = "https://docs.google.com/spreadsheets/d/1k0qCUQbKvipCa8dhFcFjccRAWVGSeYF_MJwcu1Fy5Ls/export?format=xlsx"
filename = wget.download(url)

pxl_doc = openpyxl.load_workbook(filename)

eht_sheet = pxl_doc["EHT - NTI"]
proc_sheet = pxl_doc["PROCIVITAS"]

save_images(eht_sheet)
save_images(proc_sheet)

os.remove(filename)
