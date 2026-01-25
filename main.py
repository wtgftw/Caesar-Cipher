from __future__ import annotations

from src.buffer import Buffer
from src.filehandler import FileHandler
from src.manager import Manager
from src.menu import Menu
from src.rot import Rot


class CaesarCipherFacade:
    def __init__(self, manager: Manager) -> None:
        self._manager = manager

    def run(self) -> None:
        self._manager.run()


def main() -> None:
    manager = Manager(
        menu=Menu(), file_handler=FileHandler(), buffer=Buffer(), rot=Rot()
    )
    app = CaesarCipherFacade(manager=manager)
    app.run()


if __name__ == "__main__":
    main()
