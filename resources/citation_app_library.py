from citation import Citation
from database import DatabaseHandler
from citation_app import CitationApp

class CitationAppLibrary:
    def __init__(self):
        self._db = DatabaseHandler()
        self._input = []
        self._output = []
        self.citation1 = Citation("article", "key1", {"author": "author1"}, 0)
        self.citation2 = Citation("book", "key2", {"author": "author2"}, 2147483647)

    def add_input(self, input_):
        self._input.append(input_)

    def is_in_output(self, output_):
        for out in self._output:
            if output_ in out:
                return
        raise AssertionError(f"{output_} not in {self._output}")

    def is_not_in_output(self, output_):
        for out in self._output:
            if output_ in out:
                raise AssertionError(f"{output_} is in {self._output}")

    def create_app(self):
        # Iterator syötteille
        it = iter(self._input)

        # Fake input-funktio palauttaa aina seuraavan arvon iteratorista
        def fake_input(_=""):
            return str(next(it))

        def handle_output(out):
            self._output.append(out)

        app = CitationApp(
            self._db,
            fake_input,
            handle_output
        )
        app.run()

    def add_citation_to_db(self, type_, key,
                           data : dict, timestamp = None):
        if timestamp is not None:
            self._db.add(Citation(type_, key, data, timestamp))
        else:
            self._db.add(Citation(type_, key, data))

    def init_default_database(self):
        self._db.add(self.citation1)
        self._db.add(self.citation2)
