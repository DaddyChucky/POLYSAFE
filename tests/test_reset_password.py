"""
    Polysafe - User testing.
    Description:    TestResetPassword class definition.
    File name:      test_reset_password.py
    Author:         Charles De Lafontaine
    Last edition:   07/14/2021
"""

from tests.tests_interface import *

import sys


class TestResetPassword(TestsInterface):
    def __init__(self, w_driver: webdriver) -> None:
        super().__init__(w_driver, JsonFile())
        self.__POLYSAFE_FORGOT_PASSWORD_URL = None
        self.__ACTIVE = None
        self.__LIMIT_OF_RETRIES = None
        self.__EMAIL_QRY = None
        self.__RESET_BTN = None
        self.__EMAIL_QRY_CLASS_NAME = None
        self.__RESET_BTN_CLASS_NAME = None
        self.__VALID_EMAIL_LIST = None
        self.__INVALID_EMAIL_LIST = None

    @property
    def polysafe_forgot_password_url(self) -> str:
        return self.__POLYSAFE_FORGOT_PASSWORD_URL

    @polysafe_forgot_password_url.setter
    def polysafe_forgot_password_url(self, new_polysafe_forgot_password_url: str) -> None:
        self.__POLYSAFE_FORGOT_PASSWORD_URL = new_polysafe_forgot_password_url

    @property
    def active(self) -> bool:
        return self.__ACTIVE

    @active.setter
    def active(self, new_active: bool) -> None:
        self.__ACTIVE = new_active

    @property
    def limit_of_retries(self) -> int:
        return self.__LIMIT_OF_RETRIES

    @limit_of_retries.setter
    def limit_of_retries(self, new_limit_of_retries: int) -> None:
        self.__LIMIT_OF_RETRIES = new_limit_of_retries

    @property
    def email_qry(self):
        return self.__EMAIL_QRY

    @email_qry.setter
    def email_qry(self, new_email_qry) -> None:
        self.__EMAIL_QRY = new_email_qry

    @property
    def reset_btn(self):
        return self.__RESET_BTN

    @reset_btn.setter
    def reset_btn(self, new_reset_btn) -> None:
        self.__RESET_BTN = new_reset_btn

    @property
    def email_qry_class_name(self) -> str:
        return self.__EMAIL_QRY_CLASS_NAME

    @email_qry_class_name.setter
    def email_qry_class_name(self, new_email_qry_class_name: str) -> None:
        self.__EMAIL_QRY_CLASS_NAME = new_email_qry_class_name

    @property
    def reset_btn_class_name(self) -> str:
        return self.__RESET_BTN_CLASS_NAME

    @reset_btn_class_name.setter
    def reset_btn_class_name(self, new_reset_btn_class_name: str) -> None:
        self.__RESET_BTN_CLASS_NAME = new_reset_btn_class_name

    @property
    def valid_email_list(self) -> list:
        return self.__VALID_EMAIL_LIST

    @valid_email_list.setter
    def valid_email_list(self, new_valid_email_list: list) -> None:
        self.__VALID_EMAIL_LIST = new_valid_email_list

    @property
    def invalid_email_list(self) -> list:
        return self.__INVALID_EMAIL_LIST

    @invalid_email_list.setter
    def invalid_email_list(self, new_invalid_email_list: list) -> None:
        self.__INVALID_EMAIL_LIST = new_invalid_email_list

    """
        Verify that json contains all constants for TestMainpage 
    """

    def load_constants(self, is_root: bool = True):
        break_loop = False

        while True:
            try:
                self.active = self.jsondump[TEST_RESET_PASSWORD_REP][ACTIVE_REP]
                self.polysafe_forgot_password_url = \
                    self.jsondump[TEST_RESET_PASSWORD_REP][CONSTANTS_REP][POLYSAFE_FORGOT_PASSWORD_URL_REP]
                self.limit_of_retries = self.jsondump[TEST_RESET_PASSWORD_REP][CONSTANTS_REP][LIMIT_OF_RETRIES_REP]
                self.email_qry_class_name = \
                    self.jsondump[TEST_RESET_PASSWORD_REP][CONSTANTS_REP][EMAIL_QRY_CLASS_NAME_REP]
                self.reset_btn_class_name = \
                    self.jsondump[TEST_RESET_PASSWORD_REP][CONSTANTS_REP][RESET_BTN_CLASS_NAME_REP]
                self.valid_email_list = self.jsondump[TEST_RESET_PASSWORD_REP][CONSTANTS_REP][VALID_EMAIL_LIST_REP]
                self.invalid_email_list = self.jsondump[TEST_RESET_PASSWORD_REP][CONSTANTS_REP][INVALID_EMAIL_LIST_REP]
                break_loop = True

            except Exception:
                print_failure("MAINPAGE_LD_CST",
                              "One or many errors in loading constants.")
                print_header("MAINPAGE_LD_CST",
                             "Retrying to read json file...")
                with open(self.jsonfile.file_path, self.jsonfile.file_mode_read,
                          encoding=self.jsonfile.file_encoding) as json_file:
                    self.jsonfile.json_read_failure(json_file)

            if break_loop:
                break

    def seek_error_box(self) -> bool:
        error_class_label = "alert alert-danger"
        if self.driver.find_element_by_class_name(error_class_label) is None:  # No error box while loading page
            return False
        return True

    def test_reset_password(self):
        # Load constants before actually launching the tests
        self.load_constants()

        if self.active:  # Only run if tests is activated
            n_failures = 0
            with self.wait_for_page_load(timeout=10):
                while True:
                    try:
                        print_header("RESET_PASSWORD", "Accessing forgot password url...")
                        print_warning("RESET_PASSWORD", "Slow down expected..")
                        self.driver.get(self.polysafe_forgot_password_url)
                        print_header("RESET_PASSWORD", "Testing reset password functionality...")
                        print_header("RESET_PASSWORD", "Acquiring email querry & reset button...")
                        self.email_qry = self.driver.find_element_by_class_name(self.email_qry_class_name)
                        self.reset_btn = self.driver.find_element_by_class_name(self.reset_btn_class_name)

                        count = 0
                        for invalid_email in self.invalid_email_list:
                            print_header("RESET_PASSWORD", "Sending invalid email (" + str(count)
                                         + ")...")
                            self.email_qry.send_keys(invalid_email)
                            self.reset_btn.click()
                            if self.seek_error_box():
                                print_success("RESET_PASSWORD", "Invalid email (" + str(count) +
                                              ") passed!")
                            else:
                                print_failure("ACCOUNT_CREATION", "Invalid email (" + str(count) +
                                              ") failed!")
                                self.driver.get(self.polysafe_forgot_password_url)
                            count += 1

                        count = 0
                        for valid_email in self.valid_email_list:
                            print_header("RESET_PASSWORD", "Sending valid email (" + str(count)
                                         + ")...")
                            self.email_qry.send_keys(valid_email)
                            self.reset_btn.click()
                            if self.seek_error_box():
                                print_failure("ACCOUNT_CREATION", "Valid email (" + str(count) +
                                              ") failed!")
                            else:
                                print_success("RESET_PASSWORD", "Valid email (" + str(count) +
                                              ") passed!")
                                self.driver.get(self.polysafe_forgot_password_url)
                            count += 1

                        print_success("RESET_PASSWORD", "All tests passed!")

                    except Exception:
                        n_failures += 1  # Increments number of failures
                        exc_type, value, traceback = sys.exc_info()
                        print_failure(
                            "TEST_RESET_PASSWORD", "Test failed with exception [" + exc_type.__name__ + "]")

                    # Breaking if code has no exception or reaches the limit of retries
                    if n_failures == 0 or n_failures >= self.limit_of_retries:
                        break
