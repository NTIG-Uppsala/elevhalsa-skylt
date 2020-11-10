#!/usr/bin/python3
import subprocess
import wget, os, openpyxl, pathlib
from openpyxl_image_loader import SheetImageLoader
from PIL import Image, ImageChops

PATH = pathlib.Path(__file__).parent.absolute()

img_path = f"{PATH}/site/assets/img"
avatar_img_path = img_path + "/avatar.png"
profile_img_path = img_path + "/Profile/{}.png"

# Function to calculate if the images are the same
# https://stackoverflow.com/questions/1927660/compare-two-images-the-python-linux-way/6204954#6204954
def img_equal(img1, img2):
    return ImageChops.difference(img1.convert("RGBA"), img2.convert("RGBA")).getbbox() is None

def has_changed(sheet, should_save=True):
    """
    This function checks if the images have changed.

    Parameters:

    sheet (Worksheet): Excel worksheet to check.

    should_save (bool): Whether or not to save new images if changed.

    Returns:
    
    bool: Whether or not any image has changed.
    """

    # Clear _images because the variable is stored as a class variable instead of an instance variable
    SheetImageLoader._images = {}

    image_loader = SheetImageLoader(sheet)

    changed = False

    for row in range(2, sheet.max_row + 1):
        if(sheet["A" + str(row)].value != None):
            image_filename = sheet["B" + str(row)].value
            image_path = profile_img_path.format(image_filename)

            # Checks if the cell does not contain an image
            if not image_loader.image_in("I" + str(row)):
                image = Image.open(avatar_img_path)

                try:
                    # Saves avatar image as profile image if it isn't already in use
                    with Image.open(image_path) as old_image:
                        if (not img_equal(image, old_image)):
                            if (should_save):
                                image.save(image_path)
                            changed = True

                # Runs if there was no existing image file
                except IOError:
                    if (should_save):
                        image.save(image_path)
                    changed = True

            # Runs if the cell contains an image
            else:
                image = image_loader.get("I" + str(row))
                
                try:
                    old_image = Image.open(image_path)

                    # Checks if the images are different
                    if not img_equal(image, old_image):
                        # Saves new image as profile image
                        if (should_save):
                            image.save(image_path)
                        changed = True

                # Runs if there was no existing image file
                except IOError:
                    # Saves new image as profile image
                    if (should_save):
                        image.save(image_path)
                    changed = True
    return changed

def get_images(url):
    print("DOWNLOADING EXCEL FILE")
    filename = wget.download(url)

    pxl_doc = openpyxl.load_workbook(filename)

    refresh = False

    # Sets refresh to True if any of the images have changed
    for sheet in pxl_doc:
        print(refresh)
        refresh = has_changed(sheet) or refresh
        print(refresh)

    os.remove(filename)

    if refresh:
        subprocess.run(["xdotool", "key", "F5"])

if __name__ == "__main__":
    get_images("https://docs.google.com/spreadsheets/d/1k0qCUQbKvipCa8dhFcFjccRAWVGSeYF_MJwcu1Fy5Ls/export?format=xlsx")