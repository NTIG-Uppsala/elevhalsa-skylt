import gspread
import subprocess
import time

from selenium import webdriver
from selenium.webdriver.firefox.options import Options as options

ops = options()
ops.headless = True

# Connects to service account
gc = gspread.service_account()

# Opens śpreadhseet by ID
sh = gc.open_by_key("1k0qCUQbKvipCa8dhFcFjccRAWVGSeYF_MJwcu1Fy5Ls")

# Opens specific page on spreadsheet
proc = sh.get_worksheet(1)

# Opens specific cell
cell = proc.acell("H3").value

# Updates cell
change = proc.update("H3", cell + "s")

# Runs get_csv.sh
subprocess.call(["sh", "get_csv.sh"])



