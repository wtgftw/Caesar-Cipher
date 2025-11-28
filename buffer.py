from text import Text


class Buffer:
    def __init__(self):
        self.memory: list[Text] = []

    def add(self, text: Text):
        self.memory.append(text)

    def extend(self, text: list[Text]):
        self.memory.extend(text)

    def display_buffer(self):
        if not self.memory:
            print("Buffer is empty...")
            return

        for idx, text_obj in enumerate(self.memory, start=1):
            print(f"{idx}. {text_obj.text} - {text_obj.status}")

    def display_last(self):
        if self.memory:
            text_obj = self.memory[-1]
            print(f"{text_obj.text} - {text_obj.status}")
        else:
            print("Buffer is empty")
