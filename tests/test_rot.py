from unittest import mock
from rot import Rot


def test_encrypt_should_return_encypted_string_by_specified_rot():
    rot = Rot()
    enc_type = 1 
    text_str = 'Lorem ipsum'

    encrypted = rot.encrypt(enc_type=enc_type, text_str=text_str)

    assert encrypted == 'Mpsfn jqtvn'


def test_encrypt_should_return_decrypted_string_by_specified_rot():
    rot = Rot()
    enc_type = 1
    text_str = 'Mpsfn jqtvn'

    decrypted = rot.decrypt(enc_type=enc_type, text_str=text_str)

    assert decrypted == "Lorem ipsum"


def test_process_char_should_return_whitespace_when_whitespace_provided():
    rot = Rot()
    char = " "

    encrypted_char = rot._process_char(char=char, shift=2, encrypt=True)

    assert char == encrypted_char


def test_proccess_char_shou