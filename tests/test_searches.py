import unittest


from database.google_trends.searches import *
from database.db_utils import *


class TestSearches(unittest.TestCase):

    def setUp(self):
        drop_schema()
        create_schema()
        seed_database()

    def tearDown(self):
        drop_schema()
        create_schema()

    def test_add_search_true(self):
        actual = add_search('Apple')
        expected = True
        self.assertEqual(actual, expected)

    def test_add_search_false(self):
        actual = add_search('augmented reality')
        expected = False
        self.assertEqual(actual, expected)

    def test_get_search_id_valid(self):
        actual = get_search_id('Artificial Intelligence')
        expected = 1
        self.assertEqual(actual, expected)

    def test_get_search_id_invalid(self):
        actual = get_search_id('Apple')
        expected = None
        self.assertEqual(actual, expected)

    def test_get_search_by_id_valid(self):
        actual = get_search_by_id(1)
        expected = (1, 'Artificial Intelligence')
        self.assertEqual(actual, expected)

    def test_get_search_by_id_invalid(self):
        actual = get_search_by_id(44)
        expected = None
        self.assertEqual(actual, expected)

    def test_get_all_searches(self):
        actual = get_all_searches()
        expected = [
            (1, 'Artificial Intelligence'),
            (2, 'Machine Learning'),
            (3, 'Self-Driving Cars'),
            (4, '#DeepLearning'),
            (5, '3D Printing'),
            (6, 'Virtual Reality'),
            (7, 'Quantum Computing'),
            (8, 'Lebron James'),
            (9, 'Data Science'),
            (10, 'Blockchain'),
            (11, 'augmented reality'),
            (12, '  Cybersecurity  '),
            (13, '<html>'),
            (14, 'Bitcoin ðŸš€'),
            (15, 'Big Data anÃ¡lisis'),
            (16, 'http://example.com'),
            (17, 'SQL Injection'),
            (18, 'Machine Learning sucks'),
            (19, 'Tesla'),
            (20, 'Elon Musk')
        ]
        self.assertEqual(actual, expected)


