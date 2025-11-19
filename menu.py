class Menu:
    def __init__(self):
        pass

    def start(self) -> None:
        print("Welcome in Caesar Cipher encryptor ")
        self.main_menu()

    @staticmethod
    def main_menu() -> None:
        print("*" * 30)
        print("""Encrypt text:
    1. ROT13
    2. ROT47
    3. Custom Shift
Decrypt text:
    4. ROT13
    5. ROT47
    6. Custom Shift
0. Exit""")
        print("*" * 30)

    def get_user_choice(self) -> int:
        while True:
            try:
                choice: int = int(input("Please select an option (0-6): "))
                if choice < 0 or choice > 6:
                    raise ValueError("Invalid input. Please enter a number between 0 and 6.")
                return choice
            except: 
                raise ValueError("Invalid input. Please enter a number between 0 and 6.")

    def ask_text_source(self) -> int:
        print("Please choose the text source:")
        print("1. Input from file")
        print("2. Input from console")
        return self.verify_text_choice()
    
    def ask_text_destination(self) -> int:
        print("Please choose the text destination:")
        print("1. Write to file")
        print("2. Show in console")
        return self.verify_text_choice()

    def verify_text_choice(self) -> int:
        while True:
            try:  
                choice: int = int(input("Please select an option (1-2): "))
                if choice < 1 or choice > 2:
                    raise ValueError("Invalid input. Please enter 1 or 2.")
                return choice
            except:
                raise ValueError("Invalid input. Please enter 1 or 2.")   