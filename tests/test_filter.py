from unittest import TestCase
from filter_builder import FilterBuilder

class TestFilter(TestCase):
    def fake_input(self, prompt):
        return ""

    def fake_input2(self, prompt):
        return next(self.inputs2)

    def setUp(self):
        self.inputs2 = iter([
            "key", "juup", ""
        ])

        self.filter1 = FilterBuilder(syote=self.fake_input)
        self.filter2 = FilterBuilder(syote=self.fake_input2)

    def test_initial_filter_empty(self):
        self.assertEqual(self.filter1.read_input(), {})
        self.assertEqual(self.filter2.read_input(), {"key":"juup"})

    def test_get_value_of_input(self):
        self.assertEqual(self.filter1.get_value(), "")

    def test_get_key_value_of_input(self):
        self.assertEqual(self.filter1.get_key(), "")