"""
    Polysafe - User testing.
    Description:    Simulates user interactions for polysafe with Selenium.
    File name:      pipeline.py
    Author:         Charles De Lafontaine
    Last edition:   07/25/2021
"""
from start.start_connection_test import *
from start.start_creation_test import *
from start.start_reset_password_test import *
from start.start_account_home_test import *
from tests.test_account_home import *


def main():
    print_header("PIPELINE", "Running tests by multi-threading.")
    connection_test = StartConnectionTest("CONNECTION_TEST", "Starting connection tests...")
    connection_test.start()

    creation_test = StartCreationTest("CREATION_TEST", "Starting creation tests...")
    creation_test.start()

    test_reset_password = StartResetPasswordTest("RESET_PASSWORD_TEST", "Starting reset password tests...")
    test_reset_password.start()

    test_account_home = StartAccountHomeTest("ACCOUNT_HOME_TEST", "Starting account home tests...")
    test_account_home.start()


if __name__ == '__main__':
    print_header("PIPELINE", "Starting...")
    main()
