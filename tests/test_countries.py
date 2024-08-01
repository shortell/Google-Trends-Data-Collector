import unittest


from database.google_trends.countries import *
from database.db_utils import *


class TestCountries(unittest.TestCase):

    def setUp(self):
        drop_schema()
        create_schema()
        seed_database()

    def tearDown(self):
        drop_schema()
        create_schema()

    def test_get_country_data_from_file_successful(self):
        actual = get_country_data_from_file('United States')
        expected = {
            'two_letter_code': 'US',
            'camel_case_name': 'united_states'
        }
        self.assertEqual(actual, expected)

    def test_get_country_data_from_file_unsuccessful(self):
        actual = get_country_data_from_file('Foobar')
        expected = None
        self.assertEqual(actual, expected)

    def test_add_country_true(self):
        actual = add_country_from_file('Australia')
        expected = True
        self.assertEqual(actual, expected)

    def test_add_country_false_invalid(self):
        actual = add_country_from_file('Foobar')
        expected = False
        self.assertEqual(actual, expected)

    def test_add_country_false_duplicate(self):
        actual = add_country_from_file('United States')
        expected = False
        self.assertEqual(actual, expected)

    def test_get_countries(self):
        actual = get_countries()
        expected = [
            (1, 'United States', 'US', 'united_states'),
            (2, 'Canada', 'CA', 'canada')
        ]
        self.assertEqual(actual, expected)

    def test_get_country_by_name(self):
        actual = get_country_by_name('United States')
        expected = (1, 'United States', 'US', 'united_states')
        self.assertEqual(actual, expected)

