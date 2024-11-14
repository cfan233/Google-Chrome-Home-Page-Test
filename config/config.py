# config/config.py
import os

class Config:
    BASE_URL = "https://google.com"
    USERNAME = os.getenv("TEST_USER", "default_user")
    PASSWORD = os.getenv("TEST_PASS", "default_password")
    HEADLESS = bool(os.getenv("HEADLESS", True))  # Run browser in headless mode
