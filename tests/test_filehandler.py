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
    

def test_should_raise_error_when_no_json_extension_provided_to_filepath():
    file_handler = FileHandler()

    test_data = [
        Text(text="lorem ipsum", rot_type=15, status="encrypted")
    ]

    filepath = "not_json_file.txt"
    
    with mock.patch('builtins.input', return_value=filepath):
        with pytest.raises(Exception):
            file_handler.write_file(test_data)


def test_should_raise_error_when_buffer_is_empty():
    file_handler = FileHandler()
    filepath = "data.json"
    test_data = []

    with mock.patch('builtins.input', return_value=filepath):
        with pytest.raises(Exception):
            file_handler.write_file(test_data)


def test_get_file_path_should_return_input_value():
    file_handler = FileHandler()

    with mock.patch('builtins.input', return_value="json_file.json"):
        assert file_handler._get_file_path() == "json_file.json"


def test_validate_file_exists_should_raise_FileNotFound_error_when_file_not_exists():
    file_handler = FileHandler() 
    
    with pytest.raises(FileNotFoundError):
        file_handler._validate_file_exists("test.json")


def test_validate_json_extension_should_raise_ValueError_when_no_json_extension_provided():
    file_handler = FileHandler()

    with pytest.raises(ValueError, match="JSON file extension only supported."):
        file_handler._validate_json_extension("data.txt")


def test_validate_buffer_not_empty_should_raise_ValueError_when_buffer_list_is_empty():
    file_handler = FileHandler()

    with pytest.raises(ValueError, match="Buffer was empty."):
        file_handler._validate_buffer_not_empty([])


def test_ask_for_overwrite_should_return_true_or_false_depending_on_user_choice():
    file_handler = FileHandler()

    with mock.patch('builtins.input', return_value="y"):
        assert file_handler._ask_for_overwrite() == True

    with mock.patch('builtins.input', return_value="n"):
        assert file_handler._ask_for_overwrite() != True


def test_conver_to_dict_list_should_return_list_with_dict_objects_inside():
    file_handler = FileHandler()

    test_data = [
        Text(text="lorem ipsum", rot_type=15, status="encrypted"),
        Text(text="test string", rot_type=21, status="decrypted")
    ]

    result = file_handler._convert_to_dict_list(test_data)

    assert type(result[0]) == dict
    assert type(result[1]) == dict


def test_append_to_existing_file_should_extend_current_data_with_new_values():
    file_hanlder = FileHandler()

    test_data = [
        {"text": "lorem ipsum", "rot_type": 22, "status": "decrypted"},
        {"text": "asdd asdd", "rot_type": 22, "status": "decrypted"}
    ]
    existing_data = [{"text": "dwa bułki", "rot_type": 22, "status": "decrypted"}]

    filepath = "test_json_file.json"

    with mock.patch('builtins.open', mock.mock_open(read_data=json.dumps(existing_data))):
        with mock.patch('src.filehandler.json.dump') as mock_dump:
            file_hanlder._append_to_existing_file(filepath=filepath,new_data=test_data)

    expected_combined_data = existing_data + test_data

    mock_dump.assert_called_once()

    actual_data = mock_dump.call_args[0][0]

    assert actual_data == expected_combined_data
    assert len(actual_data) == 3


