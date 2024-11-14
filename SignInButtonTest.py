# test_sign_in_button.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from BaseTest import BaseTest


class SignInButtonTest(BaseTest):
    def test_sign_in_and_enter_credentials(self):
        driver = self.driver

        # Step 1: Locate and click the "Sign In" button
        sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
        self.assertTrue(sign_in_button.is_displayed(), "Sign In button is not displayed")
        sign_in_button.click()

        # Step 2: Enter the email address on the login page
        try:
            email_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "identifierId"))
            )
            email_address = "abc@gmail.com"  # Replace with a test email
            email_input.send_keys(email_address)
            print(f"Email '{email_address}' entered successfully.")

            # Click the "Next" button after entering the email
            next_button = driver.find_element(By.ID, "identifierNext")
            next_button.click()
            print("Clicked 'Next' button after entering email.")
        except:
            print("Email input field or Next button not found on the login page")
            return  # Exit the test if email step fails

        # Step 3: Wait for the password input field and enter the password
        try:
            password_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "password"))
            )
            password = "9909901aA~"  # Replace with a test password
            password_input.send_keys(password)
            print("Password entered successfully.")

            # Click the "Next" button after entering the password
            password_next_button = driver.find_element(By.ID, "passwordNext")
            password_next_button.click()
            print("Clicked 'Next' button after entering password.")
        except:
            print("Password input field or Next button not found on the password page")
