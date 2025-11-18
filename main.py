from __future__ import annotations
from menu import Menu
from manager import Manager

class CaesarCipherFacade:
    def __init__(self) -> None:
        self._menu = Menu()
        self._manager = Manager()

    def run(self) -> None:
        self._menu.start()

def main():
    app = CaesarCipherFacade()
    app.run()

if __name__  == "__main__":
    main()