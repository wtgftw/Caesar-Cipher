from __future__ import annotations

from buffer import Buffer
from filehandler import FileHandler
from manager import Manager
from menu import Menu
from rot import Rot


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
