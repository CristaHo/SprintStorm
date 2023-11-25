import unittest
from src.references.book import Book

class TestBook(unittest.TestCase):
    def setUp(self):
        self.reference = Book(
            author = "mk", title="idk",year = "2001",
            publisher="publisher",address="address")

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
        type_as_string = str(type(self.reference))
        self.assertIn("class", type_as_string)
        self.assertIn("book", type_as_string)
        self.assertIn("Book", type_as_string)

    def test_publisher_takes_constructor_value(self):
        self.reference.publisher = "publisher"
        self.assertEqual(self.reference.publisher, "publisher")

    def test_set_publisher_changes_publisher(self):
        self.reference.publisher = "publisher2"
        self.assertEqual(self.reference.publisher, "publisher2")

    def test_address_takes_constructor_value(self):
        self.reference.address = "address"
        self.assertEqual(self.reference.address, "address")

    def test_set_address_changes_address(self):
        self.reference.address = "address2"
        self.assertEqual(self.reference.address, "address2")
