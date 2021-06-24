"""
    Polysafe - User testing.
    Description:    TestMainpage class definition.
    File name:      test_mainpage.py
    Author:         Charles De Lafontaine
    Last edition:   06/22/2021
"""

from tests_interface import *
from jsonfile import *

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import staleness_of
from contextlib import contextmanager
import sys


class TestMainpage(TestsInterface):
    def __init__(self, w_driver: webdriver) -> None:
        super().__init__(w_driver, JsonFile())
        self.__ACTIVE = None
        self.__CHECK_URLS = None
        self.__CHECK_LOGIN_CREDENTIALS = None
        self.__SEND_FAKE_LOGIN_CREDENTIALS = None
        self.__CHECK_ERROR_GENERATION = None
        self.__POLYSAFE_MAINPAGE_URL = None

    @property
    def polysafe_mainpage_url(self) -> str:
        return self.__POLYSAFE_MAINPAGE_URL

    @property
    def active(self) -> bool:
        return bool(self.__ACTIVE)

    @property
    def check_urls(self) -> bool:
        return bool(self.__CHECK_URLS)

    @property
    def check_login_credentials(self) -> bool:
        return bool(self.__CHECK_LOGIN_CREDENTIALS)

    @property
    def send_fake_login_credentials(self) -> bool:
        return bool(self.__SEND_FAKE_LOGIN_CREDENTIALS)

    @property
    def check_error_generation(self) -> bool:
        return bool(self.__CHECK_ERROR_GENERATION)

    @property
    def connection_text(self) -> str:
        return self.__CONNECTION_TEXT

    @property
    def limit_of_retries(self) -> int:
        return int(self.__LIMIT_OF_RETRIES)

    @property
    def expected_connection_url(self) -> str:
        return self.__EXPECTED_CONNECTION_URL

    @property
    def email_id(self) -> str:
        return self.__EMAIL_ID

    @property
    def password_id(self) -> str:
        return self.__PASSWORD_ID

    @property
    def connection_btn_id(self) -> str:
        return self.__CONNECTION_BTN_ID

    @property
    def invalid_email(self) -> str:
        return self.__INVALID_EMAIL

    @property
    def invalid_password(self) -> str:
        return self.__INVALID_PASSWORD

    @property
    def close_button(self) -> str:
        return self.__CLOSE_BUTTON

    @property
    def forgot_button_link(self) -> str:
        return self.__FORGOT_BUTTON_LINK

    @property
    def create_account_link(self) -> str:
        return self.__CREATE_ACCOUNT_LINK

    @property
    def about_link(self) -> str:
        return self.__ABOUT_LINK

    @property
    def support_link(self) -> str:
        return self.__SUPPORT_LINK

    """
        Verify that json contains all constants for TestMainpage 
    """

    def load_constants(self, is_root: bool = True):
        break_loop = False

        while True:
            try:
                super().load_constants()
                self.__ACTIVE = self.jsondump[TEST_MAINPAGE_REP][ACTIVE_REP]
                self.__CHECK_URLS = self.jsondump[TEST_MAINPAGE_REP][CHECK_URLS_REP]
                self.__CHECK_LOGIN_CREDENTIALS = self.jsondump[TEST_MAINPAGE_REP][CHECK_LOGIN_CREDENTIALS_REP]
                self.__CHECK_LOGIN_CREDENTIALS = self.jsondump[TEST_MAINPAGE_REP][CHECK_LOGIN_CREDENTIALS_REP]
                self.__SEND_FAKE_LOGIN_CREDENTIALS = self.jsondump[TEST_MAINPAGE_REP][SEND_FAKE_LOGIN_CREDENTIALS_REP]
                self.__CHECK_ERROR_GENERATION = self.jsondump[TEST_MAINPAGE_REP][CHECK_ERROR_GENERATION_REP]
                self.__POLYSAFE_MAINPAGE_URL = self.jsondump[TEST_MAINPAGE_REP][CONSTANTS_REP][POLYSAFE_MAINPAGE_URL_REP]
                self.__CONNECTION_TEXT = self.jsondump[TEST_MAINPAGE_REP][CONSTANTS_REP][CONNECTION_TEXT_REP]
                self.__LIMIT_OF_RETRIES = self.jsondump[TEST_MAINPAGE_REP][CONSTANTS_REP][LIMIT_OF_RETRIES_REP]
                self.__EXPECTED_CONNECTION_URL = self.jsondump[TEST_MAINPAGE_REP][CONSTANTS_REP][EXPECTED_CONNECTION_URL_REP]
                self.__EMAIL_ID = self.jsondump[TEST_MAINPAGE_REP][CONSTANTS_REP][EMAIL_ID_REP]
                self.__PASSWORD_ID = self.jsondump[TEST_MAINPAGE_REP][CONSTANTS_REP][PASSWORD_ID_REP]
                self.__CONNECTION_BTN_ID = self.jsondump[TEST_MAINPAGE_REP][CONSTANTS_REP][CONNECTION_BTN_ID_REP]
                self.__INVALID_EMAIL = self.jsondump[TEST_MAINPAGE_REP][CONSTANTS_REP][INVALID_EMAIL_REP]
                self.__INVALID_PASSWORD = self.jsondump[TEST_MAINPAGE_REP][CONSTANTS_REP][INVALID_PASSWORD_REP]
                self.__CLOSE_BUTTON = self.jsondump[TEST_MAINPAGE_REP][CONSTANTS_REP][CLOSE_BUTTON_REP]
                self.__FORGOT_BUTTON_LINK = self.jsondump[TEST_MAINPAGE_REP][CONSTANTS_REP][FORGOT_BUTTON_LINK_REP]
                self.__CREATE_ACCOUNT_LINK = self.jsondump[TEST_MAINPAGE_REP][CONSTANTS_REP][CREATE_ACCOUNT_LINK_REP]
                self.__ABOUT_LINK = self.jsondump[TEST_MAINPAGE_REP][CONSTANTS_REP][ABOUT_LINK_REP]
                self.__SUPPORT_LINK = self.jsondump[TEST_MAINPAGE_REP][CONSTANTS_REP][SUPPORT_LINK_REP]

                break_loop = True

            except TypeError or KeyError:
                print_failure("MAINPAGE_LD_CST",
                              "One or many errors in loading constants.")
                print_header("MAINPAGE_LD_CST",
                             "Retrying to read json file...")
                with open(self.jsonfile.os.getcwd() + self.jsonfile.file_name, self.jsonfile.file_mode_read,
                          encoding=self.jsonfile.file_encoding) as json_file:
                    self.jsonfile.json_read_failure(json_file)

            if break_loop:
                break

    @contextmanager
    def wait_for_page_load(self,
                           timeout=30):  # Source: https://www.cloudbees.com/blog/get-selenium-to-wait-for-page-load/
        old_page = self.driver.find_element_by_tag_name('html')
        yield
        WebDriverWait(self.driver, timeout).until(
            staleness_of(old_page)
        )

    def test_connection(self):
        # Load constants before actually launching the test
        self.load_constants()

        if self.active:  # Only run if test is activated
            n_failures = 0

            with self.wait_for_page_load(timeout=10):
                while True:
                    try:
                        print_header(
                            "MAINPAGE", "Testing connection button...")
                        print_warning("MAINPAGE", "Slow down expected.")
                        self.driver.get(self.polysafe_mainpage_url)
                        connection_button = self.driver.find_element_by_link_text(
                            self.connection_text)

                        print_header(
                            "MAINPAGE", "Found connection button! Trying to click it...")
                        print_warning("MAINPAGE", "Slow down expected.")
                        connection_button.click()

                        print_header(
                            "LOGIN_PAGE", "Connection button clicked, comparing URLs...")

                        print(type(self.expected_connection_url),
                              self.expected_connection_url)
                        if self.driver.current_url == self.expected_connection_url:
                            print_success("LOGIN_PAGE", "URLs are matching!")

                        else:
                            print_failure(
                                "LOGIN_PAGE", "URLs are not matching (", self.driver.current_url, " vs JSON{", self.expected_connection_url, "})")
                            return

                        if self.check_login_credentials:
                            print_header(
                                "LOGIN_PAGE", "Testing email & password querries...")
                            print_header(
                                "LOGIN_PAGE", "Trying to find email & password input boxes...")
                            email_input_box = self.driver.find_element_by_id(
                                self.email_id)
                            password_input_box = self.driver.find_element_by_id(
                                self.password_id)
                            print_success(
                                "LOGIN_PAGE", "Found email & password input boxes!")
                            print_header(
                                "LOGIN_PAGE", "Trying to find connection button...")
                            connection_button = self.driver.find_element_by_id(
                                self.connection_btn_id)
                            print_success(
                                "LOGIN_PAGE", "Found connection button!")

                            print_header(
                                "LOGIN_PAGE", "Sending invalid keys...")
                            email_input_box.clear()
                            password_input_box.clear()
                            email_input_box.send_keys(self.invalid_email)
                            password_input_box.send_keys(self.invalid_password)
                            print_success("LOGIN_PAGE", "Keys sent!")
                            print_header(
                                "LOGIN_PAGE", "Trying to click connection button...")
                            print_warning("LOGIN_PAGE", "Slow down expected.")
                            connection_button.click()

                            if self.check_urls:
                                print_header(
                                    "LOGIN_PAGE", "Button clicked, comparing URLs...")
                                if self.driver.current_url == self.expected_connection_url:
                                    print_success(
                                        "LOGIN_PAGE", "URLs are matching!")

                                else:
                                    print_failure(
                                        "LOGIN_PAGE", "URLs are not matching.")
                                    return

                            if self.check_error_generation:
                                print_header(
                                    "LOGIN_PAGE", "Checking if the page generated error (failed login)...")

                                if self.driver.find_element_by_class_name(self.close_button) is not None:
                                    print_success(
                                        "LOGIN_PAGE", "Error label found!")

                                print_header(
                                    "LOGIN_PAGE", "Verifying button linkings...")

                                if self.driver.find_element_by_partial_link_text(self.forgot_button_link) is not None \
                                        and self.driver.find_element_by_partial_link_text(self.create_account_link) is \
                                        not None and self.driver.find_element_by_partial_link_text(self.about_link) is \
                                        not None and self.driver.find_element_by_partial_link_text(self.support_link) \
                                        is not None:
                                    print_success(
                                        "LOGIN_PAGE", "Button linking tests passed!")

                        print_success("LOGIN_PAGE", "All tests passed!")

                    except Exception:
                        n_failures += 1  # Increments number of failures
                        exc_type, value, traceback = sys.exc_info()
                        print_failure(
                            "TEST_CONNECTION", "Test failed with exception [" + exc_type.__name__ + "]")

                    # Breaking if code has no exception or reaches the limit of retries
                    if n_failures == 0 or n_failures >= self.limit_of_retries:
                        break
