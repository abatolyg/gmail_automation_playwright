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
def login_object():
    # Read test data from JSON file
    with open('data/test_data.json') as f:
        data = json.load(f)
    return LoginObject.from_json(data) 

@pytest.fixture(scope="module")
def login_result_object_expected():
    # Read test data from JSON file
    with open('data/test_result_expected_data.json') as f:
        data = json.load(f)
    return LoginResultObject.from_json(data)   

def test_login(page, login_object, login_result_object_expected):
    # Read URL from .env
    url = os.getenv("GMAIL_URL")

    # Create LoginPage object
    login_page = LoginPage(page)

    # Navigate to login page
    login_page.navigate(url)

    # click_sign_in 
    #login_page.click_sign_in()

    # Perform login
    login_result_object = login_page.login(login_object)   
           
    # Assert conditions
    assert login_result_object.base_url == login_result_object_expected.base_url, f"Base URL is not correct: {login_result_object.base_url}"
    assert login_result_object.service_param == login_result_object_expected.service_param, f"Service parameter is not correct: {login_result_object.service_param}"

    print("Assertions passed.")