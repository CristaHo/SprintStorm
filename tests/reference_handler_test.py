from flask import Flask
from flask_testing import TestCase
from src.utils.reference_handler import ReferenceHandler
from src.references.reference import Reference
from src.references.article import Article
from src.references.book import Book
from src.utils.database import db
from src.utils import config as conf


class TestReferenceHandler(TestCase):
    def create_app(self):
        self.reference_handler = ReferenceHandler()
        app = Flask(__name__)
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = conf.db_url() # Use a separate test database
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        # Initialize SQLAlchemy with the app context
        db.init_app(app)

        return app

    def setUp(self):
        # Create the test database tables before each test
        db.create_all()

    def tearDown(self):
        # Drop the test database tables after each test
        db.session.remove()
        db.drop_all()        

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
        self.assertEqual(self.reference_handler.get_references()[0].year, 2001)

    def test_create_reference_creates_reference_with_correct_type(self):
        self.reference_handler.create_reference(reftype="reference", fields={"author": "mk", "title": "idk", "year": "2001"})
        self.assertIsInstance(self.reference_handler.get_references()[0], Reference)

    def test_create_reference_creates_article_with_correct_values(self):
        self.reference_handler.create_reference(reftype="article", fields={"author": "mk", "title": "idk", "year": "2001", "journal": "journal", "volume": 1, "pages": "pages"})
        self.assertEqual(self.reference_handler.get_references()[0].author, "mk")
        self.assertEqual(self.reference_handler.get_references()[0].title, "idk")
        self.assertEqual(self.reference_handler.get_references()[0].year, 2001)
        self.assertEqual(self.reference_handler.get_references()[1].journal, "journal")
        self.assertEqual(self.reference_handler.get_references()[1].volume, 1)
        self.assertEqual(self.reference_handler.get_references()[1].pages, "pages")

    def test_create_reference_creates_article_with_correct_type(self):
        self.reference_handler.create_reference(reftype="article", fields={"author": "mk", "title": "idk", "year": "2001", "journal": "journal", "volume": 1, "pages": "pages"})
        self.assertIsInstance(self.reference_handler.get_references()[1], Article)

    def test_create_reference_creates_book_with_correct_values(self):
        self.reference_handler.create_reference(reftype="book", fields={"author": "mk", "title": "idk", "year": "2001", "publisher": "publisher"})
        self.assertEqual(self.reference_handler.get_references()[0].author, "mk")
        self.assertEqual(self.reference_handler.get_references()[0].title, "idk")
        self.assertEqual(self.reference_handler.get_references()[0].year, 2001)
        self.assertEqual(self.reference_handler.get_references()[1].publisher, "publisher")

    def test_create_reference_creates_book_with_correct_type(self):
        self.reference_handler.create_reference(reftype="book", fields={"author": "mk", "title": "idk", "year": "2001", "publisher": "publisher"})
        self.assertIsInstance(self.reference_handler.get_references()[1], Book)
