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
        subprocess.call(["python", "get_csv.py"])
        # Opens the current csv file with data, then reads and saves every row in a list
        with open("site/_data/stored_data.csv", "r", encoding="utf-8") as r:
            currentSheet = []
            csvreader = csv.reader(r)
            for row in csvreader:
                currentSheet.append(row)
        for item in currentSheet:
            if item == []:
                currentSheet.remove(item)
        return currentSheet

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
        # List all files in the folder
        folder_path = "site/assets"

        files = os.listdir(folder_path)

        # Filter for files with the .jpg extension
        jpg_files = [file for file in files if file.lower().endswith(".jpg")]

        for jpg_file in jpg_files:
            file_path = os.path.join(folder_path, jpg_file)

            try:
                # Try to open the image with Pillow to check if it's a valid JPEG
                img = Image.open(file_path)
                print(f"Valid JPEG: {jpg_file}")
                img.close()
            except Exception as e:
                print(f"Invalid JPEG: {jpg_file} - {e}")
        pass

    def tearDown(self):
        # Close the WebDriver
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
