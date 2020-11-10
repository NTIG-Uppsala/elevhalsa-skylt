import gspread
import subprocess
import time

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as options

ops = options()
ops.headless = True

driver = webdriver.Firefox(executable_path="tests/geckodriver", options=ops)

gc = gspread.service_account()
sh = gc.open_by_key("1k0qCUQbKvipCa8dhFcFjccRAWVGSeYF_MJwcu1Fy5Ls")

procivitas = sh.get_worksheet(1)

cell_range = "K2"

now = datetime.today()
dropin_time = now.strftime('%Y-%m-%d')
dropin_time = dropin_time + " " + str(int(now.strftime('%H')) + 1) + ":" + now.strftime('%M:%S')

cell = procivitas.acell(cell_range).value
change = procivitas.update(cell_range, dropin_time)
newcell = procivitas.acell(cell_range).value

subprocess.call(["sh", "get_csv.sh", "--not-refresh"])

time.sleep(2)

driver.get("http://127.0.0.1:4000/")

pagesource = driver.page_source

if "Tillgänglig för drop-in" in pagesource:
    print("\u001b[32mTest successful\u001b[0m")
else:
    print("\u001b[31mTest failed\u001b[0m")

procivitas.update(cell_range, cell)
