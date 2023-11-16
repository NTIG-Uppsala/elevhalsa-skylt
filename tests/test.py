import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

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


if __name__ == "__main__":
    unittest.main()
