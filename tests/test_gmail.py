import json
from dotenv import load_dotenv
from pages.inbox_page import InboxPage
from pages.login_page import LoginPage, LoginResultCode, LoginState
import pytest
from objects.login_object import LoginObject
from objects.login_result_object import LoginResultObject
from utils.test_date_source import LoginObjectDataSource, LoginResultObjectDataSource
from utils.logger_config import logger  # Import the global logger

@pytest.fixture(scope="module")
def json_login_objects():
    """Fixture to provide login objects from a JSON file."""
    with open('data/login_objects.json') as f:
        return json.load(f)

def get_json_login_objects():
    """Function to get login objects from a JSON file for parameterization."""
    with open('data/login_objects.json') as f:
        return json.load(f)

@pytest.mark.parametrize("json_index", range(len(get_json_login_objects())), ids=[obj['testName'] for obj in get_json_login_objects()])
def test_gmail_login_generic(page, json_index, json_login_objects):
    json_login_object = json_login_objects[json_index]

    # Create LoginPage object
    login_page = LoginPage(page)

    # Navigate to login page
    login_page.navigate()

    # Perform login
    logger.info("Perform login")

    login_object = LoginObject.from_json(json_login_object) 
    login_state = login_page.login(login_object)  

    login_result_object_expected = LoginResultObject.from_json(json_login_object)    

    # Execute the corresponding function
    if login_state == LoginState.WAIT_INBOX:
        
          # Retrieve data from Inbox page. 
        logger.info("Retrieve data from Inbox page. check_inbox_main_availble")
        inbox_page = InboxPage(page)
        login_result_object = inbox_page.check_inbox_main_availble()
        
        # Assert conditions
        assert login_result_object.is_equal(login_result_object_expected), "login_result_object should be equal to login_result_object_expected"
        logger.info("Assertions passed")

    elif login_state == LoginState.WAIT_PASSWORD:  
        logger.info("Waiting for password input")
        assert login_result_object_expected.error_code == LoginResultCode.wrong_username.to_string() , "login_result_object_expected.error_code should be equal to 'wrong_username'"
        
    elif login_state == LoginState.WAIT_EMAIL: 
        logger.info("Waiting for password input")

    