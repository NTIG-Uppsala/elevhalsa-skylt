from selenium import webdriver
from selenium.webdriver.firefox.options import Options as options

ops = options()
ops.headless = True

driver = webdriver.Firefox(executable_path="tests/geckodriver", options=ops)

# Runs website instance
driver.get("http://127.0.0.1:4000/")

pagesource = driver.page_source

# Tries to find the new cell value on the live page
if "Tips" in pagesource:
    print("\u001b[32mTest successful\u001b[0m")
else:
    print("\u001b[31mTest failed\u001b[0m")