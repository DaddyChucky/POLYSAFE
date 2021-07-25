"""
    Polysafe - User testing.
    Description:    Simulates user interactions for polysafe with Selenium.
    File name:      pipeline.py
    Author:         Charles De Lafontaine
    Last edition:   07/25/2021
"""
from start_connection_test import *
from start_creation_test import *
from start_reset_password_test import *
from start_account_home_test import *
from test_connection import *
from test_creation import *
from test_reset_password import *
from test_account_home import *

from selenium.webdriver.chrome.options import Options


def main():
    print_header("MAIN", "Would you like to run the tests queued or by multi-threading? (<q>/<m>)")
    print_warning("MAIN", "Please note that multi-threading requires a preloaded JSON file with no errors. "
                          "If you would like to load a fresh JSON file, please run the tests queued.")
    test_running_mode = "hl"
    #test_running_mode = seek_test_running_mode()

    if test_running_mode in MULTI_THREADING_OPTIONS:
        print_header("MAIN", "Starting multi-threading testing...")
        connection_test = StartConnectionTest("CONNECTION_TEST", "Starting connection test...")
        connection_test.start()

        creation_test = StartCreationTest("CREATION_TEST", "Starting creation test...")
        creation_test.start()

        test_reset_password = StartResetPasswordTest("RESET_PASSWORD_TEST", "Starting reset password test...")
        test_reset_password.start()

        test_account_home = StartAccountHomeTest("ACCOUNT_HOME_TEST", "Starting account home test...")
        test_account_home.start()

    else:
        print_header("MAIN", "Starting queued testing...")
        print_warning("MAIN", "To start, please type the name/number of the desired test:")

        count = 0
        for test in TESTS:
            count += 1
            print_header("TEST", "Test #" + str(count) + ": " + test)

        print_warning("MAIN", "If you wish to quit, at all times you can enter <quit> or <q>.")

        while True:
            user_input = CONNECTION_TEST
            #user_input = wait_for_user_input()

            if user_input in TEST_QUIT_OPTIONS:
                exit(0)

            else:
                if user_input == CONNECTION_TEST or int(user_input) == CONNECTION_TEST_ID:
                    options = Options()
                    options.add_argument("--headless")
                    options.add_argument("--no-sandbox")
                    options.add_argument("--disable-dev-shm-usage")
                    connection_test = TestConnection(webdriver.Chrome(ChromeDriverManager().install(),
                                                                      options=options))
                    connection_test.test_connection()

                elif user_input == CREATION_TEST or int(user_input) == CREATION_TEST_ID:
                    creation_test = TestCreation(webdriver.Chrome(ChromeDriverManager().install()))
                    creation_test.test_creation()

                elif user_input == RESET_PASSWORD_TEST or int(user_input) == RESET_PASSWORD_TEST_ID:
                    test_reset_password = TestResetPassword(webdriver.Chrome(ChromeDriverManager().install()))
                    test_reset_password.test_reset_password()

                elif user_input == ACCOUNT_HOME_TEST or int(user_input) == ACCOUNT_HOME_TEST_ID:
                    test_account_home = TestAccountHome(webdriver.Chrome(ChromeDriverManager().install()))
                    test_account_home.test_account_home()

                exit(0)


if __name__ == '__main__':
    print_header("MAIN", "Running all tests...")
    main()
