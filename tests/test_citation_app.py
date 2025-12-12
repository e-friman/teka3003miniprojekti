import unittest
from citation_app import CitationApp
from database import DatabaseHandler

class TestCitationApp(unittest.TestCase):
    def setUp(self):
        self.db = DatabaseHandler()
        self.app = CitationApp(db=self.db, input_=lambda x: "q", print_=lambda x: None)

    def tearDown(self):
        # Reset or clear the database if needed
        if hasattr(self.db, "clear"):
            self.db.clear()

    def test_run_quit_immediately(self):
        # Test that the app can run and quit immediately
        self.app.run()  # Should not raise any exceptions

    def test_syote_5_creates_bibtex_file(self):
        inputs = iter(["5", "testfile", "q"])
        outputs = []
        prompts = []

        def mock_input(prompt):
            prompts.append(prompt)
            return next(inputs)

        def mock_print(output):
            outputs.append(output)

        citation_app_5 = CitationApp(db=self.db, input_=mock_input, print_=mock_print)
        citation_app_5.run()

        # Check if the prompt for filename was shown
        self.assertIn("Anna tiedoston nimi: ", prompts)

    def test_syote_6_synchronizes_references(self):
        inputs = iter(["6", "testfile", "q"])
        outputs = []
        prompts = []

        def mock_input(prompt):
            prompts.append(prompt)
            return next(inputs)

        def mock_print(output):
            outputs.append(output)

        app = CitationApp(db=self.db, input_=mock_input, print_=mock_print)
        app.run()

        # Check if synchronization message was printed
        sync_message_found = any("Synkronoitu viitteet tiedostosta." in o for o in outputs)
        self.assertTrue(sync_message_found)
