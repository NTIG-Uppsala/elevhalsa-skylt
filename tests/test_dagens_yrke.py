import subprocess, time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as options
from selenium.webdriver.common.by import By

ops = options()
ops.headless = True

subprocess.call(["python3", "parse_salary.py"])

driver = webdriver.Firefox(executable_path="tests/geckodriver", options=ops)

driver.get("http://127.0.0.1:4000/")

time.sleep(2)

print("[*] Testing with yrke brandman")
yrke = "Brandman"
driver.execute_script(f'displayProfession("{yrke}")')

expected_yrke = "brandman"
expected_salary = "32 000 kr"

page_source = driver.page_source

if expected_yrke in page_source and expected_salary in page_source:
    print("\u001b[32mTest successful\u001b[0m")
else:
    print("\u001b[31mTest failed\u001b[0m")


print("[*] Testing with yrke kirurg")
yrke = "Kirurg"
driver.execute_script(f'displayProfession("{yrke}")')

expected_yrke = "Kirurg"
expected_salary = "77 900 kr"

page_source = driver.page_source

if expected_yrke in page_source and expected_salary in page_source:
    print("\u001b[32mTest successful\u001b[0m")
else:
    print("\u001b[31mTest failed\u001b[0m")
