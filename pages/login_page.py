# pages/login_page.py
from urllib.parse import parse_qs, urlparse
from objects.login_result_object import LoginResultObject
from pages.base_page import BasePage
import logging
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from typing import Optional

# Define the selector as a constant
LOGIN_INPUT_EMAIL = 'input[type="email"]'
LOGIN_INPUT_PASWORD = 'input[type="password"]'
BUTTON_NEXT = 'button:has-text("Next")'
SELECTOR_SIGN_IN = "role=link[name='Sign in']"

class LoginPage(BasePage):
    def navigate(self, url: str):
        self.page.goto(url)

    def login(self, test_data):
        
        logger = logging.getLogger(__name__)

        try:
            # Fill in the email
            self.page.wait_for_selector(LOGIN_INPUT_EMAIL, state='visible')
            self.page.fill(LOGIN_INPUT_EMAIL, test_data.username)
            logger.info("Filled in email")

            # Click the Next button
            self.page.click(BUTTON_NEXT)
            logger.info("Clicked Next button after email")

            # Wait for the password field to be visible
            self.page.wait_for_selector(LOGIN_INPUT_PASWORD, state='visible')
            self.page.fill(LOGIN_INPUT_PASWORD, test_data.password)
            logger.info("Filled in password")

            # Click the Next button
            self.page.click(BUTTON_NEXT)
            logger.info("Clicked Next button after password")

        except PlaywrightTimeoutError as e:
            logger.error(f"Timeout error during login: {e}")
            raise
        except Exception as e:
            logger.error(f"An error occurred during login: {e}")
            raise

        return True

    def click_sign_in(self):
        
        logger = logging.getLogger(__name__)

        try:
            # Wait for the sign-in link to be visible and interactable
            self.page.wait_for_selector(SELECTOR_SIGN_IN, state='visible')
            self.page.locator(SELECTOR_SIGN_IN).click()
            logger.info("Clicked on the 'Sign in' link")

        except PlaywrightTimeoutError as e:
            logger.error(f"Timeout error while trying to click 'Sign in' link: {e}")
            raise
        except Exception as e:
            logger.error(f"An error occurred while trying to click 'Sign in' link: {e}")
            raise 
