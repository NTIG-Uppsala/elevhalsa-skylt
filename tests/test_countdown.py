import subprocess
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as options
from selenium.webdriver.common.by import By

ops = options()
ops.headless = True

driver = webdriver.Firefox(executable_path="tests/geckodriver", options=ops)


def test_specific_date(test_date, expected_timer):
    try:
        driver.get("http://127.0.0.1:4000/")
        time.sleep(2)
        driver.execute_script('SetData([{name: "SACO-mässan", info: "Bah blah blah..", date: new Date("2020-11-24")}], new Date("' + test_date + '"))')
        time.sleep(2)
        countdown_boxes = driver.find_elements(By.CLASS_NAME, "countdown-box")
        timer = driver.find_element(By.CLASS_NAME, "timer")
        if expected_timer in timer.get_attribute('innerHTML'):
            print("\u001b[32mTest successful\u001b[0m")
        else:
            print("\u001b[31mTest failed\u001b[0m")
            print("Timer has incorrect text")
    except Exception as err:
        print("\u001b[31mTest failed\u001b[0m")
        print(err)


print("[*] Testing same date as SACO")
test_specific_date("2020-11-24", "Idag")

print("[*] Testing tomorrow date as SACO")
test_specific_date("2020-11-23", "Imorgon")

print("[*] Testing 14 days from SACO")
test_specific_date("2020-11-10", "2 veckor")

print("[*] Testing 13 days from SACO")
test_specific_date("2020-11-11", "13 dagar")

print("[*] Testing two weeks from SACO")
test_specific_date("2020-11-8", "2 veckor")

print("[*] Testing three weeks from SACO")
test_specific_date("2020-11-5", "3 veckor")

print("[*] Testing no important dates")
try:
    driver.execute_script('SetData([])')
    countdown_boxes = driver.find_elements(By.CLASS_NAME, "countdown-box")
    time.sleep(1)
    if(len(countdown_boxes) == 0):
        print("\u001b[32mTest successful\u001b[0m")
    else:
        print("\u001b[31mTest failed\u001b[0m")
        print("Not 0 countdown boxes")
except Exception as err:
    print("\u001b[31mTest failed\u001b[0m")
    print(err)


print("[*] Testing four countdowns visible")
try:
    driver.execute_script('SetData([{name: "SACO-mässan", info: "Bah blah blah..", date: new Date("2020-11-24")}, {name: "SACO-mässan", info: "Bah blah blah..", date: new Date("2020-11-24")}, {name: "SACO-mässan", info: "Bah blah blah..", date: new Date("2020-11-24")}, {name: "SACO-mässan", info: "Bah blah blah..", date: new Date("2020-11-24")}], new Date("2020-11-24"))')
    countdown_boxes = driver.find_elements(By.CLASS_NAME, "countdown-box")
    time.sleep(1)
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
    driver.execute_script('SetData([{name: "SACO-mässan", info: "Bah blah blah..", date: new Date("2020-11-26")}, {name: "SACO-mässan", info: "Bah blah blah..", date: new Date("2020-11-24")}, {name: "SACO-mässan", info: "Bah blah blah..", date: new Date("2020-11-25")}, {name: "SACO-mässan", info: "Bah blah blah..", date: new Date("2020-11-27")}], new Date("2020-11-25"))')
    countdown_boxes = driver.find_elements(By.CLASS_NAME, "countdown-box")
    if(len(countdown_boxes) == 3):
        print("\u001b[32mTest successful\u001b[0m")
    else:
        print("\u001b[31mTest failed\u001b[0m")
        print("More or less than 3 contdown boxes")
except Exception as err:
    print("\u001b[31mTest failed\u001b[0m")
    print(err)

print("[*] Testing more than four countdowns")
try:
    driver.execute_script('SetData([{name: "SACO-mässan", info: "Bah blah blah..", date: new Date("2020-11-24")},{name: "SACO-mässan", info: "Bah blah blah..", date: new Date("2020-11-24")}, {name: "SACO-mässan", info: "Bah blah blah..", date: new Date("2020-11-24")},  {name: "SACO-mässan", info: "Bah blah blah..", date: new Date("2020-11-24")}, {name: "SACO-mässan", info: "Bah blah blah..", date: new Date("2020-11-24")}, {name: "SACO-mässan", info: "Bah blah blah..", date: new Date("2020-11-24")}], new Date("2020-11-24"))')
    countdown_boxes = driver.find_elements(By.CLASS_NAME, "countdown-box")
    time.sleep(1)
    if(len(countdown_boxes) == 4):
        print("\u001b[32mTest successful\u001b[0m")
    else:
        print("\u001b[31mTest failed\u001b[0m")
        print("Not 4 countdown boxes")
except Exception as err:
    print("\u001b[31mTest failed\u001b[0m")
    print(err)
