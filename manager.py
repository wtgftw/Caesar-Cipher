from menu import Menu
from filehandler import Filehandler
from text import Text

class Manager:
    def __init__(self) -> None:
        self._menu = Menu()
        self._filehandler = Filehandler()
        self._buffer: list[Text]= []
        #self._multi: list[Text] = []


    def run(self) -> None:
        self._menu.start()

        while True:
            choice = self._menu.get_user_choice()
            match choice:
                case 1:
                    print("You selected Encrypt with ROT13")
                    source = self._menu.ask_text_source()
    
                    if source == 1:
                        content = self._filehandler.get_file_content()
                        print(f"Content from file: {content}")
                        self.encrypt(text_list=content, enc_type=13)
                    else:
                        content = input("Please enter the text to encrypt: ")
                        self.encrypt(text_str=content, enc_type=13)
            

                case 2:
                    print("You selected Encrypt with ROT47")
                    source = self._menu.ask_text_source()
    
                    if source == 1:
                        content = self._filehandler.get_file_content()
                        print(f"Content from file: {content}")
                        self.encrypt(text_list=content, enc_type=47)
                    else:
                        content = input("Please enter the text to encrypt: ")
                        self.encrypt(text_str=content, enc_type=47)
                case 3:
                    print("You selected Encrypt with Custom Shift")
                    user_custom_shift = int(input("Provide custom shift: "))
                    
                    source = self._menu.ask_text_source()
    
                    if source == 1:
                        content = self._filehandler.get_file_content()
                        print(f"Content from file: {content}")
                        self.encrypt(text_list=content, enc_type=user_custom_shift)
                    else:
                        content = input("Please enter the text to encrypt: ")
                        self.encrypt(text_str=content, enc_type=user_custom_shift)
                case 4:
                    print("You selected Decrypt with ROT13")
                case 5:
                    print("You selected Decrypt with ROT47")
                case 6:
                    print("You selected Encrypt with Custom Shift")
                case 7:
                    print("You selected Display last")
                   # print(self._buffer[len(self._buffer) - 1])
                    print(self._buffer)
                case 8:
                    print("You selected Display buffer")
                case 9:
                    print("You selected Print to file")
                    #destination = self._menu.ask_text_destination()
                    '''
                    if destination == 1:
                        filepath = input("Please enter the output file path: ")
                        self._filehandler.write_file(filepath=filepath, text=text_obj)
                        print(f"Content written to file: {filepath}")'''
                case 0:
                    print("Exiting the program. Goodbye!")
                    break
                case _:
                    print("Invalid choice. Please try again.")
            
    def encrypt(self, enc_type: int, text_list=None, text_str=None) -> None:
        result: list[chr] = []
        if text_list:
            for text in text_list:
                result = []
                text = text.strip()
                for char in text:
                    encrypted_char = self._encrypt_char(char=char, shift=enc_type)
                    result.append(encrypted_char)

                encrypted_text: str = "".join(result)

                self._buffer.append(
                Text(text=encrypted_text,
                    rot_type=enc_type,
                    status="encrypted")
            )
        else:
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