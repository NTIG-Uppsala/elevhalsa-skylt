import gspread
import subprocess
import time
import os

from selenium import webdriver
from selenium.webdriver.firefox.options import Options as options

ops = options()
ops.headless = True

driver = webdriver.Firefox(executable_path="tests/geckodriver", options=ops)

# Connects to service account
gc = gspread.service_account()
# Opens śpreadhseet by ID
sh = gc.open_by_key("1k0qCUQbKvipCa8dhFcFjccRAWVGSeYF_MJwcu1Fy5Ls")
# Opens specific page on spreadsheet
procivitas = sh.get_worksheet(1)
# Opens specific cell
cell = procivitas.acell("H3").value
# Updates cell
change = procivitas.update("H3", cell + "s")
newcell = procivitas.acell("H3").value

# Runs get_csv.sh
subprocess.call(["sh", "get_csv.sh"])

# Opens website instance
driver.get("http://127.0.0.1:4000/")

pagesource = driver.page_source

# Tries to find the new cell value on the live page
if newcell in pagesource:
    print("Data changed on page successfully!")
else:
    print("ERROR: Test failed")