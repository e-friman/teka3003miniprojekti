class Citation:
    def __init__(self, _type: str, key: str, data: dict):
        self._type = _type
        self._key = key
        self._data = data

    def __str__(self) -> str:
        return f"Citation(type={self._type}, key={self._key}, data={self._data})"

    @property
    def type(self) -> str:
        return self._type
    @property
    def key(self) -> str:
        return self._key
    @property
    def data(self) -> dict:
        return self._data

    #muunna data bibtex muotoon
    def to_bibtex(self) -> str:
        type_ = self.type
        key = self.key
        data = ""
        for index in self.data:
            data += ",\n"
            data += index + "=" + f'"{self.data[index]}"'

        bibtex = "@" + type_ + "{" + key + data + "\n}"

        return bibtex
