# pages/login_page.py
from urllib.parse import parse_qs, urlparse
from objects.login_result_object import LoginResultObject
from pages.base_page import BasePage
import logging
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from typing import Optional

logger = logging.getLogger(__name__)

# Define the selector as a constant
INBOX_MAIN_SELECTOR = 'div[role="main"]'

class InboxPage(BasePage):

    def check_inbox_main_availble(self):
        
         # Check for successful login
        try:
            self.page.wait_for_selector(INBOX_MAIN_SELECTOR)  # Adjust the selector and timeout as needed
            logger.info("Login successful, inbox is visible")
            return self.BuildLoginResultObject(self.page.url)
        except Exception as e:
            logger.error(f"Login failed: {e}")
            return None
        
    def BuildLoginResultObject(self, url: str) -> Optional[LoginResultObject]:

        try:
            # Create and return LoginResultObject
            return LoginResultObject(url, "")

        except Exception as e:
            logger.error(f"An error occurred while building LoginResultObject: {e}")
            return None                       
            


        