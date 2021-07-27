"""
    Polysafe - User testing.
    Description:    StartAccountHomeTest class definition.
    File name:      start_account_home_test.py
    Author:         Charles De Lafontaine
    Last edition:   07/21/2021
"""
from config.constants import OPTIONS
from start.start_test_interface import *
from tests.test_account_home import TestAccountHome

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class StartAccountHomeTest(StartTestInterface):
    def __init__(self, thread_name: str, thread_phrase: str):
        super().__init__(thread_name, thread_phrase)

    def run(self):
        super().run()
        TestAccountHome(webdriver.Chrome(ChromeDriverManager().install(), options=OPTIONS)).test_account_home()
