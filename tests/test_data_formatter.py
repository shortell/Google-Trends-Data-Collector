import unittest
import json

from input.google_trends_fetcher import fetch_trending_searches, fetch_realtime_trending_searches, fetch_today_searches
from utils.data_formatter import *

class TestDataFormatter(unittest.TestCase):

    def test_format_trending_searches_email(self):
        data = fetch_trending_searches('united_states')
        json_data = json.loads(data.to_json())
        trending_searches = json_data["0"]
        actual, body = format_trending_searches_email(trending_searches)
        expected = True
        self.assertEqual(actual, expected)
        print(body)

    def test_format_realtime_trending_searches_email(self):
        data = fetch_realtime_trending_searches('US')
        json_data = json.loads(data.to_json())
        realtime_trending_searches = json_data['entityNames']
        actual, body = format_realtime_trending_searches_email(realtime_trending_searches)
        expected = True
        self.assertEqual(actual, expected)
        print(body)

    def test_format_today_searches_email(self):
        data = fetch_today_searches('US')
        json_data = json.loads(data.to_json())
        today_searches = json_data['query']
        actual, body = format_today_searches_email(today_searches)
        expected = True
        self.assertEqual(actual, expected)
        print(body)
    