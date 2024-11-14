# test_white_mode_rendering.py
from selenium.webdriver.common.by import By
from base_test import BaseTest

class WhiteModeRenderingTest(BaseTest):
    def test_white_mode_rendering(self):
        driver = self.driver
        body = driver.find_element(By.TAG_NAME, "body")
        background_color = body.value_of_css_property("background-color")
        valid_background_colors = ["rgb(255, 255, 255)", "rgba(255, 255, 255, 1)"]
        self.assertIn(background_color, valid_background_colors,
                      f"White mode is not properly applied. Found: '{background_color}'")
