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

    extension_list = [Text("test_string1", 15, "decrypted"),Text("test_string3", 24, "encrypted")]

    buffer.extend(extension_list)

    assert len(buffer.memory) == 3


def test_display_buffer_should_print_bufer_empty_info_then_return_when_buffer_is_empty():
    buffer = Buffer()

    with mock.patch('builtins.print') as mocked_print:
        buffer.display_buffer()

        assert mocked_print.mock_calls == [mock.call("Buffer is empty...")]

