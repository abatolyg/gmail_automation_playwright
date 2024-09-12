import json
import os
from dotenv import load_dotenv
from pages.login_page import LoginPage
from urllib.parse import urlparse, parse_qs
import pytest
from objects.login_object import LoginObject
from objects.login_result_object import LoginResultObject

load_dotenv()

@pytest.fixture(scope="module")
def test_data():
    # Read test data from JSON file
    with open('data/test_data.json') as f:
        data = json.load(f)
    return LoginObject.from_json(data)   

def test_login(page, test_data):
    # Read URL from .env
    url = os.getenv("GMAIL_URL")

    # Read test data from JSON file
    with open('data/test_data.json') as f:
        data = json.load(f)

    # Create LoginPage object
    login_page = LoginPage(page)

    # Navigate to login page
    login_page.navigate(url)

    # click_sign_in 
    #login_page.click_sign_in()

    # Perform login
    loginResultObject = login_page.login(test_data.username, test_data.password)
       
    # Assert conditions
    assert loginResultObject.base_url == 'https://accounts.google.com/v3/signin/challenge/pwd', f"Base URL is not correct: {loginResultObject.base_url}"
    assert loginResultObject.service_param == 'mail', f"Service parameter is not correct: {loginResultObject.service_param}"

    print("Assertions passed.")