"""
    Polysafe - User testing.
    Description:    TestCreation class definition.
    File name:      test_creation.py
    Author:         Charles De Lafontaine
    Last edition:   06/29/2021
"""

from tests_interface import *
import sys


class TestCreation(TestsInterface):
    def __init__(self, w_driver: webdriver) -> None:
        super().__init__(w_driver, JsonFile())
        self.__POLYSAFE_CREATE_ACCOUNT_URL = None
        self.__ACTIVE = None
        self.__LIMIT_OF_RETRIES = None
        self.__VALID_REGISTRATION_NUMBER_LIST = None
        self.__INVALID_REGISTRATION_NUMBER_LIST = None
        self.__VALID_NAME_LIST = None
        self.__INVALID_NAME_LIST = None
        self.__VALID_EMAIL_LIST = None
        self.__INVALID_EMAIL_LIST = None
        self.__VALID_PASSWORD_LIST = None
        self.__INVALID_PASSWORD_LIST = None
        self.__VALID_CELLPHONE_NUMBER_LIST = None
        self.__INVALID_CELLPHONE_NUMBER_LIST = None
        self.__ACCOUNT_CREATION_CONTRACT_LNK = None

    @property
    def polysafe_create_account_url(self) -> str:
        return self.__POLYSAFE_CREATE_ACCOUNT_URL

    @property
    def active(self) -> bool:
        return bool(self.__ACTIVE)

    @property
    def limit_of_retries(self) -> int:
        return int(self.__LIMIT_OF_RETRIES)

    @property
    def valid_registration_number_list(self) -> list:
        return list(self.__VALID_REGISTRATION_NUMBER_LIST)

    @property
    def invalid_registration_number_list(self) -> list:
        return list(self.__INVALID_REGISTRATION_NUMBER_LIST)

    @property
    def valid_name_list(self) -> list:
        return list(self.__VALID_NAME_LIST)

    @property
    def invalid_name_list(self) -> list:
        return list(self.__INVALID_NAME_LIST)

    @property
    def valid_email_list(self) -> list:
        return list(self.__VALID_EMAIL_LIST)

    @property
    def invalid_email_list(self) -> list:
        return list(self.__INVALID_EMAIL_LIST)

    @property
    def valid_password_list(self) -> list:
        return list(self.__VALID_PASSWORD_LIST)

    @property
    def invalid_password_list(self) -> list:
        return list(self.__INVALID_PASSWORD_LIST)

    @property
    def valid_cellphone_number_list(self) -> list:
        return list(self.__VALID_CELLPHONE_NUMBER_LIST)

    @property
    def invalid_cellphone_number_list(self) -> list:
        return list(self.__INVALID_CELLPHONE_NUMBER_LIST)

    @property
    def account_creation_contract(self) -> str:
        return self.__ACCOUNT_CREATION_CONTRACT_LNK

    """
        Verify that json contains all constants for TestMainpage 
    """

    def load_constants(self, is_root: bool = True):
        break_loop = False

        while True:
            try:
                self.__ACTIVE = self.jsondump[TEST_CREATION_REP][ACTIVE_REP]
                self.__POLYSAFE_CREATE_ACCOUNT_URL = \
                    self.jsondump[TEST_CREATION_REP][CONSTANTS_REP][POLYSAFE_CREATE_ACCOUNT_URL_REP]
                self.__LIMIT_OF_RETRIES = self.jsondump[TEST_CREATION_REP][CONSTANTS_REP][LIMIT_OF_RETRIES_REP]
                self.__VALID_REGISTRATION_NUMBER_LIST = \
                    self.jsondump[TEST_CREATION_REP][CONSTANTS_REP][VALID_REGISTRATION_NUMBER_LIST_REP]
                self.__INVALID_REGISTRATION_NUMBER_LIST = \
                    self.jsondump[TEST_CREATION_REP][CONSTANTS_REP][INVALID_REGISTRATION_NUMBER_LIST_REP]
                self.__VALID_NAME_LIST = self.jsondump[TEST_CREATION_REP][CONSTANTS_REP][VALID_NAME_LIST_REP]
                self.__INVALID_NAME_LIST = self.jsondump[TEST_CREATION_REP][CONSTANTS_REP][INVALID_NAME_LIST_REP]
                self.__VALID_EMAIL_LIST = self.jsondump[TEST_CREATION_REP][CONSTANTS_REP][VALID_EMAIL_LIST_REP]
                self.__INVALID_EMAIL_LIST = self.jsondump[TEST_CREATION_REP][CONSTANTS_REP][INVALID_NAME_LIST_REP]
                self.__VALID_PASSWORD_LIST = self.jsondump[TEST_CREATION_REP][CONSTANTS_REP][VALID_PASSWORD_LIST_REP]
                self.__INVALID_PASSWORD_LIST = \
                    self.jsondump[TEST_CREATION_REP][CONSTANTS_REP][INVALID_PASSWORD_LIST_REP]
                self.__VALID_CELLPHONE_NUMBER_LIST = \
                    self.jsondump[TEST_CREATION_REP][CONSTANTS_REP][VALID_CELLPHONE_NUMBER_LIST_REP]
                self.__INVALID_CELLPHONE_NUMBER_LIST = \
                    self.jsondump[TEST_CREATION_REP][CONSTANTS_REP][INVALID_CELLPHONE_NUMBER_LIST_REP]
                self.__ACCOUNT_CREATION_CONTRACT_LNK = \
                    self.jsondump[TEST_CREATION_REP][CONSTANTS_REP][ACCOUNT_CREATION_CONTRACT_LNK_REP]

                break_loop = True

            except Exception:
                print_failure("MAINPAGE_LD_CST",
                              "One or many errors in loading constants.")
                print_header("MAINPAGE_LD_CST",
                             "Retrying to read json file...")
                with open(self.jsonfile.os.getcwd() + self.jsonfile.file_name, self.jsonfile.file_mode_read,
                          encoding=self.jsonfile.file_encoding) as json_file:
                    self.jsonfile.json_read_failure(json_file)

            if break_loop:
                break

    def test_creation(self):
        # Load constants before actually launching the test
        self.load_constants()

        print(self.active)

        if self.active:  # Only run if test is activated
            n_failures = 0
            with self.wait_for_page_load(timeout=10):
                while True:
                    try:
                        print_header("MAINPAGE", "Testing account creation button...")

                        self.driver.get(self.polysafe_create_account_url)
                        print_success("LOGIN_PAGE", "All tests passed!")

                    except Exception:
                        n_failures += 1  # Increments number of failures
                        exc_type, value, traceback = sys.exc_info()
                        print_failure(
                            "TEST_CONNECTION", "Test failed with exception [" + exc_type.__name__ + "]")

                    # Breaking if code has no exception or reaches the limit of retries
                    if n_failures == 0 or n_failures >= self.limit_of_retries:
                        break
