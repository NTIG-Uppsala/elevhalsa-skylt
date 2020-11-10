#!/usr/bin/python3
import subprocess
import wget, os, openpyxl, pathlib
from openpyxl_image_loader import SheetImageLoader
from PIL import Image, ImageChops

PATH = pathlib.Path(__file__).parent.absolute()

# Function to calculate if the images are the same
# https://stackoverflow.com/questions/1927660/compare-two-images-the-python-linux-way/6204954#6204954
def img_equal(img1, img2):
    return ImageChops.difference(img1.convert("RGBA"), img2.convert("RGBA")).getbbox() is None

def save_images(sheet, image_loader):
    refresh = False
    for row in range(2, sheet.max_row + 1):
        if(sheet["A" + str(row)].value != None):
            image_filename = sheet["B" + str(row)].value
            # Checks if the cell does not contain an image
            if not image_loader.image_in("I" + str(row)):
                image = Image.open(f"site/assets/img/avatar.png")
                
                try:
                    # Saves avatar image as profile image if it isn't already in use
                    with Image.open(f"site/assets/img/Profile/{image_filename}.png") as old_image:
                        if (not img_equal(image, old_image)):
                            raise IOError

                # Runs if there was no existing image file
                except IOError:
                    image.save(f"site/assets/img/Profile/{image_filename}.png")
                    refresh = True

            # The cell contains
            else:
                image = image_loader.get("I" + str(row))
                try:
                    old_image = Image.open(f"site/assets/img/Profile/{image_filename}.png")
                    # Checks if the images are different
                    if not img_equal(image, old_image):
                        image.save(f"site/assets/img/Profile/{image_filename}.png")
                        refresh = True

                except IOError:
                    image.save(f"site/assets/img/Profile/{image_filename}.png")
                    refresh = True
    #if refresh:
    #    subprocess.run(["xdotool", "key", "F5"])
    return refresh

print("DOWNLOADING EXCEL FILE")
url = "https://docs.google.com/spreadsheets/d/1k0qCUQbKvipCa8dhFcFjccRAWVGSeYF_MJwcu1Fy5Ls/export?format=xlsx"
filename = wget.download(url)

pxl_doc = openpyxl.load_workbook(filename)

nti_sheet = pxl_doc["NTI"]
nti_image_loader = SheetImageLoader(nti_sheet)
print(save_images(nti_sheet, nti_image_loader))

# Empties the dictionary the images are stored in
SheetImageLoader._images = {}

proc_sheet = pxl_doc["PROCIVITAS"]
proc_image_loader = SheetImageLoader(proc_sheet)
print(save_images(proc_sheet, proc_image_loader))

os.remove(filename)
