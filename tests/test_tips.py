import gspread, subprocess, time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as options

ops = options()
ops.headless = True

driver = webdriver.Firefox(executable_path="tests/geckodriver", options=ops)

gc = gspread.service_account()

sh = gc.open_by_key("1k0qCUQbKvipCa8dhFcFjccRAWVGSeYF_MJwcu1Fy5Ls")

procivitas = sh.get_worksheet(1)

cell_range = "J2"
cell = procivitas.acell(cell_range).value

change = procivitas.update(cell_range, "Testing tips functionallity.")
newcell = procivitas.acell(cell_range).value

subprocess.call(["sh", "get_csv.sh"])

time.sleep(2)

# Runs website instance
driver.get("http://127.0.0.1:4000/")

pagesource = driver.page_source

# Tries to find the new cell value on the live page
if newcell in pagesource:
    print("\u001b[32mTest successful\u001b[0m")
else:
    print("\u001b[31mTest failed\u001b[0m")

procivitas.update(cell_range, cell)
