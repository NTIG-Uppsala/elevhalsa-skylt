import unittest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


# make sure to have a jekyll server up and running before running the tests
# (run "jekyll serve -s site" in an Ubuntu terminal)
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
        pass

    def test_get_csv(self):
        pass


if __name__ == "__main__":
    unittest.main()
