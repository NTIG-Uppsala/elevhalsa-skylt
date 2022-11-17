#!/usr/bin/python3
import subprocess
import wget, os, openpyxl, pathlib
from openpyxl_image_loader import SheetImageLoader
from PIL import Image, ImageChops
import time
import datetime

updateTime = datetime.datetime.now().strftime('%H:%M')

PATH = pathlib.Path(__file__).parent.absolute()

img_path = f"{PATH}/site/assets/img"
avatar_img_path = img_path + "/avatar.jpg"
profile_img_path = img_path + "/Profile/{}.jpg"

filename = wget.download("https://docs.google.com/spreadsheets/d/1qY1KYAY-AjFh2DWsjiVwOVj2qqJ29kpSs_YaBHi-TEs/export?format=xlsx")
pxl_doc = openpyxl.load_workbook(filename)

def has_changed(sheet):

    image_loader = SheetImageLoader(sheet)
    changed = False

    for row in range(2, sheet.max_row + 1):
        image_filename = sheet["K" + str(row)].value
        image_path = profile_img_path.format(image_filename)
        image = image_loader.get("I" + str(row))
        image.save(image_path)
        changed = True
        return changed

if __name__ == "__main__":
    if updateTime == "17:00":
        has_changed(pxl_doc["NTI"])
        subprocess.run(["xdotool", "key", "F5"])
        time.sleep(60)
