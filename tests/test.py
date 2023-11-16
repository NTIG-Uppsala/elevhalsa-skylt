import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

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

    def test_visible_slide_present(self):
        self.assertIn("Maria Ohlsson", self.driver.page_source)

    def test_hidden_slide_not_present(self):
        self.assertNotIn("Karl Eriksson", self.driver.page_source)
        self.assertNotIn("Skolsköterska", self.driver.page_source)
        self.assertNotIn("karl.eriksson@example.com", self.driver.page_source)
        self.assertNotIn("018-99 99 99", self.driver.page_source)

    def test_title_present(self):
        self.assertIn("Skolkurator", self.driver.page_source)

    def test_email_present(self):
        self.assertIn("maria.ohlsson@example.com", self.driver.page_source)

    def test_absent_email_icon_not_present(self):
        email_icons_count = self.driver.page_source.count("mail.svg")
        self.assertEqual(2, email_icons_count)

    def test_phone_number_present(self):
        self.assertIn("011-123 45 67", self.driver.page_source)

    def test_work_hours_present(self):
        self.assertIn("8-17", self.driver.page_source)
    
    def test_location_present(self):
        self.assertIn("NTI Gymnasiet Uppsala", self.driver.page_source)

    def test_image_present(self):
        self.driver.find_element(By.CSS_SELECTOR, "img[src$=\"2_Maria_Ohlsson.jpg\"]")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
