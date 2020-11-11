import gspread
import subprocess

from PIL import Image, ImageChops


# Connects to service account
gc = gspread.service_account()
# Opens śpreadhseet by ID
sh = gc.open_by_key("1k0qCUQbKvipCa8dhFcFjccRAWVGSeYF_MJwcu1Fy5Ls")
# Opens specific page on spreadsheet
procivitas = sh.get_worksheet(1)

# Adds "TEST" to columns A trough H
for col in range(1, 9):
    cell = procivitas.update_cell(30, col, "TEST")

subprocess.call(["sh", "get_csv.sh --not-refresh"])
subprocess.call(["python3", "get_images.py"])

placeholder_image = Image.open("site/assets/img/avatar.png")
test_image = Image.open("site/assets/img/Profile/TEST.png") 

# Function to calculate if the images are the same
# https://stackoverflow.com/questions/1927660/compare-two-images-the-python-linux-way/6204954#6204954
if ImageChops.difference(placeholder_image.convert("RGBA"), test_image.convert("RGBA")).getbbox() is None:
    print("\u001b[32mTest successful\u001b[0m")
else:
    print("\u001b[31mTest failed\u001b[0m")

# Removes "TEST" from the cells
for col in range(1, 9):
    cell_value = procivitas.cell(30, col).value
    cell = procivitas.update_cell(30, col, "")