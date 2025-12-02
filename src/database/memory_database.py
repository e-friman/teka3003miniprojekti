from citation import Citation


class MemoryDatabase:
    def __init__(self):
        self._data = []

    def add(self, citation: Citation) -> None:
        self._data.append(citation)

    def get_all(self) -> list[Citation]:
        return self._data
    #Haku
    def hae_viitteet(self, filt: dict) -> list[Citation]:
        tulokset = []
        for citation in self._data:
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
                tulokset.append(citation)

        return tulokset
