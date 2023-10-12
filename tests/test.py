import unittest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import gspread
import subprocess

from datetime import datetime

import csv
import gspread
from oauth2client.service_account import ServiceAccountCredentials


# make sure to have a jekyll server up and running before running the tests
# (run "jekyll serve -s site" in an Ubuntu terminal while in the repo directory)


class TestLocalhostPageTitle(unittest.TestCase):
    # Executes before each test
    def setUp(self):
        # Set up the Chrome WebDriver
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        # Load page
        self.driver.get("http://127.0.0.1:4000")
        time.sleep(1)

    def test_page_title(self):
        self.assertEqual("EHT-skylt", self.driver.title)


class TestLocalScripts(unittest.TestCase):
    # Executes before each test
    def setUp(self):
        # Set up the Chrome WebDriver
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        # Load page

    def helper_get_csv(self):
        subprocess.call(["python", "./get_csv.py"])
        # Opens the current csv file with data, then reads and saves every row in a list
        with open("site/_data/stored_data.csv", "r", encoding="utf-8") as r:
            currentSheet = []
            csvreader = csv.reader(r)
            for row in csvreader:
                currentSheet.append(row)
        return currentSheet

    def helper_check_name(self, name_number, expected_result):
        sheet = self.helper_get_csv()
        name = sheet[name_number][0]

        self.driver.get("http://127.0.0.1:4000")
        time.sleep(1)

        self.assertEqual(expected_result, name)

    # Megan is 2, Ulrika,
    def test_check_name(self):
        self.helper_check_name(2, "Megan Sundström")

    def tearDown(self):
        # Close the WebDriver
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
