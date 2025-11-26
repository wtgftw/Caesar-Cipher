from dataclasses import asdict
import os
import json

from text import Text

class FileHandler:
    def read_file(self) -> list[Text]:
        user_filepath = self._get_file_path()
        self._validate_file_exists(user_filepath)

        with open(user_filepath, encoding="utf-8") as file:
            data = json.load(file)
            return [
                Text(
                    text=item.get("text"),
                    rot_type=item.get("rot_type"),
                    status=item.get("status")

                )
                for item in data
            ]

    def write_file(self, data: list[Text]) -> None:
        filepath = self._get_file_path()
        self._validate_json_extension(filepath)
        self._validate_buffer_not_empty(data)

        json_list = self._convert_to_dict_list(data)

        if os.path.isfile(filepath):
            self._append_to_existing_file(filepath, json_list)
        else:
            self._create_new_file(filepath, json_list)

    def _get_file_path(self) -> str:
        return input("Please enter the file path: ")

    def _validate_file_exists(self, filepath: str) -> None:
        if not os.path.isfile(filepath):
            raise FileNotFoundError("JSON file was not found. Provide working path.")

    def _validate_json_extension(self, filepath: str) -> None:
        if not filepath.endswith(".json"):
            raise FileExistsError("JSON file extension not supported.")

    def _validate_buffer_not_empty(self, data: list[Text]):
        if not data:
            raise ValueError("Buffer was empty.")

    def _convert_to_dict_list(self, data: list[Text]) -> list[dict[str, str]]:
        return [asdict(obj) for obj in data]

    def _append_to_existing_file(self, filepath: str, new_data: list[dict[str, str]]):
        with open(filepath, "r", encoding="utf-8") as file:
            existing_data = json.load(file)

        existing_data.extend(new_data)

        with open(filepath, "w", encoding="utf-8") as file:
            json.dump(existing_data, file, indent=4)

    def _create_new_file(self, filepath: str, data: list[dict[str, str]]) -> None:
        with open(filepath, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)