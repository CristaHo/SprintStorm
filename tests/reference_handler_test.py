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
        self.reference_handler.create_reference(reftype="reference", fields={"author": "mk", "title": "idk", "year": "2001"})
        self.assertEqual(len(self.reference_handler.get_references()), 1)

    def test_create_reference_creates_reference_with_correct_values(self):
        self.reference_handler.create_reference(reftype="reference", fields={"author": "mk", "title": "idk", "year": "2001"})
        self.assertEqual(self.reference_handler.get_references()[0].author, "mk")
        self.assertEqual(self.reference_handler.get_references()[0].title, "idk")
        self.assertEqual(self.reference_handler.get_references()[0].year, "2001")

    def test_create_reference_creates_reference_with_correct_type(self):
        self.reference_handler.create_reference(reftype="reference", fields={"author": "mk", "title": "idk", "year": "2001"})
        self.assertIsInstance(self.reference_handler.get_references()[0], Reference)

    def test_create_reference_creates_article_with_correct_values(self):
        self.reference_handler.create_reference(reftype="article", fields={"author": "mk", "title": "idk", "year": "2001", "journal": "journal", "volume": "volume", "number": "number", "pages": "pages"})
        self.assertEqual(self.reference_handler.get_references()[0].author, "mk")
        self.assertEqual(self.reference_handler.get_references()[0].title, "idk")
        self.assertEqual(self.reference_handler.get_references()[0].year, "2001")
        self.assertEqual(self.reference_handler.get_references()[0].journal, "journal")
        self.assertEqual(self.reference_handler.get_references()[0].volume, "volume")
        self.assertEqual(self.reference_handler.get_references()[0].number, "number")
        self.assertEqual(self.reference_handler.get_references()[0].pages, "pages")

    def test_create_reference_creates_article_with_correct_type(self):
        self.reference_handler.create_reference(reftype="article", fields={"author": "mk", "title": "idk", "year": "2001", "journal": "journal", "volume": "volume", "number": "number", "pages": "pages"})
        self.assertIsInstance(self.reference_handler.get_references()[0], Article)

    def test_create_reference_creates_book_with_correct_values(self):
        self.reference_handler.create_reference(reftype="book", fields={"author": "mk", "title": "idk", "year": "2001", "publisher": "publisher", "address": "address"})
        self.assertEqual(self.reference_handler.get_references()[0].author, "mk")
        self.assertEqual(self.reference_handler.get_references()[0].title, "idk")
        self.assertEqual(self.reference_handler.get_references()[0].year, "2001")
        self.assertEqual(self.reference_handler.get_references()[0].publisher, "publisher")
        self.assertEqual(self.reference_handler.get_references()[0].address, "address")

    def test_create_reference_creates_book_with_correct_type(self):
        self.reference_handler.create_reference(reftype="book", fields={"author": "mk", "title": "idk", "year": "2001", "publisher": "publisher", "address": "address"})
        self.assertIsInstance(self.reference_handler.get_references()[0], Book)

    def test_get_bibtex_returns_empty_string_when_no_references(self):
        self.assertEqual(self.reference_handler.get_references_in_bibtex(),"")

    def test_get_bibtex_returns_list_of_bibtexes(self):
        self.reference_handler.create_reference(reftype="article", fields={"author": "j", "title": "lf", "year": "1999", "journal": "smt", "volume": "5", "number": "4", "pages": "123"})
        self.reference_handler.create_reference(reftype="book", fields={"author": "na", "title": "4", "year": "2012", "publisher": "pb", "address": "home"})
        test_string = self.reference_handler.get_references()[0].bibtex_str()+'\n\n'+self.reference_handler.get_references()[1].bibtex_str()
        self.assertEqual(test_string,self.reference_handler.get_references_in_bibtex())
