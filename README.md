
# Google Homepage Automation Tests

This project is a collection of automated tests for verifying the functionality of elements on the Google homepage and the Google sign-in flow. The tests are written in Python using the `unittest` framework and utilize Selenium WebDriver for browser automation. Each test case is structured to verify different components of the Google homepage, including the search functionality, Google apps menu, Gmail link, and sign-in process.

## Project Structure

```
GoogleHomePageTests/
├── BaseTest.py                    # Base test class with setup and optional teardown
├── test_google_logo_image.py       # Test for Google logo image presence
├── test_search_functionality.py    # Test for search functionality
├── test_gmail_link.py              # Test for Gmail link functionality
├── test_google_apps_menu.py        # Test for Google Apps menu
├── test_white_mode_rendering.py    # Test for white mode rendering on the homepage
├── test_search_bar_placeholder.py  # Test for search bar placeholder text
├── test_customize_chrome_button.py # Test for Customize Chrome button
└── test_sign_in_button.py          # Test for Google sign-in button and login flow
```

## Prerequisites

- **Python**: Make sure you have Python 3.x installed.
- **Selenium**: Install the Selenium library via `pip`.
- **Chrome WebDriver**: Download the Chrome WebDriver compatible with your Chrome browser version and add it to your PATH.



## Running the Tests

1. **Run All Tests**:
    ```
    python -m unittest discover
    ```

2. **Run Specific Test**:
    To run a specific test, you can use:
    ```
    python -m unittest test_sign_in_button.py
    ```

## Test Cases

### 1. Google Logo Image Test
   - Verifies that the Google logo image is present on the homepage.

### 2. Search Functionality Test
   - Verifies that the search box is present, accepts input, and provides search results.

### 3. Gmail Link Test
   - Verifies that the Gmail link is visible on the homepage and redirects to Gmail when clicked.

### 4. Google Apps Menu Test
   - Verifies that the Google Apps menu icon is present and opens the apps grid when clicked.

### 5. White Mode Rendering Test
   - Ensures that the homepage background is rendered in white mode.

### 6. Search Bar Placeholder Test
   - Checks that the placeholder text for the search bar is correct.

### 7. Customize Chrome Button Test
   - Verifies the presence of the Customize Chrome button and clicks it if available.

### 8. Sign-In Button Test
   - Clicks the "Sign In" button, enters an email, and then proceeds to enter a password.
   - ### Note for Sign-In Button Test

**Important:**
- This test is intended for demonstration purposes and does not handle MFA (multi-factor authentication) or other advanced security checks that may be associated with the account. The test only verifies the initial steps of the login process.
- **Replace the email and password values in the test code** with your own test credentials to execute the sign-in steps. These credentials are hardcoded for the purpose of testing and should not be used with real, sensitive account information.
- The test will not cover or bypass any additional security measures (such as MFA) that may be required by Google after entering the email and password. 
