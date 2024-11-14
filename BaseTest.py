# BaseTest.py
from selenium import webdriver
import unittest
import os

class BaseTest(unittest.TestCase):
    """Base test class to initialize and quit the WebDriver for each test class."""

    def setUp(self):
        # Set up the Chrome driver and open the Google homepage
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.google.com")
        self.driver.implicitly_wait(20)

    def tearDown(self):
        # Only close if the environment variable CLOSE_BROWSER is set to True
        if os.getenv("CLOSE_BROWSER", "False").lower() == "true":
            self.driver.quit()
