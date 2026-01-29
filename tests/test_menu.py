import pytest
from unittest import mock
from src.menu import Menu


def test_start_should_print_welcome_message_and_call_main_menu():
    menu = Menu()

    with mock.patch('builtins.print') as mocked_print:
        with mock.patch('src.menu.Menu.main_menu') as mocked_main_menu:
            menu.start()

    assert mocked_print.mock_has_any_call("Welcome in Caesar Cipher encryptor")
    mocked_main_menu.assert_called_once()


def test_main_menu_should_print_11_menu_options():
    menu = Menu()

    with mock.patch('builtins.print') as mocked_print:
        menu.main_menu()

    
    assert mocked_print.mock_has_calls(menu.menu_options)


def test_get_user_choice_should_raise_ValueError_when():
    pass