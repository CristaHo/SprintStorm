from unittest import TestCase
from sqlalchemy import text
from src.app import app

class TestAddReferences(TestCase):
    def setUp(self):
        self.app = app.test_client()
        with app.app_context():
            from src.utils.database import reset_database
            reset_database()

        test_user_register = {
                "username": "test",
                "password1": "1234",
                "password2": "1234"
                }
        test_user_login = {
                "username": "test",
                "password": "1234",
                }
        test_category = {
                "name": "teologia",
                }

        self.app.post("/register", data=test_user_register)
        self.app.post("/login", data=test_user_login)
        self.app.post("/add_category", data=test_category)

        # user_id was saved to session = user logged in
        with self.app.session_transaction() as s:
            self.assertEqual(s["uid"], 1)

    def test_add_reference_page_is_shown_as_logged_user(self):
        response = self.app.get("/add_reference")

        self.assertEqual(response.status_code, 200)
        self.assertFalse(b'Login needed to view this page' in response.data)
        self.assertTrue(b'Choose reference type' in response.data)

    def test_login_page_is_shown_as_not_logged_user(self):
        with self.app.session_transaction() as s:
            s["uid"] = None

        response = self.app.get("/add_reference", follow_redirects=True)

        print(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'Login needed to view this page' in response.data)
        self.assertFalse(b'Choose reference type' in response.data)

    def test_choosing_reference_type_book(self):
        response = self.app.get("/choose_reference?ref=book")
        self.assertTrue(b'Key:' in response.data)
        self.assertTrue(b'Author:' in response.data)
        self.assertTrue(b'Title:' in response.data)
        self.assertTrue(b'Year:' in response.data)
        self.assertTrue(b'Publisher:' in response.data)
        self.assertTrue(b'Address:' in response.data)
        self.assertTrue(b'Category:' in response.data)

    def test_choosing_reference_type_article(self):
        response = self.app.get("/choose_reference?ref=article")
        self.assertTrue(b'Key:' in response.data)
        self.assertTrue(b'Author:' in response.data)
        self.assertTrue(b'Title:' in response.data)
        self.assertTrue(b'Year:' in response.data)
        self.assertTrue(b'Journal:' in response.data)
        self.assertTrue(b'Volume:' in response.data)
        self.assertTrue(b'Pages:' in response.data)
        self.assertTrue(b'Category:' in response.data)

    def test_add_reference_book_with_correct_information(self):
        test_book_reference = {
                "reftype": "book",
                "key": "möö",
                "author": "Minä itse", 
                "title": "Hieno kirja", 
                "year": 2023, 
                "publisher": "Otava",
                "address": "Jokukatu 13",
                "category": 1,
                }
        response = self.app.post("/add_reference", data=test_book_reference)
        self.assertEqual(response.status_code, 302)
        with app.app_context():
            from src.utils.database import db
            result = db.session.execute(text("SELECT id FROM book")).fetchone()
            if result:
                self.assertEqual(len(result), 1)

    def test_add_reference_article_with_correct_information(self):
        test_article_reference = {
                "reftype": "article",
                "key": "möö",
                "author": "Minä itse", 
                "title": "Hieno artikkeli", 
                "year": 2023, 
                "journal": "Mikä tää on :D",
                "volume": 3,
                "pages": "20-30",
                "category": 1
                }
        response = self.app.post("/add_reference", data=test_article_reference)
        self.assertEqual(response.status_code, 302)
        with app.app_context():
            from src.utils.database import db
            result = db.session.execute(text("SELECT id FROM article")).fetchone()
            if result:
                self.assertEqual(len(result), 1)

    def test_add_reference_book_with_missing_user_id(self):
        with self.app.session_transaction() as s:
            s["uid"] = None

        test_book_reference = {
                "reftype": "book",
                "key": "möö",
                "author": "Minä itse", 
                "title": "Hieno kirja", 
                "year": 2023, 
                "publisher": "Otava",
                "address": "Jokukatu 13",
                "category": 1,
                }
        response = self.app.post("/add_reference", data=test_book_reference)
        self.assertEqual(response.status_code, 200)
        with app.app_context():
            from src.utils.database import db
            result = db.session.execute(text("SELECT id FROM book")).fetchone()
            self.assertEqual(result, None)
        self.assertTrue(b'User not logged in' in response.data)

    def test_add_reference_article_with_missing_user_id(self):
        with self.app.session_transaction() as s:
            s["uid"] = None

        test_article_reference = {
                "reftype": "article",
                "key": "möö",
                "author": "Minä itse", 
                "title": "Hieno artikkeli", 
                "year": 2023, 
                "journal": "Mikä tää on :D",
                "volume": 3,
                "pages": "20-30",
                "category": 1
                }
        response = self.app.post("/add_reference", data=test_article_reference)
        self.assertEqual(response.status_code, 200)
        with app.app_context():
            from src.utils.database import db
            result = db.session.execute(text("SELECT id FROM article")).fetchone()
            self.assertEqual(result, None)
        self.assertTrue(b'User not logged in' in response.data)
