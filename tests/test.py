import os
import unittest
import time
import csv
import subprocess
from selenium import webdriver
from selenium.webdriver.common.by import By


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
        subprocess.call(["python", "get_csv.py"])
        # Opens the current csv file with data, then reads and saves every row in a list
        with open("site/_data/stored_data.csv", "r", encoding="utf-8") as r:
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

    def helper_hide_status(self, date):
        self.driver.get("http://127.0.0.1:4000")
        time.sleep(2)
        self.driver.execute_script(
            "updateDisplayedInfo(names, status, latestChanges, arguments[0]);", date
        )

        # Find the element with class "status"
        status_element = self.driver.find_element(By.CLASS_NAME, "status")
        print(status_element)

        # Get the visibility property of the element
        visibility = status_element.value_of_css_property("visibility")

        # Check if the visibility is "visible" and fail the test if it is
        if visibility == "visible":
            self.fail("class status visible")

    def test_hide_status(self):
        self.helper_hide_status("2023-10-10T07:13:21.803Z")

    def tearDown(self):
        # Close the WebDriver
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
