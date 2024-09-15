import json
import logging
import pytest
from playwright.sync_api import sync_playwright
import os
from utils.logger_config import logger  # Import the global logger

USER_DATA_DIR = os.getenv("USER_DATA_DIR")
CHROMIUM_EXECUTABLE_PATH = os.getenv("CHROMIUM_EXECUTABLE_PATH")
FIREFOX_EXECUTABLE_PATH = os.getenv("FIREFOX_EXECUTABLE_PATH")
BROWSER_CONTEXT_SET_DEFAULT_TIMEOUT = os.getenv("BROWSER_CONTEXT_SET_DEFAULT_TIMEOUT")


@pytest.fixture(scope="session", params=["chromium", "firefox"])
def context(request):
    browser_type = request.param
    os.makedirs(USER_DATA_DIR, exist_ok=True)
    
    with sync_playwright() as p:
        if browser_type == "chromium":
            browser = p.chromium
            executable_path = CHROMIUM_EXECUTABLE_PATH
            args = [
                "--profile-directory=Default",
                "--disable-blink-features=AutomationControlled",
                "--disable-infobars"
            ]
            user_agent = None
        elif browser_type == "firefox":
            browser = p.firefox
            executable_path = FIREFOX_EXECUTABLE_PATH
            args = [
                "--disable-blink-features=AutomationControlled",
                "--disable-infobars",
                "--no-remote"
            ]
            user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0"

        context = browser.launch_persistent_context(
            user_data_dir=USER_DATA_DIR,
            headless=False,
            executable_path=executable_path,
            args=args,
            user_agent=user_agent,
            viewport={"width": 1280, "height": 800}
        )

        context.set_default_timeout(BROWSER_CONTEXT_SET_DEFAULT_TIMEOUT)  # Set default timeout in milliseconds

        yield context
        context.close()

@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    yield page
    page.close()