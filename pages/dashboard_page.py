# pages/dashboard_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DashboardPage(BasePage):
    WELCOME_BANNER = (By.CSS_SELECTOR, ".welcome-banner")

    def is_logged_in(self):
        return bool(self.find_element(self.WELCOME_BANNER))
