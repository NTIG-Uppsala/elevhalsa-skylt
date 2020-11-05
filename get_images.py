#!/usr/bin/python3
import wget, os, openpyxl, pathlib
from openpyxl_image_loader import SheetImageLoader
from PIL import Image, ImageChops

PATH = pathlib.Path(__file__).parent.absolute()

def save_images(sheet):
    image_loader = SheetImageLoader(sheet)
    for col in range(2, sheet.max_row + 1):
        if(sheet["A" + str(col)].value != None):
            image_filename = sheet['B' + str(col)].value
            if not image_loader.image_in("I" + str(col)):
                image = Image.open("{PATH}/site/assets/img/avatar.png")
                image.save(f"{PATH}/site/assets/img/Profile/{image_filename}.png")
            else:
                image = image_loader.get("I" + str(col))
                try:
                    old_image = Image.open(f"{PATH}/site/assets/img/Profile/{image_filename}.png")
                    if not ImageChops.difference(image, old_image).getbbox() is None:
                        image.save(f"{PATH}site/assets/img/Profile/{image_filename}.png")
                except IOError:
                    image.save(f"{PATH}site/assets/img/Profile/{image_filename}.png")

print("DOWNLOADING EXCEL FILE")
url = "https://docs.google.com/spreadsheets/d/1k0qCUQbKvipCa8dhFcFjccRAWVGSeYF_MJwcu1Fy5Ls/export?format=xlsx"
filename = wget.download(url)

pxl_doc = openpyxl.load_workbook(filename)

eht_sheet = pxl_doc["EHT - NTI"]
proc_sheet = pxl_doc["PROCIVITAS"]

save_images(eht_sheet)
save_images(proc_sheet)

os.remove(filename)
