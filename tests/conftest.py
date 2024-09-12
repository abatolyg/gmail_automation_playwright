# tests/conftest.py
import pytest
from playwright.sync_api import sync_playwright
import os

@pytest.fixture(scope="session")
def context():
    user_data_dir = "C:\\Users\\Admin\\AppData\\Local\\Google\\Chrome\\PlaywrightUserData"
    os.makedirs(user_data_dir, exist_ok=True)
    
    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir=user_data_dir,
            headless=False,
            executable_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
            args=[
                "--profile-directory=Default",
                "--disable-blink-features=AutomationControlled",
                "--disable-infobars"
            ]
        )
        yield context
        context.close()

@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    yield page
    page.close()