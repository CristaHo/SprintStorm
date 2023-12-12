from unittest import TestCase
from sqlalchemy import text
from src.app import app

class TestDeleteCategory(TestCase):
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

        # check that category was created
        with app.app_context():
            from src.utils.database import db
            result = db.session.execute(text("SELECT name, user_id FROM category")).fetchone()
            if result:
                print(result)
                self.assertEqual(result[0], "teologia")
                self.assertEqual(result[1], 1)

        # user_id was saved to session = user logged in
        with self.app.session_transaction() as s:
            self.assertEqual(s["uid"], 1)

    def is_empty_database(self, boolean=True):
        with app.app_context():
            from src.utils.database import db
            result = db.session.execute(text("SELECT name, user_id FROM category")).fetchone()
            if boolean:
                self.assertEqual(result, None)
            else:
                self.assertNotEqual(result, None)

    def test_delete_category_with_correct_information_is_successful(self):
        test_delete = {
                "id": 1
                }
        response = self.app.post("/delete_category", data=test_delete)

        self.assertEqual(response.status_code, 302) # redirect
        self.is_empty_database()

    def test_delete_category_with_incorrect_id_doesnt_delete(self):
        test_delete = {
                "id": 219384
                }
        response = self.app.post("/delete_category", data=test_delete)

        self.assertEqual(response.status_code, 302) # redirect
        self.is_empty_database(False)

    def test_delete_with_missing_id_fails(self):
        test_delete = {
                "id": ""
                }
        response = self.app.post("/delete_category", data=test_delete)
        self.assertEqual(response.status_code, 302) # redirect
        self.is_empty_database(False)
