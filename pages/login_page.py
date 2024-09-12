# pages/login_page.py
from pages.base_page import BasePage

class LoginPage(BasePage):
    def navigate(self, url: str):
        self.page.goto(url)

    def login(self, username: str, password: str):
        self.page.fill('input[type="email"]', username)
        self.page.click('button:has-text("Next")')
        self.page.fill('input[type="password"]', password)
        self.page.click('button:has-text("Next")')

    def click_sign_in(self):
        self.page.locator("role=link[name='Sign in']").click()