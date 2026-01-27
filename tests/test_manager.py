import pytest
from unittest import mock
from src.manager import Manager
from src.text import Text

def test_get_buffer_text_by_status_should_raise_ValueError_when_buffer_is_empty():
    mock_menu = mock.Mock()
    mock_file_handler = mock.Mock()
    mock_buffer = mock.Mock()
    mock_buffer.memory = []
    mock_rot = mock.Mock()


    manager = Manager (
        menu=mock_menu,
        file_handler=mock_file_handler,
        buffer=mock_buffer,
        rot=mock_rot
    )


    with pytest.raises(ValueError, match="Buffer is empty..."):
        manager._get_buffer_text_by_status("test")


def test_get_buffer_text_by_status_should_raise_ValueError_when_status_name_is_wrong():
    mock_menu = mock.Mock()
    mock_menu.get_user_choice.return_value = 1
    mock_file_handler = mock.Mock()
    mock_buffer = mock.Mock()
    mock_buffer.memory = [
        Text(text="test", rot_type=14, status="wrong_status")
    ]
    mock_rot = mock.Mock()

    manager = Manager(
        menu = mock_menu,
        file_handler=mock_file_handler,
        buffer=mock_buffer,
        rot=mock_rot
    )

    required_status = "encrypted"
    required_status1 = "decrypted"
    with pytest.raises(ValueError, match=f"Selected text must be {required_status}"):
        manager._get_buffer_text_by_status(required_status)

    with pytest.raises(ValueError, match=f"Selected text must be {required_status1}"):
        manager._get_buffer_text_by_status(required_status1)


def test_get_buffer_text_by_status_should_return_text_string_from_text_object():
    mock_menu = mock.Mock()
    mock_menu.get_user_choice.return_value = 1
    mock_file_handler = mock.Mock()
    mock_buffer = mock.Mock()
    mock_buffer.memory = [
        Text(text="test", rot_type=14, status="encrypted")
    ]
    mock_rot = mock.Mock()
 

    manager = Manager(
        menu = mock_menu,
        file_handler=mock_file_handler,
        buffer=mock_buffer,
        rot=mock_rot
    )

    result = manager._get_buffer_text_by_status("encrypted")

    assert result == "test"


def test_handle_encrypt_should_add_encrypted_text_to_buffer():
    mock_menu = mock.Mock()
    mock_menu.ask_text_source.return_value = 1
    mock_file_handler = mock.Mock()
    mock_buffer = mock.Mock()
    mock_rot = mock.Mock()
    mock_rot.encrypt.return_value = "lorem ipsum"
    
    manager = Manager(
        menu = mock_menu,
        file_handler=mock_file_handler,
        buffer=mock_buffer,
        rot=mock_rot
    )

    with mock.patch('builtins.input', return_value="lorem ipusm"):
        with mock.patch('src.text'):
            manager._handle_encrypt(12)

    mock_buffer.add_assert_called_once_with(enc_type=12, text_str="lorem_ipsum")
    added_text = mock_buffer.add.call_args[0][0]
    assert added_text.text == "lorem ipsum"
    assert added_text.rot_type == 12
    assert added_text.status == "encrypted"