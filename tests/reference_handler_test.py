import unittest
from src.utils.reference_handler import ReferenceHandler
from src.references.reference import Reference
from src.references.article import Article
from src.references.book import Book

class TestReferenceHandler(unittest.TestCase):
    def setUp(self):
        self.reference_handler = ReferenceHandler()

    def test_reference_handler_exists(self):
        self.assertNotEqual(self.reference_handler, None)

    def test_reference_handler_has_empty_list_of_references(self):
        self.assertEqual(self.reference_handler.get_references(), [])

    def test_create_reference_creates_reference(self):
        self.reference_handler.create_reference("reference", {"author": "mk", "title": "idk", "year": "2001"})
        self.assertEqual(len(self.reference_handler.get_references()), 1)

    def test_create_reference_creates_reference_with_correct_values(self):
        self.reference_handler.create_reference("reference", {"author": "mk", "title": "idk", "year": "2001"})
        self.assertEqual(self.reference_handler.get_references()[0].author, "mk")
        self.assertEqual(self.reference_handler.get_references()[0].title, "idk")
        self.assertEqual(self.reference_handler.get_references()[0].year, "2001")

    def test_create_reference_creates_reference_with_correct_type(self):
        self.reference_handler.create_reference("reference", {"author": "mk", "title": "idk", "year": "2001"})
        self.assertEqual(type(self.reference_handler.get_references()[0]), Reference)

    def test_create_reference_creates_article_with_correct_values(self):
        self.reference_handler.create_reference("article", {"author": "mk", "title": "idk", "year": "2001", "journal": "journal", "volume": "volume", "number": "number", "pages": "pages"})
        self.assertEqual(self.reference_handler.get_references()[0].author, "mk")
        self.assertEqual(self.reference_handler.get_references()[0].title, "idk")
        self.assertEqual(self.reference_handler.get_references()[0].year, "2001")
        self.assertEqual(self.reference_handler.get_references()[0].journal, "journal")
        self.assertEqual(self.reference_handler.get_references()[0].volume, "volume")
        self.assertEqual(self.reference_handler.get_references()[0].number, "number")
        self.assertEqual(self.reference_handler.get_references()[0].pages, "pages")

    def test_create_reference_creates_article_with_correct_type(self):
        self.reference_handler.create_reference("article", {"author": "mk", "title": "idk", "year": "2001", "journal": "journal", "volume": "volume", "number": "number", "pages": "pages"})
        self.assertEqual(type(self.reference_handler.get_references()[0]), Article)

    def test_create_reference_creates_book_with_correct_values(self):
        self.reference_handler.create_reference("book", {"author": "mk", "title": "idk", "year": "2001", "publisher": "publisher", "address": "address"})
        self.assertEqual(self.reference_handler.get_references()[0].author, "mk")
        self.assertEqual(self.reference_handler.get_references()[0].title, "idk")
        self.assertEqual(self.reference_handler.get_references()[0].year, "2001")
        self.assertEqual(self.reference_handler.get_references()[0].publisher, "publisher")
        self.assertEqual(self.reference_handler.get_references()[0].address, "address")

    def test_create_reference_creates_book_with_correct_type(self):
        self.reference_handler.create_reference("book", {"author": "mk", "title": "idk", "year": "2001", "publisher": "publisher", "address": "address"})
        self.assertEqual(type(self.reference_handler.get_references()[0]), Book)
