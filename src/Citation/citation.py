
class Citation:
    def __init__(self, _type : str, key : str, data : dict):
        self._type = _type
        self._key = key
        self._data = data
    
    def __str__(self) -> str:
        return f"Citation(type={self._type}, key={self._key}, data={self._data})"
