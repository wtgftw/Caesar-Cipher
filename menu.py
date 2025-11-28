class Menu:
    def __init__(self):
        self.menu_options: dict[int, str] = {
            1: "Encrypt with ROT13",
            2: "Encrypt with ROT47",
            3: "Encrypt with Custom Shift",
            4: "Decrypt with ROT13",
            5: "Decrypt with ROT47",
            6: "Decrypt with Custom Shift",
            7: "Display last",
            8: "Display buffer",
            9: "Load from JSON file",
            10: "Save to file",
            11: "Exit",
        }

    def start(self) -> None:
        print("Welcome in Caesar Cipher encryptor ")
        self.main_menu()

    def main_menu(self) -> None:
        print("*" * 30)
        for key, value in self.menu_options.items():
            print(f"{key}. {value}")
        print("*" * 30)

    @staticmethod
    def get_user_choice(options_range: int) -> int:
        try:
            choice = int(input(f"Please select an option (1-{options_range}): "))
            if not 1 <= choice <= options_range:
                raise ValueError
            return choice
        except ValueError:
            raise ValueError(
                f"Invalid input. Please enter a number between 1 and {options_range}."
            )

    def ask_text_source(self) -> int:
        print("\nPlease choose the text source:")
        print("1. Input from console")
        print("2. Select from buffer")
        return self.get_user_choice(options_range=2)
