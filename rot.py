
class Rot:
    MAX_BMP = 65535
    def encrypt(self, enc_type: int, text_str: str) -> str:
        text_str = text_str.strip()

        encrypted_text = "".join(
            self._process_char(char, enc_type, encrypt=True) for char in text_str
        )

        return encrypted_text

    def decrypt(self, enc_type: int, text_str: str) -> str:
        text_str = text_str.strip()

        decrypted_text = "".join(
            self._process_char(char, enc_type, encrypt=False) for char in text_str
        )

        return decrypted_text

    def _process_char(self, char: str, shift: int, encrypt: bool) -> str:
        if char == " ":
            return char

        char_code = ord(char)

        if char_code <= self.MAX_BMP:
            actual_shift = shift if encrypt else -shift
            shifted = (char_code + actual_shift) % (self.MAX_BMP + 1)
            return chr(shifted)
        return char
