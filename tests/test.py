import os
import unittest
import time
import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import filecmp
import shutil
from dotenv import load_dotenv
load_dotenv()
SHEETID = "13y1coklHJzw85RltZv5XXeMbwm_lm--5zXPaK9Ani4Q"

class TestLocalhostPageTitle(unittest.TestCase):
    # Executes before each test
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_experimental_option("detach", True)

        # Set up the Chrome WebDriver in headless mode
        self.driver = webdriver.Chrome(options=chrome_options)

        # Load page
        self.driver.get("http://127.0.0.1:4000")
        time.sleep(1)

    def test_page_title(self):
        self.assertEqual("EHT-skylt", self.driver.title)


class TestLocalScripts(unittest.TestCase):
    # Executes before each test
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_experimental_option("detach", True)

        # Set up the Chrome WebDriver in headless mode
        self.driver = webdriver.Chrome(options=chrome_options)

    def test_get_csv(self):
        downloaded_file = "tests/downloaded_test_data.csv"
        correct_file = "tests/correct_test_data.csv"
        subprocess.call(["python", "get_csv.py", os.getenv("test_sheet_id"), downloaded_file])
        downloaded_file_is_correct = filecmp.cmp(
            downloaded_file, correct_file, shallow=False
        )
        self.assertTrue(downloaded_file_is_correct)

    # A test that creates and writes down all picture sizes.
    # Removes the need to open properties for each image.
    def write_txt_image_sizes(self):
        folder_path = "tests/img/Profile/"
        pictures = os.listdir(folder_path)  # list format
        with open("tests/picture_sizes.txt", "w") as file:
            for picture in pictures:
                size = os.path.getsize(folder_path + picture)
                file.write(f"{picture} is {size}kb big \n")

    def helper_get_images_check_size(self, file_name, expected):  # Expected in Kb
        folder_path = "tests/img/"
        csv_datapath = "tests/downloaded_test_data.csv"
        subprocess.call(["python", "get_csv.py", os.getenv("test_sheet_id"), csv_datapath])
        subprocess.call(["python", "get_images.py", os.getenv("test_sheet_id"), folder_path, csv_datapath])
        picture = f"{folder_path}Profile/{file_name}"
        size = os.path.getsize(picture)
        if size != expected:
            self.fail(f"Picture {picture} is not size {expected}Kb and is {size}Kb")

    def test_get_images(self):
        # Prevent earlier tests from influencing the result of this test
        images_path = "tests/img/"
        if os.path.isdir(images_path):
            shutil.rmtree(images_path)
        
        # Check size of Image
        self.helper_get_images_check_size("2_Maria_Ohlsson.jpg", 36541)
        self.helper_get_images_check_size("3_Karl_Eriksson.jpg", 67545)
        self.helper_get_images_check_size("4_Karl_Jönsson.jpg", 116074)
        self.helper_get_images_check_size("5_Linnéa_Johansson.jpg", 16930)

        # Uncomment to generate a file with a list of image sizes
        self.write_txt_image_sizes()

    def tearDown(self):
        # Close the WebDriver
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
