from Citation import Citation
from Database import MemoryDatabase

from unittest import TestCase


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
        self.assertEqual(all_citations[0], self.citation1)
        self.assertEqual(all_citations[1], self.citation2)


