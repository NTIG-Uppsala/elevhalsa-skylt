import subprocess
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as options
from selenium.webdriver.common.by import By

ops = options()
ops.headless = True

subprocess.call(["sh", "get_csv.sh", "--not-refresh"])

driver = webdriver.Firefox(executable_path="tests/geckodriver", options=ops)

driver.get("http://127.0.0.1:4000/")

def test_specific_date(test_date, expected_timer):
    year, month, day = test_date.split("-")
    try:
        driver.execute_script(f"displayCountdowns(new Date({year}, {month}, {day}))")
        time.sleep(1)
        countdown_boxes = driver.find_elements(By.CLASS_NAME, "countdown-box")
        timer = countdown_boxes[0].find_element("timer")
        if timer.text == expected_timer:
            print("\u001b[32mTest successful\u001b[0m")
        else:
            print("\u001b[31mTest failed\u001b[0m")
            print("Timer has incorrect text")
    except Exception as err:
        print("\u001b[31mTest failed\u001b[0m")
        print(err)


print("[*] Testing same date as SACO")
test_specific_date("2020-11-24", "Idag")

print("[*] Testing 13 days from SACO")
test_specific_date("2020-11-11", "13 dagar")

print("[*] Testing two weeks from SACO")
test_specific_date("2020-11-8", "2 veckor")

print("[*] Testing three weeks from SACO")
test_specific_date("2020-11-5", "3 veckor")

print("[*] Testing two months from SACO")
test_specific_date("2020-9-24", "2 månader")


print("[*] Testing four countdowns visible")
try:
    countdown_boxes = driver.find_elements(By.CLASS_NAME, "countdown-box")
    if(len(countdown_boxes) == 4):
        print("\u001b[32mTest successful\u001b[0m")
    else:
        print("\u001b[31mTest failed\u001b[0m")
        print("Not 4 countdown boxes")
except Exception as err:
    print("\u001b[31mTest failed\u001b[0m")
    print(err)

print("[*] Testing only three countdowns after SACO passed")
try:
    countdown_boxes = driver.find_elements(By.CLASS_NAME, "countdown-box")
    if(len(countdown_boxes) == 3):
        print("\u001b[32mTest successful\u001b[0m")
    else:
        print("\u001b[31mTest failed\u001b[0m")
        print("More or less than 3 contdown boxes")
except Exception as err:
    print("\u001b[31mTest failed\u001b[0m")
    print(err)
