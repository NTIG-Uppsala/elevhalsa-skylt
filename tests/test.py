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
        sheet_id = "13y1coklHJzw85RltZv5XXeMbwm_lm--5zXPaK9Ani4Q"
        data_path = "tests/stored_data.csv"
        subprocess.call(["python", "get_csv.py", sheet_id, data_path])
        # Opens the current csv file with data, then reads and saves every row in a list
        with open(data_path, "r", encoding="utf-8") as r:
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

    # A test that creates and writes down all picture sizes.
    # Removes the need to open properties for each image.
    def write_txt_image_sizes(self):
        folder_path = "tests/img/Profile/"
        pictures = os.listdir(folder_path)  # list format
        with open("tests/picture_sizes.txt", "w") as file:
            for picture in pictures:
                size = os.path.getsize(folder_path + picture)
                file.write(f"{picture} is {size}kb big \n")

    def helper_get_images_check_size(self, name, expected):  # Expected in Kb
        folder_path = "tests/img/"
        subprocess.call(["python", "get_images.py", SHEET_ID, folder_path])
        picture = f"{folder_path}Profile/{name}.jpg"
        size = os.path.getsize(picture)
        if size != expected:
            self.fail(f"Picture {picture} is not size {expected}Kb and is {size}Kb")

    def test_get_images(self):
        # Check size of Image
        self.helper_get_images_check_size("Karl1", 67545)  # size in Kb
        self.helper_get_images_check_size("Karl2", 99287)
        self.helper_get_images_check_size("Linnea", 16930)
        self.helper_get_images_check_size("Maria", 36541)

        # Uncomment to generate a file with a list of image sizes
        self.write_txt_image_sizes()

    def tearDown(self):
        # Close the WebDriver
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
