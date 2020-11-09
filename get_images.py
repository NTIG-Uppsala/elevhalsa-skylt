#!/usr/bin/python3
import subprocess
import wget, os, openpyxl, pathlib
from openpyxl_image_loader import SheetImageLoader
from PIL import Image, ImageChops

PATH = pathlib.Path(__file__).parent.absolute()

def save_images(sheet, image_loader):
    refresh = False
    for row in range(2, sheet.max_row + 1):
        if(sheet["A" + str(row)].value != None):
            image_filename = sheet["B" + str(row)].value
            # Checks if the cell contains an image
            if not image_loader.image_in("I" + str(row)):
                image = Image.open(f"site/assets/img/avatar.png")
                image.save(f"site/assets/img/Profile/{image_filename}.png")
                refresh = True
            else:
                image = image_loader.get("I" + str(row))
                try:
                    old_image = Image.open(f"site/assets/img/Profile/{image_filename}.png")
                    # Checks if the images are different
                    if not ImageChops.difference(image.convert("RGBA"), old_image.convert("RGBA")).getbbox() is None:
                        image.save(f"site/assets/img/Profile/{image_filename}.png")
                        refresh = True

                except IOError:
                    image.save(f"site/assets/img/Profile/{image_filename}.png")
                    refresh = True
    if refresh:
        subprocess.run(["xdotool", "key", "F5"])

print("DOWNLOADING EXCEL FILE")
url = "https://docs.google.com/spreadsheets/d/1k0qCUQbKvipCa8dhFcFjccRAWVGSeYF_MJwcu1Fy5Ls/export?format=xlsx"
filename = wget.download(url)

pxl_doc = openpyxl.load_workbook(filename)

nti_sheet = pxl_doc["NTI"]
nti_image_loader = SheetImageLoader(nti_sheet)
save_images(nti_sheet, nti_image_loader)

# Empties the dictionary the images are stored in
SheetImageLoader._images = {}

proc_sheet = pxl_doc["PROCIVITAS"]
proc_image_loader = SheetImageLoader(proc_sheet)
save_images(proc_sheet, proc_image_loader)

os.remove(filename)
