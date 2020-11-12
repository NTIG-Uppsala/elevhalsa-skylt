import subprocess, time, gspread
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as options
from selenium.webdriver.common.by import By

ops = options()
ops.headless = True

driver = webdriver.Firefox(executable_path="tests/geckodriver", options=ops)

gc = gspread.service_account()
sh = gc.open_by_key("1k0qCUQbKvipCa8dhFcFjccRAWVGSeYF_MJwcu1Fy5Ls")

def test_yrke(yrke, expected_salary):
    # Gets the dagens yrke sheet
    sheet = sh.get_worksheet(3)

    placeholder_text = "TEST"
    sheet.update("A6", yrke)
    sheet.update("B6", placeholder_text)
    sheet.update("C6", placeholder_text)
    sheet.update("D6", placeholder_text)

    time.sleep(2)

    subprocess.call(["python3", "parse_salary.py"])

    time.sleep(2)

    driver.get("http://127.0.0.1:4000/")

    driver.execute_script(f'displayProfession("{yrke}")')

    page_source = driver.page_source

    if yrke in page_source and expected_salary in page_source:
        print("\u001b[32mTest successful\u001b[0m")
    else:
        print("\u001b[31mTest failed\u001b[0m")

    sheet.update("A6", "")
    sheet.update("B6", "")
    sheet.update("C6", "")
    sheet.update("D6", "")

yrke = "borrtekniker"
expected_salary = "31 600 kr"
print(f"[*] Testing with yrke {yrke}")
test_yrke(yrke, expected_salary)

yrke = "djurambulansförare "
expected_salary = "29 100 kr"
print(f"[*] Testing with yrke {yrke} to see if it works with å,ä,ö")
test_yrke(yrke, expected_salary)

