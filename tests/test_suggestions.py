import unittest


from database.google_trends.suggestions import *
from database.db_utils import *


class TestSuggestions(unittest.TestCase):

    def setUp(self):
        drop_schema()
        create_schema()
        seed_database()

    def tearDown(self):
        drop_schema()
        create_schema()

    def test_add_suggestion_true(self):
        actual = add_suggestion('Google Gemini', 1)
        expected = True
        self.assertEqual(actual, expected)

    def test_add_suggestion_false(self):
        actual = add_suggestion('ChatGPT', 1)
        expected = False
        self.assertEqual(actual, expected)

    def test_get_suggestions_by_search_id(self):
        actual = get_suggestions_by_search_id(1)
        expected = [
            ('ChatGPT',),
            ('Neural Network',)
        ]
        self.assertEqual(actual, expected)


