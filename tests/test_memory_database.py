from unittest import TestCase
import tempfile
import os

from citation import Citation
from database import MemoryDatabase



class TestMemoryDatabase(TestCase):
    def setUp(self):
        self.db = MemoryDatabase()
        self.citation1 = Citation("article", "key1", {"author": "author1"})
        self.citation2 = Citation("book", "key2", {"author": "author2"})

    def test_initial_database_empty(self):
        self.assertEqual(self.db.get_all(), [])

    def test_get_all_returns_empty_list_when_no_citations(self):
        all_citations = self.db.get_all()
        self.assertIsInstance(all_citations, list)
        self.assertEqual(len(all_citations), 0)

    def test_add_citation_to_database(self):
        not_citation = {}
        #En ole ihan varma tästä, mutta näyttää toimivan... -Vilppu
        #Testataan että raise TypeError toimii
        with self.assertRaises(TypeError) as context:
            self.db.add(not_citation)
        self.assertTrue("Not a Citation object" in str(context.exception))
        self.db.add(self.citation1)
        self.db.add(self.citation2)
        all_citations = self.db.get_all()
        self.assertIn(self.citation1, all_citations)
        self.assertIn(self.citation2, all_citations)

    def test_get_all_list_of_citations(self):
        self.db.add(self.citation1)
        self.db.add(self.citation2)
        all_citations = self.db.get_all()
        self.assertEqual(len(all_citations), 2)
        self.assertIn(self.citation1, all_citations)
        self.assertIn(self.citation2, all_citations)

    def test_hae_viitteet_returns_correct_citations(self):
        self.db.add(self.citation1)
        self.db.add(self.citation2)
        filt = {"author": "author1"}
        filt_citations = self.db.hae_viitteet(filt)
        self.assertIn(self.citation1, filt_citations)
        self.assertEqual(len(filt_citations), 1)

    def test_hae_viitteet_does_not_return_citations_with_missing_keys(self):
        self.db.add(self.citation1)
        self.db.add(self.citation2)
        filt = {"key_that_does_not_exist": "something"}
        filt_citations = self.db.hae_viitteet(filt)
        self.assertEqual(len(filt_citations), 0)

    def test_load_from_file_loads_citations_from_saved_file(self):
        self.db.add(self.citation1)
        self.db.add(self.citation2)
        with tempfile.TemporaryDirectory() as tempdir:
            filename = os.path.join(tempdir, "test_db.json")
            self.db.save_to_file(filename)
            new_db = MemoryDatabase()
            new_citation = Citation(
                "type", "some_key", {"author": "author"}
                )
            new_db.add(new_citation)
            new_db.load_from_file(filename)
            all_citations = new_db.get_all()
            self.assertIn(self.citation1, all_citations)
            self.assertIn(self.citation2, all_citations)
            self.assertIn(new_citation, all_citations)
            self.assertEqual(len(all_citations), 3)
