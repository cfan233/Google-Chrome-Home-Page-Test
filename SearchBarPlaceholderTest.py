# SearchBarPlaceholderTest.py
from selenium.webdriver.common.by import By
from BaseTest import BaseTest

class SearchBarPlaceholderTest(BaseTest):
    def test_search_bar_placeholder(self):
        driver = self.driver
        search_bar = driver.find_element(By.NAME, "q")
        placeholder_text = search_bar.get_attribute("aria-label")
        valid_placeholders = ["Search Google or type a URL", "Search"]
        self.assertIn(placeholder_text, valid_placeholders,
                      f"Search bar placeholder text is incorrect. Found: '{placeholder_text}'")
