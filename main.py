"""
    Polysafe - User testing.
    Description:    Simulates user interactions for polysafe with Selenium.
    File name:      main.py
    Author:         Charles De Lafontaine
    Last edition:   06/29/2021
"""
from start_connection_test import *
from start_creation_test import *
from test_connection import *
from test_creation import *


MULTI_THREADING_OPTIONS = ['m', 'M']
QUEUED_OPTIONS = ['q', 'Q']


def seek_test_running_mode() -> str:
    choice = input()
    while choice not in MULTI_THREADING_OPTIONS and choice not in QUEUED_OPTIONS:
        print_failure("MAIN", "Invalid answer, please try again: ")
        choice = input()
        if choice in MULTI_THREADING_OPTIONS or choice in QUEUED_OPTIONS:
            return choice


def main():
    print_header("MAIN", "Would you like to run the tests queued or by multi-threading? (q/m)")
    test_running_mode = seek_test_running_mode()

    if test_running_mode in MULTI_THREADING_OPTIONS:
        print_header("MAIN", "Starting multi-threading testing...")
        connection_test = StartConnectionTest("CONNECTION_TEST", "Starting connection test...")
        connection_test.start()
        creation_test = StartCreationTest("CREATION_TEST", "Starting creation test...")
        creation_test.start()
    else:
        print_header("MAIN", "Starting queued testing...")
        connection_test = TestConnection(webdriver.Chrome(ChromeDriverManager().install()))
        connection_test.test_connection()
        creation_test = TestCreation(webdriver.Chrome(ChromeDriverManager().install()))
        creation_test.test_creation()

    while True:
        continue


if __name__ == '__main__':
    print_header("MAIN", "Running all tests...")
    main()
