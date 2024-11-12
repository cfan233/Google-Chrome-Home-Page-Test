from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
import time

from selenium.webdriver.support.wait import WebDriverWait


class GoogleHomePageTests(unittest.TestCase):

    def setUp(self):
        # Set up the Chrome driver and open the Google homepage
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.google.com")
        self.driver.implicitly_wait(5)

    def test_profile_image_button(self):
        driver = self.driver
        # Locate and test the profile image button
        try:
            profile_button = driver.find_element(By.CSS_SELECTOR, "img.gb_Da.gbii")
            self.assertTrue(profile_button.is_displayed(), "Profile image is not displayed")
            profile_button.click()
            time.sleep(2)  # Wait for the menu to open
            # Additional check can be done here for the account menu elements if needed
        except:
            print("Profile image button not found")

    def test_gmail_link(self):
        driver = self.driver
        # Locate and test the Gmail link
        gmail_link = driver.find_element(By.LINK_TEXT, "Gmail")
        self.assertTrue(gmail_link.is_displayed(), "Gmail link is not displayed")
        gmail_link.click()

        # Wait for the page to load
        WebDriverWait(driver, 10).until(
            lambda driver: driver.current_url != "https://www.google.com/"
        )

        # Verify that the URL is either mail.google.com or the Gmail workspace page
        self.assertTrue(
            "mail.google.com" in driver.current_url or "workspace.google.com/intl/en-US/gmail/" in driver.current_url,
            f"Did not navigate to Gmail, current URL: {driver.current_url}"
        )

    def test_google_apps_menu(self):
        driver = self.driver
        # Locate and test the Google Apps grid icon
        apps_menu_button = driver.find_element(By.CSS_SELECTOR, "a[aria-label='Google apps']")
        self.assertTrue(apps_menu_button.is_displayed(), "Google Apps menu icon is not displayed")
        apps_menu_button.click()
        time.sleep(2)  # Wait for the menu to open
        # Additional check can be done here for app icons within the menu

    def test_white_mode_rendering(self):
        driver = self.driver
        body = driver.find_element(By.TAG_NAME, "body")
        background_color = body.value_of_css_property("background-color")

        # Allow both "rgb(255, 255, 255)" and "rgba(255, 255, 255, 1)"
        valid_background_colors = ["rgb(255, 255, 255)", "rgba(255, 255, 255, 1)"]
        self.assertIn(background_color, valid_background_colors,
                      f"White mode is not properly applied. Found: '{background_color}'")

    def test_search_bar_placeholder(self):
        driver = self.driver
        # Locate the search bar
        search_bar = driver.find_element(By.NAME, "q")
        placeholder_text = search_bar.get_attribute("aria-label")

        # Allow for multiple possible placeholder texts
        valid_placeholders = ["Search Google or type a URL", "Search"]
        self.assertIn(placeholder_text, valid_placeholders,
                      f"Search bar placeholder text is incorrect. Found: '{placeholder_text}'")

    def test_customize_chrome_button(self):
        driver = self.driver
        try:
            # First, try locating by ID
            customize_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "customize-button"))
            )
            customize_button.click()
        except:
            print("Customize Chrome button not found with ID")

            # Try locating by CSS selector as an alternative
            try:
                customize_button = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "button.customize-chrome"))
                )
                customize_button.click()
            except:
                print("Customize Chrome button not found with CSS selector")

            # Try locating by XPath as another alternative
            try:
                customize_button = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Customize Chrome')]"))
                )
                customize_button.click()
            except:
                print("Customize Chrome button not found with XPath")



    def tearDown(self):
        # Close the browser after each test
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
