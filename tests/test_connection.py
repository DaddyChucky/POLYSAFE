"""
    Polysafe - User testing.
    Description:    TestConnection class definition.
    File name:      test_connection.py
    Author:         Charles De Lafontaine
    Last edition:   06/29/2021
"""

from tests.tests_interface import *

import sys


class TestConnection(TestsInterface):
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

    @polysafe_mainpage_url.setter
    def polysafe_mainpage_url(self, new_polysafe_mainpage_url: str) -> None:
        self.__POLYSAFE_MAINPAGE_URL = new_polysafe_mainpage_url

    @property
    def active(self) -> bool:
        return bool(self.__ACTIVE)

    @active.setter
    def active(self, new_active: bool) -> None:
        self.__ACTIVE = new_active

    @property
    def check_urls(self) -> bool:
        return bool(self.__CHECK_URLS)

    @check_urls.setter
    def check_urls(self, new_check_urls: bool) -> None:
        self.__CHECK_URLS = new_check_urls

    @property
    def check_login_credentials(self) -> bool:
        return bool(self.__CHECK_LOGIN_CREDENTIALS)

    @check_login_credentials.setter
    def check_login_credentials(self, new_check_login_credentials: bool) -> None:
        self.__CHECK_LOGIN_CREDENTIALS = new_check_login_credentials

    @property
    def send_fake_login_credentials(self) -> bool:
        return bool(self.__SEND_FAKE_LOGIN_CREDENTIALS)

    @send_fake_login_credentials.setter
    def send_fake_login_credentials(self, new_send_fake_login_credentials: bool) -> None:
        self.__SEND_FAKE_LOGIN_CREDENTIALS = new_send_fake_login_credentials

    @property
    def check_error_generation(self) -> bool:
        return bool(self.__CHECK_ERROR_GENERATION)

    @check_error_generation.setter
    def check_error_generation(self, new_check_error_generation: bool) -> None:
        self.__CHECK_ERROR_GENERATION = new_check_error_generation

    @property
    def connection_text(self) -> str:
        return self.__CONNECTION_TEXT

    @connection_text.setter
    def connection_text(self, new_connection_text: str) -> None:
        self.__CONNECTION_TEXT = new_connection_text

    @property
    def limit_of_retries(self) -> int:
        return int(self.__LIMIT_OF_RETRIES)

    @limit_of_retries.setter
    def limit_of_retries(self, new_limit_of_retries: str) -> None:
        self.__LIMIT_OF_RETRIES = new_limit_of_retries

    @property
    def expected_connection_url(self) -> str:
        return self.__EXPECTED_CONNECTION_URL

    @expected_connection_url.setter
    def expected_connection_url(self, new_expected_connection_url: str) -> None:
        self.__EXPECTED_CONNECTION_URL = new_expected_connection_url

    @property
    def email_id(self) -> str:
        return self.__EMAIL_ID

    @email_id.setter
    def email_id(self, new_email_id: str) -> None:
        self.__EMAIL_ID = new_email_id

    @property
    def password_id(self) -> str:
        return self.__PASSWORD_ID

    @password_id.setter
    def password_id(self, new_password_id: str) -> None:
        self.__PASSWORD_ID = new_password_id

    @property
    def connection_btn_id(self) -> str:
        return self.__CONNECTION_BTN_ID

    @connection_btn_id.setter
    def connection_btn_id(self, new_connection_btn_id: str) -> None:
        self.__CONNECTION_BTN_ID = new_connection_btn_id

    @property
    def invalid_email(self) -> str:
        return self.__INVALID_EMAIL

    @invalid_email.setter
    def invalid_email(self, new_invalid_email: str) -> None:
        self.__INVALID_EMAIL = new_invalid_email

    @property
    def invalid_password(self) -> str:
        return self.__INVALID_PASSWORD

    @invalid_password.setter
    def invalid_password(self, new_invalid_password: str) -> None:
        self.__INVALID_PASSWORD = new_invalid_password

    @property
    def close_button(self) -> str:
        return self.__CLOSE_BUTTON

    @close_button.setter
    def close_button(self, new_close_button: str) -> None:
        self.__CLOSE_BUTTON = new_close_button

    @property
    def forgot_button_link(self) -> str:
        return self.__FORGOT_BUTTON_LINK

    @forgot_button_link.setter
    def forgot_button_link(self, new_forgot_button_link: str) -> None:
        self.__FORGOT_BUTTON_LINK = new_forgot_button_link

    @property
    def create_account_link(self) -> str:
        return self.__CREATE_ACCOUNT_LINK

    @create_account_link.setter
    def create_account_link(self, new_create_account_link: str) -> None:
        self.__CREATE_ACCOUNT_LINK = new_create_account_link

    @property
    def about_link(self) -> str:
        return self.__ABOUT_LINK

    @about_link.setter
    def about_link(self, new_about_link: str) -> None:
        self.__ABOUT_LINK = new_about_link

    @property
    def support_link(self) -> str:
        return self.__SUPPORT_LINK

    @support_link.setter
    def support_link(self, new_support_link: str) -> None:
        self.__SUPPORT_LINK = new_support_link

    """
        Verify that json contains all constants for TestMainpage 
    """

    def load_constants(self, is_root: bool = True):
        break_loop = False

        while True:
            try:
                self.active = self.jsondump[TEST_MAINPAGE_REP][ACTIVE_REP]
                self.check_urls = self.jsondump[TEST_MAINPAGE_REP][CHECK_URLS_REP]
                self.check_login_credentials = self.jsondump[TEST_MAINPAGE_REP][CHECK_LOGIN_CREDENTIALS_REP]
                self.send_fake_login_credentials = self.jsondump[TEST_MAINPAGE_REP][SEND_FAKE_LOGIN_CREDENTIALS_REP]
                self.check_error_generation = self.jsondump[TEST_MAINPAGE_REP][CHECK_ERROR_GENERATION_REP]
                self.polysafe_mainpage_url = \
                    self.jsondump[TEST_MAINPAGE_REP][CONSTANTS_REP][POLYSAFE_MAINPAGE_URL_REP]
                self.connection_text = self.jsondump[TEST_MAINPAGE_REP][CONSTANTS_REP][CONNECTION_TEXT_REP]
                self.limit_of_retries = self.jsondump[TEST_MAINPAGE_REP][CONSTANTS_REP][LIMIT_OF_RETRIES_REP]
                self.expected_connection_url = \
                    self.jsondump[TEST_MAINPAGE_REP][CONSTANTS_REP][EXPECTED_CONNECTION_URL_REP]
                self.email_id = self.jsondump[TEST_MAINPAGE_REP][CONSTANTS_REP][EMAIL_ID_REP]
                self.password_id = self.jsondump[TEST_MAINPAGE_REP][CONSTANTS_REP][PASSWORD_ID_REP]
                self.connection_btn_id = self.jsondump[TEST_MAINPAGE_REP][CONSTANTS_REP][CONNECTION_BTN_ID_REP]
                self.invalid_email = self.jsondump[TEST_MAINPAGE_REP][CONSTANTS_REP][INVALID_EMAIL_REP]
                self.invalid_password = self.jsondump[TEST_MAINPAGE_REP][CONSTANTS_REP][INVALID_PASSWORD_REP]
                self.close_button = self.jsondump[TEST_MAINPAGE_REP][CONSTANTS_REP][CLOSE_BUTTON_REP]
                self.forgot_button_link = self.jsondump[TEST_MAINPAGE_REP][CONSTANTS_REP][FORGOT_BUTTON_LINK_REP]
                self.create_account_link = self.jsondump[TEST_MAINPAGE_REP][CONSTANTS_REP][CREATE_ACCOUNT_LINK_REP]
                self.about_link = self.jsondump[TEST_MAINPAGE_REP][CONSTANTS_REP][ABOUT_LINK_REP]
                self.support_link = self.jsondump[TEST_MAINPAGE_REP][CONSTANTS_REP][SUPPORT_LINK_REP]

                break_loop = True

            except Exception:
                print_failure("MAINPAGE_LD_CST",
                              "One or many errors in loading constants.")
                print_header("MAINPAGE_LD_CST",
                             "Retrying to read json file...")
                with open(self.jsonfile.file_path,
                          self.jsonfile.file_mode_read,
                          encoding=self.jsonfile.file_encoding) as json_file:
                    self.jsonfile.json_read_failure(json_file)

            if break_loop:
                break

    def test_connection(self):
        # Load constants before actually launching the tests
        self.load_constants()

        if self.active:  # Only run if tests is activated
            n_failures = 0

            with self.wait_for_page_load(timeout=10):
                while True:
                    try:
                        print_header("MAINPAGE", "Testing account connection button...")
                        print_warning("MAINPAGE", "Slow down expected.")
                        self.driver.get(self.polysafe_mainpage_url)
                        connection_button = self.driver.find_element_by_link_text(
                            self.connection_text)

                        print_header("MAINPAGE", "Found connection button! Trying to click it...")
                        print_warning("MAINPAGE", "Slow down expected.")
                        connection_button.click()

                        print_header("LOGIN_PAGE", "Connection button clicked, comparing URLs...")
                        if self.driver.current_url == self.expected_connection_url:
                            print_success("LOGIN_PAGE", "URLs are matching!")

                        else:
                            print_failure(
                                "LOGIN_PAGE", "URLs are not matching (" + self.driver.current_url +
                                              " vs JSON{" + self.expected_connection_url + "})")
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
