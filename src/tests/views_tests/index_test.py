from unittest import TestCase
from src.app import app

class TestIndexViews(TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_app_test_client_works(self):
        response = self.app.get("/ping")
        self.assertTrue(b'{"message":"pong"}' in response.data)

    def test_index_page_contains_title(self):
        response = self.app.get("/")
        self.assertTrue(b'Bibtex maker' in response.data)
        self.assertTrue(b'Login' in response.data)
        self.assertTrue(b'Register' in response.data)
