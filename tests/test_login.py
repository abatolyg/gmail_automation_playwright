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

    # Perform login
    login_result_object = login_page.login(login_object)   
           
    # Assert conditions
    assert login_result_object.is_equal(login_result_object_expected), "login_result_object should be equal to login_result_object_expected"

    print("Assertions passed.")




    