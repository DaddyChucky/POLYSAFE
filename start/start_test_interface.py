"""
    Polysafe - User testing.
    Description:    StartTestInterface class definition.
    File name:      start_test_interface.py
    Author:         Charles De Lafontaine
    Last edition:   06/29/2021
"""

from config.bg_txt_color import *

import threading


class StartTestInterface(threading.Thread):
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
