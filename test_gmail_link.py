# test_gmail_link.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base_test import BaseTest

class GmailLinkTest(BaseTest):
    def test_gmail_link(self):
        driver = self.driver
        gmail_link = driver.find_element(By.LINK_TEXT, "Gmail")
        self.assertTrue(gmail_link.is_displayed(), "Gmail link is not displayed")
        gmail_link.click()

        WebDriverWait(driver, 10).until(
            lambda driver: driver.current_url != "https://www.google.com/"
        )

        self.assertTrue(
            "mail.google.com" in driver.current_url or "workspace.google.com/intl/en-US/gmail/" in driver.current_url,
            f"Did not navigate to Gmail, current URL: {driver.current_url}"
        )
