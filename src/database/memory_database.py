from citation import Citation


class MemoryDatabase:
    def __init__(self):
        self._data = []

    def add(self, citation: Citation) -> None:
        self._data.append(citation)

    def get_all(self) -> list[Citation]:
        return self._data
