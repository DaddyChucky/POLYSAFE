"""
    Polysafe - User testing.
    Description:    Simulates user interactions for polysafe with Selenium.
    File name:      main.py
    Author:         Charles De Lafontaine
    Last edition:   06/22/2021
"""
from start_connection_test import *
from start_creation_test import *
from test_connection import *
from test_creation import *


def main():
    # start_connection_test = StartConnectionTest("CONNECTION_TEST", "Starting connection test...")
    # start_connection_test.start()

    start_creation_test = StartCreationTest("CREATION_TEST", "Starting creation test...")
    start_creation_test.start()

    while True:
        continue


if __name__ == '__main__':
    print_header("MAIN", "Running all tests...")
    main()
