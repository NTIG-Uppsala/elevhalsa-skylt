import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class TestLocalhostPageTitle(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_experimental_option("detach", True)
        cls.driver = webdriver.Chrome(options=chrome_options)

        cls.driver.get("http://127.0.0.1:4000")

    def test_page_title(self):
        self.assertEqual("EHT-skylt", self.driver.title)


if __name__ == "__main__":
    unittest.main()
