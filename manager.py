from menu import Menu

class Manager:
    def __init__(self) -> None:
        self._menu = Menu()

    def run(self) -> None:
        self._menu.start()

        while True:
            choice = self._menu.get_user_choice()
            match choice:
                case 1:
                    print("You selected Encrypt with ROT13")
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
      
    