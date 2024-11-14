# test_google_apps_menu.py
from selenium.webdriver.common.by import By
import time
from base_test import BaseTest

class GoogleAppsMenuTest(BaseTest):
    def test_google_apps_menu(self):
        driver = self.driver
        apps_menu_button = driver.find_element(By.CSS_SELECTOR, "a[aria-label='Google apps']")
        self.assertTrue(apps_menu_button.is_displayed(), "Google Apps menu icon is not displayed")
        apps_menu_button.click()
        time.sleep(2)
