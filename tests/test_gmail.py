from dotenv import load_dotenv
from pages.inbox_page import InboxPage
from pages.login_page import LoginPage
import pytest
from objects.login_object import LoginObject
from objects.login_result_object import LoginResultObject
from utils.test_date_source import LoginObjectDataSource, LoginResultObjectDataSource
from utils.logger_config import logger  # Import the global logger

@pytest.fixture(scope="module")
def login_object() -> LoginObject:
    """Fixture to provide login object from test data."""
    return LoginObjectDataSource().get_data()

@pytest.fixture(scope="module")
def login_result_object_expected() -> LoginResultObject:
    """Fixture to provide expected login result object from test data."""
    return LoginResultObjectDataSource().get_data()

def test_gmail_login(page, login_object: LoginObject, login_result_object_expected: LoginResultObject):
    """Test the gmail login functionality."""
    # Create LoginPage object
    login_page = LoginPage(page)

    # Navigate to login page
    login_page.navigate()

    # Perform login
    logger.info("Perform login")
    login_page.login(login_object)
        
    # Retrieve data from Inbox page. 
    logger.info("Retrieve data from Inbox page. check_inbox_main_availble")
    inbox_page = InboxPage(page)
    login_result_object = inbox_page.check_inbox_main_availble()    

    # Assert conditions
    assert login_result_object.is_equal(login_result_object_expected), "login_result_object should be equal to login_result_object_expected"
    logger.info("Assertions passed")  