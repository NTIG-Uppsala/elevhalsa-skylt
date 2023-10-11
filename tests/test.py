import unittest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import gspread
import subprocess

from datetime import datetime


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

    def tearDown(self):
        # Close the WebDriver
        self.driver.quit()


class TestLocalScripts(unittest.TestCase):
    # Executes before each test
    def setUp(self):
        # Set up the Chrome WebDriver
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        # Load page
        self.driver.get("http://127.0.0.1:4000")
        time.sleep(1)

    def test_get_csv(self):
        # Run get_csv and save variable both from gspread and in the website
        # change a variable in gspread
        # Run step one again and check if both equal each other
        # change it back

        pass


if __name__ == "__main__":
    unittest.main()