import unittest
from src.utils.environment import read_postgres_url

class TestEnvironment(unittest.TestCase):
    def test_read_postgres_url(self):
        url = read_postgres_url()
        self.assertIsNone(url)
        self.assertIn("postgresql://", url)