from text import Text


class Manager:
    def __init__(self, menu, file_handler, buffer, rot) -> None:
        self._menu = menu
        self._file_handler = file_handler
        self._buffer = buffer
        self._rot = rot

    def _get_buffer_text_by_status(self, required_status: str) -> str:
        if not self._buffer.memory:
            raise ValueError("Buffer is empty...")

        print(f"Choose index from buffer in range (1-{len(self._buffer.memory)})")
        buffer_idx = self._menu.get_user_choice(options_range=len(self._buffer.memory))

        text_obj = self._buffer.memory[buffer_idx - 1]

        if text_obj.status != required_status:
            raise ValueError(f"Selected text must be {required_status}.")

        return text_obj.text

    def _handle_encrypt(self, shift: int):
        text_source = self._menu.ask_text_source()

        if text_source == 1:
            content = input("Please enter the text to encrypt: ")
        else:
            content = self._get_buffer_text_by_status("decrypted")

        encrypted_text = self._rot.encrypt(enc_type=shift, text_str=content)

        self._buffer.add(Text(text=encrypted_text, rot_type=shift, status="encrypted"))
        print(f"Text encrypted successful with shift {shift}")

    def _handle_decrypt(self, shift: int):
        text_source = self._menu.ask_text_source()

        if text_source == 1:
            content = input("Please enter the text to decrypt: ")
        else:
            content = self._get_buffer_text_by_status("encrypted")

        encrypted_text = self._rot.decrypt(enc_type=shift, text_str=content)

        self._buffer.add(Text(text=encrypted_text, rot_type=shift, status="decrypted"))
        print(f"Text decrypted successful with shift {shift}")

    def _get_custom_shift(self) -> int:
        return int(input("Provide custom shift: "))

    def run(self) -> None:
        self._menu.start()

        while True:
            try:
                menu_choice = self._menu.get_user_choice(options_range=11)
                match menu_choice:
                    case 1:
                        print("You selected Encrypt with ROT13")
                        self._handle_encrypt(shift=13)
                    case 2:
                        print("You selected Encrypt with ROT47")
                        self._handle_encrypt(shift=47)
                    case 3:
                        print("You selected Encrypt with Custom Shift")
                        custom_shift = self._get_custom_shift()
                        self._handle_encrypt(shift=custom_shift)
                    case 4:
                        print("You selected Decrypt with ROT13")
                        self._handle_decrypt(shift=13)
                    case 5:
                        print("You selected Decrypt with ROT47")
                        self._handle_decrypt(shift=47)
                    case 6:
                        print("You selected Decrypt with Custom Shift")
                        custom_shift = self._get_custom_shift()
                        self._handle_decrypt(shift=custom_shift)
                    case 7:
                        print("You selected Display last")
                        self._buffer.display_last()
                    case 8:
                        print("You selected Display buffer", end="\n")
                        self._buffer.display_buffer()
                    case 9:
                        print("You selected Load from JSON file")
                        content = self._file_handler.read_file()
                        self._buffer.extend(content)
                        print(
                            f"Content from file: {[(text_obj.text, text_obj.rot_type, text_obj.status) for text_obj in content]} loaded to buffer"
                        )
                    case 10:
                        print("You selected Print to file")
                        self._file_handler.write_file(data=self._buffer.memory)
                    case 11:
                        print("Exiting the program. Goodbye!")
                        break
                    case _:
                        print("Invalid choice. Please try again.")
            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Unexcepted error: {e}")
