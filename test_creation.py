"""
    Polysafe - User testing.
    Description:    TestCreation class definition.
    File name:      test_creation.py
    Author:         Charles De Lafontaine
    Last edition:   06/29/2021
"""

from tests_interface import *
import sys
from random import randint as ri


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
        self.__CHART_OF_PAYMENT_LNK = None
        self.__LEGAL_LNK = None
        self.__USERNAME_ID_REP = None
        self.__FIRST_NAME_ID_REP = None
        self.__LAST_NAME_ID_REP = None
        self.__EMAIL_ID = None
        self.__PASSWORD_ID = None
        self.__CONFIRM_PASSWORD_ID_REP = None
        self.__CELLPHONE_NUMBER_ID_REP = None
        self.__CHECKBOX_CONTRACT_ID_REP = None
        self.__CHECKBOX_CHART_OF_PAYMENT_ID_REP = None
        self.__CHECKBOX_LEGAL_ID_REP = None
        self.__USERNAME_QRY = None
        self.__FIRST_NAME_QRY = None
        self.__LAST_NAME_QRY = None
        self.__EMAIL_QRY = None
        self.__PASSWORD_QRY = None
        self.__CONFIRM_PASSWORD_QRY = None
        self.__CELLPHONE_NUMBER_QRY = None
        self.__CHECKBOX_LEGAL_QRY = None
        self.__CHECKBOX_CONTRACT_QRY = None
        self.__CHECKBOX_CHART_OF_PAYMENT_QRY = None
        self.__CREATE_ACCOUNT_BTN_LABEL = None
        self.__CREATE_ACCOUNT_BTN = None
        self.__CURR_WINDOW_ID = 0
        self.__ERROR_CLASS_LABEL = None

    @property
    def polysafe_create_account_url(self) -> str:
        return self.__POLYSAFE_CREATE_ACCOUNT_URL

    @polysafe_create_account_url.setter
    def polysafe_create_account_url(self, new_polysafe_create_account_url: str) -> None:
        self.__POLYSAFE_CREATE_ACCOUNT_URL = new_polysafe_create_account_url

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
    def limit_of_retries(self, new_limit_of_retries: int) -> None:
        self.__LIMIT_OF_RETRIES = new_limit_of_retries

    @property
    def valid_registration_number_list(self) -> list:
        return list(self.__VALID_REGISTRATION_NUMBER_LIST)

    @valid_registration_number_list.setter
    def valid_registration_number_list(self, new_valid_registration_number_list: list) -> None:
        self.__VALID_REGISTRATION_NUMBER_LIST = new_valid_registration_number_list

    @property
    def invalid_registration_number_list(self) -> list:
        return list(self.__INVALID_REGISTRATION_NUMBER_LIST)

    @invalid_registration_number_list.setter
    def invalid_registration_number_list(self, new_invalid_registration_number_list: list) -> None:
        self.__INVALID_REGISTRATION_NUMBER_LIST = new_invalid_registration_number_list

    @property
    def valid_name_list(self) -> list:
        return list(self.__VALID_NAME_LIST)

    @valid_name_list.setter
    def valid_name_list(self, new_valid_name_list: list) -> None:
        self.__VALID_NAME_LIST = new_valid_name_list

    @property
    def invalid_name_list(self) -> list:
        return list(self.__INVALID_NAME_LIST)

    @invalid_name_list.setter
    def invalid_name_list(self, new_invalid_name_list: list) -> None:
        self.__INVALID_NAME_LIST = new_invalid_name_list

    @property
    def valid_email_list(self) -> list:
        return list(self.__VALID_EMAIL_LIST)

    @valid_email_list.setter
    def valid_email_list(self, new_valid_email_list: list) -> None:
        self.__VALID_EMAIL_LIST = new_valid_email_list

    @property
    def invalid_email_list(self) -> list:
        return list(self.__INVALID_EMAIL_LIST)

    @invalid_email_list.setter
    def invalid_email_list(self, new_invalid_email_list: list) -> None:
        self.__INVALID_EMAIL_LIST = new_invalid_email_list

    @property
    def valid_password_list(self) -> list:
        return list(self.__VALID_PASSWORD_LIST)

    @valid_password_list.setter
    def valid_password_list(self, new_valid_password_list: list) -> None:
        self.__VALID_PASSWORD_LIST = new_valid_password_list

    @property
    def invalid_password_list(self) -> list:
        return list(self.__INVALID_PASSWORD_LIST)

    @invalid_password_list.setter
    def invalid_password_list(self, new_invalid_password_list: list) -> None:
        self.__INVALID_PASSWORD_LIST = new_invalid_password_list

    @property
    def valid_cellphone_number_list(self) -> list:
        return list(self.__VALID_CELLPHONE_NUMBER_LIST)

    @valid_cellphone_number_list.setter
    def valid_cellphone_number_list(self, new_valid_cellphone_number_list: list) -> None:
        self.__VALID_CELLPHONE_NUMBER_LIST = new_valid_cellphone_number_list

    @property
    def invalid_cellphone_number_list(self) -> list:
        return list(self.__INVALID_CELLPHONE_NUMBER_LIST)

    @invalid_cellphone_number_list.setter
    def invalid_cellphone_number_list(self, new_invalid_cellphone_number_list: list) -> None:
        self.__INVALID_CELLPHONE_NUMBER_LIST = new_invalid_cellphone_number_list

    @property
    def account_creation_contract(self) -> str:
        return self.__ACCOUNT_CREATION_CONTRACT_LNK

    @account_creation_contract.setter
    def account_creation_contract(self, new_account_creation_contract: str) -> None:
        self.__ACCOUNT_CREATION_CONTRACT_LNK = new_account_creation_contract

    @property
    def chart_of_payment(self) -> str:
        return self.__CHART_OF_PAYMENT_LNK

    @chart_of_payment.setter
    def chart_of_payment(self, new_chart_of_payment: str) -> None:
        self.__CHART_OF_PAYMENT_LNK = new_chart_of_payment

    @property
    def legal(self) -> str:
        return self.__LEGAL_LNK

    @legal.setter
    def legal(self, new_legal: str) -> None:
        self.__LEGAL_LNK = new_legal

    @property
    def username_id(self) -> str:
        return self.__USERNAME_ID_REP

    @username_id.setter
    def username_id(self, new_username_id: str) -> None:
        self.__USERNAME_ID_REP = new_username_id

    @property
    def first_name_id(self) -> str:
        return self.__FIRST_NAME_ID_REP

    @first_name_id.setter
    def first_name_id(self, new_first_name_id: str) -> None:
        self.__FIRST_NAME_ID_REP = new_first_name_id

    @property
    def last_name_id(self) -> str:
        return self.__LAST_NAME_ID_REP

    @last_name_id.setter
    def last_name_id(self, new_last_name_id: str) -> None:
        self.__LAST_NAME_ID_REP = new_last_name_id

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
    def confirm_password_id(self) -> str:
        return self.__CONFIRM_PASSWORD_ID_REP

    @confirm_password_id.setter
    def confirm_password_id(self, new_confirm_password_id: str) -> None:
        self.__CONFIRM_PASSWORD_ID_REP = new_confirm_password_id

    @property
    def cellphone_number_id(self) -> str:
        return self.__CELLPHONE_NUMBER_ID_REP

    @cellphone_number_id.setter
    def cellphone_number_id(self, new_cellphone_number_id: str) -> None:
        self.__CELLPHONE_NUMBER_ID_REP = new_cellphone_number_id

    @property
    def checkbox_contract_id(self) -> str:
        return self.__CHECKBOX_CONTRACT_ID_REP

    @checkbox_contract_id.setter
    def checkbox_contract_id(self, new_checkbox_contract_id: str) -> None:
        self.__CHECKBOX_CONTRACT_ID_REP = new_checkbox_contract_id

    @property
    def checkbox_chart_of_payment_id(self) -> str:
        return self.__CHECKBOX_CHART_OF_PAYMENT_ID_REP

    @checkbox_chart_of_payment_id.setter
    def checkbox_chart_of_payment_id(self, new_checkbox_chart_of_payment_id: str) -> None:
        self.__CHECKBOX_CHART_OF_PAYMENT_ID_REP = new_checkbox_chart_of_payment_id

    @property
    def checkbox_legal_id(self) -> str:
        return self.__CHECKBOX_LEGAL_ID_REP

    @checkbox_legal_id.setter
    def checkbox_legal_id(self, new_checkbox_legal_id: str) -> None:
        self.__CHECKBOX_LEGAL_ID_REP = new_checkbox_legal_id

    @property
    def username_qry(self):
        return self.__USERNAME_QRY

    @username_qry.setter
    def username_qry(self, new_username_qry) -> None:
        self.__USERNAME_QRY = new_username_qry

    @property
    def first_name_qry(self):
        return self.__FIRST_NAME_QRY

    @first_name_qry.setter
    def first_name_qry(self, new_first_name_qry) -> None:
        self.__FIRST_NAME_QRY = new_first_name_qry

    @property
    def last_name_qry(self):
        return self.__LAST_NAME_QRY

    @last_name_qry.setter
    def last_name_qry(self, new_last_name_qry) -> None:
        self.__LAST_NAME_QRY = new_last_name_qry

    @property
    def email_qry(self):
        return self.__EMAIL_QRY

    @email_qry.setter
    def email_qry(self, new_email_qry) -> None:
        self.__EMAIL_QRY = new_email_qry

    @property
    def password_qry(self):
        return self.__PASSWORD_QRY

    @password_qry.setter
    def password_qry(self, new_password_qry) -> None:
        self.__PASSWORD_QRY = new_password_qry

    @property
    def confirm_password_qry(self):
        return self.__CONFIRM_PASSWORD_QRY

    @confirm_password_qry.setter
    def confirm_password_qry(self, new_confirm_password_qry) -> None:
        self.__CONFIRM_PASSWORD_QRY = new_confirm_password_qry

    @property
    def cellphone_number_qry(self):
        return self.__CELLPHONE_NUMBER_QRY

    @cellphone_number_qry.setter
    def cellphone_number_qry(self, new_cellphone_number_qry) -> None:
        self.__CELLPHONE_NUMBER_QRY = new_cellphone_number_qry

    @property
    def checkbox_legal_qry(self):
        return self.__CHECKBOX_LEGAL_QRY

    @checkbox_legal_qry.setter
    def checkbox_legal_qry(self, new_checkbox_legal_qry) -> None:
        self.__CHECKBOX_LEGAL_QRY = new_checkbox_legal_qry

    @property
    def checkbox_contract_qry(self):
        return self.__CHECKBOX_CONTRACT_QRY

    @checkbox_contract_qry.setter
    def checkbox_contract_qry(self, new_checkbox_contract_qry) -> None:
        self.__CHECKBOX_CONTRACT_QRY = new_checkbox_contract_qry

    @property
    def checkbox_chart_of_payment_qry(self):
        return self.__CHECKBOX_CHART_OF_PAYMENT_QRY

    @checkbox_chart_of_payment_qry.setter
    def checkbox_chart_of_payment_qry(self, new_checkbox_chart_of_payment_qry) -> None:
        self.__CHECKBOX_CHART_OF_PAYMENT_QRY = new_checkbox_chart_of_payment_qry

    @property
    def create_account_btn_label(self) -> str:
        return self.__CREATE_ACCOUNT_BTN_LABEL

    @create_account_btn_label.setter
    def create_account_btn_label(self, new_create_account_btn_label: str) -> None:
        self.__CREATE_ACCOUNT_BTN_LABEL = new_create_account_btn_label

    @property
    def create_account_btn(self):
        return self.__CREATE_ACCOUNT_BTN

    @create_account_btn.setter
    def create_account_btn(self, new_create_account_btn) -> None:
        self.__CREATE_ACCOUNT_BTN = new_create_account_btn

    @property
    def window_current_id(self) -> int:
        return self.__CURR_WINDOW_ID

    @window_current_id.setter
    def window_current_id(self, new_window_current_id: int) -> None:
        self.__CURR_WINDOW_ID = new_window_current_id

    @property
    def error_class_label(self) -> str:
        return self.__ERROR_CLASS_LABEL

    @error_class_label.setter
    def error_class_label(self, new_error_class_label: str) -> None:
        self.__ERROR_CLASS_LABEL = new_error_class_label

    """
        Verify that json contains all constants for TestMainpage 
    """

    def load_constants(self, is_root: bool = True):
        break_loop = False

        while True:
            try:
                self.active = self.jsondump[TEST_CREATION_REP][ACTIVE_REP]
                self.polysafe_create_account_url = \
                    self.jsondump[TEST_CREATION_REP][CONSTANTS_REP][POLYSAFE_CREATE_ACCOUNT_URL_REP]
                self.limit_of_retries = self.jsondump[TEST_CREATION_REP][CONSTANTS_REP][LIMIT_OF_RETRIES_REP]
                self.valid_registration_number_list = \
                    self.jsondump[TEST_CREATION_REP][CONSTANTS_REP][VALID_REGISTRATION_NUMBER_LIST_REP]
                self.invalid_registration_number_list = \
                    self.jsondump[TEST_CREATION_REP][CONSTANTS_REP][INVALID_REGISTRATION_NUMBER_LIST_REP]
                self.valid_name_list = self.jsondump[TEST_CREATION_REP][CONSTANTS_REP][VALID_NAME_LIST_REP]
                self.invalid_name_list = self.jsondump[TEST_CREATION_REP][CONSTANTS_REP][INVALID_NAME_LIST_REP]
                self.valid_email_list = self.jsondump[TEST_CREATION_REP][CONSTANTS_REP][VALID_EMAIL_LIST_REP]
                self.invalid_email_list = self.jsondump[TEST_CREATION_REP][CONSTANTS_REP][INVALID_NAME_LIST_REP]
                self.valid_password_list = self.jsondump[TEST_CREATION_REP][CONSTANTS_REP][VALID_PASSWORD_LIST_REP]
                self.invalid_password_list = \
                    self.jsondump[TEST_CREATION_REP][CONSTANTS_REP][INVALID_PASSWORD_LIST_REP]
                self.valid_cellphone_number_list = \
                    self.jsondump[TEST_CREATION_REP][CONSTANTS_REP][VALID_CELLPHONE_NUMBER_LIST_REP]
                self.invalid_cellphone_number_list = \
                    self.jsondump[TEST_CREATION_REP][CONSTANTS_REP][INVALID_CELLPHONE_NUMBER_LIST_REP]
                self.account_creation_contract = \
                    self.jsondump[TEST_CREATION_REP][CONSTANTS_REP][ACCOUNT_CREATION_CONTRACT_LNK_REP]
                self.chart_of_payment = self.jsondump[TEST_CREATION_REP][CONSTANTS_REP][CHART_OF_PAYMENT_LNK_REP]
                self.legal = self.jsondump[TEST_CREATION_REP][CONSTANTS_REP][LEGAL_LNK_REP]
                self.username_id = self.jsondump[TEST_CREATION_REP][CONSTANTS_REP][USERNAME_ID_REP]
                self.first_name_id = self.jsondump[TEST_CREATION_REP][CONSTANTS_REP][FIRST_NAME_ID_REP]
                self.last_name_id = self.jsondump[TEST_CREATION_REP][CONSTANTS_REP][LAST_NAME_ID_REP]
                self.email_id = self.jsondump[TEST_CREATION_REP][CONSTANTS_REP][EMAIL_ID_REP]
                self.password_id = self.jsondump[TEST_CREATION_REP][CONSTANTS_REP][PASSWORD_ID_REP]
                self.confirm_password_id = self.jsondump[TEST_CREATION_REP][CONSTANTS_REP][CONFIRM_PASSWORD_ID_REP]
                self.cellphone_number_id = self.jsondump[TEST_CREATION_REP][CONSTANTS_REP][CELLPHONE_NUMBER_ID_REP]
                self.checkbox_contract_id = self.jsondump[TEST_CREATION_REP][CONSTANTS_REP][CHECKBOX_CONTRACT_ID_REP]
                self.checkbox_chart_of_payment_id = \
                    self.jsondump[TEST_CREATION_REP][CONSTANTS_REP][CHECKBOX_CHART_OF_PAYMENT_ID_REP]
                self.checkbox_legal_id = self.jsondump[TEST_CREATION_REP][CONSTANTS_REP][CHECKBOX_LEGAL_ID_REP]
                self.create_account_btn_label = \
                    self.jsondump[TEST_CREATION_REP][CONSTANTS_REP][CREATE_ACCOUNT_BTN_LABEL_REP]
                self.error_class_label = self.jsondump[DEV_POWERTOOL_REP][CONSTANTS_REP][ERROR_CLASS_LABEL_REP]
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

    def seek_error_box(self) -> bool:
        if self.driver.find_element_by_class_name("close") is None:  # No error box while loading page
            return False
        return True

    def auto_complete_querries(self, username: bool = True, first_name: bool = True, last_name: bool = True,
                               email: bool = True, password: bool = True, confirm_password: bool = True,
                               cellphone: bool = True, checkbox_contract: bool = True,
                               checkbox_chart_of_payment: bool = True, checkbox_legal: bool = True, ) -> None:
        if username and self.valid_registration_number_list is not None:
            self.username_qry.send_keys(
                self.valid_registration_number_list[ri(0, len(self.valid_registration_number_list) - 1)]
            )

        if first_name and self.valid_name_list is not None:
            self.first_name_qry.clear()
            self.first_name_qry.send_keys(
                self.valid_name_list[ri(0, len(self.valid_name_list) - 1)]
            )

        if last_name and self.valid_name_list is not None:
            self.last_name_qry.clear()
            self.last_name_qry.send_keys(
                self.valid_name_list[ri(0, len(self.valid_name_list) - 1)]
            )

        if email and self.valid_email_list is not None:
            self.email_qry.clear()
            self.email_qry.send_keys(
                self.valid_email_list[ri(0, len(self.valid_email_list) - 1)]
            )

        latest_password = self.valid_password_list[ri(0, len(self.valid_password_list) - 1)]

        if password and self.valid_password_list is not None:
            self.password_qry.clear()
            self.password_qry.send_keys(
                latest_password
            )

        if confirm_password and self.valid_password_list is not None:
            self.confirm_password_qry.clear()
            self.confirm_password_qry.send_keys(
                latest_password
            )

        if cellphone and self.valid_cellphone_number_list is not None:
            self.cellphone_number_qry.clear()
            self.cellphone_number_qry.send_keys(
                self.valid_cellphone_number_list[ri(0, len(self.valid_cellphone_number_list) - 1)]
            )

        if checkbox_contract:
            self.checkbox_contract_qry.clear()
            self.checkbox_contract_qry.click()

        if checkbox_legal:
            self.checkbox_legal_qry.clear()
            self.checkbox_legal_qry.click()

        if checkbox_chart_of_payment:
            self.checkbox_chart_of_payment_qry.clear()
            self.checkbox_chart_of_payment_qry.click()

        print_warning("ACCOUNT_CREATION", "Form submitted, slow down expected...")
        self.create_account_btn.click()

    def close_current_window(self):
        self.driver.close()

        if self.window_current_id > 0:
            self.window_current_id -= 1
            self.driver.switch_to_window(self.driver.window_handles[self.window_current_id])

    def switch_current_window(self):
        self.window_current_id += 1
        self.driver.switch_to_window(self.driver.window_handles[self.window_current_id])

    def test_creation(self):
        # Load constants before actually launching the test
        self.load_constants()

        if self.active:  # Only run if test is activated
            n_failures = 0
            with self.wait_for_page_load(timeout=10):
                while True:
                    try:
                        print_header("MAINPAGE", "Testing account creation button...")
                        print_warning("ACCOUNT_CREATION", "Slow down expected.")
                        self.driver.get(self.polysafe_create_account_url)
                        print_header("ACCOUNT_CREATION", "Verifying links...")
                        print_header("ACCOUNT_CREATION", "Verifying account creation contract...")
                        account_creation_contract_btn = self.driver.find_element_by_partial_link_text(
                            self.account_creation_contract)

                        if account_creation_contract_btn is not None:
                            print_success("ACCOUNT_CREATION", "Found creation contract button link, "
                                                              "verifying if link is dead...")
                            print_warning("ACCOUNT_CREATION", "Slow down expected.")
                            account_creation_contract_btn.click()

                            self.switch_current_window()

                            if self.driver.find_element_by_xpath("//*[contains(text(), ERROR_404]") \
                                    is not None:
                                print_failure("ACCOUNT_CREATION", "Contract button link is invalid.")
                            else:
                                print_success("ACCOUNT_CREATION", "Contract button link is valid!")

                            self.close_current_window()

                        else:
                            print_failure("ACCOUNT_CREATION", "Could not find contract button link.")

                        print_header("ACCOUNT_CREATION", "Redirecting to polysafe create account url...")
                        print_warning("ACCOUNT_CREATION", "Slow down expected.")
                        self.driver.get(self.polysafe_create_account_url)

                        chart_of_payment_btn = self.driver.find_element_by_partial_link_text(self.chart_of_payment)

                        if chart_of_payment_btn is not None:
                            print_success("ACCOUNT_CREATION", "Found chart of payment button link, "
                                                              "verifying if link is dead...")
                            print_warning("ACCOUNT_CREATION", "Slow down expected.")
                            chart_of_payment_btn.click()

                            self.switch_current_window()

                            if self.driver.find_element_by_xpath("//*[contains(text(), ERROR_404)]") \
                                    is not None:
                                print_failure("ACCOUNT_CREATION", "Chart of payment button link is invalid.")
                            else:
                                print_success("ACCOUNT_CREATION", "Chart of payment button link is valid!")

                            self.close_current_window()

                        else:
                            print_failure("ACCOUNT_CREATION", "Could not find chart of payment button link.")

                        print_header("ACCOUNT_CREATION", "Redirecting to polysafe create account url...")
                        print_warning("ACCOUNT_CREATION", "Slow down expected.")
                        self.driver.get(self.polysafe_create_account_url)

                        legal_btn = self.driver.find_element_by_partial_link_text(self.legal)

                        if legal_btn is not None:
                            print_success("ACCOUNT_CREATION", "Found legal button link, "
                                                              "verifying if link is dead...")
                            print_warning("ACCOUNT_CREATION", "Slow down expected.")
                            legal_btn.click()

                            self.switch_current_window()

                            if self.driver.find_element_by_xpath("//*[contains(text(), ERROR_404)]") \
                                    is not None:
                                print_failure("ACCOUNT_CREATION", "Legal button link is invalid.")

                            else:
                                print_success("ACCOUNT_CREATION", "Legal button link is valid!")

                            self.close_current_window()

                        else:
                            print_failure("ACCOUNT_CREATION", "Could not find legal button link.")

                        print_header("ACCOUNT_CREATION", "Redirecting to polysafe create account url...")
                        print_warning("ACCOUNT_CREATION", "Slow down expected.")
                        self.driver.get(self.polysafe_create_account_url)

                        print_header("ACCOUNT_CREATION", "Loading querries for testing...")
                        self.username_qry = self.driver.find_element_by_id(self.username_id)
                        self.first_name_qry = self.driver.find_element_by_id(self.first_name_id)
                        self.last_name_qry = self.driver.find_element_by_id(self.last_name_id)
                        self.email_qry = self.driver.find_element_by_id(self.email_id)
                        self.password_qry = self.driver.find_element_by_id(self.password_id)
                        self.confirm_password_qry = self.driver.find_element_by_id(self.confirm_password_id)
                        self.cellphone_number_qry = self.driver.find_element_by_id(self.cellphone_number_id)
                        self.checkbox_contract_qry = self.driver.find_element_by_id(self.checkbox_contract_id)
                        self.checkbox_legal_qry = self.driver.find_element_by_id(self.checkbox_legal_id)
                        self.checkbox_chart_of_payment_qry = self.driver.find_element_by_id(
                            self.checkbox_chart_of_payment_id)
                        self.create_account_btn = self.driver.find_element_by_id(self.create_account_btn_label)

                        if self.username_qry is not None and self.first_name_qry is not None \
                                and self.last_name_qry is not None \
                                and self.email_qry is not None and self.password_qry is not None \
                                and self.confirm_password_qry is not None and self.cellphone_number_qry is not None \
                                and self.checkbox_contract_qry is not None and self.checkbox_legal_qry is not None \
                                and self.checkbox_chart_of_payment_qry is not None \
                                and self.create_account_btn is not None:
                            print_success("ACCOUNT_CREATION", "Found all querries!")
                        else:
                            print_failure("ACCOUNT_CREATION", "Failed to load one or more querries!")

                        count = 0
                        for invalid_registration_number in self.invalid_registration_number_list:
                            print_header("ACCOUNT_CREATION", "Sending invalid registration numbers (" + str(count)
                                         + ")...")
                            self.username_qry.clear()
                            self.username_qry.send_keys(invalid_registration_number)
                            self.auto_complete_querries(username=False)
                            if self.seek_error_box():
                                print_success("ACCOUNT_CREATION", "Invalid registration numbers (" + str(count) +
                                              ") passed!")
                            else:
                                print_failure("ACCOUNT_CREATION", "Invalid registration numbers (" + str(count) +
                                              ") failed!")
                                self.driver.get(self.polysafe_create_account_url)
                            count += 1

                        count = 0
                        for invalid_name in self.invalid_name_list:
                            print_header("ACCOUNT_CREATION", "Sending invalid first name (" + str(count)
                                         + ")...")
                            self.first_name_qry.clear()
                            self.first_name_qry.send_keys(invalid_name)
                            self.auto_complete_querries(first_name=False)
                            if self.seek_error_box():
                                print_success("ACCOUNT_CREATION", "Invalid first name (" + str(count) +
                                              ") passed!")
                            else:
                                print_failure("ACCOUNT_CREATION", "Invalid first name (" + str(count) +
                                              ") failed!")
                                self.driver.get(self.polysafe_create_account_url)
                            count += 1

                        count = 0
                        for invalid_name in self.invalid_name_list:
                            print_header("ACCOUNT_CREATION", "Sending invalid last name (" + str(count)
                                         + ")...")
                            self.last_name_qry.clear()
                            self.last_name_qry.send_keys(invalid_name)
                            self.auto_complete_querries(last_name=False)
                            if self.seek_error_box():
                                print_success("ACCOUNT_CREATION", "Invalid last name (" + str(count) +
                                              ") passed!")
                            else:
                                print_failure("ACCOUNT_CREATION", "Invalid last name (" + str(count) +
                                              ") failed!")
                                self.driver.get(self.polysafe_create_account_url)
                            count += 1

                        count = 0
                        for invalid_password in self.invalid_password_list:
                            print_header("ACCOUNT_CREATION", "Sending invalid password (" + str(count)
                                         + ")...")
                            self.password_qry.clear()
                            self.password_qry.send_keys(invalid_password)
                            self.auto_complete_querries(password=False)
                            if self.seek_error_box():
                                print_success("ACCOUNT_CREATION", "Invalid password (" + str(count) +
                                              ") passed!")
                            else:
                                print_failure("ACCOUNT_CREATION", "Invalid password (" + str(count) +
                                              ") failed!")
                                self.driver.get(self.polysafe_create_account_url)
                            count += 1

                        count = 0
                        for invalid_password in self.invalid_password_list:
                            print_header("ACCOUNT_CREATION", "Sending invalid confirm password (" + str(count)
                                         + ")...")
                            self.confirm_password_qry.clear()
                            self.confirm_password_qry.send_keys(invalid_password)
                            self.auto_complete_querries(confirm_password=False)
                            if self.seek_error_box():
                                print_success("ACCOUNT_CREATION", "Invalid confirm password (" + str(count) +
                                              ") passed!")
                            else:
                                print_failure("ACCOUNT_CREATION", "Invalid confirm password (" + str(count) +
                                              ") failed!")
                                self.driver.get(self.polysafe_create_account_url)
                            count += 1

                        count = 0
                        for invalid_cellphone_number in self.invalid_cellphone_number_list:
                            print_header("ACCOUNT_CREATION", "Sending invalid cellphone number (" + str(count)
                                         + ")...")
                            self.cellphone_number_qry.clear()
                            self.cellphone_number_qry.send_keys(invalid_cellphone_number)
                            self.auto_complete_querries(cellphone=False)
                            if self.seek_error_box():
                                print_success("ACCOUNT_CREATION", "Invalid cellphone number (" + str(count) +
                                              ") passed!")
                            else:
                                print_failure("ACCOUNT_CREATION", "Invalid cellphone number (" + str(count) +
                                              ") failed!")
                                self.driver.get(self.polysafe_create_account_url)
                            count += 1

                        print_header("ACCOUNT_CREATION", "Sending valid querries but invalid checkbox acceptations...")
                        print_header("ACCOUNT_CREATION", "Pass #1: not checking contract checkbox...")
                        self.auto_complete_querries(checkbox_contract=False)
                        if self.seek_error_box():
                            print_success("ACCOUNT_CREATION", "Unchecked contract checkbox passed!")
                        else:
                            print_failure("ACCOUNT_CREATION", "Unchecked contract checkbox failed!")
                            self.driver.get(self.polysafe_create_account_url)

                        print_header("ACCOUNT_CREATION", "Pass #2: not checking chart of payment checkbox...")
                        self.auto_complete_querries(checkbox_chart_of_payment=False)
                        if self.seek_error_box():
                            print_success("ACCOUNT_CREATION", "Unchecked chart of payment checkbox passed!")
                        else:
                            print_failure("ACCOUNT_CREATION", "Unchecked chart of payment checkbox failed!")
                            self.driver.get(self.polysafe_create_account_url)

                        print_header("ACCOUNT_CREATION", "Pass #3: not checking legal checkbox...")
                        self.auto_complete_querries(checkbox_legal=False)
                        if self.seek_error_box():
                            print_success("ACCOUNT_CREATION", "Unchecked legal checkbox passed!")
                        else:
                            print_failure("ACCOUNT_CREATION", "Unchecked legal checkbox failed!")
                            self.driver.get(self.polysafe_create_account_url)

                        print_success("ACCOUNT_CREATION", "All tests passed!")

                    except Exception:
                        n_failures += 1  # Increments number of failures
                        exc_type, value, traceback = sys.exc_info()
                        print_failure(
                            "TEST_CONNECTION", "Test failed with exception [" + exc_type.__name__ + "]")

                    # Breaking if code has no exception or reaches the limit of retries
                    if n_failures == 0 or n_failures >= self.limit_of_retries:
                        break
