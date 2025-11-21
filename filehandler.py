import os 
from text import Text
import json

class Filehandler:

    def get_file_content(self) -> str:
        user_filepath: str = input("Please enter the file path: ")
        if not os.path.isfile(user_filepath):
            print("File not found. Using default 'input.txt' file.")
            return self.read_file()
        else:
            return json.loads(s=user_filepath)

    def read_file(self, filepath: str="input.txt") -> str:
        with open(filepath, 'r') as file:
            return file.read()


    def write_file(self, filepath: str, text: Text) -> None:
        
        with open('data.json', 'a', encoding="utf-8") as file:
            dict(json.dump(text, file, ensure_ascii=False, indent=4))
        print(f"Content successfully written to {filepath}")