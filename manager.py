from menu import Menu
from filehandler import Filehandler
from text import Text

class Manager:
    def __init__(self) -> None:
        self._menu = Menu()
        self._filehandler = Filehandler()
        self._buffer: list[Text]= []

    def encrypt(self, enc_type: int, text_str=None) -> None:
            result: list[str] = []
            text_str = text_str.strip()
            for char in text_str:
                encrypted_char = self._encrypt_char(char=char, shift=enc_type)
                result.append(encrypted_char)

            encrypted_text: str = "".join(result)

            self._buffer.append(
                Text(text=encrypted_text,
                    rot_type=enc_type,
                    status="encrypted")
            )

    def _encrypt_char(self, char: str, shift: int) -> str:
        MAX_BMP: int = 65535
        if char == " ":
            return char
        
        char_code = ord(char)

        if char_code <= MAX_BMP:
            shifted = (char_code + shift) % (MAX_BMP + 1)
            return chr(shifted)
        else: 
            return char     
        
    def decrypt(self, enc_type: int, text_str: str) -> None:
            result: list[str] = []
            text_str = text_str.strip()
            for char in text_str:
                decrypted_char = self._decrypt_char(char=char, shift=enc_type)
                result.append(decrypted_char)

            decrypted_text: str = "".join(result)

            self._buffer.append(
                Text(text=decrypted_text,
                    rot_type=enc_type,
                    status="decrypted")
            )

    def _decrypt_char(self, char: str, shift: int) -> str:
        MAX_BMP: int = 65535
        if char == " ":
            return char
        
        char_code = ord(char)

        if char_code <= MAX_BMP:
            shifted = (char_code - shift) % (MAX_BMP + 1)
            return chr(shifted)
        else: 
            return char   


    def run(self) -> None:
        self._menu.start()

        while True:
            menu_choice = self._menu.get_user_choice(options_range=11)
            match menu_choice:
                case 1:
                    print("You selected Encrypt with ROT13")
                    text_source = self._menu.ask_text_source()
                    if text_source == 1:
                        content = input("Please enter the text to encrypt: ")
                        self.encrypt(text_str=content, enc_type=13)
                    else:
                        if len(self._buffer) > 0:
                            print(f"Choose index from buffer in range {len(self._buffer)}")
                            buffer_idx = int(input("Index: "))

                            if self._buffer[buffer_idx-1].status == "decrypted":
                                self.encrypt(text_str=self._buffer[buffer_idx-1].text, enc_type=13)
                        else:
                            raise ValueError("Buffer is empty...")

                case 2:
                    print("You selected Encrypt with ROT47")
                    text_source = self._menu.ask_text_source()
                    if text_source == 1:
                        content = input("Please enter the text to encrypt: ")
                        self.encrypt(text_str=content, enc_type=13)
                    else:
                        if len(self._buffer) > 0:
                            print(f"Choose index from buffer in range {len(self._buffer)}")
                            buffer_idx = int(input("Index: "))

                            if self._buffer[buffer_idx-1].status == "decrypted":
                                self.encrypt(text_str=self._buffer[buffer_idx-1].text, enc_type=13)
                        else:
                            raise ValueError("Buffer is empty...")
                case 3:
                    print("You selected Encrypt with Custom Shift")
                    user_custom_shift = int(input("Provide custom shift: "))
    
                    text_source = self._menu.ask_text_source()
                    if text_source == 1:
                        content = input("Please enter the text to encrypt: ")
                        self.encrypt(text_str=content, enc_type=user_custom_shift)
                    else:
                        if len(self._buffer) > 0:
                            print(f"Choose index from buffer in range {len(self._buffer)}")
                            buffer_idx = int(input("Index: "))

                            if self._buffer[buffer_idx-1].status == "decrypted":
                                self.encrypt(text_str=self._buffer[buffer_idx-1].text, enc_type=user_custom_shift)
                        else:
                            raise ValueError("Buffer is empty...")
                case 4:
                    print("You selected Decrypt with ROT13")
                    
                    text_source = self._menu.ask_text_source()
                    if text_source == 1:
                        content = input("Please enter the text to encrypt: ")
                        self.decrypt(text_str=content, enc_type=13)
                    else:
                        if len(self._buffer) > 0:
                            print(f"Choose index from buffer in range {len(self._buffer)}")
                            buffer_idx = int(input("Index: "))

                            if self._buffer[buffer_idx-1].status == "encrypted":
                                self.decrypt(text_str=self._buffer[buffer_idx-1].text, enc_type=13)
                        else:
                            raise ValueError("Buffer is empty...")
                    
                case 5:
                    print("You selected Decrypt with ROT47")

                    text_source = self._menu.ask_text_source()
                    if text_source == 1:
                        content = input("Please enter the text to encrypt: ")
                        self.decrypt(text_str=content, enc_type=47)
                    else:
                        if len(self._buffer) > 0:
                            print(f"Choose index from buffer in range {len(self._buffer)}")
                            buffer_idx = int(input("Index: "))

                            if self._buffer[buffer_idx-1].status == "encrypted":
                                self.decrypt(text_str=self._buffer[buffer_idx-1].text, enc_type=47)
                        else:
                            raise ValueError("Buffer is empty...")
                case 6:
                    print("You selected Decrypt with Custom Shift")

                    user_custom_shift = int(input("Provide custom shift: "))
    
                    text_source = self._menu.ask_text_source()
                    if text_source == 1:
                        content = input("Please enter the text to decrypt: ")
                        self.decrypt(text_str=content, enc_type=user_custom_shift)
                    else:
                        if len(self._buffer) > 0:
                            print(f"Choose index from buffer in range {len(self._buffer)}")
                            buffer_idx = int(input("Index: "))

                            if self._buffer[buffer_idx-1].status == "encrypted":
                                self.decrypt(text_str=self._buffer[buffer_idx-1].text, enc_type=user_custom_shift)
                        else:
                            raise ValueError("Buffer is empty...")
                case 7:
                    print("You selected Load from JSON file")
                    content = self._filehandler.get_file_content()
                    self._buffer.extend(content)
                    print(f"Content from file: {content} loaded to buffer")


                case 8:
                    print("You selected Display last")
                    print(self._buffer[len(self._buffer) - 1])
                case 9:
                    print("You selected Display buffer:", end="\n")
                    [print(f"{idx}. {text_obj.text} - {text_obj.status}") for idx,text_obj in enumerate(self._buffer, start=1)] 
                case 10:
                    print("You selected Print to file")
                    self._filehandler.write_file(data=self._buffer)
                    
                case 11:
                    print("Exiting the program. Goodbye!")
                    break
                case _:
                    print("Invalid choice. Please try again.")
            
