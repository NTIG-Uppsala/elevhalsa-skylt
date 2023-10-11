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
        self.driver.get("http://127.0.0.1:4000")
        time.sleep(1)

    def helper_get_csv(self):
        # URLs the service account uses to authorize to google spreadsheets

        scope = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive",
        ]

        # Finds the json file with credentials for the service account, and authorizes the service account to gspread
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            "client_login.json", scope
        )
        client = gspread.authorize(credentials)

        # Opens the spreadsheet containing data and gets all the values from the first index (page) of the spreadsheet
        sh = client.open_by_key("1qY1KYAY-AjFh2DWsjiVwOVj2qqJ29kpSs_YaBHi-TEs")
        rows = sh.get_worksheet(0).get_all_values()

        # Opens the current csv file with data, then reads and saves every row in a list
        with open("site/_data/stored_data.csv", "r", encoding="utf-8") as r:
            currentSheet = []
            csvreader = csv.reader(r)
            for row in csvreader:
                currentSheet.append(row)
        return currentSheet

    def test_get_csv(self):
        sheet = self.helper_get_csv()
        megan_name = sheet[1][0]

        self.assertEqual("Megan Sundström", megan_name)

    def tearDown(self):
        # Close the WebDriver
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
