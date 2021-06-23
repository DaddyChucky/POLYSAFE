"""
    Polysafe - User testing.
    Description:    Simulates user interactions for polysafe with Selenium.
    File name:      tests.py
    Author:         Charles De Lafontaine
    Last edition:   06/22/2021
"""
from test_mainpage import *

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def main():
    test_mainpage = TestMainpage(webdriver.Chrome(ChromeDriverManager().install()))
    print_header("MAINPAGE", "Testing connection...")
    test_mainpage.test_connection()
    exit()


print_header("MAIN", "Running all tests...")

if __name__ == '__main__':
    main()
