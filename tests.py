"""
    Polysafe - User testing.
    Description:    Simulates user interactions for polysafe with Selenium.
    File name:      tests.py
    Author:         Charles De Lafontaine
    Last edition:   06/02/2021
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.expected_conditions import staleness_of
from webdriver_manager.chrome import ChromeDriverManager
from contextlib import contextmanager
import time
import sys
import json
import os

class BgTxtColor:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

"""
    Print color functions depending on tests
"""
def printHeader(category: str, textToPrint: str) -> None:
    print(BgTxtColor.HEADER + BgTxtColor.BOLD + "[" + category + "] > " + BgTxtColor.ENDC + BgTxtColor.OKBLUE + textToPrint + BgTxtColor.ENDC)

def printSuccess(category: str, textToPrint: str) -> None:
    print(BgTxtColor.HEADER + BgTxtColor.BOLD + "[" + category + "] > " + BgTxtColor.ENDC + BgTxtColor.OKGREEN + textToPrint + " ✓ " + BgTxtColor.ENDC)

def printWarning(category: str, textToPrint: str) -> None:
    print(BgTxtColor.HEADER + BgTxtColor.BOLD + "[" + category + "] > " + BgTxtColor.ENDC + BgTxtColor.WARNING + textToPrint + " ⚠ " + BgTxtColor.ENDC)

def printFailure(category: str, textToPrint: str) -> None:
    print(BgTxtColor.HEADER + BgTxtColor.BOLD + "[" + category + "] > " + BgTxtColor.ENDC + BgTxtColor.FAIL + textToPrint + " ✗ " + BgTxtColor.ENDC)


"""
    Globals for JSONFile creation raw output (required for constants)
"""
CONSTANTS_REP                   = "constants"

# for dev_powertool
DEV_POWERTOOL_REP               = "dev_powertool"
DEV_CREDENTIALS_REP             = "dev_credentials"
EMAIL_REP                       = "EMAIL"
PASSWORD_REP                    = "PASSWORD"

# for test_mainpage
TEST_MAINPAGE_REP               = "test_mainpage"
ACTIVE_REP                      = "active"
CHECK_URLS_REP                  = "check_urls"
CHECK_LOGIN_CREDENTIALS_REP     = "check_login_credentials"
CHECK_CONNECTION_BUTTON_REP     = "check_connection_button"
SEND_FAKE_LOGIN_CREDENTIALS_REP = "send_fake_login_credentials"
CHECK_ERROR_GENERATION_REP      = "check_error_generation"
POLYSAFE_MAINPAGE_URL_REP       = "POLYSAFE_MAINPAGE_URL"


"""
    Create a JSON file for tests
"""
class JSONFile():
    def __init__(
        self, 
        file_name               = "\\tests_data.json", 
        file_mode_create        = 'w',
        file_mode_read          = 'r',
        file_encoding           = 'utf-8',
        file_ensure_ascii       = False,
        file_sort_keys          = True,
        file_indent             = 4,
        pwd_override_changed    = ["yes", "y", "oui", "o"],
        pwd_override_unchanged  = ["no", "n", "non"],
        default_data            = {
            DEV_POWERTOOL_REP :[{
                DEV_CREDENTIALS_REP :[{
                    EMAIL_REP:      "charles.delafontaine@gmail.com",
                    PASSWORD_REP:   "Charles1"
                }]
            }],
            TEST_MAINPAGE_REP: [{
                ACTIVE_REP:                         "True",
                CHECK_URLS_REP:                     "True",
                CHECK_LOGIN_CREDENTIALS_REP:        "True",
                CHECK_CONNECTION_BUTTON_REP:        "True",
                SEND_FAKE_LOGIN_CREDENTIALS_REP:    "True",
                CHECK_ERROR_GENERATION_REP:         "True",
                CONSTANTS_REP: [{
                    POLYSAFE_MAINPAGE_URL_REP:      "http://localhost/polysafe/erp/index.php",
                }],
            }
        ]}):
            self.__FILE_NAME               = file_name
            self.__FILE_MODE_CREATE        = file_mode_create
            self.__FILE_MODE_READ          = file_mode_read
            self.__FILE_ENCODING           = file_encoding
            self.__FILE_ENSURE_ASCII       = file_ensure_ascii
            self.__FILE_SORT_KEYS          = file_sort_keys
            self.__FILE_INDENT             = file_indent
            self.__PWD_OVERRIDE_CHANGED    = pwd_override_changed
            self.__PWD_OVERRIDE_UNCHANGED  = pwd_override_unchanged
            self.__DEFAULT_DATA            = default_data
            self.__OS                      = os

    @property
    def FILE_NAME(self) -> str:
        return self.__FILE_NAME
    
    @property
    def FILE_MODE_CREATE(self) -> str:
        return self.__FILE_MODE_CREATE

    @property
    def FILE_MODE_READ(self) -> str:
        return self.__FILE_MODE_READ

    @property
    def FILE_ENCODING(self) -> str:
        return self.__FILE_ENCODING

    @property
    def FILE_ENSURE_ASCII(self) -> str:
        return self.__FILE_ENSURE_ASCII

    @property
    def FILE_SORT_KEYS(self) -> str:
        return self.__FILE_SORT_KEYS

    @property
    def FILE_INDENT(self) -> str:
        return self.__FILE_INDENT

    @property
    def PWD_OVERRIDE_CHANGED(self) -> str:
        return self.__PWD_OVERRIDE_CHANGED

    @property
    def PWD_OVERRIDE_UNCHANGED(self) -> str:
        return self.__PWD_OVERRIDE_UNCHANGED

    @property
    def DEFAULT_DATA(self) -> str:
        return self.__DEFAULT_DATA

    @property
    def OS(self) -> str:
        return self.__OS

    """
        Creates fresh copy of json file.
    """
    def create(self):
        printHeader("JSON_CREATION", "Starting JSON file creation...")
        
        printWarning("JSON_CREATION", "Current working directory: " + self.OS.getcwd() + "\nWould you like to change it? (y/n)")
        pwd_override = input()

        while True:
            if pwd_override not in self.PWD_OVERRIDE_CHANGED and pwd_override not in self.PWD_OVERRIDE_UNCHANGED:
                printFailure("JSON_CREATION", "Invalid command <" + pwd_override + ">, please try again:")
                pwd_override = input()

            elif pwd_override in self.PWD_OVERRIDE_CHANGED:
                break_loop = False

                while True:
                    try:
                        printHeader("JSON_CREATION", "Please enter the new current working directory full path:")
                        new_os_curr_dir = input()
                        self.OS.chdir(new_os_curr_dir)
                        break_loop = True
                
                    except FileNotFoundError or OSError:
                        printFailure("JSON_CREATION", "New directory <" + new_os_curr_dir + "> cannot be found. Please try again.")
                    
                    if break_loop:
                        break
                break
                    
            else:
                break

        with open(self.OS.getcwd() + self.FILE_NAME, self.FILE_MODE_CREATE, encoding=self.FILE_ENCODING) as f:
            json.dump(self.DEFAULT_DATA, f, ensure_ascii=self.FILE_ENSURE_ASCII, sort_keys=self.FILE_SORT_KEYS, indent=self.FILE_INDENT)
        
        printHeader("JSON_CREATION", "Dumped " + str(self.OS.path.getsize(self.OS.getcwd() + self.FILE_NAME)) + " bytes into " + self.OS.getcwd() + self.FILE_NAME)


    """
        Reads the json file and outputs it to a dict.
    """
    def read(self) -> dict:
        try:
            printHeader("JSON_READ", "Trying  to read <" + self.OS.getcwd() + self.FILE_NAME + ">")

            with open(self.OS.getcwd() + self.FILE_NAME, self.FILE_MODE_READ, encoding=self.FILE_ENCODING) as f:
                # Returning empty dict if it crashes
                data = {}

                # Trying to load data into variable
                try:
                    data = json.load(f)
                
                # If it fails for whatever reason, retry with fresh user file
                except Exception:
                    f.close() # Performance purposes while handling exception

                    printFailure("JSON_READ", "Cannot read <" + self.OS.getcwd() + self.FILE_NAME + "> Perhaps the file is corrupted or simply inexistant?")
                    printHeader("JSON_READ_RETRY", "Would you like to load a fresh copy of your json? (y/n)")
                    json_retry_input = input()

                    while json_retry_input not in self.PWD_OVERRIDE_CHANGED and json_retry_input not in self.PWD_OVERRIDE_UNCHANGED:
                        printFailure("JSON_READ_RETRY", "Invalid command <" + json_retry_input + ">, please try again:")
                        json_retry_input = input()

                    # User wants fresh copy
                    if json_retry_input in self.PWD_OVERRIDE_CHANGED:
                        printHeader("JSON_READ_RETRY", "Trying to override the copy of your json with a fresh one...")
                        self.create()
                        printHeader("JSON_READ_RETRY", "Retrying to load data from fresh json copy...")
                        
                        try:
                            with open(self.OS.getcwd() + self.FILE_NAME, self.FILE_MODE_READ, encoding=self.FILE_ENCODING) as f:
                                data = json.load(f)
                                printSuccess("JSON_READ", "Successfully read <" + self.OS.getcwd() + self.FILE_NAME + ">!")

                        except Exception:
                            f.close() # Performance purposes while handling exception
                            printFailure("JSON_READ_RETRY", "Fatal error while reading fresh json copy. I might not have the permission to do that.")

                    # User wants to load copy
                    else:
                        break_loop = False

                        while True:
                            try:
                                printHeader("JSON_READ_RETRY", "Please enter the directory where your .json lays:")
                                own_json_path = input()
                                self.OS.chdir(own_json_path)
                                break_loop = True
                        
                            except FileNotFoundError or OSError:
                                printFailure("JSON_READ_RETRY", "New directory <" + own_json_path + "> cannot be found. Please try again.")

                            if break_loop:
                                break
                        
                        printHeader("JSON_READ_RETRY", "Retrying to load data from fresh json copy...")

                        try:
                            with open(self.OS.getcwd() + self.FILE_NAME, self.FILE_MODE_READ, encoding=self.FILE_ENCODING) as f:
                                data = json.load(f)
                                printSuccess("JSON_READ", "Successfully read <" + self.OS.getcwd() + self.FILE_NAME + ">!")

                        except Exception:
                            f.close() # Performance purposes while handling exception
                            printFailure("JSON_READ_RETRY", "Fatal error while reading fresh json copy. I might not have the permission to do that.")
                
                return data

        except FileNotFoundError:
            printFailure("JSON_READ", "Cannot open file <" + self.OS.getcwd() + self.FILE_NAME + ">")



class TestsInterface():
    """
        Definition:
            Main class to conduct tests.

        Functions:
            driver() -> webdriver                       :: Getter for webdriver.
            driver(new_web_driver)                      :: Setter for webdriver.

        Attributes:
            __driver: webdriver                         :: The webdriver.
    """

    def __init__(self, w_driver: webdriver, jsonfile: JSONFile) -> None:
        self.__DRIVER                       = w_driver
        self.__JSONFILE                     = jsonfile
        self.__POLYSAFE_DEVELOPER_EMAIL     = None
        self.__POLYSAFE_DEVELOPER_PASSWORD  = None

    @property
    def DRIVER(self) -> webdriver:
        return self.__DRIVER

    @DRIVER.setter
    def DRIVER(self, new_web_driver: webdriver) -> None:
        self.__DRIVER = new_web_driver

    @property
    def POLYSAFE_DEVELOPER_EMAIL(self) -> str:
        return self.__POLYSAFE_DEVELOPER_EMAIL

    @property
    def POLYSAFE_DEVELOPER_PASSWORD(self) -> str:
        return self.__POLYSAFE_DEVELOPER_PASSWORD


    @property
    def jsonfile(self) -> JSONFile:
        return self.__JSONFILE

    # Simplify jsonfile getter for dictionary
    def jsondump(self) -> dict:
        return self.jsonfile.read()
    
    
    def verify_json_tests_integrity(self):
        print(self.jsondump().keys())

    
    """
        Verify that json contains all constants for TestsInterface
    """
    def load_constants(self):
        self.__POLYSAFE_DEVELOPER_EMAIL     = self.jsonfile[DEV_POWERTOOL_REP][DEV_CREDENTIALS_REP][EMAIL_REP]
        self.__POLYSAFE_DEVELOPER_PASSWORD  = self.jsonfile[DEV_POWERTOOL_REP][DEV_CREDENTIALS_REP][PASSWORD_REP]


class TestMainpage(TestsInterface):
    def __init__(self, w_driver: webdriver) -> None:
        super().__init__(w_driver, JSONFile())
        self.__ACTIVE                       = None
        self.__CHECK_URLS                   = None
        self.__CHECK_LOGIN_CREDENTIALS      = None
        self.__CHECK_CONNECTION_BUTTON      = None
        self.__SEND_FAKE_LOGIN_CREDENTIALS  = None
        self.__CHECK_ERROR_GENERATION       = None
        self.__POLYSAFE_MAINPAGE_URL        = None

    @property
    def POLYSAFE_MAINPAGE_URL(self) -> str:
        return self.__POLYSAFE_MAINPAGE_URL

    @property
    def ACTIVE(self) -> str:
        return self.__ACTIVE

    @property
    def CHECK_URLS(self) -> str:
        return self.__CHECK_URLS

    @property
    def CHECK_LOGIN_CREDENTIALS(self) -> str:
        return self.__CHECK_LOGIN_CREDENTIALS

    @property
    def CHECK_CONNECTION_BUTTON(self) -> str:
        return self.__CHECK_CONNECTION_BUTTON

    @property
    def SEND_FAKE_LOGIN_CREDENTIALS(self) -> str:
        return self.__SEND_FAKE_LOGIN_CREDENTIALS

    @property
    def CHECK_ERROR_GENERATION(self) -> str:
        return self.__CHECK_ERROR_GENERATION

    @property
    def POLYSAFE_MAINPAGE_URL(self) -> str:
        return self.__POLYSAFE_MAINPAGE_URL


    """
        Verify that json contains all constants for TestMainpage 
    """
    def load_constants(self):
        self.__POLYSAFE_MAINPAGE_URL        = self.jsonfile[TEST_MAINPAGE_REP]
        self.__ACTIVE                       = self.jsonfile[ACTIVE_REP]
        self.__CHECK_URLS                   = self.jsonfile[CHECK_URLS_REP]
        self.__CHECK_LOGIN_CREDENTIALS      = self.jsonfile[CHECK_LOGIN_CREDENTIALS_REP]
        self.__CHECK_LOGIN_CREDENTIALS      = self.jsonfile[CHECK_LOGIN_CREDENTIALS_REP]
        self.__SEND_FAKE_LOGIN_CREDENTIALS  = self.jsonfile[SEND_FAKE_LOGIN_CREDENTIALS_REP]
        self.__CHECK_ERROR_GENERATION       = self.jsonfile[CHECK_ERROR_GENERATION_REP]

    @contextmanager
    def wait_for_page_load(self, timeout=30): # Source: https://www.cloudbees.com/blog/get-selenium-to-wait-for-page-load/
        old_page = self.driver.find_element_by_tag_name('html')
        yield
        WebDriverWait(self.driver, timeout).until(
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
        #print(self.jsonfile.read()['test_mainpage']['active'])
        # for header in self.jsondump:
        #     print(header)


    def test_connection(self):
        CONNECTION_TEXT         = 'Connexion »'
        LIMIT_OF_RETRIES        = 0
        n_failures              = 0
        
        with self.wait_for_page_load(timeout=10):
            while True:
                try:
                    printHeader("MAINPAGE", "Testing connection button...")
                    printWarning("MAINPAGE", "Slow down expected.")
                    self.driver.get(POLYSAFE_MAINPAGE_URL)
                    connection_button = self.driver.find_element_by_link_text(CONNECTION_TEXT)

                    printHeader("MAINPAGE", "Found connection button! Trying to click it...")
                    printWarning("MAINPAGE", "Slow down expected.")
                    connection_button.click()
                    
                    printHeader("LOGIN_PAGE", "Connection button clicked, comparing URLs...")
                    EXPECTED_CONNECTION_URL = 'http://localhost/polysafe/erp/users/login.php'

                    if (self.driver.current_url == EXPECTED_CONNECTION_URL):
                        printSuccess("LOGIN_PAGE", "URLs are matching!")

                    else:
                        printFailure("LOGIN_PAGE", "URLs are not matching.")
                        return
                    
                    printHeader("LOGIN_PAGE", "Testing email & password querries...")
                    printHeader("LOGIN_PAGE", "Trying to find email & password input boxes...")
                    EMAIL_ID            = "username"
                    PASSWORD_ID         = "password"
                    CONNECTION_BTN_ID   = "next_button"
                    email_input_box     = self.driver.find_element_by_id(EMAIL_ID)
                    password_input_box  = self.driver.find_element_by_id(PASSWORD_ID)
                    printSuccess("LOGIN_PAGE", "Found email & password input boxes!")
                    printHeader("LOGIN_PAGE", "Trying to find connection button...")
                    connection_button   = self.driver.find_element_by_id(CONNECTION_BTN_ID)
                    printSuccess("LOGIN_PAGE", "Found connection button!")

                    printHeader("LOGIN_PAGE", "Sending invalid keys...")
                    INVALID_EMAIL       = "invalid.email@gmail.ca"
                    INVALID_PASSWORD    = "password1234"
                    email_input_box.clear()
                    password_input_box.clear()
                    email_input_box.send_keys(INVALID_EMAIL)
                    password_input_box.send_keys(INVALID_PASSWORD)
                    printSuccess("LOGIN_PAGE", "Keys sent!")
                    printHeader("LOGIN_PAGE", "Trying to click connection button...")
                    printWarning("LOGIN_PAGE", "Slow down expected.")
                    connection_button.click()

                    printHeader("LOGIN_PAGE", "Button clicked, comparing URLs...")
                    if (self.driver.current_url == EXPECTED_CONNECTION_URL):
                        printSuccess("LOGIN_PAGE", "URLs are matching!")

                    else:
                        printFailure("LOGIN_PAGE", "URLs are not matching.")
                        return

                    printHeader("LOGIN_PAGE", "Checking if the page generated error (failed login)...")
                    CLOSE_BUTTON = "close"

                    if self.driver.find_element_by_class_name(CLOSE_BUTTON) != None:
                        printSuccess("LOGIN_PAGE", "Error label found!")

                    printHeader("LOGIN_PAGE", "Verifying button linkings...")

                    FORGOT_BUTTON_LINK  = "Mot de passe oub"
                    CREATE_ACCOUNT_LINK = "Créer un compte"
                    ABOUT_LINK          = "propos"
                    SUPPORT_LINK        = "Support"

                    if  self.driver.find_element_by_partial_link_text(FORGOT_BUTTON_LINK)   != None and \
                        self.driver.find_element_by_partial_link_text(CREATE_ACCOUNT_LINK)  != None and \
                        self.driver.find_element_by_partial_link_text(ABOUT_LINK)           != None and \
                        self.driver.find_element_by_partial_link_text(SUPPORT_LINK)         != None:
                        printSuccess("LOGIN_PAGE", "Button linking tests passed!")
                    
                    printSuccess("LOGIN_PAGE", "All tests passed!")

                except Exception as e:
                    n_failures += 1 # Increments number of failures
                    exc_type, value, traceback = sys.exc_info()
                    printFailure("TEST_CONNECTION", "Test failed with exception [" + exc_type.__name__ + "]")
            

                # Breaking if code has no exception or reaches the limit of retries
                if (n_failures == 0 or n_failures >= LIMIT_OF_RETRIES):
                    break


def main():
    test_mainpage = TestMainpage(webdriver.Chrome(ChromeDriverManager().install()))
    printHeader("MAINPAGE", "Testing connection...")
    
    #test_mainpage.test_connection()
    test_mainpage.verify_json_tests_integrity()
    exit()

printHeader("MAIN", "Running all tests...")
main()
