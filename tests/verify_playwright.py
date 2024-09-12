from playwright.sync_api import sync_playwright

def run(playwright):
    #browser = playwright.chromium.launch(executable_path="C:\\Users\\Admin\\AppData\\Local\\ms-playwright\\chromium-1134\chrome-win\chrome.exe"
    browser = playwright.firefox.launch(headless=False)
    page = browser.new_page()
    page.goto("http://example.com")
    print(page.title())
    browser.close()

with sync_playwright() as playwright:
    run(playwright)