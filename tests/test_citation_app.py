import unittest
from unittest.mock import Mock
from citation_app import CitationApp
from database import DatabaseHandler


class TestCitationApp(unittest.TestCase):
    def setUp(self):
        self.db = DatabaseHandler()
        self.app = CitationApp(db=self.db,
                               input_=lambda x: "q",
                               print_=lambda x: None
                               )

    def test_run_quit_immediately(self):
        # Test that the app can run and quit immediately
        self.app.run()  # Should not raise any exceptions

    def test_syote_1_add_citation(self):
        inputs = iter(["1", "q"])
        outputs = []
        prompts = []
        lomake = Mock()
        citation_mock = Mock()
        lomake.tayta_lomake = Mock(return_value=citation_mock)

        def mock_input(prompt):
            prompts.append(prompt)
            return next(inputs)

        def mock_print(output):
            outputs.append(output)

        db_mock = Mock()
        app = CitationApp(db=db_mock, input_=mock_input, print_=mock_print, lomake=lomake)
        app.run()

        lomake.tayta_lomake.assert_called_once()
        db_mock.add.assert_called_once_with(citation_mock)

    def test_syote_1_handles_throw_from_database(self):
        inputs = iter(["1", "q"])
        outputs = []
        prompts = []
        lomake = Mock()
        citation_mock = Mock()
        lomake.tayta_lomake = Mock(return_value=citation_mock)

        def mock_input(prompt):
            prompts.append(prompt)
            return next(inputs)

        def mock_print(output):
            outputs.append(output)

        app = CitationApp(db=self.db, input_=mock_input, print_=mock_print, lomake=lomake)
        app.run()

        lomake.tayta_lomake.assert_called_once()
        self.assertIn("Not a Citation object", outputs)

    def test_syote_2_list_citations(self):
        inputs = iter(["2", "q"])
        outputs = []
        prompts = []

        def mock_input(prompt):
            prompts.append(prompt)
            return next(inputs)

        def mock_print(output):
            outputs.append(output)

        citation1 = Mock()
        citation1.__str__ = Mock(return_value="Citation 1")
        citation2 = Mock()
        citation2.__str__ = Mock(return_value="Citation 2")

        db_mock = Mock()
        db_mock.get_all.return_value = [citation1, citation2]

        app = CitationApp(db=db_mock, input_=mock_input, print_=mock_print)
        app.run()

        db_mock.get_all.assert_called_once()
        self.assertIn("Citation 1", outputs)
        self.assertIn("Citation 2", outputs)

    def test_syote_3_filter_citations(self):
        inputs = iter(["3", "q"])
        outputs = []
        prompts = []

        def mock_input(prompt):
            prompts.append(prompt)
            return next(inputs)

        def mock_print(output):
            outputs.append(output)

        filter_mock = Mock()
        filter_builder = Mock()
        db_mock = Mock()
        citation_mock = Mock()
        citation_mock.to_bibtex = Mock(return_value="BibTeX Entry")
        db_mock.hae_viitteet.return_value = [citation_mock]
        filter_builder.read_input = Mock(return_value=filter_mock)

        app = CitationApp(db=db_mock, input_=mock_input,
                        print_=mock_print,
                        filter_builder=filter_builder
                        )
        app.run()

        filter_builder.read_input.assert_called_once()
        db_mock.hae_viitteet.assert_called_once_with(filter_mock)
        self.assertIn("BibTeX Entry", outputs)

    def test_4_syote_4_prints_bibtex(self):
        inputs = iter(["4", "q"])
        outputs = []
        prompts = []

        def mock_input(prompt):
            prompts.append(prompt)
            return next(inputs)

        def mock_print(output):
            outputs.append(output)

        citation_mock = Mock()
        citation_mock.to_bibtex = Mock(return_value="BibTeX Entry")

        db_mock = Mock()
        db_mock.get_all.return_value = [citation_mock]

        app = CitationApp(db=db_mock, input_=mock_input, print_=mock_print)
        app.run()

        db_mock.get_all.assert_called_once()
        self.assertIn("BibTeX Entry", outputs)

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
        inputs = iter(["6", "testfile.json", "q"])
        outputs = []
        prompts = []

        def mock_input(prompt):
            prompts.append(prompt)
            return next(inputs)

        def mock_print(output):
            outputs.append(output)
        db_mock = Mock()
        app = CitationApp(db=db_mock, input_=mock_input, print_=mock_print)
        app.run()

        db_mock.load_from_file.assert_called_once_with("testfile.json")
        sync_message_found = any("Synkronoitu viitteet tiedostosta." in o for o in outputs)
        self.assertTrue(sync_message_found)

    def test_syote_7_saves_database_to_file(self):
        inputs = iter(["7", "testfile", "q"])
        outputs = []
        prompts = []

        def mock_input(prompt):
            prompts.append(prompt)
            return next(inputs)

        def mock_print(output):
            outputs.append(output)

        db_mock = Mock()

        app = CitationApp(db=db_mock, input_=mock_input, print_=mock_print)
        app.run()

        db_mock.save_to_file.assert_called_once_with("testfile.json")

    def test_unknown_syote_shows_instructions(self):
        inputs = iter(["unknown", "q"])
        outputs = []
        prompts = []

        def mock_input(prompt):
            prompts.append(prompt)
            return next(inputs)

        def mock_print(output):
            outputs.append(output)

        app = CitationApp(db=self.db, input_=mock_input, print_=mock_print)
        app.run()

        instructions_found = any("q = Poistu" in o for o in outputs)
        self.assertTrue(instructions_found)
