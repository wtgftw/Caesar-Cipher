from menu import Menu
from filehandler import Filehandler
from text import Text

class Manager:
    def __init__(self) -> None:
        self._menu = Menu()
        self._filehandler = Filehandler()
        self._buffer = []


    def run(self) -> None:
        self._menu.start()

        while True:
            choice = self._menu.get_user_choice()
            match choice:
                case 1:
                    print("You selected Encrypt with ROT13")
                    source = self._menu.ask_text_source()
                    destination = self._menu.ask_text_destination()
                    if source == 1:
                        content = self._filehandler.get_file_content()
                        print(f"Content from file: {content}")
                    else:
                        content = input("Please enter the text to encrypt: ")
                        print(f"Content from console: {content}")
                    text_obj = self.encrypt(content,13)
                
                    
                    if destination == 1:
                        filepath = input("Please enter the output file path: ")
                        self._filehandler.write_file(filepath=filepath, text=text_obj)
                        print(f"Content written to file: {filepath}")
                    else:
                        print(f"Encrypted content: {text_obj.text}")
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
                case 0:
                    print("Exiting the program. Goodbye!")
                    break
                case _:
                    print("Invalid choice. Please try again.")
      
    def encrypt(self, text: str, enc_type: int) -> Text:
        self._buffer.clear()
        text = text.strip()
        for char in text:
            if char != " ":
                encrypted_char = chr(ord(char) + enc_type)
            else:
                encrypted_char = char
            self._buffer.append(encrypted_char)

        encrypted_text: str = "".join(self._buffer)

        return Text(text=encrypted_text,
                    rot_type=enc_type,
                    status="encrypted")

        

        