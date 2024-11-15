from selenium import webdriver
import unittest
import os


class BaseTest(unittest.TestCase):
    """Base test class to initialize and quit the WebDriver for each test class."""

    def setUp(self):
        # Set Chrome options to remove the automation control message and spoof the user agent
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option("useAutomationExtension", False)
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")

        # Set a common user-agent string to mimic a regular browser
        chrome_options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
        )

        # Initialize the Chrome driver with the modified options
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://www.google.com")
        self.driver.implicitly_wait(20)

    def tearDown(self):
        # Only close if the environment variable CLOSE_BROWSER is set to True
        if os.getenv("CLOSE_BROWSER", "False").lower() == "true":
            self.driver.quit()
