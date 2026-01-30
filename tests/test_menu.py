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


def test_get_user_choice_should_raise_ValueError_when_not_in_options_range():
    menu = Menu()

    with mock.patch('builtins.input',return_value="12"):
        with pytest.raises(ValueError):
            menu.get_user_choice(11)


def test_get_user_choice_should_return_choice_int_when_menu_option_has_been_selected():
    menu = Menu()

    with mock.patch('builtins.input', return_value="5"):
        result = menu.get_user_choice(11)

    assert result == 5


def test_ask_text_source_should_return_choice_int_when_source_has_been_selected():
    menu = Menu()

    with mock.patch('builtins.input', return_value=2):
        result = menu.ask_text_source()

    assert result == 2