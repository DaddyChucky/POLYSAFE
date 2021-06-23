"""
    Polysafe - User testing.
    Description:    Colored printing depending on message severity.
    File name:      bg_txt_color.py
    Author:         Charles De Lafontaine
    Last edition:   06/22/2021
"""


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


def print_header(category: str, text_to_print: str) -> None:
    print(
        BgTxtColor.HEADER + BgTxtColor.BOLD + "[" + category + "] > " + BgTxtColor.ENDC + BgTxtColor.OKBLUE +
        text_to_print + BgTxtColor.ENDC)


def print_success(category: str, text_to_print: str) -> None:
    print(
        BgTxtColor.HEADER + BgTxtColor.BOLD + "[" + category + "] > " + BgTxtColor.ENDC + BgTxtColor.OKGREEN +
        text_to_print + " ✓ " + BgTxtColor.ENDC)


def print_warning(category: str, text_to_print: str) -> None:
    print(
        BgTxtColor.HEADER + BgTxtColor.BOLD + "[" + category + "] > " + BgTxtColor.ENDC + BgTxtColor.WARNING +
        text_to_print + " ⚠ " + BgTxtColor.ENDC)


def print_failure(category: str, text_to_print: str) -> None:
    print(
        BgTxtColor.HEADER + BgTxtColor.BOLD + "[" + category + "] > " + BgTxtColor.ENDC + BgTxtColor.FAIL +
        text_to_print + " ✗ " + BgTxtColor.ENDC)
