"""
    Polysafe - User testing.
    Description:    JsonFile class definition.
    File name:      jsonfile.py
    Author:         Charles De Lafontaine
    Last edition:   06/22/2021
"""

from constants import *
from bg_txt_color import *

import json
import os


class JsonFile:
    def __init__(self,
                 file_name="\\tests_data.json",
                 file_mode_create='w',
                 file_mode_read='r',
                 file_encoding='utf-8',
                 file_ensure_ascii=False,
                 file_sort_keys=True,
                 file_indent=4):
        self.__FILE_NAME = file_name
        self.__FILE_MODE_CREATE = file_mode_create
        self.__FILE_MODE_READ = file_mode_read
        self.__FILE_ENCODING = file_encoding
        self.__FILE_ENSURE_ASCII = file_ensure_ascii
        self.__FILE_SORT_KEYS = file_sort_keys
        self.__FILE_INDENT = file_indent
        self.__PWD_OVERRIDE_CHANGED = ["yes", "y", "oui", "o"]
        self.__PWD_OVERRIDE_UNCHANGED = ["no", "n", "non"]
        self.__OS = os
        self.__DEFAULT_DATA = {
            DEV_POWERTOOL_REP:
                {
                    DEV_CREDENTIALS_REP: 
                        {
                            EMAIL_REP: "charles.delafontaine@gmail.com",
                            PASSWORD_REP: "Charles1"
                        }
                },
            TEST_MAINPAGE_REP:
                {
                    ACTIVE_REP: True,
                    CHECK_URLS_REP: True,
                    CHECK_LOGIN_CREDENTIALS_REP: True,
                    SEND_FAKE_LOGIN_CREDENTIALS_REP: True,
                    CHECK_ERROR_GENERATION_REP: True,
                    CONSTANTS_REP: 
                        {
                            POLYSAFE_MAINPAGE_URL_REP: "http://localhost/polysafe_code/erp/index.php",
                            CONNECTION_TEXT_REP: "Connexion »",
                            LIMIT_OF_RETRIES_REP: 0,
                            EXPECTED_CONNECTION_URL_REP: "http://localhost/polysafe_code/erp/users/login.php",
                            EMAIL_ID_REP: "username",
                            PASSWORD_ID_REP: "password",
                            CONNECTION_BTN_ID_REP: "next_button",
                            INVALID_EMAIL_REP: "invalid.email@gmail.ca",
                            INVALID_PASSWORD_REP: "password1234",
                            CLOSE_BUTTON_REP: "close",
                            FORGOT_BUTTON_LINK_REP: "Mot de passe oub",
                            CREATE_ACCOUNT_LINK_REP: "Créer un compte",
                            ABOUT_LINK_REP: "propos",
                            SUPPORT_LINK_REP: "Support"
                        }
                },
            TEST_CREATION_REP:
                {
                    ACTIVE_REP: True,
                    CONSTANTS_REP:
                        {
                            LIMIT_OF_RETRIES_REP: 0,
                            VALID_REGISTRATION_NUMBER_LIST_REP: ["1823192", "2076522", "8904739"],
                            INVALID_REGISTRATION_NUMBER_LIST_REP: ["519859015819058", "", "9FAFX", "2*60259"],
                            VALID_NAME_LIST_REP: ["Vincent", "Timothé", "Gertrude"],
                            INVALID_NAME_LIST_REP: [" ", "Charles11", "", "IncroYABLE!"],
                            VALID_EMAIL_LIST_REP: ["poly.mtl@hotmail.ca", "polymtl.del@gmail.com",
                                                   "charbel-gendron@polymtl.ca"],
                            INVALID_EMAIL_LIST_REP: ["f@domaineinvalide.com", " ", "", "???@polymtl.ca"],
                            VALID_PASSWORD_LIST_REP: ["aaaaaa", "*!@*%$#(", "Charles123"],
                            INVALID_PASSWORD_LIST_REP: ["af214", "***   *",
                                                        "motdepassebeaucouptroplongmotdepassebeaucouptroplongmotdepassebeaucouptroplongmotdepassebeaucouptroplongmotdepassebeaucouptroplongmotdepassebeaucouptroplongmotdepassebeaucouptroplongmotdepassebeaucouptroplongmotdepassebeaucouptroplongmotdepassebeaucouptroplong"],
                            VALID_CELLPHONE_NUMBER_LIST_REP: ["1234567890", "8195551010", "5144440101"],
                            INVALID_CELLPHONE_NUMBER_LIST_REP: ["18008001010", "8!97770909", "abcdefghgh", "", " "],
                            ACCOUNT_CREATION_CONTRACT_LNK_REP: "https://polysafe.polymtl.ca/uploads/static/documents/contrat_adhesion.pdf",
                            CHART_OF_PAYMENT_LNK_REP: "https://polysafe.polymtl.ca/uploads/static/documents/contrat_paiement.pdf",
                            LEGAL_LNK_REP: "https://polysafe.polymtl.ca/uploads/static/documents/mention_legale.pdf",
                            POLYSAFE_CREATE_ACCOUNT_URL_REP: "http://localhost/polysafe_code/erp/users/join.php"
                        }
                }
        }

    @property
    def file_name(self) -> str:
        return self.__FILE_NAME

    @property
    def file_mode_create(self) -> str:
        return self.__FILE_MODE_CREATE

    @property
    def file_mode_read(self) -> str:
        return self.__FILE_MODE_READ

    @property
    def file_encoding(self) -> str:
        return self.__FILE_ENCODING

    @property
    def file_ensure_ascii(self) -> bool:
        return self.__FILE_ENSURE_ASCII

    @property
    def file_sort_keys(self) -> bool:
        return self.__FILE_SORT_KEYS

    @property
    def file_indent(self) -> int:
        return self.__FILE_INDENT

    @property
    def pwd_override_changed(self) -> list[str]:
        return self.__PWD_OVERRIDE_CHANGED

    @property
    def pwd_override_unchanged(self) -> list[str]:
        return self.__PWD_OVERRIDE_UNCHANGED

    @property
    def default_data(self) -> dict:
        return self.__DEFAULT_DATA

    @property
    def os(self):
        return self.__OS

    """
        Creates fresh copy of json file.
    """

    def create(self):
        print_header("JSON_CREATION", "Starting JSON file creation...")

        print_warning("JSON_CREATION",
                      "Current working directory: " + self.os.getcwd() + "\nWould you like to change it? (y/n)")
        pwd_override = input()

        while True:
            if pwd_override not in self.pwd_override_changed and pwd_override not in self.pwd_override_unchanged:
                print_failure("JSON_CREATION", "Invalid command <" +
                              pwd_override + ">, please try again:")
                pwd_override = input()

            elif pwd_override in self.pwd_override_changed:
                break_loop = False

                while True:
                    new_os_curr_dir = None

                    try:
                        print_header(
                            "JSON_CREATION", "Please enter the new current working directory full path:")
                        new_os_curr_dir = input()
                        self.os.chdir(new_os_curr_dir)
                        break_loop = True

                    except FileNotFoundError or OSError:
                        print_failure("JSON_CREATION",
                                      "New directory <" + new_os_curr_dir + "> cannot be found. Please try again.")

                    if break_loop:
                        break
                break

            else:
                break

        with open(self.os.getcwd() + self.file_name, self.file_mode_create, encoding=self.file_encoding) as f:
            json.dump(self.default_data, f, ensure_ascii=self.file_ensure_ascii, sort_keys=self.file_sort_keys,
                      indent=self.file_indent)

        print_header("JSON_CREATION", "Dumped " + str(self.os.path.getsize(
            self.os.getcwd() + self.file_name)) + " bytes into " + self.os.getcwd() + self.file_name)

        # Minor bug here, does not read correctly *to fix*
        exit(-1)

    def json_read_failure(self, json_file) -> str:
        print_failure("JSON_READ",
                      "Cannot read <" + self.os.getcwd() + self.file_name +
                      "> Perhaps the file is corrupted or simply inexistant?")
        print_header("JSON_READ_RETRY",
                     "Would you like to load a fresh copy of your json? (y/n)")
        json_retry_input = input()

        while json_retry_input not in self.pwd_override_changed and json_retry_input not in self.pwd_override_unchanged:
            print_failure("JSON_READ_RETRY", "Invalid command <" +
                          json_retry_input + ">, please try again:")
            json_retry_input = input()

        # User wants fresh copy
        if json_retry_input in self.pwd_override_changed:
            print_header(
                "JSON_READ_RETRY", "Trying to override the copy of your json with a fresh one...")
            self.create()
            print_header("JSON_READ_RETRY",
                         "Retrying to load data from fresh json copy...")

            try:
                with open(self.os.getcwd() + self.file_name, self.file_mode_read, encoding=self.file_encoding):
                    data = json.load(json_file)
                    print_success("JSON_READ", "Successfully read <" +
                                  self.os.getcwd() + self.file_name + ">!")

            except ValueError:
                json_file.close()  # Performance purposes while handling exception
                print_failure("JSON_READ_RETRY",
                              "Fatal error while reading fresh json copy. I might not have the permission to do that.")

        # User wants to load copy
        else:
            break_loop = False

            while True:
                own_json_path = None
                try:
                    print_header(
                        "JSON_READ_RETRY", "Please enter the directory where your .json lays:")
                    own_json_path = input()
                    self.os.chdir(own_json_path)
                    break_loop = True

                except FileNotFoundError or OSError:
                    print_failure("JSON_READ_RETRY",
                                  "New directory <" + own_json_path + "> cannot be found. Please try again.")

                if break_loop:
                    break

            print_header("JSON_READ_RETRY",
                         "Retrying to load data from fresh json copy...")

            try:
                with open(self.os.getcwd() + self.file_name, self.file_mode_read,
                          encoding=self.file_encoding) as json_file:
                    data = json.load(json_file)
                    print_success("JSON_READ", "Successfully read <" +
                                  self.os.getcwd() + self.file_name + ">!")

            except ValueError:
                json_file.close()  # Performance purposes while handling exception
                print_failure("JSON_READ_RETRY",
                              "Fatal error while reading fresh json copy. I might not have the permission to do that.")

        return data

    """
        Reads the json file and outputs it to a dict.
    """

    def read(self) -> dict:
        try:
            print_header("JSON_READ", "Trying  to read <" +
                         self.os.getcwd() + self.file_name + ">")

            with open(self.os.getcwd() + self.file_name, self.file_mode_read, encoding=self.file_encoding) as json_file:
                # Trying to load data into variable
                try:
                    data = json.load(json_file)

                # If it fails for whatever reason, retry with fresh user file
                except ValueError:
                    json_file.close()  # Performance purposes while handling exception
                    data = self.json_read_failure(json_file)

                return data

        except FileNotFoundError:
            print_failure("JSON_READ", "Cannot open file <" +
                          self.os.getcwd() + self.file_name + ">")
