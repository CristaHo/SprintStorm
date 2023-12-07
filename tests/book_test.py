import unittest
from src.references.book import Book

class TestBook(unittest.TestCase):
    def setUp(self):
        self.reference = Book(fields={
            "key": "Someuniquekey", "author":"mk", "title":"idk","year":"2001",
            "publisher":"publisher","address":"address"})

    def test_author_takes_constructor_value(self):
        self.assertEqual(self.reference.author, "mk")

    def test_set_author_changes_author(self):
        self.reference.author = "lk"
        self.assertEqual(self.reference.author,"lk")

    def test_title_takes_constructor_value(self):
        self.assertEqual(self.reference.title,"idk")

    def test_set_title_changes_title(self):
        self.reference.title = "ik"
        self.assertEqual(self.reference.title, "ik")

    def test_year_takes_constructor_value(self):
        self.assertEqual(self.reference.year,"2001")

    def test_set_year_changes_year(self):
        self.reference.year = "2005"
        self.assertEqual(self.reference.year, "2005")

    def test_get_type_returns_book(self):
        self.assertIsInstance(self.reference, Book)

    def test_publisher_takes_constructor_value(self):
        self.reference.publisher = "publisher"
        self.assertEqual(self.reference.publisher, "publisher")

    def test_set_publisher_changes_publisher(self):
        self.reference.publisher = "publisher2"
        self.assertEqual(self.reference.publisher, "publisher2")

    def test_bibtex_str(self):
        example_str = """@book{Someuniquekey
    title = idk
    author = mk
    year = 2001
    publisher = publisher
}"""
        bibtex_str = self.reference.bibtex_str()
        self.assertEqual(bibtex_str, example_str)
