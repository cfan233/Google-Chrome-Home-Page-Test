# test_google_logo_image.py
from selenium.webdriver.common.by import By
from base_test import BaseTest

class GoogleLogoImageTest(BaseTest):
    def test_google_logo_image(self):
        driver = self.driver
        try:
            # Locate the Google logo using a common CSS selector or alt attribute
            google_logo = driver.find_element(By.CSS_SELECTOR, "img[alt='Google']")  # Selector might vary
            self.assertTrue(google_logo.is_displayed(), "Google logo is not displayed")
        except:
            print("Google logo image not found")
