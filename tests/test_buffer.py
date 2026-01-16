from unittest import mock
from buffer import Buffer
from text import Text


def test_should_make_buffer_class_instance_with_empty_memory_list():
    buffer = Buffer()

    assert isinstance(buffer, Buffer)
    assert buffer.memory == []


def test_add_should_append_text_class_to_buffer_memory_list():
    buffer = Buffer()

    text_obj = Text("test string", 13, "encrypted")
    buffer.add(text_obj)

    assert len(buffer.memory) == 1
    assert buffer.memory[0] == text_obj


def test_extend_should_extend_buffer_memory_with_values_from_list():
    buffer = Buffer()

    buffer.memory = [Text("test_string1", 13, "encrypted")]

    extension_list = [Text("test_string2", 15, "decrypted"),Text("test_string3", 24, "encrypted")]

    buffer.extend(extension_list)

    assert len(buffer.memory) == 3


def test_display_buffer_should_print_bufer_empty_info_then_return_when_buffer_is_empty():
    buffer = Buffer()

    with mock.patch('builtins.print') as mocked_print:
        buffer.display_buffer()

        assert mocked_print.mock_calls == [mock.call("Buffer is empty...")]


def test_display_buffer_should_print_object_properties_with_index():
    buffer = Buffer()

    buffer.memory = [Text(text="test_string1", rot_type=15, status="decrypted"),Text(text="test_string3", rot_type=24, status="encrypted")]
    with mock.patch('builtins.print') as mocked_print:
        buffer.display_buffer()

        assert mocked_print.call_count == 2
        mocked_print.assert_called_with('2. test_string3 - encrypted')


def test_display_last_should_print_buffer_is_empty_info_when_no_objects_were_added():
    buffer = Buffer()
    buffer.memory = [Text(text="test_string1", rot_type=15, status="decrypted"),Text(text="test_string3", rot_type=24, status="encrypted")]

    with mock.patch('builtins.print') as mocked_print:
        buffer.display_last()

        assert mocked_print.call_count == 1

def test_display_last_should_print_last_object_in_buffer():
    buffer = Buffer()
    buffer.memory = [Text(text="test_string1", rot_type=15, status="decrypted"),Text(text="test_string3", rot_type=24, status="encrypted")]

    with mock.patch('builtins.print') as mocked_print:
        buffer.display_last()
        
        mocked_print.assert_called_once_with('test_string3 - encrypted')