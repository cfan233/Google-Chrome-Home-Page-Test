# tests/regression_tests/test_login.py
import pytest
from selenium import webdriver
from config.config import Config
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.helpers import load_test_data

test_data = load_test_data("data/test_data.json")

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.headless = Config.HEADLESS
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_valid_login(driver):
    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)
    login_page.load()
    login_page.login(test_data["valid_login"]["username"], test_data["valid_login"]["password"])
    assert dashboard_page.is_logged_in(), "User should be logged in with valid credentials."

def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login(test_data["invalid_login"]["username"], test_data["invalid_login"]["password"])
    # Verify error message appears or user is not logged in
    assert not dashboard_page.is_logged_in(), "User should not be logged in with invalid credentials."
