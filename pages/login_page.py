# pages/login_page.py
from selenium.webdriver.common.by import By
from config.config import Config
from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def load(self):
        self.open_url(Config.BASE_URL)

    def login(self, username, password):
        self.find_element(self.USERNAME_INPUT).send_keys(username)
        self.find_element(self.PASSWORD_INPUT).send_keys(password)
        self.find_element(self.LOGIN_BUTTON).click()
