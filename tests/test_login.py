# tests/test_login.py
import json
import os
from dotenv import load_dotenv
from pages.login_page import LoginPage
from urllib.parse import urlparse, parse_qs
import pytest

load_dotenv()

@pytest.fixture(scope="module")
def test_data():
    # Read test data from JSON file
    with open('data/test_data.json') as f:
        data = json.load(f)
    return data

def verify_login_succeded(url):

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

    # Assert conditions
    assert base_url == 'https://accounts.google.com/v3/signin/challenge/pwd', f"Base URL is not correct: {base_url}"
    assert service_param == 'mail', f"Service parameter is not correct: {service_param}"

    print("Assertions passed.")

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
    login_page.login(test_data['username'], test_data['password'])

    verify_login_succeded(page.url)  