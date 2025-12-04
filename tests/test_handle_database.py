import unittest
from unittest.mock import Mock
from database import DatabaseHandler


class TestDatabaseHandler(unittest.TestCase):
    def setUp(self):
        self.db_mock = Mock()
        self.db_handler = DatabaseHandler(self.db_mock)
    def test_add_calls_db_add(self):
        citation_mock = Mock()
        self.db_handler.add(citation_mock)
        self.db_mock.add.assert_called_once_with(citation_mock)

    def test_hae_viitteet(self):
        filt = {"author": "author"}
        self.db_handler.hae_viitteet(filt)
        self.db_mock.hae_viitteet.assert_called_once_with(filt)

    def test_get_all(self):
        self.db_handler.get_all()
        self.db_mock.get_all.assert_called_once()
