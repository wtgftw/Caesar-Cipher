import os 
from text import Text
import json

class Filehandler:

    def get_file_content(self) -> list:
        user_filepath: str = input("Please enter the file path: ")
        temp = []
        if not os.path.isfile(user_filepath):
            raise FileNotFoundError("JSON file was not found. Provide working path.")
        else:
                with open(user_filepath) as file:
                    data = json.load(file)
                    for x in data:
                        temp.append(Text(text=x.get("text"),rot_type=x.get("rot_type"),status=x.get("status")))
                    return temp

    def write_file(self, data: list) -> None:
        user_filepath: str = input("Please enter the file path: ")
        if ".json" not in user_filepath:
             raise FileNotFoundError("It must be JSON file")
        elif len(data) < 1:
             raise BufferError("Buffer is empty")
        else:
            if not os.path.isfile(user_filepath):
                json_list: list = []
                for obj in data:
                    tmp_dict = {"text":obj.text,"rot_type":obj.rot_type,"status":obj.status}
                    json_list.append(tmp_dict)
                        
                with open(user_filepath, 'a', encoding="utf-8") as jsonfile:
                    json.dump(json_list, jsonfile, indent=4)
                    print(f"Content successfully written to {user_filepath}")
            else:
                with open(user_filepath, "r", encoding="utf-8") as jsonfile:
                    extended_data = json.load(jsonfile)
                    print(extended_data)
                    for obj in data:
                        tmp_dict = {"text":obj.text,"rot_type":obj.rot_type,"status":obj.status}
                        extended_data.append(tmp_dict)
                    with open(user_filepath, "w", encoding="utf-8") as jsonfile:
                        json.dump(extended_data, jsonfile, indent=4)