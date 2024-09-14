It is mini project with the playwright, pytest and python

Requirements

1. Login to Gmail 
2. Check login completed successfully (by url for now)

See log file with successfull test 
gmail_automation_playwright.log

Details of implementation:

Test Name: test_gmail_login

The same test can be executed with different parameters several times using pytest.mark.parametrize It is DecoratorDesign Pattern implemented using Pytest @pytest.mark.parametrize
Test Parameters: LoginObject and LoginResultObject - taken from TEST_DATA_SOURCE The concept also known Data-driven approach.

TEST_DATA_SOURCE_TYPE:file / or database

TEST_DATA_FILE_PATH default: testsdata/test_data.json DataSource class implements a Singleton Design pattern - return JSON data either from a file or from a database’ based on configuration. Also WebDrive is a good candidate for Singleton Pattern.

Page Object Model (POM) design pattern used Abstraction layer between the test scripts and the web pages. 
It helps organize test code and improve maintainability by separating the page-specific details from the test logic. 
BasePage is base class base.

Logger - write logs to file 
PasswordManager encrypt_password and decrypt_password not to store plaintext

How to run tests Option 
1: From Visual Studio Code 
2: cd to gmail_automation_playwright and run pytest
