from __future__ import annotations
from manager import Manager
import os, json
class CaesarCipherFacade:
    def __init__(self) -> None:
        self._manager = Manager()

    def run(self) -> None:
        self._manager.run()

def main():
    app = CaesarCipherFacade()
    app.run()

if __name__  == "__main__":
    #main()
    def get_file_content() -> None:
        user_filepath: str = input("Please enter the file path: ")
        if not os.path.isfile(user_filepath):
            print("File not found. Using default 'input.txt' file.")
        else:
            with open(user_filepath) as file:
                data = json.load(file)
                print(data.get("rot_type"))
    get_file_content()
