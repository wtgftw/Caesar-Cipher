import pytest
from unittest import mock
from src.menu import Menu


def test_start_should_print_welcome_message_and_call_main_menu():
    menu = Menu()

    with mock.patch('builtins.print') as mocked_print:
        menu.start()

    assert mocked_print.mock_has_any_call("Welcome in Caesar Cipher encryptor")

