import os
import unittest
import time
import csv
import subprocess
from selenium import webdriver
from PIL import Image


class TestLocalhostPageTitle(unittest.TestCase):
    # Executes before each test
    def setUp(self):
        # Set up the Chrome WebDriver
        self.driver = webdriver.Chrome()
        # Load page
        self.driver.get("http://127.0.0.1:4000")
        time.sleep(1)

    def test_page_title(self):
        self.assertEqual("EHT-skylt", self.driver.title)


class TestLocalScripts(unittest.TestCase):
    # Executes before each test
    def setUp(self):
        # Set up the Chrome WebDriver
        self.driver = webdriver.Chrome()
        # Load page

    def helper_get_csv(self):
        sheet_id = "1nBV4IsQYctwF6QG8T3KaETD3Eth7-6HlPjf63COFuIk"
        subprocess.call(["python", "get_csv.py", sheet_id])
        # Opens the current csv file with data, then reads and saves every row in a list
        with open("tests/stored_data.csv", "r", encoding="utf-8") as r:
            current_sheet = []
            csvreader = csv.reader(r)
            for row in csvreader:
                current_sheet.append(row)
        # removes empty lists from currentSheet
        current_sheet = [item for item in current_sheet if item != []]
        return current_sheet

    def helper_check_name(self, name_number, expected_result):
        sheet = self.helper_get_csv()
        name = sheet[name_number][0]

        self.assertEqual(expected_result, name)

    # Name_numbers: Megan, 1, Ulrika, 2, Maud 3.....name, n
    def test_check_name(self):
        self.helper_check_name(1, "Megan Sundström")
        self.helper_check_name(2, "Maud Enbom")
        self.helper_check_name(3, "Sarah Hagberg")
        self.helper_check_name(4, "Angelica Wadström")

    def test_get_images(self):
        subprocess.call(["python", "get_images.py"])
        folder_path = "site/assets/img/Profile"
        files = os.listdir(folder_path)

        for file in files:
            if not file.endswith(".gitkeep") and not file.endswith(".jpg"):
                self.fail("There images in other formats than jpg")

    def tearDown(self):
        # Close the WebDriver
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
