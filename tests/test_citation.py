from unittest import TestCase

from citation import Citation



class TestCitation(TestCase):
    def setUp(self):
        self.citation = Citation("article", "articleKey", {"author": "author"})

    def test_initialization_creates_correct_attributes(self):
        self.assertEqual(self.citation.type, "article")
        self.assertEqual(self.citation.key, "articleKey")
        self.assertEqual(self.citation.data, {"author": "author"})

    def test_str_returns_correct_string(self):
        self.assertEqual(
            str(self.citation),
            "Citation(type=article, key=articleKey, data={'author': 'author'})",
        )

    def test_to_bibtex_returns_correctly_formatted_string(self):
        bibtex_format = self.citation.to_bibtex()
        self.assertEqual(
            bibtex_format,
            '@article{articleKey,\n\tauthor = "author"\n}'
        )

    def test_from_json_loads_citation_returned_by_to_json(self):
        json_str = self.citation.to_json()
        loaded_citation = Citation.from_json(json_str)
        self.assertEqual(loaded_citation.type, self.citation.type)
        self.assertEqual(loaded_citation.key,  self.citation.key)
        self.assertEqual(loaded_citation.data, self.citation.data)

    def test_eq_and_ne_return_correct_booleans(self):
        test_cit1 = Citation("book", "book_key", {"author": "author1"})
        test_cit2 = Citation("article", "articleKey", {"author": "author"})
        test_cit3 = {"stuff"}
        self.assertFalse(test_cit3 == test_cit1)
        self.assertFalse(test_cit1 == self.citation)
        self.assertTrue(test_cit1 != self.citation)
        self.assertTrue(test_cit2 == self.citation)
        self.assertFalse(test_cit2 != self.citation)
