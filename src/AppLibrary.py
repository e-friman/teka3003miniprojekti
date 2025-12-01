from citation import Citation
from database import MemoryDatabase
from lomake import Lomake


class AppLibrary:
    # Citation related methods
    def create_citation(self, type_, key, data: dict):
        return Citation(type_, key, data)
    
    def citation_to_string(self, citation):
        return str(citation)

    # Database related methods
    def create_database(self):
        return MemoryDatabase()

    def database_add(self, db, citation):
        db.add(citation)
        return db

    def database_all(self, db):
        return db.get_all()

    # Lomake related methods
    def create_lomake_citation(self, values):
        """
        Täyttää Lomake-luokan faken avulla.
        values: lista arvoja järjestyksessä:
        [entry_type, key, kenttä1, kenttä2, ...]
        """
        # Iterator syötteille
        it = iter(values)

        # Fake input-funktio palauttaa aina seuraavan arvon iteratorista
        def fake_input(prompt=""):
            return str(next(it))

        form = Lomake(fake_input)
        return form.tayta_lomake(None)
