"""
    Polysafe - User testing.
    Description:    TestsInterface class definition.
    File name:      tests_interface.py
    Author:         Charles De Lafontaine
    Last edition:   06/22/2021
"""

from selenium import webdriver
from jsonfile import *


class TestsInterface:
    """
        Definition:
            Class interface to conduct tests.

        Functions:
            driver -> webdriver                         :: Getter for webdriver.
            driver(new_web_driver)                      :: Setter for webdriver.

        Attributes:
            __DRIVER: webdriver                         :: The webdriver.
    """

    def __init__(self, w_driver: webdriver, jsonfile: JsonFile) -> None:
        self.__DRIVER = w_driver
        self.__JSONFILE = jsonfile
        self.__JSONDUMP = jsonfile.read()
        self.__POLYSAFE_DEVELOPER_EMAIL = None
        self.__POLYSAFE_DEVELOPER_PASSWORD = None

    @property
    def driver(self) -> webdriver:
        return self.__DRIVER

    @driver.setter
    def driver(self, new_web_driver: webdriver) -> None:
        self.__DRIVER = new_web_driver

    @property
    def polysafe_developer_email(self) -> str:
        return self.__POLYSAFE_DEVELOPER_EMAIL

    @property
    def polysafe_developer_password(self) -> str:
        return self.__POLYSAFE_DEVELOPER_PASSWORD

    @property
    def jsonfile(self) -> JsonFile:
        return self.__JSONFILE

    @property
    def jsondump(self) -> dict:
        return self.__JSONDUMP

    """
        Verify that json contains all constants for TestsInterface
        if is_root, does the exception of json_read_failure
    """

    def load_constants(self, is_root: bool = False) -> None:
        try:
            self.__POLYSAFE_DEVELOPER_EMAIL = self.jsondump[DEV_POWERTOOL_REP][DEV_CREDENTIALS_REP][EMAIL_REP]
            self.__POLYSAFE_DEVELOPER_PASSWORD = self.jsondump[DEV_POWERTOOL_REP][DEV_CREDENTIALS_REP][PASSWORD_REP]

        # If one or more constants are inaccessible
        except TypeError or KeyError:
            print_failure("INTERFACE_LOAD_CST", "One or many errors in loading constants.")

            if is_root:
                print_header("MAINPAGE_LD_CST", "Retrying to read json file...")
                with open(self.jsonfile.os.getcwd() + self.jsonfile.file_name, self.jsonfile.file_mode_read,
                          encoding=self.jsonfile.file_encoding) as json_file:
                    self.jsonfile.json_read_failure(json_file)
