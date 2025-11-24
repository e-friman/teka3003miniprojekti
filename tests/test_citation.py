from Citation import Citation

from unittest import TestCase


class TestCitation(TestCase):
    def setUp(self):
        self.citation = Citation("article", "articleKey", {"author": "author"})
    def test_initialization_creates_correct_attributes(self):
        self.assertEqual(self.citation._type, "article")
        self.assertEqual(self.citation._key, "articleKey")
        self.assertEqual(self.citation._data, {"author": "author"})
    def test_str_returns_correct_string(self):
        self.assertEqual(str(self.citation), "Citation(type=article, key=articleKey, data={'author': 'author'})")


