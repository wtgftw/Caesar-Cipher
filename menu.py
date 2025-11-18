class Menu:
    def __init__(self):
        pass

    @staticmethod
    def start() -> None:
        print("Welcome in Caesar Cipher encryptor ")
        Menu.display_menu()

    @staticmethod
    def display_menu() -> None:
        print("*" * 30)
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        print("*" * 30)
    
    def get_user_choice(self) -> int:
        while True:
            try:
                choice: int = int(input("Please select an option (1-3): "))
                return choice
            except: 
                ValueError("Invalid input. Please enter a number between 1 and 3.")
