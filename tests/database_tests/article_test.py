from unittest import TestCase

from src.app import app
from src.references.article import Article

class ArticleDatabaseTest(TestCase):
    def setUp(self):
        with app.app_context():
            from src.utils.database import reset_database
            reset_database()

    def test_article_get_all_returns_None_if_no_articles_in_database(self):
        with app.app_context():
            from src.db import article
            result = article.get_all()
        self.assertEqual(result, None)

    def test_article_insert_one_with_correct_object_is_correctly_saved_to_db(self):
        test_article = {
            "key": "key",
            "author": "Me",
            "title": "My best book", 
            "year": 2023,
            "journal": "Mitä tä tarkottaa :D", 
            "volume": 3,
            "pages": "200-300"
        }

        with app.app_context():
            from src.db import article
            pre_result = article.get_all()
            article.insert_one(test_article)
            result = article.get_all()

        if result:
            self.assertEqual(pre_result, None)
            self.assertIsInstance(result[0], Article)

            self.assertEqual(result[0].key, "key")
            self.assertEqual(result[0].author, "Me")
            self.assertEqual(result[0].title, "My best book")
            self.assertEqual(result[0].year, 2023)
            self.assertEqual(result[0].journal, "Mitä tä tarkottaa :D")
            self.assertEqual(result[0].volume, 3)
            self.assertEqual(result[0].pages, "200-300")
        else:
            raise AssertionError("No result from database")

    def test_article_get_all_multiple_references_returns_all(self):
        test_article = {
            "key": "key",
            "author": "Me",
            "title": "My best book", 
            "year": 2023,
            "journal": "Mitä tä tarkottaa :D", 
            "volume": 3,
            "pages": "200-300"
        }

        other_test_article = {
            "key": "otherkey",
            "author": "You",
            "title": "Your best book", 
            "year": 2020,
            "journal": "Edelleenkään en tiedä", 
            "volume": 1,
            "pages": "100-200"
        }

        with app.app_context():
            from src.db import article
            article.insert_one(test_article)
            article.insert_one(other_test_article)
            result = article.get_all()

        if result:
            self.assertEqual(len(result), 2)
            self.assertEqual(result[0].author, "Me")
            self.assertEqual(result[1].author, "You")
        else:
            raise AssertionError("No result from database")
