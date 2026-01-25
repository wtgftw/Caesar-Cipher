from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from text import Text


class Buffer:
    def __init__(self) -> None:
        self.memory: list["Text"] = []

    def add(self, text: "Text") -> None:
        self.memory.append(text)

    def extend(self, text: list["Text"]) -> None:
        self.memory.extend(text)

    def display_buffer(self) -> None:
        if not self.memory:
            print("Buffer is empty...")
            return

        for idx, text_obj in enumerate(self.memory, start=1):
            print(f"{idx}. {text_obj.text} - {text_obj.status}")

    def display_last(self) -> None:
        if self.memory:
            text_obj = self.memory[-1]
            print(f"{text_obj.text} - {text_obj.status}")
        else:
            print("Buffer is empty")
