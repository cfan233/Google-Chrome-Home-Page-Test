# test_search_functionality.py
from selenium.webdriver.common.by import By
from BaseTest import BaseTest

class SearchFunctionalityTest(BaseTest):
    def test_search_box_present(self):
        search_box = self.driver.find_element(By.NAME, "q")
        self.assertTrue(search_box.is_displayed(), "Search box is not displayed")

    def test_search_action(self):
        search_box = self.driver.find_element(By.NAME, "q")
        search_box.send_keys("Hello World")
        search_box.submit()
        self.assertNotEqual(self.driver.current_url, "https://www.google.com", "Search did not work")
