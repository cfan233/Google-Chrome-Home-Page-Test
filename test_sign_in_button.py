from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_test import BaseTest
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time


class SignInButtonTest(BaseTest):
    def test_sign_in_and_enter_credentials(self):
        driver = self.driver

        # Step 1: Locate and click the "Sign In" button
        try:
            sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
            self.assertTrue(sign_in_button.is_displayed(), "Sign In button is not displayed")
            sign_in_button.click()
            print("Clicked on 'Sign In' button successfully.")
        except NoSuchElementException:
            print("Sign In button not found on the page.")
            return  # Exit the test if Sign In button is not found

        # Step 2: Enter the email address on the login page
        try:
            email_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "identifierId"))
            )
            email_address = "your-email"  # Replace with a test email
            email_input.send_keys(email_address)
            print(f"Email '{email_address}' entered successfully.")

            # Click the "Next" button after entering the email
            next_button = driver.find_element(By.ID, "identifierNext")
            next_button.click()
            print("Clicked 'Next' button after entering email.")
        except TimeoutException:
            print("Timed out waiting for the email input field or Next button.")
            return  # Exit the test if email step fails

        # Step 3: Wait for the password input field, use JavaScript if necessary
        try:
            # Wait until password field is present and visible
            password_input = WebDriverWait(driver, 15).until(
                EC.visibility_of_element_located((By.XPATH, "//input[@type='password']"))
            )

            # Alternative: Use JavaScript to set the password value directly
            password = "your password"  # Replace with a test password
            driver.execute_script("arguments[0].value = arguments[1];", password_input, password)
            print("Password entered successfully using JavaScript.")

            # Click the "Next" button after entering the password
            password_next_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "passwordNext"))
            )
            password_next_button.click()
            print("Clicked 'Next' button after entering password.")
        except TimeoutException:
            print("Timed out waiting for the password input field or Next button.")
        except NoSuchElementException:
            print("Password input field or Next button not found on the password page.")
