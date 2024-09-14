import json
import os
import logging
from dotenv import load_dotenv
from pages.inbox_page import InboxPage
from pages.login_page import LoginPage
import pytest
from objects.login_object import LoginObject
from objects.login_result_object import LoginResultObject
from utils.logger_config import logger  # Import the global logger

load_dotenv()

def load_json_data(file_path: str):
    """Helper function to load JSON data from a file."""
    try:
        with open(file_path) as f:
            return json.load(f)
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        raise
    except json.JSONDecodeError as e:
        logger.error(f"Error decoding JSON from file {file_path}: {e}")
        raise

@pytest.fixture(scope="module")
def login_object() -> LoginObject:
    """Fixture to provide login object from test data."""
    data = load_json_data('data/test_data.json')
    return LoginObject.from_json(data)

@pytest.fixture(scope="module")
def login_result_object_expected() -> LoginResultObject:
    """Fixture to provide expected login result object from test data."""
    data = load_json_data('data/test_result_expected_data.json')
    return LoginResultObject.from_json(data)

def test_login(page, login_object: LoginObject, login_result_object_expected: LoginResultObject):
    """Test the login functionality."""
    # Create LoginPage object
    login_page = LoginPage(page)

    # Navigate to login page
    login_page.navigate()

    # Perform login
    login_page.login(login_object)
    logger.info("Performed login")
    
    # Retrieve data from Inbox page. 
    inbox_page = InboxPage(page)
    login_result_object = inbox_page.check_inbox_main_availble()    

    # Assert conditions
    assert login_result_object.is_equal(login_result_object_expected), "login_result_object should be equal to login_result_object_expected"
    logger.info("Assertions passed")


    
    



    