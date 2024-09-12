# pages/login_page.py
from urllib.parse import parse_qs, urlparse
from objects.login_result_object import LoginResultObject
from pages.base_page import BasePage

class LoginPage(BasePage):
    def navigate(self, url: str):
        self.page.goto(url)

    def login(self, username: str, password: str):
        self.page.fill('input[type="email"]', username)
        self.page.click('button:has-text("Next")')
        self.page.fill('input[type="password"]', password)
        self.page.click('button:has-text("Next")')

        return self.BuildLoginResultObject(self.page.url)

    def click_sign_in(self):
        self.page.locator("role=link[name='Sign in']").click()

    def BuildLoginResultObject(self,url):

        # Parse the URL
        parsed_url = urlparse(url)

        # Extract the base URL
        base_url = f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}"

        # Extract query parameters
        query_params = parse_qs(parsed_url.query)

        # Retrieve specific parameters
        service_param = query_params.get('service', [None])[0]

        # Print the results
        print(f"Base URL: {base_url}")
        print(f"Service Parameter: {service_param}")

        # Create LoginResultObject
        return  LoginResultObject(base_url=base_url, service_param=service_param)       