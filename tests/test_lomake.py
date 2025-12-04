from unittest import TestCase
from lomake import Lomake

class TestLomake(TestCase):
    def setUp(self):
        self.input_values = ["article",
                             "articleKey",
                             "author_name",
                             "title_name",
                             "journal_name",
                             "2025"]
        fake_input = iter(self.input_values)
        self.lomake = Lomake(lambda *args, **kwargs: next(fake_input))


    def test_tayta_lomake_returns_citation(self):
        citation_as_str = str(self.lomake.tayta_lomake())
        for s in self.input_values:
            self.assertIn(s, citation_as_str)

    def test_tayta_lomake_raises_with_wrong_citation_type(self):
        self.input_values[0] = "invalid_type"
        fake_input = iter(self.input_values)
        lomake = Lomake(lambda *args, **kwargs: next(fake_input))
        with self.assertRaises(ValueError):
            lomake.tayta_lomake()
