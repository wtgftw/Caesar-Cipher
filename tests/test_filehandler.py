import json
import pytest
from unittest import mock
from src.filehandler import FileHandler
from src.text import Text


def test_read_file_should_return_objects_from_json_file():
    json_filename = "test_json_data.json"
    test_json_data = [
        {"text": "lorem ipsum", "rot_type": 15, "status": "decrypted"},
        {"text": "fndnso aosidju", "rot_type": 21, "status": "encrypted"}
    ]
    mock_json_file = json.dumps(test_json_data)

    file_handler = FileHandler()

    with mock.patch('builtins.input', return_value=json_filename):
        with mock.patch('builtins.open', mock.mock_open(read_data=mock_json_file)):
            with mock.patch('os.path.isfile', return_value=True):
                result = file_handler.read_file()


    assert len(result) == 2
    assert isinstance(result[0], Text)
    assert isinstance(result[1], Text)
    assert result[0].text == 'lorem ipsum'
    assert result[0].rot_type == 15
    assert result[0].status == 'decrypted'
    assert result[1].text == 'fndnso aosidju'
    assert result[1].rot_type == 21
    assert result[1].status == 'encrypted'


def test_read_file_should_raise_error_when_problem_with_file_import_occurs():
    file_handler = FileHandler()

    with pytest.raises(Exception):
        file_handler.read_file() 


def test_write_file_should_create_new_file_when_it_was_not_created():
    file_handler = FileHandler()

    test_data = [
        Text(text="lorem ipsum", rot_type=15, status="encrypted"),
        Text(text="test string", rot_type=21, status="decrypted")
    ]

    filepath = "new_json_file.json"

    with mock.patch('builtins.input', return_value=filepath):
        with mock.patch('os.path.isfile', return_value=False):
            with mock.patch('builtins.open', mock.mock_open()) as mock_file:
                file_handler.write_file(data=test_data)


    mock_file.assert_called_once_with(filepath, 'w', encoding='utf-8')


def test_write_file_should_append_file_when_already_created_and_user_confirms():
    file_handler = FileHandler()

    test_data = [
        Text(text="lorem ipsum", rot_type=15, status="encrypted"),
        Text(text="test string", rot_type=21, status="decrypted")
    ]
    existing_data = [{"text": "dwa bułki", "rot_type": 22, "status": "decrypted"}]

    filepath = "existing_json_fille.json"

    with mock.patch('builtins.input', side_effect=[filepath, "y"]):
        with mock.patch('os.path.isfile', return_value=True):
            with mock.patch('builtins.open', mock.mock_open(read_data=json.dumps(existing_data))) as mock_file:
                file_handler.write_file(test_data)
    
    mock_file.assert_called_with(filepath, 'a', encoding='utf-8'
                                      )