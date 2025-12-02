from citation import Citation
from .memory_database import MemoryDatabase

class DatabaseHandler:
    def __init__(self,db = MemoryDatabase()):
        self._db = db

    def add(self, citation: Citation) -> None:
        self._db.add(citation)

    def get_all(self) -> list[Citation]:
        return self._db.get_all()

    def hae_viitteet(self, filt: dict) -> list[Citation]:
        return self._db.hae_viitteet(filt)
