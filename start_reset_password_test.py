"""
    Polysafe - User testing.
    Description:    StartResetPassword class definition.
    File name:      start_reset_password_test.py
    Author:         Charles De Lafontaine
    Last edition:   07/14/2021
"""

import threading
from bg_txt_color import *


class StartResetPasswordTest(threading.Thread):
    def __init__(self, thread_name: str, thread_phrase: str):
        threading.Thread.__init__(self)
        self.__THREAD_NAME = thread_name
        self.__THREAD_PHRASE = thread_phrase

    @property
    def thread_name(self):
        return self.__THREAD_NAME

    @property
    def thread_phrase(self):
        return self.__THREAD_PHRASE

    def run(self):
        print_header(self.thread_name, self.thread_phrase)
