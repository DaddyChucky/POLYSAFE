"""
    Polysafe - User testing.
    Description:    Simulates user interactions for polysafe with Selenium.
    File name:      tests.py
    Author:         Charles De Lafontaine
    Last edition:   06/22/2021
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import staleness_of
from webdriver_manager.chrome import ChromeDriverManager
from contextlib import contextmanager
import sys


from bg_txt_color import *
from jsonfile import *


class TestsInterface:
    """
        Definition:
            Main class to conduct tests.

        Functions:
            driver() -> webdriver                       :: Getter for webdriver.
            driver(new_web_driver)                      :: Setter for webdriver.

        Attributes:
            __DRIVER: webdriver                         :: The webdriver.
    """

    def __init__(self, w_driver: webdriver, jsonfile: JSONFile) -> None:
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
    def jsonfile(self) -> JSONFile:
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
                self.jsonfile.json_read_failure()


class TestMainpage(TestsInterface):
    def __init__(self, w_driver: webdriver) -> None:
        super().__init__(w_driver, JSONFile())
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
    def load_constants(self):
        break_loop = False

        while True:
            try:
                super().load_constants()
                self.__POLYSAFE_MAINPAGE_URL = self.jsondump[TEST_MAINPAGE_REP][CONSTANTS_REP][POLYSAFE_MAINPAGE_URL_REP]
                self.__ACTIVE = self.__POLYSAFE_MAINPAGE_URL[ACTIVE_REP]
                self.__CHECK_URLS = self.__POLYSAFE_MAINPAGE_URL[CHECK_URLS_REP]
                self.__CHECK_LOGIN_CREDENTIALS = self.__POLYSAFE_MAINPAGE_URL[CHECK_LOGIN_CREDENTIALS_REP]
                self.__CHECK_LOGIN_CREDENTIALS = self.__POLYSAFE_MAINPAGE_URL[CHECK_LOGIN_CREDENTIALS_REP]
                self.__SEND_FAKE_LOGIN_CREDENTIALS = self.__POLYSAFE_MAINPAGE_URL[SEND_FAKE_LOGIN_CREDENTIALS_REP]
                self.__CHECK_ERROR_GENERATION = self.__POLYSAFE_MAINPAGE_URL[CHECK_ERROR_GENERATION_REP]
                self.__CONNECTION_TEXT = self.jsondump[TEST_MAINPAGE_REP][CONSTANTS_REP][CONNECTION_TEXT_REP]
                self.__LIMIT_OF_RETRIES = self.jsondump[TEST_MAINPAGE_REP][CONSTANTS_REP][LIMIT_OF_RETRIES_REP]
                self.__EXPECTED_CONNECTION_URL = self.jsondump[TEST_MAINPAGE_REP][CONSTANTS_REP]
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
                print_failure("MAINPAGE_LD_CST", "One or many errors in loading constants.")
                print_header("MAINPAGE_LD_CST", "Retrying to read json file...")
                with open(self.jsonfile.OS.getcwd() + self.jsonfile.FILE_NAME, self.jsonfile.FILE_MODE_READ,
                          encoding=self.jsonfile.FILE_ENCODING) as json_file:
                    self.jsonfile.json_read_failure(json_file)

            if break_loop:
                break

    @contextmanager
    def wait_for_page_load(self,
                           timeout=30):  # Source: https://www.cloudbees.com/blog/get-selenium-to-wait-for-page-load/
        old_page = self.DRIVER.find_element_by_tag_name('html')
        yield
        WebDriverWait(self.DRIVER, timeout).until(
            staleness_of(old_page)
        )

    """
        Checks if a parent OR child (if specified) is present in JSON dump string
    """

    def check_dump_header(self, parent_name: str, child_name: str = ""):
        if child_name != "":
            only_check_parent = True
        else:
            only_check_parent = False

        hel = self.jsondump()
        # print(self.jsonfile.read()['test_mainpage']['active'])
        # for header in self.jsondump:
        #     print(header)

    def test_connection(self):
        # Load constants before actually launching the test
        self.load_constants()

        if (self.ACTIVE): # Only run if test is activated
            n_failures = 0

            with self.wait_for_page_load(timeout=10):
                while True:
                    try:
                        print_header("MAINPAGE", "Testing connection button...")
                        print_warning("MAINPAGE", "Slow down expected.")
                        self.driver.get(self.POLYSAFE_MAINPAGE_URL)
                        connection_button = self.driver.find_element_by_link_text(self.CONNECTION_TEXT)

                        print_header("MAINPAGE", "Found connection button! Trying to click it...")
                        print_warning("MAINPAGE", "Slow down expected.")
                        connection_button.click()

                        print_header("LOGIN_PAGE", "Connection button clicked, comparing URLs...")

                        if (self.driver.current_url == self.EXPECTED_CONNECTION_URL):
                            print_success("LOGIN_PAGE", "URLs are matching!")

                        else:
                            print_failure("LOGIN_PAGE", "URLs are not matching.")
                            return

                        if self.CHECK_LOGIN_CREDENTIALS:
                            print_header("LOGIN_PAGE", "Testing email & password querries...")
                            print_header("LOGIN_PAGE", "Trying to find email & password input boxes...")
                            email_input_box = self.driver.find_element_by_id(self.EMAIL_ID)
                            password_input_box = self.driver.find_element_by_id(self.PASSWORD_ID)
                            print_success("LOGIN_PAGE", "Found email & password input boxes!")
                            print_header("LOGIN_PAGE", "Trying to find connection button...")
                            connection_button = self.driver.find_element_by_id(self.CONNECTION_BTN_ID)
                            print_success("LOGIN_PAGE", "Found connection button!")

                            print_header("LOGIN_PAGE", "Sending invalid keys...")
                            email_input_box.clear()
                            password_input_box.clear()
                            email_input_box.send_keys(self.INVALID_EMAIL)
                            password_input_box.send_keys(self.INVALID_PASSWORD)
                            print_success("LOGIN_PAGE", "Keys sent!")
                            print_header("LOGIN_PAGE", "Trying to click connection button...")
                            print_warning("LOGIN_PAGE", "Slow down expected.")
                            connection_button.click()

                            if self.CHECK_URLS:
                                print_header("LOGIN_PAGE", "Button clicked, comparing URLs...")
                                if (self.driver.current_url == self.EXPECTED_CONNECTION_URL):
                                    print_success("LOGIN_PAGE", "URLs are matching!")

                                else:
                                    print_failure("LOGIN_PAGE", "URLs are not matching.")
                                    return

                            if self.CHECK_ERROR_GENERATION:
                                print_header("LOGIN_PAGE", "Checking if the page generated error (failed login)...")

                                if self.driver.find_element_by_class_name(self.CLOSE_BUTTON) != None:
                                    print_success("LOGIN_PAGE", "Error label found!")

                                print_header("LOGIN_PAGE", "Verifying button linkings...")

                                if self.driver.find_element_by_partial_link_text(self.FORGOT_BUTTON_LINK) != None and \
                                        self.driver.find_element_by_partial_link_text(self.CREATE_ACCOUNT_LINK) != None and \
                                        self.driver.find_element_by_partial_link_text(self.ABOUT_LINK) != None and \
                                        self.driver.find_element_by_partial_link_text(self.SUPPORT_LINK) != None:
                                    print_success("LOGIN_PAGE", "Button linking tests passed!")

                        print_success("LOGIN_PAGE", "All tests passed!")

                    except Exception as e:
                        n_failures += 1  # Increments number of failures
                        exc_type, value, traceback = sys.exc_info()
                        print_failure("TEST_CONNECTION", "Test failed with exception [" + exc_type.__name__ + "]")

                    # Breaking if code has no exception or reaches the limit of retries
                    if (n_failures == 0 or n_failures >= self.LIMIT_OF_RETRIES):
                        break


def main():
    test_mainpage = TestMainpage(webdriver.Chrome(ChromeDriverManager().install()))
    print_header("MAINPAGE", "Testing connection...")

    test_mainpage.test_connection()

    exit()


print_header("MAIN", "Running all tests...")
main()
