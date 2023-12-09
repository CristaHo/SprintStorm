from unittest import TestCase
from sqlalchemy import text
from src.app import app

class TestViewReferences(TestCase):
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
        test_article_reference = {
                "reftype": "article",
                "key": "mää",
                "author": "Minä itse", 
                "title": "Hieno artikkeli", 
                "year": 2022, 
                "journal": "Mikä tää on :D",
                "volume": 3,
                "pages": "20-30",
                "category": 1
                }

        self.app.post("/register", data=test_user_register)
        self.app.post("/login", data=test_user_login)
        self.app.post("/add_category", data=test_category)
        self.app.post("/add_reference", data=test_book_reference)
        self.app.post("/add_reference", data=test_article_reference)

        # user_id was saved to session = user logged in
        with self.app.session_transaction() as s:
            self.assertEqual(s["uid"], 1)

    def test_view_references_works_with_no_references(self):
        with app.app_context():
            from src.utils.database import db
            db.session.execute(text("DELETE FROM book"))
            db.session.execute(text("DELETE FROM article"))
            db.session.commit()

        response = self.app.get("/view_reference")
        self.assertFalse(b'Hieno kirja' in response.data)
        self.assertFalse(b'Hieno artikkeli' in response.data)
        self.assertFalse(b'2022' in response.data)
        self.assertFalse(b'2023' in response.data)

    def test_view_references_redirects_as_not_logged_user(self):
        with self.app.session_transaction() as s:
            s["uid"] = None

        response = self.app.get("/view_reference", follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'Login needed to view this page' in response.data)

    def test_download_references_as_logged_in_user(self):
        response = self.app.get("/view_reference/download", follow_redirects=True)
        with app.app_context():
            import src.db.reference as reference
            refs = reference.get_all(1)
            bibtex_str = reference.get_references_in_bibtex(refs)

        self.assertEqual(response.data, bytes(bibtex_str, "utf-8"))

    def test_download_references_should_redirect_for_logged_out_user(self):
        with self.app.session_transaction() as s:
            s["uid"] = None

        response = self.app.get("/view_reference/download", follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'Login needed' in response.data)
