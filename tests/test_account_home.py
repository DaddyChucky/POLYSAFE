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
    def formation_btn(self):
        return self.__FORMATION_BTN

    @formation_btn.setter
    def formation_btn(self, new_formation_btn) -> None:
        self.__FORMATION_BTN = new_formation_btn

    @property
    def reserve_btn(self):
        return self.__RESERVE_BTN

    @reserve_btn.setter
    def reserve_btn(self, new_reserve_btn) -> None:
        self.__RESERVE_BTN = new_reserve_btn

    @property
    def contact_btn(self):
        return self.__CONTACT_BTN

    @contact_btn.setter
    def contact_btn(self, new_contact_btn) -> None:
        self.__CONTACT_BTN = new_contact_btn

    @property
    def calendar_btn(self):
        return self.__CALENDAR_BTN

    @calendar_btn.setter
    def calendar_btn(self, new_calendar_btn) -> None:
        self.__CALENDAR_BTN = new_calendar_btn

    @property
    def membership_details_btn(self):
        return self.__MEMBERSHIP_DETAILS_BTN

    @membership_details_btn.setter
    def membership_details_btn(self, new_membership_details_btn) -> None:
        self.__MEMBERSHIP_DETAILS_BTN = new_membership_details_btn

    @property
    def billing_details_btn(self):
        return self.__BILLING_DETAILS_BTN

    @billing_details_btn.setter
    def billing_details_btn(self, new_billing_details_btn) -> None:
        self.__BILLING_DETAILS_BTN = new_billing_details_btn

    @property
    def purchase_details_btn(self):
        return self.__PURCHASE_DETAILS_BTN

    @purchase_details_btn.setter
    def purchase_details_btn(self, new_purchase_details_btn) -> None:
        self.__PURCHASE_DETAILS_BTN = new_purchase_details_btn

    @property
    def formation_btn_label(self) -> str:
        return self.__FORMATION_BTN_LABEL

    @formation_btn_label.setter
    def formation_btn_label(self, new_formation_btn_label: str) -> None:
        self.__FORMATION_BTN_LABEL = new_formation_btn_label

    @property
    def reserve_btn_label(self) -> str:
        return self.__RESERVE_BTN_LABEL

    @reserve_btn_label.setter
    def reserve_btn_label(self, new_reserve_btn_label: str) -> None:
        self.__RESERVE_BTN_LABEL = new_reserve_btn_label

    @property
    def contact_btn_label(self) -> str:
        return self.__CONTACT_BTN_LABEL

    @contact_btn_label.setter
    def contact_btn_label(self, new_contact_btn_label: str) -> None:
        self.__CONTACT_BTN_LABEL = new_contact_btn_label

    @property
    def calendar_lnk_label(self) -> str:
        return self.__CALENDAR_LNK_LABEL

    @calendar_lnk_label.setter
    def calendar_lnk_label(self, new_calendar_lnk_label: str) -> None:
        self.__CALENDAR_LNK_LABEL = new_calendar_lnk_label

    @property
    def membership_details_btn_label(self) -> str:
        return self.__MEMBERSHIP_DETAILS_BTN_LABEL

    @membership_details_btn_label.setter
    def membership_details_btn_label(self, new_membership_details_btn_label: str) -> None:
        self.__MEMBERSHIP_DETAILS_BTN_LABEL = new_membership_details_btn_label

    @property
    def billing_details_btn_label(self) -> str:
        return self.__BILLING_DETAILS_BTN_LABEL

    @billing_details_btn_label.setter
    def billing_details_btn_label(self, new_billing_details_btn_label: str) -> None:
        self.__BILLING_DETAILS_BTN_LABEL = new_billing_details_btn_label

    @property
    def purchase_details_btn_label(self) -> str:
        return self.__PURCHASE_DETAILS_BTN_LABEL

    @purchase_details_btn_label.setter
    def purchase_details_btn_label(self, new_purchase_details_btn_label: str) -> None:
        self.__PURCHASE_DETAILS_BTN_LABEL = new_purchase_details_btn_label

    @property
    def window_current_id(self) -> int:
        return self.__CURR_WINDOW_ID

    @window_current_id.setter
    def window_current_id(self, new_window_current_id: int) -> None:
        self.__CURR_WINDOW_ID = new_window_current_id

    @property
    def my_calendar_lnk_label(self) -> str:
        return self.__MY_CALENDAR_LNK_LABEL

    @my_calendar_lnk_label.setter
    def my_calendar_lnk_label(self, new_my_calendar_lnk_label: str) -> None:
        self.__MY_CALENDAR_LNK_LABEL = new_my_calendar_lnk_label

    @property
    def new_reservation_lnk_label(self) -> str:
        return self.__NEW_RESERVATION_LNK_LABEL

    @new_reservation_lnk_label.setter
    def new_reservation_lnk_label(self, new_new_reservation_lnk_label: str) -> None:
        self.__NEW_RESERVATION_LNK_LABEL = new_new_reservation_lnk_label

    @property
    def printing_lnk_label(self) -> str:
        return self.__PRINTING_LNK_LABEL

    @printing_lnk_label.setter
    def printing_lnk_label(self, new_printing_lnk_label: str) -> None:
        self.__PRINTING_LNK_LABEL = new_printing_lnk_label

    @property
    def openings_lnk_label(self) -> str:
        return self.calendar_lnk_label.capitalize()

    @openings_lnk_label.setter
    def openings_lnk_label(self, new_openings_lnk_label: str) -> None:
        self.calendar_lnk_label = new_openings_lnk_label.lower()

    @property
    def live_printing_lnk_label(self) -> str:
        return self.__LIVE_PRINTING_LNK_LABEL

    @live_printing_lnk_label.setter
    def live_printing_lnk_label(self, new_live_printing_lnk_label: str) -> None:
        self.__LIVE_PRINTING_LNK_LABEL = new_live_printing_lnk_label

    @property
    def reserve_formation_lnk_label(self) -> str:
        return self.__RESERVE_FORMATION_LNK_LABEL

    @reserve_formation_lnk_label.setter
    def reserve_formation_lnk_label(self, new_reserve_formation_lnk_label: str) -> None:
        self.__RESERVE_FORMATION_LNK_LABEL = new_reserve_formation_lnk_label

    @property
    def global_calendar_lnk_label(self) -> str:
        return self.__GLOBAL_CALENDAR_LNK_LABEL

    @global_calendar_lnk_label.setter
    def global_calendar_lnk_label(self, new_global_calendar_lnk_label: str) -> None:
        self.__GLOBAL_CALENDAR_LNK_LABEL = new_global_calendar_lnk_label

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
                self.formation_btn_label = \
                    self.jsondump[TEST_ACCOUNT_HOME_REP][CONSTANTS_REP][FORMATION_BTN_LABEL_REP]
                self.reserve_btn_label = self.jsondump[TEST_ACCOUNT_HOME_REP][CONSTANTS_REP][RESERVE_BTN_LABEL_REP]
                self.contact_btn_label = self.jsondump[TEST_ACCOUNT_HOME_REP][CONSTANTS_REP][CONTACT_BTN_LABEL_REP]
                self.calendar_lnk_label = self.jsondump[TEST_ACCOUNT_HOME_REP][CONSTANTS_REP][CALENDAR_LNK_LABEL_REP]
                self.membership_details_btn_label = \
                    self.jsondump[TEST_ACCOUNT_HOME_REP][CONSTANTS_REP][MEMBERSHIP_DETAILS_BTN_LABEL_REP]
                self.billing_details_btn_label = \
                    self.jsondump[TEST_ACCOUNT_HOME_REP][CONSTANTS_REP][BILLING_DETAILS_BTN_LABEL_REP]
                self.purchase_details_btn_label = \
                    self.jsondump[TEST_ACCOUNT_HOME_REP][CONSTANTS_REP][PURCHASE_DETAILS_BTN_LABEL_REP]
                self.my_calendar_lnk_label = \
                    self.jsondump[TEST_ACCOUNT_HOME_REP][CONSTANTS_REP][MY_CALENDAR_LNK_LABEL_REP]
                self.new_reservation_lnk_label = \
                    self.jsondump[TEST_ACCOUNT_HOME_REP][CONSTANTS_REP][NEW_RESERVATION_LNK_LABEL_REP]
                self.printing_lnk_label = \
                    self.jsondump[TEST_ACCOUNT_HOME_REP][CONSTANTS_REP][PRINTING_LNK_LABEL_REP]
                self.openings_lnk_label = \
                    self.jsondump[TEST_ACCOUNT_HOME_REP][CONSTANTS_REP][CALENDAR_LNK_LABEL_REP]
                self.live_printing_lnk_label = \
                    self.jsondump[TEST_ACCOUNT_HOME_REP][CONSTANTS_REP][LIVE_PRINTING_LNK_LABEL_REP]
                self.reserve_formation_lnk_label = \
                    self.jsondump[TEST_ACCOUNT_HOME_REP][CONSTANTS_REP][RESERVE_LNK_LABEL_REP]
                self.global_calendar_lnk_label = \
                    self.jsondump[TEST_ACCOUNT_HOME_REP][CONSTANTS_REP][GLOBAL_CALENDAR_REP]

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

                        print_header("POLYSAFE_TEST_ACCOUNT_HOME", "Getting buttons...")
                        self.formation_btn = self.driver.find_element_by_partial_link_text(self.formation_btn_label)
                        xpath_reserve_btn: str = "//button[text()='" + self.reserve_btn_label + "']"
                        self.reserve_btn = self.driver.find_element_by_xpath(xpath_reserve_btn)
                        self.contact_btn = self.driver.find_element_by_partial_link_text(self.contact_btn_label)
                        self.calendar_lnk = self.driver.find_elements_by_xpath("//a[text()=' Mon calendrier']")
                        self.membership_details_btn = \
                            self.driver.find_element_by_partial_link_text(self.membership_details_btn_label)
                        self.billing_details_btn = \
                            self.driver.find_element_by_partial_link_text(self.billing_details_btn_label)
                        self.purchase_details_btn = \
                            self.driver.find_element_by_partial_link_text(self.purchase_details_btn_label)
                        self.new_reservation_lnk = self.driver.find_elements_by_xpath("//h5[text()=' Nouvelle réservation']")
                        self.new_reservation_lnk.click()
                        print("Working")
                        # self.new_reservation_lnk = \
                        #     self.driver.find_element_by_partial_link_text(self.new_reservation_lnk_label)

                        self.my_calendar_lnk = self.driver.find_element_by_partial_link_text(self.my_calendar_lnk_label)

                        self.printing_lnk = \
                            self.driver.find_element_by_partial_link_text(self.printing_lnk_label)
                        self.openings_lnk = self.driver.find_element_by_partial_link_text(self.openings_lnk_label)
                        self.live_printing_lnk = \
                            self.driver.find_element_by_partial_link_text(self.live_printing_lnk_label)
                        self.reserve_formation_lnk = \
                            self.driver.find_element_by_partial_link_text(self.reserve_formation_lnk_label)
                        self.global_calendar_lnk = \
                            self.driver.find_element_by_partial_link_text(self.global_calendar_lnk_label)

                        print_header("POLYSAFE_TEST_ACCOUNT_HOME", "Testing buttons linking...")

                        print_header("POLYSAFE_TEST_ACCOUNT_HOME", "Testing formation button linking...")
                        print_warning("POLYSAFE_TEST_ACCOUNT_HOME", "Slow down expected.")
                        self.formation_btn.click()

                        self.switch_current_window()

                        if self.driver.find_element_by_xpath("//*[contains(text(), ERROR_404)]") \
                                is not None:
                            print_failure("POLYSAFE_TEST_ACCOUNT_HOME", "Formation button link is invalid.")

                        else:
                            print_success("POLYSAFE_TEST_ACCOUNT_HOME", "Formation button link is valid!")

                        self.close_current_window()

                        print_header("POLYSAFE_TEST_ACCOUNT_HOME", "Testing reserve button linking...")
                        print_warning("POLYSAFE_TEST_ACCOUNT_HOME", "Slow down expected.")
                        self.reserve_btn.click()

                        self.switch_current_window()

                        if self.driver.find_element_by_xpath("//*[contains(text(), ERROR_404)]") \
                                is not None:
                            print_failure("POLYSAFE_TEST_ACCOUNT_HOME", "Reserve button link is invalid.")

                        else:
                            print_success("POLYSAFE_TEST_ACCOUNT_HOME", "Reserve button link is valid!")

                        self.close_current_window()

                        print_header("POLYSAFE_TEST_ACCOUNT_HOME", "Testing contact button linking...")
                        print_warning("POLYSAFE_TEST_ACCOUNT_HOME", "Slow down expected.")
                        self.contact_btn.click()

                        self.switch_current_window()

                        if self.driver.find_element_by_xpath("//*[contains(text(), ERROR_404)]") \
                                is not None:
                            print_failure("POLYSAFE_TEST_ACCOUNT_HOME", "Contact button link is invalid.")

                        else:
                            print_success("POLYSAFE_TEST_ACCOUNT_HOME", "Contact button link is valid!")

                        self.close_current_window()

                        print_header("POLYSAFE_TEST_ACCOUNT_HOME", "Testing calendar button linking...")
                        print_warning("POLYSAFE_TEST_ACCOUNT_HOME", "Slow down expected.")
                        self.calendar_btn.click()

                        self.switch_current_window()

                        if self.driver.find_element_by_xpath("//*[contains(text(), ERROR_404)]") \
                                is not None:
                            print_failure("POLYSAFE_TEST_ACCOUNT_HOME", "Calendar button link is invalid.")

                        else:
                            print_success("POLYSAFE_TEST_ACCOUNT_HOME", "Calendar button link is valid!")

                        self.close_current_window()

                        print_header("POLYSAFE_TEST_ACCOUNT_HOME", "Testing membership button linking...")
                        print_warning("POLYSAFE_TEST_ACCOUNT_HOME", "Slow down expected.")
                        self.membership_details_btn.click()

                        self.switch_current_window()

                        if self.driver.find_element_by_xpath("//*[contains(text(), ERROR_404)]") \
                                is not None:
                            print_failure("POLYSAFE_TEST_ACCOUNT_HOME", "Membership details button link is invalid.")

                        else:
                            print_success("POLYSAFE_TEST_ACCOUNT_HOME", "Membership details button link is valid!")

                        self.close_current_window()

                        print_header("POLYSAFE_TEST_ACCOUNT_HOME", "Testing billing details button linking...")
                        print_warning("POLYSAFE_TEST_ACCOUNT_HOME", "Slow down expected.")
                        self.billing_details_btn.click()

                        self.switch_current_window()

                        if self.driver.find_element_by_xpath("//*[contains(text(), ERROR_404)]") \
                                is not None:
                            print_failure("POLYSAFE_TEST_ACCOUNT_HOME", "Billing details button link is invalid.")

                        else:
                            print_success("POLYSAFE_TEST_ACCOUNT_HOME", "Billing details button link is valid!")

                        self.close_current_window()

                        print_header("POLYSAFE_TEST_ACCOUNT_HOME", "Testing purchase details button linking...")
                        print_warning("POLYSAFE_TEST_ACCOUNT_HOME", "Slow down expected.")
                        self.purchase_details_btn.click()

                        self.switch_current_window()

                        if self.driver.find_element_by_xpath("//*[contains(text(), ERROR_404)]") \
                                is not None:
                            print_failure("POLYSAFE_TEST_ACCOUNT_HOME", "Purchase details button link is invalid.")

                        else:
                            print_success("POLYSAFE_TEST_ACCOUNT_HOME", "Purchase details button link is valid!")

                        self.close_current_window()

                        print_header("POLYSAFE_TEST_ACCOUNT_HOME", "Testing my calendar linking...")
                        print_warning("POLYSAFE_TEST_ACCOUNT_HOME", "Slow down expected.")
                        self.my_calendar_lnk.click()

                        self.switch_current_window()

                        if self.driver.find_element_by_xpath("//*[contains(text(), ERROR_404)]") \
                                is not None:
                            print_failure("POLYSAFE_TEST_ACCOUNT_HOME", "My calendar link is invalid.")

                        else:
                            print_success("POLYSAFE_TEST_ACCOUNT_HOME", "My calendar link is valid!")

                        self.close_current_window()

                        print_header("POLYSAFE_TEST_ACCOUNT_HOME", "Testing new reservation linking...")
                        print_warning("POLYSAFE_TEST_ACCOUNT_HOME", "Slow down expected.")
                        self.new_reservation_lnk.click()

                        self.switch_current_window()

                        if self.driver.find_element_by_xpath("//*[contains(text(), ERROR_404)]") \
                                is not None:
                            print_failure("POLYSAFE_TEST_ACCOUNT_HOME", "New reservation link is invalid.")

                        else:
                            print_success("POLYSAFE_TEST_ACCOUNT_HOME", "New reservation link is valid!")

                        self.close_current_window()

                        print_header("POLYSAFE_TEST_ACCOUNT_HOME", "Testing printing linking...")
                        print_warning("POLYSAFE_TEST_ACCOUNT_HOME", "Slow down expected.")
                        self.printing_lnk.click()

                        self.switch_current_window()

                        if self.driver.find_element_by_xpath("//*[contains(text(), ERROR_404)]") \
                                is not None:
                            print_failure("POLYSAFE_TEST_ACCOUNT_HOME", "Printing link is invalid.")

                        else:
                            print_success("POLYSAFE_TEST_ACCOUNT_HOME", "Printing link is valid!")

                        self.close_current_window()

                        print_header("POLYSAFE_TEST_ACCOUNT_HOME", "Testing openings linking...")
                        print_warning("POLYSAFE_TEST_ACCOUNT_HOME", "Slow down expected.")
                        self.openings_lnk.click()

                        self.switch_current_window()

                        if self.driver.find_element_by_xpath("//*[contains(text(), ERROR_404)]") \
                                is not None:
                            print_failure("POLYSAFE_TEST_ACCOUNT_HOME", "Openings link is invalid.")

                        else:
                            print_success("POLYSAFE_TEST_ACCOUNT_HOME", "Openings link is valid!")

                        self.close_current_window()

                        print_header("POLYSAFE_TEST_ACCOUNT_HOME", "Testing live printing linking...")
                        print_warning("POLYSAFE_TEST_ACCOUNT_HOME", "Slow down expected.")
                        self.live_printing_lnk.click()

                        self.switch_current_window()

                        if self.driver.find_element_by_xpath("//*[contains(text(), ERROR_404)]") \
                                is not None:
                            print_failure("POLYSAFE_TEST_ACCOUNT_HOME", "Live printing link is invalid.")

                        else:
                            print_success("POLYSAFE_TEST_ACCOUNT_HOME", "Live printing link is valid!")

                        self.close_current_window()

                        print_header("POLYSAFE_TEST_ACCOUNT_HOME", "Testing reserve a formation linking...")
                        print_warning("POLYSAFE_TEST_ACCOUNT_HOME", "Slow down expected.")
                        self.reserve_formation_lnk.click()

                        self.switch_current_window()

                        if self.driver.find_element_by_xpath("//*[contains(text(), ERROR_404)]") \
                                is not None:
                            print_failure("POLYSAFE_TEST_ACCOUNT_HOME", "Reserve formation link is invalid.")

                        else:
                            print_success("POLYSAFE_TEST_ACCOUNT_HOME", "Reserve formation link is valid!")

                        self.close_current_window()

                        print_header("POLYSAFE_TEST_ACCOUNT_HOME", "Testing global calendar linking...")
                        print_warning("POLYSAFE_TEST_ACCOUNT_HOME", "Slow down expected.")
                        self.global_calendar_lnk.click()

                        self.switch_current_window()

                        if self.driver.find_element_by_xpath("//*[contains(text(), ERROR_404)]") \
                                is not None:
                            print_failure("POLYSAFE_TEST_ACCOUNT_HOME", "Global calendar link is invalid.")

                        else:
                            print_success("POLYSAFE_TEST_ACCOUNT_HOME", "Global calendar link is valid!")

                        self.close_current_window()

                        print_success("POLYSAFE_TEST_ACCOUNT_HOME", "Tested every link!")
                        print_success("LOGIN_PAGE", "All tests passed!")

                    except Exception:
                        n_failures += 1  # Increments number of failures
                        exc_type, value, traceback = sys.exc_info()
                        print_failure(
                            "TEST_ACCOUNT_HOME", "Test failed with exception [" + exc_type.__name__ + "]")

                    # Breaking if code has no exception or reaches the limit of retries
                    if n_failures == 0 or n_failures >= self.limit_of_retries:
                        break
