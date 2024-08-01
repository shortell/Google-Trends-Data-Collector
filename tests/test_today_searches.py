import unittest
import datetime


from database.google_trends.today_searches import *
from database.db_utils import *
from utils.datetime_utils import create_datetime, datetime_to_string


class TestTodaySearches(unittest.TestCase):
    def setUp(self):
        drop_schema()
        create_schema()
        seed_database()

    def tearDown(self):
        drop_schema()
        create_schema()

    def test_add_today_search_true(self):
        timestamp = create_datetime(2024, 4, 16, 7)
        timestamp_str = datetime_to_string(timestamp)
        expected = True
        actual = add_today_search(1, 1, timestamp_str, 1)
        self.assertEqual(actual, expected)

    def test_add_today_search_false(self):
        timestamp = create_datetime(2024, 4, 16, 4)
        timestamp_str = datetime_to_string(timestamp)
        expected = False
        actual = add_today_search(1, 1, timestamp_str, 1)
        self.assertEqual(actual, expected)
