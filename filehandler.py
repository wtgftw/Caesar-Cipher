import os 

class Filehandler:

    def get_file_content(self) -> str:
        user_filepath: str = input("Please enter the file path: ")
        if not os.path.isfile(user_filepath):
            print("File not found. Using default 'input.txt' file.")
            return self.read_file()
        elif not os.path.exists("input.txt"):
            print("Default file 'input.txt' not found. Please provide a valid file path.")
            return self.get_file_content()
        else:
            return self.read_file(filepath=user_filepath)

    def read_file(self, filepath: str="input.txt") -> str:
        with open(filepath, 'r') as file:
            return file.read()


    def write_file(self, filepath: str, content: str) -> None:
        with open(filepath, 'a') as file:
            file.write(content)
        print(f"Content successfully written to {filepath}")