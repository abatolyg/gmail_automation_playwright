# pages/login_page.py
from urllib.parse import parse_qs, urlparse
from objects.login_result_object import LoginResultObject
from pages.base_page import BasePage
import logging
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from typing import Optional
from pages.login_page import LoginResultCode
from utils.logger_config import logger  # Import the global logger

# Define the selector as a constant
INBOX_MAIN_SELECTOR = 'div[role="main"]'
COMPOSE_BUTTON_SELECTOR = 'div[role="button"][gh="cm"]'

class InboxPage(BasePage):

    def check_inbox_main_availble(self):
        
         # Check for successful login
        try:
            # Check for the presence of an element that indicates a successful login (e.g., the inbox).
            logger.info("Check for the presence of an element that indicates a successful login (e.g., the inbox).")
            self.page.wait_for_selector(INBOX_MAIN_SELECTOR) 
            logger.info("Inbox is visible")
            is_inbox_visible = True

            # Extra Check - Check for the compose button
            logger.info("Extra Check - Check for the compose button.")            
            self.page.wait_for_selector(COMPOSE_BUTTON_SELECTOR)
            logger.info("Compose button is visible")
            is_compose_button_visible = True            

            logger.info(f"Login redirected to another URL to compare to expected - {self.page.url}.")            

            return self.BuildLoginResultObject(self.page.url,is_inbox_visible,is_compose_button_visible)
        except Exception as e:
            self.logger.error(f"Login failed: {e}")
            return None  

    def BuildLoginResultObject(self, url: str, is_inbox_visible: bool, is_compose_button_visible: bool) -> Optional[LoginResultObject]:
        """Build and return a LoginResultObject based on the current URL and visibility of inbox and compose button."""
        try:
            # Create and return LoginResultObject
            error_code = LoginResultCode.success.to_string()
            return LoginResultObject(error_code, url, is_inbox_visible, is_compose_button_visible)
        except Exception as e:
            logger.error(f"An error occurred while building LoginResultObject: {e}")
            return None


        