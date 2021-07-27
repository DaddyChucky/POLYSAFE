"""
    Polysafe - User testing.
    Description:    StartResetPassword class definition.
    File name:      start_reset_password_test.py
    Author:         Charles De Lafontaine
    Last edition:   07/14/2021
"""
from config.constants import OPTIONS
from start.start_test_interface import *
from tests.test_reset_password import TestResetPassword

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class StartResetPasswordTest(StartTestInterface):
    def __init__(self, thread_name: str, thread_phrase: str):
        super().__init__(thread_name, thread_phrase)

    def run(self):
        super().run()
        TestResetPassword(webdriver.Chrome(ChromeDriverManager().install(), options=OPTIONS)).test_reset_password()
