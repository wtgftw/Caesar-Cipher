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


def test_proccess_char_should_return_same_char_when_out_of_range():
    rot = Rot()
    char = chr(65537)

    encrypted_char = rot._process_char(char=char,shift=2, encrypt=True)

    assert char == encrypted_char


def test_process_char_should_return_shifted_char_when_in_range():
    rot = Rot()
    chars = ["a","→","P",chr(65534)]

    encrypted_chars = [rot._process_char(char,3,True) for char in chars]
    
    assert chars != encrypted_chars

