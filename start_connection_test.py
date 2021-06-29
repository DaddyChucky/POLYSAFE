"""
    Polysafe - User testing.
    Description:    StartConnectionTest class definition.
    File name:      start_connection_test.py
    Author:         Charles De Lafontaine
    Last edition:   06/29/2021
"""

from start_test_interface import *
from test_connection import TestConnection
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class StartConnectionTest(StartTestInterface):
    def __init__(self, thread_name: str, thread_phrase: str):
        super().__init__(thread_name, thread_phrase)

    def run(self):
        super().run()
        TestConnection(webdriver.Chrome(ChromeDriverManager().install())).test_connection()
