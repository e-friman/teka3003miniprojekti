import json
import copy
from citation import Citation

class MemoryDatabase:
    def __init__(self):
        self._data = {}

    def add(self, citation: Citation) -> None:
        if not isinstance(citation, Citation):
            raise TypeError("Not a Citation object")
        copied = copy.deepcopy(citation)
        self._data[copied.key] = copied

    def get_all(self) -> list[Citation]:
        results = []
        for citation in self._data.values():
            copy_cite = copy.deepcopy(citation)
            copy_cite.data.pop("tag", None)
            results.append(copy_cite)
        return results
    #Haku
    def hae_viitteet(self, filt: dict) -> list[Citation]:
        tulokset = []
        for citation in self._data.values():
            #filter = { "author": obj1, "title": obj2, .. }
            matches_filter = True
            for key in filt:
                if key not in citation.data:
                    matches_filter = False
                    break
                if filt[key] != citation.data[key]:
                    matches_filter = False
                    break
            if matches_filter:
                tulokset.append(copy.deepcopy(citation))

        return tulokset

    def save_to_file(self, filename: str):
        db_as_dict = {
            "citations": [citation.to_json() for citation in self._data.values()]
        }
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(db_as_dict, f)

    def load_from_file(self, filename: str):
        with open(filename, "r", encoding="utf-8") as f:
            db_as_dict = json.load(f)
            for citation_json in db_as_dict["citations"]:
                citation = Citation.from_json(citation_json)
                if citation.key not in self._data: # kato timestamp kanssa myöhemmin..
                    self._data[citation.key] = citation
