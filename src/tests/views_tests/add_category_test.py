from unittest import TestCase
from sqlalchemy import text
from src.app import app

class TestAddCategory(TestCase):
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

        self.app.post("/register", data=test_user_register)
        self.app.post("/login", data=test_user_login)

        # user_id was saved to session = user logged in
        with self.app.session_transaction() as s:
            self.assertEqual(s["uid"], 1)

    def is_empty_database(self):
        with app.app_context():
            from src.utils.database import db
            result = db.session.execute(text("SELECT name, user_id FROM category")).fetchone()
            self.assertEqual(result, None)

    def test_add_category_GET_shows_correct_information(self):
        response = self.app.get("/add_category")
        self.assertTrue(b'Add category' in response.data)
        self.assertTrue(b'Name:' in response.data)

    def test_add_category_with_correct_information(self):
        test_category = {
                "name": "teologia",
                }
        response = self.app.post("/add_category", data=test_category)

        self.assertEqual(response.status_code, 200)
        with app.app_context():
            from src.utils.database import db
            result = db.session.execute(text("SELECT name, user_id FROM category")).fetchone()
            if result:
                print(result)
                self.assertEqual(result[0], "teologia")
                self.assertEqual(result[1], 1)

    def test_add_category_with_missing_name(self):
        test_category = {
                "name": "",
                }
        response = self.app.post("/add_category", data=test_category)
        print(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'Category name not set' in response.data)
        self.is_empty_database()

    def test_add_category_with_missing_user_id(self):
        # remove user_id from session = logout
        with self.app.session_transaction() as s:
            s["uid"] = None

        test_category = {
                "name": "teologia",
                }
        response = self.app.post("/add_category", data=test_category)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'User not logged in' in response.data)
        self.is_empty_database()

    def test_add_category_GET_with_existing_categorys_are_displayed(self):
        test_category1 = {
            "name": "teologia",
            }
        test_category2 = {
            "name": "kirkkohistoria",
            }
        self.app.post("/add_category", data=test_category1)
        self.app.post("/add_category", data=test_category2)

        response = self.app.get("/add_category")
        self.assertTrue(b'teologia' in response.data)
        self.assertTrue(b'kirkkohistoria' in response.data)
