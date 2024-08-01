import unittest


from database.db_utils import *
from utils.data_collection import *
from database.google_trends.countries import add_country_from_file
from database.google_trends.suggestions import get_suggestions_by_search_id
from utils.data_formatter import *


class TestDataCollection(unittest.TestCase):

    def setUp(self):
        drop_schema()
        create_schema()
        add_country_from_file()

    def tearDown(self):
        drop_schema()
        create_schema()

    def test_store_trending_searches_successful(self):
        actual = store_trending_searches(1, 'united_states')
        not_expected = 0
        self.assertNotEqual(len(actual), not_expected)

    def test_store_trending_searches_unsuccessful(self):
        actual = store_trending_searches(2, 'foobar')
        expected = None
        self.assertEqual(actual, expected)

    def test_store_realtime_trending_searches_successful(self):
        actual = store_realtime_trending_searches(1, 'US')
        not_expected = 0
        self.assertNotEqual(len(actual), not_expected)

    def test_store_realtime_trending_searches_false(self):
        actual = store_realtime_trending_searches(2, "Foobar")
        expected = None
        self.assertEqual(actual, expected)

    def test_store_today_searches_successful(self):
        actual = store_today_searches(1, 'US')
        not_expected = 0
        self.assertNotEqual(len(actual), not_expected)

    def test_store_today_searches_unsuccessful(self):
        actual = store_today_searches(2, "Foobar")
        expected = None
        self.assertEqual(actual, expected)

    def test_store_suggestions(self):
        drop_schema()
        create_schema()
        seed_database()
        actual, data = store_suggestions(20, 'Elon Musk')
        self.assertEqual(actual, True)
        actual = len(get_suggestions_by_search_id(20))
        print(data)
        self.assertNotEqual(actual, 0)

    def test_store_all_searches(self):
        responses = store_all_searches()
        for record in responses:
            print(record)
        print(responses)
