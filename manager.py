from menu import Menu
from filehandler import Filehandler
from text import Text

class Manager:
    def __init__(self) -> None:
        self._menu = Menu()
        self._filehandler = Filehandler()
        self._buffer = []
        self._multi = []


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
                    else:
                        content = input("Please enter the text to encrypt: ")
                    text_obj = self.encrypt(text_list=content, enc_type=13)
                    self._buffer.append(text_obj)

                case 2:
                    print("You selected Encrypt with ROT47")
                case 3:
                    print("You selected Encrypt with Custom Shift")
                case 4:
                    print("You selected Decrypt with ROT13")
                case 5:
                    print("You selected Decrypt with ROT47")
                case 6:
                    print("You selected Encrypt with Custom Shift")
                case 7:
                    print("You selected Display last")
                    print(self._buffer[0])
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
            
    def encrypt(self, text_list: list, enc_type: int) -> Text:
        result: list = []
        for text in text_list:
            text = text.strip()
            result = []
            for char in text:
                if char != " ":
                    encrypted_char = chr(ord(char) + enc_type)
                else:
                    encrypted_char = char
                result.append(encrypted_char)

            encrypted_text: str = "".join(result)
            encrypted_text.encode()

            self._multi.append(
                Text(text=encrypted_text,
                    rot_type=enc_type,
                    status="encrypted")
            )


        return self._multi

        

        