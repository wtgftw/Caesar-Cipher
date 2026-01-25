from dataclasses import dataclass


@dataclass
class Text:
    text: str
    rot_type: int
    status: str
