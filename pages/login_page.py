# pages/login_page.py
from enum import Enum
import os
from urllib.parse import parse_qs, urlparse
from objects.login_result_object import LoginResultObject
from pages.base_page import BasePage
import logging
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from typing import Optional
from utils.logger_config import logger
from utils.pwd_manager import PasswordManager  # Import the global logger

# Define the LoginState enum
class LoginState(Enum):
    WAIT_EMAIL = 0
    WAIT_PASSWORD = 1
    WAIT_INBOX = 2

# Define the LoginState enum
class LoginResultCode(Enum):
    success = "success"
    wrong_username = "wrong_username"
    wrong_paswwrod = "wrong_password"    

    def to_string(self):
       return self.value

# Define the selector as a constant
LOGIN_INPUT_EMAIL = 'input[type="email"]'
LOGIN_INPUT_PASWORD = 'input[type="password"]'
BUTTON_NEXT = 'button:has-text("Next")'
SELECTOR_SIGN_IN = "role=link[name='Sign in']"
url = os.getenv("GMAIL_URL")

class LoginPage(BasePage):
    def navigate(self):

        # Read URL from .env
        if not url:
            logger.error("GMAIL_URL not set in .env file")
            raise ValueError("GMAIL_URL not set in .env file")

        logger.info(f"Navigate to URL: {url}")

        self.page.goto(url)

    def login(self, test_data):
        
        try:
            # Fill in the email
            logger.info("Fill in email")
            login_state = LoginState.WAIT_EMAIL
            self.page.wait_for_selector(LOGIN_INPUT_EMAIL, state='visible')
            self.page.fill(LOGIN_INPUT_EMAIL, test_data.username)
           
            # Click the Next button
            logger.info("Click Next button after email")
            self.page.click(BUTTON_NEXT)
            
            # Wait for the password field to be visible
            logger.info("Fill in password")
            login_state = LoginState.WAIT_PASSWORD
            self.page.wait_for_selector(LOGIN_INPUT_PASWORD, state='visible')
            self.page.fill(LOGIN_INPUT_PASWORD, PasswordManager().decrypt_password(test_data.password))

            # Click the Next button
            logger.info("Click Next button after password")            
            self.page.click(BUTTON_NEXT)
            login_state = LoginState.WAIT_INBOX

        except PlaywrightTimeoutError as e:
            logger.error(f"Timeout error during login: {e}")
            #raise
        except Exception as e:
            logger.error(f"An error occurred during login: {e}")
            #raise

        return login_state

    def click_sign_in(self):
        
        try:
            # Wait for the sign-in link to be visible and interactable
            logger.info("Wait for the sign-in link to be visible and interactable")
            self.page.wait_for_selector(SELECTOR_SIGN_IN, state='visible')
            logger.info("Click on the 'Sign in' link")
            self.page.locator(SELECTOR_SIGN_IN).click()
            
        except PlaywrightTimeoutError as e:
            logger.error(f"Timeout error while trying to click 'Sign in' link: {e}")
            raise
        except Exception as e:
            logger.error(f"An error occurred while trying to click 'Sign in' link: {e}")
            raise 
