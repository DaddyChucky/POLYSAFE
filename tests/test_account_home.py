"""
    Polysafe - User testing.
    Description:    StartAccountHomeTest class definition.
    File name:      test_account_home.py
    Author:         Charles De Lafontaine
    Last edition:   07/21/2021
"""

from tests.tests_interface import *

import sys


class TestAccountHome(TestsInterface):
    def __init__(self, w_driver: webdriver) -> None:
        super().__init__(w_driver, JsonFile())
        self.__ACTIVE = None
        self.__LIMIT_OF_RETRIES = None
        self.__POLYSAFE_LOGIN_URL = None
        self.__EMAIL_LOGIN_ID = None
        self.__EMAIL_LOGIN_QRY = None
        self.__PASSWORD_LOGIN_ID = None
        self.__PASSWORD_LOGIN_QRY = None
        self.__CONNECTION_BTN = None
        self.__CONNECTION_BTN_ID = None
        self.__ACCOUNT_REGISTRAR_VERIFIED = None
        self.__FORMATION_BTN = None
        self.__FORMATION_BTN_LABEL = None
        self.__RESERVE_BTN = None
        self.__RESERVE_BTN_LABEL = None
        self.__CONTACT_BTN = None
        self.__CONTACT_BTN_LABEL = None
        self.__CALENDAR_LNK = None
        self.__CALENDAR_LNK_LABEL = None
        self.__MEMBERSHIP_DETAILS_BTN = None
        self.__MEMBERSHIP_DETAILS_BTN_LABEL = None
        self.__BILLING_DETAILS_BTN = None
        self.__BILLING_DETAILS_BTN_LABEL = None
        self.__PURCHASE_DETAILS_BTN = None
        self.__PURCHASE_DETAILS_BTN_LABEL = None
        self.__CURR_WINDOW_ID = 0
        self.__MY_CALENDAR_LNK_LABEL = None
        self.__NEW_RESERVATION_LNK_LABEL = None
        self.__PRINTING_LNK_LABEL = None
        self.__OPENINGS_LNK_LABEL = None
        self.__LIVE_PRINTING_LNK_LABEL = None
        self.__RESERVE_FORMATION_LNK_LABEL = None
        self.__GLOBAL_CALENDAR_LNK_LABEL = None

    @property
    def active(self) -> bool:
        return bool(self.__ACTIVE)

    @active.setter
    def active(self, new_active: bool) -> None:
        self.__ACTIVE = new_active

    @property
    def limit_of_retries(self) -> int:
        return int(self.__LIMIT_OF_RETRIES)

    @limit_of_retries.setter
    def limit_of_retries(self, new_limit_of_retries: str) -> None:
        self.__LIMIT_OF_RETRIES = new_limit_of_retries

    @property
    def polysafe_login_url(self) -> str:
        return self.__POLYSAFE_LOGIN_URL

    @polysafe_login_url.setter
    def polysafe_login_url(self, new_polysafe_login_url: str) -> None:
        self.__POLYSAFE_LOGIN_URL = new_polysafe_login_url

    @property
    def email_login_id(self) -> str:
        return self.__EMAIL_LOGIN_ID

    @email_login_id.setter
    def email_login_id(self, new_email_login_id: str) -> None:
        self.__EMAIL_LOGIN_ID = new_email_login_id

    @property
    def email_login_qry(self):
        return self.__EMAIL_LOGIN_QRY

    @email_login_qry.setter
    def email_login_qry(self, new_email_login_qry) -> None:
        self.__EMAIL_LOGIN_QRY = new_email_login_qry

    @property
    def password_login_id(self) -> str:
        return self.__PASSWORD_LOGIN_ID

    @password_login_id.setter
    def password_login_id(self, new_password_login_id: str) -> None:
        self.__PASSWORD_LOGIN_ID = new_password_login_id

    @property
    def password_login_qry(self):
        return self.__PASSWORD_LOGIN_QRY

    @password_login_qry.setter
    def password_login_qry(self, new_password_login_qry) -> None:
        self.__PASSWORD_LOGIN_QRY = new_password_login_qry

    @property
    def connection_btn_id(self) -> str:
        return self.__CONNECTION_BTN_ID

    @connection_btn_id.setter
    def connection_btn_id(self, new_connection_btn_id: str) -> None:
        self.__CONNECTION_BTN_ID = new_connection_btn_id

    @property
    def connection_btn(self):
        return self.__CONNECTION_BTN

    @connection_btn.setter
    def connection_btn(self, new_connection_btn) -> None:
        self.__CONNECTION_BTN = new_connection_btn

    @property
    def account_registrar_verified(self) -> str:
        return self.__ACCOUNT_REGISTRAR_VERIFIED

    @account_registrar_verified.setter
    def account_registrar_verified(self, new_account_registrar_verified: str) -> None:
        self.__ACCOUNT_REGISTRAR_VERIFIED = new_account_registrar_verified

    @property
    def window_current_id(self) -> int:
        return self.__CURR_WINDOW_ID

    @window_current_id.setter
    def window_current_id(self, new_window_current_id: int) -> None:
        self.__CURR_WINDOW_ID = new_window_current_id

    """
        Verify that json contains all constants for TestMainpage 
    """

    def load_constants(self, is_root: bool = True):
        break_loop = False

        while True:
            try:
                super().load_constants()
                self.active = self.jsondump[TEST_ACCOUNT_HOME_REP][ACTIVE_REP]
                self.limit_of_retries = self.jsondump[TEST_ACCOUNT_HOME_REP][CONSTANTS_REP][LIMIT_OF_RETRIES_REP]
                self.polysafe_login_url = self.jsondump[TEST_ACCOUNT_HOME_REP][CONSTANTS_REP][POLYSAFE_LOGIN_URL_REP]
                self.email_login_id = self.jsondump[TEST_ACCOUNT_HOME_REP][CONSTANTS_REP][EMAIL_ID_REP]
                self.password_login_id = self.jsondump[TEST_ACCOUNT_HOME_REP][CONSTANTS_REP][PASSWORD_ID_REP]
                self.connection_btn_id = self.jsondump[TEST_ACCOUNT_HOME_REP][CONSTANTS_REP][CONNECTION_BTN_ID_REP]
                self.account_registrar_verified = \
                    self.jsondump[TEST_ACCOUNT_HOME_REP][CONSTANTS_REP][ACCOUNT_REGISTRAR_VERIFIED_REP]

                break_loop = True

            except Exception:
                print_failure("ACCOUNT_HOME_PAGE",
                              "One or many errors in loading constants.")
                print_header("ACCOUNT_HOME_PAGE",
                             "Retrying to read json file...")
                with open(self.jsonfile.file_path, self.jsonfile.file_mode_read,
                          encoding=self.jsonfile.file_encoding) as json_file:
                    self.jsonfile.json_read_failure(json_file)

            if break_loop:
                break

    def close_current_window(self):
        self.driver.close()

        if self.window_current_id > 0:
            self.window_current_id -= 1
            self.driver.switch_to_window(self.driver.window_handles[self.window_current_id])

    def switch_current_window(self):
        self.window_current_id += 1
        self.driver.switch_to_window(self.driver.window_handles[self.window_current_id])

    def test_account_home(self):
        # Load constants before actually launching the tests
        self.load_constants()

        if self.active:  # Only run if tests is activated
            n_failures = 0

            with self.wait_for_page_load(timeout=10):
                while True:
                    try:
                        print_header("MAINPAGE", "Testing account home page...")
                        print_header("POLYSAFE_LOGIN", "Redirecting to login page...")
                        print_warning("POLYSAFE_LOGIN", "Slow down expected.")
                        self.driver.get(self.polysafe_login_url)

                        print_header("POLYSAFE_LOGIN", "Verifying querries before sending developer keys...")
                        self.email_login_qry = self.driver.find_element_by_id(self.email_login_id)
                        self.password_login_qry = self.driver.find_element_by_id(self.password_login_id)
                        self.connection_btn = self.driver.find_element_by_id(self.connection_btn_id)

                        print_success("POLYSAFE_LOGIN", "All querries found!")
                        print_header("POLYSAFE_LOGIN", "Connecting to your developer account...")
                        self.email_login_qry.send_keys(self.polysafe_developer_email)
                        self.password_login_qry.send_keys(self.polysafe_developer_password)
                        print_header("POLYSAFE_LOGIN", "All keys sent!")
                        print_header("POLYSAFE_LOGIN", "Clicking connection button...")
                        print_warning("POLYSAFE_LOGIN", "Slow down expected.")
                        self.connection_btn.click()
                        xpath_account_registrar_verified: str = "//*[text()='" + \
                                                                self.account_registrar_verified + "']"

                        if len(self.driver.find_elements_by_xpath(xpath_account_registrar_verified)) != 0:
                            print_success("POLYSAFE_LOGIN", "Successfully logged in!")

                        else:
                            print_failure("POLYSAFE_LOGIN", "Cannot login in developer's account.")

                        print_header("POLYSAFE_TEST_ACCOUNT_HOME", "Verifying page linking...")

                        dead_urls = ["users/logout.php"]  # Escape logout

                        # Adding global testing url to all dead urls
                        for i in range(len(dead_urls)):
                            dead_urls[i] = TESTING_URL_REP + dead_urls[i]

                        dead_urls.append(self.polysafe_login_url)

                        for i in range(len(self.driver.find_elements_by_xpath("//a[@href]"))):
                            href = self.driver.find_elements_by_xpath("//a[@href]")[i].get_attribute("href")

                            try:
                                print_header("POLYSAFE_TEST_ACCOUNT_HOME", "Testing linking #" +
                                             str(i) + " (" + href + ")")
                                print_warning("POLYSAFE_TEST_ACCOUNT_HOME", "Loading page, delay expected...")

                                if href not in dead_urls:
                                    self.driver.get(href)

                                if len(self.driver.find_elements_by_xpath(ERROR_404_XPATH)) == 0:
                                    print_success("POLYSAFE_TEST_ACCOUNT_HOME", "Successfully tested linking #" +
                                                  str(i) + " (" + href + ")")
                                else:
                                    print_failure("POLYSAFE_TEST_ACCOUNT_HOME", "Link #" +
                                                  str(i) + " (" + href + ") is invalid!")

                            except Exception:
                                exc_type, value, traceback = sys.exc_info()
                                print_failure("POLYSAFE_TEST_ACCOUNT_HOME", "Error while testing linking #" +
                                              str(i) + " (" + href + ")" + " Exception: " + exc_type.__name__)

                            print_warning("POLYSAFE_TEST_ACCOUNT_HOME",
                                          "Redirecting to account home page, delay expected...")
                            self.driver.get(self.polysafe_login_url)

                        print_success("LOGIN_PAGE", "All tests passed!")

                    except Exception:
                        n_failures += 1  # Increments number of failures
                        exc_type, value, traceback = sys.exc_info()
                        print_failure(
                            "TEST_ACCOUNT_HOME", "Test failed with exception [" + exc_type.__name__ + "]")

                    # Breaking if code has no exception or reaches the limit of retries
                    if n_failures == 0 or n_failures >= self.limit_of_retries:
                        break
