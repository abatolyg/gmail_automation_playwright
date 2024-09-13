import pytest
from playwright.sync_api import sync_playwright
import os

@pytest.fixture(scope="session", params=["chromium", "firefox"])
def context(request):
    browser_type = request.param
    user_data_dir = f"C:\\Users\\Admin\\AppData\\Local\\Google\\Chrome\\PlaywrightUserData"
    os.makedirs(user_data_dir, exist_ok=True)
    
    with sync_playwright() as p:
        if browser_type == "chromium":
            browser = p.chromium
            executable_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            args = [
                "--profile-directory=Default",
                "--disable-blink-features=AutomationControlled",
                "--disable-infobars"
            ]
            user_agent = None
        elif browser_type == "firefox":
            browser = p.firefox
            executable_path = None  # Use default Firefox executable
            args = [
                "--disable-blink-features=AutomationControlled",
                "--disable-infobars",
                "--no-remote"
            ]
            user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0"

        context = browser.launch_persistent_context(
            user_data_dir=user_data_dir,
            headless=False,
            executable_path=executable_path,
            args=args,
            user_agent=user_agent,
            viewport={"width": 1280, "height": 800}
        )

        # Additional steps to make the browser less detectable
        context.add_init_script("""
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            });
            window.navigator.chrome = {
                runtime: {},
                // Add more properties if needed
            };
            Object.defineProperty(navigator, 'languages', {
                get: () => ['en-US', 'en']
            });
            Object.defineProperty(navigator, 'plugins', {
                get: () => [1, 2, 3, 4, 5]
            });
        """)

        yield context
        context.close()

@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    yield page
    page.close()