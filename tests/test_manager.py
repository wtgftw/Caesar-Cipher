import pytest
from unittest import mock
from src.manager import Manager
from src.text import Text

@pytest.fixture
def get_mocked_manager():
    mock_menu = mock.Mock()
    mock_file_handler = mock.Mock()
    mock_buffer = mock.Mock()
    mock_rot = mock.Mock()

    manager = Manager (
        menu=mock_menu,
        file_handler=mock_file_handler,
        buffer=mock_buffer,
        rot=mock_rot
    )

    return manager


def test_get_buffer_text_by_status_should_raise_ValueError_when_buffer_is_empty(get_mocked_manager):
    get_mocked_manager._buffer.memory = []

    with pytest.raises(ValueError, match="Buffer is empty..."):
        get_mocked_manager._get_buffer_text_by_status("test")


def test_get_buffer_text_by_status_should_raise_ValueError_when_status_name_is_wrong(get_mocked_manager):
    get_mocked_manager._menu.get_user_choice.return_value = 1
    get_mocked_manager._buffer.memory = [
        Text(text="test", rot_type=14, status="wrong_status")
    ]

    required_status = "encrypted"
    required_status1 = "decrypted"
    with pytest.raises(ValueError, match=f"Selected text must be {required_status}"):
        get_mocked_manager._get_buffer_text_by_status(required_status)

    with pytest.raises(ValueError, match=f"Selected text must be {required_status1}"):
        get_mocked_manager._get_buffer_text_by_status(required_status1)


def test_get_buffer_text_by_status_should_return_text_string_from_text_object(get_mocked_manager):
    
    get_mocked_manager._menu.get_user_choice.return_value = 1
    get_mocked_manager._buffer.memory = [
        Text(text="test", rot_type=14, status="encrypted")
    ]

    result = get_mocked_manager._get_buffer_text_by_status("encrypted")

    assert result == "test"


def test_handle_encrypt_should_add_encrypted_text_to_buffer(get_mocked_manager):
   
    get_mocked_manager._menu.ask_text_source.return_value = 1
    get_mocked_manager._rot.encrypt.return_value = "lorem ipsum"
    
    with mock.patch('builtins.input', return_value="lorem ipsum"):
        get_mocked_manager._handle_encrypt(12)


    get_mocked_manager._buffer.add.assert_called_once()
    added_text = get_mocked_manager._buffer.add.call_args[0][0]
    assert added_text.text == "lorem ipsum"
    assert added_text.rot_type == 12
    assert added_text.status == "encrypted"


def test_handle_encrypt_should_use_decrypted_text_from_buffer_to_encrypt_it(get_mocked_manager):
    get_mocked_manager._menu.ask_text_source.return_value = 2
    get_mocked_manager._buffer.memory = [Text(text="from buffer", rot_type=13, status="decrypted")]
    get_mocked_manager._rot.encrypt.return_value = "encrypted_result"
    get_mocked_manager._menu.get_user_choice.return_value = 1

    get_mocked_manager._handle_encrypt(13)
    get_mocked_manager._rot.encrypt.assert_called_once_with(enc_type=13, text_str="from buffer")


def test_handle_decrypt_should_add_encrypted_text_to_buffer(get_mocked_manager):
    get_mocked_manager._menu.ask_text_source.return_value = 1
    get_mocked_manager._rot.decrypt.return_value = "test string"

    with mock.patch('builtins.input', return_value="test string"):
        get_mocked_manager._handle_decrypt(3)


    get_mocked_manager._buffer.add.assert_called_once()
    added_text = get_mocked_manager._buffer.add.call_args[0][0]

    assert added_text.text == "test string"
    assert added_text.rot_type == 3
    assert added_text.status == "decrypted"


def test_get_custom_shift_should_return_int_number_provided_by_user(get_mocked_manager):

    with mock.patch('builtins.input', return_value="12"):
        assert get_mocked_manager._get_custom_shift() == 12 


def test_run_should_call_menu_and_exit_when_11_provided(get_mocked_manager):
    get_mocked_manager._menu.get_user_choice.return_value = 11
    
    get_mocked_manager.run()
    get_mocked_manager._menu.start.assert_called_once()


def test_run_case_7_should_call_buffer_display_last(get_mocked_manager):
    get_mocked_manager._buffer.memory = [Text(text="from buffer", rot_type=13, status="decrypted")]
    get_mocked_manager._menu.get_user_choice.side_effect = [7,11]

    get_mocked_manager.run()
    get_mocked_manager._buffer.display_last.assert_called_once()


def test_run_case_9_should_load_text_objects_from_json_file_and_extend_buffer(get_mocked_manager):
    get_mocked_manager._menu.get_user_choice.side_effect = [9,11]
    get_mocked_manager._file_handler.read_file.return_value = [Text(text="loaded", rot_type=13, status="decrypted")]

    get_mocked_manager.run()
    get_mocked_manager._file_handler.read_file.assert_called_once()
    get_mocked_manager._buffer.extend.assert_called_once()


def test_run_case_10_should_write_buffer_to_file(get_mocked_manager):
    get_mocked_manager._menu.get_user_choice.side_effect = [10, 11]
    get_mocked_manager._buffer.memory = [Text(text="from buffer", rot_type=13, status="decrypted")]

    get_mocked_manager.run()
    get_mocked_manager._file_handler.write_file.assert_called_once_with(data=get_mocked_manager._buffer.memory)
    
    