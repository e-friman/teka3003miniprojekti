import json
import time
class Citation:
    def __init__(
            self,
            type_: str,
            key: str,
            data: dict,
            timestamp = None
            ):
        self._type = type_
        self._key = key
        self._data = data
        self._timestamp = int(timestamp if timestamp is not None else time.time())
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
    @property
    def timestamp(self)-> int:
        return self._timestamp


    #muunna data bibtex muotoon
    def to_bibtex(self) -> str:
        type_ = self.type
        key = self.key
        
        data_copy = self.data.copy()
        data_copy.pop("tag", None)

        data = ""
        for index in data_copy:
            data += ",\n"
            data += "\t" + index + " = " + f'"{data_copy[index]}"'

        bibtex = "@" + type_ + "{" + key + data + "\n}"

        return bibtex

    def to_json(self) -> str:
        cit_dict = {
            "type": self.type,
            "key": self.key,
            "data": json.dumps(self.data),
            "timestamp": self.timestamp
        }
        return json.dumps(cit_dict)

    @classmethod
    def from_json(cls, json_str: str):
        cit_dict = json.loads(json_str)
        return cls(
            type_=cit_dict["type"],
            key=cit_dict["key"],
            data=json.loads(cit_dict["data"]),
            timestamp=cit_dict.get("timestamp")
        )

    def __deepcopy__(self, _memo):
        return Citation(
            self.type,
            self.key,
            self.data.copy(),
            self.timestamp)

    def __eq__(self, rhs):
        if not isinstance(rhs, Citation):
            return False
        return (
            self.type == rhs.type
            and self.key == rhs.key
            and self.data == rhs.data
        )

    def __ne__(self, rhs):
        return not self == rhs
